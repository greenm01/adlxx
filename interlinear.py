"""Build a local, two-model Greek interlinear from recorded publisher verses."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import subprocess
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
TOKEN = re.compile(r"[^\W\d_]+(?:[\u0300-\u036f]+[^\W\d_]*)*(?:[᾿᾽’ʼ'])?", re.UNICODE)


DRAFT_LIMITS = {"lemma": 55, "grammar": 150, "gloss": 60}


def valid_corpus_draft(row):
    for name, limit in DRAFT_LIMITS.items():
        value = row[name]
        if not isinstance(value, str) or not 0 < len(value.strip()) <= limit:
            return False
        if any(c in value for c in "\n\r\t"):
            return False
    return not any(
        phrase in row["gloss"].lower()
        for phrase in (
            "literal english translation",
            "let's assume",
            "as an ai",
            "do not repeat",
        )
    )


def analyze(
    host, model, verse, words, cache, positions=None, hints=None, bounded=False
):
    numbered = list(
        enumerate(words, 1) if positions is None else zip(positions, words, strict=True)
    )
    message = dict(
        verse=verse,
        tokens=[dict(position=i, surface=w) for i, w in numbered],
    )
    # Binding fields to numbered source tokens avoids relying on the model to
    # retype polytonic Greek or count repeated words correctly.
    attributes = {
        "lemma": {"type": "string", "pattern": "^[Ͱ-Ͽἀ-῿].*"},
        "grammar": {"type": "string", "minLength": 1},
        "gloss": {"type": "string", "minLength": 1},
    }
    if bounded:
        for name, limit in DRAFT_LIMITS.items():
            attributes[name]["maxLength"] = limit
    fields = {
        f"{i} {word}": {
            "type": "object",
            "properties": attributes,
            "required": list(attributes),
            "additionalProperties": False,
        }
        for i, word in numbered
    }
    prompt = (
        "For each numbered token supply lemma (Greek dictionary form written in Greek letters), "
        "grammar (contextual parsing in English), and gloss (literal English translation of this "
        "single token, not grammar or a definition). Example: ἐν -> ἐν / preposition with dative / in. "
        "Gloss every article as the, even where English idiom omits it. Report case, number and gender of nominals and applicable verbal features. "
        "Do not repeat neighboring articles or prepositions in a gloss.\n"
    )
    if bounded:
        prompt += "Use a single dictionary headword, concise grammatical labels, and a short English gloss. Return each field on one line.\n"
    if hints:
        message["morpheus_candidates"] = hints
        prompt += (
            "Morpheus candidates are independent Ancient Greek parser analyses in Beta Code. "
            "Select the lemma and parse that fit the sentence when one is appropriate. "
            "Convert Beta Code lemmas to Greek and abbreviations to English. "
            "For example fem dat sg means feminine dative singular, and aor imperat pass "
            "3rd sg means aorist passive imperative, third person singular. "
            "The parser may omit a Biblical Greek reading. Translate the word in its verse.\n"
        )
    payload = json.dumps(
        dict(
            model=model,
            prompt=prompt + json.dumps(message, ensure_ascii=False),
            stream=False,
            format={
                "type": "object",
                "properties": fields,
                "required": list(fields),
                "additionalProperties": False,
            },
            options=dict(
                temperature=0,
                seed=42,
                num_ctx=8192,
                **({"num_predict": 120 + 100 * len(numbered)} if bounded else {}),
            ),
            **({"think": False} if model.startswith("qwen") else {}),
        )
    ).encode()
    key = hashlib.sha256(host.encode() + payload).hexdigest()
    path = cache / (key + ".json")
    if path.exists():
        answer = json.loads(path.read_text())
    else:
        url = "http://localhost:11434/api/generate"
        if host == "localhost":
            with urlopen(
                Request(url, payload, {"Content-Type": "application/json"}), timeout=300
            ) as f:
                answer = json.load(f)
        else:
            raw = subprocess.check_output(
                [
                    "ssh",
                    host,
                    'curl -fsS --max-time 300 -H "Content-Type: application/json" --data-binary @- '
                    + url,
                ],
                input=payload,
                timeout=315,
            )
            answer = json.loads(raw)
    parsed = json.loads(answer["response"])
    if set(parsed) != set(fields):
        raise ValueError(f"{host}: incomplete token coverage")
    rows = [
        dict(position=i, surface=w, **parsed[k])
        for (i, w), k in zip(numbered, fields, strict=True)
    ]
    for r in rows:
        if not all(
            isinstance(r[k], str) and r[k].strip()
            for k in ("lemma", "grammar", "gloss")
        ):
            raise ValueError(f"{host}: incomplete analysis for {r['surface']}")
        if bounded and not valid_corpus_draft(r):
            raise ValueError(f"{host}: invalid interlinear fields for {r['surface']}")
    path.write_text(json.dumps(answer, ensure_ascii=False))
    return rows


def load_reviews(db):
    db.execute("DROP VIEW IF EXISTS interlinear")
    db.execute("DROP TABLE IF EXISTS review")
    db.execute(
        "CREATE TABLE review(ref TEXT,position INTEGER,surface TEXT,lemma TEXT,grammar TEXT,gloss TEXT,note TEXT,PRIMARY KEY(ref,position))"
    )
    with (ROOT / "data/reviewed.tsv").open() as stream:
        for r in csv.DictReader(stream, delimiter="\t"):
            key = (r["ref"], int(r["position"]))
            match = db.execute(
                "SELECT surface FROM token WHERE ref=? AND position=?", key
            ).fetchone()
            if match != (r["surface"],):
                raise ValueError(f"Review no longer matches source token at {key}")
            db.execute(
                "INSERT INTO review VALUES(?,?,?,?,?,?,?)",
                (*key, r["surface"], r["lemma"], r["grammar"], r["gloss"], r["note"]),
            )
    db.execute("""CREATE VIEW interlinear AS
        SELECT t.ref,t.position,t.surface,
               coalesce(r.lemma,a.lemma) AS lemma,coalesce(r.grammar,a.grammar) AS grammar,
               coalesce(r.gloss,a.gloss) AS gloss,
               CASE WHEN r.ref IS NULL THEN 'draft' ELSE 'reviewed' END AS status
        FROM token t JOIN analysis a USING(ref,position) LEFT JOIN review r USING(ref,position)
        WHERE a.role='draft'""")


def save_snapshot(db):
    """Save both independent readings with their source context for offline builds."""
    target = ROOT / "data/analyses.tsv"
    query = """SELECT v.ref,v.greek,t.position,t.surface,a.role,a.host,a.model,a.lemma,a.grammar,a.gloss
               FROM verse v JOIN token t USING(ref) JOIN analysis a USING(ref,position)
               ORDER BY v.rowid,t.position,a.role"""
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(
        "w", dir=target.parent, delete=False, encoding="utf-8"
    ) as stream:
        temp = Path(stream.name)
        try:
            writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
            writer.writerow(
                (
                    "ref",
                    "context_sha256",
                    "position",
                    "surface",
                    "role",
                    "host",
                    "model",
                    "lemma",
                    "grammar",
                    "gloss",
                )
            )
            for ref, greek, *rest in db.execute(query):
                writer.writerow(
                    (ref, hashlib.sha256(greek.encode()).hexdigest(), *rest)
                )
        except BaseException:
            temp.unlink(missing_ok=True)
            raise
    temp.replace(target)


def read_snapshot(verses, engines):
    """Validate the saved readings against both the tokens and their verse context."""
    contexts = {
        v["ref"]: (
            hashlib.sha256(v["greek"].encode()).hexdigest(),
            TOKEN.findall(v["greek"]),
        )
        for v in verses
    }
    expected = {
        (ref, role): len(words)
        for ref, (_, words) in contexts.items()
        for role, _, _ in engines
    }
    sources = {role: (host, model) for role, host, model in engines}
    saved = {}
    with (ROOT / "data/analyses.tsv").open() as f:
        for r in csv.DictReader(f, delimiter="\t"):
            key = r["ref"], r["role"]
            position = int(r["position"])
            group = saved.setdefault(key, {})
            checksum, words = contexts[r["ref"]]
            if (
                key not in expected
                or not 1 <= position <= len(words)
                or position in group
                or r["context_sha256"] != checksum
                or r["surface"] != words[position - 1]
                or sources[r["role"]] != (r["host"], r["model"])
                or not all(r[field].strip() for field in ("lemma", "grammar", "gloss"))
            ):
                raise ValueError(f"Invalid saved reading at {key}, token {position}")
            group[position] = dict(r, position=position)
    if expected != {key: len(group) for key, group in saved.items()}:
        raise ValueError("Snapshot coverage differs from source")
    return saved


def main():
    from concurrent.futures import ThreadPoolExecutor

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-host", default="localhost")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--save-snapshot",
        action="store_true",
        help="save successful model readings for offline use",
    )
    mode.add_argument(
        "--from-snapshot",
        action="store_true",
        help="load saved model readings without inference",
    )
    args = parser.parse_args()
    build = ROOT / "build"
    cache = build / "model-cache"
    cache.mkdir(parents=True, exist_ok=True)
    engines = [
        ("draft", "crunch", "qwen3.5:9b"),
        ("second reading", args.review_host, "gemma3:12b"),
    ]
    with (ROOT / "data/verses.tsv").open() as f:
        verses = list(csv.DictReader(f, delimiter="\t"))
    saved = read_snapshot(verses, engines) if args.from_snapshot else {}
    db = sqlite3.connect(build / "adlxx.sqlite")
    try:
        db.execute("BEGIN")
        for table in ("analysis", "token", "verse"):
            db.execute(f"DROP TABLE IF EXISTS {table}")
        db.execute(
            "CREATE TABLE verse(ref TEXT PRIMARY KEY,url TEXT,retrieved TEXT,greek TEXT)"
        )
        db.execute(
            "CREATE TABLE token(ref TEXT,position INTEGER,surface TEXT,PRIMARY KEY(ref,position))"
        )
        db.execute(
            "CREATE TABLE analysis(ref TEXT,position INTEGER,role TEXT,host TEXT,model TEXT,lemma TEXT,grammar TEXT,gloss TEXT,status TEXT,PRIMARY KEY(ref,position,role))"
        )
        with ThreadPoolExecutor(max_workers=2) as pool:
            for v in verses:
                ref = v["ref"]
                print(ref, flush=True)
                words = TOKEN.findall(v["greek"])
                if not words:
                    raise ValueError(f"Empty verse: {ref}")
                db.execute(
                    "INSERT INTO verse VALUES(?,?,?,?)",
                    (ref, v["url"], v["retrieved"], v["greek"]),
                )
                db.executemany(
                    "INSERT INTO token VALUES(?,?,?)",
                    [(ref, i, w) for i, w in enumerate(words, 1)],
                )
                jobs = (
                    []
                    if args.from_snapshot
                    else [
                        pool.submit(analyze, host, model, v["greek"], words, cache)
                        for role, host, model in engines
                    ]
                )
                for index, (role, host, model) in enumerate(engines):
                    rows = (
                        saved[ref, role].values()
                        if args.from_snapshot
                        else jobs[index].result()
                    )
                    for r in rows:
                        db.execute(
                            "INSERT INTO analysis VALUES(?,?,?,?,?,?,?,?,?)",
                            (
                                ref,
                                r["position"],
                                role,
                                host,
                                model,
                                r["lemma"],
                                r["grammar"],
                                r["gloss"],
                                "draft",
                            ),
                        )
        load_reviews(db)
        db.commit()
        if args.save_snapshot:
            save_snapshot(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()
