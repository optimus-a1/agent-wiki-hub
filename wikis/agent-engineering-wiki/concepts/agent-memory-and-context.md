---
title: Agent Memory And Context
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Agent Memory And Context

## Purpose
Define stable concepts for agent context, memory, handoff state, and knowledge boundaries.

## When to use
Use when designing agents that must remember task state, retrieve knowledge, or continue work across turns.

## Stable knowledge points
- KP-01: Context is the information currently available to the model; memory is information deliberately preserved for later use.
- KP-02: Working memory should contain active goals, constraints, decisions, and unresolved blockers.
- KP-03: Long-term memory should store durable user preferences and stable project facts, not transient guesses.
- KP-04: Retrieval memory is useful when it can cite or identify the source of recalled information.
- KP-05: Handoff records should distinguish completed work, pending work, assumptions, and risks.
- KP-06: Memory can become harmful when stale, private, or overgeneralized.
- KP-07: Agents should prefer explicit local instructions over inferred habits.
- KP-08: Memory design needs deletion, correction, and conflict-handling paths.

## Core rules
- Store only information with a clear future use.
- Separate user-provided facts from agent inferences.
- Preserve provenance whenever memory affects decisions.
- Avoid storing secrets or sensitive personal data.

## Workflow
1. Identify what the agent must remember to complete the task.
2. Classify memory as working, episodic, long-term, or retrieval-backed.
3. Attach provenance, confidence, and expiry needs.
4. Use memory only when relevant to the current task.
5. Update or discard memory when contradicted.

## Edge cases
- A compacted context can omit details that need explicit handoff.
- A memory can be true in one project and false in another.
- A retrieved document can be relevant but stale.

## Validation checks
- Memory contents are necessary and scoped.
- Sensitive data is excluded.
- Conflicts are surfaced instead of silently resolved.
- Human review is required for high-risk memory use.

## Source notes
Stable agent design principles only. No current tool, model, or platform capabilities are included.
