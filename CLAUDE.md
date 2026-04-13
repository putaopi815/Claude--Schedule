# Claude--Schedule Project Instructions

This repo is used by 4 Claude Code Scheduled Tasks. Each task generates content, saves it to the `output/` directory, sends a DingTalk notification, and commits/pushes to GitHub.

## Project Structure

```
Claude--Schedule/
├── CLAUDE.md                    # This file - task instructions
├── README.md                    # Project documentation
├── .gitignore
└── output/
    ├── weekly-intelligence/     # Weekly AI intelligence reports
    ├── alpha-radar/             # Daily alpha/cutting-edge AI radar
    ├── github-claude-skill/     # Daily GitHub trending + Claude skills
    └── ux-ai-daily/             # Daily UX + AI digest
```

## DingTalk Webhook Configuration

Each task has its own DingTalk robot. After generating content, you MUST send a notification using the curl command below.

**Webhook URLs:**
- **ux-ai-daily**: `https://oapi.dingtalk.com/robot/send?access_token=133b5756fa296821042b075d1f5913b47f7cea09378f9fc9640a1e5b150310a1`
- **github-claude-skill**: `https://oapi.dingtalk.com/robot/send?access_token=c2dffb9cbee65b4124e4fa478e3bba9ae7a970c9499fd5d5d2215b144cb74899`
- **alpha-radar**: `https://oapi.dingtalk.com/robot/send?access_token=fec4aa71a87432764715ac48ae2cc542f91f66a5738f6725650c5fd46ec1796c`
- **weekly-intelligence**: `https://oapi.dingtalk.com/robot/send?access_token=32d9a4e7aedd883f1f7137ce3ce8456a1dbfef10590566b294460c23dbe080d4`

## DingTalk Notification Method

After generating and saving the report, send notification using this curl command:

```bash
TITLE="任务标题"
WEBHOOK_URL="对应任务的webhook url"
SUMMARY=$(head -50 output-file-path)
PAYLOAD=$(jq -n --arg title "$TITLE" --arg text "$SUMMARY" '{"msgtype":"markdown","markdown":{"title":$title,"text":$text}}')
curl -s -X POST "$WEBHOOK_URL" -H "Content-Type: application/json" -d "$PAYLOAD"
```

If `jq` is not available, use python:
```bash
python3 -c "
import json, urllib.request
title = '任务标题'
with open('output-file-path', 'r') as f:
    text = ''.join(f.readlines()[:50])
data = json.dumps({'msgtype': 'markdown', 'markdown': {'title': title, 'text': text}}).encode()
req = urllib.request.Request('WEBHOOK_URL', data=data, headers={'Content-Type': 'application/json'})
print(urllib.request.urlopen(req).read().decode())
"
```

## Task Definitions

### 1. UX-AI-Daily (Every day at 9:30)

**Output**: `output/ux-ai-daily/YYYY-MM-DD-ai-ux-daily.md`
**DingTalk Webhook**: `https://oapi.dingtalk.com/robot/send?access_token=133b5756fa296821042b075d1f5913b47f7cea09378f9fc9640a1e5b150310a1`

#### MANDATORY: Timeliness Rules (时效性强制规则)

Every item in the report MUST have a verifiable publication date. Enforce these rules strictly:

1. **Priority window**: Past 24 hours (from report generation time)
2. **Extended window**: Past 3 calendar days (only if 24h content is insufficient)
3. **Hard cutoff**: Any content older than 3 days MUST be excluded — no exceptions
4. **Prohibited content**: Summaries, year-end lists, roundup articles, undated trend pieces
5. **Date labeling**: Every item MUST display its exact publication date AND a timeliness tag:
   - `过去24h` — published within last 24 hours
   - `过去3天内` — published within last 3 days
   - `今天` — published today
6. **Verification**: Before including any item, confirm its publication date from the source. If the date cannot be verified, do NOT include it.
7. **Self-check**: After drafting the report, re-scan all items. Remove any that fall outside the 3-day window.

#### Content Scope & Priority

**Information Sources (priority order):**
1. Official releases (product launches, model updates, company announcements)
2. High-quality tech media (The Verge, TechCrunch, InfoQ, VentureBeat, etc.)
3. GitHub Trending (repos with rapid star growth in past 1-3 days)
4. Tech communities (Hacker News, Reddit, Twitter/X)

**Focus Areas (priority order):**
1. **UX / Product Design AI tools** (HIGHEST priority)
   - UI generation / design-to-code / prototyping tools
   - AI Agent / workflow automation
   - Design assistance (user research, usability analysis)
2. **Major AI industry news**
   - New model releases / platform updates
   - AI agent / automation / human-AI interaction breakthroughs
3. **GitHub trending projects**
   - AI agents / MCP / workflow tools
   - New skill / prompt systems / frameworks
   - Must meet at least one: rapid star growth in 3 days, active community discussion, or first-time release
4. **AI-native UX trends**
   - New interaction patterns (agent UI, copilot UI)
   - Design paradigm shifts

**Fallback rule**: If UX-related content within the time window is insufficient, expand to broader AI industry (agent / infra / model) — but STILL within the 3-day time window.

#### Output Format

- 5-10 high-quality items only (quality over quantity)
- Each item MUST include: title, 1-2 sentence summary, why it matters (for UX/product), source link, **exact publication date**
- Group by category: 🧰 工具 Tools / 📰 新闻 News / 💻 GitHub / 💡 洞察 Insights
- Style: high information density, professional but concise, for UX/product designers

**After generating**, send DingTalk notification:
```bash
SUMMARY=$(head -50 output/ux-ai-daily/YYYY-MM-DD-ai-ux-daily.md)
PAYLOAD=$(jq -n --arg title "UX-AI-Daily - YYYY-MM-DD" --arg text "$SUMMARY" '{"msgtype":"markdown","markdown":{"title":$title,"text":$text}}')
curl -s -X POST "https://oapi.dingtalk.com/robot/send?access_token=133b5756fa296821042b075d1f5913b47f7cea09378f9fc9640a1e5b150310a1" -H "Content-Type: application/json" -d "$PAYLOAD"
```

### 2. GitHub + Claude-Skill (Every day at 9:00)

**Output**: `output/github-claude-skill/YYYY-MM-DD-github-claude-skill.md`
**DingTalk Webhook**: `https://oapi.dingtalk.com/robot/send?access_token=c2dffb9cbee65b4124e4fa478e3bba9ae7a970c9499fd5d5d2215b144cb74899`

**After generating**, send DingTalk notification:
```bash
SUMMARY=$(head -50 output/github-claude-skill/YYYY-MM-DD-github-claude-skill.md)
PAYLOAD=$(jq -n --arg title "GitHub+Claude-Skill - YYYY-MM-DD" --arg text "$SUMMARY" '{"msgtype":"markdown","markdown":{"title":$title,"text":$text}}')
curl -s -X POST "https://oapi.dingtalk.com/robot/send?access_token=c2dffb9cbee65b4124e4fa478e3bba9ae7a970c9499fd5d5d2215b144cb74899" -H "Content-Type: application/json" -d "$PAYLOAD"
```

### 3. Claude Code Alpha Radar (Every day at 10:00)

**Output**: `output/alpha-radar/YYYY-MM-DD-alpha-radar.md`
**DingTalk Webhook**: `https://oapi.dingtalk.com/robot/send?access_token=fec4aa71a87432764715ac48ae2cc542f91f66a5738f6725650c5fd46ec1796c`

**After generating**, send DingTalk notification:
```bash
SUMMARY=$(head -50 output/alpha-radar/YYYY-MM-DD-alpha-radar.md)
PAYLOAD=$(jq -n --arg title "Alpha Radar - YYYY-MM-DD" --arg text "$SUMMARY" '{"msgtype":"markdown","markdown":{"title":$title,"text":$text}}')
curl -s -X POST "https://oapi.dingtalk.com/robot/send?access_token=fec4aa71a87432764715ac48ae2cc542f91f66a5738f6725650c5fd46ec1796c" -H "Content-Type: application/json" -d "$PAYLOAD"
```

### 4. Claude Code Weekly Intelligence (Every Monday at 10:30)

**Output**: `output/weekly-intelligence/YYYY-MM-DD-weekly-intelligence.md`
**DingTalk Webhook**: `https://oapi.dingtalk.com/robot/send?access_token=32d9a4e7aedd883f1f7137ce3ce8456a1dbfef10590566b294460c23dbe080d4`

**After generating**, send DingTalk notification:
```bash
SUMMARY=$(head -50 output/weekly-intelligence/YYYY-MM-DD-weekly-intelligence.md)
PAYLOAD=$(jq -n --arg title "Weekly Intelligence - YYYY-MM-DD" --arg text "$SUMMARY" '{"msgtype":"markdown","markdown":{"title":$title,"text":$text}}')
curl -s -X POST "https://oapi.dingtalk.com/robot/send?access_token=32d9a4e7aedd883f1f7137ce3ce8456a1dbfef10590566b294460c23dbe080d4" -H "Content-Type: application/json" -d "$PAYLOAD"
```

## Timeliness Enforcement（强制实效性规则）

所有任务必须严格遵守以下实效性约束。这是硬性规则，不可跳过。

### 时间窗口（按优先级排列）

| 优先级 | 时间范围 | 收录条件 |
|--------|---------|---------|
| P0（最优先） | 过去 24 小时内 | 新发布 / 新版本 / star 爆发 / 社区热议 |
| P1（补充） | 过去 3 天内 | 明确的趋势信号（star 快速增长、HN/Reddit 热帖、版本发布） |
| P2（例外） | 超过 3 天 | **仅当**出现重大更新时收录（爆发式增长、里程碑版本、范式变化），并必须标注原因 |

### 搜索策略（必须执行）

1. **搜索查询必须包含当前日期或时间范围**
   - 使用 `"April 2026"`、`"this week"`、`"today"` 等时间限定词
   - 禁止使用无时间限定的泛搜索（如 "best AI tools"）
2. **多源交叉验证**
   - 每个项目至少从 2 个独立来源确认其时效性（GitHub release date、新闻报道日期、HN 讨论时间等）
   - 不能仅凭搜索结果排名判断时效性
3. **GitHub 项目必须验证**
   - 检查最近一次 commit / release 日期
   - 检查近 7 天 star 增长趋势
   - 无法验证时效性的项目不得收录

### 每条内容必须标注时效标签

每个收录项目必须包含以下标签之一：

- `🔴 24h内` — 过去 24 小时内发布/爆发
- `🟡 3天内` — 过去 3 天内发布/爆发
- `🟢 重大更新` — 超过 3 天但有重大更新（必须说明原因）
- `⚪ 持续趋势` — 持续增长中的项目（必须有近期数据支撑）

### 禁止收录的内容

- ❌ 没有明确发布日期或趋势数据的项目
- ❌ 仅因"star 总量高"而收录的老项目（没有近期增长信号）
- ❌ "awesome-xxx" 合集类仓库（除非本身在 24h 内爆发）
- ❌ 概念性项目（无可运行代码、无 release）
- ❌ 与前一天报告完全重复的内容（除非有新版本/新进展）

### 去重规则

- 生成报告前，必须检查 `output/<task>/` 目录中最近 3 天的历史报告
- 如果某项目已在历史报告中出现，仅在有**新版本、新功能、新里程碑**时才可再次收录，并必须标注"更新"
- 完全重复的内容直接跳过

### 各任务时效性要求

| 任务 | 主要时间窗口 | 最大回溯范围 |
|------|-------------|-------------|
| ux-ai-daily | 24 小时 | 3 天 |
| github-claude-skill | 24 小时 | 3 天 |
| alpha-radar | 24 小时 | 3 天 |
| weekly-intelligence | 7 天 | 14 天 |

### 报告头部必须包含时效声明

每份报告开头必须包含：

```markdown
> **Date**: YYYY-MM-DD
> **Time Window**: 过去 24h（优先）/ 3 天内（补充）
> **Sources Checked**: GitHub Trending / HN / Reddit / Twitter / Release Notes
> **Dedup Check**: ✅ 已对比最近 3 天报告
```

## Standard Workflow for Each Task (MUST follow)

1. **Check historical reports** — Read last 3 days of reports in `output/<task>/` for dedup
2. Research and generate the content using web search **with time-constrained queries**
3. **Verify timeliness** — Confirm each item has a verifiable recent date/signal
4. **Tag each item** — Add timeliness label (🔴/🟡/🟢/⚪)
5. Save the markdown file to the correct `output/<task>/` directory
6. Git add, commit, and **push to main branch** (IMPORTANT: must push to main to trigger DingTalk notification)
7. DingTalk notification is sent automatically by GitHub Actions when pushed to main

## Git Push Instructions (CRITICAL)

You MUST push to the main branch so that GitHub Actions triggers the DingTalk notification.
Use this exact command:

```bash
git add output/<task>/
git commit -m "[task-name] Add <content-type> for YYYY-MM-DD"
git push origin HEAD:main
```

**DO NOT use `git push` alone** — it pushes to the current branch which does NOT trigger notifications.
**ALWAYS use `git push origin HEAD:main`** to push directly to main.

## Commit Message Format

```
[task-name] Add <content-type> for <date>

Example:
[ux-ai-daily] Add AI+UX daily digest for 2026-04-11
[weekly-intelligence] Add weekly intelligence report for 2026-04-07
[github-claude-skill] Add GitHub+Claude skill report for 2026-04-11
[alpha-radar] Add alpha radar report for 2026-04-11
```
