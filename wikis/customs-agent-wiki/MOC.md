---
title: "customs-agent-wiki MOC"
wiki: "customs-agent-wiki"
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

# customs-agent-wiki MOC

This root map links stable wiki pages. It does not certify current facts.

## Concepts

- [Amount Currency Consistency](concepts/amount-currency-consistency.md)
- [Certificate Of Conformity Review](concepts/certificate-of-conformity-review.md)
- [Commercial Invoice Structure](concepts/commercial-invoice-structure.md)
- [Contract Field Alignment](concepts/contract-field-alignment.md)
- [Declaration Element Model](concepts/declaration-element-model.md)
- [Trade Document Types](concepts/document-types.md)
- [Factory Inspection Document Review](concepts/factory-inspection-document-review.md)
- [Gross Weight Vs Net Weight Checks](concepts/gross-weight-vs-net-weight-checks.md)
- [OCR Field Confidence](concepts/ocr-field-confidence.md)
- [Customs Document Agent Wiki Overview](concepts/overview.md)
- [Package Count Reconciliation](concepts/package-count-reconciliation.md)
- [Packing List Structure](concepts/packing-list-structure.md)

## Rules

- [Core Rules](rules/core-rules.md)
- [Currency And Amount Gate](rules/currency-and-amount-gate.md)
- [Customs Policy Source Gate](rules/customs-policy-source-gate.md)
- [Do Not Invent Missing Values](rules/do-not-invent-missing-values.md)
- [Document Version Control](rules/document-version-control.md)
- [Customs Field Extraction Rules](rules/field-extraction-rules.md)
- [Field Provenance Required](rules/field-provenance-required.md)
- [Manual Review Escalation](rules/manual-review-escalation.md)
- [OCR Uncertainty Disclosure](rules/ocr-uncertainty-disclosure.md)
- [Weight And Package Reconciliation](rules/weight-and-package-reconciliation.md)

## Workflows

- [Contract To Invoice Review](workflows/contract-to-invoice-review.md)
- [Declaration Element Review Workflow](workflows/declaration-element-review-workflow.md)
- [Document Difference Comparison Workflow](workflows/difference-comparison.md)
- [Customs Document Checking Workflow](workflows/document-checking.md)
- [Document Difference Triage](workflows/document-difference-triage.md)
- [Factory Document Review Workflow](workflows/factory-document-review-workflow.md)
- [Invoice Packing List Reconciliation](workflows/invoice-packing-list-reconciliation.md)
- [Main Workflow](workflows/main-workflow.md)
- [OCR to Structured JSON Workflow](workflows/ocr-to-json.md)
- [OCR To Structured JSON Workflow](workflows/ocr-to-structured-json-workflow.md)

## Cases

- [Case Currency Mismatch](cases/case-currency-mismatch.md)
- [Case Hidden OCR Uncertainty](cases/case-hidden-ocr-uncertainty.md)
- [Case Invented Missing Value](cases/case-invented-missing-value.md)
- [Case Manual Review Escalation](cases/case-manual-review-escalation.md)
- [Case Package Count Mismatch](cases/case-package-count-mismatch.md)
- [Case Weight Inconsistency](cases/case-weight-inconsistency.md)
- [Common Failure Cases](cases/common-failures.md)
- [Sample Document Difference Table](cases/sample-document-diff.md)
- [Sample Invoice Extraction](cases/sample-invoice-extraction.md)

## Prompts

- [Customs Source Gate Prompt](prompts/customs-source-gate-prompt.md)
- [Default Agent Prompt](prompts/default-agent.md)
- [Document Discrepancy Audit Prompt](prompts/document-discrepancy-audit-prompt.md)
- [Field Extraction Review Prompt](prompts/field-extraction-review-prompt.md)
- [Manual Review Summary Prompt](prompts/manual-review-summary-prompt.md)

## Evals

- [Customs Agent Evals](evals/customs-agent-evals.yaml)
- [Smoke Tests](evals/smoke-tests.yaml)
- [Stable Knowledge Evals](evals/stable-knowledge-evals.yaml)
