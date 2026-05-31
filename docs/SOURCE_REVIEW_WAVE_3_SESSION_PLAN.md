# Source Review Wave 3 Session Plan

Generated: 2026-05-31

## Purpose

Prepare wave 3 source review packet and work orders without browsing, verifying, importing, or writing current facts.

## Summary

- Current-fact ready: no
- Selected reviews: 10
- High-risk reviews: 0
- Human confirmation gates: 0
- Packet JSON: [source-review-session-wave-3-pending.json](../registry/source-review-packets/source-review-session-wave-3-pending.json)
- Packet JSONL: [source-review-session-wave-3-pending.jsonl](../registry/source-review-packets/source-review-session-wave-3-pending.jsonl)
- Packet checklist: [source-review-session-wave-3-pending-checklist.md](../registry/source-review-packets/source-review-session-wave-3-pending-checklist.md)
- Work order directory: [source-review-work-orders-wave-3](../registry/source-review-work-orders-wave-3)

## Selected Reviews

| Ticket | Wiki | Priority | Risk | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-026` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | medium | `agent-engineering-reviewer` | no | current Codex Skill format, plugin behavior and tool capabilities |
| `TICKET-SRC-027` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | medium | `agent-engineering-reviewer` | no | current RAG frameworks, embedding models, vector databases and rerankers |
| `TICKET-SRC-028` | [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | medium | `agent-engineering-reviewer` | no | current eval harnesses, model APIs and MCP/tool schemas |
| `TICKET-SRC-029` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | medium | `software-maintainer-reviewer` | no | current OpenAI, Codex, GitHub or Vercel product behavior |
| `TICKET-SRC-030` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | medium | `software-maintainer-reviewer` | no | current cloud platform build, deploy, runtime and pricing behavior |
| `TICKET-SRC-031` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | medium | `software-maintainer-reviewer` | no | current dependency vulnerabilities and security advisories |
| `TICKET-SRC-032` | [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | medium | `software-maintainer-reviewer` | no | current framework, library, CLI and API parameters |
| `TICKET-SRC-033` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | low | `content-fact-check-reviewer` | no | current image, chart, dataset and quote licensing |
| `TICKET-SRC-034` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | low | `content-fact-check-reviewer` | no | current news, statistics, public quotes and social media claims |
| `TICKET-SRC-035` | [content-agent-wiki](../wikis/content-agent-wiki) | P1 | low | `content-fact-check-reviewer` | no | current publishing platform rules, format limits and content policies |

## Guardrails

- Packet entries are placeholders only and remain pending.
- Do not use this session plan as verified evidence.
- Do not write current facts into wiki pages.
- Node operations work requires named human confirmation before final status.

## Next Commands

```bash
python scripts\audit_source_review_packets.py
python scripts\rehearse_source_review_packet_imports.py
python scripts\audit_links.py
python scripts\run_acceptance.py
```
