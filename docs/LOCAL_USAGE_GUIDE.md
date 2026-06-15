# Local Usage Guide

This guide describes local-only operation for Agent Wiki Hub v2. It does not require network access and does not promote current facts without a review gate.

## Prerequisites

- Run commands from the repository root.
- Keep secrets in `.env` only. Do not commit API keys, tokens, cookies, or private keys.
- Treat `pending` source evidence as review material, not as verified knowledge.

## Obsidian Mode

Open `obsidian-vault/` as an Obsidian vault.

Regenerate the vault mirror and dashboards:

```bash
python scripts/generate_obsidian_vault.py
python scripts/generate_obsidian_canvas.py
python scripts/audit_obsidian_vault.py
```

Use `obsidian-vault/02_Knowledge/MOCs/` for wiki maps and `obsidian-vault/05_Dashboard/` for review, source, and knowledge dashboards.

## Dashboard Mode

Refresh dashboard data:

```bash
python dashboard/scripts/collect_dashboard_data.py
python scripts/audit_dashboard.py
```

Open `dashboard/index.html` locally. The dashboard reads JSON snapshots from `dashboard/data/` and does not call external services.

## RAG Mode

Inspect and search local wiki content:

```bash
python rag/index_wikis.py
python rag/index_obsidian.py
python rag/search_knowledge.py --query "risk control" --top-k 5
```

Optional vector indexing uses local dependencies listed in `rag/requirements-rag.txt`. Runtime vector stores belong under `rag/chroma/` and are ignored by git.

## Crawler And Ingestion Mode

The crawler is controlled by `crawler/sources.yaml`. Use dry-run output first, then review candidates before promotion:

```bash
python crawler/generate_crawl_report.py
python scripts/classify_candidate_knowledge.py --dry-run
python scripts/promote_stable_knowledge.py --dry-run
python scripts/generate_source_review_from_candidates.py --dry-run
```

Raw material belongs in `obsidian-vault/01_Raw/`. Stable, timeless knowledge may be promoted only through the review flow. Changing facts must remain in source review and must not be written into current wiki facts.

## Source Review Gates

Use source review packets for facts that may change over time:

```bash
python scripts/generate_source_review_packet_classification.py
python scripts/audit_source_review_packets.py
python scripts/rehearse_source_review_packet_imports.py
```

Planning-only pending packets are allowed to exist without blocking acceptance. Verified evidence packets remain the only path for importing source-backed current facts.

## Acceptance

Run the full local suite before handoff:

```bash
python scripts/validate_wiki.py
python scripts/update_index.py
python scripts/audit_links.py
python scripts/run_acceptance.py
```

Acceptance reports are written to `docs/ACCEPTANCE_REPORT.md` and `registry/acceptance-report.json`.
