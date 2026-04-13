# CLAUDE.md — Schedule Intelligence System

## Project Purpose

This repo produces two daily intelligence reports:
1. **AI + UX Daily Digest** — `YYYY-MM-DD-ai-ux-daily.md`（根目录）
2. **Alpha Radar** — `output/alpha-radar/YYYY-MM-DD-alpha-radar.md`

Target audience: Top 1% AI builders, UX designers, product builders.

---

## TIMELINESS ENFORCEMENT（强制时效性规则）

> **这是本项目最高优先级的硬性约束。违反时效性 = 报告无效。**

### Hard Rules（硬规则，零容忍）

1. **默认窗口：3 天**。只收录发布时间在 `today - 3 days` 内的内容。
2. **扩展窗口：最多 7 天**。仅当 3 天内高质量内容不足 5 条时，可扩展至 7 天，但必须在报告头部用 `> 时间范围：YYYY-MM-DD ~ YYYY-MM-DD（X天，扩展窗口）` 明确标注。
3. **绝对禁止**收录超过 7 天的内容，无论质量多高。
4. **每条 item 必须标注发布日期**（精确到天）。无法确认发布日期的内容不得收录。
5. **WebSearch 查询必须包含时间限定词**：使用当前年月（如 "April 2026"）或具体日期范围，禁止无时间限定的泛搜索。

### Verification Protocol（验证协议）

- 对每个候选条目执行时效性验证：
  - 优先从页面元数据中提取发布日期
  - 次选从 URL 中的日期模式识别（如 `/2026/04/12/`）
  - 无法确认日期 → 丢弃
- 在报告输出前，扫描所有条目，移除任何不在有效窗口内的内容

### Time Labels（时间标注格式）

```
Source:
{平台名} · {链接}（YYYY-MM-DD）
```

---

## Content Quality Rules（内容质量规则）

### Inclusion Criteria（收录标准，必须全部满足）

- **Actionable** — 读者可以直接应用
- **Novel** — 不是基础认知或常识
- **Insightful** — 有认知增量
- **Workflow-level** — 工作流级别，不是零散技巧

### Exclusion Criteria（排除标准，命中任一即丢弃）

- Beginner tutorials / 入门教程
- Obvious tips（如"写好 prompt"、"多用 context"）
- Marketing content / 软文
- 低信息密度（篇幅长但核心信息可以一句话说完）
- 重复信息（与同一期其他条目实质相同）
- 无法验证时效性的内容

### Priority Topics（优先方向）

1. AI agent workflows & multi-agent systems
2. Claude Code advanced usage & new features
3. Automation systems & CI/CD integration
4. MCP / integrations / tooling
5. Prompt engineering patterns & CLAUDE.md design
6. **UX / Product Design workflows（最高优先级）**
7. **Design → Code / Code → Design workflows**
8. AI in product building

---

## Output Rules（输出规则）

### Report Structure

- 每期 5-10 条，信息密度 > 数量
- 必须包含 Meta Summary（趋势 / 认知升级 / 机会点）
- 中文输出，保留关键英文术语
- 每条包含：Source（含日期）/ Summary / Key Insight / Why it matters / How to apply

### File Naming

- AI + UX Daily: `YYYY-MM-DD-ai-ux-daily.md`（根目录）
- Alpha Radar: `output/alpha-radar/YYYY-MM-DD-alpha-radar.md`

### Post-Generation Checklist

生成报告后必须执行：

1. **时效性终审**：逐条确认所有 item 的发布日期在有效窗口内
2. **保存文件**：写入对应路径
3. **DingTalk 通知**：
   ```bash
   SUMMARY=$(head -50 <report-file>)
   PAYLOAD=$(jq -n --arg title "<report-type> - YYYY-MM-DD" --arg text "$SUMMARY" \
     '{"msgtype":"markdown","markdown":{"title":$title,"text":$text}}')
   curl -s -X POST \
     "https://oapi.dingtalk.com/robot/send?access_token=fec4aa71a87432764715ac48ae2cc542f91f66a5738f6725650c5fd46ec1796c" \
     -H "Content-Type: application/json" -d "$PAYLOAD"
   ```
4. **Git commit & push**：
   ```bash
   git add <report-file>
   git commit -m "[<report-type>] Add report for YYYY-MM-DD"
   git push -u origin <current-branch>
   ```

---

## Search Strategy（搜索策略）

### Mandatory Time-Scoped Queries

每次搜索必须包含时间限定：

```
# GOOD
"Claude Code" workflow April 2026
"Claude Code" new features April 10 11 12 2026
site:reddit.com ClaudeAI tips April 2026

# BAD (禁止)
"Claude Code" workflow tips
Claude Code best practices
```

### Source Priority（信息源优先级）

1. GitHub（repos, commits, issues, discussions, releases）
2. Reddit（r/ClaudeAI, r/ClaudeCode, r/LocalLLaMA）
3. Twitter / X（AI builders, indie hackers）
4. YouTube（workflow demos）
5. Official changelogs & docs
6. Blogs / personal sites
7. Community summaries

### Search Breadth

- 每个报告至少执行 5 组不同角度的 WebSearch
- 覆盖：官方更新 / 社区讨论 / GitHub trending / 行业分析 / UX-specific
