---
title: "Incident Response Workflow"
wiki: "nodeops-agent-wiki"
type: workflow
status: stable-general-knowledge
source_status: model-synthesized-stable
current_fact: false
requires_source_review: false
requires_human_review: true
risk_level: high
generated_by: codex
generated_on: 2026-06-15
agent_use: true
tags:
  - agent-wiki
  - stable-knowledge
---

# Incident Response Workflow

## Purpose
This page gives agents a stable workflow pattern for incident response workflow in `nodeops-agent-wiki`. It is model-synthesized stable knowledge, not an authoritative source and not a current-fact record.

## Stable Knowledge
- Incident Response Workflow should be handled as workflow knowledge that supports repeatable agent behavior.
- Operations work should preserve evidence, backups, and rollback options before mutation.
- Diagnosis separates symptoms, recent changes, resource limits, dependencies, and user impact.
- Production systems require scoped actions, logs, monitoring, and clear ownership.
- Automation should default to observation or dry-run when authority is uncertain.
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
Require human confirmation before production mutation, destructive command, firewall change, rollback, node upgrade, key handling, or irreversible data operation.

## Source Gate
Operating system versions, package versions, node client releases, chain parameters, provider limits, and live incident facts require source review before use.

## Examples
- Use incident response workflow to convert a vague request into explicit fields, checks, and boundaries.
- Use incident response workflow as a checklist item before the agent produces a final answer.
- Use incident response workflow during review to separate supported observations from unresolved risks.
- Use incident response workflow to decide whether a human gate or source gate is required.

## Anti-Patterns
- Treating incident response workflow as permission to invent missing details.
- Replacing uncertainty with confident wording because the output looks cleaner.
- Skipping human review when the action can affect money, rights, health, security, production, or compliance.
- Using stale or unsourced claims as if they were verified current facts.

## Checklist
- Confirm the request matches this wiki and this page type.
- Confirm the output is educational, operational, or review-oriented rather than a current fact claim.
- Preserve unknowns, confidence limits, and evidence gaps.
- Apply the human gate when a high-impact action or professional judgment is involved.
- Apply the source gate when a claim depends on current external information.
