"""Incrementally import AD chapters and select Athens candidates with provenance."""

import argparse
import csv
from collections import defaultdict, Counter
from datetime import date
from pathlib import Path
import sqlite3
import subprocess
import re

from athens_candidates import normalized, windows
from interlinear import TOKEN
from publisher_catalog import CACHE, ROOT
from publisher_text import addressed_verses

REV = "3ffd871904268583043ebf1886e700486504cc84"
DB = ROOT / "build/corpus.sqlite"
WORD = re.compile(r"[᾿῾]?" + TOKEN.pattern)
SCHEMA = """
CREATE TABLE IF NOT EXISTS source_page(book TEXT,chapter TEXT,url TEXT,sha256 TEXT,status TEXT,reason TEXT,PRIMARY KEY(book,chapter));
CREATE TABLE IF NOT EXISTS verse(ref TEXT PRIMARY KEY,book TEXT,chapter TEXT,label TEXT,greek TEXT);
CREATE TABLE IF NOT EXISTS token(ref TEXT,position INTEGER,surface TEXT,lemma TEXT,grammar TEXT,gloss TEXT,basis TEXT,source_ref TEXT,source_position INTEGER,source_revision TEXT,PRIMARY KEY(ref,position));
CREATE INDEX IF NOT EXISTS token_review ON token(basis,ref);
"""


class Athens:
    def __init__(self, repo):
        # Read the committed edition once, without consuming the checkout's edits.
        import tarfile

        self.verses = defaultdict(list)
        self.forms = {}
        self.conflicting = set()
        with subprocess.Popen(
            ["git", "-C", str(repo), "archive", REV, "interlinear"],
            stdout=subprocess.PIPE,
        ) as proc:
            with tarfile.open(fileobj=proc.stdout, mode="r|") as archive:
                for item in archive:
                    if not re.fullmatch(r"interlinear/[A-Z0-9]+-\d+\.tsv", item.name):
                        continue
                    rows = archive.extractfile(item).read().decode().splitlines()
                    for r in csv.DictReader(rows, delimiter="\t"):
                        if r["preference"] != "1" or r["occurrence"] != "1":
                            continue
                        ref = r["ref"]
                        pos = int(r["position"])
                        key = normalized(r["surface"])
                        entry = (key, r["lemma"], r["grammar"], r["english"], ref, pos)
                        self.verses[ref].append(entry)
                        if key not in self.forms:
                            self.forms[key] = entry
                        elif self.forms[key][1:4] != entry[1:4]:
                            self.conflicting.add(key)
            if proc.wait():
                raise RuntimeError("Athens archive failed")

    def readings(self, ref, words):
        source = self.verses.get(ref, [])
        left = [normalized(w) for w in words]
        right = [e[0] for e in source]
        context = windows(left)
        counts = Counter(context)
        matches = defaultdict(list)
        for j, window in enumerate(windows(right)):
            matches[window].append(j)
        for i, (word, key, window) in enumerate(zip(words, left, context), 1):
            e = None
            if left == right:
                basis = "same verse"
                e = source[i - 1]
            elif counts[window] == 1 and len(matches[window]) == 1:
                basis = "unique context"
                e = source[matches[window][0]]
            elif key in self.forms and key not in self.conflicting:
                basis = "consistent form"
                e = self.forms[key]
            else:
                basis = "needs local analysis"
            if e and all(e[1:4]):
                yield (ref, i, word, *e[1:4], basis, *e[4:], REV)
            else:
                yield (
                    ref,
                    i,
                    word,
                    None,
                    None,
                    None,
                    "needs local analysis",
                    None,
                    None,
                    None,
                )


def import_page(db, ath, row, path):
    import hashlib, gzip

    book, ch, url = row["book"], row["chapter_label"], row["url"]
    checksum = hashlib.sha256(gzip.decompress(path.read_bytes())).hexdigest()
    prev = db.execute(
        "SELECT sha256,status FROM source_page WHERE book=? AND chapter=?", (book, ch)
    ).fetchone()
    if prev == (checksum, "imported"):
        return
    try:
        verses = addressed_verses(path, book, ch)
        if not all(WORD.search(s) for _, s in verses):
            raise ValueError("Empty token sequence")
    except ValueError as exc:
        if prev and prev[1] == "imported":
            raise
        with db:
            db.execute(
                "INSERT OR REPLACE INTO source_page VALUES(?,?,?,?,?,?)",
                (book, ch, url, checksum, "inspect", str(exc)),
            )
        return
    with db:
        db.execute(
            "DELETE FROM token WHERE ref IN (SELECT ref FROM verse WHERE book=? AND chapter=?)",
            (book, ch),
        )
        db.execute("DELETE FROM verse WHERE book=? AND chapter=?", (book, ch))
        for ref, greek in verses:
            label = ref.split(":", 1)[1]
            words = WORD.findall(greek)
            db.execute(
                "INSERT INTO verse VALUES(?,?,?,?,?)", (ref, book, ch, label, greek)
            )
            db.executemany(
                "INSERT INTO token VALUES(?,?,?,?,?,?,?,?,?,?)",
                ath.readings(ref, words),
            )
        db.execute(
            "INSERT OR REPLACE INTO source_page VALUES(?,?,?,?,?,?)",
            (book, ch, url, checksum, "imported", ""),
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("athens_repo", type=Path)
    parser.add_argument(
        "--follow",
        action="store_true",
        help="wait for catalogued download pages to arrive",
    )
    args = parser.parse_args()
    import time

    with (ROOT / "data/publisher-chapters.tsv").open() as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ath = Athens(args.athens_repo)
    with sqlite3.connect(DB, timeout=60) as db:
        db.execute("PRAGMA journal_mode=WAL")
        db.executescript(SCHEMA)
        while rows:
            waiting = []
            for row in rows:
                p = CACHE / row["book"] / row["cache_file"]
                if p.exists():
                    import_page(db, ath, row, p)
                else:
                    waiting.append(row)
            rows = waiting
            print(
                db.execute(
                    "SELECT status,count(*) FROM source_page GROUP BY status"
                ).fetchall(),
                "awaiting downloads",
                len(rows),
                flush=True,
            )
            if not args.follow or not rows:
                break
            time.sleep(8)


if __name__ == "__main__":
    main()
