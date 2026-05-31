# Link Audit

Generated: 2026-05-31

## Summary

- Internal references checked: 3668
- Passed: 3668
- Failed: 0

## Counts By Type

| Type | References |
| --- | ---: |
| code_reference | 722 |
| markdown_link | 1698 |
| path_reference | 1248 |

## Counts By Target Kind

| Kind | References |
| --- | ---: |
| directory | 623 |
| file | 3045 |

## Failed References

No broken internal references found.

## Usage Notes

- This audit checks local Markdown links, root-relative repository paths, and common code-spanned path references.
- External URLs, anchors, placeholders such as `wikis/<domain>-agent-wiki/`, globs, and home-directory examples are intentionally skipped.
- Run this after renaming files, moving wiki pages, or changing generated report locations.
