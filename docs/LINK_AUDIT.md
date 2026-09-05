# Link Audit

Generated: 2026-09-05

## Summary

- Internal references checked: 5469
- Passed: 5469
- Failed: 0

## Counts By Type

| Type | References |
| --- | ---: |
| code_reference | 1182 |
| markdown_link | 2376 |
| path_reference | 1911 |

## Counts By Target Kind

| Kind | References |
| --- | ---: |
| directory | 659 |
| file | 4810 |

## Failed References

No broken internal references found.

## Usage Notes

- This audit checks local Markdown links, root-relative repository paths, and common code-spanned path references.
- External URLs, anchors, placeholders such as `wikis/<domain>-agent-wiki/`, globs, and home-directory examples are intentionally skipped.
- Run this after renaming files, moving wiki pages, or changing generated report locations.
