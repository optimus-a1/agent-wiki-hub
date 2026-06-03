#!/usr/bin/env python3
"""Audit automation-generated knowledge promotion outputs."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"automation-generated-knowledge.md","automation-generated-rules.md","automation-generated-workflows.md","automation-generated-cases.md"}
BAD = re.compile(r"(classification:\s*current_fact|classification:\s*high_risk|current_fact promoted|high-risk promoted)", re.I)
SECRET = re.compile(r"(ghp_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
def main():
    records=[]; issues=[]
    for path in (ROOT/"wikis").rglob("automation-generated-*.md"):
        text=path.read_text(encoding="utf-8", errors="ignore")
        rec={"path":path.relative_to(ROOT).as_posix(),"allowed_name":path.name in ALLOWED,"has_bad_marker":bool(BAD.search(text)),"has_secret":bool(SECRET.search(text)),"source_url_present":"source_url:" in text}
        records.append(rec)
        if not rec["allowed_name"] or rec["has_bad_marker"] or rec["has_secret"] or not rec["source_url_present"]: issues.append(rec)
    passed=not issues
    (ROOT/"docs").mkdir(exist_ok=True); (ROOT/"registry").mkdir(exist_ok=True)
    (ROOT/"docs"/"KNOWLEDGE_PROMOTION_AUDIT.md").write_text(f"# Knowledge Promotion Audit\n\nGenerated: {date.today().isoformat()}\n\n- Passed: {passed}\n- Files checked: {len(records)}\n",encoding="utf-8")
    (ROOT/"registry"/"knowledge-promotion-audit.json").write_text(json.dumps({"generated":date.today().isoformat(),"passed":passed,"records":records,"issues":issues},indent=2),encoding="utf-8")
    print(f"KNOWLEDGE PROMOTION AUDIT {'PASSED' if passed else 'FAILED'} ({len(records)} files)")
    return 0 if passed else 1
if __name__ == "__main__": raise SystemExit(main())
