# Batch 3 - Ecommerce P1 Review

Generated: 2026-05-31

## Purpose

Prepare source evidence collection for this wave-2 batch without browsing, verifying, importing, or writing current facts.

## Batch Summary

- Batch id: `batch-3-ecommerce`
- Reviewer role: `ecommerce-policy-reviewer`
- Tickets: 3
- High-risk tickets: 0
- Human gates: 0
- Risk note: Platform and product facts remain time-sensitive and must stay pending until source-scoped.

## Tickets

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-018` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current marketplace policy, return window, category restrictions and consumer protection rules | official marketplace policy center, consumer protection authority, merchant service agreement |
| `TICKET-SRC-019` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current product certification, recall, safety notice and warranty terms | brand official website, regulator recall database, warranty document |
| `TICKET-SRC-020` | [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | medium | `ecommerce-policy-reviewer` | no | current product price, stock, promotion, shipping fee and delivery ETA | platform product page, merchant backend, carrier tracking system |

## Evidence Fields To Fill

- `ticket_id`
- `status`
- `source_title`
- `source_publisher`
- `source_url_or_reference`
- `source_published_or_updated`
- `source_accessed_on`
- `verified_on`
- `evidence_summary`
- `affected_pages`
- `confidence`
- `remaining_uncertainty`
- `human_reviewer`
- `follow_up`

## Authoritative Source Targets

### TICKET-SRC-018

- Topic: current marketplace policy, return window, category restrictions and consumer protection rules
- Wiki: `ecommerce-agent-wiki`
- Evidence log: `wikis/ecommerce-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/ecommerce-agent-wiki/sources/source-notes.md`
- official marketplace policy center
- consumer protection authority
- merchant service agreement

### TICKET-SRC-019

- Topic: current product certification, recall, safety notice and warranty terms
- Wiki: `ecommerce-agent-wiki`
- Evidence log: `wikis/ecommerce-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/ecommerce-agent-wiki/sources/source-notes.md`
- brand official website
- regulator recall database
- warranty document

### TICKET-SRC-020

- Topic: current product price, stock, promotion, shipping fee and delivery ETA
- Wiki: `ecommerce-agent-wiki`
- Evidence log: `wikis/ecommerce-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/ecommerce-agent-wiki/sources/source-notes.md`
- platform product page
- merchant backend
- carrier tracking system

## Disallowed Sources

- unsourced summaries
- marketing copy without dates or scope
- scraped snippets without an authoritative source page
- private account data, cookies, API keys, private keys, seed phrases, or credentials
- outdated, conflicting, or jurisdiction-mismatched sources used as final authority

## Human Gate Notes

- High-risk tickets require a named human reviewer before any `verified` or `unchanged` status.
- If no reviewer is available, keep the ticket `pending` or `still-needs-source-update`.
- Keep nodeops operational boundaries visible; no production, wallet, firewall, billing, or upgrade action is authorized by this batch.

## Rollback Notes

- This batch writes planning artifacts only; rollback is removing generated batch docs/registry entries.
- If future evidence import fails, do not delete source logs blindly; add a corrective evidence entry or keep the ticket pending.
- Do not revert unrelated user changes.

## Acceptance Commands

```bash
python scripts\audit_source_review_packets.py
python scripts\rehearse_source_review_packet_imports.py
python scripts\audit_source_evidence_quality.py
python scripts\audit_source_refresh_completion.py
python scripts\audit_links.py
python scripts\run_acceptance.py
```
