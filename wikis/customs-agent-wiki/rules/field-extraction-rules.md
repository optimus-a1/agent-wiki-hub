---
title: Customs Field Extraction Rules
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Customs Field Extraction Rules

## Core fields

- shipper / seller / exporter -> 发货人/卖方/出口商
- consignee / buyer / importer -> 收货人/买方/进口商
- invoice no. -> 发票号
- contract no. -> 合同号
- description of goods -> 品名
- specification / model -> 规格型号
- quantity -> 数量
- unit price -> 单价
- amount / total -> 总价
- currency -> 币制
- gross weight -> 毛重
- net weight -> 净重
- packages -> 件数/包装
- marks / shipping marks -> 唛头
- country of origin -> 原产国/地区
- terms / incoterms -> 贸易术语
- payment terms -> 付款方式
- port of loading -> 起运港
- port of destination -> 目的港
- manufacturer -> 生产商/制造商
- inspection result -> 检验结果
- certificate no. -> 证书号

## Rules

1. 抽取结果必须保留原文 evidence。
2. 不确定字段标记 `confidence: low`，不能强行填充。
3. 金额校验：数量 × 单价 ≈ 总价，允许说明四舍五入误差。
4. 重量校验：毛重通常不小于净重；异常需提示人工复核。
5. 政策、HS 编码、监管条件属于实时信息，必须标记 `needs-source-update`。

## Normalized JSON shape

```json
{
  "document_type": "commercial_invoice",
  "document_no": {"value": "", "evidence": "", "confidence": "high"},
  "parties": {
    "seller": {"name": "", "address": "", "evidence": ""},
    "buyer": {"name": "", "address": "", "evidence": ""}
  },
  "trade_terms": {"incoterm": "", "currency": "", "payment_terms": ""},
  "items": [
    {
      "description": "",
      "specification": "",
      "quantity": {"value": null, "unit": ""},
      "unit_price": {"value": null, "currency": ""},
      "amount": {"value": null, "currency": ""},
      "evidence": ""
    }
  ],
  "totals": {
    "amount": {"value": null, "currency": ""},
    "packages": {"value": null, "unit": ""},
    "gross_weight": {"value": null, "unit": ""},
    "net_weight": {"value": null, "unit": ""}
  },
  "warnings": []
}
```

## Validation rules

- 金额：逐项金额合计应与总金额一致；差异要输出绝对值、比例和可能原因。
- 币种：单价、金额、总金额币种应一致；混用币种必须标记高风险。
- 件数：合同、发票、装箱单、提运单件数不一致时至少中风险。
- 毛重/净重：毛重小于净重为高风险；单位缺失或 kg/lb 混淆要人工复核。
- 品名/规格：品名、型号、材质、用途在关键单证中不一致时需要差异表。
- OCR 置信度：低置信度字段不能参与自动通过，只能作为待复核项。
