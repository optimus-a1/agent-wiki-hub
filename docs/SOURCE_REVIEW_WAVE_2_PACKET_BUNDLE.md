# Source Review Wave 2 Packet Bundle

Generated: 2026-05-31

## Purpose

Generate wave-2 pending packet artifacts only. No sources are verified, no evidence is imported, and no current facts are written.

## Summary

- Passed: yes
- Packet entries: 12
- High-risk entries: 3
- Human reviewer placeholders: 12
- JSON packet: [source-review-session-wave-2-pending.json](../registry/source-review-packets/source-review-session-wave-2-pending.json)
- JSONL packet: [source-review-session-wave-2-pending.jsonl](../registry/source-review-packets/source-review-session-wave-2-pending.jsonl)
- Checklist: [source-review-session-wave-2-pending-checklist.md](../registry/source-review-packets/source-review-session-wave-2-pending-checklist.md)

## Entry Field Invariants

- Every entry has `status=pending`.
- Every entry has `verified_on=""`.
- Every entry has `confidence=low`.
- Every entry has `human_reviewer="<reviewer>"`.
- Every entry has `evidence_summary="<what the source supports and does not support>"`.
- Source title, publisher, URL/reference, and publication date remain placeholders.

## Tickets

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current OS package, Docker, systemd and kernel behavior |
| `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current blockchain node client versions, network parameters and upgrade requirements |
| `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current cloud provider limits, firewall behavior, billing and incident status |
| `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest HS codes, customs supervision conditions and declaration elements |
| `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest import/export policy, inspection and quarantine requirements |
| `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest platform OCR model parameters and document template behavior |
| `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current product certification, recall, safety notice and warranty terms |
| `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current product price, stock, promotion, shipping fee and delivery ETA |
| `TICKET-SRC-024` | [research-agent-wiki](../wikis/research-agent-wiki) | medium | `research-methods-reviewer` | no | current dataset availability, license, model weights and code repository status |
| `TICKET-SRC-025` | [research-agent-wiki](../wikis/research-agent-wiki) | medium | `research-methods-reviewer` | no | latest papers, preprints, revisions, citations and benchmark leaderboards |

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| plan passed | PASS | registry/source-review-wave-2-plan.json |
| entry count matches selected reviews | PASS | 12 entries for 12 selected reviews |
| entries remain pending | PASS | all entries use status=pending |
| entries keep required placeholder fields | PASS | verified_on, confidence, human_reviewer, and evidence_summary placeholders checked |
| work orders written | PASS | 12 work order files plus manifest |
