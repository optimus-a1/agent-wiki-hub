#!/usr/bin/env python3
"""Audit RAG configuration and optional Chroma readiness."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["rag/README.md", "rag/rag_config.yaml", "rag/requirements-rag.txt", "rag/index_wikis.py", "rag/index_obsidian.py", "rag/build_chroma_index.py", "rag/inspect_chroma_index.py", "rag/search_knowledge.py"]
def main():
    checks = [{"path": item, "passed": (ROOT / item).exists()} for item in REQUIRED]
    warnings = []
    try:
        import chromadb  # noqa: F401
    except Exception:
        warnings.append("chromadb missing; keyword fallback remains available")
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8", errors="ignore")
    checks.append({"path": ".gitignore rag/chroma/", "passed": "rag/chroma/" in gitignore})
    failed = [c for c in checks if not c["passed"]]
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "registry").mkdir(exist_ok=True)
    lines = ["# RAG Config Audit", "", f"Generated: {date.today().isoformat()}", "", f"- Passed: {not failed}", *[f"- Warning: {w}" for w in warnings], "", "| Check | Result |", "| --- | --- |"]
    lines.extend(f"| {c['path']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in checks)
    (ROOT / "docs" / "RAG_CONFIG_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "registry" / "rag-config-audit.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": not failed, "warnings": warnings, "checks": checks}, indent=2), encoding="utf-8")
    print(f"RAG CONFIG AUDIT {'PASSED' if not failed else 'FAILED'} ({len(warnings)} warnings)")
    return 0 if not failed else 1
if __name__ == "__main__": raise SystemExit(main())
