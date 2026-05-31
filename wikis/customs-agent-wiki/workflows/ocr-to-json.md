---
title: OCR to Structured JSON Workflow
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# OCR to Structured JSON Workflow

## Purpose

把扫描件、图片或 PDF 文本解析为可比对的结构化 JSON，同时保留证据和置信度。

## When to use

用于合同、商业发票、装箱单、厂检单、合格保证、提运单和申报草稿的字段抽取。

## Core rules

1. 不得凭经验补齐缺失字段。
2. 每个关键字段必须保留 evidence、页码或表格位置。
3. OCR 模糊、跨行断裂、单位缺失和手写改动必须标记低置信度。
4. 最新监管字段、HS 编码和目的国要求必须登记为 `needs-source-update`。

## Workflow

1. 文档识别：判断单证类型、语言、页数、表格区域和签章区域。
2. 文本预处理：保留原始 OCR 文本，修正常见断行，不删除可疑字符。
3. 表头映射：把英文表头映射到统一中文字段和标准 schema。
4. 行项目抽取：逐行抽取品名、规格、数量、单价、金额、币种和证据片段。
5. 合计抽取：抽取总金额、总件数、总毛重、总净重、体积和包装方式。
6. 置信度标注：按 OCR 清晰度、字段位置、格式合法性和交叉验证结果赋值。
7. JSON 输出：输出标准 JSON、warnings 和 unresolved_fields。

## Edge cases

- 同一字段出现在页眉、页脚和表格中时，优先使用正式字段区域，但保留冲突提示。
- 数字中的逗号、小数点和空格可能表示不同格式，必须统一解析并保留原文。
- 中英文品名混排时，不要翻译成新事实，应保留原文并可附解释性字段。

## Validation checks

- JSON 是否包含 evidence 和 confidence？
- 是否输出 unresolved_fields？
- 是否保留金额、币种、数量、重量、件数和品名规格的原文？
- 是否把监管和政策类信息标记为需要来源更新？

## Source notes

OCR 引擎版本、单证模板、监管字段和申报要求若依赖平台或法规，均需实时核验。
