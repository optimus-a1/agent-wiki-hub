# Source Review Wave 3 Plan

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
- Selected wave: wave-3
- Planned work orders: 10
- High-risk work orders: 0
- Human confirmation gates: 0

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

## Wave 3 Work Order Plan

Sorted by risk first, then wiki priority and priority score. These are planning records only.

| Rank | Work Order | Ticket | Wiki | Priority | Score | Risk | Reviewer | Human Gate | Topic |
| ---: | --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| 1 | `WAVE3-WORKORDER-TICKET-SRC-026` | `TICKET-SRC-026` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | 6 | medium | `agent-engineering-reviewer` | no | current Codex Skill format, plugin behavior and tool capabilities |
| 2 | `WAVE3-WORKORDER-TICKET-SRC-027` | `TICKET-SRC-027` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | 6 | medium | `agent-engineering-reviewer` | no | current RAG frameworks, embedding models, vector databases and rerankers |
| 3 | `WAVE3-WORKORDER-TICKET-SRC-028` | `TICKET-SRC-028` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | 6 | medium | `agent-engineering-reviewer` | no | current eval harnesses, model APIs and MCP/tool schemas |
| 4 | `WAVE3-WORKORDER-TICKET-SRC-029` | `TICKET-SRC-029` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | 6 | medium | `software-maintainer-reviewer` | no | current OpenAI, Codex, GitHub or Vercel product behavior |
| 5 | `WAVE3-WORKORDER-TICKET-SRC-030` | `TICKET-SRC-030` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | 6 | medium | `software-maintainer-reviewer` | no | current cloud platform build, deploy, runtime and pricing behavior |
| 6 | `WAVE3-WORKORDER-TICKET-SRC-031` | `TICKET-SRC-031` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | 6 | medium | `software-maintainer-reviewer` | no | current dependency vulnerabilities and security advisories |
| 7 | `WAVE3-WORKORDER-TICKET-SRC-032` | `TICKET-SRC-032` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | 6 | medium | `software-maintainer-reviewer` | no | current framework, library, CLI and API parameters |
| 8 | `WAVE3-WORKORDER-TICKET-SRC-033` | `TICKET-SRC-033` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | 5 | low | `content-fact-check-reviewer` | no | current image, chart, dataset and quote licensing |
| 9 | `WAVE3-WORKORDER-TICKET-SRC-034` | `TICKET-SRC-034` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | 5 | low | `content-fact-check-reviewer` | no | current news, statistics, public quotes and social media claims |
| 10 | `WAVE3-WORKORDER-TICKET-SRC-035` | `TICKET-SRC-035` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | 5 | low | `content-fact-check-reviewer` | no | current publishing platform rules, format limits and content policies |

## Reviewer Workload

| Reviewer Role | Work Orders | High Risk | Human Gates | Tickets |
| --- | ---: | ---: | ---: | --- |
| `agent-engineering-reviewer` | 3 | 0 | 0 | `TICKET-SRC-026`, `TICKET-SRC-027`, `TICKET-SRC-028` |
| `content-fact-check-reviewer` | 3 | 0 | 0 | `TICKET-SRC-033`, `TICKET-SRC-034`, `TICKET-SRC-035` |
| `software-maintainer-reviewer` | 4 | 0 | 0 | `TICKET-SRC-029`, `TICKET-SRC-030`, `TICKET-SRC-031`, `TICKET-SRC-032` |

## Preflight Checklist

- [ ] Read root AGENTS.md and the target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.
- [ ] Confirm the ticket topic and scope before opening or recording any source.
- [ ] Use official, primary, dated sources whenever available.
- [ ] Record source title, publisher, URL or local reference, publication/update date, access date, confidence, and remaining uncertainty.
- [ ] Keep status pending or still-needs-source-update when evidence is missing, stale, conflicting, or out of scope.
- [ ] Do not write current facts into wiki pages from this plan.
- [ ] Do not record API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.

## Per-Ticket Source Targets

### 1. TICKET-SRC-026 - agent-engineering-wiki

- Risk: medium
- Reviewer role: `agent-engineering-reviewer`
- Human confirmation: no
- Topic: current Codex Skill format, plugin behavior and tool capabilities
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: official documentation, product changelog, local plugin manifest
- Source notes: [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/agent-engineering-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-026 --status pending --dry-run`

### 2. TICKET-SRC-027 - agent-engineering-wiki

- Risk: medium
- Reviewer role: `agent-engineering-reviewer`
- Human confirmation: no
- Topic: current RAG frameworks, embedding models, vector databases and rerankers
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: official documentation, release notes, benchmark report with date
- Source notes: [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/agent-engineering-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-027 --status pending --dry-run`

### 3. TICKET-SRC-028 - agent-engineering-wiki

- Risk: medium
- Reviewer role: `agent-engineering-reviewer`
- Human confirmation: no
- Topic: current eval harnesses, model APIs and MCP/tool schemas
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: official API documentation, tool schema, repository release notes
- Source notes: [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/agent-engineering-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-028 --status pending --dry-run`

### 4. TICKET-SRC-029 - coding-agent-wiki

- Risk: medium
- Reviewer role: `software-maintainer-reviewer`
- Human confirmation: no
- Topic: current OpenAI, Codex, GitHub or Vercel product behavior
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: official product documentation, changelog, repository or API docs
- Source notes: [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-029 --status pending --dry-run`

### 5. TICKET-SRC-030 - coding-agent-wiki

- Risk: medium
- Reviewer role: `software-maintainer-reviewer`
- Human confirmation: no
- Topic: current cloud platform build, deploy, runtime and pricing behavior
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: official platform documentation, status page, project deployment logs
- Source notes: [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-030 --status pending --dry-run`

### 6. TICKET-SRC-031 - coding-agent-wiki

- Risk: medium
- Reviewer role: `software-maintainer-reviewer`
- Human confirmation: no
- Topic: current dependency vulnerabilities and security advisories
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: official security advisory, package registry advisory, vendor bulletin
- Source notes: [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-031 --status pending --dry-run`

### 7. TICKET-SRC-032 - coding-agent-wiki

- Risk: medium
- Reviewer role: `software-maintainer-reviewer`
- Human confirmation: no
- Topic: current framework, library, CLI and API parameters
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: official documentation, release notes, source repository
- Source notes: [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-032 --status pending --dry-run`

### 8. TICKET-SRC-033 - content-agent-wiki

- Risk: low
- Reviewer role: `content-fact-check-reviewer`
- Human confirmation: no
- Topic: current image, chart, dataset and quote licensing
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: license document, rights holder page, source terms of use
- Source notes: [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/content-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-033 --status pending --dry-run`

### 9. TICKET-SRC-034 - content-agent-wiki

- Risk: low
- Reviewer role: `content-fact-check-reviewer`
- Human confirmation: no
- Topic: current news, statistics, public quotes and social media claims
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: primary source, official data release, dated reputable reporting
- Source notes: [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/content-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-034 --status pending --dry-run`

### 10. TICKET-SRC-035 - content-agent-wiki

- Risk: low
- Reviewer role: `content-fact-check-reviewer`
- Human confirmation: no
- Topic: current publishing platform rules, format limits and content policies
- Reason for wave placement: Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; this topic still needs authoritative evidence before any current-fact use.
- Dependencies: current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.; Planning-only packet artifacts must not be imported as verified evidence.; Wave-1 active packet state must remain acceptance-compatible.; Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.
- Suggested source types: platform policy center, creator documentation, account dashboard notices
- Source notes: [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)
- Evidence log: [source-refresh-log.md](../wikis/content-agent-wiki/sources/source-refresh-log.md)
- Dry run: `python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-035 --status pending --dry-run`

## Packet Skeleton

This is placeholder-only. Replace every placeholder before any real import.

```json
{
  "packet_id": "source-review-session-wave-3-pending",
  "created_on": "2026-05-31",
  "created_by": "<human reviewer or source-refresh agent>",
  "dry_run_first": true,
  "entries": [
    {
      "ticket_id": "TICKET-SRC-026",
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
      "human_reviewer": "",
      "follow_up": "Keep needs-source-update unless authoritative, dated, scoped evidence is recorded and reviewed."
    },
    {
      "ticket_id": "TICKET-SRC-027",
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
      "human_reviewer": "",
      "follow_up": "Keep needs-source-update unless authoritative, dated, scoped evidence is recorded and reviewed."
    },
    {
      "ticket_id": "TICKET-SRC-028",
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
      "human_reviewer": "",
      "follow_up": "Keep needs-source-update unless authoritative, dated, scoped evidence is recorded and reviewed."
    }
  ],
  "truncated_entries": 7
}
```

## Next Commands

```bash
python scripts/generate_source_review_wave_packet_bundle.py --plan registry/source-review-wave-3-plan.json --stem source-review-session-wave-3-pending
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
| wave-3 topics selected | PASS | 10 planned work orders |
| reviewer cards available for selected topics | PASS | 10/10 reviewer roles |
| current facts remain gated | PASS | current_fact_ready=false; plan writes no current facts |
