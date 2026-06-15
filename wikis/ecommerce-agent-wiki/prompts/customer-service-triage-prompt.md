---
title: "Customer Service Triage Prompt"
wiki: "ecommerce-agent-wiki"
type: prompt
status: stable-general-knowledge
source_status: model-synthesized-stable
current_fact: false
requires_source_review: false
requires_human_review: true
risk_level: medium
generated_by: codex
generated_on: 2026-06-15
agent_use: true
tags:
  - agent-wiki
  - stable-knowledge
---

# Customer Service Triage Prompt

## Purpose
This page gives agents a stable prompt pattern for customer service triage prompt in `ecommerce-agent-wiki`. It is model-synthesized stable knowledge, not an authoritative source and not a current-fact record.

## Stable Knowledge
- Customer Service Triage Prompt should be handled as prompt knowledge that supports repeatable agent behavior.
- Ecommerce agents should separate product data, customer intent, policy constraints, and privacy.
- Recommendations depend on stated needs, constraints, tradeoffs, and uncertainty.
- Customer-impacting actions require consent, policy review, and auditability.
- Platform rules and live catalog facts require source review before use.
- The agent should name assumptions, confidence, unknowns, and escalation criteria.
- Changing facts must remain outside stable pages and move through source review.

## Agent Use
- Read this page after the wiki `AGENTS.md`, `rules/`, and relevant workflow pages.
- Use it to structure reasoning, extraction, review, triage, or drafting.
- Keep the final output scoped to stable principles, observable inputs, and user-provided context.
- When evidence is incomplete, report the gap and propose a review step instead of filling it silently.

## Boundaries
- Do not write current facts, current prices, current versions, current rules, live policy, or real-world status.
- Do not present this page as an authoritative source.
- Do not bypass professional, compliance, security, production, financial, legal, medical, customs, or wallet-safety review.
- Do not use this page to justify irreversible action.

## Human Gate
Require human review before refunds, account actions, regulated claims, privacy-sensitive handling, or customer-impacting exceptions.

## Source Gate
Platform policies, prices, inventory, return windows, fees, shipping limits, and consumer rules require source review before use.

## Examples
- Use customer service triage prompt to convert a vague request into explicit fields, checks, and boundaries.
- Use customer service triage prompt as a checklist item before the agent produces a final answer.
- Use customer service triage prompt during review to separate supported observations from unresolved risks.
- Use customer service triage prompt to decide whether a human gate or source gate is required.

## Anti-Patterns
- Treating customer service triage prompt as permission to invent missing details.
- Replacing uncertainty with confident wording because the output looks cleaner.
- Skipping human review when the action can affect money, rights, health, security, production, or compliance.
- Using stale or unsourced claims as if they were verified current facts.

## Checklist
- Confirm the request matches this wiki and this page type.
- Confirm the output is educational, operational, or review-oriented rather than a current fact claim.
- Preserve unknowns, confidence limits, and evidence gaps.
- Apply the human gate when a high-impact action or professional judgment is involved.
- Apply the source gate when a claim depends on current external information.
