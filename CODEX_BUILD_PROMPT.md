# Copy-paste this entire prompt into Codex

你现在要把当前仓库建设成一个完整可用的 **Agent Wiki Hub**。这是一个给 Codex / AI Agent 使用的行业知识库系统，不是普通文档库。

## 0. 先做上下文读取

请先读取：

1. `AGENTS.md`
2. `README.md`
3. `registry/wiki-registry.yaml`
4. 每个 `wikis/*/manifest.yaml`
5. 每个 `wikis/*/AGENTS.md`

然后输出你识别到的知识库列表、缺失项和执行计划。

## 1. 总目标

把本仓库完善成以下形态：

```text
agent-wiki-hub/
  AGENTS.md
  README.md
  CODEX_BUILD_PROMPT.md
  .github/
    workflows/
      wiki-acceptance.yml
  registry/
    wiki-registry.yaml
  scripts/
    validate_wiki.py
    update_index.py
    search_wiki.py
    pack_wikis.py
  index/
    search_index.json
  packs/
  codex-skills/
    agent-wiki-builder/
      SKILL.md
      references/
  wikis/
    finance-agent-wiki/
    ecommerce-agent-wiki/
    coding-agent-wiki/
    nodeops-agent-wiki/
    airdrop-agent-wiki/
    customs-agent-wiki/
    agent-engineering-wiki/
    content-agent-wiki/
    legal-agent-wiki/
    health-agent-wiki/
    research-agent-wiki/
    security-agent-wiki/
```

## 2. 每个 Wiki 必须具备的标准结构

每个知识库必须包含：

```text
manifest.yaml          # 机器可读说明
README.md              # 人类可读说明
AGENTS.md              # Codex 使用规则
concepts/              # 概念解释
rules/                 # 判断规则、边界、安全约束
workflows/             # 操作流程和任务流程
cases/                 # 正反案例、失败案例、错误样本
tools/                 # API、平台、工具、文件格式说明
prompts/               # 给 Agent 的提示词模板
evals/                 # 测试题、验收题、评测 YAML
sources/               # 来源记录、更新计划、引用清单
update-log.md          # 更新日志
```

缺任何目录或文件都要补齐。

## 3. 知识填充原则

请把稳定的通用知识写入知识库，但不要伪造实时事实。

### 可以直接写入

- 稳定概念
- 通用工作流
- 风险控制框架
- 数据抽取规则
- 文档结构
- Agent 使用方式
- 测试和验收标准
- 常见错误案例
- 安全边界
- 需要人工确认的检查清单

### 必须标记为 `needs-source-update` 的内容

- 当前价格、利率、行情、交易所规则
- 法律法规、海关政策、平台政策
- API 参数、SDK 最新版本、软件安装命令
- 电商平台费率、退货政策、广告规则
- 医疗指南、药品信息
- 安全漏洞编号、依赖漏洞状态
- Web3 项目融资、TGE、空投规则

凡是需要最新信息的内容，写入 `sources/source-notes.md`，格式：

```md
- topic: xxx
  status: needs-source-update
  suggested_sources:
    - official docs
    - regulator site
    - project docs
  last_checked: YYYY-MM-DD
```

## 4. 重点扩展的 Wiki

优先级如下：

### P0 — 立刻完善

1. `finance-agent-wiki`
2. `customs-agent-wiki`
3. `coding-agent-wiki`
4. `agent-engineering-wiki`

### P1 — 第二批完善

5. `ecommerce-agent-wiki`
6. `nodeops-agent-wiki`
7. `airdrop-agent-wiki`
8. `content-agent-wiki`

### P2 — 保留标准结构并写基础规则

9. `legal-agent-wiki`
10. `health-agent-wiki`
11. `research-agent-wiki`
12. `security-agent-wiki`

## 5. 具体填充要求

### finance-agent-wiki

必须包含：

- 市场数据基础：OHLCV、order book、spread、volume、liquidity
- 财务分析基础：利润表、资产负债表、现金流、估值指标
- 风险控制：仓位、最大回撤、杠杆风险、流动性风险、操作风险
- 研究流程：从问题到数据、假设、验证、结论、风险提示
- 回测流程：数据质量、样本外测试、滑点、手续费、过拟合
- 交易系统原则：默认模拟盘、人工确认、日志、熔断、权限控制
- 输出边界：不得给个人化投资建议，不得默认执行真实交易

### customs-agent-wiki

必须包含：

- 合同、发票、装箱单、厂检单、合格保证等单证类型
- 字段映射规则：英文表头到中文字段
- 抽取流程：OCR/文本解析、结构化 JSON、差异比对、人工确认
- 校对规则：金额、币种、件数、毛重、净重、品名、规格、发货人
- 常见错误案例：单位不一致、币制不一致、数量不一致、发票号错误
- 输出格式：差异表、风险等级、建议人工复核点

### coding-agent-wiki

必须包含：

- 需求澄清、最小实现、测试先行、代码审查、回归测试
- Debug 流程：复现、定位、最小修复、测试、防回归
- 部署流程：环境变量、依赖、构建、迁移、回滚
- 安全开发：密钥不入库、输入校验、权限最小化、日志脱敏
- Codex 使用规则：先读 AGENTS.md，再改代码，再运行测试

### agent-engineering-wiki

必须包含：

- Agent = 模型 + 工具 + 记忆/知识 + 工作流 + 评测 + 安全边界
- RAG：切块、索引、召回、重排、引用、评测
- Knowledge Pack 标准：manifest、rules、workflows、evals、sources
- Codex Skills：SKILL.md、scripts、references、assets
- Eval：golden questions、behavior tests、source-grounding tests

### ecommerce-agent-wiki

必须包含：

- 商品目录、SKU、SPU、属性、库存、价格、优惠
- 客服流程：售前、售后、退换货、物流、发票
- 推荐规则：需求澄清、约束匹配、差异对比、风险提醒
- 平台政策必须标记 needs-source-update

### nodeops-agent-wiki

必须包含：

- Linux、Docker、systemd、日志、备份、监控、告警
- 变更前备份，生产操作人工确认
- 故障排查流程：症状、日志、资源、网络、依赖、回滚
- 防止破坏性命令误执行

### airdrop-agent-wiki

必须包含：

- 项目研究：官网、文档、团队、融资、生态、风险
- 钱包安全：签名前检查、权限管理、钓鱼识别
- 合规边界：不做女巫规避、不刷量、不绕过平台规则
- 只记录公开任务和安全提醒，不承诺收益

### content-agent-wiki

必须包含：

- 研究简报、日报、文章、长帖、短帖、标题、摘要
- 事实核查、引用、避免抄袭、平台差异化改写
- 风格模板与发布前检查清单

## 6. 质量验收

执行：

```bash
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
python3 scripts/search_wiki.py --query "field extraction" --wiki customs-agent-wiki
python3 scripts/pack_wikis.py
```

验收条件：

- 所有 Wiki 结构完整
- 所有 manifest 可解析
- 搜索索引可生成
- 每个 Wiki 至少有 8 个 Markdown/YAML 知识文件
- 每个 Wiki 至少有 5 个 eval 问题
- 每个高风险 Wiki 有明确安全边界
- 所有新增内容有 update-log 记录
- GitHub Actions workflow runs `scripts/run_acceptance.py`

## 7. 输出格式

完成后请输出：

1. 修改了哪些文件
2. 每个 Wiki 增强了哪些内容
3. 验证命令结果
4. 还需要联网更新的 topics
5. 下一步建议

## 8. 不允许做的事

- 不要伪造实时来源
- 不要把 API key、私钥、cookie 写入仓库
- 不要生成真实资金自动交易脚本
- 不要生成攻击、绕过、盗取、刷量、规避风控的步骤
- 不要给医疗诊断或最终法律意见
- 不要把平台政策写成永久事实；必须标记更新时间
