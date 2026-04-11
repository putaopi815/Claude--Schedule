#!/usr/bin/env bash
# ==============================================================================
# DingTalk Group Notification Script
# Sends markdown-formatted messages to DingTalk group via webhook
# Supports 4 robots — one per scheduled task
#
# Usage:
#   ./scripts/dingtalk_notify.sh --task ux-ai-daily --file output/ux-ai-daily/2026-04-11.md
#   ./scripts/dingtalk_notify.sh --task alpha-radar --file output/alpha-radar/2026-04-11.md
#
# Security: IP Whitelist mode (no signature required)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$PROJECT_ROOT/config/dingtalk.conf"

# Load config
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Config file not found: $CONFIG_FILE"
    exit 1
fi
source "$CONFIG_FILE"

# --- Parse arguments ---
if [[ "${1:-}" != "--task" ]]; then
    echo "Usage: $0 --task <task-name> --file <filepath>"
    echo "Tasks: ux-ai-daily, github-claude-skill, alpha-radar, weekly-intelligence"
    exit 1
fi

shift  # remove --task
TASK_NAME="${1:?Usage: $0 --task <task-name> --file <filepath>}"
shift  # remove task name

if [[ "${1:-}" == "--file" ]]; then
    shift
    FILE_PATH="${1:?Usage: $0 --task <task-name> --file <filepath>}"
else
    echo "Error: --file flag required"
    exit 1
fi

if [[ ! -f "$FILE_PATH" ]]; then
    echo "Error: File not found: $FILE_PATH"
    exit 1
fi

# --- Resolve webhook URL per task ---
get_webhook_url() {
    case "$1" in
        ux-ai-daily)           echo "${DINGTALK_WEBHOOK_UX_AI_DAILY:-}" ;;
        github-claude-skill)   echo "${DINGTALK_WEBHOOK_GITHUB_CLAUDE_SKILL:-}" ;;
        alpha-radar)           echo "${DINGTALK_WEBHOOK_ALPHA_RADAR:-}" ;;
        weekly-intelligence)   echo "${DINGTALK_WEBHOOK_WEEKLY_INTELLIGENCE:-}" ;;
        *)                     echo "" ;;
    esac
}

WEBHOOK_URL=$(get_webhook_url "$TASK_NAME")

if [[ -z "$WEBHOOK_URL" || "$WEBHOOK_URL" == *"YOUR_ACCESS_TOKEN_HERE"* ]]; then
    echo "Error: Webhook URL not configured for task '$TASK_NAME'"
    echo "Please update config/dingtalk.conf with the correct access_token"
    exit 1
fi

# --- Task display name mapping ---
declare -A TASK_TITLES=(
    ["weekly-intelligence"]="Weekly Intelligence"
    ["alpha-radar"]="Alpha Radar"
    ["github-claude-skill"]="GitHub + Claude-Skill"
    ["ux-ai-daily"]="UX-AI-Daily"
)

TITLE="${TASK_TITLES[$TASK_NAME]:-$TASK_NAME}"
DATE=$(date +"%Y-%m-%d")

# --- Build message content using jq for safe JSON encoding ---
SUMMARY=$(head -50 "$FILE_PATH")
FULL_TEXT="${SUMMARY}

---
> [View full report on GitHub](https://github.com/putaopi815/Claude--Schedule)"

PAYLOAD=$(jq -n \
    --arg title "${TITLE} - ${DATE}" \
    --arg text "$FULL_TEXT" \
    '{
        msgtype: "markdown",
        markdown: {
            title: $title,
            text: $text
        }
    }')

# --- Send notification ---
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$WEBHOOK_URL" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD")

HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | sed '$d')

if echo "$BODY" | grep -q '"errcode":0'; then
    echo "DingTalk notification sent successfully: ${TITLE} - ${DATE}"
    echo "Robot: ${TASK_NAME}"
else
    echo "DingTalk notification failed (HTTP ${HTTP_CODE}):"
    echo "$BODY"
    exit 1
fi
