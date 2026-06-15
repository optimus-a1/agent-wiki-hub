#!/usr/bin/env python3
"""Audit crawler Raw outputs."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "obsidian-vault" / "01_Raw"
REQUIRED = ["source_url", "content_hash", "crawled_at", "requires_review", "robots_checked"]
SECRET_RE = re.compile(r"(ghp_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
def main():
    records=[]; issues=[]
    for path in RAW.rglob("*.md") if RAW.exists() else []:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "type: raw-source" not in text:
            continue
        missing=[field for field in REQUIRED if f"{field}:" not in text]
        has_secret=bool(SECRET_RE.search(text))
        record={"path": path.relative_to(ROOT).as_posix(), "missing": missing, "has_secret": has_secret}
        records.append(record)
        if missing or has_secret: issues.append(record)
    passed = not issues
    lines=["# Crawler Output Audit","",f"Generated: {date.today().isoformat()}","",f"- Passed: {passed}",f"- Raw notes checked: {len(records)}",""]
    if not records: lines.append("No Raw source notes found; no-op PASS.")
    (ROOT/"docs"/"CRAWLER_OUTPUT_AUDIT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    (ROOT/"registry"/"crawler-output-audit.json").write_text(json.dumps({"generated":date.today().isoformat(),"passed":passed,"records":records,"issues":issues},indent=2),encoding="utf-8")
    print(f"CRAWLER OUTPUT AUDIT {'PASSED' if passed else 'FAILED'} ({len(records)} raw notes)")
    return 0 if passed else 1
if __name__ == "__main__": raise SystemExit(main())
