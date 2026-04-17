# Search code, repositories, users, issues, pull requests...
Provide feedback
Saved searches

## 文章信息


- **平台**: github

## 摘要


AI agent skill: read Lark meeting transcripts, extract action items, and actually get them done

## 内容


zarazhangrui / lark-minutes-tasks Public Notifications Fork 9 Star 36 Code Issues 1 Pull requests Actions Projects Security and quality Insights zarazhangrui/lark-minutes-tasks main 1 Branch 0 Tags Code Folders and files Name Last commit message Last commit date Latest commit zarazhangrui Update CLI command from larksuite-cli to lark-cli 72c9fe2 · History 3 Commits LICENSE Initial commit: Lark Minutes Tasks skill README.md Add Chinese README with language switcher README_CN.md Add Chinese README with language switcher minutes.md Update CLI command from larksuite-cli to lark-cli Repository files navigation README MIT license English | 中文 Lark Minutes Tasks An AI agent skill that reads Lark/Feishu meeting transcripts, extracts action items, and actually gets them done. Not just a to-do list generator. The agent executes the tasks for you. What it does You give it a meeting transcript (Lark Minutes URL or meeting notes doc). It: Reads the full transcript Scans for Wake Word commands (phrases you said during the meeting to directly instruct the agent) Extracts every action item, both explicit ("I'll send you that doc") and implied For each item, figures out the best way to execute it (schedule a meeting, draft a message, search for info, create a doc, etc.) Shows you a numbered list. You pick which ones the agent should handle. Executes them. Done. Wake Word Set a trigger phrase (like "hey agent" or anything you want). Say it during a meeting, and the agent will pick up your command from the transcript after the meeting. You don't need to remember what you said. The agent remembers for you. Install Drop minutes.md into your agent's commands directory: Claude Code: cp minutes.md ~/.claude/commands/minutes.md Other agents: Place the file wherever your agent reads skill/command definitions from. Prerequisites Lark CLI installed and configured (lark-cli config init) User authentication completed (lark-cli auth login --domain all) Usage /minutes https://your-lark-instance.com/minutes/your-minute-token Or pass a meeting notes document URL: /minutes https://your-lark-instance.com/docx/your-doc-token The agent will walk you through the rest. Supported action types Type What the agent does Send message Drafts the message, copies to clipboard for you to paste Schedule meeting Checks calendars, finds free slots, creates the event Write document Creates a Lark doc with the content Research Searches web or Lark docs, summarizes findings Try a product Finds the link/install instructions, sends to you Create task Creates a Lark task with assignee and due date Read/review doc Fetches the doc, reads it, gives you a summary License MIT About AI agent skill: read Lark meeting transcripts, extract action items, and actually get them done Resources Readme License MIT license Activity Stars 36 stars Watchers 0 watching Forks 9 forks Report repository Releases No releases published Packages No packages published Contributors 2 zarazhangrui Zara Zhang claude Claude
