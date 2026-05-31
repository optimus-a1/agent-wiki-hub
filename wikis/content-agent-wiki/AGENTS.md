# AGENTS.md — Content Agent Wiki

## Trigger

Use this wiki when the task involves: 内容, 写作, 日报, 公众号, 帖子, 标题, 摘要, 发布.

## Reading order

1. `manifest.yaml`
2. `README.md`
3. `rules/`
4. `workflows/`
5. `cases/`
6. `tools/`
7. `prompts/`
8. `evals/`
9. `sources/source-notes.md`

## Required behavior

- Prefer this wiki's rules over generic assumptions.
- Do not invent facts that require current sources.
- Update `update-log.md` after changes.
- For high-risk content, include risk notes and human confirmation points.
- If knowledge is missing, add a TODO in `sources/source-notes.md` before proceeding.
