#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import re
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [ROOT / "wikis", ROOT / "docs", ROOT / "obsidian-vault" / "02_Knowledge", ROOT / "obsidian-vault" / "03_Skills"]


def docs_to_index():
    for source in SOURCES:
        if source.exists():
            yield from source.rglob("*.md")


def parse_frontmatter(text):
    fields = {}
    text = text.lstrip("\ufeff")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for raw in parts[1].splitlines():
                if ":" in raw:
                    key, value = raw.split(":", 1)
                    fields[key.strip()] = value.strip().strip('"')
    return fields


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
            fields = parse_frontmatter(text)
            scored.append((score, path.relative_to(ROOT).as_posix(), fields))
    for score, path, fields in sorted(scored, reverse=True)[: args.top_k]:
        metadata = {
            "wiki": fields.get("wiki", ""),
            "current_fact": fields.get("current_fact", "false"),
            "source_status": fields.get("source_status", ""),
            "risk_level": fields.get("risk_level", fields.get("risk", "")),
            "human_gate_required": fields.get("requires_human_review", "false"),
            "generated_by": fields.get("generated_by", ""),
        }
        print(f"{score}\t{path}\t{json.dumps(metadata, ensure_ascii=False)}")
    if not scored:
        print("No keyword fallback results.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
