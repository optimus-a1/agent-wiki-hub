---
title: Service Reliability Signals
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Service Reliability Signals

## Purpose
Define stable operational signals for understanding service health without depending on vendor-specific metrics.

## When to use
Use when triaging incidents, designing monitoring, or explaining operational risk.

## Stable knowledge points
- KP-01: Availability describes whether a service can perform its intended function for users.
- KP-02: Latency describes how long a successful operation takes, often by percentile rather than average alone.
- KP-03: Error rate describes failed operations and should be interpreted with traffic volume.
- KP-04: Saturation describes how close a resource is to exhaustion.
- KP-05: Throughput describes work completed per time interval and can hide degraded user experience.
- KP-06: Logs provide event context, while metrics provide aggregate shape.
- KP-07: Traces connect work across components and help locate slow or failing boundaries.
- KP-08: Alerts should map to user impact or actionable risk, not noise alone.

## Core rules
- Observe before changing production systems.
- Separate symptom, suspected cause, and confirmed cause.
- Protect credentials and private user data in logs.
- Require human approval for risky operations.

## Workflow
1. Identify the affected service, user impact, and time window.
2. Review availability, latency, error rate, saturation, and recent changes.
3. Compare logs, metrics, and traces for the same time interval.
4. Form hypotheses and test them with low-risk observations.
5. Document findings, mitigations, and follow-up work.

## Edge cases
- A dependency failure can appear as local latency.
- A low error rate can still be severe if concentrated on a critical path.
- Missing telemetry is itself an operational risk.

## Validation checks
- Signal definitions are clear.
- User impact is separated from internal symptoms.
- No production change is made by default.
- Sensitive log content is redacted.

## Source notes
Stable reliability concepts only. No current infrastructure, provider, chain, or node version facts are included.
