# STORAGE Router — Payload-Index & Decision Matrix

STORAGE ist der Payload-Ordner. Hier liegt Wissen, das nicht an der Wand (in Docs) sein muss, aber jederzeit nachgeladen werden kann. Dieses Dokument listet alle verfügbaren Payloads und sagt dir, wann du sie laden solltest.

---

## Storage-Struktur

```
STORAGE/
├── INDEX.md                        ← Vollständige Payload-Liste (diese Datei)
├── marketingskills-integration-bericht.md  ← Forensische Analyse
├── TOOLS/
│   └── tool-decisions.md           ← Buffer/Metricool, Cal.com, Exa Entscheidungsmatrizen
├── CONTENT/
│   ├── 4 Mega-Guides               ← Produzierte Inhalte (Backup)
│   ├── 4 Pillar-Bundles
│   ├── 3 Social-Batches
│   ├── Prompt-Templates
│   └── Templates/
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
| "Wer sind unsere Konkurrenten?" | `DESK/HANDOVER/Marketing-research.md` | (liegt nicht in Storage, sondern in DESK/HANDOVER/) |
| "Was haben wir schon produziert?" | `STORAGE/CONTENT/INVENTAR.md` | (liegt in STORAGE/CONTENT/) |

---

## Router-Regeln

1. **Docs first, Storage second** — Prüfe zuerst ob die Info in Docs/ steht (CLAUDE.md, AGENTS.md, skill-router.md, storage-router.md). Erst wenn nicht dort: Storage laden.
2. **Inaktive Skills nicht automatisch laden** — Skills in `STORAGE/archive/skills/` sind bewusst deaktiviert. Nur laden wenn der User explizit danach fragt oder eine Aufgabe diesen Skill erfordert.
3. **Tool-Evaluations on demand** — `STORAGE/tools/` enthält Vergleiche und Entscheidungsgrundlagen. Nur laden bei Tool-Entscheidungen.
4. **Nach Nutzung merken** — Wenn ein Payload geladen wurde, kurz notieren was du daraus entnommen hast (spart Token beim nächsten Mal).
