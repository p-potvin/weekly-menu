# Agent Manifest

## Multi-Agent Architecture

This repository implements a Redis-based multi-agent coordination system.
All agents inherit from `ExtrovertAgent` and are overseen by `LonelyManager`.
The `LonelyManager` reads task assignments from `TODO.md` and project milestones
from `ROADMAP.md` to dispatch work to the appropriate specialized agents.

### Core Framework (`vaultwares-agentciation/`)

| Component | File | Description |
|---|---|---|
| **AgentStatus** | `enums.py` | Status enum: LOST, WORKING, WAITING_FOR_INPUT, RELAXING |
| **RedisCoordinator** | `redis_coordinator.py` | Redis pub/sub wrapper (channel: `tasks`, `alerts`) |
| **AgentBase** | `base_agent.py` | Heartbeat loop, status updates, stop/start lifecycle |
| **ExtrovertAgent** | `extrovert_agent.py` | Peer registry, socialization routine, task dispatching |
| **LonelyManager** | `lonely_manager.py` | Heartbeat monitoring, alignment enforcement, task dispatch |

### Weekly Menu App Agents (`agents/`)

| Agent | File | Type | Skills |
|---|---|---|---|
| **PlannerAgent** | `agents/planner_agent.py` | `planner` | Architecture design, project scaffolding, CI/CD, cloud infrastructure, Docker Compose, deployment |
| **DataAgent** | `agents/data_agent.py` | `data` | Schema design, SQL migrations, Room entities, seed data, RLS policies, Zod schemas |
| **BackendAgent** | `agents/backend_agent.py` | `backend` | Express routes, auth middleware, menu generation service, nutrition/budget services, PostgreSQL queries, rate limiting, tests |
| **AndroidAgent** | `agents/android_agent.py` | `android` | Compose screens, ViewModels, Retrofit client, Room DAOs, Navigation, DataStore, WorkManager, security hardening, i18n |
| **UIUXAgent** | `agents/uiux_agent.py` | `uiux` | Theme design, component library, glassmorphism, motion specs, accessibility audit |
| **DocAgent** | `agents/doc_agent.py` | `doc` | OpenAPI spec, README files, architecture docs, user guides, FAQ |

### Legacy Media Pipeline Agents (`agents/`)

| Agent | File | Type | Skills |
|---|---|---|---|
| **TextAgent** | `agents/text_agent.py` | `text` | Text generation, captioning, prompt engineering, VQA |
| **ImageAgent** | `agents/image_agent.py` | `image` | Image generation, editing, masking, inpainting, outpainting |
| **VideoAgent** | `agents/video_agent.py` | `video` | Video trimming, frame sampling, effects, analysis, captioning |
| **WorkflowAgent** | `agents/workflow_agent.py` | `workflow` | Workflow parsing, ComfyUI/Diffusion export, validation |

### Task Routing

The `LonelyManager` reads `[AGENT:<type>]` tags from `TODO.md` to dispatch tasks.
Each task line format:

```
- [AGENT:backend] [P1] [STATUS:TODO] Implement JWT auth middleware
```

Priority levels: P1 (critical) → P2 (high) → P3 (medium) → P4 (low)
Status values: TODO → IN_PROGRESS → DONE | BLOCKED

## Redis Coordination

The system uses Redis pub/sub for real-time agent coordination:

- **Channel `tasks`** — all agents subscribe; heartbeats, status, JOIN/LEAVE, ASSIGN messages
- **Channel `alerts`** — LonelyManager publishes LOST agent alerts here
- **Redis hash `lonely_manager:team_state:<agent_id>`** — live team state queryable by external tools

### Message Types

| Action | Publisher | Description |
|---|---|---|
| `HEARTBEAT` | All agents | Sent every 5 seconds with current status |
| `STATUS` | All agents | Sent every 60s or after 3 actions |
| `JOIN` | All agents | Announced on startup |
| `LEAVE` | All agents | Announced on shutdown |
| `ASSIGN` | LonelyManager | Task dispatched to a specific agent |
| `RESULT` | Worker agents | Task result published after completion |
| `ALERT` | LonelyManager | Fired when an agent misses 5+ heartbeats |
| `REALIGN` | LonelyManager | Nudge sent to quiet/drifting agents |
| `REQUEST_UPDATE` | LonelyManager | Periodic status request to all agents |

## Entrypoints

| Script | Description |
|---|---|
| `run_coordinated_system.py` | Start all Weekly Menu agents + manager, dispatch Phase 0 bootstrap tasks |
| `run_lonely_manager.py` | Start only the LonelyManager |
| `run_worker_agent.py` | Start a single worker agent by type and ID |

## Quick Start

```bash
# 1. Install dependencies
pip install redis

# 2. Start Redis
redis-server vaultwares-agentciation/redis.conf

# 3. Run the full system
python run_coordinated_system.py

# Or run agents individually:
python run_lonely_manager.py &
python run_worker_agent.py --type planner --id planner-agent-1 &
python run_worker_agent.py --type data --id data-agent-1 &
python run_worker_agent.py --type backend --id backend-agent-1 &
python run_worker_agent.py --type android --id android-agent-1 &
```

## Rules & Compliance

All agents follow VaultWares security, privacy, and style guidelines.
See `.github/INSTRUCTIONS.md` for the full enterprise-wide guidelines.
See `.github/CONTRIBUTING.md` for the contribution process and security checklist.
See `ROADMAP.md` for project milestones and `TODO.md` for the complete task list.

