---
name: VIRON Marketing Skill Routing — Ergänzungen
description: VIRON-spezifische Ergänzungen zum Skill-Routing: Marketing-Skills, DACH-Overrides, Content-Sequenzen, VIRON-Tool-Stack.
trigger: always_on
scope: alle
repo: marketing-setup
---

# 80_skill_routing_viron.md (VIRON Marketing-Ergänzungen)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Alle Marketing-Domänen (Content, CRO, Social, Research)
> **BLOCK:** 80 — Regel-Evolution

## 1. Mehrere Skills

Wenn mehrere Marketing-Skills in Frage kommen: **Alle lesen** und mit dem User abstimmen, welche wir nutzen.

Die drei Content-Skills (`copywriting`, `copy-editing`, `content-strategy`) sind ein 3er-Team:
- `content-strategy` = BASE (Was schreiben wir?)
- `copywriting` = EXTENDS: Text produzieren (VIRON-eigen)
- `copy-editing` = EXTENDS: Bestehenden Text verbessern (VIRON-eigen)

Die VIRON-Skills bauen aufeinander auf. Nicht selbst entscheiden, sondern dem User die Wahl lassen.

## 2. VIRON-Overrides

Die Marketing-Skills sind provider-agnostisch. Bei Konflikt zwischen generischem Skill-Inhalt und VIRON-Regel: **Immer die VIRON-Variante**.

| Generischer Skill sagt... | VIRON-Regel |
|:--|:--|
| "Nutze GPT-4 für Copy" | Provider-agnostisch. n8n wählt via VIRON_TOOL_STACK |
| "Poste direkt auf LinkedIn" | Immer über n8n → Metricool Webhook |
| "Speichere Assets lokal" | Airtable Review-Base (nur Thumbnails + URLs) |
| "Python 3.12+ nutzen" | Python 3.11 zwingend. Docker-ready. |

## 3. Sequenz-Hinweis

Wenn Skills aufeinander aufbauen: Verweise auf die Sequenz in der Skill Index (`DOCS/SKILL_INDEX.md`). Starte mit dem ersten Skill der Kette. Die vollständige Sequenz steht in der jeweiligen SKILL.md — nicht hier vorwegnehmen.

## 4. Scan-Depth

Die konkrete Lesetiefe pro Skill steht in der Skill Index (`DOCS/SKILL_INDEX.md`) — Scan-Depth-Spalte. Das ist zu befolgen.

## 5. Session-Entscheidungen

| Entscheidung | Begründung |
|---|---|
| `aso` nicht nutzen | Keine Mobile App im VIRON-Angebot |
| `paywalls` nicht nutzen | Kein SaaS mit In-App Upgrades (Agentur) |
| `churn-prevention` nicht nutzen | Projekt-basiert, keine Subscriptions |
| 14 Skills aktiv, 19 archiviert | Token-Effizienz: nur Kernkompetenzen auto-injiziert |
| Scan-Depth-Konzept | 30%-Scan + konkrete Zeilenangaben in Skill Index |

## 🔗 Light Router
- **WELCHER Skill für WELCHEN Task** → `DOCS/SKILL_INDEX.md` (Decision Matrix mit Scan-Depth)
- **WIE man Skills liest** → `80_skill_routing_reading.md`
- **Skill-Philosophie** → `80_skill_philosophy_and_workflow.md`
