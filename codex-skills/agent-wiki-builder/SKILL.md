---
name: agent-wiki-builder
description: Use this skill when creating, expanding, validating, indexing, or packaging Agent Wiki Hub knowledge packs. Triggers: knowledge base, agent wiki, RAG pack, manifest, evals, AGENTS.md, Codex instructions.
---

# Agent Wiki Builder Skill

## When to use

Use this skill when the user asks to build, improve, search, package, or connect an Agent Knowledge Pack.

## Required workflow

1. Read the repository root `AGENTS.md`.
2. Read `registry/wiki-registry.yaml`.
3. Identify the target wiki.
4. Read target `manifest.yaml`, `README.md`, and local `AGENTS.md`.
5. Add or revise pages using the standard page format.
6. Update `sources/source-notes.md` for any facts requiring freshness.
7. Update `update-log.md`.
8. Run:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
```

## Quality rules

- Keep stable knowledge in `concepts/`, `rules/`, `workflows/`, `cases/`, `tools/`, `prompts/`, and `evals/`.
- Keep live/current facts in `sources/` with update status.
- High-risk domains must include safety boundaries.
- Do not invent source-backed claims.
