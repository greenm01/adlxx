"""Let a local model choose an attested Athens reading for an AD form in context."""

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import sqlite3
import subprocess
from urllib.request import Request, urlopen

from athens_candidates import normalized
from corpus_build import Athens, DB, REV
from corpus_context import accent
from publisher_catalog import ROOT


def candidates(repo):
    counts = defaultdict(Counter)
    examples = {}
    for entries in Athens(repo).verses.values():
        for form, lemma, grammar, gloss, ref, pos in entries:
            key = accent(form)
            reading = (lemma, grammar, gloss)
            if not all(reading) or max(map(len, reading)) > 150:
                continue
            counts[key][reading] += 1
            examples.setdefault((key, reading), (ref, pos))
    return {
        key: [(*r, *examples[key, r]) for r, n in pool.most_common(8)]
        for key, pool in counts.items()
    }


def choose(host, model, batch):
    items = []
    fields = {}
    for ref, text, tokens in batch:
        asks = []
        for i, surface, options in tokens:
            key = f"{ref}/{i}"
            letters = "ABCDEFGH"[: len(options)]
            fields[key] = {"type": "string", "enum": [*letters, "pass"]}
            asks.append(
                [
                    key,
                    surface,
                    dict(zip(letters, [r[:3] for r in options], strict=True)),
                ]
            )
        items.append([ref, text, asks])
    payload = json.dumps(
        dict(
            model=model,
            prompt=(
                "Select the best lemma, grammar and English gloss for each numbered Greek token in its verse. "
                "Select the associated letter. If multiple options are equivalent, choose the first appropriate letter. Select pass when none fits the context. "
                "Return only the requested JSON. Each verse gives its full Greek and then the keys, surface forms and alternatives.\n"
                + json.dumps(items, ensure_ascii=False)
            ),
            stream=False,
            format={
                "type": "object",
                "properties": fields,
                "required": list(fields),
                "additionalProperties": False,
            },
            options=dict(temperature=0, seed=42, num_ctx=8192),
            **({"think": False} if model.startswith("qwen") else {}),
        )
    ).encode()
    # Bound the prompt conservatively; split batches before either model's context fills.
    if len(payload) > 13500 and len(batch) > 1:
        mid = len(batch) // 2
        return choose(host, model, batch[:mid]) | choose(host, model, batch[mid:])
    if len(payload) > 13500 and len(batch[0][2]) > 1:
        ref, text, tokens = batch[0]
        mid = len(tokens) // 2
        return choose(host, model, [(ref, text, tokens[:mid])]) | choose(
            host, model, [(ref, text, tokens[mid:])]
        )
    url = "http://localhost:11434/api/generate"
    if host == "localhost":
        with urlopen(
            Request(url, payload, {"Content-Type": "application/json"}), timeout=300
        ) as f:
            response = json.load(f)
    else:
        response = json.loads(
            subprocess.check_output(
                [
                    "ssh",
                    host,
                    'curl -fsS --max-time 300 -H "Content-Type: application/json" --data-binary @- '
                    + url,
                ],
                input=payload,
                timeout=315,
            )
        )
    result = json.loads(response["response"])
    if result.keys() != fields.keys() or any(
        type(v) != str or v not in fields[k]["enum"] for k, v in result.items()
    ):
        raise ValueError("Model returned an invalid candidate selection")
    return {k: 0 if v == "pass" else "ABCDEFGH".index(v) + 1 for k, v in result.items()}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("repo", type=Path)
    cli.add_argument("host", choices=["localhost", "crunch"])
    cli.add_argument("--control", action="store_true")
    cli.add_argument("--limit", type=int, default=0)
    args = cli.parse_args()
    options = candidates(args.repo)
    model = "gemma3:12b" if args.host == "localhost" else "qwen3.5:9b"
    with sqlite3.connect(DB, timeout=90) as db:
        if args.control:
            batch = []
            for ref, pos in [("GEN 1:3", 5), ("GEN 1:5", 20), ("GEN 1:26", 5)]:
                greek, surface = db.execute(
                    "SELECT v.greek,t.surface FROM verse v JOIN token t USING(ref) WHERE ref=? AND position=?",
                    (ref, pos),
                ).fetchone()
                batch.append(
                    (ref, greek, [(pos, surface, options[accent(normalized(surface))])])
                )
            result = choose(args.host, model, batch)
            for ref, _, tokens in batch:
                for pos, w, opts in tokens:
                    k = result[f"{ref}/{pos}"]
                    print(ref, w, opts[k - 1][:3] if k else "abstained")
            return
        db.execute(
            """CREATE TABLE IF NOT EXISTS candidate_decision(ref TEXT,position INTEGER,surface TEXT,model TEXT,choice INTEGER,PRIMARY KEY(ref,position,model))"""
        )
        refs = db.execute(
            """SELECT DISTINCT t.ref FROM token t WHERE t.basis='needs local analysis'
            AND NOT EXISTS(SELECT 1 FROM candidate_decision d WHERE d.ref=t.ref AND d.position=t.position AND d.model=?) ORDER BY t.ref""",
            (model,),
        ).fetchall()
        if args.host == "localhost":
            refs.reverse()
        batches = 0
        batch = []
        fetched = 0

        def apply():
            chosen = choose(args.host, model, batch)
            accepted = 0
            with db:
                for ref, text, tokens in batch:
                    if db.execute(
                        "SELECT greek FROM verse WHERE ref=?", (ref,)
                    ).fetchone() != (text,):
                        continue
                    for pos, surface, opts in tokens:
                        choice = chosen[f"{ref}/{pos}"]
                        db.execute(
                            "INSERT OR REPLACE INTO candidate_decision VALUES(?,?,?,?,?)",
                            (ref, pos, surface, model, choice),
                        )
                        if choice:
                            lemma, grammar, gloss, src, sp = opts[choice - 1]
                            count = db.execute(
                                """UPDATE token SET lemma=?,grammar=?,gloss=?,basis='local Athens choice',source_ref=?,source_position=?,source_revision=? WHERE ref=? AND position=? AND surface=? AND basis='needs local analysis'""",
                                (
                                    lemma,
                                    grammar,
                                    gloss,
                                    src,
                                    sp,
                                    REV,
                                    ref,
                                    pos,
                                    surface,
                                ),
                            ).rowcount
                            if count:
                                db.execute(
                                    "INSERT OR REPLACE INTO model_reading VALUES(?,?,?,?,?,?,?,?)",
                                    (
                                        ref,
                                        pos,
                                        surface,
                                        args.host,
                                        model,
                                        lemma,
                                        grammar,
                                        gloss,
                                    ),
                                )
                            accepted += count
                print(
                    batch[-1][0],
                    accepted,
                    "of",
                    sum(len(x[2]) for x in batch),
                    flush=True,
                )

        for (ref,) in refs:
            text = db.execute("SELECT greek FROM verse WHERE ref=?", (ref,)).fetchone()[
                0
            ]
            rows = db.execute(
                """SELECT position,surface FROM token t WHERE ref=? AND basis='needs local analysis' AND NOT EXISTS(SELECT 1 FROM candidate_decision d WHERE d.ref=t.ref AND d.position=t.position AND d.model=?) ORDER BY position""",
                (ref, model),
            )
            tokens = [
                (pos, w, options[k])
                for pos, w in rows
                if (k := accent(normalized(w))) in options
            ]
            if not tokens:
                continue
            batch.append((ref, text, tokens))
            fetched += len(tokens)
            if fetched >= 14 or len(batch) >= 8:
                apply()
                batches += 1
                batch = []
                fetched = 0
                if args.limit and batches >= args.limit:
                    return
        if batch:
            apply()


if __name__ == "__main__":
    main()
