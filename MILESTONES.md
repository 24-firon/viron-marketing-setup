# MILESTONES.md — VIRON Marketing-Setup

**Stand:** 2026-05-25

---

## Meilenstein-Übersicht

| Meilenstein | Status | Ziel-Outcome | Blocker | Erfolgskriterium |
|---|---|---|---|---|
| M1: Foundation Stand | ✅ Abgeschlossen | DOCS/, STORAGE/, opencode.jsonc, Skills-Priorisierung | — | Alle 4 DOCS/-Dateien vorhanden, 14 Skills aktiv, 19 archiviert |
| M2: Task-Checklisten | ⏳ In Arbeit | SubAgent-Reports in DESK/REPORTS/, Tool-Entscheidungen, N8N-MCP-Vorbereitung | Tool-Entscheidungen offen | Reports ausgewertet, Tool-Matrix finalisiert, MCP-Server-Plan steht |
| M3: N8N-Integration | 🔲 Geplant | MCP-Server konfiguriert, erster Workflow läuft | M2 muss Reports liefern | Mindestens 1 funktionierender n8n-Workflow mit MCP-Anbindung |
| M4: DACH-Custom-Skills | 🔲 Geplant | VIRON-eigene Skills für DACH-Besonderheiten (DSGVO, AI Act, DACH-ICP) | M3 muss laufen | Min. 3 Custom-Skills in .agents/skills/ |
| M5: Erste Kundenkampagne | 🔲 Geplant | Eine vollständige Kampagne (Brief → Copy → Asset → Metricool) deployed | M4 muss abgeschlossen sein | Kampagne live, Ergebnisse in PostgreSQL dokumentiert |

---

## Aktiver Meilenstein: M2 — Task-Checklisten

### Ziel
SubAgent-Reports auswerten, Tool-Entscheidungen finalisieren, N8N-MCP-Vorbereitung abschließen. Agent kann nach M2-Abschluss strukturierte Task-Checklisten für jede Marketing-Disziplin abarbeiten.

### Scope
- SubAgent-Reports aus DESK/REPORTS/ auswerten und zusammenführen
- Tool-Vergleiche in STORAGE/TOOLS/ abschließen (Calendly vs SavvyCal, Buffer vs Metricool, etc.)
- N8N-MCP-Server-Architektur planen und dokumentieren
- Phase-2-Aufgaben priorisieren (Guerrilla Outbound, AI Act Compliance, Takedown-Kampagnen)

### Ausgeschlossen aus M2-Scope
- N8N-Workflow-Implementierung (das ist M3)
- Custom-Skill-Entwicklung (das ist M4)
- Live-Kampagnen-Deployment (das ist M5)

### Dependencies
- Zugriffsrechte auf Linear (MKT, SAL, GROUND0 Teams)
- Zugriff auf DESK/REPORTS/ Verzeichnis
- Notion-Referenz: VIRON_TOOL_STACK, VIRON_CONTEXT_v1

### Erfolgskriterien
- [x] SubAgent-Reports ausgewertet und in einem Summary zusammengeführt
- [x] Tool-Entscheidungsmatrix finalisiert (min. 3 Tool-Vergleiche in DESK/REPORTS/)
- [x] N8N-MCP-Architektur dokumentiert (Server-Typen, Endpoints, Auth-Flow)
- [x] Phase-2-Priorisierung abgeschlossen (Tasks in TASKS.md eingetragen)
- [x] Agent kann M3-Aufgaben ohne externe Rückfragen beginnen (Implementation Plan in DESK/TASKS/)

### Aktuelle Blocker
- P0-DACH-Skills müssen noch gebaut werden (Task-Envelope in DESK/TASKS/dach-p0-skills/)
- n8n-Deployment steht aus (M3 startet erst nach Deployment)

### Verknüpfte Linear Issues
- (Bitte aktuelle Issue-IDs aus Linear eintragen)

---

## Abgeschlossener Meilenstein: M1 — Foundation Stand

### Ziel
Ein vollständig strukturiertes Repo mit standardisierten Agent-Skills, Kontext-Dokumentation und operativen Regeln, das ein Agent ohne externe Orientierung lesen und ausführen kann.

### Scope
- DOCS/ angelegt mit brand-voice.md, icp-summary.md, skill-router.md, storage-router.md
- STORAGE/ angelegt mit INDEX.md, marketingskills-integration-bericht.md, CONTENT/, TOOLS/
- ARCHIVE/skills/ mit 19 inaktiven Skills befüllt
- DESK/ angelegt mit HANDOVER/, REPORTS/, TASKS/
- opencode.jsonc konfiguriert (15 instructions, .agents/skills Pfad)
- Skills v2.0.1 priorisiert: 14 aktiv (.agents/skills/), 19 archiviert (ARCHIVE/skills/), 7 aussortiert

### Ausgeschlossen aus M1-Scope
- N8n-Integration (M3)
- SubAgent-Ausführung (M2)
- Live-Kampagnen (M5)

### Erfolgskriterien
- [x] DOCS/ mit allen 4 Dateien vorhanden
- [x] STORAGE/ mit INDEX.md und Integrationsbericht vorhanden
- [x] ARCHIVE/skills/ mit 19 inaktiven Skills befüllt
- [x] opencode.jsonc mit 15 instructions (AGENTS.md, CLAUDE.md, 4 DOCS/ + TASKS.md + 7 Regeln)
- [x] .agents/skills/ mit 14 aktiven Skills (v2.0.1)
- [x] skills-lock.json mit 32 getrackten Skills

### Abgeschlossen am
2026-04-02 (Template-Bibliothek), 2026-05-22 (Skills-Integration)

### Verknüpfte Linear Issues
- MKT-1: Auto-Moderation Make Blueprint (referenziert in MKT-1_AutoModeration_Make_Blueprint.json)

---

## Zukünftiger Meilenstein: M3 — N8N-Integration

### Ziel
MCP-Server-Stack ist mit n8n verbunden. Mindestens ein Workflow läuft produktiv (z.B. Content-Pipeline: Airtable → n8n → Vertex AI → Airtable Review).

### Scope
- MCP-Server konfigurieren (PostgreSQL, Airtable, Linear, Notion)
- Erster n8n-Workflow deployen (Content-Generation oder Linear-Sync)
- Provider-Selection-Logic in n8n implementieren (VIRON_TOOL_STACK-basiert)
- Error-Handling und Logging einrichten

### Erfolgskriterien
- [ ] MCP-Server laufen und sind von n8n erreichbar
- [ ] Mindestens 1 Workflow läuft mit Test-Daten durch
- [ ] Logs landen in PostgreSQL (public.mkt_workflow_logs)
- [ ] Agent kann Workflow per n8n-Webhook triggern

---

## Zukünftiger Meilenstein: M4 — DACH-Custom-Skills

### Ziel
VIRON-eigene Marketing-Skills für DACH-spezifische Anforderungen: DSGVO-Compliance-Marketing, AI Act Lead-Magneten, DACH-ICP-Content-Templates, German Brand Voice Optimierung.

### Scope
- Research: DACH-spezifische Marketing-Anforderungen identifizieren
- Custom-Skills entwickeln (min. 3): DSGVO-Compliance, AI-Act-Marketing, DACH-Brand-Voice
- In .agents/skills/ integrieren (Provider-agnostisch, n8n-kompatibel)
- DOCS/skill-router.md um DACH-Custom-Skills erweitern

### Erfolgskriterien
- [ ] Min. 3 Custom-Skills in .agents/skills/ (mit SKILL.md und Ressourcen)
- [ ] Jeder Skill getestet (Prompt-Output reproduzierbar)
- [ ] DOCS/skill-router.md aktualisiert
- [ ] skills-lock.json um Custom-Skills erweitert
