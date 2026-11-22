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
PROMPT = """Analyze each numbered token of the supplied Septuagint verse in context.
Return JSON with a rows array, one row per token with integer position, exact surface,
lemma in polytonic Greek, English grammar description, and a short literal English
gloss under key gloss. Include articles and conjunctions. No commentary."""
TOKEN = re.compile(r"[^\W\d_]+(?:[\u0300-\u036f]+[^\W\d_]*)*(?:[᾽’ʼ'])?", re.UNICODE)


def analyze(host, model, verse, words, cache):
    message = dict(
        verse=verse,
        tokens=[dict(position=i, surface=w) for i, w in enumerate(words, 1)],
    )
    payload = json.dumps(
        dict(
            model=model,
            prompt=PROMPT + "\n" + json.dumps(message, ensure_ascii=False),
            stream=False,
            format={
                "type": "object",
                "required": ["rows"],
                "properties": {
                    "rows": {
                        "type": "array",
                        "minItems": len(words),
                        "maxItems": len(words),
                        "items": {
                            "type": "object",
                            "properties": {
                                "position": {"type": "integer"},
                                "surface": {
                                    "type": "string",
                                    "enum": list(dict.fromkeys(words)),
                                },
                                "lemma": {"type": "string"},
                                "grammar": {"type": "string"},
                                "gloss": {"type": "string"},
                            },
                            "required": [
                                "position",
                                "surface",
                                "lemma",
                                "grammar",
                                "gloss",
                            ],
                        },
                    }
                },
            },
            options=dict(temperature=0, seed=42),
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
    rows = json.loads(answer["response"])["rows"]
    if [(r["position"], r["surface"]) for r in rows] != list(enumerate(words, 1)):
        raise ValueError(f"{host}: token alignment failed")
    for r in rows:
        if not all(
            isinstance(r[k], str) and r[k].strip()
            for k in ("lemma", "grammar", "gloss")
        ):
            raise ValueError(f"{host}: incomplete analysis for {r['surface']}")
    path.write_text(json.dumps(answer, ensure_ascii=False))
    return rows


def main():
    from concurrent.futures import ThreadPoolExecutor

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-host", default="localhost")
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
                jobs = [
                    pool.submit(analyze, host, model, v["greek"], words, cache)
                    for role, host, model in engines
                ]
                for (role, host, model), job in zip(engines, jobs):
                    for r in job.result():
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
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    main()
