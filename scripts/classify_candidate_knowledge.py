#!/usr/bin/env python3
"""Classify Raw notes into candidate knowledge categories."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import argparse, json, re
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "obsidian-vault" / "01_Raw"
CAND = ROOT / "obsidian-vault" / "02_Knowledge" / "Candidates"
HIGH_RISK = {"finance-agent-wiki","health-agent-wiki","legal-agent-wiki","security-agent-wiki","nodeops-agent-wiki","customs-agent-wiki","airdrop-agent-wiki"}
CURRENT_TERMS = ["current", "latest", "price", "policy", "regulation", "version", "vulnerability", "api"]
def classify(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    target = ""
    title = path.stem
    source_url = ""
    for line in text.splitlines():
        if line.startswith("target_wiki:"): target = line.split(":",1)[1].strip()
        if line.startswith("source_title:"): title = line.split(":",1)[1].strip() or title
        if line.startswith("source_url:"): source_url = line.split(":",1)[1].strip()
    lower = text.casefold()
    if target in HIGH_RISK:
        cls, reason, review = "high_risk", "target wiki requires human gate", True
    elif any(term in lower for term in CURRENT_TERMS):
        cls, reason, review = "current_fact", "contains current-fact indicators", True
    elif not source_url:
        cls, reason, review = "low_quality", "missing source URL", True
    else:
        cls, reason, review = "stable_knowledge", "appears stable and low risk", False
    return {"path": path.relative_to(ROOT).as_posix(), "classification": cls, "confidence": 0.8 if cls == "stable_knowledge" else 0.5, "reason": reason, "target_wiki": target, "source_url": source_url, "source_title": title, "requires_human_review": review}
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--dry-run", action="store_true"); args=parser.parse_args()
    records=[]
    for path in RAW.rglob("*.md") if RAW.exists() else []:
        text=path.read_text(encoding="utf-8", errors="ignore")
        if "type: raw-source" in text: records.append(classify(path))
    if not args.dry_run:
        CAND.mkdir(parents=True, exist_ok=True)
        for rec in records:
            out=CAND/(Path(rec["path"]).stem+" Candidate.md")
            out.write_text("---\ntype: candidate-knowledge\nclassification: {classification}\nconfidence: {confidence}\nreason: {reason}\ntarget_wiki: {target_wiki}\nsuggested_path: \nsource_url: {source_url}\nsource_title: {source_title}\nrequires_human_review: {requires_human_review}\nsource_status: unverified\ngenerated_by: scripts/classify_candidate_knowledge.py\n---\n\n# Candidate: {source_title}\n\n## Extracted stable knowledge\n\n## What this source supports\n\n## What this source does not support\n\n## Risk classification\n{classification}\n\n## Suggested destination\n\n## Required review\n".format(**rec), encoding="utf-8")
    payload={"generated":date.today().isoformat(),"passed":True,"dry_run":args.dry_run,"candidate_count":len(records),"records":records,"warnings":[] if records else ["no Raw inputs"]}
    (ROOT/"registry").mkdir(exist_ok=True); (ROOT/"docs").mkdir(exist_ok=True)
    (ROOT/"registry"/"candidate-knowledge-report.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
    (ROOT/"docs"/"CANDIDATE_KNOWLEDGE_REPORT.md").write_text(f"# Candidate Knowledge Report\n\nGenerated: {date.today().isoformat()}\n\n- Candidates: {len(records)}\n- Dry run: {args.dry_run}\n",encoding="utf-8")
    print(f"CANDIDATE KNOWLEDGE CLASSIFICATION PASSED ({len(records)} records, dry_run={args.dry_run})")
    return 0
if __name__ == "__main__": raise SystemExit(main())
