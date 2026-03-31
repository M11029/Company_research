# Claude Code Source Code Analysis

**Source:** https://github.com/nirholas/claude-code
**Analysed:** 2026-03-31
**What it is:** The leaked/open-sourced internal source code of Anthropic's Claude Code CLI - their agentic coding tool. ~512,000 lines of TypeScript across ~1,900 files.

---

## Why This Matters

This is the first time a major AI lab's production agentic tool has been fully exposed at source level. It reveals exactly how Anthropic builds AI-powered software, what capabilities they are developing behind feature flags, and where the entire AI agent industry is heading.

---

## Key Technical Facts

| Metric | Value |
|--------|-------|
| Language | TypeScript (strict mode) |
| Runtime | Bun (not Node.js) |
| Lines of code | ~512,000 |
| Files | ~1,900 |
| Commits | ~2,119 |
| UI Framework | React + Ink (terminal rendering) |
| Core engine | QueryEngine.ts (~46K lines) |
| Tools | ~40 agent tools |
| Slash commands | ~85+ |
| React hooks | ~80 |
| UI components | ~140 |

---

## Architecture Summary

**Core pipeline:** User Input -> CLI Parser -> Query Engine -> LLM API -> Tool Execution Loop -> Terminal UI

The system is a React application rendered in the terminal using Ink. The central piece is the **QueryEngine** which:
1. Streams responses from Anthropic's API character-by-character
2. Detects when the LLM requests a tool call
3. Executes the tool, feeds results back into context
4. Loops until the LLM produces a final response

Every tool is a self-contained module with: input schema (Zod), permission model, execution logic, UI component, and concurrency declaration.

---

## Hidden Feature Flags (Unreleased Capabilities)

These are gated behind build-time feature flags - capabilities Anthropic is actively building but hasn't shipped yet:

| Flag | What It Reveals |
|------|-----------------|
| `PROACTIVE` | AI that acts autonomously without being asked |
| `COORDINATOR_MODE` | Multiple AI agents working in parallel on sub-tasks |
| `VOICE_MODE` | Voice input/output for hands-free coding |
| `DAEMON` | Background daemon mode - always-on AI |
| `AGENT_TRIGGERS` | Scheduled/triggered autonomous actions (cron jobs for AI) |
| `KAIROS` | Unknown subsystem (codename) |
| `MONITOR_TOOL` | AI monitoring capabilities |
| `WORKFLOW_SCRIPTS` | Automation scripting system |
| `BRIDGE_MODE` | Deep IDE integration (VS Code, JetBrains) |

---

## The 40 Agent Tools (What AI Can Do)

### File Operations
- Read, write, edit files (including images, PDFs, Jupyter notebooks)
- Glob pattern search, regex content search (ripgrep)

### Execution
- Bash/PowerShell command execution
- Interactive REPL sessions (Python, Node)

### Agent Orchestration
- **AgentTool** - spawn sub-agents
- **SendMessageTool** - inter-agent messaging
- **TeamCreateTool / TeamDeleteTool** - parallel agent teams
- **TaskCreateTool** - background task management
- **EnterWorktreeTool** - git worktree isolation per agent

### Web Access
- Web fetch (URL content retrieval)
- Web search

### Protocol Integration
- MCP (Model Context Protocol) - connect to external tool servers
- LSP (Language Server Protocol) - IDE-level code intelligence

### Planning & Control
- Plan mode (think before acting)
- Sleep/cron triggers for scheduled execution
- Structured output generation

---

## Subsystems Deep Dive

### Memory System (`src/memdir/`)
- Persistent memory via `CLAUDE.md` files (project-level and user-level)
- Auto-extracted memories from conversations
- **Team memory sync** - shared knowledge across team members

### Permission System (`src/hooks/toolPermission/`)
- Four modes: default (prompt each), plan (batch approve), bypass, auto (ML-based)
- Wildcard rules: `Bash(git *)`, `FileEdit(/src/*)`
- Every tool invocation gated before execution

### Plugin System (`src/plugins/`)
- Full lifecycle: discovery, installation, loading, execution, auto-update
- Plugins contribute tools, commands, and prompts
- Marketplace discovery

### Skill System (`src/skills/`)
- 16 bundled skills including batch ops, debugging, memory, code verification
- Users can create custom skills
- Skills bundle prompts + tool configurations

### Task System (`src/tasks/`)
- Background shell tasks, sub-agent tasks, remote agent tasks
- Parallel teammate agents
- **DreamTask** - background ideation (AI thinking while idle)

### Coordinator (`src/coordinator/`)
- Multi-agent orchestration
- Team creation/deletion, inter-agent communication
- Parallel work distribution

---

## What This Reveals About Where AI Is Going

### 1. AI Agents Are Becoming Operating Systems
Claude Code isn't a chatbot - it's a 512K-line operating system for AI. It has its own:
- File system access
- Process management (tasks, sub-agents)
- Permission system
- Plugin/extension architecture
- Memory/state persistence
- Inter-process communication (agent messaging)
- Scheduling (cron triggers)
- Network access (web fetch, MCP)

**Signal:** The future isn't "AI assistants" - it's AI operating systems that manage entire workflows.

### 2. Multi-Agent Orchestration Is The Next Frontier
The `COORDINATOR_MODE` flag and the entire coordinator subsystem reveal that Anthropic is building systems where multiple AI agents work together in parallel. One agent breaks down a task, spawns a team, each member works on a sub-task, and results are merged.

**Signal:** Single-agent AI is a transitional phase. The money will be in multi-agent platforms.

### 3. Always-On Autonomous AI Is Coming
The `DAEMON` flag, `AGENT_TRIGGERS`, `SleepTool`, and cron scheduling reveal Anthropic is building AI that:
- Runs continuously in the background
- Wakes up on triggers or schedules
- Acts proactively without human prompting (`PROACTIVE` flag)

**Signal:** AI will shift from "tool you use" to "colleague that works 24/7."

### 4. Voice + AI Agents = New Interface Paradigm
The `VOICE_MODE` subsystem with streaming speech-to-text and domain-specific vocabulary suggests AI coding via voice commands.

**Signal:** The keyboard won't be the primary AI interface for long.

### 5. The MCP Protocol Is Anthropic's Platform Play
Claude Code is both an MCP client AND server. This means:
- It can consume tools from any MCP-compatible server
- Other tools can consume Claude Code's capabilities
- It's a universal connector protocol

**Signal:** MCP is positioning to be the "USB standard" for AI tools. Building MCP-compatible tools/servers is a strategic bet.

### 6. Memory and Context Are The Moat
The memory system (CLAUDE.md files, auto-extracted memories, team sync) shows that persistent, shared AI memory is a first-class concern. The AI remembers across sessions and shares knowledge across teams.

**Signal:** The companies that solve AI memory/context best will win. This is a massive unsolved problem at scale.

### 7. Permissions and Safety Are Product Features
The four-tier permission system with ML-based auto-approval shows that safety isn't an afterthought - it's built into every tool invocation. This is both a product differentiator and a regulatory necessity.

**Signal:** AI safety/governance tooling is a massive market opportunity.

---

## How To Profit From These Insights

### Immediate Opportunities (0-12 months)

1. **Build MCP Servers/Tools**
   - MCP is the emerging standard for AI tool integration
   - Build MCP servers that connect AI agents to specific business domains (CRM, ERP, databases, APIs)
   - Every SaaS company will need MCP adapters - be the one who builds them

2. **AI Agent Infrastructure**
   - The codebase reveals massive infrastructure needs: task queuing, agent coordination, state management, permission systems
   - Build the "AWS for AI agents" - hosting, orchestration, monitoring
   - Focus on multi-agent coordination platforms

3. **AI Memory/Context Solutions**
   - The memory system is primitive (markdown files)
   - Build better AI memory: vector databases, knowledge graphs, team knowledge management
   - Enterprise AI memory management is an untapped market

4. **AI Permission/Governance Tooling**
   - Every enterprise deploying AI agents needs permission management
   - Build audit trails, approval workflows, policy engines for AI actions
   - Compliance/regulatory tooling for autonomous AI

### Medium-Term Plays (1-3 years)

5. **AI-Native Development Tools**
   - Claude Code proves AI-first IDEs are viable products
   - Build domain-specific AI coding tools (data science, mobile, embedded, etc.)
   - The plugin/skill system shows extensibility is key

6. **Voice-First AI Interfaces**
   - Voice + AI agents will be a major interface shift
   - Build voice-controlled AI tools for specific industries (construction, healthcare, field work)

7. **Autonomous AI Workflows**
   - The daemon/trigger system shows AI will run unattended
   - Build platforms for deploying, monitoring, and managing autonomous AI workflows
   - Focus on reliability, observability, and failure recovery

### Strategic Investment Themes

8. **Anthropic Themselves**
   - This codebase shows exceptional engineering depth and a clear multi-year roadmap
   - They're building a platform, not just a model

9. **Bun/Runtime Companies**
   - Anthropic chose Bun over Node.js for their flagship product
   - The JavaScript runtime war has real commercial implications

10. **Companies Building on MCP**
    - MCP adoption is a leading indicator of AI platform winners
    - Track which companies adopt MCP early

---

## Key Codebase Entry Points for Further Study

| File | Purpose | Why It Matters |
|------|---------|----------------|
| `src/QueryEngine.ts` | Core LLM loop (~46K lines) | How production AI tool loops actually work |
| `src/Tool.ts` | Tool base types (~29K lines) | How to build AI tool systems |
| `src/tools/` | All 40 tool implementations | Patterns for building AI capabilities |
| `src/coordinator/` | Multi-agent orchestration | Future of AI agent coordination |
| `src/tasks/` | Background task system | How autonomous AI tasks are managed |
| `src/services/mcp/` | MCP client/server | The protocol layer for AI interop |
| `src/hooks/toolPermission/` | Permission system | How AI safety is implemented in practice |
| `src/memdir/` | Memory system | How AI persistence works |
| `src/plugins/` | Plugin architecture | How AI extensibility is built |
| `src/skills/` | Skill system | Reusable AI workflow patterns |
