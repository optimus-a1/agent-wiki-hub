# Agent Wiki Hub Starter

这是一个面向 Codex / AI Agent 的行业知识库仓库模板。它把每个行业知识库做成可下载、可索引、可调用、可持续更新的 **Agent Knowledge Pack**。

> 生成日期：2026-05-26

## 核心目标

- 每个行业一个独立 Wiki：`wikis/<domain>-agent-wiki/`
- 每个 Wiki 都包含：概念、规则、流程、案例、工具、提示词、评测、来源记录
- Codex 通过根目录 `AGENTS.md` 和各 Wiki 内部 `AGENTS.md` 判断什么时候读取哪个知识库
- 所有会变化的信息必须写入 `sources/source-notes.md`，并标记更新时间
- 所有高风险领域默认只做研究、模拟、审核与风控，不自动执行真实交易、真实法律/医疗/安全操作

## 快速开始

```bash
cd agent-wiki-hub-starter
python3 scripts/validate_wiki.py
python3 scripts/check_registry_consistency.py
python3 scripts/audit_ci_workflow.py
python3 scripts/audit_page_metadata.py
python3 scripts/audit_content_coverage.py
python3 scripts/audit_links.py
python3 scripts/audit_pack_integrity.py
python3 scripts/check_eval_files.py
python3 scripts/update_index.py
python3 scripts/report_wiki_status.py
python3 scripts/list_source_updates.py
python3 scripts/generate_source_refresh_playbook.py
python3 scripts/generate_source_refresh_tickets.py
python3 scripts/generate_source_refresh_logs.py
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run
python3 scripts/import_source_evidence_packet.py
python3 scripts/generate_source_evidence_packet_fixtures.py
python3 scripts/audit_source_refresh_completion.py
python3 scripts/audit_source_evidence_quality.py
python3 scripts/generate_source_refresh_dashboard.py
python3 scripts/generate_source_refresh_wave_runner.py
python3 scripts/generate_source_reviewer_queue.py
python3 scripts/generate_source_review_session_plan.py
python3 scripts/generate_source_review_readiness_matrix.py
python3 scripts/generate_source_review_work_orders.py
python3 scripts/generate_source_review_packet_bundle.py
python3 scripts/generate_source_review_packet_classification.py
python3 scripts/generate_source_review_wave_plan.py --wave wave-2
python3 scripts/generate_source_review_wave_2_batch_plan.py
python3 scripts/generate_source_review_wave_3_plan.py
python3 scripts/generate_source_review_wave_packet_bundle.py --plan registry/source-review-wave-3-plan.json --stem source-review-session-wave-3-pending --work-order-dir registry/source-review-work-orders-wave-3
python3 scripts/generate_source_review_final_status.py
python3 scripts/audit_source_review_packets.py
python3 scripts/rehearse_source_review_packet_imports.py
python3 scripts/audit_safety_boundaries.py
python3 scripts/generate_hub_navigation.py
python3 scripts/generate_agent_routing_cards.py
python3 scripts/generate_agent_handoff.py
python3 scripts/generate_release_notes.py
python3 scripts/generate_change_summary.py
python3 scripts/route_wiki.py --query "risk control backtest"
python3 scripts/run_acceptance.py
python3 scripts/search_wiki.py --query "risk control" --wiki finance-agent-wiki
```

`validate_wiki.py` now checks both wiki structure and eval file integrity. `check_eval_files.py` remains available as a focused eval-only check.
`check_registry_consistency.py` verifies that registry records, wiki directories, and manifest metadata stay aligned.
`audit_ci_workflow.py` verifies GitHub Actions acceptance workflow expectations and writes `docs/CI_AUDIT.md`.
`audit_page_metadata.py` verifies front matter for reusable knowledge pages and writes `docs/PAGE_METADATA_AUDIT.md`.
`audit_content_coverage.py` verifies required topic coverage for each wiki and writes `docs/COVERAGE_AUDIT.md`.
`audit_links.py` verifies local Markdown links and internal path references, then writes `docs/LINK_AUDIT.md`.
`audit_pack_integrity.py` verifies generated zip packages and writes `docs/PACK_AUDIT.md`.
`run_acceptance.py` runs the full local acceptance suite and writes reports to `docs/` and `registry/`.
`list_source_updates.py` builds a prioritized queue of topics that require authoritative source verification.
`generate_source_refresh_playbook.py` turns source-update topics into refresh tasks and writes `docs/SOURCE_REFRESH_PLAYBOOK.md`.
`generate_source_refresh_tickets.py` turns refresh tasks into execution tickets and writes `docs/SOURCE_REFRESH_TICKETS.md`.
`generate_source_refresh_logs.py` creates per-wiki source refresh log templates and writes `docs/SOURCE_REFRESH_LOG_STATUS.md`.
`record_source_evidence.py` records user-provided source evidence for a ticket and writes to the matching wiki source refresh log.
`import_source_evidence_packet.py` imports JSON/JSONL evidence packets after preflight validation and writes `docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md`.
`generate_source_evidence_packet_fixtures.py` writes safe dry-run packet fixtures and expected-failure examples to `registry/source-evidence-fixtures/`.
`audit_source_refresh_completion.py` checks source refresh ticket completion evidence and writes `docs/SOURCE_REFRESH_COMPLETION_AUDIT.md`.
`audit_source_evidence_quality.py` checks completed evidence entry quality and writes `docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md`.
`generate_source_refresh_dashboard.py` summarizes source refresh readiness and writes `docs/SOURCE_REFRESH_DASHBOARD.md`.
`generate_source_refresh_wave_runner.py` organizes open source-refresh tickets into wave, priority, and human-review batches without verifying external facts.
`generate_source_reviewer_queue.py` assigns open source-refresh tickets to generic reviewer roles and preserves human confirmation gates.
`generate_source_review_session_plan.py` turns reviewer queue cards into a concrete source-review session plan with safe packet placeholders.
`generate_source_review_readiness_matrix.py` summarizes per-ticket readiness across reviewer assignment, session selection, packet coverage, packet audit, rehearsal, and completion state.
`generate_source_review_work_orders.py` turns ready source-review tickets into offline work orders for human or connected source reviewers without verifying facts.
`generate_source_review_packet_bundle.py` exports the current source-review session as pending JSON/JSONL packet templates and a human checklist.
`audit_source_review_packets.py` checks source-review packet files for ticket validity, final-status readiness, human-review gates, duplicates, and obvious secrets.
`rehearse_source_review_packet_imports.py` dry-runs all source-review packet imports without writing evidence logs.
`generate_agent_handoff.py` writes `docs/AGENT_HANDOFF.md` and `registry/agent-handoff.json` for the next agent entry point.
`audit_safety_boundaries.py` checks high/medium risk wiki safety boundaries and writes `docs/SAFETY_AUDIT.md`.
`generate_release_notes.py` writes `docs/RELEASE_NOTES.md` and `registry/release-manifest.json`.
`generate_change_summary.py` writes `docs/CHANGE_SUMMARY.md` and `registry/change-summary.json`.
`generate_hub_navigation.py` writes `docs/HUB_NAVIGATION.md` and `registry/hub-navigation.json`.
`generate_agent_routing_cards.py` writes `docs/AGENT_ROUTING_CARDS.md` and `registry/agent-routing-cards.json`.
`route_wiki.py` routes a query to the best wiki and prints reading order, source gates, safety rules, and prohibited actions.

## CI

GitHub Actions workflow: `.github/workflows/wiki-acceptance.yml`

It runs `python3 scripts/run_acceptance.py` for pull requests, pushes to `main` or `master`, and manual dispatches. See `docs/CI_USAGE.md`.

## 建议放置位置

```bash
~/agent-wiki-hub/
```

具体项目通过软链接引用：

```bash
mkdir -p ~/projects/my-project/knowledge
ln -s ~/agent-wiki-hub/wikis/finance-agent-wiki ~/projects/my-project/knowledge/finance-agent-wiki
```

## 交给 Codex

把 `CODEX_BUILD_PROMPT.md` 的内容完整复制给 Codex。Codex 会根据这些规则继续扩展、校验、索引和打包知识库。
