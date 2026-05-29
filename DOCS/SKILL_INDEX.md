# VIRON Marketing-Setup — Skill Index

> **Stand:** 2026-05-29
> **Zweck:** Decision Matrix: Welcher Skill wann. Scan-Depth: Wie tief lesen.
> **Regel:** `80_skill_routing_reading.md` (WIE man Skills liest)
> **Immer injiziert** via `opencode.jsonc`

---

## 1. Foundation (IMMER zuerst)

| Skill | Trigger-Phrasen | Scan-Depth | Kombiniert mit |
|---|---|---|---|
| `product-marketing` | "Produktkontext", "Positionierung", "ICP", "Zielgruppe definieren" | YAML + Context (erste ~30%) | Alle Skills |
| `customer-research` | "Kundenforschung", "Voice of Customer", "Interviews auswerten", "Pain Points" | YAML + Source Guides (erste ~40%) | `product-marketing`, `copywriting` |
| `competitor-profiling` | "Konkurrenz analysieren", "Competitor Research", "Competitor URLs" | YAML + Templates (erste ~30%) | `product-marketing`, `content-strategy` |

---

## 2. Content & Copy

| Skill | Trigger-Phrasen | Scan-Depth | Kombiniert mit |
|---|---|---|---|
| `content-strategy` | "Content Strategie", "Topic Clusters", "Content Planning", "Editorial Calendar" | YAML + Headless CMS Ref (erste ~30%) | `copywriting`, `customer-research` |
| `copywriting` | "Copy schreiben", "Landing Page", "Hero Section", "CTA Copy", "Value Proposition" | YAML + Quick-Ref (erste ~30%) | `content-strategy`, `cro` |
| `copy-editing` | "Copy verbessern", "Copy reviewen", "zu wortreich", "Content refresh" | YAML + Checklist Ref (erste ~40%) | `copywriting` |

---

## 3. Conversion & Pages

| Skill | Trigger-Phrasen | Scan-Depth | Kombiniert mit |
|---|---|---|---|
| `cro` | "Conversion optimieren", "Landing Page Conversions", "Formular Conversions", "CRO" | YAML + Experiments Ref (erste ~30%) | `copywriting`, `social` |

---

## 4. Social & Media

| Skill | Trigger-Phrasen | Scan-Depth | Kombiniert mit |
|---|---|---|---|
| `social` | "LinkedIn Post", "Social Media", "Content Calendar", "Repurpose Content" | YAML + Platform Limits (erste ~30%) | `copywriting`, `cro` |
| `image` | "Bild erstellen", "Social Graphic", "Blog Hero", "Product Mockup", "AI Image" | YAML + AI Prompting Ref (erste ~30%) | `social`, `copywriting` |
| `video` | "Video produzieren", "AI Video", "Erklärvideo", "Video Ad", "Reel" | YAML + AI Video Prompting (erste ~30%) | `social`, `image` |

---

## 5. Growth & Launch

| Skill | Trigger-Phrasen | Scan-Depth | Kombiniert mit |
|---|---|---|---|
| `pricing` | "Pricing Strategie", "Pricing Tiers", "Freemium", "Value Metric" | YAML + Tier Structure (erste ~30%) | `copywriting`, `cro` |
| `launch` | "Product Launch", "Product Hunt", "Feature Release", "Launch Checklist" | YAML + Quick-Ref (erste ~30%) | `directory-submissions`, `social` |
| `directory-submissions` | "Directory Listings", "Submit to directories", "Backlinks", "Product Hunt" | YAML + Directory List (erste ~30%) | `launch` |

---

## 6. Research & Psychology

| Skill | Trigger-Phrasen | Scan-Depth | Kombiniert mit |
|---|---|---|---|
| `marketing-psychology` | "Psychologische Trigger", "Cognitive Bias", "Persuasion", "Anchoring" | YAML + Quick-Ref (erste ~30%) | `copywriting`, `cro`, `pricing` |

---

## 7. Archivierte Skills (on-demand aus ARCHIVE/skills/)

| Skill | Trigger-Phrasen | Scan-Depth | Status |
|---|---|---|---|
| `ab-testing` | "A/B Test planen", "Split Test", "Testdauer" | YAML + Sample Size (erste ~30%) | Archiviert |
| `ad-creative` | "Ad Creatives", "Ad Copy", "RSA Headlines", "Creative Testing" | YAML + Generative Tools (erste ~30%) | Archiviert |
| `ads` | "Ad Kampagne", "Paid Media", "Google Ads", "Meta Ads" | YAML + Platform Setup (erste ~30%) | Archiviert |
| `ai-seo` | "AI Search optimieren", "ChatGPT sichtbar", "AI citations" | YAML + Content Types (erste ~30%) | Archiviert |
| `analytics` | "Tracking einrichten", "GA4", "Event Tracking", "UTM" | YAML + Event Library (erste ~30%) | Archiviert |
| `cold-email` | "Cold Outreach", "Prospecting Emails", "Follow-Up Sequence" | YAML + Subject Lines (erste ~30%) | Archiviert |
| `competitors` | "Vergleichsseite", "vs Page", "Alternativen Page" | YAML + Templates (erste ~30%) | Archiviert |
| `emails` | "Email Sequence", "Welcome Flow", "Drip Campaign" | YAML + Email Types (erste ~30%) | Archiviert |
| `lead-magnets` | "Lead Magnet", "Ebook", "Checklist", "Downloadable" | YAML + Format Guide (erste ~30%) | Archiviert |
| `marketing-ideas` | "Marketing Ideen", "Growth Ideas", "Brainstorm" | YAML + Ideas by Category (erste ~30%) | Archiviert |
| `onboarding` | "Onboarding Flow", "User aktivieren", "Empty States" | YAML + Experiments (erste ~30%) | Archiviert |
| `popups` | "Popup erstellen", "Exit-Intent", "Lead-Capture Modal" | YAML + Quick-Ref (erste ~30%) | Archiviert |
| `programmatic-seo` | "SEO Pages bauen", "Location Pages", "Template Pages" | YAML + Playbooks (erste ~30%) | Archiviert |
| `revops` | "Lead Scoring", "Lead Routing", "MQL Definition" | YAML + Routing Rules (erste ~30%) | Archiviert |
| `sales-enablement` | "Sales Deck", "Pitch Deck", "Objection Handling" | YAML + Deck Frameworks (erste ~30%) | Archiviert |
| `schema` | "Schema Markup", "JSON-LD", "Rich Snippets" | YAML + Schema Examples (erste ~30%) | Archiviert |
| `seo-audit` | "SEO prüfen", "Warum ranken wir nicht", "Technical SEO" | YAML + International SEO (erste ~30%) | Archiviert |
| `signup` | "Signup Flow", "Registrierungsabbruch", "Trial Signup" | YAML + Quick-Ref (erste ~30%) | Archiviert |
| `site-architecture` | "Site Struktur", "Sitemap", "Navigation", "URL-Struktur" | YAML + Navigation Patterns (erste ~30%) | Archiviert |

---

## 8. Skill-Sequenzen (Empfohlene Reihenfolge)

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

---

## 🔗 Light Router
- **WIE man Skills liest** → `80_skill_routing_reading.md`
- **Skill-Philosophie** → `80_skill_philosophy_and_workflow.md`
- **Skill-Anatomie** → `80_anatomy_of_complex_skill.md`
- **Skill-Erstellung** → `80_skill_construction_law.md`
- **VIRON-Overrides** → `80_skill_routing_viron.md`
- **Conflict Resolution** → `71_skill_routing.md`
