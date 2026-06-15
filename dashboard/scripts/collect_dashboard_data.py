#!/usr/bin/env python3
"""Collect static dashboard data from registry and wiki files."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "dashboard" / "data"
REGISTRY = ROOT / "registry"
WIKIS = ROOT / "wikis"
PACKS = ROOT / "packs"
DOCS = ROOT / "docs"

def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    acceptance = read_json(REGISTRY / "acceptance-report.json")
    source_refresh = read_json(REGISTRY / "source-refresh-dashboard.json")
    final_status = read_json(REGISTRY / "source-review-final-status.json")
    readiness = read_json(REGISTRY / "source-review-readiness-matrix.json")
    wiki_dirs = sorted(p for p in WIKIS.iterdir() if p.is_dir())
    page_count = sum(1 for p in WIKIS.rglob("*.md") if p.is_file())
    risk_counts = Counter()
    for wiki in wiki_dirs:
        text = (wiki / "manifest.yaml").read_text(encoding="utf-8", errors="ignore")
        for line in text.splitlines():
            if line.startswith("risk_level:"):
                risk_counts[line.split(":", 1)[1].strip()] += 1
    packs = sorted(p.name for p in PACKS.glob("*.zip")) if PACKS.exists() else []
    summary = {
        "generated": date.today().isoformat(),
        "passed": True,
        "wiki_count": len(wiki_dirs),
        "page_count": page_count,
        "acceptance_passed": acceptance.get("passed", False),
        "open_source_topics": final_status.get("open_topic_count", source_refresh.get("source_refresh", {}).get("completion", {}).get("open_ticket_count", 0)),
        "verified_tickets": final_status.get("verified_ticket_count", source_refresh.get("source_refresh", {}).get("completion", {}).get("verified_ticket_count", 0)),
        "current_fact_ready": final_status.get("current_fact_ready", source_refresh.get("current_fact_ready", False)),
        "human_gates": final_status.get("human_gates", {}),
        "risk_counts": dict(sorted(risk_counts.items())),
        "pack_count": len(packs),
    }
    files = {
        "dashboard-summary.json": summary,
        "wiki-status.json": {"generated": date.today().isoformat(), "wikis": [p.name for p in wiki_dirs], "risk_counts": summary["risk_counts"]},
        "source-review-status.json": final_status or {"generated": date.today().isoformat(), "waves": []},
        "acceptance-status.json": acceptance or {"generated": date.today().isoformat(), "passed": False},
        "packs.json": {"generated": date.today().isoformat(), "packs": packs},
    }
    for name, payload in files.items():
        (DATA / name).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (ROOT / "registry" / "dashboard-manifest.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": True, "files": list(files)}, indent=2), encoding="utf-8")
    (DOCS / "DASHBOARD_USAGE.md").write_text("# Dashboard Usage\n\nRun `python dashboard/scripts/collect_dashboard_data.py`, then open `dashboard/index.html` in a browser.\n", encoding="utf-8")
    print(f"DASHBOARD DATA GENERATED ({summary['wiki_count']} wikis, {summary['pack_count']} packs)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
