# Claude--Schedule Project Instructions

This repo is used by 4 Claude Code Scheduled Tasks. Each task generates content, saves it to the `output/` directory, sends a DingTalk notification, and commits/pushes to GitHub.

## Project Structure

```
Claude--Schedule/
├── CLAUDE.md                    # This file - task instructions
├── README.md                    # Project documentation
├── .gitignore
├── config/
│   └── dingtalk.conf            # DingTalk webhook configuration
├── scripts/
│   └── dingtalk_notify.sh       # DingTalk notification script
└── output/
    ├── weekly-intelligence/     # Weekly AI intelligence reports
    ├── alpha-radar/             # Daily alpha/cutting-edge AI radar
    ├── github-claude-skill/     # Daily GitHub trending + Claude skills
    └── ux-ai-daily/             # Daily UX + AI digest
```

## DingTalk Notification

After generating content, ALWAYS send a DingTalk notification using:

```bash
bash scripts/dingtalk_notify.sh --task <task-name> --file <output-file-path>
```

Task names: `weekly-intelligence`, `alpha-radar`, `github-claude-skill`, `ux-ai-daily`

## Task Definitions

### 1. UX-AI-Daily (Every day at 9:30)

**Output**: `output/ux-ai-daily/YYYY-MM-DD-ai-ux-daily.md`

Generate a daily curated digest of AI + UX developments:
- **Tools**: New AI tools for design-to-code, UI generation, prototyping, agent workflows
- **News**: Industry announcements and product launches in AI + UX
- **GitHub**: Trending repos for AI agents, MCP tools, workflow automation
- **Insights**: Emerging design patterns, community discussions, expert analysis
- Top 5-10 high-signal items, quality over quantity
- Each item includes: concise summary, "Why it matters", source links

**After generating**, run:
```bash
bash scripts/dingtalk_notify.sh --task ux-ai-daily --file output/ux-ai-daily/YYYY-MM-DD-ai-ux-daily.md
```

### 2. GitHub + Claude-Skill (Every day at 9:00)

**Output**: `output/github-claude-skill/YYYY-MM-DD-github-claude-skill.md`

Generate daily GitHub trending + Claude skills report:
- **GitHub Trending**: Top trending repos related to AI, agents, MCP, developer tools
- **Claude Skills**: New or updated Claude Code skills, MCP servers, integrations
- **Developer Tools**: Notable releases, updates, and new developer tools
- **Community**: Interesting discussions, PRs, and open source contributions

**After generating**, run:
```bash
bash scripts/dingtalk_notify.sh --task github-claude-skill --file output/github-claude-skill/YYYY-MM-DD-github-claude-skill.md
```

### 3. Claude Code Alpha Radar (Every day at 10:00)

**Output**: `output/alpha-radar/YYYY-MM-DD-alpha-radar.md`

Generate a daily alpha/cutting-edge AI technology radar:
- **Breakthroughs**: Latest research papers, model releases, and technical advances
- **Alpha Products**: Early-stage AI products and tools worth watching
- **Industry Signals**: Funding, partnerships, strategic moves in AI
- **Technical Deep Dive**: One notable technical development explained in detail

**After generating**, run:
```bash
bash scripts/dingtalk_notify.sh --task alpha-radar --file output/alpha-radar/YYYY-MM-DD-alpha-radar.md
```

### 4. Claude Code Weekly Intelligence (Every Monday at 10:30)

**Output**: `output/weekly-intelligence/YYYY-MM-DD-weekly-intelligence.md`

Generate a weekly AI intelligence summary report:
- **Week in Review**: Key developments and trends from the past week
- **Model Updates**: New model releases, benchmarks, capabilities
- **Tool Ecosystem**: Major tool/framework updates and new releases
- **Market Moves**: Significant business/funding events in AI
- **Outlook**: What to watch for in the coming week
- Comprehensive weekly overview, deeper analysis than daily reports

**After generating**, run:
```bash
bash scripts/dingtalk_notify.sh --task weekly-intelligence --file output/weekly-intelligence/YYYY-MM-DD-weekly-intelligence.md
```

## Standard Workflow for Each Task

1. Research and generate the content using web search
2. Save the markdown file to the correct `output/<task>/` directory
3. Send DingTalk notification via `scripts/dingtalk_notify.sh`
4. Git add, commit, and push to the repository

## Commit Message Format

Use the following format for commit messages:
```
[task-name] Add <content-type> for <date>

Example:
[ux-ai-daily] Add AI+UX daily digest for 2026-04-11
[weekly-intelligence] Add weekly intelligence report for 2026-04-07
[github-claude-skill] Add GitHub+Claude skill report for 2026-04-11
[alpha-radar] Add alpha radar report for 2026-04-11
```
