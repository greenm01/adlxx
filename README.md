# Apostoliki Diakonia Septuagint Interlinear

A local Greek–English word database for the Septuagint text published online by Apostoliki Diakonia. The initial sample is Genesis 1:1. The project takes its Greek, verse addresses and token positions directly from the publisher. [Publisher’s Genesis](https://apostoliki-diakonia.gr/bible/genesis/)

The source table records the verse exactly as displayed, its URL and retrieval date. Token positions begin at one within each verse. The full verse retains spaces and punctuation. Lemmas, morphology and English glosses are separate analyses of the Greek in context. Each model reading carries its own status and provenance. An English gloss can depend on the construction as a whole.

## Local build

Start Ollama on the Mac. Crunch must be reachable as the SSH host `crunch` with its Ollama API listening on localhost. The pilot uses Qwen 3.5 9B on Crunch to draft and Gemma 3 12B on the Mac for an independent second reading. Each gets the same Greek verse and numbered tokens. No cloud inference is required.

```sh
python3 interlinear.py
sqlite3 -header -column build/adlxx.sqlite "SELECT position,surface,model,lemma,grammar,gloss FROM token JOIN analysis USING(ref,position) WHERE ref='GEN 1:1' ORDER BY position,model"
```

Successful responses are cached locally. Rerunning with the same inputs reuses them. A failed build rolls back the database transaction. Both model readings remain drafts, including where they agree.

For the chapter pilot, review disagreements with the verse in view, check recurring errors such as article glosses and ambiguous case forms, and spot-check agreements. Before distributing a book-length text, identify the underlying printing and document the publisher's terms for reuse.
