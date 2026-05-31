---
title: Agent Architecture
status: stable
last_updated: 2026-05-26
risk_level: medium
---

# Agent Architecture

## Definition

一个可落地的 Agent 通常不是只有模型，而是：

```text
Agent = Model + Tools + Knowledge + Workflow + Memory + Evals + Safety Boundaries
```

## Components

- Model: 理解、推理、生成。
- Tools: 搜索、文件、终端、API、浏览器。
- Knowledge: 结构化 Wiki、RAG、项目文档。
- Workflow: 任务拆解、执行顺序、确认点。
- Memory: 用户偏好、项目长期上下文。
- Evals: 行为测试、事实测试、回归测试。
- Safety: 权限、审批、风险边界。
