# VIRON DACH Custom Marketing Skills — Spezifikations-Report

**Status:** Final | **Datum:** 2026-05-25 | **Quelle:** IMPORT/05_DACH_Marketing_Spezifika.md

---

## Übersicht

| # | Skill | Priorität | Kurzbeschreibung |
|---|-------|-----------|------------------|
| 1 | `dsgvo-lead-capture` | **P0** | DSGVO-konforme Lead-Erfassung, Consent-Management, Server-Side-Tracking |
| 2 | `linkedin-dach-b2b` | **P0** | LinkedIn B2B Strategie für DACH-KMUs, Social Selling, 360-Brew |
| 3 | `local-seo-gbp` | **P0** | Local SEO & Google Business Profile als "living asset" |
| 4 | `german-email-marketing` | **P1** | Rechtssichere E-Mail-Marketing-Workflows, Double Opt-in |
| 5 | `whatsapp-business` | **P1** | WhatsApp Business für Kundenkommunikation |
| 6 | `content-authority-dach` | **P2** | Content Authority über Fachmedien, Gastbeiträge, CMCX-Networking |

---

## Skill 1: `dsgvo-lead-capture`

```yaml
name: dsgvo-lead-capture
description: >
  DSGVO-konforme Lead-Erfassung im DACH-Raum. Konsensuale Datenerhebung,
  granulare Consent-Formulare, Server-Side-Tracking, Cookie-Banner-Alternativen
  (Preference Center), DSGVO-Dokumentation. Nutze diesen Skill bei DSGVO-, Consent-,
  Lead-Generierungs- oder Tracking-Fragen mit DACH-Bezug.
```

### Trigger-Phrasen
- "DSGVO-konformes Formular erstellen"
- "Consent-Management einrichten"
- "Cookie-Banner Alternative"
- "Server-Side-Tracking DSGVO"
- "Lead-Erfassung Datenschutz"
- "Double Opt-in Lead Form"
- "Datenschutzkonforme Lead Generation"
- "GA4 Server-Side Setup"
- "Meta CAPI DSGVO-konform"
- "First-Party Data Capture"
- "Progressive Profiling DSGVO"

### Scope
- Granulare Consent-Optionen (Email, Phone, Analytics) entwerfen
- Widerrufsmechanismen automatisieren (N8N-integrierbar)
- Transparente Datenverwendungs-Dokumentation
- Interactive Content als First-Party Data Capture (Quizzes, Calculators)
- Value-First-Lead-Magneten (PDF, Tool, Template) — DSGVO-konform verpackt
- Progressive Profiling: Vertrauen aufbauen vor Datenerhebung
- Server-Side Tracking via GA4 / Meta CAPI (N8N als Proxy)
- PostgreSQL-first Tracking statt client-side GTM
- Cookie-Banner-Alternativen: Preference-Center-Ansatz
- LkSG-konforme Datenhaltung im Lieferkettenkontext
- AI Act: Kennzeichnungspflicht für KI-generierte Lead-Interaktionen

### Abhängigkeiten
1. **Foundation:** `.agents/product-marketing.md` (VIA product-marketing Skill)
2. **Rechtlich:** DSGVO-Textbausteine des Kunden (Datenschutzerklärung, AGB)
3. **Technisch:** N8N-Zugriff für Server-Side-Tracking, PostgreSQL für First-Party-Data
4. **Vorher lesen:** `IMPORT/05_DACH_Marketing_Spezifika.md` Abschnitte 5.1.1, 5.3.1

### Referenzen
- **IMPORT/05:** Abschnitt 5.1.1 (DSGVO 2026 Verschärfungen), Abschnitt 5.3.1 (DSGVO-Compliant Lead Generation Framework)
- **Regulatorik:** E-Privacy-Verordnung, Digital Services Act, AI Act
- **Framework (5.1.1):** Consent Layer → First-Party Capture → Server-Side Tracking
- **VIRON-Wettbewerbsvorteil:** DSGVO-by-Design als USP gegen US-Agencies

### Priorität
**P0** — Jeder Marketing-Service muss DSGVO-konform sein. Ohne diesen Skill ist Lead-Gen in DACH nicht rechtskonform. Top 1 der DACH-Skills.

---

## Skill 2: `linkedin-dach-b2b`

```yaml
name: linkedin-dach-b2b
description: >
  LinkedIn B2B Strategie für DACH-KMUs. Social Selling, 360-Brew-Algorithmus,
  deutschsprachiger Content-Kalender, Thought Leadership, Sie/Du-Tone-of-Voice,
  Engagement-Automatisierung, LinkedIn Ads Targeting für DACH. Nutze diesen Skill
  für alle LinkedIn-Fragen mit DACH-Bezug.
```

### Trigger-Phrasen
- "LinkedIn Strategie DACH"
- "LinkedIn B2B Deutschland"
- "LinkedIn Post auf Deutsch"
- "Social Selling DACH"
- "LinkedIn Content Kalender"
- "LinkedIn Thought Leadership"
- "LinkedIn Reichweite erhöhen"
- "LinkedIn Ads KMU"
- "LinkedIn Creator Mode"
- "XING Alternative LinkedIn"
- "360-Brew LinkedIn"
- "Kommentare statt Likes LinkedIn"

### Scope
- Deutsche LinkedIn-Algorithmus-Optimierung (360-Brew-Modell adaptieren)
- Content-Kalender für DACH-Arbeitszeiten (08:00–09:00, 17:00–18:00 MEZ)
- Sie/Du-Tone-of-Voice-Framework (Business-Kontext: primär "Sie")
- Thought-Leadership-Serien statt Product Pitching
- Kommentar-getriebenes Engagement (Tiefe > Likes)
- LinkedIn Creator Mode Setup & Optimierung
- LinkedIn Ads Targeting für DACH-Zielgruppen
- XING-Integration für 40+-Zielgruppe (wo noch relevant)
- Personal Brand vs. Unternehmensseite (Personal Brand konvertiert)
- Content-Typ-Matrix: Text-Post, Carousel, Video, Document Post für DACH
- Lead-Gen Forms DSGVO-konform gestalten

### Abhängigkeiten
1. **Foundation:** `.agents/product-marketing.md` (VIA product-marketing Skill)
2. **Inhaltlich:** `DOCS/brand-voice.md`, `DOCS/icp-summary.md`
3. **Content:** `DOCS/skill-router.md` → social Skill für Einzelposts
4. **Vorher lesen:** `IMPORT/05_DACH_Marketing_Spezifika.md` Abschnitt 5.2.1

### Referenzen
- **IMPORT/05:** Abschnitt 5.2.1 (LinkedIn als primäre B2B-Plattform)
- **Kennzahlen:** 78% Social Sellers outperform Peers [web:67]
- **VIRON-Service-Idee:** "LinkedIn DACH Strategy" mit Content-Plan, Posting, Engagement
- **Kulturell:** Substanz > Hype, Thought Leadership > Product Pitching

### Priorität
**P0** — LinkedIn ist die primäre B2B-Plattform im DACH-Raum. Social-Selling-Frameworks aus US-Bundles greifen ohne kulturelle Adaption nicht.

---

## Skill 3: `local-seo-gbp`

```yaml
name: local-seo-gbp
description: >
  Local SEO & Google Business Profile Management für DACH-KMUs. GBP-Optimierung,
  lokale Keyword-Strategien (de-de, de-at, de-ch), deutsche Branchenverzeichnisse,
  Review-Management, Schema Markup (LocalBusiness, Service, FAQ), Hreflang-Implementierung.
  Nutze diesen Skill für lokale Sichtbarkeit, Google Maps-Präsenz und regionale SEO.
```

### Trigger-Phrasen
- "Google Business Profile optimieren"
- "Local SEO Deutschland"
- "Google Maps Ranking verbessern"
- "Branchenverzeichnis eintragen"
- "Lokale Keywords recherchieren"
- "Review-Management Google"
- "GBP Posts erstellen"
- "Gelbe Seiten Eintrag"
- "Hreflang de-de de-at de-ch"
- "LocalBusiness Schema"
- "Regionale Sichtbarkeit KMU"
- "Google Q&A beantworten"

### Scope
- Google Business Profile: Posts, Q&A, Reviews, Produkte, Services aktiv managen
- Lokale Keyword-Recherche: "[Dienstleistung] + [Stadt]" für DE/AT/CH
- Deutsche Branchenverzeichnisse: Gelbe Seiten, Das Örtliche, Herold (AT), local.ch (CH)
- Review-Management auf Deutsch (Antwortstrategien, Negativ-Review-Handling)
- Schema Markup: LocalBusiness, Service, FAQ für deutsche SERPs
- Hreflang-Implementierung: de-de, de-at, de-ch korrekt taggen
- Local Hosting: Server-Standort DE/AT/CH für Page-Speed-Vorteil
- NAP-Konsistenz (Name, Adresse, Telefon) über alle Verzeichnisse
- GBP Insights lesen & Handlungsempfehlungen ableiten
- Linkbuilding über lokale Partnerschaften, Kammern, Verbände

### Abhängigkeiten
1. **Foundation:** `.agents/product-marketing.md` (VIA product-marketing Skill)
2. **Technisch:** Zugriff auf GBP-Account des Kunden, Website-Zugriff für Schema
3. **SEO:** `STORAGE/archive/skills/schema/SKILL.md` (falls Schema-Tiefe nötig)
4. **Vorher lesen:** `IMPORT/05_DACH_Marketing_Spezifika.md` Abschnitt 5.2.2

### Referenzen
- **IMPORT/05:** Abschnitt 5.2.2 (Local SEO & Google Business Profile)
- **Kennzahlen:** 46% aller Google-Suchen haben lokale Intent
- **Konzept:** GBP als "living asset" [web:19]
- **VIRON-Service-Idee:** "Local Visibility Booster" — GBP, Keywords, Verzeichnisse

### Priorität
**P0** — DACH-KMUs sind stark lokal verankert. Local SEO ist für die ICP-Zielgruppe (lokaler Einzelhandel, Dienstleister) der höchste Impact-Kanal.

---

## Skill 4: `german-email-marketing`

```yaml
name: german-email-marketing
description: >
  Rechtssichere E-Mail-Marketing-Workflows für DACH. Double Opt-in, DSGVO-konforme
  Automation, deutsche Newsletter-Strategien (Steady, Revue), Sie/Du-Tone,
  Willkommens-Sequenzen, Re-activation-Kampagnen, Segmentierung nach Branche/Rolle/Größe.
  Nutze diesen Skill für alle E-Mail-Marketing-Fragen mit DACH-Bezug.
```

### Trigger-Phrasen
- "E-Mail-Marketing Deutschland"
- "DSGVO Newsletter versenden"
- "Double Opt-in einrichten"
- "Willkommens-Sequenz Email"
- "E-Mail-Automation deutsch"
- "Newsletter Strategie KMU"
- "Re-activation Kampagne"
- "E-Mail Segmentierung B2B"
- "Siezen in E-Mails"
- "Steady Newsletter"
- "E-Mail Signatur deutsch"
- "Impressumspflicht Email"

### Scope
- Double Opt-in Flow (Bestätigungsmail, Bestätigungsseite, Willkommensmail)
- DSGVO-konforme Listenführung: Einwilligung, Widerruf, Dokumentation
- Willkommens-Sequenz-Templates (3–5 Mails) in deutscher Tone-of-Voice
- Onboarding-Flows für Neukunden (Service-basiert, nicht SaaS)
- Re-activation-Kampagnen (Inaktive Abonnenten reaktivieren — vor Löschung)
- Segmentierung: Branche, Firmengröße, Rolle, Engagement-Level
- Deutsche Newsletter-Plattformen: Steady, Revue, Mailchimp-DSGVO, CleverReach
- Content-Strategie: Nützliche Inhalte > reine Promotion (DACH-Präferenz)
- Sie/Du-Entscheidungsmatrix (B2B: Sie, B2C: Kontextabhängig)
- Impressum & rechtliche Pflichtangaben in jeder E-Mail
- Tracking-Opt-out (kein Tracking ohne explizite Einwilligung)
- Integration mit N8N für Automation

### Abhängigkeiten
1. **Foundation:** `.agents/product-marketing.md` (VIA product-marketing Skill)
2. **Rechtlich:** DSGVO-Dokumentation des Kunden, Datenschutzerklärung
3. **Content:** `DOCS/brand-voice.md` für Tone-of-Voice
4. **Skill:** `dsgvo-lead-capture` (Consent-Layer teilen)
5. **Vorher lesen:** `IMPORT/05_DACH_Marketing_Spezifika.md` Abschnitt 5.2.4

### Referenzen
- **IMPORT/05:** Abschnitt 5.2.4 (Email Marketing & Newsletter)
- **Kennzahlen:** Deutsche öffnen weniger E-Mails, engagieren sich aber stärker bei relevanten
- **VIRON-Service-Idee:** "DACH Email Engine" — DSGVO-konforme Automation
- **Prinzip:** Qualität > Quantität in der DACH-Zielgruppe

### Priorität
**P1** — E-Mail-Marketing ist für Lead-Nurture und Bestandskunden essentiell. Nachrangig zu P0-Skills, da DSGVO-Grundlagen bereits in dsgvo-lead-capture abgedeckt sind.

---

## Skill 5: `whatsapp-business`

```yaml
name: whatsapp-business
description: >
  WhatsApp Business für Kundenkommunikation im DACH-Raum. Katalog-Setup,
  automatisierte Antworten (N8N-integriert), DSGVO-konforme Broadcast-Listen,
  WhatsApp API Integration, B2C-Kommunikationsstrategien, Abgrenzung zu US-zentrierten
  SMS-Marketing-Ansätzen. Nutze diesen Skill für alle WhatsApp-Marketing-Fragen.
```

### Trigger-Phrasen
- "WhatsApp Business einrichten"
- "WhatsApp Katalog erstellen"
- "WhatsApp Automatisierung"
- "WhatsApp Broadcast DSGVO"
- "WhatsApp API N8N"
- "Kundenkommunikation WhatsApp"
- "WhatsApp Marketing KMU"
- "Auto-Response WhatsApp"
- "WhatsApp vs SMS Marketing"
- "WhatsApp Newsletter"
- "WhatsApp Business App vs API"

### Scope
- WhatsApp Business App vs. WhatsApp Business API (Entscheidungsmatrix)
- Katalog-Integration (Produkte, Services, Preisliste)
- Automatisierte Antworten: Begrüßung, Abwesenheit, FAQ-Bot
- N8N-Integration: WhatsApp-Trigger für Workflows (Anfrage → Lead → Deal)
- DSGVO-konforme Broadcast-Listen (Opt-in, Inhalt, Frequenz)
- Quick-Replies für häufige Kundenanfragen
- Chat-Transfer: Bot → Mensch (Eskalationslogik)
- WhatsApp als Service-Kanal (nicht nur Marketing)
- Abgrenzung zu US-SMS-Marketing (warum WhatsApp in DACH, nicht SMS)
- Plattformwahl: WhatsApp vs. Signal vs. Telegram für DACH-KMUs
- Analytics: Öffnungsraten, Antwortraten, Conversion-Tracking
- Template-Messages (Marketing, Utility, Authentication) via Meta Business

### Abhängigkeiten
1. **Foundation:** `.agents/product-marketing.md` (VIA product-marketing Skill)
2. **Technisch:** Meta Business Account, WhatsApp Business API-Zugang
3. **Rechtlich:** `dsgvo-lead-capture` (Consent-Layer für Broadcasts)
4. **Automation:** N8N-Zugriff für Workflow-Integration
5. **Vorher lesen:** `IMPORT/05_DACH_Marketing_Spezifika.md` Abschnitt 5.2.5

### Referenzen
- **IMPORT/05:** Abschnitt 5.2.5 (Social Commerce & Messaging)
- **Kontext:** WhatsApp dominiert B2C-Kommunikation in DACH (nicht SMS wie in US)
- **VIRON-Service-Idee:** "WhatsApp Business Automation" — Katalog, Auto-Responses, Broadcasts
- **Plattformvergleich:** TikTok Shop 2026 in DACH, aber regulatorisch gebremst

### Priorität
**P1** — Für B2C-KMUs (Einzelhandel, Dienstleister) ein dominanter Kanal. Für VIRONs primäre B2B-Ausrichtung nachrangig, aber als Service-Add-On für Kundenprojekte relevant.

---

## Skill 6: `content-authority-dach`

```yaml
name: content-authority-dach
description: >
  Content Authority Building über Fachmedien, Gastbeiträge und Networking im DACH-Raum.
  Outreach-Strategien für t3n, Kress, Horizont, OMR; Podcast-Gaststrategien,
  Webinar-Marketing-Frameworks, Case-Study-Templates für deutsche Audiences,
  Speaking-Opportunity-Identifikation (CMCX, DMEXCO, OMR Festival),
  IHK/HWK-Kooperationen, Hidden-Champion-Positionierung. Nutze diesen Skill
  für Thought Leadership und Autoritätsaufbau mit DACH-Bezug.
```

### Trigger-Phrasen
- "Thought Leadership aufbauen"
- "Fachmedien Outreach"
- "Gastbeitrag platzieren"
- "Podcast Gast werden"
- "Webinar Marketing B2B"
- "Case Study deutsch"
- "CMCX Netzwerk"
- "Hidden Champion positionieren"
- "IHK Kooperation"
- "Branchenverband Marketing"
- "Speaking Engagement DACH"
- "Content Authority Strategie"
- "Fachartikel veröffentlichen"
- "Expertenstatus aufbauen"

### Scope
- Fachmedien-Outreach-Strategie: t3n, Kress, Horizont, Werben & Verkaufen, Absatzwirtschaft
- Podcast-Gaststrategie: OMR, Marketing Mondays, weitere DACH-B2B-Podcasts
- Webinar-Marketing-Framework (höhere Teilnahmequoten in DACH als US)
- Case-Study-Templates für deutsche Audiences (Zahlen, Substanz, Transparenz)
- Speaking-Opportunity-Identifikation: CMCX, DMEXCO, OMR Festival
- IHK/HWK-Kooperationen & Branchenverband-Content
- Hidden-Champion-Positionierung ("spezialisiertes KMU mit globaler Reichweite")
- Long-form Content (Whitepapers, Studien, Reports) — DACH-Präferenz
- Datengetriebene Inhalte mit echten Daten (keine Schätzungen)
- YouTube-Content-Strategie (andere Algorithmus-Logik als US)
- Print-Digital-Hybrid: Fachzeitschriften + QR-Code-Integration
- ESG-Storytelling-Integration (LkSG-konform)

### Abhängigkeiten
1. **Foundation:** `.agents/product-marketing.md` (VIA product-marketing Skill)
2. **Content:** `DOCS/brand-voice.md`, `DOCS/icp-summary.md`
3. **Research:** ggf. `STORAGE/archive/skills/sales-enablement/SKILL.md` für Case Studies
4. **KMU-Netzwerk:** IHK/HWK-Kontakte des Kunden, Branchenverbands-Mitgliedschaften
5. **Vorher lesen:** `IMPORT/05_DACH_Marketing_Spezifika.md` Abschnitte 5.2.3, 5.2.6, 5.3.3, 5.3.4, 5.3.5

### Referenzen
- **IMPORT/05:** Abschnitte 5.2.3 (Content Marketing & Fachmedien), 5.2.6 (Print & Hybrid), 5.3.3 (Thought Leadership), 5.3.4 (ESG), 5.3.5 (Vernetzte KMU-Ökosysteme)
- **Fachmedien:** t3n, Kress, Horizont, Absatzwirtschaft
- **Konferenzen:** CMCX, OMR Festival, DMEXCO
- **VIRON-Service-Idee:** "DACH Content Authority" — Content-Plan, Podcast-Platzierungen, Webinare
- **Kulturell:** Deutsche B2B-Entscheider vertrauen auf bewiesene Expertise, Thought Leadership = Langfrist-Investition

### Priorität
**P2** — Authority Building ist ein Langfrist-Asset. Für VIRONs Eigenmarketing hochrelevant, für Kundenprojekte ab mittlerem Reifegrad. Nach P0/P1-Skills entwickeln.

---

## Implementierungs-Roadmap

| Phase | Skills | Zeitraum | Status |
|-------|--------|----------|--------|
| Phase 1 | `dsgvo-lead-capture`, `linkedin-dach-b2b`, `local-seo-gbp` | KW 22–23 | ⏳ Spezifiziert |
| Phase 2 | `german-email-marketing`, `whatsapp-business` | KW 24–25 | ⏳ Spezifiziert |
| Phase 3 | `content-authority-dach` | KW 26–27 | ⏳ Spezifiziert |

## Erweiterungspotenzial

| Skill | Beschreibung | Enthalten in |
|-------|-------------|--------------|
| `esg-marketing-mittelstand` | Impact Storytelling, LkSG-konform, B Corp | Teils in `content-authority-dach` (Abschnitt ESG) |
| `german-seo-localization` | Hreflang, DACH-Keywords, Content-Localization | Teils in `local-seo-gbp` (Abschnitt Hreflang/LocalKeywords) |
| `print-digital-hybrid` | QR-Codes, Direct Mail, Printkampagnen | Teils in `content-authority-dach` (Abschnitt Print-Hybrid) |

---

## Skill-Interdependenzen

```
dsgvo-lead-capture  ◄── depended on by ── german-email-marketing
         │                                  whatsapp-business
         │
linkedin-dach-b2b   ── uses ──► social (DOCS/skill-router.md)
                                 brand-voice (DOCS/brand-voice.md)
         │
local-seo-gbp       ── uses ──► schema (STORAGE/archive/skills/schema/)
         │
content-authority-dach ── uses ──► product-marketing
                                   sales-enablement (optional)
                                   brand-voice
```

---

*Bericht generiert: 2026-05-25 | Quelle: IMPORT/05_DACH_Marketing_Spezifika.md*
