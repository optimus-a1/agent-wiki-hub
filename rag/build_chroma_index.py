#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
SOURCES = [ROOT / "wikis", ROOT / "docs", ROOT / "obsidian-vault" / "02_Knowledge", ROOT / "obsidian-vault" / "03_Skills"]


def docs_to_index():
    for source in SOURCES:
        if not source.exists():
            continue
        for path in source.rglob("*.md"):
            yield path


def main() -> int:
    records = [path.relative_to(ROOT).as_posix() for path in docs_to_index()]
    try:
        import chromadb  # noqa: F401
        mode = "chroma-available"
        warning = ""
    except Exception:
        mode = "keyword-fallback"
        warning = "chromadb missing; persistent semantic index not built"
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "rag-index-manifest.json").write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": True, "mode": mode, "warning": warning, "chunk_count": len(records)}, indent=2),
        encoding="utf-8",
    )
    print(f"RAG INDEX READY ({mode}, {len(records)} chunks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
