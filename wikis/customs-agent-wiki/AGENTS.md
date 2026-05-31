# AGENTS.md — Customs Document Agent Wiki

## Trigger

Use this wiki when the task involves: 报关, 报检, 单证, 发票, 装箱单, 合同, 厂检, HS编码, 字段校对.

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
