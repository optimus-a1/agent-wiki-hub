# Batch 2 - Customs P0 Review

Generated: 2026-05-31

## Purpose

Prepare source evidence collection for this wave-2 batch without browsing, verifying, importing, or writing current facts.

## Batch Summary

- Batch id: `batch-2-customs`
- Reviewer role: `customs-document-reviewer`
- Tickets: 4
- High-risk tickets: 0
- Human gates: 0
- Risk note: Customs topics require official, jurisdiction-specific sources before current facts can be used.

## Tickets

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-014` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | exchange rates, tariff rates, tax rates and destination-specific fees | central bank or official exchange source, customs tariff system, destination country authority |
| `TICKET-SRC-015` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest HS codes, customs supervision conditions and declaration elements | customs authority website, official tariff database, licensed customs broker review |
| `TICKET-SRC-016` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest import/export policy, inspection and quarantine requirements | customs and inspection authority announcement, destination country regulator, official trade compliance bulletin |
| `TICKET-SRC-017` | [customs-agent-wiki](../wikis/customs-agent-wiki) | medium | `customs-document-reviewer` | no | latest platform OCR model parameters and document template behavior | OCR vendor documentation, internal extraction benchmark, manually reviewed sample set |

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

### TICKET-SRC-014

- Topic: exchange rates, tariff rates, tax rates and destination-specific fees
- Wiki: `customs-agent-wiki`
- Evidence log: `wikis/customs-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- central bank or official exchange source
- customs tariff system
- destination country authority

### TICKET-SRC-015

- Topic: latest HS codes, customs supervision conditions and declaration elements
- Wiki: `customs-agent-wiki`
- Evidence log: `wikis/customs-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- customs authority website
- official tariff database
- licensed customs broker review

### TICKET-SRC-016

- Topic: latest import/export policy, inspection and quarantine requirements
- Wiki: `customs-agent-wiki`
- Evidence log: `wikis/customs-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- customs and inspection authority announcement
- destination country regulator
- official trade compliance bulletin

### TICKET-SRC-017

- Topic: latest platform OCR model parameters and document template behavior
- Wiki: `customs-agent-wiki`
- Evidence log: `wikis/customs-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- OCR vendor documentation
- internal extraction benchmark
- manually reviewed sample set

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
