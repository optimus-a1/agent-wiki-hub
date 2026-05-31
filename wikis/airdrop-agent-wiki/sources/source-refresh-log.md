# Source Refresh Log

Wiki: airdrop-agent-wiki
Risk level: high
Freshness requirement: high
Template initialized: 2026-05-27

## Purpose

Record authoritative source verification work before current facts are written into this wiki.

## How To Use

1. Read `manifest.yaml`, `AGENTS.md`, `rules/`, and `sources/source-notes.md` first.
2. Pick a task from `docs/SOURCE_REFRESH_PLAYBOOK.md` or `registry/source-refresh-playbook.json`.
3. Verify the claim from authoritative sources before editing wiki content.
4. Record evidence below, including dates, source scope, confidence, and remaining uncertainty.
5. Update `sources/source-notes.md` and `update-log.md` after any content change.
6. Run validation and acceptance commands before release.

## Refresh Tasks

- [x] SRC-001 | wave: wave-1 | priority: 8 | human_confirmation: yes | topic: current contract addresses, wallet warnings, scam reports and signing risks
- [x] SRC-002 | wave: wave-1 | priority: 8 | human_confirmation: yes | topic: current project status, official links, task rules, snapshot and eligibility
- [x] SRC-003 | wave: wave-1 | priority: 8 | human_confirmation: yes | topic: current token launch, TGE, funding, exchange listing and airdrop allocation

## Evidence Entry Template

```yaml
- task_id: SRC-000
  topic: <copy topic from playbook>
  status: pending | verified | unchanged | still-needs-source-update | rejected
  verified_on: YYYY-MM-DD
  source_title: <source title>
  source_publisher: <official publisher or authority>
  source_url_or_reference: <URL or local reference>
  source_published_or_updated: YYYY-MM-DD | unknown
  source_accessed_on: YYYY-MM-DD
  evidence_summary: <short summary of what the source supports>
  affected_pages:
    - sources/source-notes.md
  confidence: low | medium | high
  remaining_uncertainty: <what is still unknown or scope-limited>
  human_reviewer: <name/role or required>
  follow_up: <next action or none>
```

## Completed Entries

- task_id: SRC-003
  ticket_id: TICKET-SRC-003
  topic: "current token launch, TGE, funding, exchange listing and airdrop allocation"
  status: pending
  verified_on: 2026-05-28
  source_title: "<source title>"
  source_publisher: "<official publisher or authority>"
  source_url_or_reference: "<URL or local reference>"
  source_published_or_updated: "YYYY-MM-DD | unknown"
  source_accessed_on: 2026-05-28
  evidence_summary: "<what the source supports and does not support>"
  affected_pages:
    - wikis/airdrop-agent-wiki/sources/source-notes.md
  confidence: low
  remaining_uncertainty: "<remaining uncertainty>"
  human_reviewer: "<reviewer>"
  follow_up: "Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed."
- task_id: SRC-002
  ticket_id: TICKET-SRC-002
  topic: "current project status, official links, task rules, snapshot and eligibility"
  status: pending
  verified_on: 2026-05-28
  source_title: "<source title>"
  source_publisher: "<official publisher or authority>"
  source_url_or_reference: "<URL or local reference>"
  source_published_or_updated: "YYYY-MM-DD | unknown"
  source_accessed_on: 2026-05-28
  evidence_summary: "<what the source supports and does not support>"
  affected_pages:
    - wikis/airdrop-agent-wiki/sources/source-notes.md
  confidence: low
  remaining_uncertainty: "<remaining uncertainty>"
  human_reviewer: "<reviewer>"
  follow_up: "Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed."
- task_id: SRC-001
  ticket_id: TICKET-SRC-001
  topic: "current contract addresses, wallet warnings, scam reports and signing risks"
  status: pending
  verified_on: 2026-05-28
  source_title: "<source title>"
  source_publisher: "<official publisher or authority>"
  source_url_or_reference: "<URL or local reference>"
  source_published_or_updated: "YYYY-MM-DD | unknown"
  source_accessed_on: 2026-05-28
  evidence_summary: "<what the source supports and does not support>"
  affected_pages:
    - wikis/airdrop-agent-wiki/sources/source-notes.md
  confidence: low
  remaining_uncertainty: "<remaining uncertainty>"
  human_reviewer: "<reviewer>"
  follow_up: "Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed."
## Safety Notes

- Do not write current facts into wiki pages without dated source evidence.
- Keep `needs-source-update` when sources are missing, conflicting, stale, or outside scope.
- High-risk domains keep human confirmation points even after source refresh is complete.
- Do not add personalized investment advice, final legal opinions, medical diagnoses, offensive security procedures, or platform-rule bypass guidance.
