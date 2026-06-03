---
title: Secret Handling And Log Redaction
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Secret Handling And Log Redaction

## Purpose
Provide stable defensive rules for handling credentials, tokens, private keys, and sensitive logs.

## When to use
Use when reviewing code, logs, configuration, CI output, incident notes, or repository contents.

## Stable knowledge points
- KP-01: Secrets include credentials, tokens, private keys, session material, signing keys, and recovery phrases.
- KP-02: A secret should be stored only in an approved secret-management path, not in source files.
- KP-03: Logs should record enough context for diagnosis without exposing secret values.
- KP-04: Redaction should remove the value while preserving the field name and evidence that a secret was present.
- KP-05: Once a secret is exposed to an untrusted location, rotation or revocation may be required.
- KP-06: Test fixtures should use obvious placeholders that cannot authenticate.
- KP-07: Screenshots, crash reports, and generated bundles can leak secrets just like code.
- KP-08: Commit history matters because removing a secret from the latest file may not remove exposure.

## Core rules
- Never print, copy, commit, or summarize secret values.
- Report only file path, field name, and risk category.
- Stop before publishing if real secrets are found in trackable files or history.
- Keep remediation defensive and authorized.

## Workflow
1. Scan candidate files for secret fields and secret-like values.
2. Classify hits as ignored local files, placeholders, or trackable real secrets.
3. Redact or replace trackable secrets with placeholders.
4. Check staging and history before release.
5. Recommend rotation when exposure cannot be ruled out.

## Edge cases
- A value can be fake but still match a secret pattern.
- A partial token can still be sensitive when combined with context.
- Generated reports may contain copied command output.

## Validation checks
- No secret values appear in responses.
- Ignored local secret files remain untracked.
- Placeholder examples are clearly empty or fake.
- History checks are performed before publishing.

## Source notes
Stable defensive secret-handling rules only. No real credentials, current provider policy, or vendor-specific token format is included.
