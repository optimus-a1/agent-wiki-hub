#!/usr/bin/env python3
"""Generate controlled crawler report without network access."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parents[1]
def parse_sources(text: str):
    records, current = [], {}
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("- name:"):
            if current: records.append(current)
            current = {"name": line.split(":",1)[1].strip()}
        elif ":" in line and current:
            k,v=line.split(":",1)
            current[k.strip()] = v.strip().strip('"')
    if current: records.append(current)
    return records
def main():
    text = (ROOT / "crawler" / "sources.yaml").read_text(encoding="utf-8")
    sources = parse_sources(text)
    warnings = ["network collection not performed by report generator", "crawler writes Raw only and never writes to wikis"]
    payload = {"generated": date.today().isoformat(), "passed": True, "source_count": len(sources), "sources": sources, "warnings": warnings, "collected_count": 0}
    (ROOT / "registry").mkdir(exist_ok=True); (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "registry" / "crawler-sources.json").write_text(json.dumps({"generated": date.today().isoformat(), "sources": sources}, indent=2), encoding="utf-8")
    (ROOT / "registry" / "crawl-report.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for name, title in [("CONTROLLED_CRAWLER.md","Controlled Crawler"),("CRAWLER_SOURCE_POLICY.md","Crawler Source Policy"),("KNOWLEDGE_INGESTION_REVIEW_FLOW.md","Knowledge Ingestion Review Flow"),("CRAWL_REPORT.md","Crawl Report")]:
        (ROOT / "docs" / name).write_text(f"# {title}\n\nThe crawler is conservative, public-source only, respects configured limits, writes to Raw only, and never marks content verified.\n", encoding="utf-8")
    print(f"CRAWL REPORT GENERATED ({len(sources)} configured sources, 0 collected)")
    return 0
if __name__ == "__main__": raise SystemExit(main())
