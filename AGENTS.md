# AGENTS.md — VIRON Marketing-Setup

**Stand:** 2026-06-07 | **Version:** 3.0

> **Zweck:** Diese Datei ist die kanonische Root-Readme für das Repo. Sie orchestriert alle Session-Prompts (P00 → P01 → P02), Steuerdateien, SubAgent-Workflows und Provider-Konventionen. Agents und Operatoren starten hier.

---

## 1. Was ist VIRON Marketing-Setup

VIRON ist eine AI-Automatisierungsagentur (Ground-Zero Agency Infrastructure) für KMU im DACH-Raum. Kernleistungen: Custom n8n-Workflows, KI-Agenten, CRM-Integrationen, Content- und Marketing-Automatisierung.

- **ICP:** 5–50 MA, DACH-Raum, Branchen lokaler Einzelhandel & Premium-Dienstleister, Budget 5–15 k EUR pro Projekt
- **Tool-Stack:** n8n (Automation), Gemini/Vertex AI (LLM-Default), PostgreSQL 16 (DB), Linear (Tasks, Source-of-Truth), Notion (Wissen, read-only für Agenten), Metricool (Publishing)
- **Tone:** Direkt, deutsch, kein Buzzword-Bullshit. Vollständige Brand-Voice: [DOCS/brand-voice.md](./DOCS/brand-voice.md)
- **ICP-Detail:** [DOCS/icp-summary.md](./DOCS/icp-summary.md)

---

## 2. Die 3 Modi (Schnell / Normal / Ausführlich)

Der Operator wählt pro Session einen Modus. Folge EXAKT dem passenden Modus. **Bei Unsicherheit: frag den Operator.**

| Modus | Wann | Dateien (Beispiel) |
|:------|:-----|:-------------------|
| 🔵 **Schnell** | Session-Wechsel, nur Daten + kurzer Plan | P00 → Implementation Plan → HANDOVER |
| 🟡 **Normal** | Standard-Session mit Tier-1-Leseliste | P00 → P01-Leseliste → Implementation Plan → HANDOVER |
| 🟢 **Ausführlich** | Forensic / Sub-Agents / Planungs-Session | Modus 2 + Operator-Workflow, Orchestrator-Workflow, Konservierungs-Manifest, Comprehension-Gate |

**Vollständige Modi-Definition (30 Dateien, 17 Ordner):** [STORAGE/TEMPLATES/HANDOVER_BUNDLE/README.md](./STORAGE/TEMPLATES/HANDOVER_BUNDLE/README.md)

---

## 3. Root-Level-Steuerdateien (kanonisch)

| Datei | Zweck | Liest wann? |
|:------|:------|:------------|
| **AGENTS.md** (diese) | Repo-Orchestrierung | IMMER zuerst |
| **CONTEXT.md** | Repo-Status, Phase, Blocker | Session-Start |
| **MILESTONES.md** | M1–M5 Status, Erfolgskriterien | Nach AGENTS.md |
| **TASKS.md** | Aktive Tasks, Welle 4 | Nach MILESTONES |
| **DECISIONS.md** | ADRs, Architektur-Wahrheit | Bei "warum"-Fragen |
| **CLAUDE.md** | VIRON AI OS Context, Tool-Stack | Bei Tool-Fragen |
| **DOCS/brand-voice.md** | Tone of Voice, Beispiel-Hooks | Bei Copy-Tasks |
| **DOCS/icp-summary.md** | ICP, Pain Points, Anti-ICP | Bei Strategie-Tasks |
| **DOCS/skill-router.md** | Welcher Skill wofür | Bei Skill-Auswahl |
| **DOCS/storage-router.md** | Wann STORAGE/ laden | Bei Wissens-Loader |
| **DOCS/SKILL_INDEX.md** | Aktive Skills, Scan-Depth | Bei Skill-Erstellung |

**Lese-Reihenfolge Session-Start:** AGENTS → CONTEXT → MILESTONES → TASKS → DECISIONS → DOCS/ (nur was gebraucht wird).

---

## 4. Session-Lebenszyklus (P00 → P01 → P02)

### 4.1 Kanonische Pfade

| Stufe | Datei | Inhalt |
|:------|:------|:-------|
| **P00** | `DIRECTOR/PROMPTS/active/P00_BOOTSTRAP.md` | Kontrollfragen, I/O-Lock, READ-ONLY |
| **P01** | `DIRECTOR/PROMPTS/active/P01_SESSION_INIT.md` | SSoT-Leseliste, Prioritätskette, Stops |
| **P02** | `DIRECTOR/PROMPTS/active/P02_HANDOFF.md` | Session-Abschluss, Übergabe |
| **P03** | `DIRECTOR/PROMPTS/TEMPLATES/P03_RESERVED.md` | Spezial-Sessions (Security, Research, Incident) |

### 4.2 Workflow

```
1. P00 (READ-ONLY) → Kontrollfragen beantworten → P00 bestanden?
        ↓ (Operator GO)
2. P01 (EXECUTION) → SSoT-Leseliste laden → Prioritätskette abarbeiten
        ↓ (nach jedem P0.x: STOPP, Report, GO warten)
3. [Arbeit M1–M5]
        ↓
4. P02 → Session-Handover befüllen → Commit
        ↓
5. P03 (nur bei Spezial-Sessions)
```

**Regel:** P01 NIEMALS vor P00. Nach jedem Meilenstein STOPP, Bericht, GO warten.

---

## 5. SubAgent-Workflow (4-Pfeiler-Briefing)

**Wann SubAgent spawnen:** Tasks > 50 LoC, multi-step, isolierbar. Bei < 50 LoC: direkt im Haupt-Chat.

**4-Pfeiler-Prompt:**

1. **SCOPE** — Exakte Datei-Liste (was darf Agent anfassen, was nicht)
2. **GOAL** — Klares Ergebnis (kein "adapt", "migrate", "clean up" — exakt was rauskommen soll)
3. **CONSTRAINTS** — Verbote: TodoWrite FORBIDDEN, Opus FORBIDDEN, scope-violation FORBIDDEN
4. **REPORT** — Pfad zur Report-Datei (z.B. `DESK/REPORTS/[task-id].md`) + Regel: "MUST NOT begin step N+1 before marking step N as DONE"

**Report-Format:**

```
| # | Step | Status |
|---|------|--------|
| 1 | Create file X | DONE |
| 2 | Edit file Y | PENDING |
```

**Vollständige Regel:** [.opencode/rules/sub-agents.md](./.opencode/rules/sub-agents.md)

---

## 6. Provider-Stack (KEIN Anthropic ohne Approval)

| Provider | Use Case | Tag |
|:---------|:---------|:----|
| **OpenCode ZEN** | Copy-Writing, Kampagnen, Strategie, komplexe Tasks | Standard |
| **OpenCode Go** | Research, Evals, Katalogisierung, Bulk-Reads | Light |
| **NVIDIA NIM** | Fallback wenn Go/ZEN nicht verfügbar | Fallback |

**Verboten ohne explizite Operator-Freigabe:**

- Anthropic (Opus, Haiku, Sonnet) — Provider-Stack verbietet (DECISIONS.md ADR-005)
- OpenAI — absolut verboten (CLAUDE.md §2)
- Proprietäre Modellnamen hardcoden — Prompts müssen provider-agnostisch sein

**Modell-Routing-Pflicht:** Bei Modell-Wechsel immer HARD STOP + GO vom Operator.

---

## 7. Verboten

| Verboten | Quelle | Wann erlaubt |
|:---------|:-------|:-------------|
| OpenAI | CLAUDE.md §2 | Niemals |
| Zapier | CLAUDE.md §2 | Nie (n8n ersetzt) |
| Anthropic | DECISIONS.md ADR-005 | Nur mit Operator-GO |
| Python 3.12 Features | CLAUDE.md §2 | Immer Python 3.11 |
| File-Löschung ohne ARCHIVE | Konservierungs-Manifest | Immer archivieren |
| Notion schreiben (Agent) | CLAUDE.md §2 | Nur Operator schreibt |
| Linear ohne SoT-Pflege | CLAUDE.md §2 | Immer updaten |
| Provider-Namen hardcoden | DECISIONS.md | Provider-agnostisch prompten |
| Tasks ohne Plan | Marketing-Rules | Erst 3–7 Steps, dann GO, dann execute |

---

## 8. Contributing & Commits

### 8.1 Commit-Format

```
<type>(<scope>): <subject> [LINEAR-XXX]

<body>
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`
**Scope:** Skill-Name, Datei-Pfad oder Domain (mkt, sal, ful, ops, ground0)
**Subject:** Imperativ, max 50 Zeichen, kein Punkt am Ende

### 8.2 Linear-Referenz

Jeder Commit mit Task-Bezug MUSS `[LINEAR-XXX]` (z.B. `[MKT-35]`) am Subject-Ende haben.

### 8.3 Branching

- `main` — produktiv, nur via PR
- `feat/<scope>-<short-desc>` — Feature-Branches
- `fix/<scope>-<short-desc>` — Fix-Branches
- `docs/<scope>-<short-desc>` — Doku-Branches

### 8.4 Was nicht committed wird

- Secrets, API-Keys, .env-Dateien
- Base64-Bilder in Airtable
- WIP-Content aus `STORAGE/CONTENT/_wip/` (nur finaler Content in `STORAGE/CONTENT/`)

---

## 9. Build / Lint / Test (VIRON Linear Setup)

### 9.0 OpenCode TUI starten (MCP-Server: Linear + Notion)

```bash
# Empfohlen: Startscript laedt ENV aus .env.local, dann TUI
pwsh -NoProfile -File scripts/start-opencode.ps1

# Oder manuell in aktueller Session:
. .\scripts\load-env.ps1
opencode
```

ENV-Variablen aus `.env.local` werden in die Process-Scope geladen, damit MCP-Server sie via `{env:VAR}` in `opencode.jsonc` aufloesen koennen.

MCP-Status pruefen: `opencode mcp list` (erwartet: `notionApi` + `linear` connected)

### 9.1 Python-Ausführung

```bash
# Hauptskript ausführen (erfordert LINEAR_API_KEY)
python VIRON_Full_Package_v2/viron_linear_setup.py

# Einzelne Funktion
python -c "
import sys
sys.path.insert(0, 'VIRON_Full_Package_v2')
from viron_linear_setup import get_organization_id
get_organization_id()
"
```

### 9.2 Linting (falls installiert)

```bash
black VIRON_Full_Package_v2/
flake8 VIRON_Full_Package_v2/
isort VIRON_Full_Package_v2/
```

### 9.3 Testen

```bash
pytest tests/
pytest tests/test_file.py::test_function
```

### 9.4 Codestil

- 4 Leerzeichen Einrückung (keine Tabs)
- 100 Zeichen max Zeilenlänge
- 2 Leerzeilen zwischen Top-Level, 1 zwischen Methoden
- Keine trailing whitespaces
- Imports: stdlib → third-party → lokal, alphabetisch
- Konstanten: UPPER_SNAKE_CASE
- Funktionen/Variablen: snake_case
- Klassen: PascalCase
- `try/except` mit spezifischen Exceptions, `r.raise_for_status()` bei HTTP

### 9.5 Wichtige ENV-Variablen

| Variable | Beschreibung |
|:---------|:-------------|
| `LINEAR_API_KEY` | Linear API Token (erforderlich) |
| `VIRON-OpenCode-ReadOnly` | Notion Token (read-only) |
| `OPENROUTER_API_KEY` | LLM-Routing |
| `NVIDIA_NIM_API_KEY` | NVIDIA NIM Fallback |
| `OPENCODE_GO` | OpenCode Go Provider |

### 9.6 Wichtige Funktionen (Viron Linear Setup Script)

| Funktion | Beschreibung |
|:---------|:-------------|
| `gql(query, variables)` | Führt GraphQL-Request aus |
| `get_organization_id()` | Holt Workspace-ID |
| `create_teams()` | Erstellt Teams |
| `create_labels()` | Erstellt Labels |
| `create_issues()` | Erstellt Issues |

### 9.7 Debugging

- API-Key prüfen: `echo %LINEAR_API_KEY%` (Windows)
- Response debuggen: `print(r.text)` nach Request
- GraphQL Playground: https://api.linear.app/graphql
- Linear Rate Limits: bei Fehlern Pausen einbauen

---

## 10. Versions-Hinweis

- **Version:** 3.0 (2026-06-07)
- **Vorherige:** 2.0 (VIRON Linear Setup only, 2026-03-12)
- **Änderungen v3.0:**
  - AGENTS.md ist jetzt kanonische Root-Readme (vorher: nur Linear-Setup-Doku)
  - P00-P02-Kanones definiert: `DIRECTOR/PROMPTS/active/`
  - Provider-Stack: OpenCode Go / OpenCode ZEN / NVIDIA NIM (KEIN Anthropic ohne Approval)
  - P00-P03 Workflow + 3-Modi-System (Schnell/Normal/Ausführlich) zentral
  - Build/Lint/Test (vormals §1-§9) jetzt §9 als Sektion
- **Quellen-Integration:** HANDOVER/README.md (3-Modi), DECISIONS.md (Provider), STORAGE/TEMPLATES/HANDOVER_BUNDLE/ (Master-Bundle)
- **Compacted from:** HANDOVER/README.md, .opencode/rules/sub-agents.md, CLAUDE.md, DECISIONS.md ADR-005+006
