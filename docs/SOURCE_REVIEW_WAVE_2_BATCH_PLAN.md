# Source Review Wave 2 Batch Plan

Generated: 2026-05-31

## Purpose

Prepare wave-2 evidence collection batches without source verification or current-fact writes.

## Summary

- Passed: yes
- Planning only: yes
- Current facts written: no
- Tickets: 12
- Batches: 4
- High-risk tickets: 3
- Human gates: 3
- Batch directory: [source-review-wave-2-batches](../registry/source-review-wave-2-batches)

## Batches

| Batch | Reviewer Role | Tickets | High Risk | Human Gates | File |
| --- | --- | ---: | ---: | ---: | --- |
| `batch-1-nodeops` | `operations-change-reviewer` | 3 | 3 | 3 | [batch-1-nodeops.md](../registry/source-review-wave-2-batches/batch-1-nodeops.md) |
| `batch-2-customs` | `customs-document-reviewer` | 4 | 0 | 0 | [batch-2-customs.md](../registry/source-review-wave-2-batches/batch-2-customs.md) |
| `batch-3-ecommerce` | `ecommerce-policy-reviewer` | 3 | 0 | 0 | [batch-3-ecommerce.md](../registry/source-review-wave-2-batches/batch-3-ecommerce.md) |
| `batch-4-research` | `research-methods-reviewer` | 2 | 0 | 0 | [batch-4-research.md](../registry/source-review-wave-2-batches/batch-4-research.md) |

## Ticket Overview

### batch-1-nodeops

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current OS package, Docker, systemd and kernel behavior | official documentation, local version output, release notes |
| `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current blockchain node client versions, network parameters and upgrade requirements | official client release notes, chain foundation announcement, node logs and version output |
| `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current cloud provider limits, firewall behavior, billing and incident status | cloud provider documentation, status page, account console |

### batch-2-customs

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | exchange rates, tariff rates, tax rates and destination-specific fees | central bank or official exchange source, customs tariff system, destination country authority |
| `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest HS codes, customs supervision conditions and declaration elements | customs authority website, official tariff database, licensed customs broker review |
| `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest import/export policy, inspection and quarantine requirements | customs and inspection authority announcement, destination country regulator, official trade compliance bulletin |
| `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest platform OCR model parameters and document template behavior | OCR vendor documentation, internal extraction benchmark, manually reviewed sample set |

### batch-3-ecommerce

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current marketplace policy, return window, category restrictions and consumer protection rules | official marketplace policy center, consumer protection authority, merchant service agreement |
| `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current product certification, recall, safety notice and warranty terms | brand official website, regulator recall database, warranty document |
| `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current product price, stock, promotion, shipping fee and delivery ETA | platform product page, merchant backend, carrier tracking system |

### batch-4-research

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-024` | [research-agent-wiki](../wikis/research-agent-wiki) | medium | `research-methods-reviewer` | no | current dataset availability, license, model weights and code repository status | official dataset page, repository release notes, model card |
| `TICKET-SRC-025` | [research-agent-wiki](../wikis/research-agent-wiki) | medium | `research-methods-reviewer` | no | latest papers, preprints, revisions, citations and benchmark leaderboards | publisher page, arXiv or conference page, official benchmark leaderboard |

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| wave-2 plan exists and passed | PASS | registry/source-review-wave-2-plan.json |
| all wave-2 tickets assigned to batches | PASS | 12/12 tickets |
| no current facts written | PASS | planning-only batch preparation |
