---
title: Sample Disk Pressure Incident
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Sample Disk Pressure Incident

## Purpose
Show safe reasoning for a disk pressure incident without deleting data or giving environment-specific commands.

## When to use
Use as a case pattern when storage exhaustion threatens service reliability.

## Stable knowledge points
- KP-01: Disk pressure can cause write failures, database errors, log loss, and service instability.
- KP-02: The first safe question is what data is growing and whether it is required.
- KP-03: Removing files without ownership knowledge can destroy evidence or application state.
- KP-04: Log retention should balance diagnostics, compliance, privacy, and capacity.
- KP-05: Temporary relief should not replace root-cause analysis.
- KP-06: Snapshots and backups can increase storage pressure if unmanaged.
- KP-07: Growth rate matters because a system can recover briefly and fail again.
- KP-08: The final report should distinguish immediate mitigation from permanent prevention.

## Core rules
- Do not delete, truncate, or move production data automatically.
- Verify paths, ownership, and backup state before proposing cleanup.
- Escalate if data criticality is unknown.
- Keep commands as review prompts unless explicitly authorized.

## Workflow
1. State affected service, disk usage symptom, and user impact.
2. Identify top growth categories conceptually: logs, data, cache, temporary files, backups, artifacts.
3. Ask for or inspect ownership and retention rules.
4. Propose low-risk mitigations and human approval gates.
5. Recommend prevention through monitoring, retention, and capacity planning.

## Edge cases
- Deleted open files may not free space until processes release handles.
- Databases may require application-aware compaction or retention.
- Moving data across filesystems can change permissions or performance.

## Validation checks
- No destructive action is executed.
- Critical paths are identified before cleanup.
- Backup and restore assumptions are checked.
- Human operator approval is required.

## Source notes
Stable incident pattern only. No current filesystem layout, node data path, or vendor-specific procedure is included.
