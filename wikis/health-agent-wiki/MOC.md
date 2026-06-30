---
title: "health-agent-wiki MOC"
wiki: "health-agent-wiki"
type: moc
status: stable-general-knowledge
source_status: model-synthesized-stable
current_fact: false
requires_source_review: false
requires_human_review: false
risk_level: medium
generated_by: codex
generated_on: 2026-06-30
agent_use: true
tags:
  - agent-wiki
  - stable-knowledge
---

# health-agent-wiki MOC

This root map links stable wiki pages. It does not certify current facts.

## Concepts

- [Clinician Review Role](concepts/clinician-review-role.md)
- [Health Education Boundary](concepts/health-education-boundary.md)
- [Lab Result Explanation Limits](concepts/lab-result-explanation-limits.md)
- [Health Education Agent Wiki Overview](concepts/overview.md)
- [Red Flag Escalation](concepts/red-flag-escalation.md)
- [Risk And Uncertainty Language](concepts/risk-and-uncertainty-language.md)
- [Symptom Context Factors](concepts/symptom-context-factors.md)

## Rules

- [Clinical Guideline Source Gate](rules/clinical-guideline-source-gate.md)
- [Core Rules](rules/core-rules.md)
- [Emergency Red Flag Escalation](rules/emergency-red-flag-escalation.md)
- [Licensed Clinician Review Required](rules/licensed-clinician-review-required.md)
- [Health Boundary Rules](rules/no-diagnosis.md)
- [No Dosage Instruction](rules/no-dosage-instruction.md)
- [No Treatment Plan Without Clinician](rules/no-treatment-plan-without-clinician.md)

## Workflows

- [Clinician Handoff Summary Workflow](workflows/clinician-handoff-summary-workflow.md)
- [Educational Explanation Workflow](workflows/educational-explanation-workflow.md)
- [Health Education Triage Workflow](workflows/health-education-triage.md)
- [Health Question Triage Workflow](workflows/health-question-triage-workflow.md)
- [Main Workflow](workflows/main-workflow.md)
- [Red Flag Escalation Workflow](workflows/red-flag-escalation-workflow.md)

## Cases

- [Case Diagnosis Request Refusal](cases/case-diagnosis-request-refusal.md)
- [Case Dosage Request Boundary](cases/case-dosage-request-boundary.md)
- [Case Educational Report Explanation](cases/case-educational-report-explanation.md)
- [Case Red Flag Escalation](cases/case-red-flag-escalation.md)
- [Common Failure Cases](cases/common-failures.md)
- [Sample Lab Report Explanation](cases/sample-lab-report-explanation.md)

## Prompts

- [Clinician Handoff Prompt](prompts/clinician-handoff-prompt.md)
- [Default Agent Prompt](prompts/default-agent.md)
- [Health Education Triage Prompt](prompts/health-education-triage-prompt.md)
- [Red Flag Screening Prompt](prompts/red-flag-screening-prompt.md)

## Evals

- [Health Agent Evals](evals/health-agent-evals.yaml)
- [Smoke Tests](evals/smoke-tests.yaml)
- [Stable Knowledge Evals](evals/stable-knowledge-evals.yaml)
