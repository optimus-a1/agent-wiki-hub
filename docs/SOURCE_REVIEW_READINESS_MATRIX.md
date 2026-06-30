# Source Review Readiness Matrix

Generated: 2026-06-30

## Purpose

Show per-ticket readiness across reviewer assignment, session selection, packet coverage, packet audit, rehearsal, and completion state.

## Summary

- Passed: yes
- Current-fact ready: no
- Tickets: 35
- Open tickets: 35
- Finalized tickets: 0
- Verified tickets: 0
- Ready for source collection: 22
- Queued outside current session: 13
- Selected finalized tickets: 0
- Selected verified tickets: 0
- Source review phase: pre-import-or-in-progress
- Packet audit issues: 0
- Packet rehearsal failures: 0

## Stage Counts

- queued-not-in-current-session: 13
- ready-for-source-collection: 22

## Matrix

| Ticket | Wiki | Priority | Wave | Risk | Reviewer | Session | Packet | Audit | Rehearsal | Stage | Topic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-1 | medium | customs-document-reviewer | yes | 2 | yes | yes | ready-for-source-collection | exchange rates, tariff rates, tax rates and destination-specific fees |
| `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-1 | medium | customs-document-reviewer | yes | 2 | yes | yes | ready-for-source-collection | latest HS codes, customs supervision conditions and declaration elements |
| `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-1 | medium | customs-document-reviewer | yes | 2 | yes | yes | ready-for-source-collection | latest import/export policy, inspection and quarantine requirements |
| `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-1 | medium | customs-document-reviewer | yes | 2 | yes | yes | ready-for-source-collection | latest platform OCR model parameters and document template behavior |
| `TICKET-SRC-004` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | finance-risk-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current fees, funding rates, margin rules, tax rules and trading API parameters |
| `TICKET-SRC-005` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | finance-risk-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current legal, regulatory or suitability requirements for financial products |
| `TICKET-SRC-006` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | finance-risk-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| `TICKET-SRC-007` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | high | finance-risk-reviewer | yes | 2 | yes | yes | ready-for-source-collection | latest financial statements, filings, restatements and audit opinions |
| `TICKET-SRC-026` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | wave-3 | medium | agent-engineering-reviewer | no | 0 | no | no | queued-not-in-current-session | current Codex Skill format, plugin behavior and tool capabilities |
| `TICKET-SRC-027` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | wave-3 | medium | agent-engineering-reviewer | no | 0 | no | no | queued-not-in-current-session | current RAG frameworks, embedding models, vector databases and rerankers |
| `TICKET-SRC-028` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | wave-3 | medium | agent-engineering-reviewer | no | 0 | no | no | queued-not-in-current-session | current eval harnesses, model APIs and MCP/tool schemas |
| `TICKET-SRC-029` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | wave-3 | medium | software-maintainer-reviewer | no | 0 | no | no | queued-not-in-current-session | current OpenAI, Codex, GitHub or Vercel product behavior |
| `TICKET-SRC-030` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | wave-3 | medium | software-maintainer-reviewer | no | 0 | no | no | queued-not-in-current-session | current cloud platform build, deploy, runtime and pricing behavior |
| `TICKET-SRC-031` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | wave-3 | medium | software-maintainer-reviewer | no | 0 | no | no | queued-not-in-current-session | current dependency vulnerabilities and security advisories |
| `TICKET-SRC-032` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | wave-3 | medium | software-maintainer-reviewer | no | 0 | no | no | queued-not-in-current-session | current framework, library, CLI and API parameters |
| `TICKET-SRC-001` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | web3-wallet-safety-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current contract addresses, wallet warnings, scam reports and signing risks |
| `TICKET-SRC-002` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | web3-wallet-safety-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current project status, official links, task rules, snapshot and eligibility |
| `TICKET-SRC-003` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | high | web3-wallet-safety-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current token launch, TGE, funding, exchange listing and airdrop allocation |
| `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-1 | medium | ecommerce-policy-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current marketplace policy, return window, category restrictions and consumer protection rules |
| `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-1 | medium | ecommerce-policy-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current product certification, recall, safety notice and warranty terms |
| `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-1 | medium | ecommerce-policy-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current product price, stock, promotion, shipping fee and delivery ETA |
| `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | high | operations-change-reviewer | no | 0 | no | no | queued-not-in-current-session | current OS package, Docker, systemd and kernel behavior |
| `TICKET-SRC-024` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | high | operations-change-reviewer | no | 0 | no | no | queued-not-in-current-session | current blockchain node client versions, network parameters and upgrade requirements |
| `TICKET-SRC-025` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | high | operations-change-reviewer | no | 0 | no | no | queued-not-in-current-session | current cloud provider limits, firewall behavior, billing and incident status |
| `TICKET-SRC-033` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | wave-3 | low | content-fact-check-reviewer | no | 0 | no | no | queued-not-in-current-session | current image, chart, dataset and quote licensing |
| `TICKET-SRC-034` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | wave-3 | low | content-fact-check-reviewer | no | 0 | no | no | queued-not-in-current-session | current news, statistics, public quotes and social media claims |
| `TICKET-SRC-035` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | wave-3 | low | content-fact-check-reviewer | no | 0 | no | no | queued-not-in-current-session | current publishing platform rules, format limits and content policies |
| `TICKET-SRC-008` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | high | clinical-safety-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| `TICKET-SRC-009` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | high | clinical-safety-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| `TICKET-SRC-010` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | high | legal-counsel-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current platform agreements, data processing terms and consumer protection rules |
| `TICKET-SRC-011` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | high | legal-counsel-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements |
| `TICKET-SRC-021` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | wave-1 | medium | research-methods-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current dataset availability, license, model weights and code repository status |
| `TICKET-SRC-022` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | wave-1 | medium | research-methods-reviewer | yes | 2 | yes | yes | ready-for-source-collection | latest papers, preprints, revisions, citations and benchmark leaderboards |
| `TICKET-SRC-012` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | high | defensive-security-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current CVEs, vendor advisories, patches, dependency versions and exploit status |
| `TICKET-SRC-013` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | high | defensive-security-reviewer | yes | 2 | yes | yes | ready-for-source-collection | current security tool rules, detection signatures, cloud defaults and compliance requirements |

## Related Reports

- source_refresh_dashboard: [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- source_review_work_orders: [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- source_review_packet_rehearsal: [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- source_review_packet_audit: [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- source_review_packet_bundle: [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- source_review_session_plan: [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- source_reviewer_queue: [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- source_refresh_completion: [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- source_evidence_quality: [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| required source review artifacts exist | PASS | core source review registry artifacts |
| all tickets represented in matrix | PASS | 35 rows for 35 tickets |
| open tickets have reviewer cards | PASS | 35/35 rows have reviewer cards |
| selected reviews have packet entries | PASS | 22/22 selected rows have packet entries |
| packet audit passed | PASS | 2 packets, 0 issues |
| packet rehearsal passed | PASS | 2/2 dry-runs passed |
| current facts remain gated while open tickets exist | PASS | current_fact_ready=false while open tickets remain |

## Safety Boundary

- This matrix does not fetch, verify, or certify external facts.
- `ready-for-source-collection` means local packet and dry-run gates are ready, not that facts are verified.
- Current facts remain gated until completion and evidence quality audits show all relevant tickets are finalized.
