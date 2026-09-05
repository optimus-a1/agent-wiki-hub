# Source Review Work Order: TICKET-SRC-001

Generated: 2026-09-05

## Scope

- Work order: `WORKORDER-TICKET-SRC-001`
- Ticket: `TICKET-SRC-001`
- Task: `SRC-001`
- Wiki: `airdrop-agent-wiki`
- Priority: `P1`
- Wave: `wave-1`
- Risk: `high`
- Freshness: `high`
- Category: `web3_project_status`
- Readiness stage: `ready-for-source-collection`
- Reviewer role: `web3-wallet-safety-reviewer`
- Human review gate: yes
- Topic: current contract addresses, wallet warnings, scam reports and signing risks

## Required Reading

- `wikis/airdrop-agent-wiki/AGENTS.md`
- `wikis/airdrop-agent-wiki/manifest.yaml`
- `wikis/airdrop-agent-wiki/README.md`
- `wikis/airdrop-agent-wiki/rules/`
- `wikis/airdrop-agent-wiki/sources/source-notes.md`

## Source Targets

- official contract registry
- block explorer
- wallet security warning

## Local Artifacts

- Source notes: `wikis/airdrop-agent-wiki/sources/source-notes.md`
- Evidence log: `wikis/airdrop-agent-wiki/sources/source-refresh-log.md`
- Packet JSON: `registry/source-review-packets/source-review-session-wave-1-pending.json`
- Packet JSONL: `registry/source-review-packets/source-review-session-wave-1-pending.jsonl`
- Packet checklist: `registry/source-review-packets/source-review-session-wave-1-pending-checklist.md`

## Evidence Fields To Fill

Replace every placeholder before any real import. Leave `status` as `pending` until source evidence has actually been reviewed.

```json
{
  "ticket_id": "TICKET-SRC-001",
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
  "human_reviewer": "<reviewer>",
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
- [ ] Name a human reviewer before marking this ticket verified or unchanged.
- [ ] Keep the relevant high-risk boundary visible in the evidence summary.
- [ ] Do not use this work order as permission for autonomous finance, legal, medical, security, Web3, or production operations.
- [ ] Verify source authority, publication/update date, scope, and access date before recording evidence.
- [ ] Confirm the source supports the exact ticket topic; put unsupported parts in remaining uncertainty.
- [ ] Prefer official, primary, dated sources and do not use summaries as the only authority.
- [ ] Do not record API keys, private keys, cookies, seed phrases, credentials, or private account data.
- [ ] Do not move current facts into stable wiki pages until ticket evidence, audits, and package checks pass.
- [ ] Obtain explicit human confirmation before marking the ticket verified or unchanged.
- [ ] Keep the high-risk domain boundary visible in the final note and require manual acceptance.

## Commands

Run only dry-run imports until every placeholder is replaced.

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-001 --status pending --dry-run
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.jsonl --dry-run --no-post-checks
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-001 --status still-needs-source-update --source-title "<source title>" --source-publisher "<publisher>" --source-url-or-reference "<url or local reference>" --source-published-or-updated "YYYY-MM-DD | unknown" --evidence-summary "<what the source supports and does not support>" --confidence low --remaining-uncertainty "<remaining uncertainty>" --human-reviewer "<reviewer>"
```

## Safety Boundary

- This work order is an offline collection aid; it does not verify or certify current facts.
- It does not authorize real-money trading, final legal or medical advice, offensive security activity, wallet signing, or production changes.
- Keep `needs-source-update` in the wiki until authoritative source evidence is recorded and audits pass.
