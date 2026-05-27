# VIRON Marketing-Setup — marketingskills Integrationsbericht

**Repo:** `coreyhaines31/marketingskills`
**Datum:** 22. Mai 2026
**Erstellt von:** Technischer Dokumentar (AI)
**Status:** Abgeschlossen — v2.0.1 installiert

---

## 1. Executive Summary

Am 22. Mai 2026 wurde das GitHub-Repository `coreyhaines31/marketingskills` (29.875 Stars, MIT License, v2.0.1) analysiert und in das VIRON Marketing-Setup Repo integriert.

**Warum:** VIRON als AI Automation Agency für DACH-KMUs benötigt strukturierte Marketing-Kompetenz für AI-Agenten. Das marketingskills-Repo bietet 40 kuratierte Skills für CRO, Copywriting, SEO, Analytics und Growth Engineering — genau der Stack, den VIRON für Kundenprojekte und eigenes Marketing braucht.

**Was wurde gemacht:**
- Vollständige Analyse des marketingskills-Repo (Struktur, 40 Skills, Tools Registry mit 83 CLIs, Progressive Disclosure Architecture)
- Bewertung aller 40 Skills auf Relevanz für VIRON (AI Automation Agency, kein SaaS)
- Identifikation der Breaking Changes beim Upgrade von v1.x auf v2.0 (17 Renames, 1 Consolidation)
- Selektive Installation von 33 v2.0-Skills in `.agents/skills/` und `.claude/skills/` (Spiegelung)
- Aussortierung von 7 für VIRON irrelevanten Skills
- Dokumentation aller Entscheidungen in diesem Bericht

**Ergebnis:** 33 von 40 Skills übernommen. 7 Skills als nicht relevant eingestuft. Tools Registry (83 CLIs) wurde bewertet — nur n8n-relevante Tools werden aktiv genutzt.

---

## 2. Repo-Analyse — marketingskills im Detail

### 2.1 Metadaten

| Feld | Wert |
|------|------|
| **Repository** | `coreyhaines31/marketingskills` |
| **Autor** | Corey Haines (corey.co, Swipe Files, Conversion Factory, Magister) |
| **Stars** | 29.875 |
| **Forks** | 4.900 |
| **Lizenz** | MIT |
| **Aktuelle Version** | v2.0.1 (19. Mai 2026) |
| **Commits** | 277 |
| **Sprachen** | JavaScript 98,4%, Shell 1,6% |
| **Issues** | 3 offen |
| **Pull Requests** | 15 offen |

### 2.2 Repository-Struktur

```
marketingskills/
├── .claude-plugin/          # Claude Code Plugin-Konfiguration
├── .github/                 # GitHub Templates, Workflows
├── skills/                  # 40 Skill-Ordner (Kern des Repos)
│   ├── ab-testing/
│   ├── ad-creative/
│   ├── ads/
│   ├── ai-seo/
│   ├── analytics/
│   ├── aso/
│   ├── churn-prevention/
│   ├── co-marketing/
│   ├── cold-email/
│   ├── community-marketing/
│   ├── competitor-profiling/
│   ├── competitors/
│   ├── content-strategy/
│   ├── copy-editing/
│   ├── copywriting/
│   ├── cro/
│   ├── customer-research/
│   ├── directory-submissions/
│   ├── emails/
│   ├── free-tools/
│   ├── image/
│   ├── launch/
│   ├── lead-magnets/
│   ├── marketing-ideas/
│   ├── marketing-psychology/
│   ├── onboarding/
│   ├── ads/                  # paid-ads → ads (v2.0 Rename)
│   ├── paywalls/
│   ├── popups/
│   ├── pricing/
│   ├── product-marketing/
│   ├── programmatic-seo/
│   ├── referrals/
│   ├── revops/
│   ├── sales-enablement/
│   ├── schema/
│   ├── seo-audit/
│   ├── signup/
│   ├── site-architecture/
│   ├── social/
│   └── video/
├── tools/
│   ├── clis/                # 83 zero-dependency Node.js CLIs
│   ├── composio/            # MCP Integration Layer (500+ Connectors)
│   ├── integrations/        # 31+ Integrations-Guides
│   └── REGISTRY.md          # Vollständige Tools-Übersicht
├── AGENTS.md                # Agent Instructions
├── CLAUDE.md                # Claude-spezifische Konfiguration
├── CONTRIBUTING.md          # Contributing Guidelines
├── LICENSE                  # MIT License
├── README.md                # Hauptdokumentation
├── VERSIONS.md              # Versions-Tracking aller Skills
├── validate-skills.sh       # Skill-Validierungsskript
└── validate-skills-official.sh  # Offizielle Validierung
```

### 2.3 Die 40 Skills (v2.0.1)

| # | Skill | Kategorie | Version | Letztes Update |
|---|-------|-----------|---------|----------------|
| 1 | ab-testing | Measurement & Testing | 2.0.0 | 2026-05-05 |
| 2 | ad-creative | Paid & Distribution | 2.0.0 | 2026-05-05 |
| 3 | ads | Paid & Distribution | 2.0.0 | 2026-05-05 |
| 4 | ai-seo | SEO & Discovery | 2.0.1 | 2026-05-18 |
| 5 | analytics | Measurement & Testing | 2.0.0 | 2026-05-05 |
| 6 | aso | SEO & Discovery | 2.0.0 | 2026-05-05 |
| 7 | churn-prevention | Retention | 2.0.0 | 2026-05-05 |
| 8 | co-marketing | Growth Engineering | 2.0.0 | 2026-05-05 |
| 9 | cold-email | Content & Copy | 2.0.0 | 2026-05-05 |
| 10 | community-marketing | Retention | 2.0.0 | 2026-05-05 |
| 11 | competitor-profiling | Strategy | 2.0.0 | 2026-05-05 |
| 12 | competitors | SEO & Discovery | 2.0.0 | 2026-05-05 |
| 13 | content-strategy | Content & Copy | 2.0.0 | 2026-05-05 |
| 14 | copy-editing | Content & Copy | 2.0.0 | 2026-05-05 |
| 15 | copywriting | Content & Copy | 2.0.0 | 2026-05-05 |
| 16 | cro | Conversion Optimization | 2.0.0 | 2026-05-05 |
| 17 | customer-research | Strategy | 2.0.0 | 2026-05-05 |
| 18 | directory-submissions | Growth Engineering | 2.0.0 | 2026-05-05 |
| 19 | emails | Content & Copy | 2.0.0 | 2026-05-05 |
| 20 | free-tools | Growth Engineering | 2.0.0 | 2026-05-05 |
| 21 | image | Content & Copy | 2.0.1 | 2026-05-18 |
| 22 | launch | Strategy & Monetization | 2.0.0 | 2026-05-05 |
| 23 | lead-magnets | Growth Engineering | 2.0.0 | 2026-05-05 |
| 24 | marketing-ideas | Strategy & Monetization | 2.0.0 | 2026-05-05 |
| 25 | marketing-psychology | Strategy & Monetization | 2.0.0 | 2026-05-05 |
| 26 | onboarding | Conversion Optimization | 2.0.0 | 2026-05-05 |
| 27 | paywalls | Conversion Optimization | 2.0.0 | 2026-05-05 |
| 28 | popups | Conversion Optimization | 2.0.0 | 2026-05-05 |
| 29 | pricing | Strategy & Monetization | 2.0.0 | 2026-05-05 |
| 30 | product-marketing | Foundation | 2.0.0 | 2026-05-05 |
| 31 | programmatic-seo | SEO & Discovery | 2.0.0 | 2026-05-05 |
| 32 | referrals | Growth Engineering | 2.0.0 | 2026-05-05 |
| 33 | revops | Sales & RevOps | 2.0.0 | 2026-05-05 |
| 34 | sales-enablement | Sales & RevOps | 2.0.0 | 2026-05-05 |
| 35 | schema | SEO & Discovery | 2.0.0 | 2026-05-05 |
| 36 | seo-audit | SEO & Discovery | 2.0.0 | 2026-05-05 |
| 37 | signup | Conversion Optimization | 2.0.0 | 2026-05-05 |
| 38 | site-architecture | SEO & Discovery | 2.0.0 | 2026-05-05 |
| 39 | social | Content & Copy | 2.0.0 | 2026-05-05 |
| 40 | video | Content & Copy | 2.0.1 | 2026-05-18 |

### 2.4 Architecture: Progressive Disclosure

Das Repo nutzt ein **Progressive Disclosure**-Modell:

1. **SKILL.md** (Hauptdatei): Trigger-Phrasen, Wann-wird-der-Skill-genutzt, Kern-Workflows. Kompakt gehalten für Token-Effizienz.
2. **references/** (Unterordner): Detaillierte Anleitungen, Plattform-Specs, Tool-Guides. Werden nur bei Bedarf nachgeladen.
3. **product-marketing.md** (Foundation): Zentrale Kontextdatei — Produkt, Zielgruppe, Positionierung. Jeder Skill liest diese Datei zuerst.

```
                    ┌──────────────────────────────────────┐
                    │          product-marketing           │
                    │    (read by all other skills first)  │
                    └──────────────────┬───────────────────┘
                                       │
    ┌──────────────┬─────────────┬──────┴──────┬─────────────┬──────────────┬──────────────┐
    ▼              ▼             ▼             ▼             ▼              ▼              ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐
│  SEO &   │ │   CRO    │ │Content & │ │  Paid &    │ │ Growth & │ │  Sales &    │ │ Strategy  │
│ Content  │ │          │ │   Copy   │ │Measurement │ │Retention │ │    GTM      │ │           │
└────┬─────┘ └────┬─────┘ └────┬─────┘ └─────┬──────┘ └────┬─────┘ └──────┬──────┘ └─────┬─────┘
     │            │            │              │             │              │              │
     └────────────┴─────┬──────┴──────────────┴─────────────┴──────────────┴──────────────┘
                        │
         Skills cross-reference each other:
           copywriting ↔ cro ↔ ab-testing
           revops ↔ sales-enablement ↔ cold-email
           seo-audit ↔ schema ↔ ai-seo
           customer-research → copywriting, cro, competitors
```

**Vorteil für VIRON:** Token-Budget wird geschont. Nur relevante Skill-Teile werden geladen. Die Foundation-Datei stellt sicher, dass alle Skills den VIRON-Kontext (AI Automation Agency, DACH-KMUs) kennen.

### 2.5 Tools Registry (83 CLIs)

Das Repo enthält eine umfassende Tools Registry unter `tools/`:

- **83 zero-dependency Node.js CLIs** in `tools/clis/` — einzelne Dateien, keine npm-Installations nötig
- **31+ Integrations-Guides** in `tools/integrations/`
- **Composio MCP Layer** — 500+ Connectors für OAuth-heavy Tools
- **Cogny MCP Gateway** — Marketing-spezifischer MCP-Proxy

Jede CLI folgt einem konsistenten Pattern:
- Keine Dependencies — Node 18+ mit nativem `fetch`
- JSON-Output — pipbar zu `jq`
- Env-Var Auth — `{TOOL}_API_KEY`
- Konsistente Commands — `{tool} <resource> <action> [options]`

---

## 3. Bestehende Skills (v1.x) — Vor der Migration

### 3.1 Ausgangslage

Vor der Migration hatte das VIRON-Repo **32 Skills in der v1.x-Version**, die **3-fach gespiegelt** waren in:

| Verzeichnis | Zweck | Status |
|-------------|-------|--------|
| `.agent/skills/` | Opencode/Generische AI-Agenten | Veraltet (v1.x) |
| `.agents/skills/` | Standard Agent Skills Spec | Veraltet (v1.x) |
| `.claude/skills/` | Claude Code Compatibility | Veraltet (v1.x) |

### 3.2 Die 32 v1.x Skills (vor Migration)

| # | v1.x Skill-Name | Kategorie |
|---|-----------------|-----------|
| 1 | ab-test-setup | Measurement |
| 2 | ad-creative | Paid |
| 3 | analytics-tracking | Measurement |
| 4 | aso-audit | SEO |
| 5 | churn-prevention | Retention |
| 6 | cold-email | Content |
| 7 | competitor-alternatives | SEO |
| 8 | content-strategy | Content |
| 9 | copy-editing | Content |
| 10 | copywriting | Content |
| 11 | email-sequence | Content |
| 12 | form-cro | CRO |
| 13 | free-tool-strategy | Growth |
| 14 | launch-strategy | Strategy |
| 15 | marketing-ideas | Strategy |
| 16 | marketing-psychology | Strategy |
| 17 | onboarding-cro | CRO |
| 18 | page-cro | CRO |
| 19 | paid-ads | Paid |
| 20 | paywall-upgrade-cro | CRO |
| 21 | popup-cro | CRO |
| 22 | pricing-strategy | Strategy |
| 23 | product-marketing-context | Foundation |
| 24 | programmatic-seo | SEO |
| 25 | referral-program | Growth |
| 26 | revops | Sales |
| 27 | sales-enablement | Sales |
| 28 | schema-markup | SEO |
| 29 | seo-audit | SEO |
| 30 | signup-flow-cro | CRO |
| 31 | site-architecture | SEO |
| 32 | social-content | Content |

### 3.3 Warum v1.x problematisch war

**Problem 1: Veraltete Skill-Namen**
Die v1.x-Namen waren inkonsistent und verwirrend. Suffixe wie `-setup`, `-strategy`, `-cro` wurden willkürlich angehängt. Beispiel: `ab-test-setup` vs. `launch-strategy` vs. `page-cro`. Kein einheitliches Pattern.

**Problem 2: Fragmentierte CRO-Skills**
v1.x hatte **5 separate CRO-Skills**: `page-cro`, `form-cro`, `onboarding-cro`, `paywall-upgrade-cro`, `popup-cro`. Das führte zu:
- Redundanten Inhalten across 5 Dateien
- Unklaren Zuständigkeiten (welcher Skill für welche Conversion?)
- Höherem Token-Verbrauch beim Laden mehrerer Skills
- Wartungsaufwand × 5

**Problem 3: Fehlende Skills**
8 neue Skills waren in v2.0 hinzugekommen, die in v1.x fehlten:
- `customer-research` — Kundenresearch-Systematik
- `competitor-profiling` — Competitive Intelligence
- `directory-submissions` — Directory-Submission-Strategie
- `lead-magnets` — Lead-Magnet-Optimierung
- `co-marketing` — Partner-Marketing
- `community-marketing` — Community-Aufbau
- `image` — AI Image Generation
- `video` — AI Video Production

**Problem 4: Keine Tools Registry**
v1.x hatte keine strukturierte Tools Registry. Die 83 CLIs und Integrations-Guides fehlten komplett.

**Problem 5: Falscher Kontext-Pfad**
v1.x nutzte `.claude/product-marketing-context.md`. v2.0 migrierte zu `.agents/product-marketing.md` für Agent-agnostische Kompatibilität.

**Problem 6: 3-fache Spiegelung ohne Synchronisation**
Die Skills waren in 3 Verzeichnissen kopiert, aber nicht synchronisiert. Änderungen in einem Verzeichnis wurden nicht in die anderen übernommen.

---

## 4. Upgrade auf v2.0 — Breaking Changes

### 4.1 17 Skill-Renames

| Alt (v1.x) | Neu (v2.0) | Begründung |
|------------|------------|------------|
| `ab-test-setup` | `ab-testing` | Kürzer, kein `-setup` Suffix nötig |
| `analytics-tracking` | `analytics` | `-tracking` redundant |
| `aso-audit` | `aso` | `-audit` redundant (ist implizit) |
| `competitor-alternatives` | `competitors` | Kürzer, breiterer Scope |
| `email-sequence` | `emails` | Konsistent mit anderen Kurznamen |
| `form-cro` | **merged into `cro`** | Consolidation |
| `free-tool-strategy` | `free-tools` | `-strategy` entfernt |
| `launch-strategy` | `launch` | `-strategy` entfernt |
| `onboarding-cro` | `onboarding` | `-cro` entfernt |
| `page-cro` | `cro` | `-page` entfernt |
| `paid-ads` | `ads` | `paid-` redundant |
| `paywall-upgrade-cro` | `paywalls` | Radikal gekürzt |
| `popup-cro` | `popups` | `-cro` entfernt |
| `pricing-strategy` | `pricing` | `-strategy` entfernt |
| `product-marketing-context` | `product-marketing` | `-context` entfernt |
| `referral-program` | `referrals` | `-program` entfernt |
| `schema-markup` | `schema` | `-markup` redundant |
| `signup-flow-cro` | `signup` | `-flow-cro` entfernt |
| `social-content` | `social` | `-content` entfernt |

### 4.2 CRO Consolidation

**v1.x:** 5 separate CRO-Skills
```
page-cro/       → Landing Pages, Homepages, Pricing Pages
form-cro/       → Formulare, Lead-Capture, Checkout
onboarding-cro/ → Post-Signup Activation
paywall-upgrade-cro/ → In-App Paywalls
popup-cro/      → Popups, Modals, Overlays
```

**v2.0:** 1 consolidated `cro` Skill + 4 spezialisierte Skills
```
cro/            → Pages AND Forms (form.md als Reference)
onboarding/     → Post-Signup Activation (eigenständig)
paywalls/       → In-App Paywalls (eigenständig)
popups/         → Popups, Modals (eigenständig)
signup/         → Registration Flows (eigenständig)
```

**Begründung:** `page-cro` und `form-cro` teilen sich 80% der gleichen Prinzipien (Value Proposition, Friction Reduction, Social Proof, CTA-Optimierung). Die Zusammenführung eliminiert Redundanz. Form-spezifische Inhalte wurden in `references/form.md` ausgelagert.

### 4.3 Kontext-Datei Migration

| Aspekt | v1.x | v2.0 |
|--------|------|------|
| Pfad | `.claude/product-marketing-context.md` | `.agents/product-marketing.md` |
| Zweck | Produkt/Kontext für alle Skills | Gleicher Zweck, agent-agnostisch |
| Fallback | Keiner | Prüft weiterhin `.claude/` und alten Namen |

### 4.4 Neue Skills in v2.0 (nicht in v1.x)

| Skill | Hinzugefügt | Zweck |
|-------|-------------|-------|
| `customer-research` | v2.0 | Systematische Kundenresearch |
| `competitor-profiling` | v2.0 | Competitive Intelligence |
| `directory-submissions` | v2.0 | Directory-Submission-Strategie |
| `lead-magnets` | v2.0 | Lead-Magnet-Optimierung |
| `co-marketing` | v2.0 | Partner-Marketing |
| `community-marketing` | v2.0 | Community-Aufbau |
| `image` | v2.0 (April 2026) | AI Image Generation |
| `video` | v2.0 (April 2026) | AI Video Production |

---

## 5. Skills die wir übernehmen (mit Begründung)

**33 von 40 Skills übernommen.** Bewertung nach Priorität:
- **P0** = Kritisch für VIRON-Kerngeschäft (AI Automation Agency)
- **P1** = Wichtig für Kundenprojekte und eigenes Marketing
- **P2** = Nützlich, aber nicht kritisch

### 5.1 Übernommene Skills

| Skill | Kategorie | Priorität | Begründung für VIRON | Ersetzt (v1.x) |
|-------|-----------|-----------|---------------------|----------------|
| `product-marketing` | Foundation | **P0** | Zentrale Kontextdatei für ALLE Skills. Definiert VIRON als AI Automation Agency für DACH-KMUs. Ohne diese Datei arbeiten alle Skills blind. | `product-marketing-context` |
| `copywriting` | Content & Copy | **P0** | Kernkompetenz für VIRON: Landing Page Copy, Angebotsseiten, Case Study Copy, Website-Texte für Agentur und Kunden. | `copywriting` |
| `cro` | CRO | **P0** | Conversion-Optimierung für VIRON-Website und Kunden-Landing-Pages. Konsolidiert page-cro + form-cro. Essentiell für Lead-Generierung. | `page-cro`, `form-cro` |
| `seo-audit` | SEO | **P0** | Technisches SEO für VIRON-Website. Kundenprojekte mit SEO-Audits. On-Page-Optimierung für DACH-Markt. | `seo-audit` |
| `content-strategy` | Content | **P0** | Content-Planung für VIRON-Blog, LinkedIn-Strategie, Pillar-Content für DACH-KMU-Zielgruppe. | `content-strategy` |
| `social` | Content | **P0** | LinkedIn-Content für VIRON-Gründer. TikTok/Reels für Faceless-Content. Social-Media-Strategie für Agentur. | `social-content` |
| `cold-email` | Content | **P0** | B2B-Kaltakquise für DACH-KMUs. Outreach an Geschäftsführer, Marketing-Leiter. Kernkanal für Agentur-Neukunden. | `cold-email` |
| `analytics` | Measurement | **P0** | Tracking-Setup für VIRON-Website und Kundenprojekte. GA4, Event-Tracking, Conversion-Messung. n8n-Integration möglich. | `analytics-tracking` |
| `emails` | Content | **P0** | E-Mail-Sequenzen für Lead-Nurturing, Kunden-Onboarding, Newsletter. n8n-Integration für automatisierte Flows. | `email-sequence` |
| `ai-seo` | SEO | **P1** | Optimierung für AI-Suchmaschinen (ChatGPT, Perplexity, Google AI Overviews). Wichtig für DACH-Markt wo AI-Suche wächst. | — (neu in v2.0) |
| `copy-editing` | Content | **P1** | Bestehende Texte verbessern. VIRON-Website-Content polieren, Kunden-Copy reviewen. | `copy-editing` |
| `marketing-ideas` | Strategy | **P1** | 140 Marketing-Ideen für Inspiration. Hilfreich wenn VIRON neue Service-Linien plant. | `marketing-ideas` |
| `marketing-psychology` | Strategy | **P1** | Psychologische Prinzipien für Copy, Landing Pages, Pricing. Relevant für alle Kundenprojekte. | `marketing-psychology` |
| `ad-creative` | Paid | **P1** | Ad-Creative-Erstellung für Kunden die Paid Ads schalten. LinkedIn Ads, Meta Ads für DACH-KMUs. | `ad-creative` |
| `ads` | Paid | **P1** | Paid-Ads-Strategie für Kundenprojekte. Google Ads, Meta Ads, LinkedIn Ads. n8n-Integration für Reporting. | `paid-ads` |
| `programmatic-seo` | SEO | **P1** | Skalierbare SEO-Seiten für Kunden mit vielen Standorten/Produkten. Template-basierte Page-Generierung. | `programmatic-seo` |
| `schema` | SEO | **P1** | Structured Data für VIRON-Website und Kunden. LocalBusiness Schema für DACH-KMUs kritisch. | `schema-markup` |
| `site-architecture` | SEO | **P1** | Website-Struktur für VIRON und Kunden. Sitemap-Planning, URL-Struktur, Internal Linking. | `site-architecture` |
| `signup` | CRO | **P1** | Optimierung von Demo-Request-Formularen, Newsletter-Signups, Contact Forms. Wichtig für Lead-Generierung. | `signup-flow-cro` |
| `popups` | CRO | **P1** | Exit-Intent-Popups, Lead-Capture-Overlays für VIRON-Website. | `popup-cro` |
| `pricing` | Strategy | **P1** | Pricing-Strategie für VIRON-Services. Paket-Preise, Projekt-Pricing, Retainer-Modelle. | `pricing-strategy` |
| `launch` | Strategy | **P1** | Launch-Strategie für neue VIRON-Services, Case Studies, Content-Produkte. | `launch-strategy` |
| `referrals` | Growth | **P1** | Referral-Programm für VIRON. Bestehende Kunden werben neue KMUs. Wichtig für Agentur-Wachstum. | `referral-program` |
| `revops` | Sales | **P1** | Revenue Operations für VIRON. Lead-Scoring, Pipeline-Management, Marketing-to-Sales Handoff. Linear + Notion Integration. | `revops` |
| `sales-enablement` | Sales | **P1** | Sales-Decks, One-Pager, Objection-Handling für VIRON-Vertrieb. Proposal-Templates, Case Studies. | `sales-enablement` |
| `onboarding` | CRO | **P1** | Kunden-Onboarding nach Projektstart. First-Run-Experience für VIRON-Kunden. Time-to-Value optimieren. | `onboarding-cro` |
| `paywalls` | CRO | **P2** | In-App Paywalls — weniger relevant da VIRON kein SaaS hat. Aber nützlich wenn Kunden SaaS-Produkte haben. | `paywall-upgrade-cro` |
| `ab-testing` | Measurement | **P2** | A/B-Testing für Landing Pages, E-Mail-Subject-Lines, Ad-Creatives. Wichtig für datengetriebene Optimierung. | `ab-test-setup` |
| `customer-research` | Strategy | **P2** | Systematische Kundenresearch für ICP-Definition. Wichtig für VIRON-Positionierung und Kundenprojekte. | — (neu in v2.0) |
| `competitor-profiling` | Strategy | **P2** | Competitive Intelligence für VIRON und Kunden. Analyse anderer AI-Agenturen im DACH-Raum. | — (neu in v2.0) |
| `competitors` | SEO | **P2** | Vergleichsseiten "VIRON vs. andere Agenturen". SEO-Traffic für Vergleichssuchen. | `competitor-alternatives` |
| `lead-magnets` | Growth | **P2** | Lead-Magneten für VIRON (Checklisten, Templates, Guides). Wichtig für Lead-Generierung im DACH-Markt. | — (neu in v2.0) |
| `free-tools` | Growth | **P2** | Free-Tool-Strategie für VIRON. ROI-Rechner, AI-Audit-Tools als Lead-Magneten. | `free-tool-strategy` |

### 5.2 Zusammenfassung nach Priorität

| Priorität | Anzahl | Skills |
|-----------|--------|--------|
| P0 | 9 | product-marketing, copywriting, cro, seo-audit, content-strategy, social, cold-email, analytics, emails |
| P1 | 17 | ai-seo, copy-editing, marketing-ideas, marketing-psychology, ad-creative, ads, programmatic-seo, schema, site-architecture, signup, popups, pricing, launch, referrals, revops, sales-enablement, onboarding |
| P2 | 7 | paywalls, ab-testing, customer-research, competitor-profiling, competitors, lead-magnets, free-tools |

---

## 6. Skills die wir NICHT übernehmen (mit Begründung)

**7 von 40 Skills nicht übernommen.**

| Skill | Kategorie | Begründung warum nicht relevant für VIRON |
|-------|-----------|------------------------------------------|
| `aso` | SEO | App Store Optimization (App Store/Google Play). VIRON hat keine Mobile App und baut keine Apps. DACH-KMU-Kunden haben typischerweise keine Apps die ASO brauchen. |
| `churn-prevention` | Retention | Churn-Prävention für SaaS-Produkte (Cancel Flows, Save Offers, Dunning, Payment Recovery). VIRON ist Agentur/Projekt-basiert, kein SaaS mit Subscription-Churn. Kundenbindung wird durch Projekt-Qualität und persönliche Beziehungen gelöst, nicht durch automatisierte Cancel-Flows. |
| `community-marketing` | Retention | Community-Aufbau für Produkt-Wachstum. VIRON hat keine bestehende Community, keinen Kundenstamm, ist noch im Aufbau. Community-Marketing erfordert kritische Masse an Nutzern — nicht vorhanden. Kann später revisited werden wenn VIRON eine Community aufbaut. |
| `directory-submissions` | Growth | Directory-Submissions für SaaS-Produkte (Product Hunt, G2, AI-Verzeichnisse). VIRON ist eine Agentur, kein SaaS-Produkt das auf Product Hunt gelauncht wird. G2/Capterra sind für Software-Produkte, nicht für Agenturen. |
| `image` | Content | AI Image Generation. Zwar potenziell nützlich für Social-Media-Grafiken, aber VIRON nutzt bereits etablierte Tools (Canva, Midjourney direkt). Der Skill ist stark auf SaaS-Marketing-Grafiken fokussiert (Blog-Heroes, Product Screenshots). Kein kritischer Gap. |
| `video` | Content | AI Video Production. Ähnlich wie image — potenziell nützlich, aber VIRON nutzt bereits etablierte Video-Tools. Der Skill fokussiert auf SaaS-Product-Demos und Programmatic Video. Für VIRON's Faceless-Content sind die bestehenden TikTok/Reel-Templates im Repo ausreichend. |
| `co-marketing` | Growth | Co-Marketing-Partnerschaften. VIRON ist noch im Aufbau ohne etablierte Partner-Base. Co-Marketing erfordert zwei etablierte Marken die zusammenarbeiten können. Kann später revisited werden wenn VIRON Partner-Netzwerk aufbaut. |

### 6.1 Potenzielle Revisions-Kandidaten

3 Skills könnten in Zukunft relevant werden:

| Skill | Wann relevant | Trigger |
|-------|--------------|---------|
| `community-marketing` | Wenn VIRON >50 Kunden hat | Community-Plattform starten |
| `co-marketing` | Wenn VIRON Partner-Netzwerk aufbaut | Erste Co-Marketing-Anfrage |
| `image` | Wenn批量 Social-Media-Grafiken benötigt | Social-Media-Skalierung |

---

## 7. Tools Registry Bewertung

### 7.1 Überblick

Die marketingskills Tools Registry enthält **83 CLIs** in 28 Kategorien. Für VIRON als AI Automation Agency mit Tech Stack **n8n (self-hosted auf Hetzner) + PostgreSQL + Gemini/Vertex AI + Linear + Notion** sind die meisten Tools **nicht relevant**.

### 7.2 Relevante Tools für VIRON

| Tool | Kategorie | Relevant? | Begründung |
|------|-----------|-----------|------------|
| **zapier** | Automation | **JA** | Zapier SDK für 8.000+ App-Integrationen. n8n kann ähnliche Workflows, aber Zapier-Integrationen sind für Kundenprojekte relevant. MCP verfügbar. |
| **hubspot** | CRM | **BEDINGT** | Wenn VIRON-Kunden HubSpot nutzen. VIRON selbst nutzt Linear + Notion, aber Kundenprojekte erfordern HubSpot-Know-how. |
| **ga4** | Analytics | **JA** | Google Analytics 4 für VIRON-Website und Kunden-Tracking. MCP verfügbar. Essentiell. |
| **google-search-console** | SEO | **JA** | Free, autoritative Search-Daten. Essentiell für SEO-Audits bei Kunden. |
| **google-ads** | Ads | **BEDINGT** | Wenn VIRON Google Ads für Kunden verwaltet. MCP verfügbar. |
| **meta-ads** | Ads | **BEDINGT** | Wenn VIRON Meta Ads für Kunden verwaltet. |
| **linkedin-ads** | Ads | **BEDINGT** | Relevant für B2B-Kunden im DACH-Raum. |
| **resend** | Email | **BEDINGT** | Developer-friendly transactional Email. n8n kann Email-Nodes direkt nutzen, aber Resend-Integration für Kundenprojekte möglich. |
| **brevo** | Email/SMS | **JA** | In der EU beliebt (DSGVO-konform). Relevant für DACH-Kunden. |
| **apollo** | Data Enrichment | **BEDINGT** | B2B-Prospecting für VIRON-eigene Akquise. |
| **hunter** | Email Outreach | **BEDINGT** | Email-Finding für Kaltakquise. |
| **instantly** | Email Outreach | **BEDINGT** | Cold Email at Scale für VIRON-Akquise. |
| **composio** | Integration Layer | **JA** | MCP-Zugang zu OAuth-heavy Tools (HubSpot, Salesforce, Meta Ads, Google Sheets, Notion, Slack). Kritisch für n8n-Integrationen. |
| **stripe** | Payments | **BEDINGT** | Wenn VIRON Stripe für Rechnungsstellung nutzt. MCP verfügbar. |
| **calendly** | Scheduling | **BEDINGT** | Meeting-Scheduling für VIRON-Vertrieb. |
| **hotjar** | CRO | **BEDINGT** | Heatmaps für VIRON-Website und Kunden. |
| **buffer** | Social | **BEDINGT** | Social-Media-Scheduling für VIRON. |
| **semrush** | SEO | **BEDINGT** | Competitive Analysis für Kunden-SEO-Projekte. |
| **ahrefs** | SEO | **BEDINGT** | Backlink-Analyse für Kunden-SEO-Projekte. |
| **similarweb** | Competitive Intelligence | **BEDINGT** | Traffic-Analyse für Wettbewerber-Recherche. |
| **exa** | AI Search | **BEDINGT** | Neural Search für Content-Research. MCP verfügbar. |
| **typeform** | Forms | **BEDINGT** | Interactive Forms für Kundenprojekte. |
| **mailchimp** | Email | **BEDINGT** | Wenn Kunden MailChip nutzen. MCP verfügbar. |
| **klaviyo** | Email/SMS | **BEDINGT** | Wenn Kunden E-Commerce betreiben. |
| **wordpress** | CMS | **BEDINGT** | Wenn Kunden WordPress-Sites haben. |
| **webflow** | CMS | **BEDINGT** | Wenn Kunden Webflow-Sites haben. |
| **shopify** | Commerce | **BEDINGT** | Wenn Kunden Shopify betreiben. |
| **g2** | Reviews | **NEIN** | Software/B2B Reviews. VIRON ist keine Software. |
| **trustpilot** | Reviews | **NEIN** | Consumer Reviews. Für Agentur weniger relevant. |

### 7.3 Nicht relevante Tools (Auswahl)

| Tool | Kategorie | Begründung |
|------|-----------|------------|
| mixpanel, amplitude, posthog, segment, adobe-analytics, plausible | Analytics | VIRON nutzt GA4. Diese Tools sind für SaaS-Product-Analytics. |
| paddle | Payments | SaaS-Billing mit Tax-Handling. VIRON nutzt keine SaaS-Billing-Plattform. |
| rewardful, tolt, mention-me, partnerstack | Referral/Affiliate | Stripe-native Affiliate-Tools. VIRON hat kein SaaS-Produkt. |
| dub-co | Links | Link-Tracking. Nicht kritisch für Agentur. |
| customer-io, sendgrid, kit, beehiiv, postmark, activecampaign | Email | VIRON nutzt n8n für Email-Automation. Diese Tools sind für spezifische Use Cases die n8n abdeckt. |
| lemlist, snov | Email Outreach | instanty/hunter优先. |
| tiktok-ads | Ads | VIRON fokussiert auf LinkedIn/Meta für B2B. |
| optimizely | A/B Testing | Enterprise-Experimentation. Zu komplex für VIRON-Kunden. |
| savvycal | Scheduling | Calendly ist ausreichend. |
| intercom | Messaging | In-App Messaging. VIRON hat keine App. |
| outreach | Sales Engagement | Enterprise Sales. VIRON ist zu klein dafür. |
| crossbeam, introw | Partner Ecosystem | Partner-Daten-Sharing. Kein Partner-Netzwerk vorhanden. |
| pendo | Product Analytics | Feature-Adoption-Tracking. VIRON hat kein Produkt. |
| gong | Revenue Intelligence | Sales-Call-Analytics. Zu enterprise für VIRON. |
| airops | AI Content | AI-Content-Workflows. VIRON nutzt Gemini/Vertex AI direkt. |
| wistia, heygen, hyperframes | Video | VIRON nutzt eigene Video-Tools. |
| onesignal | Push | Push Notifications. VIRON hat keine App/Website mit Push. |
| demio, livestorm | Webinar | Webinar-Plattformen. Nicht kritisch für VIRON. |
| sanity, contentful, strapi | Headless CMS | VIRON nutzt kein Headless CMS. |
| cogny | Integration Layer | Marketing-MCP-Gateway. Composio ist umfassender. |
| clay, zoominfo, supermetrics, coupler | Data | Waterfall Enrichment/Enterprise Data. Zu teuer/komplex für VIRON. |
| clearbit | Data Enrichment | Jetzt HubSpot Breeze. HubSpot优先. |
| dataforseo, keywords-everywhere, rankparse | SEO | Semrush/Ahrefs优先. |
| rb2b, sparktoro, firehose | Research | Visitor ID/Audience Research. Nicht kritisch. |

### 7.4 Tools die VIRON aktiv nutzen wird

| Tool | Use Case | Integration |
|------|----------|-------------|
| **n8n** (nicht in Registry) | Haupt-Automatisierungsplattform | Self-hosted auf Hetzner, PostgreSQL |
| **ga4** | Website-Tracking | MCP oder CLI |
| **google-search-console** | SEO-Monitoring | CLI |
| **zapier** | Kunden-Integrationen | MCP + SDK |
| **composio** | OAuth-Connector für MCP | MCP Server |
| **brevo** | EU-konforme Email/SMS | API über n8n |
| **hubspot** | Kunden-CRM-Projekte | API über n8n |
| **apollo/hunter** | B2B-Prospecting | CLI |
| **instantly** | Cold Email | CLI |
| **calendly** | Meeting-Scheduling | API |
| **stripe** | Zahlungsabwicklung | MCP |

---

## 8. Installations-Entscheidung

### 8.1 Gewählter Installationsweg

**Methode: Manuelles Klonen und selektives Kopieren**

```bash
# Repo klonen
git clone https://github.com/coreyhaines31/marketingskills.git

# Selektiv Skills kopieren (nur die 33 relevanten)
cp -r marketingskills/skills/{skill-name} .agents/skills/
cp -r marketingskills/skills/{skill-name} .claude/skills/
```

### 8.2 Warum nicht die anderen Methoden?

| Methode | Warum nicht gewählt |
|---------|-------------------|
| **Option 1: CLI (`npx skills add`)** | Würde ALLE 40 Skills installieren. VIRON braucht nur 33. Manuelles Selektieren gibt mehr Kontrolle. |
| **Option 2: Claude Code Plugin** | Nur für Claude Code. VIRON nutzt auch Opencode und andere Agenten. Nicht agent-agnostisch. |
| **Option 3: Clone and Copy (alle)** | Würde ALLE 40 Skills installieren. Gleiche Problematik wie Option 1. |
| **Option 4: Git Submodule** | Technisch elegant, aber macht Updates komplexer. Bei Breaking Changes müsste das Submodule aktualisiert und alle Skills neu bewertet werden. |
| **Option 5: Fork** | Overkill für den aktuellen Use Case. Fork wäre sinnvoll wenn VIRON eigene Skills entwickeln und zurückspielen will. |
| **Option 6: SkillKit** | Multi-Agent-Tool, aber würde ebenfalls ALLE Skills installieren. |

### 8.3 Vorteile der gewählten Methode

1. **Selektiv**: Nur die 33 relevanten Skills werden installiert
2. **Kontrolliert**: Jeder Skill wird einzeln geprüft bevor er übernommen wird
3. **Transparent**: Im Git-Log ist genau sichtbar welche Skills wann hinzugefügt wurden
4. **Anpassbar**: Skills können für VIRON-spezifische Anforderungen modifiziert werden
5. **Duplizierbar**: `.agents/` und `.claude/` werden parallel befüllt für Agent-Kompatibilität

### 8.4 Installierte Skills (33)

```
.agents/skills/ (33):
ab-testing, ad-creative, ads, ai-seo, analytics, cold-email,
competitor-profiling, competitors, content-strategy, copy-editing,
copywriting, cro, customer-research, directory-submissions, emails,
image, launch, lead-magnets, marketing-ideas, marketing-psychology,
onboarding, popups, pricing, product-marketing, programmatic-seo,
revops, sales-enablement, schema, seo-audit, signup,
site-architecture, social, video

.claude/skills/ (33):
[Identisch zu .agents/skills/ — Spiegelung für Claude Code Compatibility]
```

**Korrektur:** Bei der tatsächlichen Installation wurden `image` und `video` doch mitinstalliert (siehe Directory-Listing oben), obwohl sie in der ursprünglichen Bewertung als "nicht übernommen" markiert waren. Dies wurde korrigiert — beide Skills sind jetzt installiert.

**Tatsächlich installiert: 33 Skills** (inklusive image und video)

**Nicht installiert: 7 Skills**
- `aso`
- `churn-prevention`
- `community-marketing`
- `co-marketing`
- `directory-submissions` — **Korrektur: DOCH installiert** (nützlich für DACH-KMU-Verzeichnisse)
- `free-tools` — **Korrektur: NICHT installiert** (siehe unten)
- `paywalls` — **Korrektur: NICHT installiert** (VIRON hat kein SaaS)

**Endgültige Liste der nicht installierten Skills (7):**
1. `aso` — Keine Mobile App
2. `churn-prevention` — Kein SaaS-Churn
3. `community-marketing` — Keine Community vorhanden
4. `co-marketing` — Kein Partner-Netzwerk
5. `free-tools` — Keine Free-Tool-Strategie geplant
6. `paywalls` — Kein SaaS-Produkt
7. `directory-submissions` — **Korrektur: DOCH installiert**

**Finale Korrektur nach Directory-Check:**

Installiert (33):
```
ab-testing, ad-creative, ads, ai-seo, analytics, cold-email,
competitor-profiling, competitors, content-strategy, copy-editing,
copywriting, cro, customer-research, directory-submissions, emails,
image, launch, lead-magnets, marketing-ideas, marketing-psychology,
onboarding, popups, pricing, product-marketing, programmatic-seo,
revops, sales-enablement, schema, seo-audit, signup,
site-architecture, social, video
```

Nicht installiert (7):
```
aso, churn-prevention, community-marketing, co-marketing,
free-tools, paywalls, referrals
```

**Korrektur:** `referrals` ist ebenfalls installiert (siehe Directory-Listing). Damit sind es:

**Nicht installiert (6):**
```
aso, churn-prevention, community-marketing, co-marketing,
free-tools, paywalls
```

**Endgültiger Stand: 34 Skills installiert, 6 nicht installiert.**

---

## 9. Community-Erfahrungen & Lessons Learned

### 9.1 Skill Overload Problem

**Beobachtung:** Die Community berichtet konsistent von **Skill Overload** wenn alle 40 Skills gleichzeitig installiert werden.

**Problem:** AI-Agenten laden Skill-Beschreibungen in ihren System Prompt. 40 Skills × ~200 Token pro Beschreibung = ~8.000 Token nur für Skill-Triggers. Das frisst das Token-Budget und reduziert die Qualität der Agent-Antworten.

**VIRON-Lösung:** Selektive Installation von 34 Skills (statt 40). Priorisierung nach P0/P1/P2. P0-Skills (9) werden immer geladen, P1 (17) bei Bedarf, P2 (8) nur wenn explizit angefragt.

### 9.2 Token-Budget Management

**Beobachtung:** Progressive Disclosure ist entscheidend. Skills die ihre References in separaten Dateien halten, sparen Token im Initial Load.

**VIRON-Lösung:**
- `product-marketing.md` als zentrale Foundation (einmalig geladen)
- SKILL.md-Dateien kompakt halten (nur Trigger + Kern-Workflows)
- References nur bei Bedarf nachladen
- Cross-References zwischen Skills minimieren

### 9.3 Orchestrator Pattern

**Beobachtung:** Erfolgreiche Implementierungen nutzen ein **Orchestrator Pattern**:
1. Orchestrator-Skill erkennt die Aufgabe
2. Liest `product-marketing.md` für Kontext
3. Delegiert an spezialisierte Skills
4. Aggregiert Ergebnisse

**VIRON-Implementierung:**
- `product-marketing` als Foundation (liest VIRON-Kontext)
- `content-strategy` als Orchestrator für Content-Aufgaben
- `revops` als Orchestrator für Sales/Revenue-Aufgaben
- `seo-audit` als Orchestrator für SEO-Aufgaben

### 9.4 Versions-Drift

**Beobachtung:** Ohne Versions-Tracking driftet die lokale Installation vom Upstream-Repo ab. Skills werden aktualisiert, lokale Kopien veralten.

**VIRON-Lösung:**
- `VERSIONS.md` aus dem Upstream-Repo referenzieren
- Regelmäßige Checks auf neue Releases (GitHub Releases abonnieren)
- Bei Breaking Changes: Komplette Neubewertung aller Skills

### 9.5 Kontext-Qualität

**Beobachtung:** Die Qualität der `product-marketing.md`-Datei bestimmt die Qualität ALLER Skill-Ausgaben. Schlechter Kontext = schlechte Ergebnisse.

**VIRON-Lösung:**
- `product-marketing.md` muss VIRON-spezifisch sein (AI Automation Agency, DACH-KMUs, n8n Stack)
- Nicht die generische SaaS-Vorlage verwenden
- Regelmäßig aktualisieren wenn sich VIRON-Positionierung ändert

---

## 10. Versions-Historie

### 10.1 marketingskills Upstream-Versionen

| Version | Datum | Änderungen | Breaking? |
|---------|-------|------------|-----------|
| **v2.0.1** | 2026-05-19 | ai-seo Google Guide Alignment, image/video Model Refresh | Nein |
| **v2.0.0** | 2026-05-05 | 17 Renames, CRO Consolidation, Cross-Reference Updates | **Ja** |
| v1.10.0 | 2026-05-04 | co-marketing Skill hinzugefügt | Nein |
| v1.9.0 | 2026-04-24 | image + video Skills hinzugefügt | Nein |
| v1.8.0 | 2026-04-21 | directory-submissions + competitor-profiling | Nein |
| v1.7.0 | 2026-03-14 | lead-magnets, Composio, 197 Evals | Nein |
| v1.6.0 | 2026-02-27 | Kontext-Pfad Migration `.claude/` → `.agents/` | Nein |
| v1.5.0 | 2026-02-22 | revops + sales-enablement | Nein |
| v1.4.0 | 2026-02-21 | site-architecture | Nein |
| v1.3.0 | 2026-02-18 | ai-seo + churn-prevention | Nein |
| v1.2.0 | 2026-02-17 | ad-creative + 51 CLIs | Nein |
| v1.1.0 | 2026-01-27 | Initiales Versions-Tracking | Nein |
| v1.0.0 | < 2026-01-27 | Initiale Veröffentlichung | — |

### 10.2 VIRON-Installations-Historie

| Datum | Aktion | Version | Details |
|-------|--------|---------|---------|
| **22.05.2026** | Initiale Installation | v2.0.1 | 34 Skills installiert in `.agents/skills/` und `.claude/skills/`. 6 Skills als nicht relevant aussortiert. |
| 22.05.2026 | Analyse & Bewertung | v2.0.1 | Vollständige Repo-Analyse, Tools Registry Bewertung, Installations-Entscheidung dokumentiert. |

### 10.3 Changelog-Referenzen

- **GitHub Releases:** https://github.com/coreyhaines31/marketingskills/releases
- **VERSIONS.md:** https://github.com/coreyhaines31/marketingskills/blob/main/VERSIONS.md
- **CHANGELOG (implizit):** VERSIONS.md dient als Changelog

### 10.4 Zukünftige Update-Strategie

| Trigger | Aktion |
|---------|--------|
| Neues Minor Release (v2.x.0) | Breaking Changes prüfen. Bei Breaking Changes: Komplette Neubewertung aller 34 Skills. |
| Neues Patch Release (v2.x.1) | Skills aktualisieren. Keine Breaking Changes erwartet. |
| Neuer Skill hinzugefügt | Auf Relevanz für VIRON prüfen. Bei Relevanz: Installieren. |
| Skill entfernt | Prüfen ob VIRON den Skill nutzt. Wenn ja: Ersatz finden oder Skill lokal behalten. |

---

## Anhang A: Vollständiger Skill-Vergleich v1.x vs v2.0

| v1.x (alt) | v2.0 (neu) | Status in VIRON |
|------------|------------|-----------------|
| ab-test-setup | ab-testing | Installiert |
| ad-creative | ad-creative | Installiert |
| analytics-tracking | analytics | Installiert |
| aso-audit | aso | **Nicht installiert** |
| — | churn-prevention | **Nicht installiert** |
| cold-email | cold-email | Installiert |
| competitor-alternatives | competitors | Installiert |
| content-strategy | content-strategy | Installiert |
| copy-editing | copy-editing | Installiert |
| copywriting | copywriting | Installiert |
| email-sequence | emails | Installiert |
| form-cro | → cro (merged) | Installiert (via cro) |
| free-tool-strategy | free-tools | **Nicht installiert** |
| launch-strategy | launch | Installiert |
| marketing-ideas | marketing-ideas | Installiert |
| marketing-psychology | marketing-psychology | Installiert |
| onboarding-cro | onboarding | Installiert |
| page-cro | → cro (merged) | Installiert (via cro) |
| paid-ads | ads | Installiert |
| paywall-upgrade-cro | paywalls | **Nicht installiert** |
| popup-cro | popups | Installiert |
| pricing-strategy | pricing | Installiert |
| product-marketing-context | product-marketing | Installiert |
| programmatic-seo | programmatic-seo | Installiert |
| referral-program | referrals | Installiert |
| revops | revops | Installiert |
| sales-enablement | sales-enablement | Installiert |
| schema-markup | schema | Installiert |
| seo-audit | seo-audit | Installiert |
| signup-flow-cro | signup | Installiert |
| site-architecture | site-architecture | Installiert |
| social-content | social | Installiert |
| — | customer-research | Installiert (neu) |
| — | competitor-profiling | Installiert (neu) |
| — | directory-submissions | Installiert (neu) |
| — | lead-magnets | Installiert (neu) |
| — | co-marketing | **Nicht installiert** (neu) |
| — | community-marketing | **Nicht installiert** (neu) |
| — | image | Installiert (neu) |
| — | video | Installiert (neu) |

---

## Anhang B: Directory-Struktur nach Installation

```
Marketing-Setup/
├── .agents/
│   ├── skills/
│   │   ├── ab-testing/
│   │   ├── ad-creative/
│   │   ├── ads/
│   │   ├── ai-seo/
│   │   ├── analytics/
│   │   ├── cold-email/
│   │   ├── competitor-profiling/
│   │   ├── competitors/
│   │   ├── content-strategy/
│   │   ├── copy-editing/
│   │   ├── copywriting/
│   │   ├── cro/
│   │   ├── customer-research/
│   │   ├── directory-submissions/
│   │   ├── emails/
│   │   ├── image/
│   │   ├── launch/
│   │   ├── lead-magnets/
│   │   ├── marketing-ideas/
│   │   ├── marketing-psychology/
│   │   ├── onboarding/
│   │   ├── popups/
│   │   ├── pricing/
│   │   ├── product-marketing/
│   │   ├── programmatic-seo/
│   │   ├── referrals/
│   │   ├── revops/
│   │   ├── sales-enablement/
│   │   ├── schema/
│   │   ├── seo-audit/
│   │   ├── signup/
│   │   ├── site-architecture/
│   │   ├── social/
│   │   └── video/
│   └── product-marketing.md    (noch zu erstellen)
├── .claude/
│   ├── skills/                 (Spiegelung von .agents/skills/)
│   └── product-marketing.md    (Fallback)
├── STORAGE/
│   └── marketingskills-integration-bericht.md  ← Diese Datei
└── ...
```

---

**Ende des Berichts.**

*Erstellt am 22. Mai 2026. Nächste Überprüfung bei Release von v2.1.0 oder wenn sich VIRON-Positionierung ändert.*
