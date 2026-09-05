# Agent Handoff

Generated: 2026-09-05

## Purpose

Give the next agent a safe, source-aware entry point for continuing Agent Wiki Hub work.

## Current State

- Internal release ready: yes
- Current-fact ready: no
- Acceptance passed: yes
- Source-refresh tickets: 35
- Open tickets: 35
- Verified tickets: 0
- Finalized tickets: 0
- Source evidence entries: 13
- Evidence quality issues: 0
- Evidence quality warnings: 0
- Source reviewer queue: 35 open reviews
- Source reviewer human gates: 16
- Source review session: 25 selected reviews
- Source review session human gates: 16
- Source review packet bundle: 25 pending entries
- Source review packet human gates: 16
- Source review packet audit: 2 packets
- Source review packet audit issues: 0
- Source review packet rehearsal: 2/2 dry-runs passed
- Source review ready for collection: 25
- Source review queued outside session: 10
- Source review work orders: 25
- Source review work order human gates: 16

## First Reads

- [AGENTS.md](../AGENTS.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [AGENT_ROUTING_CARDS.md](../docs/AGENT_ROUTING_CARDS.md)
- [HUB_NAVIGATION.md](../docs/HUB_NAVIGATION.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)
- [SAFETY_AUDIT.md](../docs/SAFETY_AUDIT.md)

## Hard Boundaries

- Do not treat open source-refresh tickets as verified facts.
- Do not write current prices, policies, laws, medical guidance, CVEs, API parameters, platform rules, exchange rules, or Web3 project rules without dated evidence.
- Do not record API keys, private keys, cookies, seed phrases, credentials, or private account data.
- Do not generate real-money autonomous trading flows.
- Do not produce final legal opinions, medical diagnoses, offensive security steps, Sybil evasion, spam, fake identity, or platform-rule bypass guidance.
- For high-risk wikis, read rules/ before workflows/ and preserve human confirmation points.

## Next Best Work

- If source access is unavailable, keep current-fact tickets open and add only stable concepts, workflows, prompts, evals, and safety boundaries.
- If source access is available, start with wave-1 and P0 tickets, then record evidence through scripts/record_source_evidence.py.
- After any source update, rerun source completion, evidence quality, dashboard generation, search index, and full acceptance.
- Keep affected wiki update-log.md files current whenever wiki content changes.

## P0 Open Tickets

| Wiki | Open | Ticket Topics |
| --- | ---: | --- |
| [agent-engineering-wiki](../wikis/agent-engineering-wiki) | 3 | `TICKET-SRC-026` current Codex Skill format, plugin behavior and tool capabilities<br>`TICKET-SRC-027` current RAG frameworks, embedding models, vector databases and rerankers<br>`TICKET-SRC-028` current eval harnesses, model APIs and MCP/tool schemas |
| [coding-agent-wiki](../wikis/coding-agent-wiki) | 4 | `TICKET-SRC-029` current OpenAI, Codex, GitHub or Vercel product behavior<br>`TICKET-SRC-030` current cloud platform build, deploy, runtime and pricing behavior<br>`TICKET-SRC-031` current dependency vulnerabilities and security advisories<br>`TICKET-SRC-032` current framework, library, CLI and API parameters |
| [customs-agent-wiki](../wikis/customs-agent-wiki) | 4 | `TICKET-SRC-014` exchange rates, tariff rates, tax rates and destination-specific fees<br>`TICKET-SRC-015` latest HS codes, customs supervision conditions and declaration elements<br>`TICKET-SRC-016` latest import/export policy, inspection and quarantine requirements<br>`TICKET-SRC-017` latest platform OCR model parameters and document template behavior |
| [finance-agent-wiki](../wikis/finance-agent-wiki) | 0 | - |

## Top Open Tickets

| Ticket | Wiki | Wave | Risk | Topic | Human Confirm |
| --- | --- | --- | --- | --- | --- |

## Wiki Order

| Wiki | Priority | Risk | Freshness | Domain |
| --- | --- | --- | --- | --- |
| [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | medium | medium | ai_agent_engineering |
| [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | medium | medium | software_engineering |
| [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | medium | high | customs_trade_documents |
| [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | high | high | finance |
| [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | high | high | web3_research |
| [content-agent-wiki](../wikis/content-agent-wiki) | P1 | low | medium | content_operations |
| [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | medium | high | ecommerce |
| [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | high | medium | operations |
| [health-agent-wiki](../wikis/health-agent-wiki) | P2 | high | high | health_education |
| [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | high | high | legal_information |
| [research-agent-wiki](../wikis/research-agent-wiki) | P2 | medium | high | research |
| [security-agent-wiki](../wikis/security-agent-wiki) | P2 | high | high | defensive_security |

## Useful Commands

```bash
python3 scripts/route_wiki.py --query "risk control backtest"
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run
python3 scripts/audit_source_refresh_completion.py
python3 scripts/audit_source_evidence_quality.py
python3 scripts/generate_source_refresh_dashboard.py
python3 scripts/generate_source_refresh_wave_runner.py --wave wave-1 --limit 5
python3 scripts/generate_source_reviewer_queue.py
python3 scripts/generate_source_review_session_plan.py --wave wave-1 --limit 5
python3 scripts/generate_source_review_packet_bundle.py
python3 scripts/audit_source_review_packets.py
python3 scripts/rehearse_source_review_packet_imports.py
python3 scripts/generate_source_review_readiness_matrix.py
python3 scripts/generate_source_review_work_orders.py
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks
python3 scripts/import_source_evidence_packet.py --template --ticket-id TICKET-SRC-006
python3 scripts/generate_source_evidence_packet_fixtures.py
python3 scripts/run_acceptance.py
```

## Notes

- This handoff is generated from local registry and audit artifacts.
- It does not verify external facts by itself.
- Treat every open current-fact topic as `needs-source-update` until evidence is recorded and audits are rerun.
