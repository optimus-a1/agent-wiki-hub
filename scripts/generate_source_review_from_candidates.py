#!/usr/bin/env python3
"""Generate non-blocking source-review queue from current/high-risk candidates."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import argparse, json
ROOT=Path(__file__).resolve().parents[1]
CAND=ROOT/"obsidian-vault"/"02_Knowledge"/"Candidates"
PACKETS=ROOT/"registry"/"source-review-packets"
def parse(path):
    fields={}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if ":" in line and not line.startswith("#"):
            k,v=line.split(":",1); fields[k.strip()]=v.strip()
    return fields
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--dry-run", action="store_true"); args=parser.parse_args()
    entries=[]
    for idx,path in enumerate(CAND.rglob("*.md") if CAND.exists() else [], start=1):
        fields=parse(path)
        if fields.get("classification") in {"current_fact","high_risk"}:
            entries.append({"ticket_id":f"AUTO-SRC-{date.today().strftime('%Y%m%d')}-{idx:03d}","status":"pending","source_title":fields.get("source_title","<source title>"),"source_publisher":"<publisher>","source_url_or_reference":fields.get("source_url","<url or local reference>"),"source_published_or_updated":"YYYY-MM-DD | unknown","source_accessed_on":date.today().isoformat(),"verified_on":"","evidence_summary":"<what the source supports and does not support>","affected_pages":[],"confidence":"low","remaining_uncertainty":"<remaining uncertainty>","human_reviewer":"<reviewer>","follow_up":"Keep pending until authoritative, dated, scoped evidence is reviewed."})
    PACKETS.mkdir(parents=True, exist_ok=True); (ROOT/"docs").mkdir(exist_ok=True); (ROOT/"registry").mkdir(exist_ok=True)
    packet={"packet_id":"source-review-session-auto-pending","created_on":date.today().isoformat(),"planning_only":True,"no_current_fact_write":True,"entries":entries}
    if not args.dry_run or not (PACKETS/"source-review-session-auto-pending.json").exists():
        (PACKETS/"source-review-session-auto-pending.json").write_text(json.dumps(packet,indent=2),encoding="utf-8")
        (PACKETS/"source-review-session-auto-pending.jsonl").write_text("\n".join(json.dumps(e) for e in entries)+("\n" if entries else ""),encoding="utf-8")
    (ROOT/"registry"/"knowledge-review-queue.json").write_text(json.dumps({"generated":date.today().isoformat(),"passed":True,"dry_run":args.dry_run,"entry_count":len(entries),"entries":entries},indent=2),encoding="utf-8")
    (ROOT/"docs"/"AUTO_SOURCE_REVIEW_QUEUE.md").write_text(f"# Auto Source Review Queue\n\n- Dry run: {args.dry_run}\n- Pending entries: {len(entries)}\n- This queue is planning-only and must not be imported automatically.\n",encoding="utf-8")
    print(f"AUTO SOURCE REVIEW QUEUE PASSED ({len(entries)} entries, dry_run={args.dry_run})")
    return 0
if __name__ == "__main__": raise SystemExit(main())
