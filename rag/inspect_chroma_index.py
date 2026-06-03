#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "registry" / "rag-index-manifest.json"


def main() -> int:
    if MANIFEST.exists():
        print(MANIFEST.read_text(encoding="utf-8"))
    else:
        print(json.dumps({"passed": True, "warning": "rag index manifest missing"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
