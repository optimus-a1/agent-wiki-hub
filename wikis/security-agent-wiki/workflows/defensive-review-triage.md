---
title: Defensive Review Triage
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Defensive Review Triage

## Purpose
Provide a stable workflow for triaging defensive security findings without enabling misuse.

## When to use
Use for code review, configuration review, release checks, or incident-adjacent defensive analysis.

## Stable knowledge points
- KP-01: Triage starts by confirming authorization and scope.
- KP-02: A finding should identify asset, exposure, impact, likelihood, and evidence.
- KP-03: Severity should reflect real impact and exploitability without giving exploitation steps.
- KP-04: Remediation should prefer reducing blast radius and removing root cause.
- KP-05: Compensating controls can reduce risk but should not hide unresolved issues.
- KP-06: Sensitive evidence should be minimized, redacted, and access-controlled.
- KP-07: Verification should prove the defensive fix works without attacking a live target.
- KP-08: Risk acceptance requires explicit ownership and time-bound review.

## Core rules
- Stay within authorized defensive scope.
- Avoid exploit payloads, bypass steps, persistence, or credential theft instructions.
- Provide safe reproduction descriptions when needed.
- Escalate high-impact findings to human owners.

## Workflow
1. Confirm scope, asset owner, and review objective.
2. Collect safe evidence from code, configuration, logs, or documented behavior.
3. Classify impact, likelihood, affected data, and control gaps.
4. Recommend defensive fixes and verification checks.
5. Record residual risk, owner, and human approval needs.

## Edge cases
- A low-severity issue can become serious when chained with other weaknesses.
- A scanner result can be false positive or false negative.
- A fix can break availability if applied without operational review.

## Validation checks
- No offensive steps are present.
- Evidence is redacted and scoped.
- Remediation is actionable and defensive.
- Human gates are preserved for high-risk changes.

## Source notes
Stable defensive workflow only. No current vulnerabilities, signatures, advisories, or exploit details are included.
