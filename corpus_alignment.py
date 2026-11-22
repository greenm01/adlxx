"""Reuse unambiguously aligned words in close parallel verses."""
import argparse
from pathlib import Path
import sqlite3
import unicodedata

from athens_candidates import normalized
from corpus_build import Athens, DB, REV
from corpus_context import accent


def key(surface):
    word = normalized(surface)
    # Athens frequently uses a spacing breathing before an initial capital.
    if len(word) > 1 and word[0] in "’῾" and word[1] in "αεηιουωρ":
        mark = "\u0313" if word[0] == "’" else "\u0314"
        word = word[1] + mark + word[2:]
    return accent(unicodedata.normalize("NFC", word))


def lengths(left, right):
    """Length of a longest common subsequence for every prefix pair."""
    rows = [[0] * (len(right) + 1)]
    for a in left:
        prev = rows[-1]
        row = [0]
        for j, b in enumerate(right):
            row.append(prev[j] + 1 if a == b else max(prev[j + 1], row[-1]))
        rows.append(row)
    return rows


def pairs(left, right):
    forward = lengths(left, right)
    score = forward[-1][-1]
    if score < 5 or score < 0.8 * max(len(left), len(right)):
        return
    backward = lengths(left[::-1], right[::-1])
    for i, word in enumerate(left):
        prefix = forward[i]
        suffix = backward[len(left) - i - 1][::-1]
        if any(a + b == score for a, b in zip(prefix, suffix)):
            continue  # An equally good alignment skips this AD word entirely.
        possible = [
            j for j, b in enumerate(right)
            if b == word and prefix[j] + 1 + suffix[j + 1] == score
        ]
        if len(possible) == 1:
            yield i, possible[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    athens = Athens(parser.parse_args().repo)
    db = sqlite3.connect(DB, timeout=90)
    refs = db.execute("SELECT DISTINCT ref FROM token WHERE basis='needs local analysis'").fetchall()
    count = 0
    for (ref,) in refs:
        source = athens.verses.get(ref)
        if not source:
            continue
        rows = db.execute("SELECT position,surface,basis FROM token WHERE ref=? ORDER BY position", (ref,)).fetchall()
        updates = []
        for i, j in pairs([key(r[1]) for r in rows], [key(e[0]) for e in source]):
            e = source[j]
            if rows[i][2] == "needs local analysis" and all(e[1:4]):
                updates.append((*e[1:4], e[4], e[5], REV, ref, rows[i][0]))
        if updates:
            with db:
                count += db.executemany("""UPDATE token SET lemma=?,grammar=?,gloss=?,
                    source_ref=?,source_position=?,source_revision=?,basis='aligned verse'
                    WHERE ref=? AND position=? AND basis='needs local analysis'""", updates).rowcount
    print(f"{count} aligned verse readings")


if __name__ == "__main__":
    main()
