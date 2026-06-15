---
title: Codebase Orientation
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Codebase Orientation

## Purpose
Explain stable principles for understanding a codebase before making changes.

## When to use
Use when an agent enters an unfamiliar repository, prepares a patch, or reviews an implementation request.

## Stable knowledge points
- KP-01: Entry points reveal how users, systems, and tests interact with the code.
- KP-02: Project conventions reduce risk because they encode local decisions and tradeoffs.
- KP-03: Dependency boundaries show where behavior belongs and where changes should not leak.
- KP-04: Tests describe intended behavior, but missing tests do not prove behavior is unimportant.
- KP-05: Configuration files often define runtime assumptions that code alone does not show.
- KP-06: Error handling patterns reveal what failures the system already expects.
- KP-07: A minimal patch should fit the existing shape before introducing new abstractions.
- KP-08: Reading recent changes helps avoid overwriting user work or repeating rejected designs.

## Core rules
- Read instructions, manifests, tests, and local style before editing.
- Prefer existing helpers and patterns over new frameworks.
- Keep scope tied to the user request.
- Preserve unrelated worktree changes.

## Workflow
1. Identify build system, language, entry points, and test commands.
2. Map the target feature or bug to files, modules, and interfaces.
3. Read nearby tests, fixtures, and examples.
4. Make the smallest coherent change.
5. Verify behavior and document remaining risk.

## Edge cases
- Generated files may look editable but require changing a source template.
- Monorepos can hide cross-package contracts.
- A failing test may reflect environment setup rather than product behavior.

## Validation checks
- The patch follows local naming, formatting, and module structure.
- Tests or manual checks cover the changed behavior.
- No unrelated files are modified.
- Secrets and local environment files remain uncommitted.

## Source notes
Stable software engineering principles only. No current library versions, APIs, or platform behavior are included.
