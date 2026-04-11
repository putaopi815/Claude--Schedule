# Claude--Schedule

Claude Code Scheduled Tasks with DingTalk (钉钉) group notifications.

## Scheduled Tasks

| Task | Schedule | Description |
|------|----------|-------------|
| **UX-AI-Daily** | Every day 9:30 | AI + UX daily digest for designers & product builders |
| **GitHub + Claude-Skill** | Every day 9:00 | GitHub trending repos + Claude skills report |
| **Claude Code Alpha Radar** | Every day 10:00 | Cutting-edge AI technology & product radar |
| **Claude Code Weekly Intelligence** | Every Monday 10:30 | Weekly AI intelligence summary |

## Project Structure

```
Claude--Schedule/
├── CLAUDE.md                        # Task instructions for Claude Code
├── config/
│   └── dingtalk.conf                # DingTalk webhook config
├── scripts/
│   └── dingtalk_notify.sh           # DingTalk notification script
└── output/
    ├── weekly-intelligence/         # Weekly reports (Monday)
    ├── alpha-radar/                 # Daily alpha radar
    ├── github-claude-skill/         # Daily GitHub + skill reports
    └── ux-ai-daily/                 # Daily UX + AI digests
```

## DingTalk Setup

1. Open your DingTalk group → `...` → Group Settings → Smart Assistant → Add Robot
2. Choose **Custom** robot, set security to **IP Whitelist**
3. Copy the Webhook URL
4. Edit `config/dingtalk.conf` and replace `YOUR_ACCESS_TOKEN_HERE` with your actual token

## Manual Notification

```bash
# Send notification from a generated report
bash scripts/dingtalk_notify.sh --task ux-ai-daily --file output/ux-ai-daily/2026-04-11-ai-ux-daily.md

# Send a custom message
bash scripts/dingtalk_notify.sh "Custom Title" "Message content in **markdown**"
```

## How It Works

Each scheduled task runs as a Claude Code session that:
1. Researches and generates a markdown report
2. Saves it to `output/<task-name>/`
3. Sends a summary to DingTalk via webhook
4. Commits and pushes to this repository
