# Claude--Schedule Project Instructions

This repo is used by 4 Claude Code Scheduled Tasks. Each task generates content, saves it to the `output/` directory, and commits/pushes to GitHub. DingTalk notifications are sent automatically by GitHub Actions — do NOT attempt to send them directly via curl.

## 语言要求（Language Requirement）

**所有报告内容必须用中文输出。** 包括：正文、摘要、洞察、模式描述、机会点等所有内容。
标题可保留中英双语格式（如 `## 🧩 Top Signals（本周关键信号）`），但内容一律使用中文。

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

## Task Definitions

### 1. UX-AI-Daily (Every day at 9:30)

**Output**: `output/ux-ai-daily/YYYY-MM-DD-ai-ux-daily.md`

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

### 2. GitHub + Claude-Skill (Every day at 9:00)

**Output**: `output/github-claude-skill/YYYY-MM-DD-github-claude-skill.md`

### 3. Claude Code Alpha Radar (Every day at 10:00)

**Output**: `output/alpha-radar/YYYY-MM-DD-alpha-radar.md`

### 4. Claude Code Weekly Intelligence (Every Monday at 10:30)

**Output**: `output/weekly-intelligence/YYYY-MM-DD-weekly-intelligence.md`

**⚡ Efficiency rules（防超时）:**
- Max **4 web searches** total — combine topics into broad queries
- Report length: **max 400 lines** — quality over quantity
- Do NOT read more than 1 historical report for dedup check
- Write directly from search results; do NOT loop back to verify every item

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

**⚡ Step 0 — Skip if already done（幂等检查）**
Before doing anything, check if today's output file already exists:
```bash
ls output/<task>/YYYY-MM-DD-*.md 2>/dev/null
```
If the file exists → **STOP. Do nothing. Output "Report already exists, skipping."**
Do NOT regenerate, do NOT re-search, do NOT re-commit.

1. **Check historical reports** — Read last 3 days of reports in `output/<task>/` for dedup
2. Research using web search — **max 3 searches total** (make them count, use broad queries)
3. **Verify timeliness** — Confirm each item has a verifiable recent date/signal
4. **Tag each item** — Add timeliness label (🔴/🟡/🟢/⚪)
5. Save the markdown file to the correct `output/<task>/` directory
6. Git add, commit, and **push to main branch** (IMPORTANT: must push to main to trigger DingTalk notification)
7. DingTalk notification is sent automatically by GitHub Actions when pushed to main

**Search limit by task:**
| Task | Max searches |
|------|-------------|
| ux-ai-daily | 3 |
| github-claude-skill | 3 |
| alpha-radar | 3 |
| weekly-intelligence | 4 |

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
