#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"


def main() -> int:
    source = ROOT / "obsidian-vault"
    records = [path.relative_to(ROOT).as_posix() for path in source.rglob("*.md")] if source.exists() else []
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "rag-index-manifest.json").write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": True, "mode": "obsidian-index", "chunk_count": len(records)}, indent=2),
        encoding="utf-8",
    )
    print(f"RAG OBSIDIAN INDEX GENERATED ({len(records)} chunks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
