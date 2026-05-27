# Repo Operating Files Templates

## Zweck
Diese Datei enthält die Vollvorlagen für die Standarddateien, die in jedes aktive Repository gelegt werden sollen. Die Vorlagen sind so formuliert, dass ein Agent sie zuverlässig lesen und aktualisieren kann.

---

## `CONTEXT.md`

```md
# Repository Context

## Identity
- Repository name:
- Primary purpose:
- Business domain:
- Owner:
- Main deployment target:

## Current status
- Status summary:
- Current phase:
- Active branch or release line:
- Last major verified milestone:

## Active work
- Active Linear issues:
- Current implementation goal:
- Current blocker:
- Immediate next action:

## Architecture snapshot
- Main services:
- Main database(s):
- Message queues / brokers:
- External APIs:
- LLM routing layer:
- Automation / orchestration touchpoints:

## Constraints
- Security constraints:
- Performance constraints:
- Cost constraints:
- Deployment constraints:

## Source of supporting context
- Notion pages:
- Spec documents:
- Runbooks:
- Relevant dashboards:

## Known risks
- Risk 1:
- Risk 2:
- Risk 3:

## Last completed items
1.
2.
3.

## Update rules for agents
- Read this file before making changes.
- Update only facts that changed.
- Keep entries concrete and short.
- Reference Linear issue IDs when applicable.
- Do not add speculative future architecture as if it already exists.
```

---

## `MILESTONES.md`

```md
# Milestones

## Milestone overview
| Milestone | Status | Target outcome | Blocking dependency | Verification method |
|---|---|---|---|---|
| Example | Planned | Example outcome | Example dependency | Example verification |

## Active milestone
### Name

### Goal

### Scope
- 
- 
- 

### Excluded from scope
- 
- 

### Dependencies
- 
- 

### Success criteria
- 
- 
- 

### Current blockers
- 
- 

### Linked issues
- 
- 
```

---

## `DECISIONS.md`

```md
# Architecture Decisions

## Decision log

### ADR-001
- Title:
- Date:
- Status:
- Context:
- Decision:
- Alternatives considered:
- Why this won:
- Tradeoffs accepted:
- Follow-up implications:

### ADR-002
- Title:
- Date:
- Status:
- Context:
- Decision:
- Alternatives considered:
- Why this won:
- Tradeoffs accepted:
- Follow-up implications:
```

---

## `SYSTEM_MAP.md`

```md
# System Map

## Components
| Component | Type | Purpose | Dependencies | Runtime location |
|---|---|---|---|---|
| | | | | |

## Data flows
| Source | Destination | Protocol / Mechanism | Payload type | Failure mode |
|---|---|---|---|---|
| | | | | |

## Infrastructure references
- Primary host:
- Postgres:
- Redis:
- Queue / AMQP:
- Object storage:
- Reverse proxy:
- Observability:

## Ports and endpoints
| Service | Port | Exposure | Notes |
|---|---|---|---|
| | | | |
```

---

## Agent policy snippet
Diese Policy kann zusätzlich in ein Repo als `AGENT_OPERATING_RULES.md` gelegt werden.

```md
# Agent Operating Rules

1. Read `CONTEXT.md` first.
2. Validate active milestone in `MILESTONES.md`.
3. Check whether a decision already exists in `DECISIONS.md` before changing architecture.
4. Keep changes local to current scope.
5. Update the repo operating files after implementation.
6. Reference the relevant Linear issue in commits and status notes.
7. Do not assume external sync succeeded unless verified.
```
