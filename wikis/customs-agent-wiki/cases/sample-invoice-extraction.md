---
title: Sample Invoice Extraction
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Sample Invoice Extraction

## Purpose

提供一个合成商业发票字段抽取样例，展示英文表头到标准 JSON 的映射方式。

## When to use

用于训练或测试 OCR/文本解析到结构化 JSON 的流程，不代表真实单证或真实交易。

## Core rules

1. 所有字段必须保留 evidence。
2. 不确定字段使用 `confidence: low`，不得强填。
3. 金额、币种、数量、件数、毛重和净重必须可校验。
4. HS 编码、监管条件和目的国规则必须标记 `needs-source-update`。

## Workflow

1. 识别文档类型为 commercial invoice。
2. 映射英文表头到标准字段。
3. 抽取 parties、items、totals 和 trade_terms。
4. 运行金额、币种和重量校验。
5. 输出 JSON 和 warnings。

## Sample input

```text
COMMERCIAL INVOICE
Invoice No.: INV-EXAMPLE-001
Invoice Date: 2026-05-01
Seller: Example Export Co., Ltd.
Buyer: Example Import LLC
Description of Goods: Stainless Steel Bottle
Specification/Model: 750ml, Model SB-750
Quantity: 1000 PCS
Unit Price: USD 3.20
Amount: USD 3200.00
Currency: USD
Incoterms: FOB Shanghai
Packages: 50 CTNS
Gross Weight: 620 KGS
Net Weight: 560 KGS
Country of Origin: China
```

## Expected JSON

```json
{
  "document_type": "commercial_invoice",
  "document_no": {
    "value": "INV-EXAMPLE-001",
    "evidence": "Invoice No.: INV-EXAMPLE-001",
    "confidence": "high"
  },
  "parties": {
    "seller": {
      "name": "Example Export Co., Ltd.",
      "evidence": "Seller: Example Export Co., Ltd.",
      "confidence": "high"
    },
    "buyer": {
      "name": "Example Import LLC",
      "evidence": "Buyer: Example Import LLC",
      "confidence": "high"
    }
  },
  "trade_terms": {
    "incoterm": "FOB Shanghai",
    "currency": "USD"
  },
  "items": [
    {
      "description": "Stainless Steel Bottle",
      "specification": "750ml, Model SB-750",
      "quantity": {"value": 1000, "unit": "PCS"},
      "unit_price": {"value": 3.20, "currency": "USD"},
      "amount": {"value": 3200.00, "currency": "USD"},
      "evidence": "Description of Goods ... Amount: USD 3200.00",
      "confidence": "high"
    }
  ],
  "totals": {
    "amount": {"value": 3200.00, "currency": "USD"},
    "packages": {"value": 50, "unit": "CTNS"},
    "gross_weight": {"value": 620, "unit": "KGS"},
    "net_weight": {"value": 560, "unit": "KGS"}
  },
  "warnings": []
}
```

## Edge cases

- 如果 `Currency` 和金额前缀不一致，应输出高风险 warning。
- 如果毛重小于净重，应输出高风险 warning。
- 如果 OCR 把 `3.20` 识别为 `320`，应通过总价校验发现异常。

## Validation checks

- 是否映射 Description of Goods、Specification、Quantity、Unit Price、Amount、Currency？
- 是否校验 1000 × 3.20 = 3200.00？
- 是否保留 evidence 和 confidence？

## Source notes

本样例为合成数据。真实 HS 编码、监管条件、目的国要求和汇率均需来源更新。
