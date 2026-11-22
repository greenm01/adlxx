"""Locate close parallel verses with different addresses using unique Greek phrases."""
import argparse
from collections import Counter, defaultdict
from pathlib import Path
import sqlite3

from corpus_alignment import key, pairs
from corpus_build import Athens, DB, REV


def anchors(words):
    return set(zip(words, words[1:], words[2:]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    athens = Athens(parser.parse_args().repo)
    db = sqlite3.connect(DB, timeout=90)
    books = defaultdict(dict)
    for ref, entries in athens.verses.items():
        books[ref.split()[0]][ref] = entries
    count = 0
    for book, sources in books.items():
        words = {ref: [key(e[0]) for e in rows] for ref, rows in sources.items()}
        locations = {}
        for ref, seq in words.items():
            for phrase in anchors(seq):
                if locations.setdefault(phrase, ref) != ref:
                    locations[phrase] = None
        refs = db.execute("""SELECT DISTINCT ref FROM token WHERE basis='needs local analysis'
            AND ref GLOB ?""",(book+" *",)).fetchall()
        for ref, in refs:
            rows = db.execute("SELECT position,surface,basis FROM token WHERE ref=? ORDER BY position",(ref,)).fetchall()
            target = [key(r[1]) for r in rows]
            votes = Counter(locations[f] for f in anchors(target) if locations.get(f))
            if not votes:
                continue
            best, n = votes.most_common(1)[0]
            if best == ref or n < 2 or (len(votes)>1 and n < 2 * votes.most_common(2)[1][1]):
                continue
            updates = []
            for i,j in pairs(target,words[best]):
                e = sources[best][j]
                if rows[i][2]=='needs local analysis' and all(e[1:4]):
                    updates.append((*e[1:4], *e[4:], REV, ref, rows[i][0]))
            if updates:
                with db:
                    count += db.executemany("""UPDATE token SET lemma=?,grammar=?,gloss=?,source_ref=?,
                        source_position=?,source_revision=?,basis='aligned parallel verse'
                        WHERE ref=? AND position=? AND basis='needs local analysis'""", updates).rowcount
    print(f"{count} aligned parallel verse readings")


if __name__ == "__main__":
    main()
