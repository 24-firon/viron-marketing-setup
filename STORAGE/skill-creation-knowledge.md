# Skill Creation Knowledge – Viron Agency Stack

> **Source:** Context-Dispatcher-System `_EXPORT/cds_lite_erweiterung`, skills.sh research, skill-creator skill
> **Stand:** 2026-05-21
> **Purpose:** Definitive guide for agents creating or managing skills in `.opencode/skills/` and `.claude/skills/`

---

## 1. How to Find Skills (skills.sh)

All public agent skills are indexed at `https://www.skills.sh/`.

### Link Pattern

```
https://www.skills.sh/[owner]/[repo]/[skill-name]
```

Every entry in the skills.sh Leaderboard is a link. Read the page, extract owner/repo/skill-name from each entry, and construct the URL.

### Installation Command

```
npx skills add <owner/repo> --skill <skill-name>
```

Or full URL variant:

```
npx skills add https://github.com/<owner>/<repo> --skill <skill-name>
```

**The `--skill` flag is CRITICAL.** Without it, `npx skills add` installs ALL skills from the entire repo. With `--skill`, it installs only the one you want.

### Installation Example

```
npx skills add mattpocock/skills --skill write-a-skill
npx skills add affaan-m/everything-claude-code --skill hookify-rules
npx skills add figma/mcp-server-guide --skill create-design-system-rules
```

---

## 2. The Router Paradigm (Skills ≠ Archives)

A skill is **not a textbook or archive**. It is a **TOKEN-EFFICIENT ROUTER** that tells the agent: "When you do X, read file Y."

### Progressive Disclosure (3 Levels)

1. **Metadata** (name + description) — Always in context (~100 words). The agent sees this in `available_skills` and decides whether to open the skill.
2. **SKILL.md body** — Loaded when the skill triggers (<500 lines ideal).
3. **Bundled resources** — Loaded as needed (unlimited, scripts can execute without loading).

### The 3 Mistakes Agents Make

| Wrong | Right |
|:---|:---|
| Merge everything into SKILL.md | SKILL.md is a router, templates/examples stay separate |
| Read everything top to bottom | Follow the condition matrix, read only what's needed |
| Ignore examples | Treat examples as "Definition of Done" |
| Guess the result | Compare result with example |
| Say "I'm done" | Say "My result meets the example's criteria" |

---

## 3. Skill Structure

```
.opencode/skills/<skill-name>/
├── SKILL.md                    ← THE ROUTER (not the archive!)
├── examples/                   ← "Definition of Done" references
│   ├── EXAMPLE_A.md
│   └── EXAMPLE_B.md
├── templates/                  ← Templates to be filled
│   ├── 01_template.md
│   └── 02_template.md
├── scripts/                    ← Executable scripts (optional)
│   └── helper.py
└── references/                 ← Domain knowledge (optional)
    ├── domain-a.md
    └── domain-b.md
```

### What Each Folder Means

| Folder | Contains | Does NOT contain |
|:---|:---|:---|
| **SKILL.md** | YAML header, context block, condition matrix, sub-action prompts | Templates or examples |
| **examples/** | Complete, finished artifacts | Placeholder content |
| **templates/** | Empty or partially filled structures with the format (tables, sections) | Final data |
| **scripts/** | Bash/Python scripts referenced in workflows | Documentation |
| **references/** | Domain knowledge, process docs, research findings | Workflow instructions |

---

## 4. The 4 Pillars of a Valid Skill

Every skill MUST have:

| Pillar | Purpose | Implementation |
|:---|:---|:---|
| **1. Examples** | "Definition of Done" — prevents knowledge bias | `examples/` folder with complete reference artifacts (`Before`/`After` patterns) |
| **2. Templates** | Scaffolding (formatting) | `templates/` folder with exact Markdown/JSON structures to be filled |
| **3. Role Assignment** | Defines the agent's mindset | In the router: "You act here as Enterprise Forensics, not as a Coder" |
| **4. Hard Directives** | Prevents the agent from guessing | In the router: "Read file Z when you perform action A." |

**Iron rule:** If you create a skill and forget the `examples/` folder, you have completely failed.

---

## 5. YAML Header (Skills)

Skills have a MINIMAL header:

```yaml
---
name: archive-workflow
description: "Workflow for ARCHIVE imports. Trigger: creating MANIFEST.md, moving to quarantine, updating index. Contains ToC in first 23 lines — then conditional load via matrix."
---
```

| Field | Required | Purpose |
|-------|----------|---------|
| `name` | ✅ | Skill identifier (kebab-case) |
| `description` | ✅ | **ONLY auto-injected part.** The agent decides here whether to open the skill. Must include: what the skill does, when to trigger it, how many lines to read initially. |

**Forbidden:** Custom fields like `first_read` or `read_lines`. Every system handles YAML differently. The description field is the only hook.

### The description is the trigger mechanism

Claude Code/OpenCode shows the agent a list of `available_skills` with name + description. The agent decides based on the description whether to load the skill. Therefore: be specific about trigger contexts!

---

## 6. SKILL.md Body (The Router)

The SKILL.md body should contain:

1. **YAML Header** (see Section 5)
2. **Context Block** (first ~30 lines): What is this about? WHEN do I need it? The agent should decide after 50 lines whether to abort or continue.
3. **Router (Condition Matrix):** A table or list with hard conditions. NOT "You may read here" but **"WHEN condition X occurs, you MUST read file Y completely."**
4. **Sub-Action Prompts:** (Optional) Copy-paste commands for the user to invoke the skill.

### Token Efficiency

Through the router paradigm:

- **Phase 1:** Load SKILL.md (60 lines) + Example A (100 lines) + Template 1 (50 lines) = **210 lines**
- **Phase 3:** Load SKILL.md (60 lines) + Example B (90 lines) + Template 2 (70 lines) = **220 lines**

**Without** router paradigm (everything in SKILL.md): **800+ lines** — regardless of whether needed.

---

## 7. How Skills Differ from Rules

| Aspect | Rules | Skills |
|:---|:---|:---|
| **Location** | `.opencode/rules/` | `.opencode/skills/` or `.claude/skills/` |
| **Loading** | Via `opencode.jsonc` → `instructions` (always injected) | Via description matching in `available_skills` |
| **Purpose** | Permanent constraints, always active | Structured multi-step workflows, on demand |
| **Structure** | Single `.md` file with YAML header | SKILL.md + folders (examples, templates, references) |
| **Updates** | Manual edit of rule file | Via `npx skills` from GitHub (can overwrite custom patches!) |
| **Token cost** | Always loaded → must be compact | Only loaded when triggered → can be detailed |

---

## 8. The Problem with Patching Vendor Skills

Vendor skills (from `npx skills`) are updated regularly. If you patch them locally, your patches get LOST on the next update.

**The Solution — STORAGE separation:**

- Vendor skills stay unchanged (update-safe)
- Proprietary knowledge lives in `STORAGE/` or referenced via the skill's `references/` folder
- The skill routes to storage knowledge when needed

**Example:** The `skill-creator` skill stays as-is. The Viron-specific knowledge about rule formulation, prefixes, YAML standards, and opencode.jsonc lives in `storage/rule-creation-knowledge.md`. The archive workflow skill references this storage knowledge.

---

## 9. Available Public Skills (2026-05-21)

| Skill | Source | Installs | Purpose | Keep? |
|:---|:---|:---|:---|:---|
| **skill-creator** | anthropics/skills | 198K | Full pipeline: test cases, baseline, evaluation, iteration, description optimization | ✅ Yes |
| **write-a-skill** | mattpocock/skills | 120K | 4-step: requirements → draft → review → finalize. SKILL.md template | ✅ Yes |
| **hookify-rules** | affaan-m/everything-claude-code | 2.5K | Hookify rules: `.claude/hookify.{name}.local.md` files with YAML frontmatter + event/pattern monitoring | Study, then ❌ Delete |
| **create-design-system-rules** | figma/mcp-server-guide | 1.3K | Figma-specific: generates CLAUDE.md / AGENTS.md / .cursor/rules for design systems | ✅ Yes |

### Install Commands

```
npx skills add mattpocock/skills --skill write-a-skill
npx skills add affaan-m/everything-claude-code --skill hookify-rules
npx skills add figma/mcp-server-guide --skill create-design-system-rules
```

---

## 10. Checklist for New Skill Creation

- [ ] Skill has YAML header with name + description
- [ ] Description contains trigger keywords (when to load)
- [ ] Description hints at line count for first read ("Read first 23 lines")
- [ ] SKILL.md body is under 500 lines
- [ ] Router (condition matrix) is present
- [ ] `examples/` folder with at least one reference artifact
- [ ] `templates/` folder with empty structures
- [ ] Role assignment is defined
- [ ] Hard directives prevent guessing
- [ ] Format is defined in the skill body
