# Source Review Session Plan

Generated: 2026-09-05

## Purpose

Turn reviewer-queue cards into a concrete source-review session plan without fetching or certifying external facts.

## Current State

- Current-fact ready: no
- Open reviews: 35
- Selected reviews: 25
- Selected high-risk reviews: 16
- Selected human review gates: 16
- Filters: `{"wave": "wave-1", "priority": null, "wiki": null, "reviewer_role": null, "human_only": false, "all_open": false, "limit": null, "default_session": true}`

## Preflight Checklist

- [ ] Read root AGENTS.md and the target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.
- [ ] Confirm the selected ticket scope before opening external sources.
- [ ] Use official, primary, dated sources whenever available.
- [ ] Record source title, publisher, URL or reference, publication/update date, access date, confidence, and remaining uncertainty.
- [ ] Keep human-review-gated tickets open until a human reviewer is named in the evidence log.
- [ ] Do not record API keys, private keys, cookies, seed phrases, credentials, or private account data.
- [ ] Use still-needs-source-update when source evidence is missing, stale, conflicting, or out of scope.

## Selected Reviews

| Review | Ticket | Wiki | Priority | Wave | Risk | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REVIEW-SRC-001` | `TICKET-SRC-004` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | finance-risk-reviewer | yes | current fees, funding rates, margin rules, tax rules and trading API parameters |
| `REVIEW-SRC-002` | `TICKET-SRC-005` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | finance-risk-reviewer | yes | current legal, regulatory or suitability requirements for financial products |
| `REVIEW-SRC-003` | `TICKET-SRC-006` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | finance-risk-reviewer | yes | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| `REVIEW-SRC-004` | `TICKET-SRC-007` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | finance-risk-reviewer | yes | latest financial statements, filings, restatements and audit opinions |
| `REVIEW-SRC-005` | `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-1 | medium | customs-document-reviewer | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| `REVIEW-SRC-006` | `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-1 | medium | customs-document-reviewer | no | latest HS codes, customs supervision conditions and declaration elements |
| `REVIEW-SRC-007` | `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-1 | medium | customs-document-reviewer | no | latest import/export policy, inspection and quarantine requirements |
| `REVIEW-SRC-008` | `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-1 | medium | customs-document-reviewer | no | latest platform OCR model parameters and document template behavior |
| `REVIEW-SRC-015` | `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-1 | high | operations-change-reviewer | yes | current OS package, Docker, systemd and kernel behavior |
| `REVIEW-SRC-016` | `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-1 | high | operations-change-reviewer | yes | current blockchain node client versions, network parameters and upgrade requirements |
| `REVIEW-SRC-017` | `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-1 | high | operations-change-reviewer | yes | current cloud provider limits, firewall behavior, billing and incident status |
| `REVIEW-SRC-009` | `TICKET-SRC-001` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | web3-wallet-safety-reviewer | yes | current contract addresses, wallet warnings, scam reports and signing risks |
| `REVIEW-SRC-010` | `TICKET-SRC-002` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | web3-wallet-safety-reviewer | yes | current project status, official links, task rules, snapshot and eligibility |
| `REVIEW-SRC-011` | `TICKET-SRC-003` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | web3-wallet-safety-reviewer | yes | current token launch, TGE, funding, exchange listing and airdrop allocation |
| `REVIEW-SRC-012` | `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-1 | medium | ecommerce-policy-reviewer | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| `REVIEW-SRC-013` | `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-1 | medium | ecommerce-policy-reviewer | no | current product certification, recall, safety notice and warranty terms |
| `REVIEW-SRC-014` | `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-1 | medium | ecommerce-policy-reviewer | no | current product price, stock, promotion, shipping fee and delivery ETA |
| `REVIEW-SRC-018` | `TICKET-SRC-008` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | high | clinical-safety-reviewer | yes | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| `REVIEW-SRC-019` | `TICKET-SRC-009` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | high | clinical-safety-reviewer | yes | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| `REVIEW-SRC-022` | `TICKET-SRC-012` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | high | defensive-security-reviewer | yes | current CVEs, vendor advisories, patches, dependency versions and exploit status |
| `REVIEW-SRC-023` | `TICKET-SRC-013` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | high | defensive-security-reviewer | yes | current security tool rules, detection signatures, cloud defaults and compliance requirements |
| `REVIEW-SRC-020` | `TICKET-SRC-010` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | high | legal-counsel-reviewer | yes | current platform agreements, data processing terms and consumer protection rules |
| `REVIEW-SRC-021` | `TICKET-SRC-011` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | high | legal-counsel-reviewer | yes | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements |
| `REVIEW-SRC-024` | `TICKET-SRC-024` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | wave-1 | medium | research-methods-reviewer | no | current dataset availability, license, model weights and code repository status |
| `REVIEW-SRC-025` | `TICKET-SRC-025` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | wave-1 | medium | research-methods-reviewer | no | latest papers, preprints, revisions, citations and benchmark leaderboards |

## Role Workload

| Reviewer Role | Reviews | High Risk | Human Gates | Wikis |
| --- | ---: | ---: | ---: | --- |
| `clinical-safety-reviewer` | 2 | 2 | 2 | health-agent-wiki:2 |
| `customs-document-reviewer` | 4 | 0 | 0 | customs-agent-wiki:4 |
| `defensive-security-reviewer` | 2 | 2 | 2 | security-agent-wiki:2 |
| `ecommerce-policy-reviewer` | 3 | 0 | 0 | ecommerce-agent-wiki:3 |
| `finance-risk-reviewer` | 4 | 4 | 4 | finance-agent-wiki:4 |
| `legal-counsel-reviewer` | 2 | 2 | 2 | legal-agent-wiki:2 |
| `operations-change-reviewer` | 3 | 3 | 3 | nodeops-agent-wiki:3 |
| `research-methods-reviewer` | 2 | 0 | 0 | research-agent-wiki:2 |
| `web3-wallet-safety-reviewer` | 3 | 3 | 3 | airdrop-agent-wiki:3 |

## Session Steps

- Run the dry-run command for each selected review to confirm ticket and log wiring.
- Collect source evidence outside this script; this planner does not browse or verify facts.
- Record evidence with record_source_evidence.py or import_source_evidence_packet.py.
- Re-run completion, evidence quality, reviewer queue, session plan, dashboard, index, and acceptance.
- Only then consider whether any wiki page can move from needs-source-update to stable wording.

## Stop Conditions

- The source is not official, primary, dated, or clearly scoped to the ticket.
- Sources conflict and no authoritative resolution is available.
- A high-risk topic lacks human confirmation.
- A source requires credentials, private account data, cookies, tokens, or private keys.
- The evidence would enable unsafe finance, legal, medical, security, Web3, or production operations.

## Evidence Packet Skeleton

Use this only as a template. Replace every placeholder before a real import.

```json
{
  "packet_id": "source-review-session-2026-09-05",
  "created_on": "2026-09-05",
  "created_by": "<human reviewer or source-refresh agent>",
  "dry_run_first": true,
  "entries": [
    {
      "ticket_id": "TICKET-SRC-004",
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
    },
    {
      "ticket_id": "TICKET-SRC-005",
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
    },
    {
      "ticket_id": "TICKET-SRC-006",
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
    },
    {
      "ticket_id": "TICKET-SRC-007",
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
    },
    {
      "ticket_id": "TICKET-SRC-014",
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
  ],
  "truncated_entries": 20
}
```

## Per-Ticket Dry Runs

### REVIEW-SRC-001

- Ticket: `TICKET-SRC-004`
- Wiki: [finance-agent-wiki](../wikis/finance-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-004 --status pending --dry-run
```

### REVIEW-SRC-002

- Ticket: `TICKET-SRC-005`
- Wiki: [finance-agent-wiki](../wikis/finance-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-005 --status pending --dry-run
```

### REVIEW-SRC-003

- Ticket: `TICKET-SRC-006`
- Wiki: [finance-agent-wiki](../wikis/finance-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run
```

### REVIEW-SRC-004

- Ticket: `TICKET-SRC-007`
- Wiki: [finance-agent-wiki](../wikis/finance-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-007 --status pending --dry-run
```

### REVIEW-SRC-005

- Ticket: `TICKET-SRC-014`
- Wiki: [customs-agent-wiki](../wikis/customs-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-014 --status pending --dry-run
```

### REVIEW-SRC-006

- Ticket: `TICKET-SRC-015`
- Wiki: [customs-agent-wiki](../wikis/customs-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-015 --status pending --dry-run
```

### REVIEW-SRC-007

- Ticket: `TICKET-SRC-016`
- Wiki: [customs-agent-wiki](../wikis/customs-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-016 --status pending --dry-run
```

### REVIEW-SRC-008

- Ticket: `TICKET-SRC-017`
- Wiki: [customs-agent-wiki](../wikis/customs-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-017 --status pending --dry-run
```

### REVIEW-SRC-015

- Ticket: `TICKET-SRC-021`
- Wiki: [nodeops-agent-wiki](../wikis/nodeops-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-021 --status pending --dry-run
```

### REVIEW-SRC-016

- Ticket: `TICKET-SRC-022`
- Wiki: [nodeops-agent-wiki](../wikis/nodeops-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-022 --status pending --dry-run
```

### REVIEW-SRC-017

- Ticket: `TICKET-SRC-023`
- Wiki: [nodeops-agent-wiki](../wikis/nodeops-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-023 --status pending --dry-run
```

### REVIEW-SRC-009

- Ticket: `TICKET-SRC-001`
- Wiki: [airdrop-agent-wiki](../wikis/airdrop-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-001 --status pending --dry-run
```

### REVIEW-SRC-010

- Ticket: `TICKET-SRC-002`
- Wiki: [airdrop-agent-wiki](../wikis/airdrop-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-002 --status pending --dry-run
```

### REVIEW-SRC-011

- Ticket: `TICKET-SRC-003`
- Wiki: [airdrop-agent-wiki](../wikis/airdrop-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-003 --status pending --dry-run
```

### REVIEW-SRC-012

- Ticket: `TICKET-SRC-018`
- Wiki: [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-018 --status pending --dry-run
```

### REVIEW-SRC-013

- Ticket: `TICKET-SRC-019`
- Wiki: [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-019 --status pending --dry-run
```

### REVIEW-SRC-014

- Ticket: `TICKET-SRC-020`
- Wiki: [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-020 --status pending --dry-run
```

### REVIEW-SRC-018

- Ticket: `TICKET-SRC-008`
- Wiki: [health-agent-wiki](../wikis/health-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-008 --status pending --dry-run
```

### REVIEW-SRC-019

- Ticket: `TICKET-SRC-009`
- Wiki: [health-agent-wiki](../wikis/health-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-009 --status pending --dry-run
```

### REVIEW-SRC-022

- Ticket: `TICKET-SRC-012`
- Wiki: [security-agent-wiki](../wikis/security-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/security-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-012 --status pending --dry-run
```

### REVIEW-SRC-023

- Ticket: `TICKET-SRC-013`
- Wiki: [security-agent-wiki](../wikis/security-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/security-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-013 --status pending --dry-run
```

### REVIEW-SRC-020

- Ticket: `TICKET-SRC-010`
- Wiki: [legal-agent-wiki](../wikis/legal-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-010 --status pending --dry-run
```

### REVIEW-SRC-021

- Ticket: `TICKET-SRC-011`
- Wiki: [legal-agent-wiki](../wikis/legal-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-011 --status pending --dry-run
```

### REVIEW-SRC-024

- Ticket: `TICKET-SRC-024`
- Wiki: [research-agent-wiki](../wikis/research-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/research-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-024 --status pending --dry-run
```

### REVIEW-SRC-025

- Ticket: `TICKET-SRC-025`
- Wiki: [research-agent-wiki](../wikis/research-agent-wiki)
- Evidence log: [source-refresh-log.md](../wikis/research-agent-wiki/sources/source-refresh-log.md)

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-025 --status pending --dry-run
```

## Command Examples

```bash
python3 scripts/generate_source_review_session_plan.py
python3 scripts/generate_source_review_session_plan.py --wave wave-1 --limit 5
python3 scripts/generate_source_review_session_plan.py --reviewer-role finance-risk-reviewer --human-only
python3 scripts/generate_source_review_session_plan.py --wiki customs-agent-wiki --json
python3 scripts/generate_source_review_session_plan.py --all-open
```

## Post-Session Commands

```bash
python3 scripts/audit_source_refresh_completion.py
python3 scripts/audit_source_evidence_quality.py
python3 scripts/generate_source_refresh_wave_runner.py
python3 scripts/generate_source_reviewer_queue.py
python3 scripts/generate_source_review_session_plan.py
python3 scripts/generate_source_review_packet_bundle.py
python3 scripts/audit_source_review_packets.py
python3 scripts/rehearse_source_review_packet_imports.py
python3 scripts/generate_source_review_readiness_matrix.py
python3 scripts/generate_source_review_work_orders.py
python3 scripts/generate_source_refresh_dashboard.py
python3 scripts/update_index.py
python3 scripts/run_acceptance.py
```

## Related Reports

- source_refresh_dashboard: [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- source_refresh_wave_runner: [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- source_reviewer_queue: [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- source_review_readiness_matrix: [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- source_review_packet_bundle: [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- source_review_packet_audit: [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- source_review_packet_rehearsal: [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- source_evidence_recorder: [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- source_evidence_packet_importer: [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- source_evidence_packet_fixtures: [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- source_refresh_completion: [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- source_evidence_quality: [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| required reviewer artifacts exist | PASS | all required artifacts present |
| selected reviews available | PASS | 25 selected from 35 open reviews |
| selected reviews have reviewer roles and commands | PASS | reviewer role and dry-run command present for every selected review |
| current facts remain gated while tickets are open | PASS | current_fact_ready=false while open reviews remain |

## Safety Boundary

- This planner does not browse, verify, or certify current facts.
- It is safe to run offline because it only reorganizes existing open review cards and placeholder packet fields.
- Keep high-risk and human-gated tickets open until authoritative evidence and human confirmation are recorded.
