# Source Review Wave 2 Work Orders

Generated: 2026-05-31

## Purpose

Provide independent wave-2 work orders for source reviewers without verifying, importing, or writing current facts.

## Summary

- Passed: yes
- Work orders: 12
- High-risk work orders: 3
- Human confirmation gates: 3
- Work order directory: [source-review-work-orders-wave-2](../registry/source-review-work-orders-wave-2)

## Work Orders

| Work Order | Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- | --- |
| [WAVE2-WORKORDER-TICKET-SRC-021](../registry/source-review-work-orders-wave-2/TICKET-SRC-021.md) | `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current OS package, Docker, systemd and kernel behavior |
| [WAVE2-WORKORDER-TICKET-SRC-022](../registry/source-review-work-orders-wave-2/TICKET-SRC-022.md) | `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current blockchain node client versions, network parameters and upgrade requirements |
| [WAVE2-WORKORDER-TICKET-SRC-023](../registry/source-review-work-orders-wave-2/TICKET-SRC-023.md) | `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current cloud provider limits, firewall behavior, billing and incident status |
| [WAVE2-WORKORDER-TICKET-SRC-014](../registry/source-review-work-orders-wave-2/TICKET-SRC-014.md) | `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| [WAVE2-WORKORDER-TICKET-SRC-015](../registry/source-review-work-orders-wave-2/TICKET-SRC-015.md) | `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest HS codes, customs supervision conditions and declaration elements |
| [WAVE2-WORKORDER-TICKET-SRC-016](../registry/source-review-work-orders-wave-2/TICKET-SRC-016.md) | `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest import/export policy, inspection and quarantine requirements |
| [WAVE2-WORKORDER-TICKET-SRC-017](../registry/source-review-work-orders-wave-2/TICKET-SRC-017.md) | `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest platform OCR model parameters and document template behavior |
| [WAVE2-WORKORDER-TICKET-SRC-018](../registry/source-review-work-orders-wave-2/TICKET-SRC-018.md) | `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| [WAVE2-WORKORDER-TICKET-SRC-019](../registry/source-review-work-orders-wave-2/TICKET-SRC-019.md) | `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current product certification, recall, safety notice and warranty terms |
| [WAVE2-WORKORDER-TICKET-SRC-020](../registry/source-review-work-orders-wave-2/TICKET-SRC-020.md) | `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current product price, stock, promotion, shipping fee and delivery ETA |
| [WAVE2-WORKORDER-TICKET-SRC-024](../registry/source-review-work-orders-wave-2/TICKET-SRC-024.md) | `TICKET-SRC-024` | [research-agent-wiki](../wikis/research-agent-wiki) | medium | `research-methods-reviewer` | no | current dataset availability, license, model weights and code repository status |
| [WAVE2-WORKORDER-TICKET-SRC-025](../registry/source-review-work-orders-wave-2/TICKET-SRC-025.md) | `TICKET-SRC-025` | [research-agent-wiki](../wikis/research-agent-wiki) | medium | `research-methods-reviewer` | no | latest papers, preprints, revisions, citations and benchmark leaderboards |

## Safety Boundary

- These work orders are planning-only.
- They do not authorize production changes, wallet actions, cloud changes, live upgrades, or billing-sensitive operations.
- They do not certify any source fields; reviewer-filled evidence is still required.
