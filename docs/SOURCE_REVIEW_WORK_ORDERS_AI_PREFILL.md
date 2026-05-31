# Source Review Work Orders — AI Prefill Report

Generated: 2026-05-28

## What this package is

This is an AI-assisted evidence prefill for the 13 wave-1 source review work orders. It collects authoritative or official source references and fills the evidence fields so a human reviewer can perform the required authority, scope, recency, conflict, and acceptance checks.

## What this package is not

- It is not a certification that current facts are ready.
- It does not remove `needs-source-update`.
- It does not write current facts into stable wiki pages.
- It is not legal, medical, financial, tax, trading, security, or Web3 participation advice.

## Status

- Tickets covered: 13 / 13
- Evidence entries: 66
- Entry status: `still-needs-source-update` for every entry
- Human review gate: required for every ticket
- current_fact_ready: false

## Ticket counts

| Ticket | Wiki | Priority | Topic | Evidence entries | Status |
| --- | --- | --- | --- | ---: | --- |
| `TICKET-SRC-001` | `airdrop-agent-wiki` | `P1` | current contract addresses, wallet warnings, scam reports and signing risks | 5 | still-needs-source-update |
| `TICKET-SRC-002` | `airdrop-agent-wiki` | `P1` | current project status, official links, task rules, snapshot and eligibility | 4 | still-needs-source-update |
| `TICKET-SRC-003` | `airdrop-agent-wiki` | `P1` | current token launch, TGE, funding, exchange listing and airdrop allocation | 5 | still-needs-source-update |
| `TICKET-SRC-004` | `finance-agent-wiki` | `P0` | current fees, funding rates, margin rules, tax rules and trading API parameters | 6 | still-needs-source-update |
| `TICKET-SRC-005` | `finance-agent-wiki` | `P0` | current legal, regulatory or suitability requirements for financial products | 5 | still-needs-source-update |
| `TICKET-SRC-006` | `finance-agent-wiki` | `P0` | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity | 5 | still-needs-source-update |
| `TICKET-SRC-007` | `finance-agent-wiki` | `P0` | latest financial statements, filings, restatements and audit opinions | 5 | still-needs-source-update |
| `TICKET-SRC-008` | `health-agent-wiki` | `P2` | current clinical guidelines, drug labels, dosage, contraindications and safety warnings | 4 | still-needs-source-update |
| `TICKET-SRC-009` | `health-agent-wiki` | `P2` | current public health guidance, screening recommendations and nutrition/exercise guidelines | 5 | still-needs-source-update |
| `TICKET-SRC-010` | `legal-agent-wiki` | `P2` | current platform agreements, data processing terms and consumer protection rules | 6 | still-needs-source-update |
| `TICKET-SRC-011` | `legal-agent-wiki` | `P2` | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements | 5 | still-needs-source-update |
| `TICKET-SRC-012` | `security-agent-wiki` | `P2` | current CVEs, vendor advisories, patches, dependency versions and exploit status | 5 | still-needs-source-update |
| `TICKET-SRC-013` | `security-agent-wiki` | `P2` | current security tool rules, detection signatures, cloud defaults and compliance requirements | 6 | still-needs-source-update |

## Recommended next commands

Run these in your repository after copying the packet into the expected `registry/source-review-packets/` path. Keep imports dry-run until human review is complete.

```bash
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-ai-prefill.json --dry-run --no-post-checks
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl --dry-run --no-post-checks
python3 scripts/audit_source_evidence_quality.py
python3 scripts/audit_source_refresh_completion.py
python3 scripts/run_acceptance.py
```

## Human-review focus

1. Finance tickets require exact product, venue, account type, tax jurisdiction, and API version checks.
2. Airdrop tickets are project-specific; historical examples are not current eligibility. Never treat this packet as instructions to participate.
3. Health tickets require clinician review before any patient-facing use.
4. Legal tickets require jurisdiction-specific lawyer review before legal conclusions.
5. Security tickets require environment-specific validation, patch testing, and defensive-use review before production changes.
