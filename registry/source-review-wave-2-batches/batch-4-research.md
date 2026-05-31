# Batch 4 - Research P2 Review

Generated: 2026-05-31

## Purpose

Prepare source evidence collection for this wave-2 batch without browsing, verifying, importing, or writing current facts.

## Batch Summary

- Batch id: `batch-4-research`
- Reviewer role: `research-methods-reviewer`
- Tickets: 2
- High-risk tickets: 0
- Human gates: 0
- Risk note: Research artifacts require primary pages, repository/model-card evidence, and license checks.

## Tickets

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |
| --- | --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-024` | [research-agent-wiki](../wikis/research-agent-wiki) | medium | `research-methods-reviewer` | no | current dataset availability, license, model weights and code repository status | official dataset page, repository release notes, model card |
| `TICKET-SRC-025` | [research-agent-wiki](../wikis/research-agent-wiki) | medium | `research-methods-reviewer` | no | latest papers, preprints, revisions, citations and benchmark leaderboards | publisher page, arXiv or conference page, official benchmark leaderboard |

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

### TICKET-SRC-024

- Topic: current dataset availability, license, model weights and code repository status
- Wiki: `research-agent-wiki`
- Evidence log: `wikis/research-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/research-agent-wiki/sources/source-notes.md`
- official dataset page
- repository release notes
- model card

### TICKET-SRC-025

- Topic: latest papers, preprints, revisions, citations and benchmark leaderboards
- Wiki: `research-agent-wiki`
- Evidence log: `wikis/research-agent-wiki/sources/source-refresh-log.md`
- Source notes: `wikis/research-agent-wiki/sources/source-notes.md`
- publisher page
- arXiv or conference page
- official benchmark leaderboard

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
