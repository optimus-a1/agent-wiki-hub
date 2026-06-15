---
title: Incident Triage Runbook
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Incident Triage Runbook

## Purpose
Provide a stable incident triage workflow for service or node operations without issuing unsafe production commands.

## When to use
Use when a service is slow, unavailable, unstable, or producing abnormal logs.

## Stable knowledge points
- KP-01: Triage starts by defining user impact and severity.
- KP-02: The timeline should include symptoms, alerts, deployments, config changes, and external dependencies.
- KP-03: Mitigation can be different from root-cause fix.
- KP-04: A rollback should be evaluated against current state, not treated as automatically safe.
- KP-05: Communication should state known facts, unknowns, actions, and next update time.
- KP-06: Evidence should be collected before it disappears, but not at the cost of worsening impact.
- KP-07: Incident roles reduce confusion by separating command, investigation, communication, and execution.
- KP-08: Post-incident review should focus on system improvement rather than blame.

## Core rules
- Do not run destructive or production-changing actions automatically.
- Redact secrets and private data from logs.
- Prefer reversible mitigations.
- Escalate when impact, authority, or safety is unclear.

## Workflow
1. Declare impact, severity, affected components, and owner.
2. Freeze context: time window, recent changes, alerts, and visible symptoms.
3. Inspect metrics, logs, traces, capacity, and dependency health.
4. Choose a low-risk mitigation or escalation path.
5. Validate recovery and write a follow-up review.

## Edge cases
- Multiple simultaneous failures can create misleading correlations.
- An alert can be correct while its label points to the wrong layer.
- A mitigation can hide evidence needed for root-cause analysis.

## Validation checks
- User impact is stated.
- Actions are separated into observe, mitigate, fix, and follow-up.
- Human confirmation exists for production changes.
- Incident notes avoid sensitive data.

## Source notes
Stable runbook pattern only. No current provider dashboards, node versions, or incident data are included.
