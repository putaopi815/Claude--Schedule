# Claude Schedule

A collection of automated schedules — curated digests, reports, and notifications powered by Claude Code.

## Structure

```
Claude--Schedule/
├── ai-ux-daily/                     # AI+UX 每日日报
│   ├── YYYY-MM-DD-ai-ux-daily.md    # 日报内容
│   ├── dingtalk_notify.py           # 钉钉推送脚本
│   └── .env                         # 钉钉凭证（本地创建，不入库）
├── .github/workflows/               # GitHub Actions 自动化
│   └── dingtalk-ai-ux-daily.yml     # AI+UX 日报自动推送
├── .gitignore
└── README.md
```

## Schedules

### ai-ux-daily

AI + UX 每日精选日报，涵盖工具、新闻、GitHub 趋势和行业洞察。

- **推送**: 钉钉群（自动 + 手动）
- **触发**: push 新日报 / 每天北京时间 09:00 / 手动触发
- **格式**: Markdown，按分类组织，附来源链接

## Adding a New Schedule

1. 创建新目录: `your-schedule-name/`
2. 添加内容文件和推送脚本
3. 在 `.github/workflows/` 下创建对应的 workflow
4. 仓库级 Secrets 可共享，无需重复配置
