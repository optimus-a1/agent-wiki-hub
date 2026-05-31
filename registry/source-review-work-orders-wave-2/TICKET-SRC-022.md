# Wave 2 Source Review Work Order: TICKET-SRC-022

Generated: 2026-05-31

## Scope

- Work order: `WAVE2-WORKORDER-TICKET-SRC-022`
- Ticket: `TICKET-SRC-022`
- Task: `SRC-022`
- Wiki: `nodeops-agent-wiki`
- Priority: `P1`
- Wave: `wave-2`
- Risk: `high`
- Freshness: `medium`
- Category: `technical_docs`
- Reviewer role: `operations-change-reviewer`
- Human confirmation: yes
- Topic: current blockchain node client versions, network parameters and upgrade requirements

## Required Reading

- wikis/nodeops-agent-wiki/AGENTS.md
- wikis/nodeops-agent-wiki/manifest.yaml
- wikis/nodeops-agent-wiki/README.md
- wikis/nodeops-agent-wiki/rules/
- wikis/nodeops-agent-wiki/sources/source-notes.md

## Suggested Source Types

- official client release notes
- chain foundation announcement
- node logs and version output

## Local Artifacts

- Source notes: `wikis/nodeops-agent-wiki/sources/source-notes.md`
- Evidence log: `wikis/nodeops-agent-wiki/sources/source-refresh-log.md`
- Packet JSON: `registry/source-review-packets/source-review-session-wave-2-pending.json`
- Packet JSONL: `registry/source-review-packets/source-review-session-wave-2-pending.jsonl`
- Packet checklist: `registry/source-review-packets/source-review-session-wave-2-pending-checklist.md`

## Packet Entry Placeholder

This is not verified evidence. Replace every placeholder before any real import.

```json
{
  "ticket_id": "TICKET-SRC-022",
  "status": "pending",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "2026-05-31",
  "verified_on": "",
  "evidence_summary": "<what the source supports and does not support>",
  "affected_pages": [],
  "confidence": "low",
  "remaining_uncertainty": "<remaining uncertainty>",
  "human_reviewer": "<reviewer>",
  "follow_up": "Keep needs-source-update unless authoritative, dated, scoped evidence is recorded and reviewed."
}
```

## Collection Checklist

- [ ] Confirm exact ticket scope before collecting sources.
- [ ] Use authoritative, dated, scoped sources only.
- [ ] Record title, publisher, URL or local reference, publication/update date, access date, confidence, and uncertainty.
- [ ] Keep status pending or still-needs-source-update unless evidence has been reviewed.
- [ ] Fill `human_reviewer` before any final status; high-risk nodeops tickets require named human confirmation.
- [ ] Do not write current facts into wiki pages from this work order.
- [ ] Do not record API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.

## Dry Run

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-022 --status pending --dry-run
```

## Safety Boundary

- Planning-only work order; it does not browse, verify, certify, import, or write current facts.
- It does not authorize production operations, wallet actions, cloud changes, live upgrades, or billing-sensitive actions.
