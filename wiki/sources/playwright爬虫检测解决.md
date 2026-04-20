---
title: "Playwright爬虫检测问题解决"
type: source
sources:
  - "raw/articles/f46fff1a_playwright自动化脚本工具打开浏览器网页被检测为爬虫导致无法执行脚本代码请问怎么解决playwright自动化脚本工具打开浏览器网页被检测为爬虫.md"
tags:
  - "playwright"
  - "anti-bot"
  - "stealth"
  - "web-scraping"
confidence: medium
created_at: "2026-04-20T10:00:00"
updated_at: "2026-04-20T10:00:00"
---

# Playwright爬虫检测问题解决

## 来源信息

- **作者**: 罗马车夫、测试逆转大师、xin TANG
- **平台**: 知乎
- **原始问题**: playwright自动化脚本工具打开浏览器网页被检测为爬虫，导致无法执行脚本代码，请问怎么解决？

## 问题分析

### 检测原理

网站检测Playwright的方式：
1. **navigator.webdriver** - 直接返回true
2. **User-Agent** - 包含HeadlessChrome标识
3. **插件列表** - 为空暴露自动化特征
4. **WebGL信息** - 不符合正常浏览器特征

### 两层问题

**罗马车夫**指出存在两个层面：
1. **第一层** - 反爬检测(浏览器指纹不对)
2. **第二层** - Chromium功能残缺(浏览器本身缺失)

## 解决方案

### 第一层：反爬检测绕过

使用**playwright-stealth**:

```python
from playwright_stealth import stealth_sync, StealthConfig

BROWSER_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]

stealth_config = StealthConfig(
    webdriver=True,
    webgl_vendor=True,
    navigator_plugins=True,
    navigator_languages=True,
    navigator_user_agent=True,
    chrome_runtime=True,
    languages=("zh-CN", "zh", "en"),
    vendor="Google Inc.",
    renderer="ANGLE (Intel, Intel(R) UHD Graphics 630, OpenGL 4.5)"
)
```

### 第二层：功能缺失问题

**测试逆转大师**提供三种方案：

1. **启动本地Chrome**
   ```python
   browser = p.chromium.launch(channel="chrome", headless=False)
   ```

2. **加载本地缓存**
   ```python
   browser = driver.chromium.launch_persistent_context(
       channel="chrome",
       user_data_dir=USER_DIR_PATH,
       headless=False
   )
   ```

3. **CDP远程调试**
   ```bash
   chrome.exe --remote-debugging-port=1234 --user-data-dir="D:\\playwright_chrome"
   ```
   然后使用`connect_over_cdp()`接管。

### Cookie注入方案

最省事的方案：
```python
context.add_cookies(json.loads(Path("zhihu_cookies.json").read_text()))
```

## 技术对比

| 方案 | 优点 | 缺点 |
|------|------|------|
| playwright-stealth | 简单配置 | 基础检测约60-80%成功率 |
| 本地Chrome启动 | 完整功能 | 需要本地Chrome |
| Cookie注入 | 最省事 | 需要预先获取Cookie |
| Patchright | 更强反爬 | 更重依赖 |

## Related

- [[Playwright反爬虫突破]]
- [[浏览器自动化工具弊病]]
- [[playwright-stealth]]
- [[反爬虫技术]]