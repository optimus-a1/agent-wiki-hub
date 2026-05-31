# CI Usage

## Purpose

This repository includes a GitHub Actions workflow at `.github/workflows/wiki-acceptance.yml`.

The workflow runs the local acceptance suite on pull requests, pushes to `main` or `master`, and manual dispatches.

## What It Checks

The CI entrypoint is:

```bash
python scripts/run_acceptance.py
```

That suite validates wiki structure, registry alignment, page metadata, content coverage, links, eval files, source-update queues, safety boundaries, search behavior, package generation, and package integrity.

The CI workflow itself is checked by:

```bash
python scripts/audit_ci_workflow.py
```

That audit writes `docs/CI_AUDIT.md` and `registry/ci-audit.json`.

## Operating Rules

- Treat CI failures as release blockers for wiki package updates.
- Do not add secrets, API keys, cookies, private keys, or production credentials to workflow files.
- Keep CI source-free by default; current facts still belong in `sources/source-notes.md` until authoritative sources are checked.
- If a workflow failure is caused by generated reports, rerun `python scripts/run_acceptance.py` locally and commit the refreshed docs, registry files, index, and packages.
