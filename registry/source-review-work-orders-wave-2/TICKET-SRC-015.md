# Wave 2 Source Review Work Order: TICKET-SRC-015

Generated: 2026-05-31

## Scope

- Work order: `WAVE2-WORKORDER-TICKET-SRC-015`
- Ticket: `TICKET-SRC-015`
- Task: `SRC-015`
- Wiki: `customs-agent-wiki`
- Priority: `P0`
- Wave: `wave-2`
- Risk: `medium`
- Freshness: `high`
- Category: `general_current_fact`
- Reviewer role: `customs-document-reviewer`
- Human confirmation: no
- Topic: latest HS codes, customs supervision conditions and declaration elements

## Required Reading

- wikis/customs-agent-wiki/AGENTS.md
- wikis/customs-agent-wiki/manifest.yaml
- wikis/customs-agent-wiki/README.md
- wikis/customs-agent-wiki/rules/
- wikis/customs-agent-wiki/sources/source-notes.md

## Suggested Source Types

- customs authority website
- official tariff database
- licensed customs broker review

## Local Artifacts

- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- Evidence log: `wikis/customs-agent-wiki/sources/source-refresh-log.md`
- Packet JSON: `registry/source-review-packets/source-review-session-wave-2-pending.json`
- Packet JSONL: `registry/source-review-packets/source-review-session-wave-2-pending.jsonl`
- Packet checklist: `registry/source-review-packets/source-review-session-wave-2-pending-checklist.md`

## Packet Entry Placeholder

This is not verified evidence. Replace every placeholder before any real import.

```json
{
  "ticket_id": "TICKET-SRC-015",
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
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-015 --status pending --dry-run
```

## Safety Boundary

- Planning-only work order; it does not browse, verify, certify, import, or write current facts.
- It does not authorize production operations, wallet actions, cloud changes, live upgrades, or billing-sensitive actions.
