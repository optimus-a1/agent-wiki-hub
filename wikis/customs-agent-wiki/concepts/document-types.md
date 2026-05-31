---
title: Trade Document Types
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Trade Document Types

## Common documents

- Contract / Sales Contract: 买卖双方、合同号、签署日期、货物、数量、价格、贸易术语、付款方式、交货条件。
- Commercial Invoice: 发票号、发票日期、卖方、买方、品名、规格、数量、单价、总价、币制、贸易术语。
- Packing List: 包装件数、包装方式、毛重、净重、体积、唛头、箱号、托盘或箱明细。
- Factory Inspection Sheet / Factory Test Report: 生产批次、检验项目、检验结果、检验日期、检验员或质检章。
- Certificate of Conformity / Quality Guarantee: 合格保证、适用标准、批次或型号、制造商声明、签章日期。
- Bill of Lading / Air Waybill: 承运人、收发货人、通知方、起运港、目的港、件数、重量、运输编号。
- Declaration Draft / Customs Form: 申报要素、HS 编码、监管条件、成交方式、原产国、境内收发货人。

## Extraction principle

同一字段在不同单证中可能名称不同。Agent 应把字段映射到统一 schema，再做差异比对。

## Cross-document roles

- 合同通常是交易基础，适合校验双方、货物、价格、贸易术语和付款条件。
- 发票通常是金额基础，适合校验金额、币制、单价、数量和收付款主体。
- 装箱单通常是物流基础，适合校验件数、包装、毛重、净重和体积。
- 厂检单和合格保证通常是质量基础，适合校验批次、型号、标准和检验结论。
- 提运单通常是运输基础，适合校验承运信息、目的港、件重和收发货信息。

## Source notes

HS 编码、监管条件、单证格式要求、目的国进口要求和最新申报规则均为 `needs-source-update`。
