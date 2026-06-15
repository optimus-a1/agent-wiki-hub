---
title: "Tool Call Audit Prompt"
wiki: "agent-engineering-wiki"
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

# Tool Call Audit Prompt

## Purpose
This page gives agents a stable prompt pattern for tool call audit prompt in `agent-engineering-wiki`. It is model-synthesized stable knowledge, not an authoritative source and not a current-fact record.

## Stable Knowledge
- Tool Call Audit Prompt should be handled as prompt knowledge that supports repeatable agent behavior.
- An agent is a system of model, tools, knowledge, workflow, memory, evals, and boundaries.
- RAG quality depends on chunking, retrieval, grounding, citations, and evaluation.
- Tool use should be justified by task need, permission, and evidence.
- Autonomy requires explicit action gates and observable audit trails.
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
Require human confirmation before enabling autonomous actions, external writes, memory persistence, or high-risk tool access.

## Source Gate
Model capabilities, tool schemas, API parameters, platform behavior, and product features require source review before use.

## Examples
- Use tool call audit prompt to convert a vague request into explicit fields, checks, and boundaries.
- Use tool call audit prompt as a checklist item before the agent produces a final answer.
- Use tool call audit prompt during review to separate supported observations from unresolved risks.
- Use tool call audit prompt to decide whether a human gate or source gate is required.

## Anti-Patterns
- Treating tool call audit prompt as permission to invent missing details.
- Replacing uncertainty with confident wording because the output looks cleaner.
- Skipping human review when the action can affect money, rights, health, security, production, or compliance.
- Using stale or unsourced claims as if they were verified current facts.

## Checklist
- Confirm the request matches this wiki and this page type.
- Confirm the output is educational, operational, or review-oriented rather than a current fact claim.
- Preserve unknowns, confidence limits, and evidence gaps.
- Apply the human gate when a high-impact action or professional judgment is involved.
- Apply the source gate when a claim depends on current external information.
