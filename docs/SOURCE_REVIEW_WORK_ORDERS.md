# Source Review Work Orders

Generated: 2026-06-16

## Purpose

Convert ready source-review tickets into offline work orders for human or connected source reviewers without fetching or certifying facts.

## Summary

- Passed: yes
- Current-fact ready: no
- Source-review tickets: 35
- Ready for source collection: 13
- Selected finalized tickets: 0
- Selected verified tickets: 0
- Source review phase: pre-import-or-in-progress
- Work orders: 13
- Human review gates: 13
- Work order directory: [source-review-work-orders](../registry/source-review-work-orders)
- Work order manifest: [manifest.json](../registry/source-review-work-orders/manifest.json)

## Work Orders

| Work Order | Ticket | Wiki | Priority | Wave | Risk | Human Gate | Reviewer Role | Topic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [WORKORDER-TICKET-SRC-004](../registry/source-review-work-orders/TICKET-SRC-004.md) | `TICKET-SRC-004` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | yes | finance-risk-reviewer | current fees, funding rates, margin rules, tax rules and trading API parameters |
| [WORKORDER-TICKET-SRC-005](../registry/source-review-work-orders/TICKET-SRC-005.md) | `TICKET-SRC-005` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | yes | finance-risk-reviewer | current legal, regulatory or suitability requirements for financial products |
| [WORKORDER-TICKET-SRC-006](../registry/source-review-work-orders/TICKET-SRC-006.md) | `TICKET-SRC-006` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | yes | finance-risk-reviewer | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| [WORKORDER-TICKET-SRC-007](../registry/source-review-work-orders/TICKET-SRC-007.md) | `TICKET-SRC-007` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | yes | finance-risk-reviewer | latest financial statements, filings, restatements and audit opinions |
| [WORKORDER-TICKET-SRC-001](../registry/source-review-work-orders/TICKET-SRC-001.md) | `TICKET-SRC-001` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | yes | web3-wallet-safety-reviewer | current contract addresses, wallet warnings, scam reports and signing risks |
| [WORKORDER-TICKET-SRC-002](../registry/source-review-work-orders/TICKET-SRC-002.md) | `TICKET-SRC-002` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | yes | web3-wallet-safety-reviewer | current project status, official links, task rules, snapshot and eligibility |
| [WORKORDER-TICKET-SRC-003](../registry/source-review-work-orders/TICKET-SRC-003.md) | `TICKET-SRC-003` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | yes | web3-wallet-safety-reviewer | current token launch, TGE, funding, exchange listing and airdrop allocation |
| [WORKORDER-TICKET-SRC-008](../registry/source-review-work-orders/TICKET-SRC-008.md) | `TICKET-SRC-008` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | high | yes | clinical-safety-reviewer | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| [WORKORDER-TICKET-SRC-009](../registry/source-review-work-orders/TICKET-SRC-009.md) | `TICKET-SRC-009` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | high | yes | clinical-safety-reviewer | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| [WORKORDER-TICKET-SRC-010](../registry/source-review-work-orders/TICKET-SRC-010.md) | `TICKET-SRC-010` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | high | yes | legal-counsel-reviewer | current platform agreements, data processing terms and consumer protection rules |
| [WORKORDER-TICKET-SRC-011](../registry/source-review-work-orders/TICKET-SRC-011.md) | `TICKET-SRC-011` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | high | yes | legal-counsel-reviewer | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements |
| [WORKORDER-TICKET-SRC-012](../registry/source-review-work-orders/TICKET-SRC-012.md) | `TICKET-SRC-012` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | high | yes | defensive-security-reviewer | current CVEs, vendor advisories, patches, dependency versions and exploit status |
| [WORKORDER-TICKET-SRC-013](../registry/source-review-work-orders/TICKET-SRC-013.md) | `TICKET-SRC-013` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | high | yes | defensive-security-reviewer | current security tool rules, detection signatures, cloud defaults and compliance requirements |

## Wiki Counts

- airdrop-agent-wiki: 3
- finance-agent-wiki: 4
- health-agent-wiki: 2
- legal-agent-wiki: 2
- security-agent-wiki: 2

## Reviewer Role Counts

- clinical-safety-reviewer: 2
- defensive-security-reviewer: 2
- finance-risk-reviewer: 4
- legal-counsel-reviewer: 2
- web3-wallet-safety-reviewer: 3

## Commands

```bash
python3 scripts/audit_source_review_packets.py
python3 scripts/rehearse_source_review_packet_imports.py
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks
python3 scripts/audit_source_refresh_completion.py
python3 scripts/audit_source_evidence_quality.py
python3 scripts/generate_source_review_readiness_matrix.py
python3 scripts/generate_source_review_work_orders.py
python3 scripts/generate_source_refresh_dashboard.py
python3 scripts/run_acceptance.py
```

## Related Reports

- source_refresh_dashboard: [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- source_review_readiness_matrix: [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- source_review_packet_bundle: [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- source_review_packet_audit: [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- source_review_packet_rehearsal: [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- source_review_session_plan: [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- source_reviewer_queue: [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- source_evidence_packet_importer: [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- source_refresh_completion: [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- source_evidence_quality: [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| required local review artifacts exist | PASS | all required artifacts present |
| readiness matrix passed | PASS | 13 ready rows |
| ready tickets have reviewer cards | PASS | 13/13 work orders |
| ready tickets have packet entries | PASS | 13/13 work orders |
| work order files written | PASS | 13 work order files plus manifest |
| human gates preserved | PASS | 13 human-gated work orders |
| current facts remain gated | PASS | current_fact_ready=false while source tickets remain open |

## Safety Boundary

- Work orders are collection templates only; they do not fetch, verify, or certify external facts.
- Zero work orders is acceptable when the selected review tickets are already finalized after evidence import.
- Keep current facts gated until evidence is recorded, human gates are satisfied, and audits pass.
- Do not use these files to store secrets, credentials, cookies, private keys, seed phrases, or private account data.
