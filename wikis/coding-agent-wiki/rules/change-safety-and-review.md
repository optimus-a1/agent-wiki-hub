---
title: Change Safety And Review
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Change Safety And Review

## Purpose
Define stable safety rules for code edits, reviews, and delivery.

## When to use
Use before modifying shared code, handling a mixed worktree, or preparing a commit.

## Stable knowledge points
- KP-01: Safe changes have a clear problem statement, scoped files, and observable verification.
- KP-02: A code review should prioritize bugs, regressions, missing tests, and operational risk.
- KP-03: Refactoring is safest when behavior is locked by tests or simple invariants.
- KP-04: Public interfaces require more caution than private implementation details.
- KP-05: Secrets must never appear in commits, logs, fixtures, screenshots, or generated reports.
- KP-06: Backward compatibility depends on callers, data shape, configuration, and deployment order.
- KP-07: Rollback planning is part of safe delivery when changes affect runtime behavior.
- KP-08: A clean final report should state what changed, how it was checked, and what remains risky.

## Core rules
- Do not revert user changes unless explicitly asked.
- Do not commit local secrets or environment-specific files.
- Keep comments useful and sparse.
- Run the most relevant available checks.

## Workflow
1. Confirm the intended scope from the request and local instructions.
2. Inspect status and nearby code before editing.
3. Patch only the necessary files.
4. Run focused tests, then broader checks when risk warrants.
5. Summarize changed files, verification, and residual risk.

## Edge cases
- Formatting tools can create large diffs unrelated to the fix.
- A test can pass while an integration contract is broken.
- A patch can be correct but unsafe to deploy without migration order.

## Validation checks
- No secrets are staged or printed.
- Diff is explainable file by file.
- Tests align with changed behavior.
- Rollback or mitigation is documented when needed.

## Source notes
Stable engineering review rules only. No current platform policies, dependency versions, or API parameters are included.
