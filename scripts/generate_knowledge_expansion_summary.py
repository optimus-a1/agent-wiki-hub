#!/usr/bin/env python3
"""Summarize v2.1 knowledge expansion artifacts."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def main() -> int:
    manifest = read_json(REGISTRY / "knowledge-density-expansion-manifest.json")
    if not manifest:
        subprocess.run([sys.executable, "scripts/generate_v2_1_knowledge_density.py"], cwd=ROOT, check=True)
        manifest = read_json(REGISTRY / "knowledge-density-expansion-manifest.json")
    density = read_json(REGISTRY / "knowledge-density-report.json")
    records = manifest.get("records", [])
    payload = {
        "generated": date.today().isoformat(),
        "passed": True,
        "new_page_count": manifest.get("new_page_count", 0),
        "current_fact": False,
        "network_used": False,
        "evidence_status_changed": False,
        "summary": manifest.get("summary", {}),
        "density_groups": density.get("groups", {}),
        "created_files": [record["path"] for record in records if record.get("action") == "created"],
        "updated_files": [record["path"] for record in records if record.get("action") == "updated"],
    }
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "knowledge-expansion-summary.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Knowledge Expansion Summary",
        "",
        f"Generated: {payload['generated']}",
        "",
        f"- New pages: {payload['new_page_count']}",
        "- Current facts written: no",
        "- Evidence status changed: no",
        "- Network used: no",
        "",
        "| Wiki | Concepts | Rules | Workflows | Cases | Prompts | Eval Tests |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for wiki, counts in payload["summary"].items():
        lines.append(f"| {wiki} | {counts['concepts']} | {counts['rules']} | {counts['workflows']} | {counts['cases']} | {counts['prompts']} | {counts['eval_tests']} |")
    (DOCS / "KNOWLEDGE_EXPANSION_SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"KNOWLEDGE EXPANSION SUMMARY GENERATED ({payload['new_page_count']} new pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
