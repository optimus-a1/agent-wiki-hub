---
title: Secure Development Rules
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Secure Development Rules

## Purpose

为编码 Agent 提供安全开发和密钥管理底线。

## When to use

用于处理身份认证、权限、文件上传、支付、数据库、日志、CI/CD 和第三方 API。

## Core rules

1. 不写入 API key、私钥、cookie、token、密码或真实凭据。
2. 不在日志、错误信息、测试快照或示例输出中回显敏感信息。
3. 权限默认最小化；写权限、生产权限和删除权限必须人工确认。
4. 输入必须验证，输出必须编码，文件路径必须防止越界。
5. 依赖漏洞、框架安全公告和平台规则属于 `needs-source-update`。

## Workflow

1. 识别数据分类：公开、内部、敏感、受监管。
2. 检查入口：HTTP、CLI、队列、文件、webhook、定时任务。
3. 检查权限：认证、授权、租户隔离、角色和审计日志。
4. 检查存储：密钥管理、加密、备份、保留期限和删除流程。
5. 检查输出：错误处理、日志脱敏、响应字段和下载权限。

## Edge cases

- 测试凭据也不能硬编码，使用占位符或本地环境变量名。
- 复制用户提供的配置前要扫描敏感字段。
- 安全修复不能通过关闭校验或扩大权限来完成。

## Validation checks

- 是否没有新增真实凭据？
- 是否有输入验证和权限检查？
- 是否对日志和错误输出做脱敏？

## Source notes

具体 CVE、依赖版本、框架安全默认值和云平台安全配置必须查官方来源。
