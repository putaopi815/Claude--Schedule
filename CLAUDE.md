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

## Standard Workflow for Each Task (MUST follow)

1. Research and generate the content using web search
2. Save the markdown file to the correct `output/<task>/` directory
3. **Send DingTalk notification using curl command above (MANDATORY, do NOT skip)**
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
