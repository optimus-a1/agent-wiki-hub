---
title: Sample Tool Overreach
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Sample Tool Overreach

## Purpose
Show how an agent should handle a request that tempts unnecessary or unsafe tool execution.

## When to use
Use as a case pattern for tool-using agents that can read files, edit systems, call APIs, or run commands.

## Stable knowledge points
- KP-01: Tool overreach happens when an agent acts before it has enough scope, permission, or evidence.
- KP-02: A read-only check can often reduce uncertainty before any state-changing step.
- KP-03: User intent should be mapped to the smallest tool action that satisfies it.
- KP-04: A reversible local edit is lower risk than an external irreversible action.
- KP-05: Credentials should never be requested or exposed when a safer authentication path exists.
- KP-06: A tool result should be summarized with relevance, not dumped without context.
- KP-07: Refusal can be paired with a safer diagnostic or planning alternative.
- KP-08: Human confirmation is required when actions affect money, production, legal, health, security, or private data.

## Core rules
- Do not run state-changing tools without task-aligned need.
- Prefer inspection, validation, and dry-run modes.
- Stop on evidence of credential exposure.
- Keep audit trails for important actions.

## Workflow
1. Identify whether the request needs observation, modification, or external action.
2. Choose the lowest-risk tool path.
3. Ask or stop only when missing information creates material risk.
4. Execute, validate, and summarize the outcome.
5. Record blocked actions and safer alternatives.

## Edge cases
- A user can ask for speed while still needing safety gates.
- Tool output can contain sensitive data that must be redacted.
- A successful command can be outside the intended project.

## Validation checks
- The action matches the user goal.
- No hidden or unrelated operation occurred.
- Secrets are not printed or persisted.
- High-risk actions include explicit confirmation.

## Source notes
Stable agent behavior case only. No current platform-specific tool behavior is included.
