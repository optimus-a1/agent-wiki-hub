---
title: "ecommerce-agent-wiki MOC"
wiki: "ecommerce-agent-wiki"
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

# ecommerce-agent-wiki MOC

This root map links stable wiki pages. It does not certify current facts.

## Concepts

- [Attribute Normalization](concepts/attribute-normalization.md)
- [Customer Intent Signals](concepts/customer-intent-signals.md)
- [Inventory Vs Availability](concepts/inventory-vs-availability.md)
- [Ecommerce Agent Wiki Overview](concepts/overview.md)
- [Price And Promotion Boundary](concepts/price-and-promotion-boundary.md)
- [Product Catalog Model](concepts/product-catalog-model.md)
- [Product Catalog Foundations](concepts/product-catalog.md)
- [Recommendation Constraint Matching](concepts/recommendation-constraint-matching.md)
- [Return And Refund Concepts](concepts/return-and-refund-concepts.md)
- [SKU And SPU Distinction](concepts/sku-and-spu-distinction.md)

## Rules

- [Core Rules](rules/core-rules.md)
- [Customer Impact Human Gate](rules/customer-impact-human-gate.md)
- [No Invented Stock Or Price](rules/no-invented-stock-or-price.md)
- [Ecommerce Order and Customer Safety Rules](rules/order-customer-safety.md)
- [Platform Policy Source Gate](rules/platform-policy-source-gate.md)
- [Privacy And Consent Rule](rules/privacy-and-consent-rule.md)
- [Recommendation Transparency](rules/recommendation-transparency.md)
- [Return Window Source Gate](rules/return-window-source-gate.md)

## Workflows

- [Catalog Data Quality Review](workflows/catalog-data-quality-review.md)
- [Customer Service and Returns Workflow](workflows/customer-service-returns.md)
- [Customer Service Triage](workflows/customer-service-triage.md)
- [Main Workflow](workflows/main-workflow.md)
- [Pre Publication Product Claim Review](workflows/pre-publication-product-claim-review.md)
- [Product Fit Recommendation Workflow](workflows/product-fit-recommendation-workflow.md)
- [Ecommerce Recommendation Workflow](workflows/product-recommendation.md)
- [Return Refund Review Workflow](workflows/return-refund-review-workflow.md)

## Cases

- [Case Invented Inventory](cases/case-invented-inventory.md)
- [Case Policy Assumption Risk](cases/case-policy-assumption-risk.md)
- [Case Privacy Overcollection](cases/case-privacy-overcollection.md)
- [Case Transparent Recommendation](cases/case-transparent-recommendation.md)
- [Common Failure Cases](cases/common-failures.md)
- [Sample Return Request](cases/sample-return-request.md)

## Prompts

- [Customer Service Triage Prompt](prompts/customer-service-triage-prompt.md)
- [Default Agent Prompt](prompts/default-agent.md)
- [Platform Policy Source Gate Prompt](prompts/platform-policy-source-gate-prompt.md)
- [Product Recommendation Review Prompt](prompts/product-recommendation-review-prompt.md)

## Evals

- [Ecommerce Agent Evals](evals/ecommerce-agent-evals.yaml)
- [Smoke Tests](evals/smoke-tests.yaml)
- [Stable Knowledge Evals](evals/stable-knowledge-evals.yaml)
