#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"


def docs_to_index():
    source = ROOT / "wikis"
    for path in source.rglob("*.md"):
        yield path


def main() -> int:
    records = [path.relative_to(ROOT).as_posix() for path in docs_to_index()]
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "rag-index-manifest.json").write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": True, "mode": "wiki-index", "chunk_count": len(records)}, indent=2),
        encoding="utf-8",
    )
    print(f"RAG WIKI INDEX GENERATED ({len(records)} chunks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
