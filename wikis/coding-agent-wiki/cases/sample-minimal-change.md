---
title: Sample Minimal Change
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Sample Minimal Change

## Purpose
Show how a coding agent should avoid unnecessary refactors while fixing a focused defect.

## When to use
Use as a case pattern when the requested fix touches code that tempts broad cleanup.

## Stable knowledge points
- KP-01: The smallest useful change still needs to be complete enough to solve the user-visible problem.
- KP-02: Nearby code style is a constraint unless it conflicts with correctness or safety.
- KP-03: New abstractions should pay for themselves by reducing real complexity.
- KP-04: A focused bug fix can include a focused test without redesigning the subsystem.
- KP-05: Unrelated cleanup increases review burden and regression surface.
- KP-06: Local helper reuse is usually safer than introducing a new dependency.
- KP-07: Comments should explain non-obvious reasoning, not narrate simple statements.
- KP-08: A final answer should identify checks run and any checks not run.

## Core rules
- Patch the defect path first.
- Add tests proportional to risk.
- Leave unrelated formatting alone.
- Explain why broader refactors were not needed.

## Workflow
1. Read the failing code path and existing tests.
2. Identify the minimal behavioral correction.
3. Patch the narrowest file set.
4. Add a regression test or a direct verification step.
5. Report the diff and verification result.

## Edge cases
- A small patch is not enough if the bug is caused by a shared contract.
- A test-only fix may hide missing production behavior.
- A local workaround can become debt if it bypasses a central invariant.

## Validation checks
- Diff scope matches the request.
- Behavior is verified before final response.
- No secrets or local-only files are included.
- Remaining risk is clear.

## Source notes
Stable case guidance only. No current API or product behavior is included.
