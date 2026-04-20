---
title: "Browser Fingerprinting"
type: "concept"
sources:
  - "raw/articles/709aff76_朱卫军 的想法 这几天用selenium操作chrome浏览器尝试采集一些电商数据但被网站检测出来后面就没法访问了我怀疑是 - 知乎.md"
tags:
  - "concept"
  - "browser"
  - "tracking"
  - "privacy"
  - "anti-bot"
  - "fingerprinting"
  - "security"
confidence: "high"
created_at: "2026-04-17T22:26:16.847986"
updated_at: "2026-04-17T22:26:16.847986"
related:
  - "Web Scraping Anti-Detection"
  - "Managed Scraping Browser"
  - "Selenium"
  - "Zhihu Discussion: Using Bright Data's Scraping Browser to Bypass Anti-Bot Detection"
---

# Browser Fingerprinting

## Definition
A technique used by websites to identify and track individual browsers based on unique configuration characteristics, even when cookies are cleared or private browsing is used. Anti-bot systems leverage fingerprinting to detect automated browsers like [[Selenium]] and Playwright.

## How It Works
Websites collect dozens of data points about a browser's configuration and environment, then combine them to create a "fingerprint" that is often unique among millions of browsers.

## Common Fingerprinting Vectors
1. **User Agent:** Browser name, version, and operating system
2. **Screen Resolution & Color Depth:** Display characteristics
3. **Installed Fonts:** List of available fonts (highly distinctive)
4. **Browser Plugins/Extensions:** Installed components and versions
5. **Canvas Fingerprinting:** Slight rendering differences in HTML5 Canvas
6. **WebGL Fingerprinting:** Graphics card and driver characteristics
7. **AudioContext Fingerprinting:** Audio processing capabilities
8. **Time Zone & Language Settings:** Regional configurations
9. **HTTP Header Ordering:** Sequence of headers sent by browser
10. **Hardware Concurrency:** Number of CPU cores available

## Anti-Bot Applications
Websites use fingerprinting to:
- Detect automation tools that have inconsistent or uncommon fingerprints
- Identify returning users attempting to evade tracking
- Flag suspicious behavior patterns for further scrutiny
- Block known scraper fingerprints shared among security services

## Evasion Techniques
As discussed in [[Zhihu Discussion: Using Bright Data's Scraping Browser to Bypass Anti-Bot Detection]], modern [[Web Scraping Anti-Detection]] requires:
- **Fingerprint Spoofing:** Systematically modifying browser characteristics
- **Fingerprint Randomization:** Generating new, plausible fingerprints for each session
- **Fingerprint Consistency:** Ensuring all spoofed characteristics align logically (e.g., Windows fonts with Windows user agent)
- **Real Fingerprint Databases:** Using actual browser fingerprints from real devices rather than generating synthetic ones

## Managed Solutions
Services like [[Bright Data (亮数据)]]'s [[Managed Scraping Browser]] maintain large databases of real browser fingerprints and automatically apply them with proper consistency checks.

## Privacy Implications
Browser fingerprinting raises significant privacy concerns as it enables persistent tracking without user consent. This has led to increased browser protections and regulatory scrutiny.

## Related
- [[Web Scraping Anti-Detection]]
- [[Managed Scraping Browser]]
- [[Selenium]]
- [[Zhihu Discussion: Using Bright Data's Scraping Browser to Bypass Anti-Bot Detection]]

## Related
- [[Web Scraping Anti-Detection]]
- [[Managed Scraping Browser]]
- [[Selenium]]
- [[Zhihu Discussion: Using Bright Data's Scraping Browser to Bypass Anti-Bot Detection]]