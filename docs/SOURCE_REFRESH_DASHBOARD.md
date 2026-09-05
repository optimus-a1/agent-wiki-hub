# Source Refresh Dashboard

Generated: 2026-09-05

## Summary

- Release ready for internal use: yes
- Current-fact ready: no
- Requires source update for current facts: yes
- Source-update topics: 35
- Source-refresh tasks: 35
- Source-refresh tickets: 35
- Source reviewer queue: 35 open reviews, 16 human gates
- Source review session plan: 25 selected reviews, 16 human gates
- Source review packet bundle: 25 pending entries
- Source review packet audit: 2 packets, 0 issues
- Source review packet rehearsal: 2/2 dry-runs passed
- Source review readiness matrix: 25 ready, 10 queued
- Source review work orders: 25 work orders, 16 human gates
- Open tickets: 35
- Verified tickets: 0
- Evidence entries: 13
- Evidence quality issues: 0

## Quick Links

- source_update_queue: [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- source_refresh_playbook: [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- source_refresh_tickets: [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- source_refresh_wave_runner: [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- source_reviewer_queue: [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- source_review_session_plan: [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- source_review_readiness_matrix: [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- source_review_work_orders: [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- source_review_packet_bundle: [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- source_review_packet_audit: [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- source_review_packet_rehearsal: [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- source_evidence_recorder: [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- source_evidence_packet_importer: [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- source_evidence_packet_fixtures: [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- source_refresh_completion: [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- source_evidence_quality: [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)
- source_refresh_log_status: [SOURCE_REFRESH_LOG_STATUS.md](../docs/SOURCE_REFRESH_LOG_STATUS.md)
- safety_audit: [SAFETY_AUDIT.md](../docs/SAFETY_AUDIT.md)
- acceptance: [ACCEPTANCE_REPORT.md](../docs/ACCEPTANCE_REPORT.md)
- release_notes: [RELEASE_NOTES.md](../docs/RELEASE_NOTES.md)

## Readiness Gates

| Gate | Result | Detail |
| --- | --- | --- |
| source tickets generated | PASS | 35 tickets |
| source refresh logs ready | PASS | 12 wiki logs |
| completion audit structurally passed | PASS | 35 open, 0 verified |
| evidence quality passed | PASS | 13 entries, 0 issues |
| source reviewer queue generated | PASS | reviewer roles and human gates assigned |
| source review session plan generated | PASS | next source-review session selected |
| source review packet bundle generated | PASS | pending packet templates ready for dry-run import |
| source review packet audit passed | PASS | packet templates checked before import |
| source review packet rehearsal passed | PASS | packet templates dry-run through importer |
| source review readiness matrix generated | PASS | per-ticket readiness summarized |
| source review work orders generated | PASS | ready tickets have offline work orders |
| current-fact completion ready | OPEN | requires all tickets finalized before current-fact use |
| safety audit passed | PASS | high-risk boundaries checked |
| acceptance passed | PASS | full local acceptance suite |
| package audit passed | PASS | zip package integrity |
| link audit passed | PASS | local references checked |

## Priority Progress

| Priority | Tickets | Open | Finalized | Verified | Issues |
| --- | ---: | ---: | ---: | ---: | ---: |
| P0 | 15 | 15 | 0 | 0 | 0 |
| P1 | 12 | 12 | 0 | 0 | 0 |
| P2 | 8 | 8 | 0 | 0 | 0 |

## Wave Progress

| Wave | Tickets | Open | Finalized | Verified | Human Confirmation |
| --- | ---: | ---: | ---: | ---: | ---: |
| wave-1 | 25 | 25 | 0 | 0 | 16 |
| wave-2 | 7 | 7 | 0 | 0 | 0 |
| wave-3 | 3 | 3 | 0 | 0 | 0 |

## Wiki Progress

| Wiki | Priority | Risk | Freshness | Tickets | Open | Finalized | Verified | Human Confirmation | Issues |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| agent-engineering-wiki | P0 | medium | medium | 3 | 3 | 0 | 0 | 0 | 0 |
| coding-agent-wiki | P0 | medium | medium | 4 | 4 | 0 | 0 | 0 | 0 |
| customs-agent-wiki | P0 | medium | high | 4 | 4 | 0 | 0 | 0 | 0 |
| finance-agent-wiki | P0 | high | high | 4 | 4 | 0 | 0 | 4 | 0 |
| airdrop-agent-wiki | P1 | high | high | 3 | 3 | 0 | 0 | 3 | 0 |
| content-agent-wiki | P1 | low | medium | 3 | 3 | 0 | 0 | 0 | 0 |
| ecommerce-agent-wiki | P1 | medium | high | 3 | 3 | 0 | 0 | 0 | 0 |
| nodeops-agent-wiki | P1 | high | medium | 3 | 3 | 0 | 0 | 3 | 0 |
| health-agent-wiki | P2 | high | high | 2 | 2 | 0 | 0 | 2 | 0 |
| legal-agent-wiki | P2 | high | high | 2 | 2 | 0 | 0 | 2 | 0 |
| research-agent-wiki | P2 | medium | high | 2 | 2 | 0 | 0 | 0 | 0 |
| security-agent-wiki | P2 | high | high | 2 | 2 | 0 | 0 | 2 | 0 |

## Top Open Tickets

| Ticket | Wave | Wiki | Priority | Topic | Log |
| --- | --- | --- | ---: | --- | --- |
| TICKET-SRC-001 | wave-1 | airdrop-agent-wiki | 9 | current contract addresses, wallet warnings, scam reports and signing risks | [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-002 | wave-1 | airdrop-agent-wiki | 9 | current project status, official links, task rules, snapshot and eligibility | [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-003 | wave-1 | airdrop-agent-wiki | 9 | current token launch, TGE, funding, exchange listing and airdrop allocation | [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-004 | wave-1 | finance-agent-wiki | 9 | current fees, funding rates, margin rules, tax rules and trading API parameters | [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-005 | wave-1 | finance-agent-wiki | 9 | current legal, regulatory or suitability requirements for financial products | [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-006 | wave-1 | finance-agent-wiki | 9 | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity | [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-007 | wave-1 | finance-agent-wiki | 9 | latest financial statements, filings, restatements and audit opinions | [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-008 | wave-1 | health-agent-wiki | 9 | current clinical guidelines, drug labels, dosage, contraindications and safety warnings | [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-009 | wave-1 | health-agent-wiki | 9 | current public health guidance, screening recommendations and nutrition/exercise guidelines | [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-010 | wave-1 | legal-agent-wiki | 9 | current platform agreements, data processing terms and consumer protection rules | [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-011 | wave-1 | legal-agent-wiki | 9 | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements | [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-012 | wave-1 | security-agent-wiki | 9 | current CVEs, vendor advisories, patches, dependency versions and exploit status | [source-refresh-log.md](../wikis/security-agent-wiki/sources/source-refresh-log.md) |

## Next Actions

- Refresh wave-1 tickets first, especially high-risk finance, legal, health, security, airdrop, and operations topics.
- Use `scripts/record_source_evidence.py` only after authoritative source evidence has been checked.
- Keep `still-needs-source-update` when sources are missing, stale, conflicting, or outside scope.
- Run completion and quality audits after recording evidence.
- Do not write current facts into wiki pages until the relevant ticket has dated evidence.

## Commands

```bash
python3 scripts/generate_source_refresh_dashboard.py
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run
python3 scripts/audit_source_refresh_completion.py
python3 scripts/audit_source_evidence_quality.py
python3 scripts/run_acceptance.py
```
