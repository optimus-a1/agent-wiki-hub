# Source Review Wave 3 Packet Checklist

Generated: 2026-05-31

## Packet Files

- JSON packet: `registry/source-review-packets/source-review-session-wave-3-pending.json`
- JSONL packet: `registry/source-review-packets/source-review-session-wave-3-pending.jsonl`

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
python scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-3-pending.json --dry-run --no-post-checks
python scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-3-pending.jsonl --dry-run --no-post-checks
```

## Entries

| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic |
| --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-026` | agent-engineering-wiki | medium | `agent-engineering-reviewer` | no | current Codex Skill format, plugin behavior and tool capabilities |
| `TICKET-SRC-027` | agent-engineering-wiki | medium | `agent-engineering-reviewer` | no | current RAG frameworks, embedding models, vector databases and rerankers |
| `TICKET-SRC-028` | agent-engineering-wiki | medium | `agent-engineering-reviewer` | no | current eval harnesses, model APIs and MCP/tool schemas |
| `TICKET-SRC-029` | coding-agent-wiki | medium | `software-maintainer-reviewer` | no | current OpenAI, Codex, GitHub or Vercel product behavior |
| `TICKET-SRC-030` | coding-agent-wiki | medium | `software-maintainer-reviewer` | no | current cloud platform build, deploy, runtime and pricing behavior |
| `TICKET-SRC-031` | coding-agent-wiki | medium | `software-maintainer-reviewer` | no | current dependency vulnerabilities and security advisories |
| `TICKET-SRC-032` | coding-agent-wiki | medium | `software-maintainer-reviewer` | no | current framework, library, CLI and API parameters |
| `TICKET-SRC-033` | content-agent-wiki | low | `content-fact-check-reviewer` | no | current image, chart, dataset and quote licensing |
| `TICKET-SRC-034` | content-agent-wiki | low | `content-fact-check-reviewer` | no | current news, statistics, public quotes and social media claims |
| `TICKET-SRC-035` | content-agent-wiki | low | `content-fact-check-reviewer` | no | current publishing platform rules, format limits and content policies |
