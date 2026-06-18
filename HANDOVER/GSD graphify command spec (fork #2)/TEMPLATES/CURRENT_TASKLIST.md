# CURRENT TASKLIST (Kompakt)

> Task-Tracker mit Silo-Struktur. [ ] = offen, [x] = erledigt, [!] = blockiert. **DENN** ohne klare Status-Übersicht weiß der nächste Agent nicht was noch zu tun ist.

## KOPFZEILE

```
SPRINT: 2026-W25
STAND: 2026-06-17
ZÄHLER: 7 offen / 10 erledigt / 1 blockiert
```

## SILO 01: DACH-P0 Skills Build

**DoD für Silo 01:** 3 DACH-Custom-Skills in `.agents/skills/` + Router-Update in DOCS/skill-router.md

- [x] **TS-01.10** `[READ-ONLY]` — Spec aus DESK/REPORTS/dach-custom-skills.md lesen
- [x] **TS-01.20** `[WRITE]` — Skill `dsgvo-lead-capture` (SKILL.md + evals/)
- [x] **TS-01.30** `[WRITE]` — Skill `linkedin-dach-b2b` (SKILL.md + evals/)
- [x] **TS-01.40** `[WRITE]` — Skill `local-seo-gbp` (SKILL.md + evals/)
- [x] **TS-01.50** `[WRITE]` — Spiegelung nach .agent/skills/ und .claude/skills/
- [x] **TS-01.60** `[EDIT]` — DOCS/skill-router.md um 3 neue Skills erweitern
- [x] **TS-01.70** `[EDIT]` — 13 chirurgische Korrekturen an den 3 Skills (Spec-Drift markiert)

## SILO 02: M2-Milestone abschließen

**DoD für Silo 02:** M2 von „In Arbeit" auf „Abgeschlossen", Status in allen SSoT-Dateien synchron

- [x] **TS-02.10** `[EDIT]` — TASKS.md: D-1..D-4 Status auf Done
- [x] **TS-02.20** `[EDIT]` — MILESTONES.md: M2 als Abgeschlossen markieren, Blocker löschen
- [x] **TS-02.30** `[EDIT]` — CONTEXT.md: Last completed items rotieren
- [x] **TS-02.40** `[EDIT]` — P00_BOOTSTRAP.md: Fragen 9-13 aktualisieren

## SILO 03: Git-Push-Integration

**DoD für Silo 03:** Alle Commits auf origin/main, Working tree clean

- [x] **TS-03.10** `[BASH]` — `gh auth switch -u 24-firon` (Viron-Agency hat keine Schreibrechte)
- [x] **TS-03.20** `[BASH]` — 4 Commits erstellen (666a6a3, 80391bb, 39b9012, 4c1366a)
- [x] **TS-03.30** `[BASH]` — `git push` für alle Commits

## SILO 04: Spec-TODOs auflösen

**DoD für Silo 04:** Jeder der 7 TODOs hat eine Entscheidung (Spec erweitert oder bewusste Lücke)

- [ ] **TS-04.10** `[DECISION]` — PostgreSQL-Schema-Namen für Lead-Capture
- [ ] **TS-04.20** `[DECISION]` — LinkedIn Posting-Cadence
- [ ] **TS-04.30** `[DECISION]` — LinkedIn Ads Mindestbudget
- [ ] **TS-04.40** `[DECISION]` — GBP Review-Antwort-Zeit
- [ ] **TS-04.50** `[DECISION]` — DACH-Verzeichnis-Priorisierung
- [ ] **TS-04.60** `[DECISION]` — Service-Package-Definitionen
- [ ] **TS-04.70** `[DECISION]` — Compliance-Summary 1-Page-Template

## SILO 05: M3 N8N-Integration

**DoD für Silo 05:** N8N auf Hetzner deployed, MCP-Server konfiguriert, erster Test-Workflow läuft

- [ ] **TS-05.10** `[DEPLOY]` — Hetzner VPS bereitstellen (CX22+)
- [ ] **TS-05.20** `[DEPLOY]` — docker-compose.yml für n8n + PostgreSQL
- [ ] **TS-05.30** `[CONFIG]` — n8n deployen, per HTTPS erreichbar
- [ ] **TS-05.40** `[CONFIG]` — n8n-nodes-mcp Community Node installieren
- [ ] **TS-05.50** `[CONFIG]` — n8n API-Key generieren
- [ ] **TS-05.60** `[TEST]` — "VIRON Test Ping" Workflow erstellen

## SILO 06: Repository-Hygiene

**DoD für Silo 06:** Working tree clean, keine Spec-Drift, keine Copy-Paste-Architektur

- [ ] **TS-06.10** `[DECISION]` — Git-Cred-Persistenz fixen (SSH-Key oder Load-Script)
- [ ] **TS-06.20** `[ARCHIV]` — Alte Handover-Datei in DESK/HANDOVER/sessions/ archivieren oder Root-Handover-Datei löschen
- [ ] **TS-06.30** `[REFACTOR]` — Copy-Paste-Architektur der 3 Skills aufbrechen

## BLOCKIERTE TASKS

- [!] **M3 N8N-Integration** — blockiert durch: Hetzner-Deployment steht aus, WORKAROUND: SubAgent-Prompts aus DESK/REPORTS/n8n-mcp-integration.md vorbereiten, ausführen sobald Deployment steht

## PRIORITÄTEN

- **P0 🔴 KRITISCH** — Sofort, blockiert alles andere
- **P1 🟡 HOCH** — Diese Session, wichtig
- **P2 🟢 NORMAL** — Nächste Session
- **P3 ⚪ NIEDRIG** — Irgendwann
