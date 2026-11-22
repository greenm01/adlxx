"""Inventory publisher book and chapter navigation and cache the original pages."""

from concurrent.futures import ThreadPoolExecutor
import csv
import gzip
from pathlib import Path
import re
import subprocess
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parent
BASE = "https://apostoliki-diakonia.gr/bible/"
CACHE = ROOT / "build/publisher"
CODES = dict(
    zip(
        "genesis exodos levitikon arithmoi deuteronomion ihsous-navi kritai routh vasileion-a vasileion-b vasileion-c vasileion-d paraleipomenon-a paraleipomenon-b esdras-a esdras-b neemias tovit ioudith esthir makkavaion-a makkavaion-b makkavaion-c psalmoi iov parimiai-solomontos ekklisiastis asma-asmaton sofia-solomontos sofia-seirax osie amos michaias ioil ovdiou ionas naoum amvakoum sofonias aggaios zacharias malachias isaias ieremias varouch thrinoi-ieremiou epistoli-ieremiou iezekiil daniil makkavaion-d-parartima".split(),
        "GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH 1ES EZR NEH TOB JDT ESG 1MA 2MA 3MA PSA JOB PRO ECC SNG WIS SIR HOS AMO MIC JOL OBA JON NAM HAB ZEP HAG ZEC MAL ISA JER BAR LAM LJE EZK DAG 4MA".split(),
        strict=True,
    )
)


def fetch(url, path):
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        body = subprocess.check_output(
            ["curl", "-fsSL", "--retry", "3", "--max-time", "45", url]
        )
        if b"</html>" not in body.lower():
            raise ValueError(f"Incomplete HTML at {url}")
        tmp = path.with_suffix(".part")
        tmp.write_bytes(gzip.compress(body, compresslevel=3))
        tmp.replace(path)
    return gzip.decompress(path.read_bytes()).decode("utf-8-sig")


def book(slug):
    code = CODES[slug]
    url = BASE + slug + "/"
    html = fetch(url, CACHE / code / "index.gz")
    links = list(
        dict.fromkeys(
            re.findall(
                r'<a\s+href="(\?file=[^"]+)"[^>]*>\s*([^<]+?)\s*</a>', html, re.I
            )
        )
    )
    if not links:
        return [(code, "1", url, "index.gz")]
    return [
        (code, label, urljoin(url, q), f"{i:03}.gz")
        for i, (q, label) in enumerate(links, 1)
    ]


def main():
    source = fetch(BASE + "genesis/", CACHE / "GEN/index.gz")
    ordered = list(
        dict.fromkeys(
            re.findall(
                r'href="https://apostoliki-diakonia\.gr/bible/([^"/]+)/"', source
            )
        )
    )
    if set(ordered) != set(CODES):
        raise ValueError("Review updated publisher book list")
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = [row for result in pool.map(book, ordered) for row in result]
        dest = ROOT / "data/publisher-chapters.tsv"
        with dest.open("w") as f:
            writer = csv.writer(f, delimiter="\t", lineterminator="\n")
            writer.writerow(("book", "chapter_label", "url", "cache_file"))
            writer.writerows(rows)
        print(f"{len(ordered)} books, {len(rows)} chapter entries", flush=True)

        def download(row):
            code, label, url, name = row
            fetch(url, CACHE / code / name)

        for i, _ in enumerate(pool.map(download, rows), 1):
            if i % 50 == 0:
                print(f"{i}/{len(rows)}", flush=True)


if __name__ == "__main__":
    main()
