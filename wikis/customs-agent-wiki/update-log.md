# Update Log — Customs Document Agent Wiki

## 2026-05-27

- Added source refresh log template for authoritative source verification.

- Added sample invoice extraction and document difference cases with expected JSON/table outputs.
- Expanded document type coverage for contracts, invoices, packing lists, factory inspection sheets, conformity guarantees, transport documents, and declaration drafts.
- Expanded English-to-Chinese field mapping and normalized JSON extraction rules.
- Added OCR-to-JSON workflow with evidence, confidence, warnings, and unresolved fields.
- Added cross-document difference comparison workflow with risk levels and human review suggestions.
- Added validation rules for amount, currency, packages, gross/net weight, product name, and specification.
- Updated evals and source notes for HS codes, regulatory conditions, OCR templates, exchange rates, tariffs, and destination rules.

## 2026-05-26

- Initialized standard Agent Wiki structure.
- Added base rules, workflow, cases, tools, prompts, evals, and source notes.

## 2026-06-15 - v2.1 knowledge density expansion

- Added model-synthesized stable knowledge pages for concepts, rules, workflows, cases, and prompts.
- Added `evals/stable-knowledge-evals.yaml` with 10 stable eval tests.
- No current facts, live prices, live policies, current laws, current vulnerabilities, or evidence verification were added.
- High-risk outputs remain gated by human review and source review.
