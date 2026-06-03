---
title: Agent Eval Loop
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Agent Eval Loop

## Purpose
Describe a stable evaluation loop for improving agent behavior without relying on changing benchmark facts.

## When to use
Use when creating regression tests, behavior tests, source-grounding tests, or safety checks for an agent.

## Stable knowledge points
- KP-01: Evals should test behavior that matters to users, not only wording similarity.
- KP-02: Golden questions capture expected decisions, refusals, clarifications, and outputs.
- KP-03: Behavior tests should include positive cases, negative cases, and edge cases.
- KP-04: Source-grounding tests check whether claims are supported by provided material.
- KP-05: Safety tests should cover prohibited actions and required human confirmations.
- KP-06: Regression tests protect previously fixed failures from returning.
- KP-07: An eval result is useful when it points to a fixable prompt, workflow, tool, or knowledge issue.
- KP-08: Evals need review because test suites can become stale or incomplete.

## Core rules
- Define pass criteria before running the test.
- Keep test inputs free of secrets.
- Separate deterministic checks from human judgment.
- Track failures by root cause category.

## Workflow
1. Identify target behaviors and safety boundaries.
2. Write representative prompts with expected behavior.
3. Run the agent or implementation under controlled conditions.
4. Classify failures as instruction, retrieval, tool, reasoning, or safety issues.
5. Update prompts, rules, tools, or knowledge packs and rerun tests.

## Edge cases
- A response can be fluent but unsupported.
- A strict test can reject an acceptable paraphrase.
- A passing eval can miss a workflow failure outside the test scope.

## Validation checks
- Tests include refusal and uncertainty behavior.
- Expected outputs are checkable.
- Failures are linked to corrective actions.
- High-risk domains include human gate cases.

## Source notes
Stable evaluation design only. No current benchmark rankings, model scores, or tool versions are included.
