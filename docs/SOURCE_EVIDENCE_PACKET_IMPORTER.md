# Source Evidence Packet Importer

Generated: 2026-05-31

## Purpose

Import human-reviewed source evidence packets into per-wiki source refresh logs. This importer validates the packet through `record_source_evidence.py` before writing and does not fetch or certify external facts by itself.

## Summary

- Packet path: `G:\11\agent-wiki-hub-starter\registry\source-review-packets\source-review-session-wave-1-pending.jsonl`
- Entries: 13
- Final entries: 0
- Passed: yes

## Packet Format

Use JSON, JSON object with `entries`, JSON list, or JSONL. Field names:

- `ticket_id`
- `status`
- `source_title`
- `source_publisher`
- `source_url_or_reference`
- `source_published_or_updated`
- `source_accessed_on`
- `verified_on`
- `evidence_summary`
- `affected_pages`
- `confidence`
- `remaining_uncertainty`
- `human_reviewer`
- `follow_up`

Example packet:

```json
{
  "packet_id": "source-evidence-packet-example",
  "created_on": "2026-05-31",
  "created_by": "<human reviewer or source-refresh agent>",
  "entries": [
    {
      "ticket_id": "TICKET-SRC-006",
      "status": "still-needs-source-update",
      "source_title": "<source title>",
      "source_publisher": "<official publisher or authority>",
      "source_url_or_reference": "<URL or local reference>",
      "source_published_or_updated": "YYYY-MM-DD | unknown",
      "source_accessed_on": "2026-05-31",
      "verified_on": "2026-05-31",
      "evidence_summary": "<what the source supports and what it does not support>",
      "affected_pages": [
        "wikis/finance-agent-wiki/sources/source-notes.md"
      ],
      "confidence": "low",
      "remaining_uncertainty": "<unknown, stale, conflicting, or out-of-scope facts>",
      "human_reviewer": "<required for high-risk tickets>",
      "follow_up": "none"
    }
  ]
}
```

## Import Flow

- Preflight every entry with `record_source_evidence.py --dry-run`.
- Reject duplicate ticket ids in the same packet unless `--allow-duplicate` is explicit.
- Write entries only after the whole packet preflight passes.
- Run completion audit, evidence quality audit, dashboard, wave runner, handoff, index update, and acceptance unless skipped.

## Commands

```bash
python3 scripts/import_source_evidence_packet.py
python3 scripts/import_source_evidence_packet.py --template --ticket-id TICKET-SRC-006
python3 scripts/generate_source_evidence_packet_fixtures.py
python3 scripts/import_source_evidence_packet.py --packet source-evidence.json --dry-run
python3 scripts/import_source_evidence_packet.py --packet source-evidence.json
```

## Results

| Phase | Ticket/Script | Result | Command |
| --- | --- | --- | --- |
| preflight | TICKET-SRC-004 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-004 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-005 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-005 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-006 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-007 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-007 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-001 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-001 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-002 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-002 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-003 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-003 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-008 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-008 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-009 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-009 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-012 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-012 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-013 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-013 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-010 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-010 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |
| preflight | TICKET-SRC-011 | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-011 --status pending --source-title <source title> --source-publisher <official publisher or authority> --source-url-or-reference <URL or local reference> --source-published-or-updated YYYY-MM-DD | unknown --source-accessed-on 2026-05-31 --evidence-summary <what the source supports and does not support> --confidence low --remaining-uncertainty <remaining uncertainty> --human-reviewer <reviewer> --follow-up Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed. --dry-run --allow-duplicate --no-audit` |

## Safety Boundary

- Do not put API keys, private keys, cookies, bearer tokens, seed phrases, or private account data in packets.
- Do not mark a ticket `verified` without dated authoritative evidence.
- High-risk tickets require `human_reviewer` for final statuses.
- Use `still-needs-source-update` when sources are unavailable, stale, conflicting, or outside the ticket scope.
