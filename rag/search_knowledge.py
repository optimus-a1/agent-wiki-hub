#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [ROOT / "wikis", ROOT / "docs", ROOT / "obsidian-vault" / "02_Knowledge", ROOT / "obsidian-vault" / "03_Skills"]


def docs_to_index():
    for source in SOURCES:
        if source.exists():
            yield from source.rglob("*.md")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()
    terms = [term.casefold() for term in re.findall(r"[A-Za-z0-9_-]+", args.query)]
    scored = []
    for path in docs_to_index():
        text = path.read_text(encoding="utf-8", errors="ignore")
        score = sum(text.casefold().count(term) for term in terms)
        if score:
            scored.append((score, path.relative_to(ROOT).as_posix()))
    for score, path in sorted(scored, reverse=True)[: args.top_k]:
        print(f"{score}\t{path}")
    if not scored:
        print("No keyword fallback results.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
