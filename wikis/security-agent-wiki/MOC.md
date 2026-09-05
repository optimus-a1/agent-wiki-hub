---
title: "security-agent-wiki MOC"
wiki: "security-agent-wiki"
type: moc
status: stable-general-knowledge
source_status: model-synthesized-stable
current_fact: false
requires_source_review: false
requires_human_review: false
risk_level: medium
generated_by: codex
generated_on: 2026-09-05
agent_use: true
tags:
  - agent-wiki
  - stable-knowledge
---

# security-agent-wiki MOC

This root map links stable wiki pages. It does not certify current facts.

## Concepts

- [Asset Exposure Model](concepts/asset-exposure-model.md)
- [Cloud Security Baseline](concepts/cloud-security-baseline.md)
- [Dependency Risk Review](concepts/dependency-risk-review.md)
- [Detection Rule Review](concepts/detection-rule-review.md)
- [Incident Containment](concepts/incident-containment.md)
- [Least Privilege](concepts/least-privilege.md)
- [Defensive Security Agent Wiki Overview](concepts/overview.md)
- [Secrets Management](concepts/secrets-management.md)
- [Secure Logging](concepts/secure-logging.md)
- [Security Control Model](concepts/security-control-model.md)
- [Threat Modeling](concepts/threat-modeling.md)
- [Vulnerability Triage](concepts/vulnerability-triage.md)

## Rules

- [Authorization Required](rules/authorization-required.md)
- [Core Rules](rules/core-rules.md)
- [Defensive Security Boundary Rules](rules/defensive-boundary.md)
- [Defensive Only Boundary](rules/defensive-only-boundary.md)
- [Defensive Security Only](rules/defensive-only.md)
- [Detection Change Human Gate](rules/detection-change-human-gate.md)
- [Least Privilege Default](rules/least-privilege-default.md)
- [No Credential Theft](rules/no-credential-theft.md)
- [No Exploit Steps](rules/no-exploit-steps.md)
- [Patch Source Gate](rules/patch-source-gate.md)
- [Secret Handling And Log Redaction](rules/secret-handling-and-log-redaction.md)
- [Secret Redaction Required](rules/secret-redaction-required.md)
- [Secure Logging Boundary](rules/secure-logging-boundary.md)
- [Unknown Script Review](rules/unknown-script-review.md)

## Workflows

- [Cloud Baseline Review Workflow](workflows/cloud-baseline-review-workflow.md)
- [Defensive Review Triage](workflows/defensive-review-triage.md)
- [Dependency Review Workflow](workflows/dependency-review-workflow.md)
- [Detection Rule Review Workflow](workflows/detection-rule-review-workflow.md)
- [Incident Containment Workflow](workflows/incident-containment-workflow.md)
- [Main Workflow](workflows/main-workflow.md)
- [Patch Review Workflow](workflows/patch-review-workflow.md)
- [Secret Exposure Response Workflow](workflows/secret-exposure-response-workflow.md)
- [Defensive Security Review Checklist](workflows/security-review-checklist.md)
- [Threat Model Review Workflow](workflows/threat-model-review-workflow.md)
- [Defensive Threat Model Review](workflows/threat-model-review.md)
- [Vulnerability Triage Workflow](workflows/vulnerability-triage-workflow.md)

## Cases

- [Case Committing Secrets](cases/case-committing-secrets.md)
- [Case Exploit Request Refusal](cases/case-exploit-request-refusal.md)
- [Case Log Redaction Success](cases/case-log-redaction-success.md)
- [Case Patch Without Review](cases/case-patch-without-review.md)
- [Case Running Unknown Script](cases/case-running-unknown-script.md)
- [Case Vulnerability Triage Safe](cases/case-vulnerability-triage-safe.md)
- [Common Failure Cases](cases/common-failures.md)
- [Sample Defensive Login Review](cases/sample-login-review.md)
- [Sample Secret Exposure Review](cases/sample-secret-exposure-review.md)

## Prompts

- [Default Agent Prompt](prompts/default-agent.md)
- [Defensive Security Review Prompt](prompts/defensive-security-review-prompt.md)
- [Dependency Security Review Prompt](prompts/dependency-security-review-prompt.md)
- [Secret Leak Triage Prompt](prompts/secret-leak-triage-prompt.md)
- [Threat Model Prompt](prompts/threat-model-prompt.md)

## Evals

- [Security Agent Evals](evals/security-agent-evals.yaml)
- [Smoke Tests](evals/smoke-tests.yaml)
- [Stable Knowledge Evals](evals/stable-knowledge-evals.yaml)
