"""Supervise two local inference workers through release of the completed OT."""

import argparse
import fcntl
import re
import sqlite3
import subprocess
import sys
import time
from contextlib import closing
from pathlib import Path

from corpus_build import DB
from publisher_catalog import ROOT
from release_corpus import release


def live_workers():
    listing = subprocess.check_output(["ps", "-Ao", "pid=,command="], text=True)
    live = set()
    for line in listing.splitlines():
        match = re.fullmatch(
            r"\s*(\d+)\s+\S*[Pp]ython\S*\s+(?:\S*/)?corpus_local\.py\s+(crunch|localhost)",
            line,
        )
        if not match:
            continue
        cwd = subprocess.run(
            ["lsof", "-a", "-p", match[1], "-d", "cwd", "-Fn"],
            check=False,
            capture_output=True,
            text=True,
        )
        if "n" + str(ROOT) in cwd.stdout.splitlines():
            live.add(match[2])
    return live


def supervise(repo):
    with (ROOT / "build/supervisor.lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        children = {}
        while True:
            with closing(sqlite3.connect(DB, timeout=90)) as db:
                pending = db.execute(
                    "SELECT count(*) FROM token WHERE basis='needs local analysis'"
                ).fetchone()[0]
                if (
                    not pending
                    or not db.execute(
                        "SELECT 1 FROM interlinear WHERE status='pending' LIMIT 1"
                    ).fetchone()
                ):
                    break
                available = db.execute(
                    """SELECT 1 FROM token t WHERE basis='needs local analysis'
                    AND NOT EXISTS (SELECT 1 FROM lease l WHERE l.ref=t.ref AND l.expires>?)
                    LIMIT 1""",
                    (int(time.time()),),
                ).fetchone()
            if available:
                live = live_workers()
                for host in ("localhost", "crunch"):
                    child = children.get(host)
                    if host in live or (child and child.poll() is None):
                        continue
                    with (ROOT / f"build/finish-{host}.log").open("a") as out:
                        children[host] = subprocess.Popen(
                            [sys.executable, "corpus_local.py", host],
                            cwd=ROOT,
                            stdout=out,
                            stderr=subprocess.STDOUT,
                        )
                    print(f"Started {host} worker {children[host].pid}", flush=True)
            time.sleep(60)
        release(repo, ROOT / "build/adlxx-ot.sqlite")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    supervise(parser.parse_args().repo.resolve())
