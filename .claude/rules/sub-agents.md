> **Regel-Zweck:** TODO: LLM needs to write a proper description for sub-agents.

# 🛑 CRITICAL RULESET: SUB-AGENT ORCHESTRATION

> **MANDATORY READ:** This file defines non-negotiable protocols.
> **VIOLATION:** Ignoring this file leads to immediate failure.

## 1. ABSOLUTE PROHIBITIONS (every sub-agent prompt must include these)

- **TodoWrite is FORBIDDEN** — sub-agents must NOT use the TodoWrite tool
- **Opus model is FORBIDDEN** — only `sonnet` or `haiku`; Opus only on explicit user instruction
- **Scope violation is FORBIDDEN** — every prompt must explicitly name the allowed scope

## 2. REPORT-FIRST TRACKING

- **Single tracking instrument:** A markdown file in `reports/[phase-name].md`
- The report file must be **created before the first code step** (table with PENDING status)
- **Hard condition (NOT a suggestion):** "You are FORBIDDEN from starting step N+1 before marking step N as ✅ DONE in the report file."
- Report format:

```
| # | Step | Status |
|---|------|--------|
| 1 | Create file X | ✅ DONE |
| 2 | Edit file Y | ⏳ PENDING |
```

## 3. MODEL ROUTING

| Task Type | Model | When |
|---|---|---|
| Implementation (>50 lines) | `sonnet` | Writing code, creating files |
| Exploration / search | `haiku` | Grep, Glob, read-only |
| Architectural decisions | **Ask user** | Never decide alone |
| Opus | **FORBIDDEN** | Only on explicit user instruction |

## 4. MANDATORY PROMPT STRUCTURE

Every sub-agent prompt must contain:

1. **SCOPE** — Explicit list of files that may be touched
2. **GOAL** — Exact result (no soft terms like "adapt", "migrate", "clean up")
3. **CONSTRAINTS** — List all prohibitions (TodoWrite, Opus, scope violations)
4. **REPORT FILE** — Path to report file + instruction: "Update report after every step"
5. **STEPS** — Atomic step list: "Step 1: create X → update report → Step 2: edit Y → update report"

## 5. WHEN NOT TO SPAWN A SUB-AGENT

- Single curl tests / API calls → main agent directly
- Tool-rejections → main agent finds alternative approach (no sub-agent as workaround)
- Plan-mode exploration → `Explore` agent type (not `general-purpose`)
- Any task under ~50 lines of code → main agent directly

## 6. FAILURE PATTERN (learned from agent af4f17a, 2026-02-18)

- **Anti-pattern:** Sub-agent makes 13+ tool calls without updating the report → all checkboxes remain PENDING
- **Root cause:** Prompt phrased report-update as a suggestion, not a hard precondition
- **Fix:** Always write: "You MUST NOT begin step N+1 until step N is marked ✅ DONE in the report."