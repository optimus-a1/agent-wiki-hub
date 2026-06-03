# CI Workflow Audit

Generated: 2026-06-03

## Summary

- Checks: 11
- Passed: 11
- Failed: 0

## Checks

| Check | Result | Evidence |
| --- | --- | --- |
| workflow_exists | PASS | `.github/workflows/wiki-acceptance.yml` |
| workflow_not_empty | PASS | `505 characters` |
| trigger:pull_request | PASS | `pull_request:` |
| trigger:workflow_dispatch | PASS | `workflow_dispatch:` |
| permissions:contents_read | PASS | `contents: read` |
| checkout | PASS | `actions/checkout@` |
| setup_python | PASS | `actions/setup-python@` |
| run_acceptance | PASS | `python scripts/run_acceptance.py` |
| no_github_secrets | PASS | `\bsecrets\.` |
| no_api_key_literals | PASS | `(?i)(api[_-]?key|private[_-]?key|access[_-]?token|cookie)\s*[:=]` |
| no_write_permissions | PASS | `contents:\s*write` |

## Usage Notes

- CI should run the same local acceptance suite that maintainers run manually.
- Keep workflow permissions minimal and do not store secrets in workflow files.
- If this audit fails, fix `.github/workflows/wiki-acceptance.yml` before publishing packages.
