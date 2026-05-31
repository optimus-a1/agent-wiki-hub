# Wave 2 Source Review Work Order: TICKET-SRC-025

Generated: 2026-05-31

## Scope

- Work order: `WAVE2-WORKORDER-TICKET-SRC-025`
- Ticket: `TICKET-SRC-025`
- Task: `SRC-025`
- Wiki: `research-agent-wiki`
- Priority: `P2`
- Wave: `wave-2`
- Risk: `medium`
- Freshness: `high`
- Category: `general_current_fact`
- Reviewer role: `research-methods-reviewer`
- Human confirmation: no
- Topic: latest papers, preprints, revisions, citations and benchmark leaderboards

## Required Reading

- wikis/research-agent-wiki/AGENTS.md
- wikis/research-agent-wiki/manifest.yaml
- wikis/research-agent-wiki/README.md
- wikis/research-agent-wiki/rules/
- wikis/research-agent-wiki/sources/source-notes.md

## Suggested Source Types

- publisher page
- arXiv or conference page
- official benchmark leaderboard

## Local Artifacts

- Source notes: `wikis/research-agent-wiki/sources/source-notes.md`
- Evidence log: `wikis/research-agent-wiki/sources/source-refresh-log.md`
- Packet JSON: `registry/source-review-packets/source-review-session-wave-2-pending.json`
- Packet JSONL: `registry/source-review-packets/source-review-session-wave-2-pending.jsonl`
- Packet checklist: `registry/source-review-packets/source-review-session-wave-2-pending-checklist.md`

## Packet Entry Placeholder

This is not verified evidence. Replace every placeholder before any real import.

```json
{
  "ticket_id": "TICKET-SRC-025",
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
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-025 --status pending --dry-run
```

## Safety Boundary

- Planning-only work order; it does not browse, verify, certify, import, or write current facts.
- It does not authorize production operations, wallet actions, cloud changes, live upgrades, or billing-sensitive actions.
