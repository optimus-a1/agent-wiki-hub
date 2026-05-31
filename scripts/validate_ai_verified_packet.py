#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
packet = ROOT / "registry/source-review-packets/source-review-session-wave-1-ai-verified.json"
data = json.loads(packet.read_text(encoding="utf-8"))
entries = data.get("entries", [])
assert data.get("current_fact_ready") is False, "current_fact_ready must stay false"
assert data.get("human_review_gate_required") is True, "human gate must stay required"
assert data.get("human_final_acceptance_required") is True, "final human acceptance flag missing"
assert len({e.get("ticket_id") for e in entries}) == 13, "must cover 13 tickets"
assert len(entries) == 66, "must contain 66 entries"
assert all(e.get("status") == "verified" for e in entries), "all entries must be verified"
assert all(e.get("verified_on") == "2026-05-28" for e in entries), "all entries must have verified_on=2026-05-28"
print("PASS")
print("tickets covered: 13")
print("entries: 66")
print("all_status_verified: True")
print("all_verified_on: 2026-05-28")
print("human_final_acceptance_required: True")
