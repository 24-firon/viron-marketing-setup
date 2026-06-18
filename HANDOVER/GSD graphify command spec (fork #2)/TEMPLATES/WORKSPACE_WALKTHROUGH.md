# WORKSPACE WALKTHROUGH (Kompakt)

> Topology + Reading List für den nächsten Agent. **DENN** ohne Kontext über die Repo-Struktur verliert er 30 Minuten beim Suchen.

## 1. TECHNICAL TOPOLOGY

Kurze Verzeichnis-Landkarte mit Erklärung was wo liegt:

```
[REPO-ROOT]/
├── .agents/skills/         — 14 aktive Skills (v2.0.1) + 3 neue DACH-Skills (P0)
│   ├── dsgvo-lead-capture/  — NEU (2026-06-17)
│   ├── linkedin-dach-b2b/   — NEU (2026-06-17)
│   ├── local-seo-gbp/       — NEU (2026-06-17)
│   ├── product-marketing/   — Foundation
│   ├── social/              — Plattform-übergreifend
│   ├── copywriting/         — Page-Copy
│   ├── cro/                 — Conversion-Optimierung
│   └── [10 weitere]
├── .agent/skills/          — Spiegel für OpenCode-Format
├── .claude/skills/          — Spiegel für Claude-Code-Format
├── .opencode/               — Konfiguration + Rules
│   ├── rules/               — 8+ Boot-Regeln
│   └── skills/session_handover_generator/  — SSOT für Handover-Generator
├── DOCS/                    — Permanent injizierte Doku
│   ├── brand-voice.md
│   ├── icp-summary.md
│   ├── skill-router.md
│   └── storage-router.md
├── STORAGE/                 — On-demand Payload-Wissen
│   ├── TEMPLATES/BUNDLE_KOMPAKT/  — 17 Handover-Templates
│   ├── CONTENT/             — Produzierte Inhalte
│   └── TOOLS/               — Tool-Entscheidungsmatrizen
├── DIRECTOR/                — Session-Steuerung
│   ├── PROMPTS/active/      — P00/P01/P02 (auto-injiziert)
│   └── SESSIONS/            — Handover-Dateien pro Session
├── DESK/                    — WIP-Zone
│   ├── HANDOVER/sessions/   — Alte Handover-Dateien (M2-Konvention)
│   ├── REPORTS/             — SubAgent-Reports
│   └── TASKS/               — Task-Envelopes + Implementation Plans
├── HANDOVER/                — NEU: Root-Pfad für Handover-Bundles
│   └── GSD graphify command spec (fork #2)/  — Skill-konforme Handover-Ablage
│       ├── TEMPLATES/       — 10 befüllte Templates
│       ├── PROMPTS/         — 6 unveränderte Prompts
│       └── ADDITIONAL/      — 2 unveränderte Zusatz-Dateien
├── IMPORT/                  — Externe Research-Berichte
├── .graphify/               — Lokaler Graph-Cache (nicht committed)
└── .planning/               — GSD-Planning (lokal, nicht committed)
```

**Modifiziere NIEMALS Dateien außerhalb deines explizit zugewiesenen Silos!**

## 2. READING LIST (Pflicht vor Code-Änderung)

Reihenfolge der Dateien die der Agent lesen MUSS:

1. **`AGENTS.md`** — Repo-Identität, Zonen, 3 Modi (Schnell/Normal/Ausführlich)
2. **`CONTEXT.md`** — Repo-Status, aktive Phase, Blocker
3. **`MILESTONES.md`** — Aktiver Meilenstein (M2 abgeschlossen 2026-06-17)
4. **`TASKS.md`** — Aktive Tasks (D-1..D-4 Done, M2b ausstehend)
5. **`DECISIONS.md`** — Warum ist was wie entschieden (ADRs)
6. **`DESK/REPORTS/dach-custom-skills.md`** — Spec für DACH-Skills
7. **`DESK/REPORTS/dach-p0-skills-build.md`** — Build-Report mit 7 Spec-TODOs
8. **`HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/HANDOVER.md`** — Skill-konforme Datenübergabe
9. **`HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/SESSION_HANDOVER.md`** — Forensischer Bericht dieser Session

## 3. CORE LOGIC (Wie Daten fließen)

- **Skill-Architektur:** Skills in `.agents/skills/<skill>/` mit `SKILL.md` + `evals/evals.json`. Gespiegelt nach `.agent/skills/` und `.claude/skills/`.
- **Provider-Routing:** Provider-agnostisch via n8n Config. Gemini/Vertex AI Default, OpenCode ZEN + Go als Alternativen, Anthropic VERBOTEN (ADR-005).
- **Spec-Quelle:** DACH-Skills in `DESK/REPORTS/dach-custom-skills.md` (kanonische Spec). Import-Dateien in `IMPORT/` sind Sekundärquellen.
- **Milestone-Tracking:** M1 ✅, M2 ✅ (2026-06-17), M3 🔲 (N8N, blockiert durch Hetzner-Deployment), M4 🔲 (DACH-Custom-Skills Phase 2), M5 🔲 (Erste Kundenkampagne).
- **Handover-Workflow:** Skill `session_handover_generator` (in `.opencode/skills/`) ist SSOT. 6 Schritte: kopieren, lesen, aussortieren, bearbeiten, ausführen, P00-Fragen.

## 4. NICHT ANFASSEN (TABU)

| Pfad/Bereich | Warum tabu |
|:---|:---|
| `.planning/` | GSD-Thread (deaktiviert), nicht committed |
| `.graphify/` | Lokaler Cache, nicht committed |
| `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` | Original-Templates, nur kopieren |
| `.opencode/rules/` (außer auf Anweisung) | Boot-Regeln, externe Abhängigkeit |
| `_ARCHIVE/` | Historisch, nicht mehr aktiv |
| `node_modules/` | Dependencies |
