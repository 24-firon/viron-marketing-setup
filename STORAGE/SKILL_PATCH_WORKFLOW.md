# Viron Skill Patch Workflow

> **Erstellt:** Phase 20 — 2026-02-28
> **Zweck:** Anleitung zum Re-Patchen von Vendor-Skills nach `npx skills add` Updates.

---

## 1. Warum wir patchen

Der Viron Agency Stack weicht in 6 kritischen Punkten vom Vendor-Standard ab:

| # | Constraint | Standard-Default | Viron-Standard |
|---|---|---|---|
| C1 | Tailwind Config | `tailwind.config.js` | CSS-first: `@theme inline {}` in CSS, kein Config-File |
| C2 | Farb-Format | HEX / HSL | OKLCH ausschließlich (`--background: oklch(1 0 0)`) |
| C3 | React Ref | `React.forwardRef()` | React 19: `ref` direkt als Prop |
| C4 | Form-Resolver | `zodResolver` aus `@hookform/resolvers/zod` | `standardSchemaResolver` aus `@hookform/resolvers/standard-schema` (Zod v4) |
| C5 | Animate-Plugin | `tailwindcss-animate` | `tw-animate-css` |
| C6 | Farb-Klassen | Hardcoded Tailwind-Farben (`bg-blue-500`) | CSS-Variable-Klassen (`bg-primary`, `text-destructive`) |

Zusätzlich gibt es Viron-Stack-spezifische Architektur-Abweichungen:

| Skill | Original-Konzept | Viron-Übersetzung |
|---|---|---|
| `clean-architecture` | Controller-Layer | Server Actions (`'use server'` Functions) |
| `clean-architecture` | Generische Layer-Beschreibung | Turborepo-Packages: domain, application, ui |
| `framer-motion` | Kein Scope-Limit | Nur `apps/web` — nie `apps/video` |
| `framer-motion` | Beliebige Easing | Spring-Standard oder Custom Bezier — nie `linear` |
| `feature-arch` | react-router-dom | Next.js App Router (`next/navigation`) |
| `feature-arch` | Prisma | Supabase |

---

## 2. Welche 4 Skills wurden gepatcht (v4, 2026-02-28)

### Skill 1: `clean-architecture`
**Patch-Dateien:** 3 (+ SKILL.md)
| Datei | Patch | Grund |
|---|---|---|
| `references/adapt-controller-thin.md` | Server Actions als Thin Controller | C: Controller-Begriff Next.js-fremd |
| `references/frame-web-in-infrastructure.md` | Hybrid Server Actions Pattern | C: Express-Pattern → Next.js Server Action |
| `SKILL.md` | `[!IMPORTANT]`-Block: Turborepo Layer-Mapping, Dependency Direction, Hybrid-OOP, Feature-Scoping | Fehlender Viron-Kontext |

### Skill 2: `framer-motion`
**Patch-Dateien:** 10 (+ SKILL.md)
| Datei | Patch | Constraint |
|---|---|---|
| `SKILL.md` | Scope-Restriction, GPU-Guard, Easing-Standard, LazyMotion, Motion-Split | Gesamt-Viron-Kontext |
| `anim-independent-transforms.md` | `ease: "linear"` für rotate verboten | Easing-Standard |
| `anim-keyframes-array.md` | `ease: "easeInOut"` + `linear` verboten | Easing-Standard |
| `bundle-dom-animation.md` | `color: "#0066cc"` paint-triggernd + hardcoded Hex verboten | C6 + GPU-Guard |
| `gesture-variants-flow.md` | `color: "#3b82f6"` verboten | C6 |
| `gesture-while-props.md` | `backgroundColor` in `whileHover` verboten | GPU-Guard |
| `rerender-animate-prop.md` | `backgroundColor` in variants verboten | GPU-Guard |
| `scroll-use-spring-smooth.md` | Spring-Params aus `lib/motion.ts` | Easing-Standard |
| `spring-physics-based.md` | Import aus `lib/motion.ts` presets | Easing-Standard |
| `svg-motion-components.md` | `duration: 0.3` ohne Spring + hardcoded Color | Easing-Standard + C6 |

### Skill 3: `feature-arch`
**Patch-Dateien:** 8 (+ SKILL.md)
| Datei | Patch | Constraint |
|---|---|---|
| `SKILL.md` | 6 Viron-Constraints (Monorepo, Next.js, Supabase, FSD, Tailwind v4, Functional-only) | Gesamt |
| `import-avoid-barrel-files.md` | `index.ts` als absolute Pflicht — keine "Alternative" | FSD Public API |
| `bound-feature-scoped-routing.md` | `react-router-dom` → Next.js App Router | Stack-Kontext |
| `struct-app-layer.md` | React Router Struktur → Next.js `layout.tsx`/`page.tsx` | Stack-Kontext |
| `fcomp-colocate-styles.md` | CSS Modules → Tailwind v4 + CSS Variables | C1/C2 |
| `fquery-single-responsibility.md` | Prisma → Supabase mit Client-Tabelle | Stack-Kontext |
| `fquery-avoid-n-plus-one.md` | Prisma `.findMany()` → Supabase `.in()` | Stack-Kontext |
| `fstate-context-sparingly.md` | Viron State-Hierarchie (TanStack → URL → useState → Context) | Stack-Kontext |

### Skill 4: `shadcn`
**Patch-Dateien:** 14 (+ SKILL.md)

**Batch A (7 Dateien):**
| Datei | Patch | Constraint |
|---|---|---|
| `style-use-tailwind-theme-extend.md` | Tailwind v4 CSS-first + OKLCH-Beispiel | C1 + C2 |
| `arch-forward-refs-for-composable-components.md` | React 19 ref-as-prop | C3 |
| `form-use-zod-for-schema-validation.md` | standardSchemaResolver | C4 |
| `form-use-react-hook-form-integration.md` | standardSchemaResolver | C4 |
| `form-show-validation-errors-correctly.md` | standardSchemaResolver | C4 |
| `form-handle-async-validation.md` | standardSchemaResolver | C4 |
| `form-reset-form-state-correctly.md` | standardSchemaResolver | C4 |

**Batch B (7 Dateien):**
| Datei | Patch | Constraint |
|---|---|---|
| `comp-create-reusable-form-fields.md` | standardSchemaResolver | C4 |
| `setup-components-json.md` | Kein `"config": "tailwind.config.js"` Feld | C1 |
| `style-dark-mode-support.md` | OKLCH statt HSL für Dark Mode | C2 |
| `ally-ensure-color-contrast.md` | OKLCH statt HSL im Kontrast-Beispiel | C2 |
| `arch-extend-variants-with-cva.md` | CSS-Variable-Klassen statt direkter Farben | C6 |
| `arch-isolate-component-variants.md` | CSS-Variable-Klassen statt direkter Farben | C6 |
| `SKILL.md` | Vollständiger `[!IMPORTANT]`-Block C1–C6 | Gesamt |

---

## 3. Patch-Mechanik (Inline-Append)

**Prinzip:** Original-Content wird NIE verändert. Patches werden am Dateiende angehängt.

```
[Original-Datei-Content]
                            ← unverändert
---

## Viron Stack: [Beschreibung]

> [!IMPORTANT]
> [Viron-Override-Inhalt]

[Code-Beispiele]
```

**Warum append-only:**
- Keine Merge-Konflikte bei zukünftigen Vendor-Updates
- Klare Trennung: "Was ist Original?" vs. "Was ist Viron-Patch?"
- Git diff zeigt sofort was Viron-spezifisch ist

---

## 4. Re-Patch-Anleitung nach `npx skills add`

Wenn ein Vendor-Skill per `npx skills add` aktualisiert wird, verlieren alle Patches ihren Stand. Vorgehensweise:

### Schritt 1: Diff erstellen
```bash
# Neues Original vs. letzter gepatchter Stand
git diff HEAD~1 .agents/skills/[skill-name]/
```

### Schritt 2: Bekannte Konflikt-Checklisten prüfen

**Für `clean-architecture`:**
- [ ] Wird "Controller" erwähnt ohne Server-Actions-Alternative? → Patch `adapt-controller-thin.md`
- [ ] Fehlt Turborepo Layer-Mapping in SKILL.md? → Patch SKILL.md

**Für `framer-motion`:**
- [ ] Wird `ease: "linear"` gezeigt (außer Loop-Animationen)? → GPU-Guard-Note
- [ ] Wird `backgroundColor`, `color`, `width`, `height` animiert? → GPU-Guard-Patch
- [ ] Fehlt Scope-Restriction in SKILL.md? → Patch SKILL.md
- [ ] Gibt es hardcoded Hex-Farben (`#xxxxxx`) in Animationswerten? → C6-Patch

**Für `feature-arch`:**
- [ ] Wird `react-router-dom` importiert? → Next.js App Router Patch
- [ ] Wird Prisma/Drizzle verwendet? → Supabase Patch
- [ ] CSS Modules statt Tailwind? → C1-Patch
- [ ] Fehlt FSD Public API in `import-avoid-barrel-files.md`? → Patch

**Für `shadcn`:**
- [ ] Wird `tailwind.config.js` erwähnt? → C1-Patch
- [ ] Werden HSL oder HEX-Farbwerte definiert? → C2-Patch (OKLCH)
- [ ] Wird `React.forwardRef` gezeigt? → C3-Patch (React 19)
- [ ] Wird `zodResolver` verwendet? → C4-Patch (standardSchemaResolver)
- [ ] Wird `tailwindcss-animate` erwähnt? → C5-Patch
- [ ] Werden hardcoded Tailwind-Farb-Klassen in Varianten gezeigt? → C6-Patch

### Schritt 3: Datei für Datei patchen

Reihenfolge pro Skill:
1. Alle reference-Dateien mit Konflikten (append-only, read-before-write)
2. SKILL.md zuletzt (Zusammenfassung aller Patches im `[!IMPORTANT]`-Block)

### Schritt 4: Report erstellen

`reports/phase[N]-[skill-name]-patch.md` mit Konflikt-Matrix und Patch-Log.

---

## 5. Versions-Tracking

| Skill | Original-Version (gepatcht) | Patch-Datum | Patch-Phase |
|---|---|---|---|
| `clean-architecture` | v4 (fresh via `npx skills add`) | 2026-02-28 | Phase 20 |
| `framer-motion` | v4 (fresh via `npx skills add`) | 2026-02-28 | Phase 20 |
| `feature-arch` | v4 (fresh via `npx skills add`) | 2026-02-28 | Phase 20 |
| `shadcn` | v4 (fresh via `npx skills add`) | 2026-02-28 | Phase 20 |

---

## 6. Was NICHT gepatcht wird

Diese Skills haben keine Viron-Konflikte und brauchen nach Updates keine Re-Patches:
- `zod` — Schema-Syntax ist Zod-v4-konform
- `tanstack-query` — TanStack Query v5 Syntax korrekt
- `react-hook-form` — Per se kein zodResolver
- `turborepo` — Passt zu Viron-Monorepo
- `remotion-best-practices` — Passt (wird durch remotion-studio/architect erweitert)
- `emilkowal-animations` — Motion-Philosophie ist Viron-konform
- `tdd`, `vitest`, `knip-deadcode` — Keine Viron-spezifischen Konflikte

---

## 7. Architektur: Warum Inline statt Extension-Skills

**Das Problem mit Extension-Skills (`-agency` Pattern):**
Ein Agent der nur den Base-Skill liest (weil das Routing ihn falsch zuordnet) sieht dann NICHT die Viron-Overrides. Die Extension-SKILL.md hilft nur wenn der Agent aktiv die Extension lädt.

**Die Lösung — Inline-Patch:**
Da jede reference-Datei direkt vom Agenten gelesen wird (bei tieferer Analyse), sind Inline-Patches in jeder einzelnen Datei wirksamer. Der Agent sieht den Viron-Block SOFORT nach dem Original-Content — egal ob er nur eine einzelne Reference-Datei oder die ganze SKILL.md liest.

> "Ein Agent der `adapt-controller-thin.md` liest und darin einen Server-Actions-Block sieht, ist sofort auf Kurs — egal ob er weiß dass clean-architecture-agency existiert."
