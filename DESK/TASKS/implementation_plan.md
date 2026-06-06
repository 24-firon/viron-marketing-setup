# IMPLEMENTATION PLAN — Phase 2 Rest + Phase 3

> **Zweck:** Linearer Bauplan für die nächsten Schritte. Phase 2 Rest (P0-Skills) sofort umsetzbar. Phase 3 (N8N) wartet auf Deployment.

---

## MEILENSTEIN 2a: P0-DACH-Skills bauen

**Ziel:** 3 DACH-spezifische Marketing-Skills in `.agents/skills/` installiert. Jeder Skill hat SKILL.md, evals/, und ist in `DOCS/skill-router.md` eingetragen.

### 2.1 Skill 1: `dsgvo-lead-capture`

- **Unterpunkt:** SKILL.md erstellen nach Spezifikation aus `DESK/REPORTS/dach-custom-skills.md` Abschnitt 1
  - `write .agents/skills/dsgvo-lead-capture/SKILL.md`
- **Unterpunkt:** evals/ erstellen (6 Testfälle)
  - `write .agents/skills/dsgvo-lead-capture/evals/evals.json`
- **Unterpunkt:** Spiegelung in .agent/ und .claude/
  - `copy .agents/skills/dsgvo-lead-capture → .agent/skills/ und .claude/skills/`

### 2.2 Skill 2: `linkedin-dach-b2b`

- **Unterpunkt:** SKILL.md erstellen nach Spezifikation aus `DESK/REPORTS/dach-custom-skills.md` Abschnitt 2
  - `write .agents/skills/linkedin-dach-b2b/SKILL.md`
- **Unterpunkt:** evals/ erstellen (6 Testfälle)
  - `write .agents/skills/linkedin-dach-b2b/evals/evals.json`
- **Unterpunkt:** Spiegelung in .agent/ und .claude/
  - `copy .agents/skills/linkedin-dach-b2b → .agent/skills/ und .claude/skills/`

### 2.3 Skill 3: `local-seo-gbp`

- **Unterpunkt:** SKILL.md erstellen nach Spezifikation aus `DESK/REPORTS/dach-custom-skills.md` Abschnitt 3
  - `write .agents/skills/local-seo-gbp/SKILL.md`
- **Unterpunkt:** evals/ erstellen (6 Testfälle)
  - `write .agents/skills/local-seo-gbp/evals/evals.json`
- **Unterpunkt:** Spiegelung in .agent/ und .claude/
  - `copy .agents/skills/local-seo-gbp → .agent/skills/ und .claude/skills/`

### 2.4 Skill-Router aktualisieren

- **Unterpunkt:** `DOCS/skill-router.md` um die 3 neuen Skills erweitern
  - `edit DOCS/skill-router.md` — Trigger-Phrasen und Kategorie eintragen

**⏸️ STOPP — Berichte Ergebnis, warte auf GO für M2b.**

---

## MEILENSTEIN 2b: Reports verarbeiten & Tasks finalisieren

**Ziel:** Alle offenen Tasks aus Phase 2 in TASKS.md eingetragen. Tool-Entscheidungen nach STORAGE/TOOLS/ kopiert. MILESTONES.md M2-Kriterien abgehakt.

### 2.5 Tool-Entscheidungen persistent machen

- **Unterpunkt:** `DESK/REPORTS/tool-decisions.md` nach `STORAGE/TOOLS/tool-decisions.md` kopieren
  - `copy DESK/REPORTS/tool-decisions.md → STORAGE/TOOLS/tool-decisions.md`

### 2.6 TASKS.md aktualisieren

- **Unterpunkt:** Phase 2 Tasks eintragen (P0-Skills, N8N-MCP, Cal.com, Exa, Buffer/Metricool)
  - `edit TASKS.md`

### 2.7 MILESTONES.md aktualisieren

- **Unterpunkt:** M2-Kriterien abhaken (soweit erfüllt)
  - `edit MILESTONES.md`

### 2.8 CONTEXT.md aktualisieren

- **Unterpunkt:** Last completed items erweitern
  - `edit CONTEXT.md`

**⏸️ STOPP — Berichte Ergebnis, warte auf GO für M3.**

---

## MEILENSTEIN 3: N8N-Integration (vorbereitet, wartet auf Deployment)

**Ziel:** n8n auf Hetzner deployed. MCP-Server konfiguriert. Erster Test-Workflow läuft.

### 3.1 N8N Docker Deployment

- **Unterpunkt:** Hetzner VPS bereitstellen (CX22+)
- **Unterpunkt:** docker-compose.yml für n8n + PostgreSQL erstellen
- **Unterpunkt:** n8n deployen und per HTTPS erreichbar machen

### 3.2 MCP-Integration

- **Unterpunkt:** n8n-nodes-mcp Community Node installieren
- **Unterpunkt:** n8n API-Key generieren
- **Unterpunkt:** opencode.jsonc mit MCP-Server konfigurieren

### 3.3 Erster Test-Workflow

- **Unterpunkt:** "VIRON Test Ping" Workflow erstellen (MCP Server Trigger → "PONG")
- **Unterpunkt:** MCP-Verbindung validieren
- **Unterpunkt:** "VIRON LinkedIn Publisher" Workflow erstellen

**⏸️ STOPP — Berichte Ergebnis, warte auf GO.**

---

> **Alle Meilensteine definiert. Bereit für Execution.**
