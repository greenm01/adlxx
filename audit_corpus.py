"""Audit the corpus against cached publisher pages and report unresolved coverage."""

import argparse
from collections import Counter
import csv
import gzip
import hashlib
import json
from pathlib import Path
import sqlite3
from corpus_build import DB, WORD
from publisher_catalog import ROOT, CACHE
from publisher_text import addressed_verses


def audit(db):
    with (ROOT / "data/publisher-chapters.tsv").open() as f:
        catalog = list(csv.DictReader(f, delimiter="\t"))
    pages = {
        (b, c): (url, h, status)
        for b, c, url, h, status in db.execute(
            "SELECT book,chapter,url,sha256,status FROM source_page"
        )
    }
    problems = []
    counts = Counter()
    book_counts = Counter()
    for r in catalog:
        key = r["book"], r["chapter_label"]
        path = CACHE / key[0] / r["cache_file"]
        if not path.exists():
            counts["pages awaiting download"] += 1
            continue
        if key not in pages:
            counts["pages awaiting import"] += 1
            continue
        url, h, status = pages[key]
        if (
            h != hashlib.sha256(gzip.decompress(path.read_bytes())).hexdigest()
            or url != r["url"]
        ):
            problems.append(f"Source fingerprint mismatch: {key}")
            continue
        if status != "imported":
            counts["pages needing inspection"] += 1
            continue
        try:
            expected = addressed_verses(path, *key)
        except ValueError as e:
            problems.append(f"Source parser: {key}: {e}")
            continue
        actual = db.execute(
            "SELECT ref,greek FROM verse WHERE book=? AND chapter=? ORDER BY rowid", key
        ).fetchall()
        if expected != actual:
            problems.append(f"Verse text or order differs from source: {key}")
            continue
        for ref, text in expected:
            tokens = WORD.findall(text)
            if (
                list(enumerate(tokens, 1))
                != db.execute(
                    "SELECT position,surface FROM token WHERE ref=? ORDER BY position",
                    (ref,),
                ).fetchall()
            ):
                problems.append("Token sequence differs: " + ref)
            counts["verified verse records"] += 1
            counts["verified source tokens"] += len(tokens)
        counts["verified source pages"] += 1
        book_counts[key[0]] += 1
    counts["catalog books"] = len({r["book"] for r in catalog})
    counts["catalog pages"] = len(catalog)
    counts["books with all source pages verified"] = sum(
        book_counts[b] == n for b, n in Counter(r["book"] for r in catalog).items()
    )
    unexpected = set(pages) - {(r["book"], r["chapter_label"]) for r in catalog}
    if unexpected:
        problems.append(f"Unexpected page keys: {sorted(unexpected)}")
    counts["database tokens"] = db.execute("SELECT count(*) FROM token").fetchone()[0]
    counts.update(
        {
            "reading " + s: n
            for s, n in db.execute(
                "SELECT status,count(*) FROM interlinear GROUP BY status"
            )
        }
    )
    if counts["database tokens"] != sum(
        v for k, v in counts.items() if k.startswith("reading ")
    ):
        problems.append("Reader view loses or duplicates tokens")
    invalid = db.execute("""SELECT count(*) FROM interlinear WHERE status<>'pending' AND
    (coalesce(trim(lemma),'')='' OR coalesce(trim(grammar),'')='' OR coalesce(trim(gloss),'')='')""").fetchone()[
        0
    ]
    if invalid:
        problems.append(f"{invalid} incomplete readings labeled ready")
    if db.execute("PRAGMA quick_check").fetchone() != ("ok",):
        problems.append("SQLite quick_check failed")
    return dict(counts), problems


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument(
        "--final",
        action="store_true",
        help="also require complete chapter and interlinear coverage",
    )
    cli.add_argument("--database", type=Path, default=DB)
    args = cli.parse_args()
    with sqlite3.connect(
        args.database.resolve().as_uri() + "?mode=ro", uri=True, timeout=90
    ) as db:
        db.execute("BEGIN")
        counts, problems = audit(db)
    print(
        json.dumps(
            {"coverage": counts, "problems": problems}, ensure_ascii=False, indent=2
        )
    )
    complete = (
        counts["verified source pages"] == counts["catalog pages"]
        and counts["verified source tokens"] == counts["database tokens"]
        and not counts.get("reading pending")
    )
    raise SystemExit(int(bool(problems) or (args.final and not complete)))
