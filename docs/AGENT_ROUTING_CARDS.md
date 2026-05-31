# Agent Routing Cards

Generated: 2026-05-31

## Purpose

These cards tell an agent which wiki to read, what order to read it in, where current facts are gated, and which actions are outside the allowed boundary.

## Start Here

- Agent handoff: [AGENT_HANDOFF.md](../docs/AGENT_HANDOFF.md)
- Hub navigation: [HUB_NAVIGATION.md](../docs/HUB_NAVIGATION.md)
- Routing CLI: [ROUTING_CLI.md](../docs/ROUTING_CLI.md)
- Source update queue: [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- Source refresh dashboard: [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- Source refresh playbook: [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- Source refresh tickets: [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- Source refresh wave runner: [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- Source reviewer queue: [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- Source review session plan: [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- Source review readiness matrix: [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- Source review work orders: [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- Source review packet bundle: [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- Source review packet audit: [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- Source review packet rehearsal: [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- Source evidence recorder: [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- Source evidence packet importer: [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- Source evidence packet fixtures: [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- Source refresh completion audit: [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- Source evidence quality audit: [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)
- Acceptance report: [ACCEPTANCE_REPORT.md](../docs/ACCEPTANCE_REPORT.md)
- Safety audit: [SAFETY_AUDIT.md](../docs/SAFETY_AUDIT.md)

## Router Table

| Wiki | Priority | Risk | Freshness | Triggers | Read First |
| --- | --- | --- | --- | --- | --- |
| [finance-agent-wiki](../wikis/finance-agent-wiki) | P0 | high | high | 金融, 投资, 财报, 估值, 市场数据, 回测, 风控, 交易系统, 资金费率, 套利 | [AGENTS.md](../wikis/finance-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/finance-agent-wiki/manifest.yaml), [README.md](../wikis/finance-agent-wiki/README.md) |
| [customs-agent-wiki](../wikis/customs-agent-wiki) | P0 | medium | high | 报关, 报检, 单证, 发票, 装箱单, 合同, 厂检, HS编码, 字段校对 | [AGENTS.md](../wikis/customs-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/customs-agent-wiki/manifest.yaml), [README.md](../wikis/customs-agent-wiki/README.md) |
| [coding-agent-wiki](../wikis/coding-agent-wiki) | P0 | medium | medium | 代码, 编程, debug, 测试, 部署, API, 数据库, Codex, GitHub | [AGENTS.md](../wikis/coding-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/coding-agent-wiki/manifest.yaml), [README.md](../wikis/coding-agent-wiki/README.md) |
| [agent-engineering-wiki](../wikis/agent-engineering-wiki) | P0 | medium | medium | Agent, RAG, 知识库, Codex Skill, AGENTS.md, 评测, MCP, 工作流 | [AGENTS.md](../wikis/agent-engineering-wiki/AGENTS.md), [manifest.yaml](../wikis/agent-engineering-wiki/manifest.yaml), [README.md](../wikis/agent-engineering-wiki/README.md) |
| [ecommerce-agent-wiki](../wikis/ecommerce-agent-wiki) | P1 | medium | high | 电商, 商品, 购物, 客服, 退货, 物流, SKU, 选品, 比价 | [AGENTS.md](../wikis/ecommerce-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/ecommerce-agent-wiki/manifest.yaml), [README.md](../wikis/ecommerce-agent-wiki/README.md) |
| [nodeops-agent-wiki](../wikis/nodeops-agent-wiki) | P1 | high | medium | 服务器, Linux, Docker, systemd, 日志, 监控, 节点, RPC, 故障 | [AGENTS.md](../wikis/nodeops-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/nodeops-agent-wiki/manifest.yaml), [README.md](../wikis/nodeops-agent-wiki/README.md) |
| [airdrop-agent-wiki](../wikis/airdrop-agent-wiki) | P1 | high | high | 空投, Web3, 项目研究, TGE, 钱包安全, 签名, 代币 | [AGENTS.md](../wikis/airdrop-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/airdrop-agent-wiki/manifest.yaml), [README.md](../wikis/airdrop-agent-wiki/README.md) |
| [content-agent-wiki](../wikis/content-agent-wiki) | P1 | low | medium | 内容, 写作, 日报, 公众号, 帖子, 标题, 摘要, 发布 | [AGENTS.md](../wikis/content-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/content-agent-wiki/manifest.yaml), [README.md](../wikis/content-agent-wiki/README.md) |
| [legal-agent-wiki](../wikis/legal-agent-wiki) | P2 | high | high | 法律, 合同, 条款, 法务, 合规, 协议 | [AGENTS.md](../wikis/legal-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/legal-agent-wiki/manifest.yaml), [README.md](../wikis/legal-agent-wiki/README.md) |
| [health-agent-wiki](../wikis/health-agent-wiki) | P2 | high | high | 健康, 体检, 营养, 运动, 症状, 药品 | [AGENTS.md](../wikis/health-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/health-agent-wiki/manifest.yaml), [README.md](../wikis/health-agent-wiki/README.md) |
| [research-agent-wiki](../wikis/research-agent-wiki) | P2 | medium | high | 论文, 研究, 综述, 实验, 数据集, 引用, benchmark | [AGENTS.md](../wikis/research-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/research-agent-wiki/manifest.yaml), [README.md](../wikis/research-agent-wiki/README.md) |
| [security-agent-wiki](../wikis/security-agent-wiki) | P2 | high | high | 安全, 审计, 漏洞, 权限, 密钥, 上线检查, 防御 | [AGENTS.md](../wikis/security-agent-wiki/AGENTS.md), [manifest.yaml](../wikis/security-agent-wiki/manifest.yaml), [README.md](../wikis/security-agent-wiki/README.md) |

## Cards

### finance-agent-wiki

- Domain: `finance`
- Priority: `P0`
- Risk level: `high`
- Freshness requirement: `high`
- Summary: Finance research, accounting analysis, market data, backtesting, risk control, and simulated trading systems.
- Source-update topics: 4
- Source-refresh tasks: 4
- Package: [finance-agent-wiki.zip](../packs/finance-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/finance-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/finance-agent-wiki/manifest.yaml)
- [README.md](../wikis/finance-agent-wiki/README.md)
- [rules](../wikis/finance-agent-wiki/rules/)
- [workflows](../wikis/finance-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Explain OHLCV, spread, order book, volume, and liquidity for research use.
- Design a paper-trading backtest with fee, slippage, and out-of-sample checks.
- Review a finance answer for personalized-investment-advice or real-money execution risk.

Safety rules:

- Educational, research, and simulation use only.
- Do not provide personalized investment advice.
- Default to paper trading or human-approved simulation.
- Require human confirmation before any high-risk financial action.

Do not do:

- Autonomous real-money order placement.
- Personalized buy, sell, hold, leverage, or allocation instructions.
- Claims about current prices, rates, exchange rules, or market conditions without source refresh.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "risk control" --wiki finance-agent-wiki
python3 scripts/run_acceptance.py
```

### customs-agent-wiki

- Domain: `customs_trade_documents`
- Priority: `P0`
- Risk level: `medium`
- Freshness requirement: `high`
- Summary: Trade document extraction, invoice and packing-list comparison, field mapping, validation, and review support.
- Source-update topics: 4
- Source-refresh tasks: 4
- Package: [customs-agent-wiki.zip](../packs/customs-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/customs-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/customs-agent-wiki/manifest.yaml)
- [README.md](../wikis/customs-agent-wiki/README.md)
- [rules](../wikis/customs-agent-wiki/rules/)
- [workflows](../wikis/customs-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Extract contract, invoice, packing list, inspection, and guarantee fields into JSON.
- Map English headers to Chinese document fields with confidence and evidence.
- Compare amount, currency, package count, gross weight, net weight, product name, and specification differences.

Safety rules:

- Treat outputs as structured review support, not final customs advice.
- Preserve source snippets, confidence, and unresolved fields.
- Flag policy, tariff, HS code, and regulatory questions as source-update topics.
- Require manual review for medium and high risk discrepancies.

Do not do:

- Inventing missing document values.
- Presenting current customs policy or legal classification as verified without authoritative sources.
- Hiding OCR uncertainty or document conflicts.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "field extraction" --wiki customs-agent-wiki
python3 scripts/run_acceptance.py
```

### coding-agent-wiki

- Domain: `software_engineering`
- Priority: `P0`
- Risk level: `medium`
- Freshness requirement: `medium`
- Summary: Software engineering workflows for clarification, minimal implementation, tests, debugging, deployment, and secure coding.
- Source-update topics: 4
- Source-refresh tasks: 4
- Package: [coding-agent-wiki.zip](../packs/coding-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/coding-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/coding-agent-wiki/manifest.yaml)
- [README.md](../wikis/coding-agent-wiki/README.md)
- [rules](../wikis/coding-agent-wiki/rules/)
- [workflows](../wikis/coding-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Clarify requirements and implement the smallest safe code change.
- Plan a test-first debugging workflow and regression check.
- Review deployment steps, secret handling, and Codex usage rules.

Safety rules:

- Read repository instructions before editing.
- Preserve user changes and keep edits scoped.
- Protect secrets, tokens, cookies, and private keys.
- Run relevant tests or explain why they could not run.

Do not do:

- Writing credentials into source files or logs.
- Discarding unrelated user changes.
- Skipping safety checks for deployment or destructive operations.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "test first debug deployment secrets" --wiki coding-agent-wiki
python3 scripts/run_acceptance.py
```

### agent-engineering-wiki

- Domain: `ai_agent_engineering`
- Priority: `P0`
- Risk level: `medium`
- Freshness requirement: `medium`
- Summary: Agent architecture, RAG, Knowledge Packs, Codex Skills, evals, source grounding, and safety boundaries.
- Source-update topics: 3
- Source-refresh tasks: 3
- Package: [agent-engineering-wiki.zip](../packs/agent-engineering-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/agent-engineering-wiki/AGENTS.md)
- [manifest.yaml](../wikis/agent-engineering-wiki/manifest.yaml)
- [README.md](../wikis/agent-engineering-wiki/README.md)
- [rules](../wikis/agent-engineering-wiki/rules/)
- [workflows](../wikis/agent-engineering-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/agent-engineering-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Design an agent as model plus tools plus knowledge plus workflow plus memory plus evals plus safety boundary.
- Build a RAG workflow with chunking, indexing, recall, reranking, citations, and evals.
- Define a Knowledge Pack with manifest, rules, workflows, evals, sources, and update logs.

Safety rules:

- Make instructions explicit and auditable.
- Do not add hidden instructions, secrets, or credentials.
- Use source-grounding tests for current or externally sourced facts.
- Keep evals tied to observable behavior and refusal boundaries.

Do not do:

- Embedding hidden behavior or unreviewed authority into packs.
- Claiming current model, API, MCP, or platform facts without source refresh.
- Skipping evals for safety-critical agent behavior.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "RAG source grounding evals" --wiki agent-engineering-wiki
python3 scripts/run_acceptance.py
```

### ecommerce-agent-wiki

- Domain: `ecommerce`
- Priority: `P1`
- Risk level: `medium`
- Freshness requirement: `high`
- Summary: Product catalog, SKU and SPU operations, customer service, recommendation constraints, returns, privacy, and platform policy gates.
- Source-update topics: 3
- Source-refresh tasks: 3
- Package: [ecommerce-agent-wiki.zip](../packs/ecommerce-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/ecommerce-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/ecommerce-agent-wiki/manifest.yaml)
- [README.md](../wikis/ecommerce-agent-wiki/README.md)
- [rules](../wikis/ecommerce-agent-wiki/rules/)
- [workflows](../wikis/ecommerce-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Normalize product catalog attributes and SKU data.
- Draft a customer support workflow for returns, refunds, logistics, and invoices.
- Review recommendation output for policy, consent, and privacy risk.

Safety rules:

- Respect privacy, consent, consumer protection, and platform rules.
- Mark fees, return policies, ads policy, and platform rules as source-update topics.
- Avoid deceptive claims, fake scarcity, or unsupported product promises.

Do not do:

- Inventing product availability, current pricing, or platform policy.
- Using private customer data without a clear need and consent basis.
- Generating manipulative or misleading sales tactics.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "customer service returns privacy" --wiki ecommerce-agent-wiki
python3 scripts/run_acceptance.py
```

### nodeops-agent-wiki

- Domain: `operations`
- Priority: `P1`
- Risk level: `high`
- Freshness requirement: `medium`
- Summary: Linux, Docker, systemd, logs, backups, monitoring, alerts, node operations, incident review, and rollback support.
- Source-update topics: 3
- Source-refresh tasks: 3
- Package: [nodeops-agent-wiki.zip](../packs/nodeops-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/nodeops-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/nodeops-agent-wiki/manifest.yaml)
- [README.md](../wikis/nodeops-agent-wiki/README.md)
- [rules](../wikis/nodeops-agent-wiki/rules/)
- [workflows](../wikis/nodeops-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Build an incident triage checklist using symptoms, logs, resources, network, and dependencies.
- Plan a backup and rollback gate before a production change.
- Review Docker or systemd operations for destructive-command risk.

Safety rules:

- Require backup and rollback planning before production changes.
- Require human confirmation for destructive or irreversible operations.
- Prefer read-only diagnostics before changes.
- Protect credentials, node keys, and private infrastructure details.

Do not do:

- Running destructive production commands without confirmation.
- Exposing private keys, mnemonics, tokens, or infrastructure secrets.
- Treating current install commands, versions, or chain rules as stable facts without source refresh.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "backup rollback monitoring" --wiki nodeops-agent-wiki
python3 scripts/run_acceptance.py
```

### airdrop-agent-wiki

- Domain: `web3_research`
- Priority: `P1`
- Risk level: `high`
- Freshness requirement: `high`
- Summary: Web3 project research, public task tracking, token and airdrop safety checks, wallet hygiene, and compliance boundaries.
- Source-update topics: 3
- Source-refresh tasks: 3
- Package: [airdrop-agent-wiki.zip](../packs/airdrop-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/airdrop-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/airdrop-agent-wiki/manifest.yaml)
- [README.md](../wikis/airdrop-agent-wiki/README.md)
- [rules](../wikis/airdrop-agent-wiki/rules/)
- [workflows](../wikis/airdrop-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/airdrop-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Research a project using official docs and public ecosystem signals.
- Create a wallet-safety checklist before signing a transaction.
- Review an airdrop task plan for Sybil, spam, fake identity, or platform-bypass risk.

Safety rules:

- Public research and safety checks only.
- Never request or store private keys, seed phrases, cookies, or session tokens.
- Flag project funding, TGE, tokenomics, eligibility, and rules as source-update topics.
- Require human review before signing or granting wallet permissions.

Do not do:

- Sybil evasion, spam, fake identity, or platform-rule bypass.
- Automating wallet actions that risk assets or account bans.
- Promising rewards or treating current airdrop rules as verified without source refresh.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "wallet safety public tasks" --wiki airdrop-agent-wiki
python3 scripts/run_acceptance.py
```

### content-agent-wiki

- Domain: `content_operations`
- Priority: `P1`
- Risk level: `low`
- Freshness requirement: `medium`
- Summary: Research briefs, newsletters, articles, posts, titles, summaries, style templates, fact checking, and publishing review.
- Source-update topics: 3
- Source-refresh tasks: 3
- Package: [content-agent-wiki.zip](../packs/content-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/content-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/content-agent-wiki/manifest.yaml)
- [README.md](../wikis/content-agent-wiki/README.md)
- [rules](../wikis/content-agent-wiki/rules/)
- [workflows](../wikis/content-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/content-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Turn source notes into a research brief with citations and uncertainty labels.
- Create a publishing checklist for style, claims, and platform fit.
- Review content for plagiarism, missing citations, or unsupported claims.

Safety rules:

- Separate facts, inference, opinion, and draft language.
- Cite sources for factual claims and mark current facts for source refresh.
- Avoid plagiarism and undisclosed copied text.

Do not do:

- Fabricating citations or current events.
- Publishing private, confidential, or copyrighted material without permission.
- Treating platform policy or trend claims as stable without source refresh.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "fact checking citations" --wiki content-agent-wiki
python3 scripts/run_acceptance.py
```

### legal-agent-wiki

- Domain: `legal_information`
- Priority: `P2`
- Risk level: `high`
- Freshness requirement: `high`
- Summary: Legal information support, contract review checklists, risk spotting, issue lists, and lawyer handoff preparation.
- Source-update topics: 2
- Source-refresh tasks: 2
- Package: [legal-agent-wiki.zip](../packs/legal-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/legal-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/legal-agent-wiki/manifest.yaml)
- [README.md](../wikis/legal-agent-wiki/README.md)
- [rules](../wikis/legal-agent-wiki/rules/)
- [workflows](../wikis/legal-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/legal-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Extract contract parties, obligations, deadlines, termination, liability, and dispute clauses.
- Create a legal-risk checklist for human counsel review.
- Summarize unresolved legal questions and source-update needs by jurisdiction.

Safety rules:

- Information and checklist support only.
- Do not provide final legal opinions.
- Require jurisdiction, date, and authoritative source checks for law or regulation.
- Escalate high-risk legal decisions to qualified counsel.

Do not do:

- Final legal advice or guaranteed outcomes.
- Inventing statutes, cases, regulatory status, or filing requirements.
- Removing attorney review points from high-risk outputs.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "contract review human counsel" --wiki legal-agent-wiki
python3 scripts/run_acceptance.py
```

### health-agent-wiki

- Domain: `health_education`
- Priority: `P2`
- Risk level: `high`
- Freshness requirement: `high`
- Summary: Health education, wellness explanations, triage-style safety reminders, red flags, and clinician handoff support.
- Source-update topics: 2
- Source-refresh tasks: 2
- Package: [health-agent-wiki.zip](../packs/health-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/health-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/health-agent-wiki/manifest.yaml)
- [README.md](../wikis/health-agent-wiki/README.md)
- [rules](../wikis/health-agent-wiki/rules/)
- [workflows](../wikis/health-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/health-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Explain a health topic in plain language with red-flag reminders.
- Create a question list for a clinician visit.
- Review an answer for diagnosis, prescription, or medical-guideline freshness risk.

Safety rules:

- Education and triage-style safety reminders only.
- Do not diagnose, prescribe, or replace clinician judgment.
- Mark guidelines, drug information, and medical recommendations as source-update topics.
- Escalate urgent symptoms or red flags to professional care.

Do not do:

- Diagnosis or treatment orders.
- Medication dosing or contraindication claims without authoritative source refresh and clinician review.
- Suppressing emergency or clinician escalation advice.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "red flags clinician review" --wiki health-agent-wiki
python3 scripts/run_acceptance.py
```

### research-agent-wiki

- Domain: `research`
- Priority: `P2`
- Risk level: `medium`
- Freshness requirement: `high`
- Summary: Academic research workflows, paper reading, source grounding, citation hygiene, synthesis, limitations, and reproducibility.
- Source-update topics: 2
- Source-refresh tasks: 2
- Package: [research-agent-wiki.zip](../packs/research-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/research-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/research-agent-wiki/manifest.yaml)
- [README.md](../wikis/research-agent-wiki/README.md)
- [rules](../wikis/research-agent-wiki/rules/)
- [workflows](../wikis/research-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/research-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/research-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Summarize a paper with claims, method, evidence, limitations, and citation trail.
- Build a literature review workflow with source-grounding checks.
- Design evals for citation accuracy and unsupported-claim detection.

Safety rules:

- Keep citations traceable to source text.
- Label speculation, limitations, and unresolved evidence gaps.
- Mark newest papers, datasets, leaderboards, and benchmarks as source-update topics.

Do not do:

- Fabricating citations, abstracts, datasets, or benchmark results.
- Presenting weak or unverified evidence as consensus.
- Omitting limitations that affect interpretation.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "source grounding citations" --wiki research-agent-wiki
python3 scripts/run_acceptance.py
```

### security-agent-wiki

- Domain: `defensive_security`
- Priority: `P2`
- Risk level: `high`
- Freshness requirement: `high`
- Summary: Defensive security review, hardening, secure code review, incident documentation, and risk triage.
- Source-update topics: 2
- Source-refresh tasks: 2
- Package: [security-agent-wiki.zip](../packs/security-agent-wiki.zip)

Required reading order:

- [AGENTS.md](../wikis/security-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/security-agent-wiki/manifest.yaml)
- [README.md](../wikis/security-agent-wiki/README.md)
- [rules](../wikis/security-agent-wiki/rules/)
- [workflows](../wikis/security-agent-wiki/workflows/)

Source gates:

- [source-notes.md](../wikis/security-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/security-agent-wiki/sources/source-refresh-log.md)
- [SOURCE_UPDATE_QUEUE.md](../docs/SOURCE_UPDATE_QUEUE.md)
- [SOURCE_REFRESH_DASHBOARD.md](../docs/SOURCE_REFRESH_DASHBOARD.md)
- [SOURCE_REFRESH_PLAYBOOK.md](../docs/SOURCE_REFRESH_PLAYBOOK.md)
- [SOURCE_REFRESH_TICKETS.md](../docs/SOURCE_REFRESH_TICKETS.md)
- [SOURCE_REFRESH_WAVE_RUNNER.md](../docs/SOURCE_REFRESH_WAVE_RUNNER.md)
- [SOURCE_REVIEWER_QUEUE.md](../docs/SOURCE_REVIEWER_QUEUE.md)
- [SOURCE_REVIEW_SESSION_PLAN.md](../docs/SOURCE_REVIEW_SESSION_PLAN.md)
- [SOURCE_REVIEW_READINESS_MATRIX.md](../docs/SOURCE_REVIEW_READINESS_MATRIX.md)
- [SOURCE_REVIEW_WORK_ORDERS.md](../docs/SOURCE_REVIEW_WORK_ORDERS.md)
- [SOURCE_REVIEW_PACKET_BUNDLE.md](../docs/SOURCE_REVIEW_PACKET_BUNDLE.md)
- [SOURCE_REVIEW_PACKET_AUDIT.md](../docs/SOURCE_REVIEW_PACKET_AUDIT.md)
- [SOURCE_REVIEW_PACKET_REHEARSAL.md](../docs/SOURCE_REVIEW_PACKET_REHEARSAL.md)
- [SOURCE_EVIDENCE_RECORDER.md](../docs/SOURCE_EVIDENCE_RECORDER.md)
- [SOURCE_EVIDENCE_PACKET_IMPORTER.md](../docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md)
- [SOURCE_EVIDENCE_PACKET_FIXTURES.md](../docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md)
- [SOURCE_REFRESH_COMPLETION_AUDIT.md](../docs/SOURCE_REFRESH_COMPLETION_AUDIT.md)
- [SOURCE_EVIDENCE_QUALITY_AUDIT.md](../docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md)

Example intents:

- Review code for defensive security weaknesses and remediation priorities.
- Create a hardening checklist without exploit steps.
- Triage security findings while excluding bypass, theft, persistence, or evasion instructions.

Safety rules:

- Defensive review only.
- Focus on risk explanation, detection, mitigation, and verification.
- Mark current CVEs, exploit status, dependency versions, and advisories as source-update topics.
- Require human approval for production security changes.

Do not do:

- Exploitation, persistence, evasion, credential theft, or bypass steps.
- Payloads or procedures that enable unauthorized access.
- Claims about current vulnerabilities or advisories without source refresh.

Validation commands:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
python3 scripts/search_wiki.py --query "defensive security hardening" --wiki security-agent-wiki
python3 scripts/run_acceptance.py
```

## Global Routing Rules

- Read root `AGENTS.md` before using or editing any wiki.
- For a specific domain task, read that wiki's `AGENTS.md`, `manifest.yaml`, `README.md`, `rules/`, then `workflows/`.
- For high-risk domains, read `rules/` before `workflows/` and keep human confirmation points in the output.
- Treat current prices, policies, laws, medical guidance, security advisories, platform rules, API parameters, and Web3 project rules as `needs-source-update` unless verified from authoritative sources.
- Do not add credentials, API keys, private keys, cookies, hidden instructions, or unsafe operational steps.
