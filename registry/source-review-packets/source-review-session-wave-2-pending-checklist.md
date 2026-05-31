# Source Review Wave 2 Packet Checklist

Generated: 2026-05-31

## Packet Files

- JSON packet: `registry/source-review-packets/source-review-session-wave-2-pending.json`
- JSONL packet: `registry/source-review-packets/source-review-session-wave-2-pending.jsonl`

## Safety

- This packet is planning-only pending evidence.
- It does not verify, certify, import, or write current facts.
- Every entry must remain `status=pending` until a reviewer replaces placeholders with authoritative evidence.
- Do not add API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.
- Do not delete or overwrite wave-1 artifacts.

## Required Field State

- `status`: `pending`
- `verified_on`: empty string
- `confidence`: `low`
- `human_reviewer`: `<reviewer>`
- `evidence_summary`: `<what the source supports and does not support>`

## Dry Run

```bash
python scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-2-pending.json --dry-run --no-post-checks
python scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-2-pending.jsonl --dry-run --no-post-checks
```

## Entries

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-021` | nodeops-agent-wiki | high | `operations-change-reviewer` | yes | current OS package, Docker, systemd and kernel behavior |
| `TICKET-SRC-022` | nodeops-agent-wiki | high | `operations-change-reviewer` | yes | current blockchain node client versions, network parameters and upgrade requirements |
| `TICKET-SRC-023` | nodeops-agent-wiki | high | `operations-change-reviewer` | yes | current cloud provider limits, firewall behavior, billing and incident status |
| `TICKET-SRC-014` | customs-agent-wiki | medium | `customs-document-reviewer` | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| `TICKET-SRC-015` | customs-agent-wiki | medium | `customs-document-reviewer` | no | latest HS codes, customs supervision conditions and declaration elements |
| `TICKET-SRC-016` | customs-agent-wiki | medium | `customs-document-reviewer` | no | latest import/export policy, inspection and quarantine requirements |
| `TICKET-SRC-017` | customs-agent-wiki | medium | `customs-document-reviewer` | no | latest platform OCR model parameters and document template behavior |
| `TICKET-SRC-018` | ecommerce-agent-wiki | medium | `ecommerce-policy-reviewer` | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| `TICKET-SRC-019` | ecommerce-agent-wiki | medium | `ecommerce-policy-reviewer` | no | current product certification, recall, safety notice and warranty terms |
| `TICKET-SRC-020` | ecommerce-agent-wiki | medium | `ecommerce-policy-reviewer` | no | current product price, stock, promotion, shipping fee and delivery ETA |
| `TICKET-SRC-024` | research-agent-wiki | medium | `research-methods-reviewer` | no | current dataset availability, license, model weights and code repository status |
| `TICKET-SRC-025` | research-agent-wiki | medium | `research-methods-reviewer` | no | latest papers, preprints, revisions, citations and benchmark leaderboards |
