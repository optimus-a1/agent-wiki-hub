#!/usr/bin/env python3
"""Audit local static dashboard files."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "dashboard/README.md", "dashboard/package.json", "dashboard/index.html", "dashboard/src/main.js", "dashboard/src/styles.css",
    "dashboard/data/dashboard-summary.json", "dashboard/data/wiki-status.json", "dashboard/data/source-review-status.json",
    "dashboard/data/acceptance-status.json", "dashboard/data/packs.json", "dashboard/data/knowledge-density.json",
    "dashboard/data/high-risk-boundaries.json", "dashboard/data/current-fact-gates.json", "dashboard/data/wiki-moc-status.json",
]
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"

def main() -> int:
    checks = []
    for item in REQUIRED:
        path = ROOT / item
        passed = path.exists()
        if passed and path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                passed = False
        checks.append({"path": item, "passed": passed})
    failed = [c for c in checks if not c["passed"]]
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    lines = ["# Dashboard Audit", "", f"Generated: {date.today().isoformat()}", "", f"- Passed: {not failed}", "", "| Path | Result |", "| --- | --- |"]
    lines.extend(f"| {c['path']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in checks)
    (DOCS / "DASHBOARD_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REGISTRY / "dashboard-audit.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": not failed, "checks": checks}, indent=2), encoding="utf-8")
    print(f"DASHBOARD AUDIT {'PASSED' if not failed else 'FAILED'} ({len(checks)} checks)")
    return 0 if not failed else 1

if __name__ == "__main__":
    raise SystemExit(main())
