"""Find additional Athens draft analyses using three consecutive Greek words."""

from collections import defaultdict
from pathlib import Path
import argparse
import sqlite3
import unicodedata

from corpus_build import Athens, DB, REV
from athens_candidates import normalized


def accent(word):
    # A grave frequently becomes an acute before punctuation. Keep breathings,
    # iota subscript, and all other lexical accents distinct.
    return unicodedata.normalize(
        "NFC", unicodedata.normalize("NFD", word).replace("\u0300", "\u0301")
    )


def triples(entries):
    for i in range(1, len(entries) - 1):
        yield tuple(entries[i - 1 : i + 2]), i


def index(ath):
    exact = {}
    conflicts = set()
    for entries in ath.verses.values():
        words = [accent(e[0]) for e in entries]
        for key, i in triples(words):
            entry = entries[i]
            if not all(entry[1:4]):
                continue
            previous = exact.setdefault(key, entry)
            if previous[1:4] != entry[1:4]:
                conflicts.add(key)
    for key in conflicts:
        del exact[key]
    return exact


def enrich(db, contexts):
    refs = [
        r[0]
        for r in db.execute(
            "SELECT DISTINCT ref FROM token WHERE basis='needs local analysis'"
        )
    ]
    total = 0
    for ref in refs:
        rows = db.execute(
            "SELECT position,surface,basis FROM token WHERE ref=? ORDER BY position",
            (ref,),
        ).fetchall()
        updates = []
        for key, i in triples([accent(normalized(row[1])) for row in rows]):
            if rows[i][2] != "needs local analysis":
                continue
            e = contexts.get(key)
            if e:
                updates.append((*e[1:4], e[4], e[5], REV, ref, rows[i][0]))
        if updates:
            with db:
                result = db.executemany(
                    """UPDATE token SET lemma=?,grammar=?,gloss=?,basis='corpus context',source_ref=?,source_position=?,source_revision=?
                    WHERE ref=? AND position=? AND basis='needs local analysis'""",
                    updates,
                )
                total += result.rowcount
    return total


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("repo", type=Path)
    args = cli.parse_args()
    contexts = index(Athens(args.repo))
    with sqlite3.connect(DB, timeout=90) as db:
        print("Added", enrich(db, contexts), "Athens context drafts")


if __name__ == "__main__":
    main()
