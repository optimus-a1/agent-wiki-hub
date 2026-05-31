# Source Review Wave 2 Session Plan

Generated: 2026-05-31

## Purpose

Prepare wave-2 source review packet and work orders without browsing, verifying, importing, or writing current facts.

## Summary

- Current-fact ready: no
- Selected reviews: 12
- High-risk reviews: 3
- Human confirmation gates: 3
- Packet JSON: [source-review-session-wave-2-pending.json](../registry/source-review-packets/source-review-session-wave-2-pending.json)
- Packet JSONL: [source-review-session-wave-2-pending.jsonl](../registry/source-review-packets/source-review-session-wave-2-pending.jsonl)
- Packet checklist: [source-review-session-wave-2-pending-checklist.md](../registry/source-review-packets/source-review-session-wave-2-pending-checklist.md)
- Work order directory: [source-review-work-orders-wave-2](../registry/source-review-work-orders-wave-2)

## Selected Reviews

| Ticket | Wiki | Priority | Risk | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | high | `operations-change-reviewer` | yes | current OS package, Docker, systemd and kernel behavior |
| `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | high | `operations-change-reviewer` | yes | current blockchain node client versions, network parameters and upgrade requirements |
| `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | high | `operations-change-reviewer` | yes | current cloud provider limits, firewall behavior, billing and incident status |
| `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | medium | `customs-document-reviewer` | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | medium | `customs-document-reviewer` | no | latest HS codes, customs supervision conditions and declaration elements |
| `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | medium | `customs-document-reviewer` | no | latest import/export policy, inspection and quarantine requirements |
| `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | medium | `customs-document-reviewer` | no | latest platform OCR model parameters and document template behavior |
| `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | medium | `ecommerce-policy-reviewer` | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | medium | `ecommerce-policy-reviewer` | no | current product certification, recall, safety notice and warranty terms |
| `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | medium | `ecommerce-policy-reviewer` | no | current product price, stock, promotion, shipping fee and delivery ETA |
| `TICKET-SRC-024` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | medium | `research-methods-reviewer` | no | current dataset availability, license, model weights and code repository status |
| `TICKET-SRC-025` | [research-agent-wiki](../wikis/research-agent-wiki) | P2 | medium | `research-methods-reviewer` | no | latest papers, preprints, revisions, citations and benchmark leaderboards |

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
