"""Index independent Perseus Morpheus candidate parses for AD word forms."""

import argparse
import os
import re
import sqlite3
import subprocess
import unicodedata
from collections import defaultdict
from pathlib import Path

from corpus_build import DB

REVISION = "ab6898ffed335fc6169fa02c9940657a9b5a78e0"
LETTERS = dict(zip("αβγδεζηθικλμνξοπρστυφχψω", "abgdezhqiklmncoprstufxyw", strict=True))
MARKS = {
    "\u0300": "/",
    "\u0301": "/",
    "\u0342": "=",
    "\u0313": ")",
    "\u0314": "(",
    "\u0345": "|",
    "\u0308": "+",
    "\u0304": "_",
    "\u0306": "^",
    "’": "'",
    "ʼ": "'",
}


def beta(surface):
    word = unicodedata.normalize("NFC", surface.lower().replace("ς", "σ"))
    if len(word) > 1 and word[0] in "᾿῾" and word[1] in "αεηιουωρ":
        mark = "\u0313" if word[0] == "᾿" else "\u0314"
        word = word[1] + mark + word[2:]
    text = unicodedata.normalize("NFD", word).translate(
        str.maketrans({"᾿": "’", "᾽": "’"})
    )
    return "".join(LETTERS.get(ch, MARKS.get(ch, ch)) for ch in text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    root = parser.parse_args().checkout.resolve()
    revision = subprocess.check_output(
        ["git", "-C", root, "rev-parse", "HEAD"], text=True
    ).strip()
    if revision != REVISION:
        raise ValueError("Unexpected Morpheus revision")
    with sqlite3.connect(DB, timeout=90) as db:
        db.executescript("""CREATE TABLE IF NOT EXISTS morpheus_form(surface TEXT PRIMARY KEY,beta TEXT NOT NULL,revision TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS morpheus_parse(beta TEXT,revision TEXT,analysis TEXT,PRIMARY KEY(beta,revision,analysis));""")
        forms = [
            (w, beta(w), revision)
            for (w,) in db.execute("SELECT DISTINCT surface FROM token")
        ]
        queries = sorted(
            {q for _, q, _ in forms if re.fullmatch(r"[a-z/+()=|'_^]+", q)}
        )
        found = defaultdict(set)
        for start in range(0, len(queries), 500):
            chunk = queries[start : start + 500]
            proc = subprocess.run(
                [root / "bin/cruncher", "-S"],
                input="\n".join(chunk) + "\n",
                text=True,
                env=dict(os.environ, MORPHLIB=str(root / "stemlib")),
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                timeout=180,
                check=True,
            )
            current = None
            valid = set(chunk)
            for line in proc.stdout.splitlines():
                if line in valid:
                    current = line
                elif line.startswith("<NL>") and current:
                    found[current].update(
                        " ".join(s.split()) for s in re.findall(r"<NL>(.*?)</NL>", line)
                    )
                elif line.strip():
                    raise ValueError(f"Unrecognized Morpheus output: {line[:80]}")
        controls = {
            "a)rxh=|": "fem dat sg",
            "genhqh/tw": "aor imperat pass 3rd sg",
            "sou/": "gen 2nd sg",
        }
        for word, expected in controls.items():
            if not any(expected in r for r in found[word]):
                raise ValueError(f"Control failed for {word}")
        db.execute("DELETE FROM morpheus_parse")
        db.execute("DELETE FROM morpheus_form")
        db.executemany("INSERT INTO morpheus_form VALUES(?,?,?)", forms)
        db.executemany(
            "INSERT INTO morpheus_parse VALUES(?,?,?)",
            (
                (q, revision, analysis)
                for q, readings in found.items()
                for analysis in sorted(readings)
            ),
        )
        print(
            f"{len(forms)} spellings indexed; {len(found)}/{len(queries)} Beta Code queries returned candidates"
        )


if __name__ == "__main__":
    main()
