# Link Audit

Generated: 2026-06-16

## Summary

- Internal references checked: 5265
- Passed: 5265
- Failed: 0

## Counts By Type

| Type | References |
| --- | ---: |
| code_reference | 1170 |
| markdown_link | 2316 |
| path_reference | 1779 |

## Counts By Target Kind

| Kind | References |
| --- | ---: |
| directory | 623 |
| file | 4642 |

## Failed References

No broken internal references found.

## Usage Notes

- This audit checks local Markdown links, root-relative repository paths, and common code-spanned path references.
- External URLs, anchors, placeholders such as `wikis/<domain>-agent-wiki/`, globs, and home-directory examples are intentionally skipped.
- Run this after renaming files, moving wiki pages, or changing generated report locations.
