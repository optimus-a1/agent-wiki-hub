#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
OUT = ROOT / "rag" / "obsidian-index.jsonl"


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


def main() -> int:
    source = ROOT / "obsidian-vault"
    records = []
    if source.exists():
        for path in source.rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="ignore")
            fields = parse_frontmatter(text)
            records.append({
                "path": path.relative_to(ROOT).as_posix(),
                "wiki": fields.get("wiki", ""),
                "title": fields.get("title", path.stem),
                "knowledge_density_group": "obsidian-navigation",
                "current_fact": fields.get("current_fact", "false").casefold() == "true",
                "source_status": fields.get("source_status", ""),
                "generated_by": fields.get("generated_by", ""),
                "risk_level": fields.get("risk", fields.get("risk_level", "")),
                "human_gate_required": fields.get("requires_human_review", "false").casefold() == "true",
            })
    REGISTRY.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n", encoding="utf-8")
    (REGISTRY / "rag-index-manifest.json").write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": True, "mode": "obsidian-index", "chunk_count": len(records), "index": OUT.relative_to(ROOT).as_posix()}, indent=2),
        encoding="utf-8",
    )
    print(f"RAG OBSIDIAN INDEX GENERATED ({len(records)} chunks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
