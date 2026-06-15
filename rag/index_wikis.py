#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
OUT = ROOT / "rag" / "wiki-index.jsonl"


def parse_frontmatter(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    text = text.lstrip("\ufeff")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for raw in parts[1].splitlines():
                if ":" in raw:
                    key, value = raw.split(":", 1)
                    fields[key.strip()] = value.strip().strip('"')
    return fields


def density_group(path: Path) -> str:
    parts = path.relative_to(ROOT).parts
    if len(parts) > 2 and parts[0] == "wikis":
        area = parts[2]
        if area in {"concepts", "rules", "workflows", "cases", "prompts"}:
            return "stable-page"
        if area == "evals":
            return "eval"
    return "wiki-support"


def docs_to_index():
    source = ROOT / "wikis"
    for path in source.rglob("*.md"):
        yield path


def main() -> int:
    records = []
    for path in docs_to_index():
        text = path.read_text(encoding="utf-8", errors="ignore")
        fields = parse_frontmatter(text)
        records.append({
            "path": path.relative_to(ROOT).as_posix(),
            "wiki": fields.get("wiki", path.relative_to(ROOT).parts[1] if "wikis" in path.parts else ""),
            "title": fields.get("title", path.stem.replace("-", " ").title()),
            "knowledge_density_group": density_group(path),
            "current_fact": fields.get("current_fact", "false").casefold() == "true",
            "source_status": fields.get("source_status", ""),
            "generated_by": fields.get("generated_by", ""),
            "risk_level": fields.get("risk_level", ""),
            "human_gate_required": fields.get("requires_human_review", "false").casefold() == "true",
            "tokens": re.findall(r"[A-Za-z0-9_-]+", text.casefold())[:80],
        })
    REGISTRY.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n", encoding="utf-8")
    (REGISTRY / "rag-index-manifest.json").write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": True, "mode": "wiki-index", "chunk_count": len(records), "index": OUT.relative_to(ROOT).as_posix()}, indent=2),
        encoding="utf-8",
    )
    print(f"RAG WIKI INDEX GENERATED ({len(records)} chunks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
