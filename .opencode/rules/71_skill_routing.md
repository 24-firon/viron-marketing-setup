---
name: Skill Routing — Lade-Reihenfolge & Conflict Resolution
description: Lade-Reihenfolge bei Mehrfach-Treffern, Conflict Resolution zwischen generischen und Viron-spezifischen Regeln, Skill Inheritance Map, Scan-Depth Quick-Referenz.
trigger: conditional
scope: alle
repo: marketing-setup
---

# 71_skill_routing.md

> **STATUS:** CONDITIONAL
> **SCOPE:** Alle Domänen (Factory, Studio, Lab)
> **BLOCK:** 70-79 — Agent & Knowledge
> **TRIGGER:** WENN du Skills lädst und mehrere Skills in Frage kommen oder Konflikte zwischen generischen und Viron-spezifischen Regeln auftreten

## 1. Lade-Reihenfolge bei Mehrfach-Treffern

**SOG:** Wenn eine Aufgabe mehrere Skills betrifft, lade in dieser Reihenfolge, DENN Foundation-Skills müssen vor Execution-Skills geladen werden um den Kontext korrekt aufzubauen. Wenn mehrere Skills passen: **Alle lesen** und mit dem User abstimmen.

| Ebene | Skills | Scan-Depth | Warum diese Reihenfolge |
|:--|:--|:--|:--|
| 1 | `clean-architecture`, `feature-arch`, `turborepo` | YAML + Quick-Ref (~30%) | Foundation zuerst — Architektur und Monorepo-Struktur müssen vor Implementierung klar sein |
| 2 | `tailwind`, `shadcn`, `zod`, `react-hook-form`, `tanstack-query` | YAML + Quick-Ref (~30%) | Core-Technologie — CSS, UI, Validierung, Daten-Fetching |
| 3 | `framer-motion`, `emil-design-eng`, `transitions-dev`, `gsap` | YAML + Framework-Sektion | Animation — baut auf UI auf, nicht umgekehrt |
| 4 | `remotion-best-practices`, `remotion-studio`, `remotion-architect` | YAML + Skill Router Tabelle | Video — separate Domäne, muss nach Foundation aber vor Quality geladen werden |
| 5 | `vitest`, `tdd`, `find-bugs`, `security-review`, `code-review`, `knip-deadcode` | YAML + Quick-Ref (~30%) | Qualität — Tests und Review nachdem Code existiert |
| 6 | Design-Skills: `frontend-design`, `design-taste-frontend`, `impeccable`, `high-end-visual-design`, `make-interfaces-feel-better`, `minimalist-ui`, `ui-ux-pro-max`, `landing-page-design`, `web-design-guidelines` | YAML + Kern-Sektionen (siehe SKILL_INDEX) | Design — parallel zu Core-Tech, informiert die visuelle Umsetzung |
| 7 | Specialized: `ui-cloner` Pipeline, `supabase`, `mcp-builder`, `doc-coauthoring`, alle Office/Dokumenten-Skills | YAML + jeweiliger Workflow | Spezialisiert — nur bei konkretem Task |

**Niemals beide aus derselben Extension-Kette überspringen:** `remotion-studio` + `remotion-architect` gleichzeitig ist erlaubt (verschiedene Aspekte). `remotion-studio` + `remotion-best-practices` nur als Fallback. Die beiden Viron-Skills bauen auf `remotion-best-practices` auf.

**Mehrere Skills:** Wenn 3 oder 4 Skills für eine Aufgabe in Frage kommen, alle lesen und mit dem User abstimmen welche wir nutzen. Entweder sie passen oder sie passen nicht — es gibt keine automatische Priorität die andere Skills ausschließt. Die Lade-Reihenfolge stellt nur sicher dass Abhängigkeiten korrekt aufgelöst werden.

## 2. Conflict Resolution

**SOG:** Wenn ein generischer Skill der Viron-spezifischen Variante widerspricht, folge der Viron-Variante, DENN die Inline-Patches enthalten projekt-spezifische Overrides, die für den Viron-Stack zwingend sind.

| Generischer Skill sagt... | Viron-Regel |
|:--|:--|
| `framer-motion`: "Use anywhere" | **Nur `apps/web`** — FORBIDDEN in `apps/video` |
| `framer-motion`: "Animate any property" | **GPU-Guard:** Nur `transform` + `opacity` |
| `clean-architecture`: "Use Controllers" | **Server Actions** = Thin Controllers, kein separater Controller-Layer |
| `clean-architecture`: "Functional entities" | **Hybrid-OOP:** Klassen erlaubt (private constructor + `create()`) |
| `feature-arch`: "react-router-dom" | **Next.js App Router** + `features/` in `apps/web/src/` |
| `feature-arch`: "Prisma / Drizzle" | **Supabase** — SSOT, kein Prisma |
| `tailwind`: "Configure via JS" | **CSS-first:** `@theme inline {}`, OKLCH, kein `tailwind.config.ts` |
| `shadcn`: "JS config, forwardRef" | **Tailwind v4 CSS-first, React 19** (kein forwardRef, `use()` statt `useContext()`) |
| `shadcn`: "zodResolver" | **standardSchemaResolver** (Zod v4 Kompatibilität) |
| `supabase`: "getSession()" | **getClaims()** für Auth-Checks — JWT-Signatur validiert |

## 3. Skill Inheritance Map (Workflows die aufeinander aufbauen)

```
remotion-best-practices              ← BASE (atomare Syntax: useCurrentFrame, spring, interpolate, Sequence)
├── remotion-studio                  ← EXTENDS: Art Direction (AgX, Physics, Cinematic, Failsafe-Mechanismen)
└── remotion-architect               ← EXTENDS: Infrastructure (Zod-Schemas, Pipelines, Daten-Engine, RTX Rendering)

clean-architecture                   ← INLINE-PATCHED: Turborepo-Mapping, Hybrid-OOP, Server Actions
feature-arch                         ← INLINE-PATCHED: FSD Public API, Next.js App Router, Supabase

tailwind                             ← BASE (CSS-first v4)
└── shadcn                           ← EXTENDS: Radix + CVA, React 19, Zod v4. Nutzt tailwind als Styling-Basis.

framer-motion                        ← INLINE-PATCHED: Scope (apps/web only), GPU-Guard, Motion-Split
emil-design-eng                      ← PHILOSOPHIE-EBENE: Purpose-Check VOR jeder framer-motion-Nutzung

algorithmic-art                      ← KONZEPT (Philosophie, Manifesto)
└── p5js                             ← IMPLEMENTIERUNG (Scripts, Templates, Export)

landing-page-design                  ← BASE (Conversion-Struktur, Hero-Formel, CTA, Section-Reihenfolge)
├── frontend-design                  ← EXTENDS: Kreative Richtung, Anti-Slop
└── ui-ux-pro-max                    ← EXTENDS: Suchbare Datenbank (161 Paletten, 57 Fonts)

ui-cloner                            ← ENTRY-POINT (AUDIT_MODE: standard / high-fidelity)
├── ui-cloner-forensic-audit         ← Phase 1: Site DNA (9 Steps)
├── ui-cloner-brand-interview        ← Phase 2: 12 Brand-Fragen
├── ui-cloner-synthesis              ← Phase 3: DNA + Brand → Prompt
├── ui-cloner-quality-check          ← Phase 4: Fidelity-Checkliste
└── ui-cloner-iterator               ← Post-Pipeline: 5-Pass Refinement

subagent-driven-development          ← BASE (Fresh SubAgent pro Task + Two-Stage Review)
├── agent-batching                   ← EXTENDS: Batch-Größen, Analyse≠Patch Trennung
└── git-worktree                     ← EXTENDS: Branch-Isolation für parallele Agenten

git-commit                           ← BASE (Conventional Commits, Diff-Analyse)
└── 40_git_policy.md (Regel)         ← EXTENDS: Account, Commit-Budget, Double-Turn-Lock, Secret-Check
```

## 4. Scan-Depth Quick-Referenz

Für die vollständige Scan-Depth-Tabelle mit exakten Zeilenangaben pro Skill: **`DOCS/SKILL_INDEX.md`**

| Skill | Kern-Sektion | Umfang |
|:--|:--|:--|
| `clean-architecture` | YAML + Quick-Ref + `dep-` Sektion | ~35 Zeilen |
| `feature-arch` | YAML + Quick-Ref + `struct-` Sektion | ~35 Zeilen |
| `tailwind` | YAML + `build-` und `gen-` Referenzen | ~30 Zeilen |
| `shadcn` | YAML + Quick-Ref | ~35 Zeilen |
| `framer-motion` | YAML + Quick-Ref | ~30 Zeilen |
| `emil-design-eng` | YAML + Animation Decision Framework + Review-Checklist | ~50 Zeilen |
| `react-hook-form` | YAML + Quick-Ref | ~30 Zeilen |
| `zod` | YAML + Quick-Ref | ~30 Zeilen |
| `tanstack-query` | YAML + Quick-Ref | ~30 Zeilen |
| `remotion-best-practices` | YAML + Quick Reference | ~30 Zeilen |
| `remotion-studio` | YAML + Skill Router Tabelle | ~15 Zeilen |
| `remotion-architect` | YAML + Critical Commandments + Decision Matrix | ~20 Zeilen |
| `supabase` | YAML + Core Principles + Security Checklist | ~50 Zeilen |
| `design-taste-frontend` | YAML + Section 0 (Brief Inference) + Section 1 (3 Dials) | ~75 Zeilen |
| `impeccable` | YAML + Commands-Tabelle + Shared Laws | ~40 Zeilen |
| `ui-ux-pro-max` | YAML + Quick Reference §1-§3 (CRITICAL + HIGH) | ~60 Zeilen |
| `turborepo` | YAML + Quick Decision Trees | ~25 Zeilen |
| `systematic-debugging` | YAML + The Four Phases | ~25 Zeilen |
| `git-commit` | Komplett | ~124 Zeilen |
| `git-worktree` | YAML + Core Operations | ~30 Zeilen |
| `memory-shrink` | Komplett | ~44 Zeilen |

## 5. Rules vs. Skills — Wichtige Unterscheidung

| Aspekt | Rules | Skills |
|:--|:--|:--|
| **Ort** | `.opencode/rules/` | `.agents/skills/` |
| **Laden** | Via `opencode.jsonc` → `instructions` (immer injiziert) | Via Description-Matching in `available_skills` |
| **Zweck** | Permanente Constraints, immer aktiv | Strukturierte Multi-Step-Workflows, on demand |
| **Struktur** | Einzelne `.md`-Datei mit YAML-Header | SKILL.md + Ordner (examples, templates, references) |
| **Token-Kosten** | Immer geladen → muss kompakt sein | Nur bei Trigger geladen → darf detailliert sein |

**SOG:** Rules sind GESETZE (immer da, kompakt). Skills sind ROUTER (bei Bedarf, detailliert). Verwechsle sie nicht.

## 6. Die 3 Fehler die Agenten beim Skill-Laden machen

| Falsch | Richtig |
|:--|:--|
| Alles in SKILL.md mergen | SKILL.md ist ein Router, Templates/Examples bleiben getrennt |
| Von oben nach unten lesen | Bedingungs-Matrix folgen, nur Nötiges laden |
| Examples ignorieren | Examples als "Definition of Done" behandeln |
| Ergebnis raten | Ergebnis mit Example vergleichen |

## 🔗 Light Router
- **WENN** du die vollständige Skill Index (alle 70 Skills, Trigger-Phrasen, Scan-Depth) brauchst ➔ **LIES** `DOCS/SKILL_INDEX.md`
- **WENN** du die Skill-Philosophie (Router statt Archiv) vertiefen willst ➔ **LIES** `80_skill_philosophy_and_workflow.md`
- **WENN** du wissen willst WIE man Skills liest (30%-Scan, Lazy-Loading) ➔ **LIES** `80_skill_routing_reading.md`
