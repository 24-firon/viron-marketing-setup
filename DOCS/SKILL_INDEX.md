# VIRON Marketing-Setup — Skill Index

> **Stand:** 2026-05-29
> **Zweck:** Decision Matrix: Welcher Skill wann. Scan-Depth: Wie tief lesen.
> **Regel:** `80_skill_routing_reading.md` (WIE man Skills liest)
> **Immer injiziert** via `opencode.jsonc`

---

## 1. Foundation (IMMER zuerst)

| Skill | Trigger-Phrasen | Zeilen | Refs | Scan-Depth | Kombiniert mit |
|---|---|---|---|---|---|
| `product-marketing` | "Produktkontext", "Positionierung", "ICP", "Zielgruppe definieren" | 241 | 0 | YAML + Sections 1-4 (Zeilen 1-80) | Alle Skills |
| `customer-research` | "Kundenforschung", "Voice of Customer", "Interviews auswerten", "Pain Points", "Reddit mining" | 270 | 1 (`source-guides.md`) | YAML + Extraction Framework (Z. 58-91) + Persona Template (Z. 176-220) | `product-marketing`, `copywriting` |
| `competitor-profiling` | "Konkurrenz analysieren", "Competitor Research", "Competitor URLs", "Competitor deep dive" | 411 | 2 (`templates.md`, `tool-reference.md`) | YAML + Tool-Reference komplett (references/tool-reference.md) | `product-marketing`, `content-strategy` |

---

## 2. Content & Copy

| Skill | Trigger-Phrasen | Zeilen | Refs | Scan-Depth | Kombiniert mit |
|---|---|---|---|---|---|
| `content-strategy` | "Content Strategie", "Topic Clusters", "Content Planning", "Editorial Calendar" | 365 | 1 (`headless-cms.md`) | YAML + Content Pillars (Z. 125-164) + Prioritizing (Z. 283-316) | `copywriting`, `customer-research` |
| `copywriting` | "Copy schreiben", "Landing Page", "Hero Section", "CTA Copy", "Value Proposition" | 252 | 2 (`copy-frameworks.md`, `natural-transitions.md`) | YAML + Writing Style Rules (Z. 61-80) + Page Structure (Z. 106-146) | `content-strategy`, `cro` |
| `copy-editing` | "Copy verbessern", "Copy reviewen", "zu wortreich", "Content refresh" | 457 | 3 (`checklist.md`, `content-refresh.md`, `plain-english-alternatives.md`) | YAML + Seven Sweeps (Z. 27-256 komplett) + Expert Panel (Z. 259-306) | `copywriting` |

---

## 3. Conversion & Pages

| Skill | Trigger-Phrasen | Zeilen | Refs | Scan-Depth | Kombiniert mit |
|---|---|---|---|---|---|
| `cro` | "Conversion optimieren", "Landing Page Conversions", "Formular Conversions", "CRO" | 187 | 1 (`experiments.md`), 1 (`form.md`) | YAML + CRO Analysis Framework (Z. 25-104 komplett) | `copywriting`, `social` |

---

## 4. Social & Media

| Skill | Trigger-Phrasen | Zeilen | Refs | Scan-Depth | Kombiniert mit |
|---|---|---|---|---|---|
| `social` | "LinkedIn Post", "Social Media", "Content Calendar", "Repurpose Content", "Reel" | 409 | 5 (`platforms.md`, `platform-limits.md`, `post-templates.md`, `reverse-engineering.md`, `short-form-video.md`) | YAML + Platform Quick Ref (Z. 41-51) + Hook Formulas (Z. 82-106) + Short-Form Video (Z. 312-389) | `copywriting`, `cro` |
| `image` | "Bild erstellen", "Social Graphic", "Blog Hero", "Product Mockup", "AI Image" | 340 | 1 (`ai-image-prompting.md`) | YAML + Model Comparison (Z. 54-65) + When to Use Which (Z. 68-93) | `social`, `copywriting` |
| `video` | "Video produzieren", "AI Video", "Erklärvideo", "Video Ad", "Reel" | 342 | 1 (`ai-video-prompting.md`) | YAML + Choosing Your Approach (Z. 37-46) + AI Video Model Comparison (Z. 129-148) | `social`, `image` |

---

## 5. Growth & Launch

| Skill | Trigger-Phrasen | Zeilen | Refs | Scan-Depth | Kombiniert mit |
|---|---|---|---|---|---|
| `pricing` | "Pricing Strategie", "Pricing Tiers", "Freemium", "Value Metric" | 231 | 2 (`tier-structure.md`, `research-methods.md`) | YAML + Three Pricing Axes (Z. 42-56) + Value Metrics (Z. 70-98) + Tier Structure (Z. 101-116) | `copywriting`, `cro` |
| `launch` | "Product Launch", "Product Hunt", "Feature Release", "Launch Checklist" | 353 | 0 | YAML + ORB Framework (Z. 31-101) + Five-Phase Launch (Z. 105-178) | `directory-submissions`, `social` |
| `directory-submissions` | "Directory Listings", "Submit to directories", "Backlinks", "Product Hunt" | 381 | 3 (`directory-list.md`, `positioning-variations.md`, `submission-tracker-template.csv`) | YAML + Three Hard Rules (Z. 33-65) + Workflow Step 1-2 (Z. 68-106) + PH Deep Dive (Z. 135-163) | `launch` |

---

## 6. Research & Psychology

| Skill | Trigger-Phrasen | Zeilen | Refs | Scan-Depth | Kombiniert mit |
|---|---|---|---|---|---|
| `marketing-psychology` | "Psychologische Trigger", "Cognitive Bias", "Persuasion", "Anchoring" | 455 | 0 | YAML + Quick Reference Tabelle (Z. 424-435) + gezielt einzelne Sektion nach Challenge | `copywriting`, `cro`, `pricing` |

---

## 7. Archivierte Skills (on-demand aus ARCHIVE/skills/)

| Skill | Zeilen | Refs | Scan-Depth | Status |
|---|---|---|---|---|
| `ab-testing` | ~266 | 2 | YAML + Sample Size (erste ~30%) | Archiviert |
| `ad-creative` | ~362 | 2 | YAML + Generative Tools (erste ~30%) | Archiviert |
| `ads` | ~315 | 3 | YAML + Platform Setup (erste ~30%) | Archiviert |
| `ai-seo` | ~398 | 3 | YAML + Content Types (erste ~30%) | Archiviert |
| `analytics` | ~309 | 3 | YAML + Event Library (erste ~30%) | Archiviert |
| `cold-email` | ~158 | 5 | YAML + Subject Lines (erste ~30%) | Archiviert |
| `competitors` | ~256 | 2 | YAML + Templates (erste ~30%) | Archiviert |
| `emails` | ~310 | 3 | YAML + Email Types (erste ~30%) | Archiviert |
| `lead-magnets` | ~neu | 2 | YAML + Format Guide (erste ~30%) | Archiviert |
| `marketing-ideas` | ~167 | 1 | YAML + Ideas by Category (erste ~30%) | Archiviert |
| `onboarding` | ~220 | 1 | YAML + Experiments (erste ~30%) | Archiviert |
| `popups` | ~454 | 0 | YAML + Quick-Ref (erste ~30%) | Archiviert |
| `programmatic-seo` | ~238 | 1 | YAML + Playbooks (erste ~30%) | Archiviert |
| `revops` | ~343 | 4 | YAML + Routing Rules (erste ~30%) | Archiviert |
| `sales-enablement` | ~349 | 4 | YAML + Deck Frameworks (erste ~30%) | Archiviert |
| `schema` | ~179 | 1 | YAML + Schema Examples (erste ~30%) | Archiviert |
| `seo-audit` | ~412 | 3 | YAML + International SEO (erste ~30%) | Archiviert |
| `signup` | ~359 | 0 | YAML + Quick-Ref (erste ~30%) | Archiviert |
| `site-architecture` | ~357 | 3 | YAML + Navigation Patterns (erste ~30%) | Archiviert |

---

## 8. Skill-Sequenzen (Workflows die aufeinander aufbauen)

| Goal | Reihenfolge |
|---|---|
| Neue Landing Page | `product-marketing` → `customer-research` → `copywriting` → `cro` |
| Content Engine | `product-marketing` → `content-strategy` → `copywriting` → `social` |
| Social Media | `content-strategy` → `copywriting` → `social` → `image` |
| Video Content | `content-strategy` → `copywriting` → `video` → `social` |
| Product Launch | `product-marketing` → `launch` → `directory-submissions` → `social` |
| Lead Gen | `product-marketing` → `customer-research` → `copywriting` → `cro` |
| Pricing Page | `product-marketing` → `pricing` → `copywriting` → `cro` |
| Competitor Analysis | `competitor-profiling` → `content-strategy` → `copywriting` |
| Copy verbessern | `copy-editing` (allein — Seven Sweeps nacheinander) |
| Content Refresh | `copy-editing` → `content-strategy` (Content Refresh Sektion) |
| Research-basiert | `customer-research` → `copywriting` → `cro` |
| Image Creation | `image` (allein — Model Comparison → Prompting → Optimization) |
| Video Production | `video` → `social` (Distribution) |

---

## 🔗 Light Router
- **WIE man Skills liest** → `80_skill_routing_reading.md`
- **Skill-Philosophie** → `80_skill_philosophy_and_workflow.md`
- **Skill-Anatomie** → `80_anatomy_of_complex_skill.md`
- **Skill-Erstellung** → `80_skill_construction_law.md`
- **VIRON-Overrides** → `80_skill_routing_viron.md`
- **Conflict Resolution** → `71_skill_routing.md`
