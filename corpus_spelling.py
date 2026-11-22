"""Compare accent variants in aligned Greek verses while preserving AD spelling."""

import argparse
import sqlite3
import unicodedata
from collections import defaultdict
from pathlib import Path

from corpus_alignment import key, pairs
from corpus_build import DB, REV, Athens


def letters(form):
    # Retain breathing, diaeresis, iota and elision. Ignore only pitch accents.
    return unicodedata.normalize("NFD", form).translate(
        {0x300: None, 0x301: None, 0x342: None}
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    athens = Athens(parser.parse_args().repo)
    attested = defaultdict(set)
    family = defaultdict(set)
    for entries in athens.verses.values():
        for e in entries:
            form = key(e[0])
            attested[form].add(e[1:4])
            family[letters(form)].add(e[1:4])
    db = sqlite3.connect(DB, timeout=90)
    refs = db.execute(
        "SELECT DISTINCT ref FROM token WHERE basis='needs local analysis'"
    ).fetchall()
    count = 0
    for (ref,) in refs:
        source = athens.verses.get(ref)
        if not source:
            continue
        rows = db.execute(
            "SELECT position,surface,basis FROM token WHERE ref=? ORDER BY position",
            (ref,),
        ).fetchall()
        left = [key(r[1]) for r in rows]
        right = [key(e[0]) for e in source]
        matches = dict(
            pairs(
                [letters(f) for f in left],
                [letters(f) for f in right],
                minimum_fraction=0.55,
            )
        )
        updates = []
        for i, j in matches.items():
            if rows[i][2] != "needs local analysis" or left[i] == right[j]:
                continue
            before = (
                i > 0
                and j > 0
                and matches.get(i - 1) == j - 1
                and left[i - 1] == right[j - 1]
            )
            after = (
                i + 1 < len(left)
                and j + 1 < len(right)
                and matches.get(i + 1) == j + 1
                and left[i + 1] == right[j + 1]
            )
            if not (before and after):
                continue
            e = source[j]
            possibilities = attested.get(left[i])
            if not all(e[1:4]):
                continue
            if possibilities:
                if e[1:4] not in possibilities:
                    continue
            elif family[letters(left[i])] != {e[1:4]}:
                continue
            updates.append((*e[1:4], *e[4:], REV, ref, rows[i][0]))
        if updates:
            with db:
                count += db.executemany(
                    """UPDATE token SET lemma=?,grammar=?,gloss=?,source_ref=?,
                    source_position=?,source_revision=?,basis='aligned accent variant'
                    WHERE ref=? AND position=? AND basis='needs local analysis'""",
                    updates,
                ).rowcount
    print(f"{count} aligned accent variants")


if __name__ == "__main__":
    main()
