"""Locate homologous shorter Greek phrases in parallel verses with wider differences."""

import argparse
import sqlite3
from pathlib import Path

from corpus_alignment import key, pairs
from corpus_build import DB, REV, Athens


def correspondences(left, right):
    def triples(words):
        positions = {}
        for i in range(len(words) - 2):
            phrase = tuple(words[i : i + 3])
            positions[phrase] = None if phrase in positions else i
        return positions

    targets = triples(left)
    sources = triples(right)
    matches = {}
    for phrase, i in targets.items():
        j = sources.get(phrase)
        if i is None or j is None:
            continue
        for offset in range(3):
            a, b = i + offset, j + offset
            if matches.setdefault(a, b) != b:
                matches[a] = None
    # A short exact pair at a clause boundary can also be anchored by an
    # independently matched word on its other side in the same parallel verse.
    stable = dict(pairs(left, right, minimum_fraction=0.45))
    for i, j in stable.items():
        near_before = any(
            0 < j - stable[k] <= 4 for k in range(i - 4, i) if k in stable
        )
        near_after = any(
            0 < stable[k] - j <= 4 for k in range(i + 1, i + 5) if k in stable
        )
        anchored = (stable.get(i - 1) == j - 1 and near_after) or (
            stable.get(i + 1) == j + 1 and near_before
        )
        if anchored and matches.setdefault(i, j) != j:
            matches[i] = None
    return [(i, j) for i, j in matches.items() if j is not None]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    athens = Athens(parser.parse_args().repo)
    db = sqlite3.connect(DB, timeout=90)
    refs = db.execute(
        "SELECT DISTINCT ref FROM token WHERE basis='needs local analysis'"
    ).fetchall()
    count = 0
    consistent = {}
    for entries in athens.verses.values():
        for e in entries:
            form = key(e[0])
            other = consistent.setdefault(form, e)
            if other is None or other[1:4] != e[1:4] or not all(e[1:4]):
                consistent[form] = None
    forms = 0
    for (ref,) in refs:
        source = athens.verses.get(ref)
        source = source or []
        rows = db.execute(
            "SELECT position,surface,basis FROM token WHERE ref=? ORDER BY position",
            (ref,),
        ).fetchall()
        updates = []
        for i, j in correspondences(
            [key(r[1]) for r in rows], [key(e[0]) for e in source]
        ):
            e = source[j]
            if rows[i][2] == "needs local analysis" and all(e[1:4]):
                updates.append((*e[1:4], *e[4:], REV, ref, rows[i][0]))
        if updates:
            with db:
                count += db.executemany(
                    """UPDATE token SET lemma=?,grammar=?,gloss=?,source_ref=?,
                    source_position=?,source_revision=?,basis='parallel phrase'
                    WHERE ref=? AND position=? AND basis='needs local analysis'""",
                    updates,
                ).rowcount
        updates = []
        for pos, surface, basis in rows:
            e = consistent.get(key(surface))
            if e and basis == "needs local analysis":
                updates.append((*e[1:4], *e[4:], REV, ref, pos))
        if updates:
            with db:
                forms += db.executemany(
                    """UPDATE token SET lemma=?,grammar=?,gloss=?,source_ref=?,
                    source_position=?,source_revision=?,basis='normalized consistent form'
                    WHERE ref=? AND position=? AND basis='needs local analysis'""",
                    updates,
                ).rowcount
    print(f"{count} parallel phrase readings, {forms} consistent normalized forms")


if __name__ == "__main__":
    main()
