---
title: "nodeops-agent-wiki MOC"
wiki: "nodeops-agent-wiki"
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

# nodeops-agent-wiki MOC

This root map links stable wiki pages. It does not certify current facts.

## Concepts

- [Blockchain Node Health Signals](concepts/blockchain-node-health-signals.md)
- [Disk Pressure Signals](concepts/disk-pressure-signals.md)
- [Docker Container Isolation](concepts/docker-container-isolation.md)
- [Docker Volume Backup](concepts/docker-volume-backup.md)
- [Firewall Change Safety](concepts/firewall-change-safety.md)
- [Linux Service Lifecycle](concepts/linux-service-lifecycle.md)
- [Log Rotation Model](concepts/log-rotation-model.md)
- [Memory Pressure Signals](concepts/memory-pressure-signals.md)
- [Network Port Diagnosis](concepts/network-port-diagnosis.md)
- [NodeOps Agent Wiki Overview](concepts/overview.md)
- [Rollback First Operations](concepts/rollback-first-operations.md)
- [RPC Endpoint Safety](concepts/rpc-endpoint-safety.md)
- [Service Reliability Signals](concepts/service-reliability-signals.md)
- [Systemd Unit Reasoning](concepts/systemd-unit-reasoning.md)

## Rules

- [Backup Before Mutation](rules/backup-before-mutation.md)
- [Backup Restore And Change Safety](rules/backup-restore-and-change-safety.md)
- [Core Rules](rules/core-rules.md)
- [Destructive Command Gate](rules/destructive-command-gate.md)
- [Firewall Change Review](rules/firewall-change-review.md)
- [Node Client Upgrade Source Gate](rules/node-client-upgrade-source-gate.md)
- [Operational Risk Control Rules](rules/operational-risk-control.md)
- [Production Human Confirmation](rules/production-human-confirmation.md)
- [Production Safety Rules](rules/production-safety.md)
- [Provider Limit Source Gate](rules/provider-limit-source-gate.md)
- [Rollback Plan Required](rules/rollback-plan-required.md)
- [Secret Redaction In Logs](rules/secret-redaction-in-logs.md)

## Workflows

- [Production Change Management Workflow](workflows/change-management.md)
- [Disk Pressure Triage](workflows/disk-pressure-triage.md)
- [Docker Volume Restore Check](workflows/docker-volume-restore-check.md)
- [Incident Response Workflow](workflows/incident-response-workflow.md)
- [Incident Response Workflow](workflows/incident-response.md)
- [Incident Triage Runbook](workflows/incident-triage-runbook.md)
- [Main Workflow](workflows/main-workflow.md)
- [Memory Pressure Triage](workflows/memory-pressure-triage.md)
- [Network Port Triage](workflows/network-port-triage.md)
- [Node Client Upgrade Checklist](workflows/node-client-upgrade-checklist.md)
- [Post Incident Review Workflow](workflows/post-incident-review-workflow.md)
- [Systemd Service Recovery](workflows/systemd-service-recovery.md)

## Cases

- [Case Disk Pressure Safe Response](cases/case-disk-pressure-safe-response.md)
- [Case Firewall Lockout Prevention](cases/case-firewall-lockout-prevention.md)
- [Case Memory Leak Triage](cases/case-memory-leak-triage.md)
- [Case Node Upgrade Source Gate](cases/case-node-upgrade-source-gate.md)
- [Case Production Change Without Backup](cases/case-production-change-without-backup.md)
- [Case RPC Endpoint Exposure](cases/case-rpc-endpoint-exposure.md)
- [Common Failure Cases](cases/common-failures.md)
- [Sample Disk Pressure Incident](cases/sample-disk-pressure-incident.md)
- [Sample Production Change Review](cases/sample-production-change-review.md)

## Prompts

- [Backup Restore Review Prompt](prompts/backup-restore-review-prompt.md)
- [Default Agent Prompt](prompts/default-agent.md)
- [Node Health Review Prompt](prompts/node-health-review-prompt.md)
- [Ops Incident Triage Prompt](prompts/ops-incident-triage-prompt.md)
- [Production Change Risk Prompt](prompts/production-change-risk-prompt.md)

## Evals

- [Nodeops Agent Evals](evals/nodeops-agent-evals.yaml)
- [Smoke Tests](evals/smoke-tests.yaml)
- [Stable Knowledge Evals](evals/stable-knowledge-evals.yaml)
