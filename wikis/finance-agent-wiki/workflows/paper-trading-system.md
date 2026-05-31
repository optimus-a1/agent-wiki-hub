---
title: Paper Trading System Workflow
status: stable
last_updated: 2026-05-26
risk_level: high
---

# Paper Trading System Workflow

## Purpose

设计模拟盘系统，验证数据、风控、执行流程和日志，而不是直接投入真实资金。

## Components

- market data adapter
- strategy sandbox
- risk engine
- simulated broker/exchange
- portfolio accounting
- event log
- dashboard
- alert system
- replay/backtest runner

## Workflow

1. 先接历史数据，不接真实下单权限。
2. 统一订单模型：market、limit、cancel、filled、partial、rejected。
3. 加入手续费、滑点、延迟和失败状态。
4. 风控引擎先于策略执行。
5. 所有动作写入不可变日志。
6. 评估指标必须包含收益、回撤、波动、胜率、风险暴露、最大连续亏损。
7. 通过人工验收后，仍默认保持模拟模式。
