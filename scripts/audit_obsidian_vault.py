#!/usr/bin/env python3
"""Audit generated Obsidian vault structure."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "obsidian-vault"
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"
REQUIRED = [
    "00_System/README.md", "01_Raw/README.md", "02_Knowledge/README.md", "03_Skills/README.md",
    "04_Output/README.md", "05_Dashboard/Wiki Status.md", "05_Dashboard/Source Review Status.md",
    "05_Dashboard/Acceptance Status.md", "05_Dashboard/Needs Source Update.md", "05_Dashboard/Human Gates.md",
    "05_Dashboard/Knowledge Graph Status.md", "05_Dashboard/Knowledge Density.md",
    "05_Dashboard/Current Fact Gates.md", "05_Dashboard/Human Review Gates.md",
    "05_Dashboard/High Risk Boundaries.md", "99_Archive/README.md",
]

def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

def main() -> int:
    checks = [{"path": item, "passed": (VAULT / item).exists()} for item in REQUIRED]
    mocs = list((VAULT / "02_Knowledge" / "MOCs").glob("*.md")) if VAULT.exists() else []
    checks.append({"path": "02_Knowledge/MOCs", "passed": len(mocs) >= 12})
    failed = [c for c in checks if not c["passed"]]
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    lines = ["# Obsidian Vault Audit", "", f"Generated: {date.today().isoformat()}", "", f"- Passed: {not failed}", f"- MOCs: {len(mocs)}", "", "| Check | Result |", "| --- | --- |"]
    lines.extend(f"| {c['path']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in checks)
    (DOCS / "OBSIDIAN_VAULT_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REGISTRY / "obsidian-vault-audit.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": not failed, "checks": checks, "moc_count": len(mocs)}, indent=2), encoding="utf-8")
    print(f"OBSIDIAN VAULT AUDIT {'PASSED' if not failed else 'FAILED'} ({len(checks)} checks)")
    return 0 if not failed else 1

if __name__ == "__main__":
    raise SystemExit(main())
