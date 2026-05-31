# Source Evidence Recorder

## Purpose

`scripts/record_source_evidence.py` appends a completed evidence entry to the correct wiki's `sources/source-refresh-log.md` for a source refresh ticket.

It does not search the web, verify a source, or certify current facts by itself. It only records evidence that a human or source-refresh agent has already checked.

## Usage

Dry-run without writing:

```bash
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run
```

Record a final evidence entry:

```bash
python3 scripts/record_source_evidence.py \
  --ticket-id TICKET-SRC-006 \
  --status still-needs-source-update \
  --source-title "Official source title" \
  --source-publisher "Official publisher" \
  --source-url-or-reference "https://example.invalid/source" \
  --source-accessed-on 2026-05-28 \
  --evidence-summary "Source was checked, but scope does not support writing a stable current fact." \
  --confidence medium \
  --remaining-uncertainty "Current data still requires a live authoritative feed." \
  --human-reviewer "required reviewer role"
```

## Required Fields For Final Status

Final statuses are `verified`, `unchanged`, `still-needs-source-update`, and `rejected`.

For final status, provide:

- `--source-title`
- `--source-publisher`
- `--source-url-or-reference`
- `--source-accessed-on`
- `--evidence-summary`
- `--confidence`
- `--remaining-uncertainty`
- `--human-reviewer` for high-risk tickets

## Safety Checks

The recorder rejects inputs that appear to contain API keys, private keys, cookies, authorization headers, bearer tokens, seed phrases, or mnemonics.

Do not use this tool to invent source evidence. If the source does not support the claim, use `still-needs-source-update` or `rejected`.

## After Recording

The script runs:

```bash
python3 scripts/audit_source_refresh_completion.py
python3 scripts/audit_source_evidence_quality.py
```

Then run the full acceptance suite before release:

```bash
python3 scripts/run_acceptance.py
```
