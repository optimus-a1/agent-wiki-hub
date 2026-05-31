# Source Review Wave 2 Plan

Generated: 2026-05-31

## Purpose

Plan source-review work orders for one source-refresh wave without browsing, verifying, importing, or writing current facts.

## Inputs Read

- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [source-refresh-dashboard.json](../registry/source-refresh-dashboard.json)

## Guardrails

- This plan does not browse, verify, certify, or write current facts.
- All entries remain planning-only until authoritative evidence is recorded.
- High-risk tickets require named human confirmation before final status.
- Node operations tickets do not authorize production changes, wallet actions, live upgrades, firewall changes, or billing-sensitive operations.

## Summary

- Passed: yes
- Current-fact ready: no
- Current facts written by this plan: no
- Remaining open topics: 35
- Selected wave: wave-2
- Planned work orders: 12
- High-risk work orders: 3
- Human confirmation gates: 3

## Remaining Open Source Update Topics

| Ticket | Wave | Wiki | Priority | Score | Risk | Human Gate | Status | Topic |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| `TICKET-SRC-004` | wave-1 | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | 8 | high | yes | pending | current fees, funding rates, margin rules, tax rules and trading API parameters |
| `TICKET-SRC-005` | wave-1 | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | 8 | high | yes | pending | current legal, regulatory or suitability requirements for financial products |
| `TICKET-SRC-006` | wave-1 | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | 8 | high | yes | pending | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| `TICKET-SRC-007` | wave-1 | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | 8 | high | yes | pending | latest financial statements, filings, restatements and audit opinions |
| `TICKET-SRC-001` | wave-1 | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | 8 | high | yes | pending | current contract addresses, wallet warnings, scam reports and signing risks |
| `TICKET-SRC-002` | wave-1 | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | 8 | high | yes | pending | current project status, official links, task rules, snapshot and eligibility |
| `TICKET-SRC-003` | wave-1 | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | 8 | high | yes | pending | current token launch, TGE, funding, exchange listing and airdrop allocation |
| `TICKET-SRC-021` | wave-2 | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | 7 | high | yes | open_pending_source_refresh | current OS package, Docker, systemd and kernel behavior |
| `TICKET-SRC-022` | wave-2 | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | 7 | high | yes | open_pending_source_refresh | current blockchain node client versions, network parameters and upgrade requirements |
| `TICKET-SRC-023` | wave-2 | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | 7 | high | yes | open_pending_source_refresh | current cloud provider limits, firewall behavior, billing and incident status |
| `TICKET-SRC-008` | wave-1 | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | 8 | high | yes | pending | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| `TICKET-SRC-009` | wave-1 | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | 8 | high | yes | pending | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| `TICKET-SRC-010` | wave-1 | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | 8 | high | yes | pending | current platform agreements, data processing terms and consumer protection rules |
| `TICKET-SRC-011` | wave-1 | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | 8 | high | yes | pending | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements |
| `TICKET-SRC-012` | wave-1 | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | 8 | high | yes | pending | current CVEs, vendor advisories, patches, dependency versions and exploit status |
| `TICKET-SRC-013` | wave-1 | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | 8 | high | yes | pending | current security tool rules, detection signatures, cloud defaults and compliance requirements |
| `TICKET-SRC-014` | wave-2 | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | 7 | medium | no | open_pending_source_refresh | exchange rates, tariff rates, tax rates and destination-specific fees |
| `TICKET-SRC-015` | wave-2 | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | 7 | medium | no | open_pending_source_refresh | latest HS codes, customs supervision conditions and declaration elements |
| `TICKET-SRC-016` | wave-2 | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | 7 | medium | no | open_pending_source_refresh | latest import/export policy, inspection and quarantine requirements |
| `TICKET-SRC-017` | wave-2 | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | 7 | medium | no | open_pending_source_refresh | latest platform OCR model parameters and document template behavior |
| `TICKET-SRC-026` | wave-3 | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | 6 | medium | no | open_pending_source_refresh | current Codex Skill format, plugin behavior and tool capabilities |
| `TICKET-SRC-027` | wave-3 | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | 6 | medium | no | open_pending_source_refresh | current RAG frameworks, embedding models, vector databases and rerankers |
| `TICKET-SRC-028` | wave-3 | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | 6 | medium | no | open_pending_source_refresh | current eval harnesses, model APIs and MCP/tool schemas |
| `TICKET-SRC-029` | wave-3 | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | 6 | medium | no | open_pending_source_refresh | current OpenAI, Codex, GitHub or Vercel product behavior |
| `TICKET-SRC-030` | wave-3 | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | 6 | medium | no | open_pending_source_refresh | current cloud platform build, deploy, runtime and pricing behavior |
| `TICKET-SRC-031` | wave-3 | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | 6 | medium | no | open_pending_source_refresh | current dependency vulnerabilities and security advisories |
| `TICKET-SRC-032` | wave-3 | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | 6 | medium | no | open_pending_source_refresh | current framework, library, CLI and API parameters |
| `TICKET-SRC-018` | wave-2 | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | 7 | medium | no | open_pending_source_refresh | current marketplace policy, return window, category restrictions and consumer protection rules |
| `TICKET-SRC-019` | wave-2 | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | 7 | medium | no | open_pending_source_refresh | current product certification, recall, safety notice and warranty terms |
| `TICKET-SRC-020` | wave-2 | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | 7 | medium | no | open_pending_source_refresh | current product price, stock, promotion, shipping fee and delivery ETA |
| `TICKET-SRC-024` | wave-2 | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | 7 | medium | no | open_pending_source_refresh | current dataset availability, license, model weights and code repository status |
| `TICKET-SRC-025` | wave-2 | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | 7 | medium | no | open_pending_source_refresh | latest papers, preprints, revisions, citations and benchmark leaderboards |
| `TICKET-SRC-033` | wave-3 | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | 5 | low | no | open_pending_source_refresh | current image, chart, dataset and quote licensing |
| `TICKET-SRC-034` | wave-3 | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | 5 | low | no | open_pending_source_refresh | current news, statistics, public quotes and social media claims |
| `TICKET-SRC-035` | wave-3 | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | 5 | low | no | open_pending_source_refresh | current publishing platform rules, format limits and content policies |

## Wave 2 Work Order Plan

Sorted by risk first, then wiki priority and priority score. These are planning records only.

| Rank | Work Order | Ticket | Wiki | Priority | Score | Risk | Reviewer | Human Gate | Topic |
| ---: | --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| 1 | `WAVE2-WORKORDER-TICKET-SRC-021` | `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | 7 | high | `operations-change-reviewer` | yes | current OS package, Docker, systemd and kernel behavior |
| 2 | `WAVE2-WORKORDER-TICKET-SRC-022` | `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | 7 | high | `operations-change-reviewer` | yes | current blockchain node client versions, network parameters and upgrade requirements |
| 3 | `WAVE2-WORKORDER-TICKET-SRC-023` | `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | 7 | high | `operations-change-reviewer` | yes | current cloud provider limits, firewall behavior, billing and incident status |
| 4 | `WAVE2-WORKORDER-TICKET-SRC-014` | `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | 7 | medium | `customs-document-reviewer` | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| 5 | `WAVE2-WORKORDER-TICKET-SRC-015` | `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | 7 | medium | `customs-document-reviewer` | no | latest HS codes, customs supervision conditions and declaration elements |
| 6 | `WAVE2-WORKORDER-TICKET-SRC-016` | `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | 7 | medium | `customs-document-reviewer` | no | latest import/export policy, inspection and quarantine requirements |
| 7 | `WAVE2-WORKORDER-TICKET-SRC-017` | `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | 7 | medium | `customs-document-reviewer` | no | latest platform OCR model parameters and document template behavior |
| 8 | `WAVE2-WORKORDER-TICKET-SRC-018` | `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | 7 | medium | `ecommerce-policy-reviewer` | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| 9 | `WAVE2-WORKORDER-TICKET-SRC-019` | `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | 7 | medium | `ecommerce-policy-reviewer` | no | current product certification, recall, safety notice and warranty terms |
| 10 | `WAVE2-WORKORDER-TICKET-SRC-020` | `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | 7 | medium | `ecommerce-policy-reviewer` | no | current product price, stock, promotion, shipping fee and delivery ETA |
| 11 | `WAVE2-WORKORDER-TICKET-SRC-024` | `TICKET-SRC-024` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | 7 | medium | `research-methods-reviewer` | no | current dataset availability, license, model weights and code repository status |
| 12 | `WAVE2-WORKORDER-TICKET-SRC-025` | `TICKET-SRC-025` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | 7 | medium | `research-methods-reviewer` | no | latest papers, preprints, revisions, citations and benchmark leaderboards |

## Reviewer Workload

| Reviewer Role | Work Orders | High Risk | Human Gates | Tickets |
| --- | ---: | ---: | ---: | --- |
| `customs-document-reviewer` | 4 | 0 | 0 | `TICKET-SRC-014`, `TICKET-SRC-015`, `TICKET-SRC-016`, `TICKET-SRC-017` |
| `ecommerce-policy-reviewer` | 3 | 0 | 0 | `TICKET-SRC-018`, `TICKET-SRC-019`, `TICKET-SRC-020` |
| `operations-change-reviewer` | 3 | 3 | 3 | `TICKET-SRC-021`, `TICKET-SRC-022`, `TICKET-SRC-023` |
| `research-methods-reviewer` | 2 | 0 | 0 | `TICKET-SRC-024`, `TICKET-SRC-025` |

## Preflight Checklist

- [ ] Read root AGENTS.md and the target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.
- [ ] Confirm the ticket topic and scope before opening or recording any source.
- [ ] Use official, primary, dated sources whenever available.
- [ ] Record source title, publisher, URL or local reference, publication/update date, access date, confidence, and remaining uncertainty.
- [ ] Keep status pending or still-needs-source-update when evidence is missing, stale, conflicting, or out of scope.
- [ ] Do not write current facts into wiki pages from this plan.
- [ ] Do not record API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.

## Per-Ticket Source Targets

### 1. TICKET-SRC-021 - nodeops-agent-wiki

- Risk: high
- Reviewer role: `operations-change-reviewer`
- Human confirmation: yes
- Topic: current OS package, Docker, systemd and kernel behavior
- Suggested source types: official documentation, local version output, release notes
- Source notes: [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-021 --status pending --dry-run`

### 2. TICKET-SRC-022 - nodeops-agent-wiki

- Risk: high
- Reviewer role: `operations-change-reviewer`
- Human confirmation: yes
- Topic: current blockchain node client versions, network parameters and upgrade requirements
- Suggested source types: official client release notes, chain foundation announcement, node logs and version output
- Source notes: [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-022 --status pending --dry-run`

### 3. TICKET-SRC-023 - nodeops-agent-wiki

- Risk: high
- Reviewer role: `operations-change-reviewer`
- Human confirmation: yes
- Topic: current cloud provider limits, firewall behavior, billing and incident status
- Suggested source types: cloud provider documentation, status page, account console
- Source notes: [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-023 --status pending --dry-run`

### 4. TICKET-SRC-014 - customs-agent-wiki

- Risk: medium
- Reviewer role: `customs-document-reviewer`
- Human confirmation: no
- Topic: exchange rates, tariff rates, tax rates and destination-specific fees
- Suggested source types: central bank or official exchange source, customs tariff system, destination country authority
- Source notes: [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-014 --status pending --dry-run`

### 5. TICKET-SRC-015 - customs-agent-wiki

- Risk: medium
- Reviewer role: `customs-document-reviewer`
- Human confirmation: no
- Topic: latest HS codes, customs supervision conditions and declaration elements
- Suggested source types: customs authority website, official tariff database, licensed customs broker review
- Source notes: [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-015 --status pending --dry-run`

### 6. TICKET-SRC-016 - customs-agent-wiki

- Risk: medium
- Reviewer role: `customs-document-reviewer`
- Human confirmation: no
- Topic: latest import/export policy, inspection and quarantine requirements
- Suggested source types: customs and inspection authority announcement, destination country regulator, official trade compliance bulletin
- Source notes: [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-016 --status pending --dry-run`

### 7. TICKET-SRC-017 - customs-agent-wiki

- Risk: medium
- Reviewer role: `customs-document-reviewer`
- Human confirmation: no
- Topic: latest platform OCR model parameters and document template behavior
- Suggested source types: OCR vendor documentation, internal extraction benchmark, manually reviewed sample set
- Source notes: [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-017 --status pending --dry-run`

### 8. TICKET-SRC-018 - ecommerce-agent-wiki

- Risk: medium
- Reviewer role: `ecommerce-policy-reviewer`
- Human confirmation: no
- Topic: current marketplace policy, return window, category restrictions and consumer protection rules
- Suggested source types: official marketplace policy center, consumer protection authority, merchant service agreement
- Source notes: [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-018 --status pending --dry-run`

### 9. TICKET-SRC-019 - ecommerce-agent-wiki

- Risk: medium
- Reviewer role: `ecommerce-policy-reviewer`
- Human confirmation: no
- Topic: current product certification, recall, safety notice and warranty terms
- Suggested source types: brand official website, regulator recall database, warranty document
- Source notes: [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-019 --status pending --dry-run`

### 10. TICKET-SRC-020 - ecommerce-agent-wiki

- Risk: medium
- Reviewer role: `ecommerce-policy-reviewer`
- Human confirmation: no
- Topic: current product price, stock, promotion, shipping fee and delivery ETA
- Suggested source types: platform product page, merchant backend, carrier tracking system
- Source notes: [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-020 --status pending --dry-run`

### 11. TICKET-SRC-024 - research-agent-wiki

- Risk: medium
- Reviewer role: `research-methods-reviewer`
- Human confirmation: no
- Topic: current dataset availability, license, model weights and code repository status
- Suggested source types: official dataset page, repository release notes, model card
- Source notes: [source-notes.md](../wikis/research-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/research-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-024 --status pending --dry-run`

### 12. TICKET-SRC-025 - research-agent-wiki

- Risk: medium
- Reviewer role: `research-methods-reviewer`
- Human confirmation: no
- Topic: latest papers, preprints, revisions, citations and benchmark leaderboards
- Suggested source types: publisher page, arXiv or conference page, official benchmark leaderboard
- Source notes: [source-notes.md](../wikis/research-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/research-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-025 --status pending --dry-run`

## Packet Skeleton

This is placeholder-only. Replace every placeholder before any real import.

```json
{
  "packet_id": "source-review-session-wave-2-pending",
  "created_on": "2026-05-31",
  "created_by": "<human reviewer or source-refresh agent>",
  "dry_run_first": true,
  "entries": [
    {
      "ticket_id": "TICKET-SRC-021",
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
    },
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
    },
    {
      "ticket_id": "TICKET-SRC-023",
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
  ],
  "truncated_entries": 9
}
```

## Next Commands

```bash
python scripts/generate_source_review_packet_bundle.py --session-plan registry/source-review-wave-2-plan.json --stem source-review-session-wave-2-pending
python scripts/audit_source_review_packets.py
python scripts/rehearse_source_review_packet_imports.py
python scripts/audit_source_refresh_completion.py
python scripts/audit_source_evidence_quality.py
python scripts/run_acceptance.py
```

## Related Reports

- source_refresh_dashboard: [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- source_review_readiness_matrix: [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- source_refresh_dashboard_json: [source-refresh-dashboard.json](../registry/source-refresh-dashboard.json)
- source_reviewer_queue: [source-reviewer-queue.json](../registry/source-reviewer-queue.json)
- source_refresh_tickets: [source-refresh-tickets.json](../registry/source-refresh-tickets.json)
- source_evidence_packet_importer: [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- source_review_packet_bundle: [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| required dashboard artifacts exist | PASS | registry/source-refresh-dashboard.json, registry/source-review-readiness-matrix.json |
| open topics loaded | PASS | 35 open topics |
| wave-2 topics selected | PASS | 12 planned work orders |
| reviewer cards available for selected topics | PASS | 12/12 reviewer roles |
| current facts remain gated | PASS | current_fact_ready=false; plan writes no current facts |
