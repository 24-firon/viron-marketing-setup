# P01 — Leseliste (Kompakt)

> **LESE-MODUS.** Lade alle Tier-1-Dateien physisch und mach dir pro Datei eine 3-5 Zeilen Notiz. **DENN** der nächste Schritt (P02) verlangt nachweisbares Verständnis.

## VOR DEM START

Bestätige Comprehension Gate 1:
> "Ich habe die P00-Antworten verinnerlicht. Ich beginne jetzt mit dem Lesen."

## TIER 1 — PFLECHT (3 Batches)

### BATCH 1: Das Herzstück
- [ ] `AGENTS.md` — Repo-Identität, Zonen, 3 Modi (Schnell/Normal/Ausführlich)
- [ ] `CONTEXT.md` — Repo-Status, aktive Phase, Blocker
- [ ] `MILESTONES.md` — Aktiver Meilenstein (M2 ✅ 2026-06-17, M3 🔲 blockiert durch Hetzner)
- [ ] `TASKS.md` — Aktive Tasks (D-1..D-4 ✅ Done)

**Notiz (5 Zeilen):** Was ist die Mission? Was blockiert? Was sind die 3 Kern-Constraints?

1. Mission: M2b starten (7 Spec-TODOs auflösen ODER bewusst lassen) oder M3 (N8N-Integration, blockiert durch Hetzner-Deployment)
2. Blocker: M3 wartet auf Hetzner-Deployment. 7 Spec-TODOs in Build-Report offen. Git-Cred-Persistenz nicht gefixt.
3. 3 Kern-Constraints: (a) Spec-Drift = TODO markieren, (b) Sub-Schritt-GO explizit anfordern, (c) Skill-Vorgaben exakt befolgen

### BATCH 2: Das Fundament
- [ ] `DECISIONS.md` — vergangene Architektur-Entscheidungen (ADRs)
- [ ] `CLAUDE.md` — VIRON AI OS Context & Guidelines
- [ ] `HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/HANDOVER.md` — Datenübergabe dieser Session
- [ ] `HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/SESSION_HANDOVER.md` — Forensischer Bericht

**Notiz (5 Zeilen):** Welche Fehler sind hier relevant? Welche Entscheidungen sind getroffen? Wo ist der Stand?

1. 3 Operator-Korrekturen in dieser Session: (a) Sub-Schritt-GO, (b) edit statt write, (c) Skill-Vorgaben exakt befolgen
2. Entscheidungen: Spec-Drift = TODO markieren, Trigger-Phrasen nur in YAML, Git-Push nur mit 24-firon
3. Stand: M2 abgeschlossen, 5 Commits auf origin/main, 7 Spec-TODOs offen, M3 wartet auf Hetzner

### BATCH 3: Das Material
- [ ] `HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/CURRENT_TASKLIST.md` — Silo-Struktur mit 28 Tasks
- [ ] `HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/IMPLEMENTATION_PLAN.md` — M1-M3 mit Status
- [ ] `HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/WORKSPACE_WALKTHROUGH.md` — Topology + Reading List
- [ ] `DESK/REPORTS/dach-p0-skills-build.md` — Build-Report mit 7 Spec-TODOs

**Notiz (5 Zeilen):** Was ist der IST-Zustand? Was ist das SOLL? Welche Dateien sind betroffen?

1. IST: 3 DACH-Skills in `.agents/skills/`, gespiegelt, committet, gepusht. 7 Spec-TODOs offen. M3 blockiert.
2. SOLL: 7 Spec-TODOs auflösen. M3 N8N-Integration starten. Git-Cred-Persistenz fixen.
3. Betroffene Dateien: `STORAGE/TOOLS/tool-decisions.md` (M2b), `HETZNER-Deployment-Skripte` (M3), `scripts/load-env.ps1` (Git-Cred-Fix)

## TIER 2 — BEI BEDARF

| Datei | Wann lesen |
|:---|:---|
| `DESK/REPORTS/dach-custom-skills.md` | Wenn an DACH-Skills weitergearbeitet wird (Spec-Quelle) |
| `DESK/REPORTS/n8n-mcp-integration.md` | Wenn M3 N8N-Integration startet |
| `DESK/REPORTS/tool-decisions.md` | Wenn Tool-Entscheidungen getroffen werden (M2b) |
| `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` | Wenn ein neuer Handover erstellt wird (Skill-Workflow) |
| `.opencode/skills/session_handover_generator/` | Wenn Session abgeschlossen wird |

## WAS DU NICHT LIEST (SKIP)

- `node_modules/`, `.next/`, `dist/`, `build/` — Build-Artefakte
- `.git/` — Git-Metadaten
- `_ARCHIVE/` — Historisch
- `DELIVERY/` — Bundles, nicht für internes Verständnis

## BESTÄTIGUNG

> "P01 gelesen. [X]/[X] Dateien. 3 Notizen erstellt. Bereit für P02."

⏸️ **STOPP** — Nächstes Modell: 🔴 STARK.
