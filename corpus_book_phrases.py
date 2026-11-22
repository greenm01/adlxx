"""Recover unique four-word parallels within a book, including shifted chapters."""

import argparse
import sqlite3
from collections import defaultdict
from pathlib import Path

from corpus_alignment import key
from corpus_build import DB, REV, Athens


def index(verses):
    result = {}
    for ref, words in verses.items():
        for i in range(len(words) - 3):
            phrase = tuple(words[i : i + 4])
            result[phrase] = None if phrase in result else (ref, i)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    sources = defaultdict(dict)
    for ref, rows in Athens(parser.parse_args().repo).verses.items():
        sources[ref.split()[0]][ref] = rows
    db = sqlite3.connect(DB, timeout=90)
    count = 0
    for book, verses in sources.items():
        greek = index({r: [key(e[0]) for e in v] for r, v in verses.items()})
        wanted = set()
        words = defaultdict(list)
        for ref, pos, surface, basis in db.execute(
            "SELECT ref,position,surface,basis FROM token WHERE ref GLOB ? ORDER BY ref,position",
            (book + " *",),
        ):
            words[ref].append(key(surface))
            if basis == "needs local analysis":
                wanted.add((ref, pos))
        candidates = defaultdict(set)
        for phrase, address in index(words).items():
            src = greek.get(phrase)
            if address and src:
                ref, i = address
                s, j = src
                for offset in range(4):
                    token = (ref, i + offset + 1)
                    if token in wanted:
                        candidates[token].add((s, j + offset))
        changes = []
        for (ref, pos), options in candidates.items():
            if len(options) == 1:
                s, j = options.pop()
                e = verses[s][j]
                if all(e[1:4]):
                    changes.append((*e[1:4], *e[4:], REV, ref, pos))
        with db:
            count += db.executemany(
                """UPDATE token SET lemma=?,grammar=?,gloss=?,source_ref=?,
                source_position=?,source_revision=?,basis='unique book phrase'
                WHERE ref=? AND position=? AND basis='needs local analysis'""",
                changes,
            ).rowcount
    print(f"{count} readings from unique book phrases")


if __name__ == "__main__":
    main()
