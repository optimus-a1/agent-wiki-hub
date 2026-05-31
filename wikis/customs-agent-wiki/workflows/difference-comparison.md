---
title: Document Difference Comparison Workflow
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Document Difference Comparison Workflow

## Purpose

比较多份单证之间的关键字段一致性，输出差异表、风险等级和人工复核建议。

## When to use

用于合同、发票、装箱单、厂检单、合格保证、提运单和申报草稿之间的校对。

## Core rules

1. 差异输出必须说明字段、文档、值、证据、严重程度和建议。
2. 不能只输出“有差异”，必须给出可复核定位。
3. 高风险差异不得自动通过。
4. 政策判断和 HS 编码判断必须要求权威来源。

## Workflow

1. 标准化字段：统一币种符号、数量单位、重量单位、日期格式和主体名称。
2. 建立对照：按合同号、发票号、品名、规格、批次或箱号建立匹配关系。
3. 数值校验：金额、币种、件数、毛重、净重、数量、单价和总价交叉计算。
4. 文本校验：品名、规格、型号、原产国、贸易术语和收发货人模糊匹配。
5. 风险分级：金额币种错误、毛重小于净重、主体错误为高风险；格式差异可为低风险。
6. 输出表格：生成字段差异表、风险摘要、人工复核建议和未能判断的字段。

## Difference table

```text
field | expected_source | document_a_value | document_b_value | evidence | risk_level | review_suggestion
```

## Edge cases

- 名称缩写、大小写和标点差异不一定是实质差异，但要保留原文。
- 四舍五入差异应设置容忍范围，并报告差异金额。
- 单位换算必须显示换算路径，不能静默修改。

## Validation checks

- 是否覆盖金额、币种、件数、毛重、净重、品名和规格？
- 是否输出风险等级和人工复核建议？
- 是否把低置信度 OCR 字段从自动通过中排除？

## Source notes

监管条件、申报要素、目的国规则、最新单证格式要求均为 `needs-source-update`。
