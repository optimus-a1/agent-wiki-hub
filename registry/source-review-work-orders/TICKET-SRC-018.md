# Source Review Work Order: TICKET-SRC-018

Generated: 2026-09-05

## Scope

- Work order: `WORKORDER-TICKET-SRC-018`
- Ticket: `TICKET-SRC-018`
- Task: `SRC-018`
- Wiki: `ecommerce-agent-wiki`
- Priority: `P1`
- Wave: `wave-1`
- Risk: `medium`
- Freshness: `high`
- Category: `policy_or_regulation`
- Readiness stage: `ready-for-source-collection`
- Reviewer role: `ecommerce-policy-reviewer`
- Human review gate: no
- Topic: current marketplace policy, return window, category restrictions and consumer protection rules

## Required Reading

- `wikis/ecommerce-agent-wiki/AGENTS.md`
- `wikis/ecommerce-agent-wiki/manifest.yaml`
- `wikis/ecommerce-agent-wiki/README.md`
- `wikis/ecommerce-agent-wiki/rules/`
- `wikis/ecommerce-agent-wiki/sources/source-notes.md`

## Source Targets

- official marketplace policy center
- consumer protection authority
- merchant service agreement

## Local Artifacts

- Source notes: `wikis/ecommerce-agent-wiki/sources/source-notes.md`
- Evidence log: `wikis/ecommerce-agent-wiki/sources/source-refresh-log.md`
- Packet JSON: `registry/source-review-packets/source-review-session-wave-1-pending.json`
- Packet JSONL: `registry/source-review-packets/source-review-session-wave-1-pending.jsonl`
- Packet checklist: `registry/source-review-packets/source-review-session-wave-1-pending-checklist.md`

## Evidence Fields To Fill

Replace every placeholder before any real import. Leave `status` as `pending` until source evidence has actually been reviewed.

```json
{
  "ticket_id": "TICKET-SRC-018",
  "status": "pending",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "2026-09-05",
  "verified_on": "",
  "evidence_summary": "<what the source supports and does not support>",
  "affected_pages": [],
  "confidence": "low",
  "remaining_uncertainty": "<remaining uncertainty>",
  "human_reviewer": "",
  "follow_up": "Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed."
}
```

## Collection Checklist

- [ ] Read root AGENTS.md, target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.
- [ ] Collect only authoritative, dated, scoped evidence for the exact ticket topic.
- [ ] Prefer official primary sources; do not use secondary summaries as the only authority.
- [ ] Record source title, publisher, URL or local reference, publication/update date, access date, confidence, and uncertainty.
- [ ] Keep status pending or still-needs-source-update when evidence is missing, stale, conflicting, or out of scope.
- [ ] Replace every placeholder before any non-dry-run packet import.
- [ ] Do not record API keys, private keys, cookies, seed phrases, credentials, bearer tokens, or private account data.
- [ ] Do not write current facts into wiki pages until evidence logs, quality audit, completion audit, acceptance, and package checks pass.
- [ ] Verify source authority, publication/update date, scope, and access date before recording evidence.
- [ ] Confirm the source supports the exact ticket topic; put unsupported parts in remaining uncertainty.
- [ ] Prefer official, primary, dated sources and do not use summaries as the only authority.
- [ ] Do not record API keys, private keys, cookies, seed phrases, credentials, or private account data.
- [ ] Do not move current facts into stable wiki pages until ticket evidence, audits, and package checks pass.

## Commands

Run only dry-run imports until every placeholder is replaced.

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-018 --status pending --dry-run
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.jsonl --dry-run --no-post-checks
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-018 --status still-needs-source-update --source-title "<source title>" --source-publisher "<publisher>" --source-url-or-reference "<url or local reference>" --source-published-or-updated "YYYY-MM-DD | unknown" --evidence-summary "<what the source supports and does not support>" --confidence low --remaining-uncertainty "<remaining uncertainty>"
```

## Safety Boundary

- This work order is an offline collection aid; it does not verify or certify current facts.
- It does not authorize real-money trading, final legal or medical advice, offensive security activity, wallet signing, or production changes.
- Keep `needs-source-update` in the wiki until authoritative source evidence is recorded and audits pass.
