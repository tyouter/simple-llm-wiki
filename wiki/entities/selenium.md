---
title: "Selenium"
type: "entity"
sources:
  - "wiki/sources/知乎讨论-使用Selenium采集数据被检测.md"
  - "wiki/sources/zhihu-discussion-using-bright-data-s-scraping-browser-to-bypass-anti-bot-detection.md"
tags:
  - "tool"
  - "automation"
  - "web-scraping"
confidence: "high"
created_at: "2026-04-17T22:26:16.943136"
updated_at: "2026-04-20T00:00:00"
---

# Selenium

## 概述
开源的Web浏览器自动化工具，用于网页测试和数据采集，但因容易被反爬检测系统识别，常需配合代理轮换和指纹管理工具使用。

## 基本信息
- 类型：自动化工具
- 相关领域：Web自动化、数据采集、测试

## 挑战
- 容易被电商网站检测封锁
- 基本配置不足以应对高级指纹检测
- 需要配合[[Bright Data (亮数据)]]等解决方案

## 解决方案
- 使用Bright Data的Scraping Browser
- 通过API管理浏览器指纹
- 轮换住宅代理
- 自动处理CAPTCHA

## 相关概念
- [[Web Scraping Anti-Detection]]
- [[Bright Data (亮数据)]]
- [[朱卫军]]

## 相关
- [[知乎讨论-使用Selenium采集数据被检测]]