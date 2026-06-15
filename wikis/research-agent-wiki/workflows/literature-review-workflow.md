---
title: "Literature Review Workflow"
wiki: "research-agent-wiki"
type: workflow
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

# Literature Review Workflow

## Purpose
This page gives agents a stable workflow pattern for literature review workflow in `research-agent-wiki`. It is model-synthesized stable knowledge, not an authoritative source and not a current-fact record.

## Stable Knowledge
- Literature Review Workflow should be handled as workflow knowledge that supports repeatable agent behavior.
- Research claims need traceable evidence, uncertainty, limitations, and reproducibility context.
- Benchmarks require task, data, metric, protocol, baseline, and leakage review.
- Citations must support the exact claim being made.
- Current literature coverage requires source review before use.
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
Require human review before making strong claims, comparing systems, relying on benchmarks, or publishing conclusions.

## Source Gate
Latest papers, revisions, citations, benchmarks, dataset availability, model weights, and repository status require source review before use.

## Examples
- Use literature review workflow to convert a vague request into explicit fields, checks, and boundaries.
- Use literature review workflow as a checklist item before the agent produces a final answer.
- Use literature review workflow during review to separate supported observations from unresolved risks.
- Use literature review workflow to decide whether a human gate or source gate is required.

## Anti-Patterns
- Treating literature review workflow as permission to invent missing details.
- Replacing uncertainty with confident wording because the output looks cleaner.
- Skipping human review when the action can affect money, rights, health, security, production, or compliance.
- Using stale or unsourced claims as if they were verified current facts.

## Checklist
- Confirm the request matches this wiki and this page type.
- Confirm the output is educational, operational, or review-oriented rather than a current fact claim.
- Preserve unknowns, confidence limits, and evidence gaps.
- Apply the human gate when a high-impact action or professional judgment is involved.
- Apply the source gate when a claim depends on current external information.
