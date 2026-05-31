# Batch 1 - NodeOps High-Risk Review

Generated: 2026-05-31

## Purpose

Prepare source evidence collection for this wave-2 batch without browsing, verifying, importing, or writing current facts.

## Batch Summary

- Batch id: `batch-1-nodeops`
- Reviewer role: `operations-change-reviewer`
- Tickets: 3
- High-risk tickets: 3
- Human gates: 3
- Risk note: High-risk operations topics require named human confirmation before any final status.

## Tickets

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-021` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current OS package, Docker, systemd and kernel behavior | official documentation, local version output, release notes |
| `TICKET-SRC-022` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current blockchain node client versions, network parameters and upgrade requirements | official client release notes, chain foundation announcement, node logs and version output |
| `TICKET-SRC-023` | [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | high | `operations-change-reviewer` | yes | current cloud provider limits, firewall behavior, billing and incident status | cloud provider documentation, status page, account console |

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

### TICKET-SRC-021

- Topic: current OS package, Docker, systemd and kernel behavior
- Wiki: `nodeops-agent-wiki`
- Evidence log: `wikis/nodeops-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/nodeops-agent-wiki/sources/source-notes.md`
- official documentation
- local version output
- release notes

### TICKET-SRC-022

- Topic: current blockchain node client versions, network parameters and upgrade requirements
- Wiki: `nodeops-agent-wiki`
- Evidence log: `wikis/nodeops-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/nodeops-agent-wiki/sources/source-notes.md`
- official client release notes
- chain foundation announcement
- node logs and version output

### TICKET-SRC-023

- Topic: current cloud provider limits, firewall behavior, billing and incident status
- Wiki: `nodeops-agent-wiki`
- Evidence log: `wikis/nodeops-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/nodeops-agent-wiki/sources/source-notes.md`
- cloud provider documentation
- status page
- account console

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
