# Source Review Packet Audit

Generated: 2026-06-16

## Purpose

Audit active source-review packet files before import, while keeping historical AI-prefill packets visible as non-blocking advisory artifacts.

## Summary

- Passed: yes
- Active packet files: 2
- Discovered packet files: 10
- Advisory packet files: 8
- Planning-only packet files: 6
- Historical/prefill packet files: 2
- Entries: 26
- Advisory entries: 176
- Pending entries: 26
- Final entries: 0
- Human-gated entries: 26
- Issues: 0
- Advisory issues: 136
- Warnings: 0

## Packets

| Packet | Scope | Result | Entries | Pending | Final | Human-Gated | Issues | Warnings |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [source-review-session-auto-pending.json](../registry/source-review-packets/source-review-session-auto-pending.json) | planning-only-pending-packet | PASS | 0 | 0 | 0 | 0 | 0 | 0 |
| [source-review-session-auto-pending.jsonl](../registry/source-review-packets/source-review-session-auto-pending.jsonl) | planning-only-pending-packet | PASS | 0 | 0 | 0 | 0 | 0 | 0 |
| [source-review-session-wave-1-ai-prefill.json](../registry/source-review-packets/source-review-session-wave-1-ai-prefill.json) | advisory-ai-prefill | ADVISORY | 66 | 0 | 66 | 66 | 68 | 0 |
| [source-review-session-wave-1-ai-prefill.jsonl](../registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl) | advisory-ai-prefill | ADVISORY | 66 | 0 | 66 | 66 | 68 | 0 |
| [source-review-session-wave-1-pending.json](../registry/source-review-packets/source-review-session-wave-1-pending.json) | active-import-packet | PASS | 13 | 13 | 0 | 13 | 0 | 0 |
| [source-review-session-wave-1-pending.jsonl](../registry/source-review-packets/source-review-session-wave-1-pending.jsonl) | active-import-packet | PASS | 13 | 13 | 0 | 13 | 0 | 0 |
| [source-review-session-wave-2-pending.json](../registry/source-review-packets/source-review-session-wave-2-pending.json) | planning-only-pending-packet | PASS | 12 | 12 | 0 | 3 | 0 | 0 |
| [source-review-session-wave-2-pending.jsonl](../registry/source-review-packets/source-review-session-wave-2-pending.jsonl) | planning-only-pending-packet | PASS | 12 | 12 | 0 | 3 | 0 | 0 |
| [source-review-session-wave-3-pending.json](../registry/source-review-packets/source-review-session-wave-3-pending.json) | planning-only-pending-packet | PASS | 10 | 10 | 0 | 0 | 0 | 0 |
| [source-review-session-wave-3-pending.jsonl](../registry/source-review-packets/source-review-session-wave-3-pending.jsonl) | planning-only-pending-packet | PASS | 10 | 10 | 0 | 0 | 0 | 0 |

## Status Counts

- pending: 26

## Issues

No active packet issues found.

## Advisory Packet Observations

- `registry/source-review-packets/source-review-session-auto-pending.json`: Auto-pending packets are source-review planning artifacts and do not block acceptance. No issues found.
- `registry/source-review-packets/source-review-session-auto-pending.jsonl`: Auto-pending packets are source-review planning artifacts and do not block acceptance. No issues found.
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: duplicate ticket ids: TICKET-SRC-001, TICKET-SRC-002, TICKET-SRC-003, TICKET-SRC-004, TICKET-SRC-005, TICKET-SRC-006, TICKET-SRC-007, TICKET-SRC-008, TICKET-SRC-009, TICKET-SRC-010, TICKET-SRC-011, TICKET-SRC-012, TICKET-SRC-013
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-002: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-002: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-002: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-002: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-008: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-008: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-008: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-008: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: final status requires non-placeholder evidence_summary
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.json`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: duplicate ticket ids: TICKET-SRC-001, TICKET-SRC-002, TICKET-SRC-003, TICKET-SRC-004, TICKET-SRC-005, TICKET-SRC-006, TICKET-SRC-007, TICKET-SRC-008, TICKET-SRC-009, TICKET-SRC-010, TICKET-SRC-011, TICKET-SRC-012, TICKET-SRC-013
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-004: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-005: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-006: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-007: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-001: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-002: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-002: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-002: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-002: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-003: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-008: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-008: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-008: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-008: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-009: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-010: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-011: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-012: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: final status requires non-placeholder evidence_summary
- `registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl`: AI-prefill packets are historical source-assistance artifacts, not active import packets. Observation: TICKET-SRC-013: human-gated ticket requires human_reviewer before final status
- `registry/source-review-packets/source-review-session-wave-2-pending.json`: Planning-only pending packets are templates for future source review and do not block acceptance. No issues found.
- `registry/source-review-packets/source-review-session-wave-2-pending.jsonl`: Planning-only pending packets are templates for future source review and do not block acceptance. No issues found.
- `registry/source-review-packets/source-review-session-wave-3-pending.json`: Planning-only pending packets are templates for future source review and do not block acceptance. No issues found.
- `registry/source-review-packets/source-review-session-wave-3-pending.jsonl`: Planning-only pending packets are templates for future source review and do not block acceptance. No issues found.

## Warnings

No packet warnings found.

## Related Reports

- source_review_readiness_matrix: [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- source_review_packet_rehearsal: [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- source_review_packet_bundle: [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- source_review_session_plan: [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- source_evidence_packet_importer: [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- source_evidence_quality: [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)
- source_refresh_completion: [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| ticket registry available | PASS | registry/source-refresh-tickets.json |
| packet directory available | PASS | registry/source-review-packets |
| packet files discovered | PASS | 10 discovered packet files |
| active packet files discovered | PASS | 2 active packet files |
| active packet files passed | PASS | 2/2 active packets passed |
| advisory packets do not block acceptance | PASS | 8 advisory packet files, 136 advisory issues |

## Safety Boundary

- This audit does not verify external facts.
- It checks packet structure, final-status readiness, human-review gates, duplicate tickets, and obvious secret patterns.
- Passing this audit does not mean the packet evidence is true or current.
