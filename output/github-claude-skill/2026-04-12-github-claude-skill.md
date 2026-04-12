# AI Skills & Agents Daily

> Date: 2026-04-12 | Sources: GitHub Trending, HackerNews, Dev Community, X/Twitter

---

## 1. UX / Design Focused

### 1.1 VoltAgent/awesome-design-md

- **GitHub**: https://github.com/VoltAgent/awesome-design-md
- **Type**: Tool / Design Protocol
- **Trend**: 3天内爆发 -- 10天内从0到35K stars，GitHub史上增长最快的awesome列表
- **做什么**: 收集59+知名品牌的 DESIGN.md 文件，拖入项目即可让 AI coding agent 生成匹配的 UI 风格
- **核心能力**: 将设计系统（色彩、字体、视觉哲学、Do's/Don'ts）编码为 Markdown，成为 AI agent 的"设计上下文协议层"
- **使用场景**: 开发者将品牌 DESIGN.md 放入项目根目录，Claude Code / Cursor / Codex 自动按品牌风格生成 UI 组件
- **为什么重要（UX视角）**: 这是 design-to-code 的新范式 -- Markdown 成为人类设计师、AI agent 和代码之间的协议层。将"好看"从主观判断变为可编程的上下文输入，极大缩短 design → development gap
- **是否值得收藏**: **Yes** -- 代表AI原生设计工作流的基础设施级变化，CJK 扩展(awesome-design-md-jp)已出现

### 1.2 nextlevelbuilder/ui-ux-pro-max-skill

- **GitHub**: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **Type**: Claude Skill / Design Intelligence
- **Trend**: 持续活跃，4月7日Wiki更新，v2.0 发布
- **做什么**: AI SKILL，为 Claude Code 等 AI 助手提供专业 UI/UX 设计智能 -- 含161种产品类型、50+风格、99条UX指南
- **核心能力**: Design System Generator -- AI推理引擎分析项目需求，秒级生成完整定制设计系统（色板、字体、组件规范）
- **使用场景**: 输入"电商App"，自动生成完整设计系统；支持 React/Next.js/Vue/Svelte/SwiftUI/Flutter 等10种技术栈
- **为什么重要（UX视角）**: 将设计决策从人工判断变为AI驱动的推理系统，设计师可专注于策略层而非执行层
- **是否值得收藏**: **Yes** -- 跨平台兼容（Claude/Cursor/Copilot/Codex等18+助手），实用性极高

### 1.3 Dualite Alpha

- **Website**: https://dualite.dev
- **Type**: Tool / AI Frontend Engineer
- **Trend**: 已脱离Beta，进入Alpha正式发布
- **做什么**: 本地优先的AI前端工程师，支持从 Figma 导入设计、GitHub 双向同步，将设计/Prompt转为生产级代码
- **核心能力**: 全流程在浏览器本地执行（数据零外传），Figma→Code + GitHub同步，企业级数据隐私
- **使用场景**: 设计师在 Figma 完成设计后，Dualite 直接生成 React/Vue/Angular 代码并推送到 GitHub
- **为什么重要（UX视角）**: 真正缩短 Figma → Production 的距离，且解决了企业最大顾虑（数据隐私），local-first 是差异化关键
- **是否值得收藏**: **Yes** -- local-first + Figma集成 + GitHub同步是稀缺组合

---

## 2. GitHub Trending Agents

### 2.1 NousResearch/hermes-agent

- **GitHub**: https://github.com/NousResearch/hermes-agent
- **Type**: Agent / Self-Improving System
- **Trend**: **今日爆发** -- 今日+6,438 stars，总计59K stars，GitHub Trending #1
- **做什么**: 自我进化的AI Agent -- 从经验中创建技能、使用中改进技能、搜索自身历史对话、跨session构建用户模型
- **核心能力**: 内置学习循环（experience → skill creation → skill improvement），支持 Telegram/Discord/Slack/WhatsApp/Signal 多平台
- **使用场景**: 作为团队的持续进化助手 -- 处理客服、代码审查、研究任务，越用越聪明
- **为什么重要**: v0.8.0（4月8日发布）引入 MCP OAuth 2.1、实时模型切换、危险命令审批按钮 -- 这是 agent 从"工具"向"队友"进化的标志
- **是否值得收藏**: **Yes** -- 自进化agent的标杆项目，209个PR/82个issue在单版本解决

### 2.2 coleam00/Archon

- **GitHub**: https://github.com/coleam00/Archon
- **Type**: Workflow Engine / Harness Builder
- **Trend**: **今日GitHub Trending Top 3** -- 今日+1,346 stars，总计16.5K stars
- **做什么**: 首个开源AI编码Harness Builder -- 将AI编码工作流定义为YAML，使AI编码变得确定性和可重复
- **核心能力**: 像 Dockerfile 之于基础设施、GitHub Actions 之于 CI/CD -- Archon 之于 AI 编码工作流。规划→实现→验证→Code Review→PR创建全流程YAML化
- **使用场景**: 团队定义标准编码工作流（如：fix bug必须先规划→写测试→实现→验证→PR），AI agent严格按流程执行
- **为什么重要**: 解决了AI编码最大痛点 -- "每次结果不同"。从TypeScript完全重写，是 Harness Engineering 范式的开创者
- **是否值得收藏**: **Yes** -- 新范式（Harness Engineering），将改变团队管理AI编码的方式

### 2.3 multica-ai/multica

- **GitHub**: https://github.com/multica-ai/multica
- **Type**: Agent Platform / Multi-Agent Orchestration
- **Trend**: **今日GitHub Trending** -- 今日+1,948 stars，总计7.9K stars
- **做什么**: 开源 Managed Agents 平台 -- 将 coding agents 变成真正的团队成员，分配任务、追踪进度、技能复合
- **核心能力**: Agent全生命周期管理（任务分配→执行监控→技能复用），每个solution自动变成团队可复用skill
- **使用场景**: 像给同事分配Issue一样给Agent分配 -- Agent自动pickup、写代码、报告阻塞、更新状态
- **为什么重要**: 开源版 Claude Managed Agents，支持 Claude Code/Codex/OpenClaw/OpenCode，厂商中立+可自托管
- **是否值得收藏**: **Yes** -- 多agent协作的基础设施层，解决了"agent如何像人类团队一样工作"

### 2.4 obra/superpowers

- **GitHub**: https://github.com/obra/superpowers
- **Type**: Skill Framework / Development Methodology
- **Trend**: 持续热门 -- 今日+1,591 stars，总计147K stars
- **做什么**: Agent技能框架+软件开发方法论 -- 基于可组合"技能"的完整软件开发工作流
- **核心能力**: Brainstorming（写代码前先理清需求）→ Git Worktrees（隔离工作区）→ Writing Plans（2-5分钟粒度的任务拆解）
- **使用场景**: 让AI agent按方法论工作 -- 先问"你真正想做什么"，拆解为可验证的小任务，逐步实现
- **为什么重要**: 不只是工具而是方法论 -- 定义了AI agent应该如何做软件工程，而非只是"写代码"
- **是否值得收藏**: **Yes** -- 147K stars验证了其价值，代表agent开发的"正确方式"

---

## 3. Claude Skills

### 3.1 last30days-skill

- **GitHub**: https://github.com/mvanhorn/last30days-skill
- **Type**: Claude Skill / Research Agent
- **Trend**: v2.9.5 发布，新增 Bluesky/AT Protocol
- **工作流描述**: `/last30 [topic]` -- 并行搜索 Reddit/X/YouTube/HN/Polymarket/Web，按社区参与度评分，AI裁判综合为一份简报
- **使用时机**: 需要快速了解某话题近期社区动态时（如 `/last30 cursor vs windsurf` 获得对比分析）
- **是否值得收藏**: **Yes** -- 真正可用的research agent skill，跨平台兼容（Claude/Codex/Gemini CLI）

### 3.2 andrej-karpathy-skills (CLAUDE.md)

- **GitHub**: https://github.com/forrestchang/andrej-karpathy-skills
- **Type**: Claude Skill / Coding Best Practice
- **Trend**: **今日GitHub Trending** -- 今日+1,066 stars，总计13.6K stars
- **工作流描述**: 基于 Andrej Karpathy 对 LLM 编码陷阱的观察，封装为单个 CLAUDE.md 文件，改善 Claude Code 的编码行为
- **使用时机**: 任何使用 Claude Code 的项目 -- 拖入根目录即可提升代码质量和一致性

### 3.3 SkillsMP (Skills Marketplace)

- **Website**: https://skillsmp.com
- **Type**: Skill Marketplace / Ecosystem
- **Trend**: 已聚合96,751+ Claude Code Skills
- **工作流描述**: 从GitHub聚合agent skills，支持 SKILL.md 统一格式，一键安装到 Claude Code / Codex CLI
- **使用时机**: 寻找特定能力的 skill 时（如设计、测试、部署等），作为skill发现入口

---

## 4. Emerging Patterns（关键）

### Pattern 1: Markdown-as-Protocol（Markdown即协议）

**信号**: DESIGN.md + SKILL.md + CLAUDE.md + AGENTS.md 形成完整的 Markdown 协议生态
**含义**: Markdown 不再只是文档格式，而是**人类与AI agent之间的通用协议层**。设计意图（DESIGN.md）、技能定义（SKILL.md）、行为约束（CLAUDE.md）、agent角色（AGENTS.md）-- 全部用Markdown编码
**对UX的影响**: 设计师可以直接用Markdown定义设计系统，AI agent直接消费，完全跳过传统的设计交接流程

### Pattern 2: Harness Engineering（约束工程）

**信号**: Archon（YAML化AI编码流程）+ Superpowers（方法论驱动的agent工作流）
**含义**: 从"让AI自由发挥"转向"用确定性约束框架管理AI行为"。AI编码不再是黑盒，而是可审计、可重复的工程流程
**对UX的影响**: UX团队可以定义标准化的设计实现流程（如：accessibility检查 → responsive验证 → design token对齐），agent严格执行

### Pattern 3: Agent-as-Teammate（Agent即队友）

**信号**: Multica（任务分配+进度追踪）+ Hermes Agent（自我进化+跨session记忆）
**含义**: Agent从"一次性工具调用"进化为"持续存在的团队成员"，有记忆、有技能积累、有状态汇报
**对UX的影响**: 产品团队可以将"设计QA Agent"作为永久团队成员，持续检查UI一致性、无障碍性、响应式适配

### Pattern 4: Skill Composability（技能可组合性）

**信号**: Superpowers（可组合技能框架）+ SkillsMP（96K+ skills市场）+ everything-claude-code（136 skills + 30 agents）
**含义**: Agent能力不再是单一prompt，而是由可组合、可复用、可共享的模块化技能构成
**对UX的影响**: UI组件库的设计模式正在被复制到AI世界 -- "技能库"就是AI agent的"组件库"

---

## 5. Microsoft Agent Framework 1.0（行业基础设施）

- **Release**: 2026年4月3日正式发布
- **为什么重要**: .NET + Python 双语言支持，内置 MCP + A2A 协议，DevUI 可视化调试器。标志着 MCP+A2A 架构成为企业级agent系统的生产标准
- **MCP生态**: SDK月下载量突破9700万（Python+TypeScript），MCP v2.1 新增 Server Cards 标准

---

## Summary

| # | 项目 | 类型 | 趋势 | UX相关度 |
|---|------|------|------|----------|
| 1 | awesome-design-md | Design Protocol | 3天爆发 35K stars | ★★★★★ |
| 2 | ui-ux-pro-max-skill | Claude Skill | v2.0 发布 | ★★★★★ |
| 3 | Dualite Alpha | Figma→Code Tool | 正式发布 | ★★★★☆ |
| 4 | hermes-agent | Self-Evolving Agent | 今日#1 +6.4K | ★★☆☆☆ |
| 5 | Archon | Harness Builder | 今日Top3 +1.3K | ★★★☆☆ |
| 6 | multica | Agent Platform | 今日热门 +1.9K | ★★☆☆☆ |
| 7 | superpowers | Skill Framework | 持续热门 147K | ★★★☆☆ |
| 8 | last30days-skill | Research Skill | v2.9.5 | ★☆☆☆☆ |
| 9 | karpathy-skills | CLAUDE.md | 今日热门 +1K | ★★☆☆☆ |
| 10 | MS Agent Framework | Enterprise Infra | 4月3日GA | ★★☆☆☆ |

---

> **Today's Key Insight**: Markdown正在成为AI时代的"HTTP" -- 设计系统(DESIGN.md)、技能定义(SKILL.md)、行为约束(CLAUDE.md)全部编码为Markdown，构建出人类与AI agent之间的通用协议栈。对UX行业而言，掌握"用Markdown定义设计意图"将成为核心竞争力。
