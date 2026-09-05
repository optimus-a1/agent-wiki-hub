---
title: "agent-engineering-wiki MOC"
wiki: "agent-engineering-wiki"
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

# agent-engineering-wiki MOC

This root map links stable wiki pages. It does not certify current facts.

## Concepts

- [Agent Architecture](concepts/agent-architecture.md)
- [Agent Memory And Context](concepts/agent-memory-and-context.md)
- [Agent Planning Loop](concepts/agent-planning-loop.md)
- [Agent System Components](concepts/agent-system-components.md)
- [Autonomous Ingestion Safety](concepts/autonomous-ingestion-safety.md)
- [Codex Skills Foundations](concepts/codex-skills.md)
- [Evaluation Harness](concepts/evaluation-harness.md)
- [Knowledge Pack Lifecycle](concepts/knowledge-pack-lifecycle.md)
- [Memory Hierarchy](concepts/memory-hierarchy.md)
- [Obsidian Vault Integration](concepts/obsidian-vault-integration.md)
- [Agent Engineering Wiki Overview](concepts/overview.md)
- [Prompt Routing](concepts/prompt-routing.md)
- [RAG and Knowledge Pack Foundations](concepts/rag-knowledge-pack.md)
- [RAG Retrieval Design](concepts/rag-retrieval-design.md)
- [Reflection Boundary](concepts/reflection-boundary.md)
- [Source Review Gate](concepts/source-review-gate.md)
- [Tool Calling Contract](concepts/tool-calling-contract.md)

## Rules

- [Autonomy Action Boundary](rules/autonomy-action-boundary.md)
- [Core Rules](rules/core-rules.md)
- [Eval Before Promotion](rules/eval-before-promotion.md)
- [Grounded Answer Boundary](rules/grounded-answer-boundary.md)
- [Knowledge Pack Quality Rules](rules/knowledge-pack-quality.md)
- [Memory Write Human Gate](rules/memory-write-human-gate.md)
- [No Hidden Instructions](rules/no-hidden-instructions.md)
- [RAG Quality Rules](rules/rag-quality.md)
- [Retrieval Citation Required](rules/retrieval-citation-required.md)
- [Source Gate For Current Claims](rules/source-gate-for-current-claims.md)
- [Tool Use And Grounding](rules/tool-use-and-grounding.md)
- [Tool Use Justification](rules/tool-use-justification.md)

## Workflows

- [Agent Eval Loop](workflows/agent-eval-loop.md)
- [Agent Task Routing Workflow](workflows/agent-task-routing-workflow.md)
- [Autonomous Ingestion Review Workflow](workflows/autonomous-ingestion-review-workflow.md)
- [Build a New Agent Wiki](workflows/build-new-wiki.md)
- [Eval Design Workflow](workflows/eval-design.md)
- [Knowledge Pack Release Workflow](workflows/knowledge-pack-release-workflow.md)
- [Main Workflow](workflows/main-workflow.md)
- [Memory Review Workflow](workflows/memory-review-workflow.md)
- [Prompt Routing Workflow](workflows/prompt-routing-workflow.md)
- [RAG Eval Workflow](workflows/rag-eval-workflow.md)
- [Source Grounding Test Workflow](workflows/source-grounding-test-workflow.md)
- [Tool Call Review Workflow](workflows/tool-call-review-workflow.md)

## Cases

- [Case RAG Citation Gap](cases/case-rag-citation-gap.md)
- [Case Stale Memory Risk](cases/case-stale-memory-risk.md)
- [Case Tool Overreach Remediation](cases/case-tool-overreach-remediation.md)
- [Case Ungrounded Agent Answer](cases/case-ungrounded-agent-answer.md)
- [Case Unsafe Autonomy Request](cases/case-unsafe-autonomy-request.md)
- [Common Failure Cases](cases/common-failures.md)
- [Sample RAG Source Grounding Case](cases/sample-rag-source-grounding.md)
- [Sample Tool Overreach](cases/sample-tool-overreach.md)

## Prompts

- [Agent Routing Prompt](prompts/agent-routing-prompt.md)
- [Default Agent Prompt](prompts/default-agent.md)
- [Eval Design Prompt](prompts/eval-design-prompt.md)
- [Knowledge Pack Review Prompt](prompts/knowledge-pack-review-prompt.md)
- [Memory Safety Review Prompt](prompts/memory-safety-review-prompt.md)
- [RAG Grounding Review Prompt](prompts/rag-grounding-review-prompt.md)
- [Tool Call Audit Prompt](prompts/tool-call-audit-prompt.md)

## Evals

- [Agent Engineering Evals](evals/agent-engineering-evals.yaml)
- [Smoke Tests](evals/smoke-tests.yaml)
- [Stable Knowledge Evals](evals/stable-knowledge-evals.yaml)
