# IMPLEMENTATION PLAN (Kompakt)

> **Linearer Plan** mit Meilensteinen. M1 → STOPP → M2 → STOPP → M3. **DENN** der Operator braucht Haltepunkte zur Freigabe.

## KOPFZEILE

```
TASK-ID: M2_DACH_P0_SKILLS
PHASE: M2 abgeschlossen (2026-06-17), M2b in Vorbereitung
RISIKO: 🟢 Low (alle Commits auf origin/main, Spec-TODOs dokumentiert)
GESCHÄTZTE DAUER: ~3h (diese Session)
```

## M1: DACH-P0 Skills Build

**Ziel:** 3 DACH-Custom-Skills in `.agents/skills/` + Router-Update in DOCS/skill-router.md

### Schritte
- [x] **Schritt 1.1** `[READ-ONLY]` — Spec aus DESK/REPORTS/dach-custom-skills.md gelesen
- [x] **Schritt 1.2** `[WRITE]` — Skill `dsgvo-lead-capture` (SKILL.md + evals/)
- [x] **Schritt 1.3** `[WRITE]` — Skill `linkedin-dach-b2b` (SKILL.md + evals/)
- [x] **Schritt 1.4** `[WRITE]` — Skill `local-seo-gbp` (SKILL.md + evals/)
- [x] **Schritt 1.5** `[WRITE]` — Spiegelung nach .agent/skills/ und .claude/skills/
- [x] **Schritt 1.6** `[EDIT]` — DOCS/skill-router.md um 3 neue Skills erweitern
- [x] **Schritt 1.7** `[EDIT]` — 13 chirurgische Korrekturen an den 3 Skills (Spec-Drift markiert)

### DoD (Definition of Done)
- Alle 3 Skills in `.agents/skills/` mit SKILL.md + evals/evals.json
- Spiegelung in `.agent/skills/` und `.claude/skills/`
- DOCS/skill-router.md enthält neue Sektion „DACH Custom Skills"
- 13 chirurgische Korrekturen angewendet (Spec-Drift markiert, nicht halluziniert)
- Build-Report unter `DESK/REPORTS/dach-p0-skills-build.md`

⏸️ **STOPP 1** — Operator hat nach Skill 1 gestoppt und chirurgische Edits verlangt. 13 Edits angewendet. ✅ ABGESCHLOSSEN

---

## M2: M2-Milestone abschließen

**Ziel:** M2 von „In Arbeit" auf „Abgeschlossen", Status in allen SSoT-Dateien synchron

### Schritte
- [x] **Schritt 2.1** `[EDIT]` — TASKS.md: D-1..D-4 Status auf Done
- [x] **Schritt 2.2** `[EDIT]` — MILESTONES.md: M2 als Abgeschlossen markieren, Blocker löschen
- [x] **Schritt 2.3** `[EDIT]` — CONTEXT.md: Last completed items rotieren
- [x] **Schritt 2.4** `[EDIT]` — P00_BOOTSTRAP.md: Fragen 9-13 aktualisieren

### DoD
- M2 in MILESTONES.md als „Abgeschlossen" markiert
- M2-Blocker (P0-Skills) gelöscht
- M2-Completion in CONTEXT.md Top-Eintrag
- Commits auf origin/main: 666a6a3, 80391bb, 39b9012, 4c1366a

⏸️ **STOPP 2** — ✅ ABGESCHLOSSEN

---

## M3: Git-Push-Integration + Session-Handover (skill-konform)

**Ziel:** Alle Commits auf origin/main, Working tree clean, skill-konforme Handover-Dateien

### Schritte
- [x] **Schritt 3.1** `[BASH]` — `gh auth switch -u 24-firon` (Viron-Agency hat keine Schreibrechte)
- [x] **Schritt 3.2** `[BASH]` — 4 Commits erstellen und pushen (666a6a3, 80391bb, 39b9012, 4c1366a)
- [x] **Schritt 3.3** `[BASH]` — Commit c4ba10d (Handover + P00) pushen
- [x] **Schritt 3.4** `[COPY]` — Templates aus STORAGE/TEMPLATES/BUNDLE_KOMPAKT/ nach HANDOVER/GSD graphify command spec (fork #2)/ kopieren
- [x] **Schritt 3.5** `[EDIT]` — HANDOVER.md, SESSION_HANDOVER.md, CURRENT_TASKLIST.md, WORKSPACE_WALKTHROUGH.md, SESSION_RITUAL.md, P00_BOOTSTRAP.md, COMPREHENSION_GATE.md, IMPLEMENTATION_PLAN.md befüllen
- [ ] **Schritt 3.6** `[BASH]` — Handover-Ordner committen und pushen

### DoD
- Alle 5 Commits auf origin/main
- HANDOVER-Ordner in `HANDOVER/GSD graphify command spec (fork #2)/` mit 10 befüllten Templates
- Working tree clean

⏸️ **STOPP 3** — ⏳ LÄUFT (Schritt 3.6 ausstehend)

---

## ABBRUCH-BEDINGUNGEN

Stopp SOFORT und Operator informieren wenn:
- Mehr als [X] Dateien betroffen sind als geplant
- Eine externe Abhängigkeit (API, Service) nicht erreichbar
- Konflikt mit existierender Architektur erkannt
- Mehr als [X] STOPPs ohne klares Ergebnis durchlaufen

## VERIFIKATIONS-PLAN

Pro Meilenstein definieren:
- [Was] wird verifiziert
- [Wie] (z.B. "ls zeigt Datei", "grep findet 0 Treffer", "pnpm test läuft clean")
- [Wer] ist verantwortlich (Agent vs. Operator)
