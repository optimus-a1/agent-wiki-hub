#!/usr/bin/env python3
"""Promote safe stable candidate knowledge to automation-generated files."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import argparse, json, re
ROOT = Path(__file__).resolve().parents[1]
CAND = ROOT / "obsidian-vault" / "02_Knowledge" / "Candidates"
HIGH_RISK_WIKIS = {"finance-agent-wiki","health-agent-wiki","legal-agent-wiki","security-agent-wiki","nodeops-agent-wiki","customs-agent-wiki","airdrop-agent-wiki"}
def parse(path):
    fields={}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if ":" in line and not line.startswith("#"):
            k,v=line.split(":",1); fields[k.strip()]=v.strip()
    return fields
def eligible(fields):
    return fields.get("classification")=="stable_knowledge" and fields.get("requires_human_review","true")=="false" and float(fields.get("confidence","0") or 0)>=0.75 and fields.get("target_wiki") not in HIGH_RISK_WIKIS and fields.get("source_url") and fields.get("source_title")
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--dry-run", action="store_true"); args=parser.parse_args()
    promotions=[]; blocked=[]
    for path in CAND.rglob("*.md") if CAND.exists() else []:
        fields=parse(path)
        if eligible(fields):
            promotions.append({"candidate": path.relative_to(ROOT).as_posix(), "target_wiki": fields.get("target_wiki"), "source_url": fields.get("source_url"), "source_title": fields.get("source_title")})
        else:
            blocked.append({"candidate": path.relative_to(ROOT).as_posix(), "reason": "not eligible"})
    if not args.dry_run:
        for item in promotions:
            out=ROOT/"wikis"/item["target_wiki"]/ "concepts" / "automation-generated-knowledge.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            block=f"\n## {item['source_title']}\n\n- source_status: stable\n- generated_from_raw: {item['candidate']}\n- source_url: {item['source_url']}\n- confidence: 0.8\n- promoted_on: {date.today().isoformat()}\n- reviewed_by: automation\n- limitations: Automation-generated low-risk stable candidate; human review recommended before broad reuse.\n\nNo current facts are promoted by this scaffold.\n"
            out.write_text((out.read_text(encoding="utf-8") if out.exists() else "---\ntitle: Automation Generated Knowledge\nstatus: stable\nlast_updated: "+date.today().isoformat()+"\nrisk_level: medium\n---\n\n# Automation Generated Knowledge\n") + block, encoding="utf-8")
    payload={"generated":date.today().isoformat(),"passed":True,"dry_run":args.dry_run,"promotion_count":len(promotions),"blocked_count":len(blocked),"promotions":promotions,"blocked":blocked}
    (ROOT/"registry").mkdir(exist_ok=True); (ROOT/"docs").mkdir(exist_ok=True)
    (ROOT/"registry"/"knowledge-promotion-report.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
    (ROOT/"docs"/"KNOWLEDGE_PROMOTION_REPORT.md").write_text(f"# Knowledge Promotion Report\n\n- Dry run: {args.dry_run}\n- Promotions: {len(promotions)}\n- Blocked: {len(blocked)}\n",encoding="utf-8")
    print(f"KNOWLEDGE PROMOTION PASSED ({len(promotions)} eligible, dry_run={args.dry_run})")
    return 0
if __name__ == "__main__": raise SystemExit(main())
