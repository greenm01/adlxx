"""Publish a verified, standalone local OT interlinear from the working database."""

from study_morphology import build_morphology
import argparse
import os
import sqlite3
import subprocess
import sys
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

from corpus_build import DB
from publisher_catalog import ROOT


def release(repo, destination):
    with closing(
        sqlite3.connect(DB.resolve().as_uri() + "?mode=ro", uri=True, timeout=90)
    ) as live:
        outstanding = live.execute(
            "SELECT count(*) FROM interlinear WHERE status='pending'"
        ).fetchone()[0]
        if outstanding:
            raise SystemExit(f"{outstanding:,} words still need readings.")
        with TemporaryDirectory(dir=destination.parent) as scratch:
            snapshot = Path(scratch) / "snapshot.sqlite"
            with closing(sqlite3.connect(snapshot)) as copy:
                live.backup(copy)
                copy.execute("PRAGMA journal_mode=DELETE")
                copy.executescript((ROOT / "data/lexical-tools.sql").read_text(encoding="utf-8"))
                build_morphology(copy)
                copy.commit()
            for script, args in [
                ("audit_corpus.py", ["--final"]),
                ("audit_readings.py", [str(repo)]),
            ]:
                subprocess.run(
                    [
                        sys.executable,
                        str(ROOT / script),
                        *args,
                        "--database",
                        str(snapshot),
                    ],
                    check=True,
                )
            os.replace(snapshot, destination)
    print(destination)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    args = parser.parse_args()
    release(args.repo, ROOT / "build/adlxx-ot.sqlite")
