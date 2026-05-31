# Source Review Packet Classification

Generated: 2026-05-31

## Purpose

Document which source-review packets are active import targets versus advisory, planning-only, or historical artifacts.

## Summary

- Passed: yes
- Packet files: 8
- active-import-packet: 2
- advisory-prefill-artifact: 2
- planning-only-pending-packet: 4

## Classification Table

| Packet | Classification | Acceptance Role | Strict Audit | Entries | Rationale |
| --- | --- | --- | --- | ---: | --- |
| [source-review-session-wave-1-ai-prefill.json](../registry/source-review-packets/source-review-session-wave-1-ai-prefill.json) | advisory-prefill-artifact | non-blocking | no | 66 | Historical AI-prefill/source-assistance artifact; retained for traceability, not an active import target. |
| [source-review-session-wave-1-ai-prefill.jsonl](../registry/source-review-packets/source-review-session-wave-1-ai-prefill.jsonl) | advisory-prefill-artifact | non-blocking | no | 66 | Historical AI-prefill/source-assistance artifact; retained for traceability, not an active import target. |
| [source-review-session-wave-1-pending.json](../registry/source-review-packets/source-review-session-wave-1-pending.json) | active-import-packet | blocking | yes | 13 | Current active packet; participates in strict packet audit and rehearsal. |
| [source-review-session-wave-1-pending.jsonl](../registry/source-review-packets/source-review-session-wave-1-pending.jsonl) | active-import-packet | blocking | yes | 13 | Current active packet; participates in strict packet audit and rehearsal. |
| [source-review-session-wave-2-pending.json](../registry/source-review-packets/source-review-session-wave-2-pending.json) | planning-only-pending-packet | non-blocking | no | 12 | Pending template packet for future source review; it contains placeholders and must not certify current facts. |
| [source-review-session-wave-2-pending.jsonl](../registry/source-review-packets/source-review-session-wave-2-pending.jsonl) | planning-only-pending-packet | non-blocking | no | 12 | Pending template packet for future source review; it contains placeholders and must not certify current facts. |
| [source-review-session-wave-3-pending.json](../registry/source-review-packets/source-review-session-wave-3-pending.json) | planning-only-pending-packet | non-blocking | no | 10 | Pending template packet for future source review; it contains placeholders and must not certify current facts. |
| [source-review-session-wave-3-pending.jsonl](../registry/source-review-packets/source-review-session-wave-3-pending.jsonl) | planning-only-pending-packet | non-blocking | no | 10 | Pending template packet for future source review; it contains placeholders and must not certify current facts. |

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| packet directory exists | PASS | registry/source-review-packets |
| packet files classified | PASS | 8 packet files |
| active packet exists | PASS | 2 active packet files |
| planning packets are non-blocking | PASS | 4 planning-only packet files |

## Safety Boundary

- Classification does not verify external facts.
- Planning-only and advisory packets are retained for traceability but must not be treated as verified evidence.
- Active import packets still require audit and rehearsal before any real evidence import.
