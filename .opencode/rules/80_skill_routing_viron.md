---
name: Viron Skill Routing — Ergänzungen
description: Viron-spezifische Ergänzungen zum Skill-Routing: Mehrere Skills, Viron-Overrides, Sequenzen, Session-Entscheidungen. Ergänzt die 4 Context-Dispatcher-Regeln.
trigger: always_on
scope: alle
repo: marketing-setup
---

# 80_skill_routing_viron.md (Viron-Ergänzungen)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Alle Domänen (Factory, Studio, Lab)
> **BLOCK:** 80 — Regel-Evolution

## 1. Die 3 Entscheidungswege beim Skill-Laden

Basierend auf `80_skill_routing_reading.md` §1:

1. **Komplett lesen** — Kleine Skills (< 200 Zeilen, z.B. `find-bugs`, `memory-shrink`, `git-commit`) — monolithisch, keine Router-Struktur nötig.
2. **YAML + Kern-Sektion** — Große Skills (200-500 Zeilen, z.B. `turborepo`, `p5js`) — welche Sektion steht in `DOCS/SKILL_INDEX.md`.
3. **YAML + gezielt** — Sehr große Skills (> 500 Zeilen, z.B. `design-taste-frontend`, `ui-ux-pro-max`) — nur die spezifische Sektion nach Task.

**NIEMALS blind auf Zeile 25 oder 50 springen. Jeder Skill hat eine andere Struktur.**

## 2. Mehrere Skills

Wenn mehrere Skills in Frage kommen: **Alle lesen** und mit dem User abstimmen, welche wir nutzen. Entweder sie passen oder sie passen nicht — es gibt keine automatische Priorität die andere Skills ausschließt. Die Lade-Reihenfolge aus `71_skill_routing.md` §1 stellt nur sicher dass Abhängigkeiten korrekt aufgelöst werden.

Die drei Remotion-Skills sind ein 3er-Team:
- `remotion-best-practices` = BASE (atomare Syntax)
- `remotion-studio` = EXTENDS: Art Direction (Viron-eigen)
- `remotion-architect` = EXTENDS: Infrastructure (Viron-eigen)

Nicht selbst entscheiden, sondern dem User die Wahl lassen.

## 3. Viron-Overrides

Die gepatchten Skills (`clean-architecture`, `framer-motion`, `feature-arch`, `shadcn`) enthalten die Viron-Overrides bereits inline. Die konkreten Override-Regeln stehen in `71_skill_routing.md` §2. Bei Konflikt zwischen generischem Skill-Inhalt und Viron-Regel: **Immer die Viron-Variante**.

## 4. Sequenz-Hinweis

Wenn Skills aufeinander aufbauen: Verweise auf die Sequenz in der Skill Index (`DOCS/SKILL_INDEX.md`). Starte mit dem ersten Skill der Kette. Arbeite sequentiell — nutze die Output-Dateien des vorherigen Skills als Input für den nächsten. Die vollständige Sequenz steht dort — nicht hier vorwegnehmen.

## 5. Scan-Depth

Die konkrete Lesetiefe pro Skill steht in der Skill Index (`DOCS/SKILL_INDEX.md`) — Scan-Depth-Spalte. Das ist zu befolgen. Nicht pauschal 30 Zeilen oder 30%. Siehe auch `80_skill_routing_reading.md` §1-2.

## 6. Vendor-Skills und Patches

Vendor-Skills (von `npx skills`) werden regelmäßig aktualisiert. Unsere inline-gepatchten Skills (`clean-architecture`, `framer-motion`, `feature-arch`, `shadcn`) müssen bei Updates neu gepatcht werden. Der Patch-Workflow ist in `STORAGE/SKILL_PATCH_WORKFLOW.md` dokumentiert.

## 7. Session-Entscheidungen

| Entscheidung | Begründung |
|---|---|
| `emilkowal-animations` nicht nutzen | Duplikat von `emil-design-eng`. `emil-design-eng` ist umfassender (43 Regeln + Review-Format + Sonner + clip-path). |
| `git-policy` gelöscht | Redundant mit `40_git_policy.md` + `git-commit`. |
| 9 neue Skills aus opencode-core | security-review, agent-batching, find-bugs, memory-shrink, code-review, code-simplifier, git-commit, git-worktree. |
| Scan-Depth pro Skill in SKILL_INDEX | 3 Entscheidungswege statt pauschal 30% — jeder Skill hat andere Struktur. |
| 4 Context-Dispatcher-Regeln 1:1 übernommen | Vendor-Regeln bleiben update-safe, Viron-Ergänzungen nur hier. |

## 🔗 Light Router
- **WELCHER Skill für WELCHEN Task** → `DOCS/SKILL_INDEX.md` (Decision Matrix mit Scan-Depth)
- **WIE man Skills liest** → `80_skill_routing_reading.md` (3 Entscheidungswege)
- **Skill-Philosophie** → `80_skill_philosophy_and_workflow.md`
- **Conflict Resolution + Lade-Reihenfolge** → `71_skill_routing.md`
