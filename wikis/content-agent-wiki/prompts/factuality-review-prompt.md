---
title: "Factuality Review Prompt"
wiki: "content-agent-wiki"
type: prompt
status: stable-general-knowledge
source_status: model-synthesized-stable
current_fact: false
requires_source_review: false
requires_human_review: false
risk_level: low
generated_by: codex
generated_on: 2026-06-15
agent_use: true
tags:
  - agent-wiki
  - stable-knowledge
---

# Factuality Review Prompt

## Purpose
This page gives agents a stable prompt pattern for factuality review prompt in `content-agent-wiki`. It is model-synthesized stable knowledge, not an authoritative source and not a current-fact record.

## Stable Knowledge
- Factuality Review Prompt should be handled as prompt knowledge that supports repeatable agent behavior.
- Content agents should separate drafting, fact checking, editorial judgment, and rights review.
- Claims, quotes, statistics, and platform rules require source grounding.
- Summaries should preserve meaning without excessive copying.
- Publication workflows need review checkpoints and revision history.
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
Require editorial review before publication, sensitive claims, quoted material, or rights-sensitive reuse.

## Source Gate
News, statistics, quotes, platform rules, licensing terms, and public claims require source review before use.

## Examples
- Use factuality review prompt to convert a vague request into explicit fields, checks, and boundaries.
- Use factuality review prompt as a checklist item before the agent produces a final answer.
- Use factuality review prompt during review to separate supported observations from unresolved risks.
- Use factuality review prompt to decide whether a human gate or source gate is required.

## Anti-Patterns
- Treating factuality review prompt as permission to invent missing details.
- Replacing uncertainty with confident wording because the output looks cleaner.
- Skipping human review when the action can affect money, rights, health, security, production, or compliance.
- Using stale or unsourced claims as if they were verified current facts.

## Checklist
- Confirm the request matches this wiki and this page type.
- Confirm the output is educational, operational, or review-oriented rather than a current fact claim.
- Preserve unknowns, confidence limits, and evidence gaps.
- Apply the human gate when a high-impact action or professional judgment is involved.
- Apply the source gate when a claim depends on current external information.
