# CONTEXT.md — VIRON Marketing-Setup

**Stand:** 2026-06-07 | **Version:** 2.1

---

## Identity
- **Repository name:** marketing-setup
- **Primary purpose:** Zentrales Marketing-Repository für VIRON — eine Ground-Zero Agency Infrastructure, die KI-Automatisierungslösungen für KMU im DACH-Raum baut. Enthält Agent-Skills, Content-Workflows, Copy-Templates, Campaign-Assets, Automatisierungslogik für Marketing-Outputs sowie Schnittstellen zu n8n und Linear.
- **Business domain:** B2B Marketing / AI Automation Agency / DACH SME
- **Owner:** Solo Developer / Operator (Inspektor)
- **Main deployment target:** Content wird über n8n-Workflows verteilt. Assets liegen lokal und in Hetzner-PostgreSQL/Supabase Storage. Kein öffentlich deploytes Web-Frontend in diesem Repo.

---

## Current status
- **Status summary:** Aufbauphase. Skills v2.0.1 installiert, 14 aktiv, 19 archiviert. `opencode.jsonc` konfiguriert (16 instructions). DOCS/- und STORAGE/-Struktur steht. Linear-Tickets für aktive Marketing-Arbeitspakete existieren.
- **Current phase:** Phase 1 (Foundation) abgeschlossen. Phase 2 (Task-Checklisten) in Arbeit — SubAgent-Reports laufen in DESK/REPORTS/.
- **Active branch or release line:** main
- **Last major verified milestone:** M1 Foundation Stand (DOCS/, STORAGE/, opencode.jsonc, Skills-Priorisierung)

---

## Active work
- **Active Linear issues:** Bitte vor Arbeitsbeginn in Linear unter Team "MKT" (Marketing) nach offenen Issues mit Status "In Progress" suchen.
- **Current implementation goal:** Welle 4 — Hustle Marketing & Growth. Guerrilla-Outbound-Kampagnen, AI-Act-Compliance-Lead-Magneten, provokante LinkedIn-Posts gegen "KI-Experten"-Agenturen.
- **Current blocker:** n8n-Integration noch nicht produktiv. SubAgents arbeiten in Sandbox. Keine automatischen Sync-Flows Linear ↔ Notion.
- **Immediate next action:** SubAgent-Reports aus DESK/REPORTS/ auswerten, Phase-2-Aufgaben priorisieren, Tool-Entscheidungen finalisieren.

---

## Architecture snapshot
- **Content storage:** Lokales Dateisystem + Supabase Storage (Assets wie Bilder, PDFs) + geplantes Hetzner Postgres
- **Automatisierungsschicht:** n8n (geplant — Webhooks, MCP-Server, erster Workflow in M3)
- **LLM-Routing:** Provider-agnostisch via n8n Config (NIEMALS Modelle hardcoden). Default: Gemini/Vertex AI ($300 Credit). Fallback: Claude Sonnet (Qualität), Claude Haiku (Speed).
- **Task-Tracking:** Linear — Source of Truth für alle Tasks (Teams: MKT, SAL, FUL, OPS, GROUND0)
- **Wissens-Referenz:** Notion — Read-Only für Agenten (VIRON OS Master Index, VIRON_CONTEXT_v1, VIRON_AGENT_BLUEPRINT, Foundation Blocks F1–F5)
- **Skills:** `.agents/skills/` (14 aktiv, referenziert via opencode.jsonc), Archiv in `ARCHIVE/skills/` (19 inaktiv)

---

## Repo-Struktur (Ist-Stand Mai 2026)

```
marketing-setup/
├── CONTEXT.md              ← Agent liest zuerst
├── MILESTONES.md           ← Meilenstein-Tracker
├── DECISIONS.md            ← ADR-Log (4 Einträge)
├── TASKS.md                ← Aktive Task-Liste
├── AGENTS.md               ← Agent-Setup-Dokumentation
├── CLAUDE.md               ← VIRON AI OS Context & Guidelines
├── opencode.jsonc          ← 16 instructions, .agents/skills Pfad
├── DIRECTOR/               ← Session-Steuerung & Prompt-System
│   ├── PROMPTS/
│   │   ├── active/         ← Aktuelle Session-Prompts (auto-injiziert)
│   │   │   ├── P00_BOOTSTRAP.md
│   │   │   ├── P01_SESSION_INIT.md
│   │   │   └── P02_HANDOFF.md
│   │   └── TEMPLATES/      ← 7 Prompt-Templates (P00-P03, Handover, etc.)
│   └── SESSIONS/
│       └── 2026-05-25/
│           └── HANDOVER.md ← Versioniertes Session-Handover
├── DOCS/                   ← Auto-injizierte Dokumentation
│   ├── brand-voice.md
│   ├── icp-summary.md
│   ├── skill-router.md
│   └── storage-router.md
├── STORAGE/                ← Payload-Wissen (on-demand)
│   ├── INDEX.md
│   ├── marketingskills-integration-bericht.md
│   ├── CONTENT/            ← Produzierte Inhalte (Mega-Guides, Pillars)
│   ├── TOOLS/              ← Tool-Entscheidungsmatrizen
│   └── archive/
│       └── skills/         ← 19 inaktive Skills
├── ARCHIVE/
│   └── skills/             ← Legende: 19 inaktive Skills
├── DESK/                   ← WIP-Zone
│   ├── HANDOVER/           ← Session-Handovers + Research
│   ├── REPORTS/            ← SubAgent-Reports (N8N-MCP, Tools, DACH)
│   └── TASKS/              ← Task-Envelopes + Implementation Plans
├── IMPORT/                 ← Externe Research & Architektur
│   ├── 00_Master_Executive_Summary.md
│   ├── 01_Marketing_Skill_Bundles.md  ─┐
│   ├── 02_Aktuelle_Marketing_Techniken │ 6 Perplexity
│   ├── 03_Agent_Skill_Orchestrierung   │ Research
│   ├── 04_N8N_Integration              │ Reports
│   ├── 05_DACH_Marketing_Spezifika     │
│   ├── 06_Tool_Kategorien              ─┘
│   ├── SEO 2026 für Personal Brands.md
│   ├── VIRON 2026 Go-To-Market Playbook.md
│   ├── marketing_setup_complete/
│   └── orchestration_architecture_package/
├── VIRON_Full_Package_v2/  ← Linear Setup Script
├── .agents/skills/         ← 14 aktive Skills (v2.0.1)
├── .opencode/rules/        ← 8 operative Regeln
└── .claude/skills/         ← 14 Skills (Claude Code Spiegel)
```

---

## Constraints
- **Sprache:** Primär Deutsch für DACH-Inhalte, Englisch für technische Dokumentation und Skill-Definitionen.
- **OpenAI:** ABSOLUT VERBOTEN. Kein OpenAI in irgendeiner Form.
- **Python:** Python 3.11 zwingend. KEINE 3.12-Features.
- **n8n:** Primärer Automatisierungsstandard. Kein Zapier.
- **LLM-Provider:** Provider-agnostische Prompts. Niemals Modellnamen hardcoden.
- **Datenschutz:** Keine echten Kundendaten im Repo. Personenbezogene Daten nur in PostgreSQL mit RLS.
- **Tone of Voice:** Direkt, professionell, kein Fluff. Zielgruppe: pragmatische Geschäftsführer (35–55) im DACH-Raum.
- **Linear:** Source of Truth für alle Tasks. Alle Agenten updaten Linear.
- **Notion:** Read-Only für Agenten. Nur Operator schreibt Notion.

---

## Source of supporting context
- **CLAUDE.md:** `./CLAUDE.md` — Primärreferenz für Agenten (ARCHITEKTUR, REGELN, KONTEXT-QUELLEN)
- **AGENTS.md:** `./AGENTS.md` — Build/Lint/Test-Befehle, Codestil
- **Linear — MKT Team:** https://linear.app (Team/Projekt-Link einfügen)
- **Notion:** VIRON OS Master Index, VIRON_CONTEXT_v1, Foundation Blocks F1–F5
- **Brand Voice:** `./DOCS/brand-voice.md`
- **ICP Summary:** `./DOCS/icp-summary.md`
- **Skill Router:** `./DOCS/skill-router.md`
- **Storage Router:** `./DOCS/storage-router.md`
- **Marketing Skills Integration:** `./STORAGE/marketingskills-integration-bericht.md` (44 KB)

---

## Known risks
- **n8n noch nicht produktiv:** Solange keine automatisierten Flows laufen, muss Archivierung und Status-Sync manuell erfolgen.
- **LLM-Output-Qualität:** Generierte Marketing-Copy muss immer reviewed werden, bevor sie an Kunden geht.
- **Skills-Drift:** 19 Skills in ARCHIVE/ — Änderungen im Upstream-Repo (coreyhaines31/marketingskills) müssen manuell nachgezogen werden.
- **Token-Budget:** Bei Content-Batching strikt auf 5–8 Assets pro Batch begrenzen. 50+ Assets auf einmal verbrauchen zu viele Tokens.

---

## Last completed items
0. 2026-06-17 — M2 abgeschlossen: 3 DACH-P0-Skills gebaut (`dsgvo-lead-capture`, `linkedin-dach-b2b`, `local-seo-gbp`) + Router-Update in DOCS/. 7 Spec-TODOs dokumentiert in `DESK/REPORTS/dach-p0-skills-build.md`. Commits 666a6a3 + 80391bb auf main, gepusht.
1. 2026-06-07 — AGENTS.md als kanonische Root-Readme restrukturiert (v3.0). MCP-Server Linear+Notion konfiguriert (ADR-006). Provider-Stack finalisiert (ADR-005). 4 No-Touch-Lessons angelegt (DESK/HANDOVER/lessons/).
2. 2026-05-25 — Phase 2 Reports erstellt: 3 SubAgent-Reports (N8N-MCP, Tool-Decisions, DACH-Skills) + 3 Steuerdateien (CONTEXT/MILESTONES/DECISIONS).

---

## Update rules for agents
- Diese Datei VOR jeder Arbeitssitzung lesen (zusammen mit CLAUDE.md).
- Nur Fakten aktualisieren, die sich tatsächlich geändert haben.
- Linear Issue IDs in Commit-Messages und in "Active work" referenzieren.
- Keine spekulativen Zukunftsarchitekturen als bestehend eintragen.
- Nach jedem abgeschlossenen Task: "Last completed items" um einen Eintrag ergänzen (ältesten entfernen, max. 3 Einträge).
- Phasenwechsel in MILESTONES.md synchron halten.
