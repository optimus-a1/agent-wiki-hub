# Source Reviewer Queue

Generated: 2026-06-16

## Purpose

Assign source-refresh tickets to generic reviewer roles while preserving human confirmation and current-fact gates.

## Current State

- Queue generated cleanly: yes
- Current-fact ready: no
- Tickets: 35
- Open tickets: 35
- Verified tickets: 0
- Finalized tickets: 0
- Evidence entries: 13
- Evidence issues: 0
- Reviewer roles: 12
- Human review gates: 16

## Reviewer Roles

| Reviewer Role | Tickets | High Risk | Human Gates | Wikis | Scope |
| --- | ---: | ---: | ---: | --- | --- |
| `agent-engineering-reviewer` | 3 | 0 | 0 | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | Checks agent architecture, RAG, skills, evals, MCP, and source-grounding evidence. |
| `clinical-safety-reviewer` | 2 | 2 | 2 | [health-agent-wiki](../wikis/health-agent-wiki) | Checks guideline, drug, symptom, and health-education evidence while preserving clinician review and red flags. |
| `content-fact-check-reviewer` | 3 | 0 | 0 | [content-agent-wiki](../wikis/content-agent-wiki) | Checks publication, trend, citation, platform, and source-backed claim evidence. |
| `customs-document-reviewer` | 4 | 0 | 0 | [customs-agent-wiki](../wikis/customs-agent-wiki) | Checks trade-document, field-mapping, OCR, discrepancy, and customs-policy evidence while preserving manual review gates. |
| `defensive-security-reviewer` | 2 | 2 | 2 | [security-agent-wiki](../wikis/security-agent-wiki) | Checks defensive security, advisory, dependency, and hardening evidence without exploit or evasion steps. |
| `ecommerce-policy-reviewer` | 3 | 0 | 0 | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | Checks product, pricing, customer-service, returns, privacy, ads, and marketplace-policy evidence. |
| `finance-risk-reviewer` | 4 | 4 | 4 | [finance-agent-wiki](../wikis/finance-agent-wiki) | Checks market, accounting, regulatory, and trading-system evidence while preserving investment-advice and real-money execution boundaries. |
| `legal-counsel-reviewer` | 2 | 2 | 2 | [legal-agent-wiki](../wikis/legal-agent-wiki) | Checks jurisdiction, statute, regulation, contract, and legal-process evidence while preserving counsel review. |
| `operations-change-reviewer` | 3 | 3 | 3 | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | Checks infrastructure, deployment, install, monitoring, node, and destructive-operation evidence with rollback gates. |
| `research-methods-reviewer` | 2 | 0 | 0 | [research-agent-wiki](../wikis/research-agent-wiki) | Checks papers, datasets, benchmarks, citations, and reproducibility evidence. |
| `software-maintainer-reviewer` | 4 | 0 | 0 | [coding-agent-wiki](../wikis/coding-agent-wiki) | Checks software, dependency, API, deployment, and security-development evidence without recording secrets. |
| `web3-wallet-safety-reviewer` | 3 | 3 | 3 | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | Checks public Web3 project, token, airdrop, and wallet-safety evidence without Sybil, spam, or signing automation. |

## Wave Summary

| Wave | Reviews | High Risk | Human Gates | Wikis |
| --- | ---: | ---: | ---: | --- |
| wave-1 | 13 | 13 | 13 | airdrop-agent-wiki:3, finance-agent-wiki:4, health-agent-wiki:2, legal-agent-wiki:2, security-agent-wiki:2 |
| wave-2 | 12 | 3 | 3 | customs-agent-wiki:4, ecommerce-agent-wiki:3, nodeops-agent-wiki:3, research-agent-wiki:2 |
| wave-3 | 10 | 0 | 0 | agent-engineering-wiki:3, coding-agent-wiki:4, content-agent-wiki:3 |

## Priority Summary

| Priority | Reviews | High Risk | Human Gates | Wikis |
| --- | ---: | ---: | ---: | --- |
| P0 | 15 | 4 | 4 | agent-engineering-wiki:3, coding-agent-wiki:4, customs-agent-wiki:4, finance-agent-wiki:4 |
| P1 | 12 | 6 | 6 | airdrop-agent-wiki:3, content-agent-wiki:3, ecommerce-agent-wiki:3, nodeops-agent-wiki:3 |
| P2 | 8 | 6 | 6 | health-agent-wiki:2, legal-agent-wiki:2, research-agent-wiki:2, security-agent-wiki:2 |

## Human Confirmation Queue

| Review | Ticket | Wiki | Priority | Wave | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `REVIEW-SRC-001` | `TICKET-SRC-004` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | finance-risk-reviewer | yes | current fees, funding rates, margin rules, tax rules and trading API parameters |
| `REVIEW-SRC-002` | `TICKET-SRC-005` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | finance-risk-reviewer | yes | current legal, regulatory or suitability requirements for financial products |
| `REVIEW-SRC-003` | `TICKET-SRC-006` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | finance-risk-reviewer | yes | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| `REVIEW-SRC-004` | `TICKET-SRC-007` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | finance-risk-reviewer | yes | latest financial statements, filings, restatements and audit opinions |
| `REVIEW-SRC-005` | `TICKET-SRC-001` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | web3-wallet-safety-reviewer | yes | current contract addresses, wallet warnings, scam reports and signing risks |
| `REVIEW-SRC-006` | `TICKET-SRC-002` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | web3-wallet-safety-reviewer | yes | current project status, official links, task rules, snapshot and eligibility |
| `REVIEW-SRC-007` | `TICKET-SRC-003` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | web3-wallet-safety-reviewer | yes | current token launch, TGE, funding, exchange listing and airdrop allocation |
| `REVIEW-SRC-008` | `TICKET-SRC-008` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | clinical-safety-reviewer | yes | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| `REVIEW-SRC-009` | `TICKET-SRC-009` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | clinical-safety-reviewer | yes | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| `REVIEW-SRC-010` | `TICKET-SRC-010` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | legal-counsel-reviewer | yes | current platform agreements, data processing terms and consumer protection rules |
| `REVIEW-SRC-011` | `TICKET-SRC-011` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | legal-counsel-reviewer | yes | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements |
| `REVIEW-SRC-012` | `TICKET-SRC-012` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | defensive-security-reviewer | yes | current CVEs, vendor advisories, patches, dependency versions and exploit status |
| `REVIEW-SRC-013` | `TICKET-SRC-013` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | defensive-security-reviewer | yes | current security tool rules, detection signatures, cloud defaults and compliance requirements |
| `REVIEW-SRC-021` | `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | operations-change-reviewer | yes | current OS package, Docker, systemd and kernel behavior |
| `REVIEW-SRC-022` | `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | operations-change-reviewer | yes | current blockchain node client versions, network parameters and upgrade requirements |
| `REVIEW-SRC-023` | `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | operations-change-reviewer | yes | current cloud provider limits, firewall behavior, billing and incident status |

## Review Cards

| Review | Ticket | Wiki | Priority | Wave | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `REVIEW-SRC-001` | `TICKET-SRC-004` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | finance-risk-reviewer | yes | current fees, funding rates, margin rules, tax rules and trading API parameters |
| `REVIEW-SRC-002` | `TICKET-SRC-005` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | finance-risk-reviewer | yes | current legal, regulatory or suitability requirements for financial products |
| `REVIEW-SRC-003` | `TICKET-SRC-006` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | finance-risk-reviewer | yes | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| `REVIEW-SRC-004` | `TICKET-SRC-007` | [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | wave-1 | finance-risk-reviewer | yes | latest financial statements, filings, restatements and audit opinions |
| `REVIEW-SRC-005` | `TICKET-SRC-001` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | web3-wallet-safety-reviewer | yes | current contract addresses, wallet warnings, scam reports and signing risks |
| `REVIEW-SRC-006` | `TICKET-SRC-002` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | web3-wallet-safety-reviewer | yes | current project status, official links, task rules, snapshot and eligibility |
| `REVIEW-SRC-007` | `TICKET-SRC-003` | [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | wave-1 | web3-wallet-safety-reviewer | yes | current token launch, TGE, funding, exchange listing and airdrop allocation |
| `REVIEW-SRC-008` | `TICKET-SRC-008` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | clinical-safety-reviewer | yes | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| `REVIEW-SRC-009` | `TICKET-SRC-009` | [health-agent-wiki](../wikis/health-agent-wiki) | P2 | wave-1 | clinical-safety-reviewer | yes | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| `REVIEW-SRC-010` | `TICKET-SRC-010` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | legal-counsel-reviewer | yes | current platform agreements, data processing terms and consumer protection rules |
| `REVIEW-SRC-011` | `TICKET-SRC-011` | [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | wave-1 | legal-counsel-reviewer | yes | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements |
| `REVIEW-SRC-012` | `TICKET-SRC-012` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | defensive-security-reviewer | yes | current CVEs, vendor advisories, patches, dependency versions and exploit status |
| `REVIEW-SRC-013` | `TICKET-SRC-013` | [security-agent-wiki](../wikis/security-agent-wiki) | P2 | wave-1 | defensive-security-reviewer | yes | current security tool rules, detection signatures, cloud defaults and compliance requirements |
| `REVIEW-SRC-014` | `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-2 | customs-document-reviewer | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| `REVIEW-SRC-015` | `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-2 | customs-document-reviewer | no | latest HS codes, customs supervision conditions and declaration elements |
| `REVIEW-SRC-016` | `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-2 | customs-document-reviewer | no | latest import/export policy, inspection and quarantine requirements |
| `REVIEW-SRC-017` | `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | wave-2 | customs-document-reviewer | no | latest platform OCR model parameters and document template behavior |
| `REVIEW-SRC-018` | `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-2 | ecommerce-policy-reviewer | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| `REVIEW-SRC-019` | `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-2 | ecommerce-policy-reviewer | no | current product certification, recall, safety notice and warranty terms |
| `REVIEW-SRC-020` | `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | wave-2 | ecommerce-policy-reviewer | no | current product price, stock, promotion, shipping fee and delivery ETA |
| `REVIEW-SRC-021` | `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | operations-change-reviewer | yes | current OS package, Docker, systemd and kernel behavior |
| `REVIEW-SRC-022` | `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | operations-change-reviewer | yes | current blockchain node client versions, network parameters and upgrade requirements |
| `REVIEW-SRC-023` | `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | wave-2 | operations-change-reviewer | yes | current cloud provider limits, firewall behavior, billing and incident status |
| `REVIEW-SRC-024` | `TICKET-SRC-024` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | wave-2 | research-methods-reviewer | no | current dataset availability, license, model weights and code repository status |
| `REVIEW-SRC-025` | `TICKET-SRC-025` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | wave-2 | research-methods-reviewer | no | latest papers, preprints, revisions, citations and benchmark leaderboards |
| `REVIEW-SRC-026` | `TICKET-SRC-026` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | wave-3 | agent-engineering-reviewer | no | current Codex Skill format, plugin behavior and tool capabilities |
| `REVIEW-SRC-027` | `TICKET-SRC-027` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | wave-3 | agent-engineering-reviewer | no | current RAG frameworks, embedding models, vector databases and rerankers |
| `REVIEW-SRC-028` | `TICKET-SRC-028` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | wave-3 | agent-engineering-reviewer | no | current eval harnesses, model APIs and MCP/tool schemas |
| `REVIEW-SRC-029` | `TICKET-SRC-029` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | wave-3 | software-maintainer-reviewer | no | current OpenAI, Codex, GitHub or Vercel product behavior |
| `REVIEW-SRC-030` | `TICKET-SRC-030` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | wave-3 | software-maintainer-reviewer | no | current cloud platform build, deploy, runtime and pricing behavior |
| `REVIEW-SRC-031` | `TICKET-SRC-031` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | wave-3 | software-maintainer-reviewer | no | current dependency vulnerabilities and security advisories |
| `REVIEW-SRC-032` | `TICKET-SRC-032` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | wave-3 | software-maintainer-reviewer | no | current framework, library, CLI and API parameters |
| `REVIEW-SRC-033` | `TICKET-SRC-033` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | wave-3 | content-fact-check-reviewer | no | current image, chart, dataset and quote licensing |
| `REVIEW-SRC-034` | `TICKET-SRC-034` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | wave-3 | content-fact-check-reviewer | no | current news, statistics, public quotes and social media claims |
| `REVIEW-SRC-035` | `TICKET-SRC-035` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | wave-3 | content-fact-check-reviewer | no | current publishing platform rules, format limits and content policies |

## Reviewer Checklist

- Read root and wiki-level instructions before collecting sources.
- Use official, primary, dated sources whenever available.
- Record publication or update date, access date, scope, confidence, and uncertainty.
- Keep high-risk finance, legal, health, security, Web3, and operations topics behind human confirmation.
- Do not record secrets, credentials, cookies, private keys, seed phrases, or private account data.
- Keep `needs-source-update` in place until evidence logs and audits support a final status.

## Useful Commands

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
- source_refresh_tickets: [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- source_evidence_recorder: [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- source_evidence_packet_importer: [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- source_evidence_packet_fixtures: [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- source_refresh_completion: [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- source_evidence_quality: [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| required source-refresh artifacts exist | PASS | all required artifacts present |
| open tickets have reviewer roles | PASS | 35 review cards for 35 open tickets |
| human review gates are preserved | PASS | 16 human-gated cards |
| current facts remain gated | PASS | current_fact_ready=false while open tickets remain |

## Safety Boundary

- This queue does not fetch, verify, or certify external facts.
- Reviewer roles are generic operating roles, not real people or external authorities.
- A ticket can remain open with `still-needs-source-update` when evidence is missing, stale, conflicting, or outside scope.
