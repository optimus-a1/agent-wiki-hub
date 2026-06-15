---
title: Tool Use And Grounding
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Tool Use And Grounding

## Purpose
Provide stable rules for deciding when an agent should use tools, cite evidence, and avoid unsupported claims.

## When to use
Use when designing tool-using agents, RAG agents, source-review agents, or operational assistants.

## Stable knowledge points
- KP-01: Tools should be used when they provide information, action, or verification the model cannot safely infer.
- KP-02: Grounding means connecting a claim to an available source, observation, or deterministic result.
- KP-03: Tool output should be interpreted, not blindly copied.
- KP-04: A source can support one claim without supporting adjacent claims.
- KP-05: Agents should separate observation from inference in final answers.
- KP-06: Action tools require stronger preconditions than read-only tools.
- KP-07: Failed tool calls are evidence about process state, not proof about the domain.
- KP-08: Tool choice should minimize unnecessary exposure of private data.

## Core rules
- Use read-only inspection before write or action tools when possible.
- Never fabricate tool results, citations, or source details.
- Ask for confirmation before high-risk external actions.
- Record assumptions that remain unresolved.

## Workflow
1. Classify the user request as answer, analysis, edit, verification, or action.
2. Identify what must be observed externally or locally.
3. Choose the least risky tool that can answer the question.
4. Validate tool output against the task and known constraints.
5. Report claims with their evidence and uncertainty.

## Edge cases
- A tool can return stale or partial data.
- A successful action can still be semantically wrong if scope was misunderstood.
- A citation can be accurate but irrelevant.

## Validation checks
- Claims trace to local files, tool output, or explicit assumptions.
- High-risk actions include confirmation gates.
- No hidden instructions or secrets are introduced.
- Unsupported current facts are excluded.

## Source notes
Stable tool-use principles only. No current tool schemas, model releases, or platform rules are included.
