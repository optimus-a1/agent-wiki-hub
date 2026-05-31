---
title: Sample Document Difference Table
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Sample Document Difference Table

## Purpose

提供合同、发票和装箱单差异比对样例，展示风险等级和人工复核建议。

## When to use

用于测试单证差异表输出、金额币种校验、件重校验和品名规格一致性检查。

## Core rules

1. 差异表必须包含字段、各文档值、证据、风险等级和复核建议。
2. 高风险差异不得自动通过。
3. OCR 低置信度字段必须单列，不能覆盖确定字段。
4. 监管和申报判断必须要求权威来源。

## Workflow

1. 标准化合同、发票、装箱单字段。
2. 按合同号、发票号、品名、规格和数量匹配。
3. 比对金额、币种、件数、毛重、净重、品名和规格。
4. 输出差异表、风险摘要和人工复核建议。

## Sample input

```text
Contract:
Contract No.: SC-EXAMPLE-001
Goods: Stainless Steel Bottle
Specification: 750ml, Model SB-750
Quantity: 1000 PCS
Currency: USD
Total Amount: USD 3200.00

Commercial Invoice:
Invoice No.: INV-EXAMPLE-001
Goods Description: Stainless Steel Bottle
Specification: 750ml, Model SB-750
Quantity: 1000 PCS
Currency: EUR
Total Amount: EUR 3200.00

Packing List:
Goods: Stainless Steel Bottle
Packages: 48 CTNS
Gross Weight: 540 KGS
Net Weight: 560 KGS
```

## Expected difference table

```text
field | contract_value | invoice_value | packing_value | evidence | risk_level | review_suggestion
currency | USD | EUR | - | Contract Currency: USD; Invoice Currency: EUR | high | 核对发票币种是否录错，未确认前不得通过
packages | - | - | 48 CTNS | Packing List Packages: 48 CTNS; expected may be invoice/contract absent | medium | 补充发票或合同件数来源，确认是否少箱
gross_weight_vs_net_weight | - | - | gross 540 KGS, net 560 KGS | Packing List Gross Weight/Net Weight | high | 毛重小于净重，要求人工复核原始装箱单
amount | USD 3200.00 | EUR 3200.00 | - | Total Amount fields | high | 金额数字相同但币种冲突，需确认合同或发票更正
goods_specification | Stainless Steel Bottle / SB-750 | Stainless Steel Bottle / SB-750 | Stainless Steel Bottle | all goods fields | low | 装箱单缺少规格，建议补充或确认箱单模板
```

## Edge cases

- 币种不一致通常高风险，即使金额数字一致。
- 毛重小于净重为高风险。
- 件数缺失不一定错误，但会影响申报和物流核对。

## Validation checks

- 是否覆盖金额、币种、件数、毛重、净重、品名和规格？
- 是否输出 high/medium/low 风险等级？
- 是否给出人工复核建议？

## Source notes

真实单证的申报要求、监管条件、HS 编码和目的国规则必须实时核验。
