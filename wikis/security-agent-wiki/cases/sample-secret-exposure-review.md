---
title: Sample Secret Exposure Review
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Sample Secret Exposure Review

## Purpose
Show how a defensive security agent should report possible secret exposure without revealing the secret.

## When to use
Use as a case pattern for repository scans, release checks, CI logs, or pasted diagnostic output.

## Stable knowledge points
- KP-01: The agent should never echo the suspected secret value.
- KP-02: The safe report identifies path, field name, status, and required action.
- KP-03: Ignored local files can still be risky if copied into reports or history.
- KP-04: Trackable files with real secrets should block release.
- KP-05: Placeholders should be clearly nonfunctional.
- KP-06: If exposure reached shared history or external systems, rotation should be considered.
- KP-07: Redaction must preserve enough context for humans to locate the issue.
- KP-08: The final check should confirm ignore rules, staging state, and commit history.

## Core rules
- Do not print token substrings.
- Do not write tokens into remote URLs, docs, commits, or examples.
- Stop publishing when a real secret appears in trackable content.
- Keep recommendations defensive.

## Workflow
1. Scan files and classify hits without printing values.
2. Confirm whether each hit is ignored, staged, tracked, or committed.
3. Replace trackable secrets with empty placeholders.
4. Run validation and history checks.
5. Report status and remaining human actions.

## Edge cases
- A token can be hidden in generated JSON or packaged archives.
- A false positive can still indicate dangerous wording in docs.
- A secret removed from the worktree can remain in previous commits.

## Validation checks
- Report includes no secret values.
- `.env`-style local files are ignored.
- Trackable files contain placeholders only.
- Release is blocked if history exposure is detected.

## Source notes
Stable defensive case only. No real token, provider policy, or current credential format is included.
