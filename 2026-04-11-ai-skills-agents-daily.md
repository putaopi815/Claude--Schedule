# AI Skills & Agents Daily — April 11, 2026

> Curated feed of the freshest AI Skills, Agents, and reusable Workflows.
> Priority: UX/Design > Agent/Workflow > General AI Skills.
> Time window: past 24h (preferred), extended to 3 days where needed.

---

## 1. UX / Design Focused

### Figma Canvas Open to AI Agents (use_figma MCP)
- **Type:** Tool / Workflow
- **Link:** [Figma Blog — Agents, Meet the Canvas](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/)
- **Trend:** Open beta launched late March, April updates rolling out now
- **What it does:** Two new MCP tools — `use_figma` gives coding agents (Claude Code, Codex, Cursor, Copilot CLI, etc.) direct **write access** to Figma design files (frames, components, variables, auto layout, design tokens). `generate_figma_design` converts live HTML/websites into editable Figma layers.
- **Core capability:** Agents can now create and modify designs on the Figma canvas using your actual design system — not mockups, but real components and variables.
- **Use case:** A developer changes a UI component in code; `generate_figma_design` syncs it back to Figma. Then `use_figma` lets an AI agent iterate on the design using team conventions. Designers review and approve — no manual recreation.
- **Why important (UX):** This is the single biggest **design-development gap closure** of 2026. The design canvas is no longer read-only for AI. Figma's new **Skills** (markdown instruction files) let teams encode design-system intent — not just assets — so agents follow your conventions.
- **Collect:** Yes — foundational shift. Every UX team using Figma should evaluate this immediately.

### awesome-design-md — Plain-Text Design Systems for AI Agents
- **Type:** Skill / Tool
- **Link:** [github.com/VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | [getdesign.md](https://getdesign.md/)
- **Trend:** Created March 31, **41.6K stars** (+4.3K in first 3 days) — explosive viral growth
- **What it does:** A collection of 55+ DESIGN.md files capturing complete design systems (colors, typography, components, spacing, depth, responsive behavior) from **Stripe, Figma, Linear, Notion** and more — in plain-text Markdown. Drop one into your project root and coding agents generate UI matching that brand's visual language.
- **Core capability:** Design system as a single markdown file that any AI agent can read. No Figma, no tokens, no special tooling.
- **Use case:** Want Claude Code to generate UI that looks like Linear? Drop `linear-design.md` into your repo. Agent reads it, generates code with correct colors, spacing, typography, and component patterns.
- **Why important (UX):** This is the **AGENTS.md of design** — while AGENTS.md tells agents how to build, DESIGN.md tells them how things should look. Already spawned localized forks (JP, CN) and a companion site. This is becoming a de facto standard.
- **Collect:** Yes — one of the highest-signal UX items this month. Immediately usable.

### react-grab — Select Context from Running Apps for Coding Agents
- **Type:** Tool
- **Link:** [github.com/aidenybai/react-grab](https://github.com/aidenybai/react-grab)
- **Trend:** 3-day — 6.9K stars, actively maintained
- **What it does:** Point at any element on your running website, press Cmd+C → copies file name, React component, and HTML source to clipboard for pasting into coding agents. Plugins for Claude Code, Cursor, Codex, Gemini.
- **Core capability:** Solves the "context problem" — agents lack precise DOM/component context. react-grab bridges running app ↔ agent.
- **Use case:** Designer spots a spacing issue in the browser → Cmd+C on the element → paste into Claude Code → agent fixes the exact component with full context.
- **Why important (UX):** Claims **3x faster** frontend agent work. Eliminates the "which file is this?" problem entirely. Bridges visual review and code editing.
- **Collect:** Yes — small tool, huge workflow impact for frontend teams.

### Google Stitch 2.0 — AI-Native Design Canvas
- **Type:** Tool
- **Link:** [Google Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/)
- **Trend:** Relaunched March 18, still gaining adoption in April
- **What it does:** Complete overhaul into an AI-native infinite canvas. Features **Vibe Design** (start from emotion/intent, not wireframes), voice commands for real-time design critique, instant prototyping ("Stitch" screens together → click Play), and **DESIGN.md** support for agent-friendly design system export.
- **Core capability:** Full arc from concept → prototype without switching tools. Voice-driven iteration.
- **Use case:** PM describes a "calm onboarding flow that feels reassuring" → Stitch generates UI. Designer speaks refinements → agent updates in real-time. Export DESIGN.md → pass to Claude Code for implementation.
- **Why important (UX):** First truly **AI-native** design tool (not AI bolted onto existing UI). DESIGN.md as a design-system interchange format is a new pattern worth watching. Free during Google Labs phase.
- **Collect:** Yes — especially for rapid prototyping and design exploration phases.

---

## 2. GitHub Trending Agents

### Claude Managed Agents — Anthropic (April 8, 2026)
- **Type:** Agent Infrastructure / PaaS
- **Link:** [Claude Managed Agents Docs](https://platform.claude.com/docs/en/managed-agents/overview) | [TechRadar](https://www.techradar.com/pro/go-from-prototype-to-launch-in-days-rather-than-months-anthropic-reveals-claude-managed-agents-promises-to-make-agent-building-10x-faster)
- **Trend:** Launched April 8 (24h) — public beta
- **What it does:** Fully managed infrastructure for running Claude as an autonomous agent: sandboxed code execution, checkpointing, credential management, scoped permissions, end-to-end tracing. Supports single-task flows and complex multi-agent pipelines.
- **Use case:** Deploy a research agent that gathers data, writes reports, and commits code — Anthropic handles sandbox, state, error recovery. You focus on task design.
- **Why important:** Shifts agent deployment from DIY infrastructure to PaaS. Early adopters: **Notion, Rakuten, Sentry**. Pricing: standard token rates + $0.08/session hour. 10-point improvement in task success vs. standard prompting loops.
- **Collect:** Yes — if you're building production agents on Claude, this is the new default path.

### Hermes Agent v0.8.0 — Nous Research (April 8, 2026)
- **Type:** Agent Framework
- **Link:** [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Trend:** 24h — v0.8.0 "The Intelligence Release" | 52K+ stars | +26K stars this week
- **What it does:** Self-improving AI agent that creates skills from experience, maintains persistent memory, and deepens its model of you over time. Runs on any model (Nous Portal, OpenRouter 200+ models, OpenAI, self-hosted). Multi-platform: Telegram, Discord, Slack, WhatsApp, Signal, CLI.
- **Key v0.8.0 features:** Background task auto-notifications, live model switching, MCP OAuth 2.1, approval buttons, free MiMo v2 Pro support, 209 merged PRs.
- **Use case:** Personal AI agent that manages your comms across platforms, learns your preferences, and compounds skills over time — running on a $5 VPS.
- **Why important:** The hottest open-source agent on GitHub right now. Self-improving + multi-platform + skill-learning is the new agent baseline.
- **Collect:** Yes — reference implementation for self-improving agent architecture.

### Multica — Agents as Teammates (Trending this week)
- **Type:** Agent / Workflow
- **Link:** [github.com/multica-ai/multica](https://github.com/multica-ai/multica)
- **Trend:** 3-day — 6.1K stars | +3.5K this week | +1.5K today (viral growth)
- **What it does:** Open-source managed agents platform that turns coding agents (Claude Code, Codex, OpenClaw) into **real teammates** — assign issues, they write code, report blockers, update statuses autonomously. Agents have profiles, show up on boards, post comments, create issues.
- **Use case:** Assign a GitHub issue to an AI agent. It picks it up, writes the code, opens a PR, and reports back. Human reviews and merges.
- **Why important:** New paradigm: **agent lifecycle management**. Not "use an agent" but "manage a fleet of agents as team members." Self-hostable via Docker/K8s.
- **Collect:** Yes — represents the "agents as coworkers" pattern that's defining 2026.

### Archon — YAML Workflow Engine for Coding Agents (April 7 rewrite)
- **Type:** Workflow
- **Link:** [github.com/coleam00/Archon](https://github.com/coleam00/Archon)
- **Trend:** 3-day — 15.6K stars | Major rewrite April 7
- **What it does:** 17 default YAML-defined workflows that mix deterministic steps (bash, tests, linters) with AI-powered code generation. Git worktree isolation per workflow run. Automatic workflow routing from natural language.
- **Use case:** Define a "fix-bug" workflow in YAML: lint → reproduce → patch → test → commit. Agent follows it deterministically. No hallucination on process.
- **Why important:** Makes AI coding **repeatable and auditable** — YAML-as-process-definition for agents is a new infrastructure pattern.
- **Collect:** Yes — for teams wanting deterministic agent workflows.

### Microsoft Agent Framework 1.0 (April 7, 2026)
- **Type:** Agent Framework
- **Link:** [Microsoft DevBlog](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) | [github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- **Trend:** 3-day — v1.0 production release, unification of Semantic Kernel + AutoGen
- **What it does:** Microsoft's official SDK for building, orchestrating, and deploying AI agents. Python and .NET. Full MCP support for tool discovery, A2A 1.0 for cross-framework agent collaboration, browser-based DevUI debugger for visualizing agent execution.
- **Use case:** Enterprise multi-agent pipeline: sequential, concurrent, handoff, group chat patterns — all with streaming, checkpointing, human-in-the-loop, and pause/resume.
- **Why important:** The most concrete signal that **MCP + A2A** is becoming the enterprise default. If you're in a .NET shop, this is now your agent framework.
- **Collect:** Yes — enterprise-grade, production-ready, defines the enterprise agent standard.

### Goose v2026.4 — Block (Ongoing April updates)
- **Type:** Agent
- **Link:** [github.com/block/goose](https://github.com/block/goose)
- **Trend:** 3-day — 29K+ stars, MCP reference implementation
- **What it does:** Free, open-source AI agent by Block. Runs locally, supports any LLM, connects to 3,000+ tools via MCP. New: `goose serve` background service, Gemini OAuth, egress logging inspector (security), configurable fast models.
- **Use case:** Local-first coding agent that connects to your entire tool stack through MCP. Background mode for overnight tasks.
- **Why important:** MCP reference implementation — every new MCP spec feature lands in Goose first. The security-focused egress logging sets a new bar for agent transparency.
- **Collect:** Yes — best MCP-native agent for local development.

---

## 3. Claude Skills

### Claude Code Skills 2.0 Ecosystem
- **Link:** [Claude Code Skills Docs](https://code.claude.com/docs/en/skills) | [SkillsMP Marketplace](https://skillsmp.com/)
- **What changed:** Skills are now **folders**, not just markdown files. A skill folder can contain scripts, templates, reference docs, config. The SKILL.md format is an open standard working across Claude Code, Cursor, Codex CLI, Gemini CLI, Copilot.
- **Ecosystem:** SkillsMP indexes 500K+ skills. `skills.sh` (by Vercel Labs) is the main open directory. Install via `npx skills add <owner/repo>`.
- **Top trending skills this week:**
  - **Superpowers** (145K stars, +2.1K/day) — Complete agentic dev workflow: brainstorm → spec → plan → subagent execution → review → merge.
  - **andrej-karpathy-skills** (11.7K stars, +3.7K/week) — CLAUDE.md that fixes LLM coding pitfalls: don't assume, don't hide confusion, surface tradeoffs.
  - **Front-End Design Skill** (22K stars, 133K weekly installs) — Standard for web interface validation.
- **When to use:** Install Superpowers for structured development. Use andrej-karpathy-skills to improve agent code quality. Browse SkillsMP for domain-specific skills.

### New Skills This Week (April 7–11)
- **[project-architect](https://github.com/ersinkoc/project-architect)** (114 stars) — Documentation-first project planning agent. Generates specs, implementation plans, tasks, single-shot prompts. Works with Claude Code, Cursor, Codex, 40+ agents.
- **[PaperOrchestra](https://github.com/Ar9av/PaperOrchestra)** (42 stars) — Automated research paper writer: 5 composable skills + benchmark + autoraters. No API keys needed.
- **[marp-slides](https://github.com/robonuggets/marp-slides)** (42 stars) — MARP presentation skill with 22 curated example decks, SVG charts, dark/light themes.
- **[claude-office-skills](https://github.com/fivetaku/claude-office-skills)** (25 stars) — Claude in Excel/PowerPoint: DCF, LBO, 3-statement models, comps, deck refresh.
- **[fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)** (26 stars) — SVG+PNG technical diagram generation: 8 diagram types, 5 visual styles.

### Anthropic `ant` CLI
- **Link:** [github.com/anthropics/anthropic-cli](https://github.com/anthropics/anthropic-cli)
- **What it does:** Official CLI client for the Claude API. Build requests from typed flags or piped YAML (not hand-written JSON). Inline file contents with `@path`. Built-in `--transform` query for response extraction. Claude Code shells out to `ant` natively.
- **When to use:** Scripting Claude API calls, CI/CD pipelines, or when building agent orchestration that needs programmatic API access.

---

## 4. Emerging Patterns (Critical)

### Pattern 1: Design-System-as-Code (DESIGN.md / SKILL.md)
Both Figma (Skills as markdown) and Google Stitch (DESIGN.md) now use **markdown files as the interchange format for design intent**. This isn't just component libraries — it's encoding _why_ and _how_ a design system should be applied. Agents can read these files and make design-system-compliant decisions. **This is the bridge between design tools and coding agents.**

### Pattern 2: Managed Agent Infrastructure (DIY → PaaS)
Claude Managed Agents (Anthropic) and Multica (open-source) both represent the shift from "build your own agent loop" to "deploy agents on managed infrastructure." Sandboxing, state management, error recovery, and credential handling are now platform concerns, not developer concerns. Expect this pattern to become standard within months.

### Pattern 3: Agents as Persistent Team Members
Multica assigns issues to agents. Hermes Agent maintains memory across sessions. Rowboat (11.7K stars) turns work into a knowledge graph. The pattern: agents are no longer stateless tools — they're **persistent collaborators** with identity, memory, and autonomy. The "teammate" metaphor is replacing the "assistant" metaphor.

### Pattern 4: MCP OAuth 2.1 + Universal Connectivity
MCP now has 10,000+ servers, 97M monthly SDK downloads, and OAuth 2.1 support (landed in Hermes v0.8.0). The protocol is Linux Foundation-governed and supported by OpenAI, Google, Amazon, and Anthropic. MCP is the TCP/IP of agent tool-use — it's no longer optional.

### Pattern 5: YAML-Defined Deterministic Agent Workflows
Archon's rewrite to YAML workflow definitions represents a counter-movement to fully autonomous agents. For production use, teams want **repeatable, auditable, deterministic** agent behavior. YAML workflows provide guardrails while preserving AI flexibility at the code-generation step.

### Pattern 6: Biologically-Inspired Agent Memory (Hippo)
[Show HN: Hippo](https://github.com/kitfunso/hippo-memory) — Open-source library implementing 7 hippocampal memory mechanisms for AI agents: two-speed storage, memory decay, retrieval strengthening, sleep-based consolidation, confidence tiers, conflict detection, and multi-agent shared memory. Key insight: **"forget by default, earn persistence through use."** Running `hippo sleep` compresses episodes into semantic patterns. Already deployed on physical robots (Unitree Go2). This is a new primitive for agent architecture.

### Pattern 7: Generative UI as a Protocol (AG-UI / CopilotKit)
[CopilotKit](https://github.com/CopilotKit/CopilotKit) (30K stars) created the **AG-UI (Agent-User Interaction Protocol)** — a universal runtime for three generative UI patterns: Controlled (AG-UI), Declarative (A2UI/Open-JSON-UI), and Open-ended (MCP Apps). UI is no longer fixed developer-defined screens — it's **agent-adaptive interfaces** that reshape based on context. This is the frontend equivalent of MCP for the backend.

---

## UX Impact Summary

| Signal | Impact on UX Workflow |
|--------|----------------------|
| Figma `use_figma` MCP | Agents can now **write** to the design canvas. Design iteration becomes a code-design feedback loop. |
| awesome-design-md (41K stars) | Drop a markdown file → agent generates brand-consistent UI. Design systems become **portable text files**. |
| react-grab (7K stars) | Point at any UI element → agent gets full component context. **3x faster** frontend agent work. |
| Figma Skills (markdown) | Design system intent is now machine-readable. Agents follow your conventions, not generic defaults. |
| Google Stitch DESIGN.md | Design systems become portable between tools via markdown. Design → code handoff formalized. |
| AG-UI / CopilotKit | UI itself becomes agent-generated. Fixed screens → adaptive interfaces shaped by AI in real-time. |
| Claude Managed Agents | UX research agents, content generation pipelines, and design-QA agents can run in production. |
| Multica "agent teammates" | Design team could assign "create responsive variants" to an agent like assigning to a junior designer. |

**The design → development gap is shrinking from both sides.** Design tools are opening APIs to agents (Figma, Stitch). Coding agents are gaining design awareness (Skills, DESIGN.md). The convergence point: agents that understand both design intent and code implementation.

---

## AI-Native Product Design Opportunities

1. **Design-system-aware code generation** — Agent reads Figma Skills + DESIGN.md → generates code using correct components, spacing, tokens.
2. **Continuous design-code sync** — `generate_figma_design` + `use_figma` create a loop: code → design → iterate → code.
3. **Agent-driven design QA** — Deploy a managed agent that checks every PR against design system rules encoded in Skills.
4. **Voice-first prototyping** — Google Stitch's voice canvas as a new input modality for rapid UX exploration.
5. **Fleet-managed design operations** — Multica-style agent management for design tasks: responsive variants, accessibility audits, localization.

---

---

## Security Alert

### Flowise CVE-2025-59528 — CVSS 10.0 RCE (Active Exploitation)
Critical RCE in Flowise AI agent builder's CustomMCP node — 12,000+ instances exposed. The `convertToValidJSONString` function passes user mcpServerConfig directly into a `Function()` constructor. **Fix: upgrade to Flowise 3.0.6.** If you use Flowise in any agent workflow, patch immediately. [The Hacker News](https://thehackernews.com/2026/04/flowise-ai-agent-builder-under-active.html)

---

*Sources:*
- [Figma Blog: Agents, Meet the Canvas](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/)
- [awesome-design-md — GitHub](https://github.com/VoltAgent/awesome-design-md)
- [react-grab — GitHub](https://github.com/aidenybai/react-grab)
- [Google Stitch 2.0](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/)
- [Claude Managed Agents — TechRadar](https://www.techradar.com/pro/go-from-prototype-to-launch-in-days-rather-than-months-anthropic-reveals-claude-managed-agents-promises-to-make-agent-building-10x-faster)
- [Claude Managed Agents — API Docs](https://platform.claude.com/docs/en/managed-agents/overview)
- [Hermes Agent v0.8.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.4.8)
- [Multica — GitHub](https://github.com/multica-ai/multica)
- [Microsoft Agent Framework 1.0 — DevBlog](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/)
- [Archon — GitHub](https://github.com/coleam00/Archon)
- [Goose — GitHub](https://github.com/block/goose)
- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [SkillsMP Marketplace](https://skillsmp.com/)
- [Anthropic CLI](https://github.com/anthropics/anthropic-cli)
- [Superpowers — GitHub](https://github.com/obra/superpowers)
- [andrej-karpathy-skills — GitHub](https://github.com/forrestchang/andrej-karpathy-skills)
- [Hippo Memory — GitHub](https://github.com/kitfunso/hippo-memory)
- [CopilotKit AG-UI — GitHub](https://github.com/CopilotKit/CopilotKit)
- [Figma Release Notes April 2026](https://releasebot.io/updates/figma)
- [Anthropic Release Notes April 2026](https://releasebot.io/updates/anthropic)
- [Flowise CVE — The Hacker News](https://thehackernews.com/2026/04/flowise-ai-agent-builder-under-active.html)
