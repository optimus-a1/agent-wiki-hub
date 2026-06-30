# Source Evidence Packet Fixtures

Generated: 2026-06-30

## Purpose

These fixtures exercise the source evidence packet importer without verifying or certifying external facts. Use them with `--dry-run`; fill real source evidence before any actual import.

## Summary

- Fixture directory: `registry/source-evidence-fixtures`
- Fixtures: 8
- Valid/template fixtures: 4
- Invalid fixtures: 4
- Passed: yes

## Fixtures

| Fixture | Kind | Expected Dry Run | Ticket IDs | Description |
| --- | --- | --- | --- | --- |
| [valid-pending-single.json](../registry/source-evidence-fixtures/valid-pending-single.json) | valid | pass | TICKET-SRC-006 | Minimal pending packet for one ticket; safe because it records no source facts. |
| [valid-still-needs-source-update-dry-run-only.json](../registry/source-evidence-fixtures/valid-still-needs-source-update-dry-run-only.json) | valid | pass | TICKET-SRC-006 | Final-status shape for dry-run testing only; replace all fixture fields before real import. |
| [template-wave-1-p0-pending.json](../registry/source-evidence-fixtures/template-wave-1-p0-pending.json) | template | pass | TICKET-SRC-004, TICKET-SRC-005, TICKET-SRC-006, TICKET-SRC-007 | Pending packet template for wave-1 P0 finance tickets. |
| [template-wave-2-customs-pending.json](../registry/source-evidence-fixtures/template-wave-2-customs-pending.json) | template | pass | TICKET-SRC-014, TICKET-SRC-015, TICKET-SRC-016, TICKET-SRC-017 | Pending packet template for customs source-refresh tickets. |
| [invalid-duplicate-ticket.json](../registry/source-evidence-fixtures/invalid-duplicate-ticket.json) | invalid | fail | TICKET-SRC-006, TICKET-SRC-006 | Expected failure: duplicate ticket id in one packet. |
| [invalid-missing-human-reviewer.json](../registry/source-evidence-fixtures/invalid-missing-human-reviewer.json) | invalid | fail | TICKET-SRC-006 | Expected failure: high-risk final status without human_reviewer. |
| [invalid-placeholder-source.json](../registry/source-evidence-fixtures/invalid-placeholder-source.json) | invalid | fail | TICKET-SRC-006 | Expected failure: final status still contains placeholder source fields. |
| [invalid-secret-marker.json](../registry/source-evidence-fixtures/invalid-secret-marker.json) | invalid | fail | TICKET-SRC-006 | Expected failure: fixture contains a redacted secret marker that must be rejected. |

## Dry-Run Validation

| Fixture | Expected | Actual | Result |
| --- | --- | --- | --- |
| `valid-pending-single.json` | pass | pass | PASS |
| `valid-still-needs-source-update-dry-run-only.json` | pass | pass | PASS |
| `template-wave-1-p0-pending.json` | pass | pass | PASS |
| `template-wave-2-customs-pending.json` | pass | pass | PASS |
| `invalid-duplicate-ticket.json` | fail | fail | PASS |
| `invalid-missing-human-reviewer.json` | fail | fail | PASS |
| `invalid-placeholder-source.json` | fail | fail | PASS |
| `invalid-secret-marker.json` | fail | fail | PASS |

## Commands

```bash
python3 scripts/generate_source_evidence_packet_fixtures.py
python3 scripts/import_source_evidence_packet.py --packet registry/source-evidence-fixtures/valid-pending-single.json --dry-run --no-post-checks
python3 scripts/import_source_evidence_packet.py --packet registry/source-evidence-fixtures/invalid-secret-marker.json --dry-run --no-post-checks
```

## Safety Boundary

- Fixtures are for importer tests and packet authoring only.
- Do not import dry-run-only fixtures as evidence for current facts.
- Invalid fixtures intentionally contain placeholders or redacted secret markers to test rejection paths.
- No fixture contains real credentials, private keys, cookies, or verified current facts.
