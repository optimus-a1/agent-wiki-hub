# Source Review Packet Bundle

Generated: 2026-06-30

## Purpose

Provide offline-safe source evidence packet templates for the current source-review session.

## Summary

- Passed: yes
- Current-fact ready: no
- Selected reviews: 22
- Human review gates: 13
- High-risk reviews: 13
- JSON packet: [source-review-session-wave-1-pending.json](../registry/source-review-packets/source-review-session-wave-1-pending.json)
- JSONL packet: [source-review-session-wave-1-pending.jsonl](../registry/source-review-packets/source-review-session-wave-1-pending.jsonl)
- Checklist: [source-review-session-wave-1-pending-checklist.md](../registry/source-review-packets/source-review-session-wave-1-pending-checklist.md)

## Dry-Run Commands

```bash
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.jsonl --dry-run --no-post-checks
```

## Real Import Warning

Replace placeholders with authoritative, dated evidence before any non-dry-run import.

## Related Reports

- source_review_readiness_matrix: [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- source_review_packet_audit: [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- source_review_packet_rehearsal: [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- source_review_session_plan: [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- source_reviewer_queue: [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- source_refresh_dashboard: [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- source_evidence_packet_importer: [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- source_evidence_quality: [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)
- source_refresh_completion: [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| source review session plan exists | PASS | registry/source-review-session-plan.json |
| source review session plan passed | PASS | selected reviews: 22 |
| packet entry count matches selected reviews | PASS | 22 packet entries for 22 selected reviews |
| packet keeps entries pending | PASS | all generated entries use pending status |
| packet contains no final statuses | PASS | generated bundle cannot mark evidence verified |
| packet contains no detected secrets | PASS | secret scan over generated packet entries |
| bundle files written | PASS | registry/source-review-packets/source-review-session-wave-1-pending.json, registry/source-review-packets/source-review-session-wave-1-pending.jsonl, registry/source-review-packets/source-review-session-wave-1-pending-checklist.md, registry/source-review-packets/source-review-session-wave-1-pending-manifest.json |

## Safety Boundary

- This bundle is a template bundle only.
- It does not fetch, verify, or certify external facts.
- It intentionally keeps every entry at `pending` status.
- Do not use a non-dry-run import until every placeholder has been replaced with authoritative source evidence.
