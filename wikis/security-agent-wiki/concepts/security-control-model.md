---
title: Security Control Model
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Security Control Model

## Purpose
Define stable defensive security control concepts for audits, design reviews, and pre-release checks.

## When to use
Use when explaining how preventive, detective, and corrective controls reduce risk.

## Stable knowledge points
- KP-01: Preventive controls try to stop unsafe actions before they happen.
- KP-02: Detective controls identify suspicious or failed behavior after observation.
- KP-03: Corrective controls restore safe state or reduce impact after a failure.
- KP-04: Least privilege limits what a compromised or mistaken actor can do.
- KP-05: Defense in depth assumes one control can fail and layers independent protections.
- KP-06: Secure defaults reduce reliance on perfect user or operator behavior.
- KP-07: Auditability makes important actions attributable and reviewable.
- KP-08: Risk acceptance should be explicit, scoped, and approved by accountable humans.

## Core rules
- Keep analysis defensive and authorized.
- Do not provide exploit, evasion, persistence, or credential theft steps.
- Redact secrets in examples and logs.
- Require human approval for high-risk remediation.

## Workflow
1. Identify assets, actors, trust boundaries, and data flows.
2. Map threats to preventive, detective, and corrective controls.
3. Review gaps by severity, likelihood, and business impact.
4. Recommend defensive mitigations and verification checks.
5. Record residual risk and human decision points.

## Edge cases
- A control can exist on paper but fail operationally.
- Too many alerts can weaken detection by causing fatigue.
- Centralized secrets can improve management but increase blast radius if poorly controlled.

## Validation checks
- Recommendations are defensive.
- No attack procedure is included.
- Secrets are not exposed.
- Residual risk and ownership are documented.

## Source notes
Stable security control principles only. No current vulnerability, patch, compliance, or vendor configuration facts are included.
