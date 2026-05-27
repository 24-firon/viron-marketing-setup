# CONTEXT.md — marketing-setup

## Identity
- **Repository name:** marketing-setup
- **Primary purpose:** Zentrales Marketing-Repository für B2B-AI-Automation-Angebote im DACH-Raum. Enthält Content-Workflows, Copy-Templates, Campaign-Assets, Automatisierungslogik für Marketing-Outputs sowie Schnittstellen zu n8n und LiteLLM.
- **Business domain:** B2B Marketing / AI Automation / DACH SME
- **Owner:** Solo Developer / Operator
- **Main deployment target:** Content wird über n8n-Workflows verteilt. Assets liegen lokal und in Supabase Storage. Kein öffentlich deploytes Web-Frontend in diesem Repo.

---

## Current status
- **Status summary:** Aufbau. Ordnerstruktur und Basis-Templates sind vorhanden. Noch keine vollständige n8n-Integration. Linear-Tickets für aktive Marketing-Arbeitspakete existieren.
- **Current phase:** Phase 1 — Struktur und Templates konsolidieren, bevor Automatisierung greift.
- **Active branch or release line:** main
- **Last major verified milestone:** Grundstruktur angelegt, erste Copy-Templates aus Notion-Freebies portiert.

---

## Active work
- **Active Linear issues:** Bitte vor Arbeitsbeginn in Linear unter Projekt "Marketing" nach offenen Issues mit Status "In Progress" suchen.
- **Current implementation goal:** Alle gesammelten Marketing-Ressourcen (Notion-Freebies) systematisch als wiederverwendbare Templates in `/templates` überführen.
- **Current blocker:** n8n-Anbindung noch nicht finalisiert. Automatische Sync-Flows zwischen Linear (Done) → Notion-Archiv fehlen noch.
- **Immediate next action:** Bestehende Notion-Freebies sichten, nach Kategorie sortieren und als Markdown-Templates in `/templates/copy/` ablegen.

---

## Architecture snapshot
- **Content storage:** Lokales Dateisystem + Supabase Storage (Assets wie Bilder, PDFs)
- **Automatisierungsschicht:** n8n (noch im Aufbau — Webhooks geplant, aber noch nicht aktiv)
- **LLM-Routing:** LiteLLM (Claude Sonnet für Copy-Generation, günstigere Modelle für Klassifikation)
- **Task-Tracking:** Linear (Projekt: Marketing)
- **Wissens-Referenz:** Notion (Freebies, Strategiedokumente, Swipe-Files)
- **IDE-Zugang:** Antigravity / ClaudeCode / Cursor

---

## Repo-Struktur (Zielzustand)
```
marketing-setup/
├── CONTEXT.md              ← diese Datei (Agent liest zuerst)
├── MILESTONES.md
├── DECISIONS.md
├── AGENT_OPERATING_RULES.md
├── templates/
│   ├── copy/               ← E-Mail-Templates, LinkedIn-Copy, Ad-Copy
│   ├── seo/                ← SEO-Brief-Templates, Keyword-Frameworks
│   ├── social/             ← Post-Templates nach Plattform
│   └── outreach/           ← Cold-Outreach-Sequenzen B2B DACH
├── campaigns/
│   └── [campaign-slug]/    ← je Kampagne ein Ordner
│       ├── brief.md
│       ├── copy/
│       └── assets/
├── workflows/
│   ├── n8n/                ← n8n-Workflow-Exports (.json)
│   └── prompts/            ← LLM-Prompts für Marketing-Automatisierung
├── research/
│   ├── icp/                ← Ideal Customer Profile Dokumente
│   ├── competitors/        ← Wettbewerbsanalysen
│   └── swipe/              ← portierte Notion-Freebies als Markdown
└── docs/
    ├── brand-voice.md
    └── icp-summary.md
```

---

## Constraints
- **Sprache:** Primär Deutsch für DACH-Inhalte, Englisch für technische Dokumentation.
- **Datenschutz:** Keine echten Kundendaten im Repo. Personenbezogene Daten nur in Supabase mit RLS.
- **LLM-Kosten:** Teure Modelle (Claude Opus) nur für strategische Copy. Günstigere Modelle für Batch-Klassifikation und Tagging.
- **Tone of Voice:** Professionell, direkt, kein Bullshit-Bingo. Zielgruppe sind technisch versierte Entscheider in kleinen und mittleren Unternehmen.

---

## Source of supporting context
- **Notion — Freebies & Swipe Files:** https://notion.so (Link aus Notion-Workspace einfügen)
- **Linear — Marketing-Projekt:** https://linear.app (Team/Projekt-Link einfügen)
- **Brand Voice Guideline:** `./docs/brand-voice.md`
- **ICP Summary:** `./docs/icp-summary.md`

---

## Known risks
- **Notion-Freebies sind unstrukturiert:** Qualität und Relevanz variieren stark. Templates ohne Quellenprüfung nicht direkt verwenden.
- **n8n noch nicht aktiv:** Solange keine automatisierten Flows laufen, muss Archivierung manuell via Linear → Notion erfolgen.
- **LLM-Output-Qualität:** Generierte Marketing-Copy muss immer reviewed werden, bevor sie an Kunden geht.

---

## Last completed items
1. (Datum) — Initiales Repo angelegt, Basisstruktur erstellt.
2. (Datum) — Erste Notion-Freebies gesichtet und grob kategorisiert.
3. (Datum) — CONTEXT.md, MILESTONES.md, DECISIONS.md angelegt.

---

## Update rules for agents
- Diese Datei VOR jeder Arbeitssitzung lesen.
- Nur Fakten aktualisieren, die sich tatsächlich geändert haben.
- Linear Issue IDs in Commit-Messages und in "Active work" referenzieren.
- Keine spekulativen Zukunftsarchitekturen als bestehend eintragen.
- Nach jedem abgeschlossenen Task: "Last completed items" um einen Eintrag ergänzen (ältesten entfernen, max. 3 Einträge).
