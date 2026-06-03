---
title: Backup Restore And Change Safety
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Backup Restore And Change Safety

## Purpose
Define stable rules for backups, restores, and operational changes in high-risk environments.

## When to use
Use before production changes, data migrations, service restarts, node maintenance, or destructive operations.

## Stable knowledge points
- KP-01: A backup is not reliable until a restore path has been tested.
- KP-02: Restore planning must identify data scope, consistency point, credentials, dependencies, and validation checks.
- KP-03: Change safety depends on blast radius, reversibility, observability, and human accountability.
- KP-04: Destructive actions need explicit target verification and rollback discussion.
- KP-05: A dry run reduces risk only when it exercises the same assumptions as the real action.
- KP-06: Maintenance windows reduce user impact but do not replace rollback planning.
- KP-07: Access control should give operators only the permissions needed for the task.
- KP-08: Post-change monitoring is part of the change, not an optional afterthought.

## Core rules
- Do not perform production operations without human confirmation.
- Verify absolute paths and targets before move, delete, or overwrite operations.
- Keep secrets out of logs, tickets, and command output.
- Stop if backup or rollback assumptions are unknown.

## Workflow
1. Define the change, owner, affected systems, and success criteria.
2. Confirm backup, restore, and rollback paths.
3. Inspect target paths, permissions, dependencies, and current health.
4. Execute the smallest safe step with monitoring.
5. Validate service behavior and record lessons.

## Edge cases
- A backup can be internally consistent but incompatible with the restore environment.
- Rolling back code without data rollback can leave an invalid state.
- Partial failure can require containment rather than immediate retry.

## Validation checks
- Backup and restore assumptions are documented.
- Human approval is recorded for high-risk operations.
- Commands avoid broad wildcards and ambiguous targets.
- Monitoring and rollback criteria are explicit.

## Source notes
Stable operational safety rules only. No current provider, OS, node, or service-specific procedure is included.
