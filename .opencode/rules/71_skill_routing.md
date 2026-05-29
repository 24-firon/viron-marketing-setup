---
name: Skill Routing — Conflict Resolution & Hierarchie
description: Skill-Hierarchie bei Mehrfach-Treffern, Conflict Resolution zwischen generischen und VIRON-spezifischen Regeln, Marketing-Skill-Übersicht.
trigger: conditional
scope: alle
repo: all
---

# 71_skill_routing.md

> **STATUS:** CONDITIONAL
> **SCOPE:** Alle Marketing-Domänen (Content, CRO, Social, Research)
> **BLOCK:** 70-79 — Agent & Knowledge
> **TRIGGER:** WENN du Skills lädst und Konflikte zwischen generischen und VIRON-spezifischen Regeln auftreten

## 1. Skill-Hierarchie bei Mehrfach-Treffern

**SOG:** Wenn eine Aufgabe mehrere Skills betrifft, lade in der Reihenfolge der Prioritäts-Ebene, DENN der Skill der höheren Ebene hat bei Konflikten Vorrang und verhindert Regelkollisionen.

| Ebene | Skills | Priorität |
|:--|:--|:--|
| 1 | `product-marketing`, `customer-research` | Höchste (Foundation) |
| 2 | `copywriting`, `cro`, `content-strategy` | Hoch (Execution) |
| 3 | `social`, `image`, `video` | Mittel (Distribution) |
| 4 | `pricing`, `launch`, `directory-submissions` | Mittel (Growth) |
| 5 | `competitor-profiling`, `marketing-psychology` | Niedrig (Research) |

**Niemals beide aus derselben Extension-Kette laden:** `copywriting` + `copy-editing` gleichzeitig ist erlaubt (verschiedene Aspekte). `content-strategy` + `copywriting` nur als Fallback.

## 2. Conflict Resolution

**SOG:** Wenn ein generischer Skill der VIRON-spezifischen Variante widerspricht, folge der VIRON-Variante, DENN die Inline-Overrides enthalten projekt-spezifische Regeln, die für den VIRON-Stack zwingend sind.

| Generischer Skill sagt... | VIRON-Regel |
|:--|:--|
| "Nutze OpenAI/GPT-4" | ABSOLUT VERBOTEN. Gemini/Vertex AI oder Claude |
| "Zapier für Automation" | n8n ist Standard. Open Source. Selbstbestimmt. |
| "Python 3.12+ nutzen" | Python 3.11 zwingend. Keine 3.12-Features. |
| "Speichere alles in Airtable" | Airtable nur für Review. Max 1.000 Records. |
| "Schreibe Notion-Dokus" | Notion ist Read-Only für Agenten. Nur Operator schreibt. |

## 3. Skill Inheritance Map

```
product-marketing                    ← BASE (ICP, Positionierung, Kontext)
├── customer-research                ← EXTENDS: Voice of Customer
└── competitor-profiling             ← EXTENDS: Competitive Intelligence

content-strategy                     ← BASE (Topic Clusters, Editorial)
├── copywriting                      ← EXTENDS: Copy produzieren
└── copy-editing                     ← EXTENDS: Copy verbessern

cro                                  ← BASE (Conversion-Optimierung)
├── social                           ← EXTENDS: Social Distribution
├── image                            ← EXTENDS: Visual Assets
└── video                            ← EXTENDS: Video Content

pricing                              ← BASE (Monetarisierung)
launch                               ← BASE (Go-to-Market)
directory-submissions                ← EXTENDS: Directory Listings
marketing-psychology                 ← EXTENDS: Behavioral Science
```

## 🔗 Light Router
- **WENN** du die vollständige Skill Index (alle 33 Skills, Trigger-Phrasen, Scan-Depth) brauchst ➔ **LIES** `DOCS/SKILL_INDEX.md`
- **WENN** du die Skill-Philosophie (Router statt Archiv) vertiefen willst ➔ **LIES** `80_skill_philosophy_and_workflow.md`
