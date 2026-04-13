# Claude--Schedule Project Rules

## Project Overview

This repo produces time-sensitive intelligence reports (daily digests, weekly intelligence) about AI + UX developments. All output is date-stamped and must reflect real-world recency.

## Mandatory Timeliness Enforcement

### Date Accuracy

- All reports MUST use the **actual current date** from the system context (`currentDate`). Never guess or hardcode dates.
- File names follow `YYYY-MM-DD-{report-type}.md`. The date in the filename MUST match the report's publication date.
- If the current date is unavailable, STOP and ask the user rather than fabricating one.

### Source Freshness Rules

| Report Type | Source Window | Hard Cutoff |
|---|---|---|
| Daily Digest | Past 24–48 hours | 72 hours max |
| Weekly Intelligence | Past 7 days | 10 days max |

- Every claim, tool mention, or trend MUST originate from a source within the allowed window.
- Older references are permitted ONLY to establish patterns, and MUST be explicitly labeled: `(older reference, {date}, included for pattern context)`.
- If insufficient fresh sources exist, reduce scope. Never pad with stale content.

### Search Query Rules

- All web searches MUST include the **current year** (e.g., "April 2026", not just "April").
- Prefer date-filtered queries. Include explicit time markers: "this week", "past 7 days", current month/year.
- Cross-validate: if a source lacks a visible publication date, do not treat it as fresh.

### Content Validation Checklist (run before finalizing any report)

1. **Date check** — Does the filename date match today's date?
2. **Window check** — Is every source within the allowed freshness window?
3. **Label check** — Are all older references explicitly labeled?
4. **Staleness check** — Does any section rehash information from a prior report in this repo? If yes, remove or reframe with new angle.
5. **Dead link risk** — Prefer primary sources (official blogs, GitHub repos, docs) over aggregator rewrites.

### Deduplication

- Before writing, READ all existing reports in the repo (`*.md` in root and `output/` subdirs).
- Do NOT repeat items already covered in a prior report unless there is a meaningful update.
- If a topic spans multiple days (e.g., a leak on day 1, official response on day 3), write the NEW development only and reference the prior report.

## Output Structure

```
/                                    # root
  YYYY-MM-DD-ai-ux-daily.md         # daily digests
  output/
    weekly-intelligence/
      YYYY-MM-DD-weekly-intelligence.md
```

## Quality Over Quantity

- Daily: 5-10 high-signal items max.
- Weekly: 5-8 top signals, 3-5 patterns, 3-5 workflows. No filler.
- If the week was quiet, say so. A short honest report beats a padded long one.

## Git Workflow

- Develop on the assigned feature branch (check session instructions).
- Commit message format: `[report-type] Add report for YYYY-MM-DD`
  - Examples: `[daily-digest] Add report for 2026-04-13`, `[weekly-intelligence] Add report for 2026-04-13`
- Push to the assigned branch. Do NOT push to `main` unless explicitly instructed by the user.

## External Notifications

- Do NOT send webhook/API calls (DingTalk, Slack, etc.) unless the user explicitly confirms the endpoint and payload in the current session.
- Treat all webhook URLs in task templates as **drafts requiring confirmation** — never auto-execute.
