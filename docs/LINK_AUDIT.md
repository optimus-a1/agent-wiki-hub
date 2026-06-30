# Link Audit

Generated: 2026-06-30

## Summary

- Internal references checked: 5338
- Passed: 5338
- Failed: 0

## Counts By Type

| Type | References |
| --- | ---: |
| code_reference | 1179 |
| markdown_link | 2361 |
| path_reference | 1798 |

## Counts By Target Kind

| Kind | References |
| --- | ---: |
| directory | 650 |
| file | 4688 |

## Failed References

No broken internal references found.

## Usage Notes

- This audit checks local Markdown links, root-relative repository paths, and common code-spanned path references.
- External URLs, anchors, placeholders such as `wikis/<domain>-agent-wiki/`, globs, and home-directory examples are intentionally skipped.
- Run this after renaming files, moving wiki pages, or changing generated report locations.
