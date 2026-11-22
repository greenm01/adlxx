"""Recover runs of five or more shared words across nearby chapter and verse divisions."""

import argparse
from collections import defaultdict
from pathlib import Path
import sqlite3

from corpus_build import Athens, DB, REV
from corpus_context import accent
from athens_candidates import normalized


def unique_runs(words, width=5):
    result = {}
    for i in range(len(words) - width + 1):
        key = tuple(words[i : i + width])
        result[key] = None if key in result else i
    return result


def chapter(db, book, ch, source):
    # Page order matters because AD sometimes presents the remaining verses
    # separately at the end. Never sort verse labels lexicographically.
    rows = db.execute(
        """SELECT t.ref,t.position,t.surface,t.basis FROM verse v JOIN token t USING(ref)
        WHERE v.book=? AND v.chapter=? ORDER BY v.rowid,t.position""",
        (book, ch),
    ).fetchall()
    if not any(r[3] == "needs local analysis" for r in rows):
        return 0
    ad = unique_runs([accent(normalized(r[2])) for r in rows])
    greek = unique_runs([accent(r[0]) for r in source])
    matches = {}
    for key, i in ad.items():
        j = greek.get(key)
        if i is None or j is None:
            continue
        for pos in range(5):
            a = i + pos
            b = j + pos
            if rows[a][3] != "needs local analysis":
                continue
            if a in matches and matches[a] != b:
                matches[a] = None
            else:
                matches[a] = b
    updates = []
    for i, j in matches.items():
        if j is None:
            continue
        e = source[j]
        if all(e[1:4]):
            updates.append((*e[1:4], e[4], e[5], REV, rows[i][0], rows[i][1]))
    with db:
        return db.executemany(
            """UPDATE token SET lemma=?,grammar=?,gloss=?,basis='parallel passage',
        source_ref=?,source_position=?,source_revision=?
        WHERE ref=? AND position=? AND basis='needs local analysis'""",
            updates,
        ).rowcount


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("repo", type=Path)
    args = cli.parse_args()
    by_chapter = defaultdict(list)
    for ref, entries in Athens(args.repo).verses.items():
        b, c = ref.split(":")[0].split()
        by_chapter[b, int(c)].extend(entries)
    with sqlite3.connect(DB, timeout=90) as db:
        total = 0
        for b, c in db.execute("SELECT DISTINCT book,chapter FROM verse").fetchall():
            n = int(c)
            source = [e for k in (n - 1, n, n + 1) for e in by_chapter.get((b, k), ())]
            total += chapter(db, b, c, source)
        print("Added", total, "parallel passage drafts")


if __name__ == "__main__":
    main()
