# Source Refresh Log

Wiki: agent-engineering-wiki
Risk level: medium
Freshness requirement: medium
Template initialized: 2026-05-27

## Purpose

Record authoritative source verification work before current facts are written into this wiki.

## How To Use

1. Read `manifest.yaml`, `AGENTS.md`, `rules/`, and `sources/source-notes.md` first.
2. Pick a task from `docs/SOURCE_REFRESH_PLAYBOOK.md` or `registry/source-refresh-playbook.json`.
3. Verify the claim from authoritative sources before editing wiki content.
4. Record evidence below, including dates, source scope, confidence, and remaining uncertainty.
5. Update `sources/source-notes.md` and `update-log.md` after any content change.
6. Run validation and acceptance commands before release.

## Refresh Tasks

- [ ] SRC-026 | wave: wave-3 | priority: 6 | human_confirmation: no | topic: current Codex Skill format, plugin behavior and tool capabilities
- [ ] SRC-027 | wave: wave-3 | priority: 6 | human_confirmation: no | topic: current RAG frameworks, embedding models, vector databases and rerankers
- [ ] SRC-028 | wave: wave-3 | priority: 6 | human_confirmation: no | topic: current eval harnesses, model APIs and MCP/tool schemas

## Evidence Entry Template

```yaml
- task_id: SRC-000
  topic: <copy topic from playbook>
  status: pending | verified | unchanged | still-needs-source-update | rejected
  verified_on: YYYY-MM-DD
  source_title: <source title>
  source_publisher: <official publisher or authority>
  source_url_or_reference: <URL or local reference>
  source_published_or_updated: YYYY-MM-DD | unknown
  source_accessed_on: YYYY-MM-DD
  evidence_summary: <short summary of what the source supports>
  affected_pages:
    - sources/source-notes.md
  confidence: low | medium | high
  remaining_uncertainty: <what is still unknown or scope-limited>
  human_reviewer: <name/role or required>
  follow_up: <next action or none>
```

## Completed Entries

<Add completed evidence entries here. Do not record secrets, credentials, cookies, private keys, or private account data.>

## Safety Notes

- Do not write current facts into wiki pages without dated source evidence.
- Keep `needs-source-update` when sources are missing, conflicting, stale, or outside scope.
- High-risk domains keep human confirmation points even after source refresh is complete.
- Do not add personalized investment advice, final legal opinions, medical diagnoses, offensive security procedures, or platform-rule bypass guidance.
