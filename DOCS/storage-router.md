# STORAGE Router — Payload-Index & Decision Matrix

STORAGE ist der Payload-Ordner. Hier liegt Wissen, das nicht an der Wand (in Docs) sein muss, aber jederzeit nachgeladen werden kann. Dieses Dokument listet alle verfügbaren Payloads und sagt dir, wann du sie laden solltest.

---

## Storage-Struktur

```
STORAGE/
├── INDEX.md                        ← Vollständige Payload-Liste (diese Datei)
├── marketingskills-integration-bericht.md  ← Forensische Analyse
├── TOOLS/
│   ├── tool-decisions.md           ← Buffer/Metricool, Cal.com, Exa Entscheidungsmatrizen
│   └── ppl-network-comparison.md   ← PPL-Netzwerk-Matrix (US + DACH-Lücken) [2026-06-19]
├── CONTENT/
│   ├── 4 Mega-Guides               ← Produzierte Inhalte (Backup)
│   ├── 4 Pillar-Bundles
│   ├── 3 Social-Batches
│   ├── Prompt-Templates
│   ├── Templates/
│   └── research/                   ← Themen-Research (pSEO, Architektur, GTM)
│       ├── pseo-tool-led-pattern.md  ← Pattern-Library pSEO [2026-06-19]
│       ├── architecture-paperclip-stack.md
│       ├── meta-bericht-paperclip-stack.md
│       └── VIRON Go-To-Market DACH 2026 – Legacy-Tech-Falle.md
├── TEMPLATES/
│   ├── BUNDLE_KOMPAKT/             ← 17 Handover-Templates (30-80 Z.)
│   └── HANDOVER_BUNDLE/            ← ältere Template-Version (Legacy)
└── archive/
    └── skills/                     ← 19 inaktive Skills (Payload für später)
        ├── seo-audit/
        ├── ai-seo/
        ├── programmatic-seo/
        ├── site-architecture/
        ├── schema/
        ├── ab-testing/
        ├── analytics/
        ├── ads/
        ├── ad-creative/
        ├── popups/
        ├── signup/
        ├── onboarding/
        ├── lead-magnets/
        ├── cold-email/
        ├── emails/
        ├── revops/
        ├── sales-enablement/
        ├── competitors/
        └── marketing-ideas/

WISSENSDATENBANK (extern, nicht im Repo):
C:\Ground-Zero\VIRON_DATABASE\
├── _system/                        ← Admin, Schema-CSVs, Sync-Log
├── repos/                          ← Content pro Schema (Notion-Mirror)
│   ├── marketing_setup/            ← Marketing-Skills, ICP
│   ├── knowledge_base/             ← Foundation Blocks F1-F5
│   ├── client_acme/                ← Kundenprojekte
│   └── agent_sandbox/              ← KI-Agenten-Experimente
└── _search-index/                  ← DuckDB-Indizes (optional)
```

---

## Decision Matrix: Wann welchen Payload laden?

| Wenn User sagt... | Payload laden | Warum |
|---|---|---|
| "Was war nochmal mit den Skills?" | `STORAGE/marketingskills-integration-bericht.md` | Vollständige Analyse was übernommen wurde und warum |
| "Ich brauche Skill X" (inaktiv) | `STORAGE/archive/skills/X/SKILL.md` | Skill liegt im Archiv, aktivieren wenn gebraucht |
| "Was ist mit SEO/Analytics/SEO?" | `STORAGE/archive/skills/<skill>/SKILL.md` | Inaktiver Skill, Kontext aus Archiv holen |
| "Vergleich Calendly vs SavvyCal" | `STORAGE/TOOLS/tool-decisions.md` | Tool-Evaluation |
| "Buffer vs Metricool?" | `STORAGE/TOOLS/tool-decisions.md` | Tool-Evaluation |
| "Welches PPL-Netzwerk für [Nische]?" | `STORAGE/TOOLS/ppl-network-comparison.md` | Netzwerk-Matrix (US + DACH-Lücken) |
| "Wer sind unsere Konkurrenten?" | `DESK/HANDOVER/Marketing-research.md` | (liegt nicht in Storage, sondern in DESK/HANDOVER/) |
| "Was haben wir schon produziert?" | `STORAGE/CONTENT/INVENTAR.md` | (liegt in STORAGE/CONTENT/) |
| "Wie bauen wir pSEO?" | `STORAGE/CONTENT/research/pseo-tool-led-pattern.md` | Pattern-Library (6 Patterns + Tech-Stack) |
| "Was sagt Perplexity-Recherche X im Original?" | `ARCHIVE/research/[slug]-raw.md` | Rohe 715-Zeilen-Recherche, on-demand |
| "Wo liegt die Knowledge-Base?" | `C:\Ground-Zero\VIRON_DATABASE\` | Notion-Spiegel, Foundation Blocks F1-F5 |
| "Gib mir F1 Brand Identity" | `C:\Ground-Zero\VIRON_DATABASE\repos\knowledge_base\...\page.md` | Foundation Block als Markdown |
| "Notion-Inventar" | `DESK/REPORTS/notion-inventory-*.md` | Vollständige Notion-Page-Liste |
| "Notion-Schema" | `C:\Ground-Zero\VIRON_DATABASE\_system\_config\templates\notion-schema.sql` | PostgreSQL Schema-Definition |

---

## Router-Regeln

**Hinweis: 4 Zonen vs. 3 Zonen** — In diesem Repo gibt es zwei Zonen-Konzepte: Die **4-Zonen-Architektur** (DOCS/STORAGE/ARCHIVE/DESK) beschreibt das Repo-Top-Level-Layout für auto-injiziertes Wissen, Payload, Archiv und WIP. Das **3-Zonen-Content-Modell** (Brain/WIP/Final) beschreibt den Content-Erstellungs-Workflow (siehe .opencode/rules/marketing_workflow_dod.md). Beide nutzen "Zone" für unterschiedliche Konzepte — nicht verwechseln.

1. **Docs first, Storage second** — Prüfe zuerst ob die Info in Docs/ steht (CLAUDE.md, AGENTS.md, skill-router.md, storage-router.md). Erst wenn nicht dort: Storage laden.
2. **Inaktive Skills nicht automatisch laden** — Skills in `STORAGE/archive/skills/` sind bewusst deaktiviert. Nur laden wenn der User explizit danach fragt oder eine Aufgabe diesen Skill erfordert.
3. **Tool-Evaluations on demand** — `STORAGE/tools/` enthält Vergleiche und Entscheidungsgrundlagen. Nur laden bei Tool-Entscheidungen.
4. **Nach Nutzung merken** — Wenn ein Payload geladen wurde, kurz notieren was du daraus entnommen hast (spart Token beim nächsten Mal).
