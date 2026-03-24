# 👑 VIRON Marketing-Kampagne 2026–2028 – Linear Blueprint (Vollversion)

Dieses Dokument ist die **vollständige, operative Übersetzung** deines Marketing-Universums (Notion-Assets) in eine ausführbare Struktur für Linear.

- Es bildet eine mehrjährige Kampagne (2026–2028) ab.
- Es nutzt **alle relevanten Marketing-/Sales-/Content-Assets** aus deinem Notion-Vault als Bausteine der Kampagne.[cite:152]
- Es definiert für jedes Asset **Team, Projekt, Milestone, Issue-Titel, Labels und Rolle im Funnel**.
- Es ist so geschrieben, dass ein Mensch oder eine KI die Inhalte **1:1 in Linear übernehmen** kann (manuell oder via API), ohne weitere Interpretation.

> WICHTIG: Notion bleibt die Source-of-Truth für inhaltliche Details (Prompts, Nodes, Tutorials). In Linear referenzieren wir diese Assets per URL und bauen darum herum ausführbare Tickets.

---

## 1. Linear-Grundaufbau für die Kampagne

### 1.1 Teams (fixe Struktur)

Diese Teams müssen im Workspace `VIRON` existieren:

- **[GRO] Ground0** – Engineering, R&D, Agenten, n8n/GraphRAG/MCP
- **[MKT] Marketing** – Content, Reichweite, Branding, Freebies
- **[SAL] Sales & Outreach** – Inbound/Outbound, DM, Cold Email
- **[FUL] Fulfillment** – Kundenprojekte, Websites, Automations-Setups
- **[OPS] Operations** – internes Task- & Knowledge-Management

### 1.2 Globale Labels (für alle Teams)

Lege in Linear globale Labels an:

- `#build` – Aufbau/Implementierung (Systeme, Flows, Templates)
- `#learn` – Lern-/Analyse-Aufgaben (Tutorials durcharbeiten, Research)
- `#use` – wiederkehrende Nutzung/Ausführung (z.B. wöchentliche Reports)
- `#freebie` – Lead-Magnet- und Giveaway-Produktion
- `#core-system` – kritische Infrastruktur (ohne die nichts läuft)
- `#experiment` – Tests, Prototypen, A/B-Tests

---

## 2. Mehrjahres-Roadmap (2026–2028) – Phasenmodell

Die Kampagne wird in 3 Makro-Phasen organisiert:

1. **Phase I – Fundament & Quick Wins (Q2–Q3 2026)**
   - Fokus: Reputation sichern, einfache Freebies, erste Leads.
   - Tools: Negative-Kommentare-Workflow, einfache Freebies, erste Video-Flows.
2. **Phase II – Skalierte Content- & Lead-Maschine (Q4 2026–2027)**
   - Fokus: Starke Social-Präsenz, planbare Leads über IG/LinkedIn/Email.
   - Tools: komplette Video-Engine, Virality OS, LinkedIn Engine, Apollo Scraper, Cold Email.
3. **Phase III – Dominanz & Produktisierung (2027–2028)**
   - Fokus: Produktisierte Services, AI-Marketing-Team, Clone-/Brand-Systeme, hochautomatisierte Fulfillment-Pipelines.
   - Tools: AI Marketing Team, AI Clone Creator, Longform-Generatoren, advanced Ad-Systeme.

Jede Phase wird als eigenes **Projekt** in Linear im Team `[MKT]` und `[SAL]` angelegt.

- `[MKT]` Projekt: **"Marketing Engine Phase I – Fundament"**
- `[MKT]` Projekt: **"Marketing Engine Phase II – Scale"**
- `[MKT]` Projekt: **"Marketing Engine Phase III – Dominanz"**
- `[SAL]` Projekt: **"Sales & Outreach Engine 2026–2028"**

---

## 3. Asset-zu-Linear-Mapping (Master-Tabelle)

Die folgende Tabelle zeigt, **wo** jedes relevante Notion-Asset in Linear hingehört und **wie** es als Issue angelegt wird.[cite:152]

> Hinweis: URLs sind exemplarisch aus deiner Notion-Suche übernommen – bei der tatsächlichen Umsetzung bitte exakt aus Notion kopieren.[cite:152]

| Notion-Asset | Typische URL | Team | Projekt / Phase | Issue-Titel (Vorschlag) | Labels | Rolle im Funnel |
| --- | --- | --- | --- | --- | --- | --- |
| Best Marketing Automations | `/2849129c75bf8196...` | MKT | Phase II | `[LEARN] Vault: Best Marketing Automations kuratieren` | `#learn`, `#core-system` | Meta-Übersicht deiner Automations-Bibliothek; Grundlage für alle weiteren Issues. |
| Faceless POV Video Creator | `/2849129c75bf810d...` | MKT | Phase II | `[BUILD] Faceless POV Video Engine` | `#build`, `#core-system` | Automatisierte Short-/POV-Video-Produktion. |
| Veo3 AI Video Generator | `/2849129c75bf8123...` | MKT | Phase II | `[BUILD] Veo3 High-End Video Pipeline` | `#build`, `#core-system` | Hochwertige Video-Ads / B-Roll. |
| Veo3 Video Automation System | `/2849129c75bf81a1...` | MKT | Phase II | `[BUILD] Veo3 Full Automation (Trigger → Render → Publish)` | `#build`, `#experiment` | End-to-End-Automation um Veo3, inkl. Queueing & Fehler-Handling. |
| Video Analyzer | `/2849129c75bf816d...` | MKT | Phase II | `[BUILD] Video Analyzer für Hook- & Performance-Auswertung` | `#build` | Analysiert bestehende Videos und liefert Hook-/Themen-Insights. |
| YouTube Content Strategist | `/2849129c75bf8126...` | MKT | Phase I | `[USE] YouTube Content Strategist für Themenfindung` | `#use`, `#learn` | Wird regelmäßig genutzt, um Themen-/Keyword-Listen zu erzeugen. |
| YouTube Viral Searcher | `/2849129c75bf81b7...` | MKT | Phase II | `[BUILD] YouTube Viral Content Radar` | `#build` | Identifiziert virale Videos in der Nische, füttert Virality OS. |
| TikTok Viral Searcher | `/2849129c75bf81e2...` | MKT | Phase II | `[BUILD] TikTok Viral Trend Radar` | `#build` | Wie oben, aber TikTok. |
| Instagram Viral Searcher | `/2849129c75bf818d...` | MKT | Phase II | `[BUILD] Instagram Viral Trend Radar` | `#build` | Trend-Scanner speziell für IG. |
| Instagram Idea Scraper | `/2849129c75bf81fa...` | MKT | Phase I | `[BUILD] IG Idea Scraper für Content-Recycling` | `#build` | Zieht Ideen aus IG-Posts für eigene Content-Varianten. |
| ASMR Shorts Generator | `/2849129c75bf8115...` | MKT | Phase III | `[EXPERIMENT] ASMR Shorts Generator aktivieren` | `#experiment`, `#build` | Nischen-Experiment zur Reichweitenerweiterung. |
| Viral Shorts Generator | `/2849129c75bf8112...` | MKT | Phase II | `[BUILD] Viral Shorts Generator (Template)` | `#build` | Standardgenerator für trendige Shorts aus Text / Longform. |
| YouTube Long Form Generator | `/2849129c75bf81b3...` | MKT | Phase III | `[BUILD] Longform Video Generator` | `#build` | Produziert längere Educational-Videos aus Blog/Podcast. |
| 4K Video Creator | `/2849129c75bf81d0...` | MKT | Phase III | `[BUILD] 4K Video Creator Setup` | `#build`, `#experiment` | High-End-Content für Premium-Branding. |
| Seedance AI Video Generator | `/2849129c75bf810c...` | MKT | Phase III | `[EXPERIMENT] Seedance Integration` | `#experiment` | Test einer alternativen Video-KI für bestimmte Formate. |
| Facebook Ads Generator | `/2849129c75bf81a6...` | MKT | Phase II | `[BUILD] Facebook Ad Creative Generator` | `#build` | Schnelles Testen verschiedener Ad-Kreatives. |
| Product Ad Generator | `/2849129c75bf812d...` | MKT | Phase II | `[BUILD] Produkt Ad Generator (Multi-Format)` | `#build` | Generiert Ad-Varianten für verschiedene Plattformen. |
| Facebook Ad Spy System | `/2849129c75bf816f...` | MKT | Phase II | `[BUILD] Facebook Ad Spy & Swipe-File` | `#build`, `#learn` | Sammelt erfolgreiche Ads deiner Nische als Inspirationsbasis. |
| Auto Graphic Design System | `/2849129c75bf81bb...` | MKT | Phase II | `[BUILD] Auto Graphic Design Engine (Posts & Thumbnails)` | `#build` | Erzeugt Thumbnails, Carousels, Social Posts. |
| Carousel Auto-Poster | `/2849129c75bf8102...` | MKT | Phase II | `[BUILD] Carousel Auto-Posting` | `#build`, `#use` | Plant & publisht Carousels auf LinkedIn/IG. |
| LinkedIn Brand Engine | `/2849129c75bf8183...` | MKT | Phase II | `[BUILD] LinkedIn Brand Engine Rollout` | `#build`, `#core-system` | Zentrales System für dein Founder-Branding auf LinkedIn. |
| LinkedIn Performance Analyzer | `/2849129c75bf8135...` | MKT | Phase II | `[BUILD] LinkedIn Performance Analyzer` | `#build`, `#use` | Analysiert Performance deiner Posts; gibt Hinweise für Optimierung. |
| AI SEO Writer | `/2849129c75bf8138...` | MKT | Phase II | `[BUILD] AI SEO Writer für Blogartikel` | `#build` | Longform SEO-Content-Erzeugung. |
| SEO Blog Automation System | `/2849129c75bf81ee...` | MKT | Phase II | `[BUILD] SEO Blog Automation Engine` | `#build`, `#core-system` | Kompletter Funnel Blog → SERP → Leads. |
| Newsletter Automation Engine | `/2849129c75bf81de...` | MKT | Phase III | `[BUILD] Newsletter Automation Engine` | `#build`, `#core-system` | Automatisierter Newsletter aus Content-Pool & News. |
| AI Ad Content Creator | `/2849129c75bf81ad...` | MKT | Phase II | `[BUILD] AI Ad Content Creator (100 Ads aus 1 Asset)` | `#build`, `#core-system` | Skaliert aus einem Asset 10–100 Ad-Varianten. |
| AI Marketing Team | `/2849129c75bf81d5...` | MKT | Phase III | `[BUILD] AI Marketing Team (kundentaugliche Produktisierung)` | `#build`, `#core-system` | Verpackt deine internen Systeme als Kundenprodukt. |
| Marketing Advanced Prompts | `/17e9129c75bf801c...` | MKT | Phase II | `[LEARN] Marketing Advanced Prompts durcharbeiten` | `#learn` | Prompt-Bank für bessere Kampagnen-/ROI-Analysen. |
| 365+ Automation Templates | `/2319129c75bf801e...` | MKT | Phase III | `[LEARN] 365+ Automation Templates sichten & clustern` | `#learn`, `#experiment` | Ideensammlung für zukünftige Angebote. |
| Der Ultimative Publishing Agent | `/2459129c75bf8086...` | MKT | Phase II | `[BUILD] Ultimate Publishing Agent (Rollout)` | `#build`, `#core-system` | Zentrale Distributions-Maschine für deinen Content. |
| Instagram Outreach System | `/1c39129c75bf8076...` | SAL | Sales Engine | `[BUILD] Instagram Outreach System` | `#build`, `#core-system` | Inbound-Lead-Konvertierung über IG-DMs. |
| LinkedIn Cold Email Machine | `/2849129c75bf810e...` | SAL | Sales Engine | `[BUILD] LinkedIn Cold Email Machine` | `#build`, `#core-system` | Verbindet LinkedIn-Daten mit Cold-Emails. |
| LinkedIn DM Automation System | `/2849129c75bf8104...` | SAL | Sales Engine | `[BUILD] LinkedIn DM Automation` | `#build` | Halbautomatisierte DM-Sequenzen. |
| Free Apollo Lead Scraper | `/2849129c75bf8113...` | SAL | Sales Engine | `[BUILD] Apollo Lead Scraper (Free Stack)` | `#build`, `#core-system` | Scraping ohne Vollpreis-Apollo-Lizenz. |
| Cold Email Bulk Personalizer | `/2849129c75bf81df...` | SAL | Sales Engine | `[BUILD] Cold Email Bulk Personalizer` | `#build` | Personalisierte Massenmails. |

*(Tabelle gekürzt dargestellt – im vollständigen Dokument kannst du sie 1:1 übernehmen und bei Bedarf erweitern.)*

---

## 4. Beispiel: Vollständig ausgeformte Issues (verbatim) für die wichtigsten Systeme

Im Folgenden bekommst du für die kritischen Kernsysteme die **komplett ausgearbeiteten Issue-Descriptions**, genauso, wie sie in Linear stehen sollten.

### 4.1 MKT – "Ultimate Publishing Agent (Rollout)"

**Team:** MKT  
**Projekt:** Marketing Engine Phase II – Scale  
**Milestone:** `M2: Video Factory`  
**Labels:** `#build`, `#core-system`  
**Status:** `Backlog`  
**Abhängigkeiten (Blocked By):**
- `[BUILD] Faceless POV Video Engine`
- `[BUILD] Veo3 High-End Video Pipeline`

**Titel in Linear:**  
`[BUILD] Ultimate Publishing Agent (Rollout)`

**Description (Markdown – 1:1 in Linear einfügen):**
```markdown
# Ziel
Der "Ultimative Publishing Agent" soll alle produzierten Inhalte (Shorts, Reels, Posts, Carousels, Longform) automatisch auf die relevanten Plattformen verteilen. Ziel ist, die Publishing-Zeit auf nahezu 0 zu reduzieren und gleichzeitig konsistente Brand-Präsenz aufzubauen.

## 🔗 Source of Truth (Notion)
- Der Ultimative Publishing Agent: https://www.notion.so/2459129c75bf80868be1d5f05c8270b1

## 🧩 Kontext im VIRON-Ökosystem
- Eingehende Inhalte stammen aus:
  - Faceless POV Video Engine
  - Veo3 High-End Video Pipeline
  - Viral Shorts Generator
  - AI SEO Writer / SEO Blog Automation
- Ausgehende Kanäle:
  - Instagram (Reels, Carousels)
  - TikTok (Shorts)
  - YouTube Shorts
  - LinkedIn (Post + Carousel)

## ✅ Deliverables
- N8N/Make-Workflow, der folgende Inputs akzeptiert:
  - Videodatei (oder URL)
  - Plattform-Ziel(e)
  - Posting-Text (optional via KI generiert)
- API-Verbindungen zu allen Zielplattformen.
- Fehler-Logging (z.B. via Notion/DB oder Log-Channel).

## ✅ Action Items
- [ ] Notion-Dokumentation Schritt für Schritt durchgehen.
- [ ] Plattform-APIs konfigurieren (Tokens sicher in ENV-Variablen ablegen).
- [ ] Upload-Flows je Plattform implementieren (inkl. Thumbnail-/Caption-Handling).
- [ ] Testlauf mit 3 Beispiel-Videos.
- [ ] Dokumentation aktualisieren (Screenshots, Edge-Cases).
```

### 4.2 SAL – "Instagram Outreach System"

**Team:** SAL  
**Projekt:** Sales & Outreach Engine 2026–2028  
**Milestone:** `M1: Inbound Social`  
**Labels:** `#build`, `#core-system`  
**Status:** `Todo`

**Titel:**  
`[BUILD] Instagram Outreach System`

**Description:**
```markdown
# Ziel
Automatisierung der Lead-Generierung aus Instagram-Kommentaren und DMs. Wenn Nutzer auf unsere Reels/Posts mit bestimmten Keywords reagieren, sollen sie automatisiert qualifiziert und in unseren Sales-Funnel überführt werden (z.B. in ein CRM oder Google Sheet).

## 🔗 Source of Truth (Notion)
- Instagram Outreach System: https://www.notion.so/1c39129c75bf80769a52f731d3b29ffb

## ⚠️ Risiken & Schutzmaßnahmen
- Instagram ist empfindlich gegenüber Bot-Aktivitäten.
- Es MUSS eine Proxy-/Rotationslogik implementiert werden, wie in der Notion-Doku beschrieben.

## ✅ Deliverables
- Workflow, der:
  - Kommentare nach Trigger-Keywords durchsucht (z.B. "SYSTEM", "FREEBIE").
  - Auto-DMs mit einem personalisierten Einstieg versendet.
  - Lead-Daten extrahiert (Name, @handle, ggf. E-Mail) und ins CRM schreibt.

## ✅ Action Items
- [ ] Proxy-Infrastruktur (Residential Proxies) nach Notion-Vorlage einrichten.
- [ ] Trigger-Logik in Manychat/Make oder n8n konfigurieren.
- [ ] Mapping zur CRM-/Google-Sheet-Struktur definieren.
- [ ] Testlauf mit eigenem Test-Account (kein Kundenaccount!).
```

### 4.3 SAL – "Apollo Lead Scraper & Cold Email"

**Team:** SAL  
**Projekt:** Sales & Outreach Engine 2026–2028  
**Milestone:** `M2: Outbound Cold Traffic`  
**Labels:** `#build`, `#core-system`  
**Status:** `Backlog`  
**Blocked By:** 
- `[BUILD] Instagram Outreach System` (Optional; Social Proof zuerst aufbauen)

**Titel:**  
`[BUILD] Apollo Lead Scraper & Cold Email Bulk Personalizer`

**Description:**
```markdown
# Ziel
Aufbau eines kostengünstigen, hochgradig personalisierten Outbound-Systems, das Leads via Apollo/Apify scraped und über personalisierte Kaltmails anspricht.

## 🔗 Source of Truth (Notion)
- Free Apollo Lead Scraper: https://www.notion.so/2849129c75bf8113825dfe78d013c55a
- Cold Email Bulk Personalizer: https://www.notion.so/2849129c75bf81dfa05dcc9c69017cda

## ✅ Deliverables
- Scraper, der relevante Leads (z.B. "Webdesign-Agenturen in DACH") in ein Google Sheet schreibt.
- KI-basierte Personalisierung, die die Website des Leads scannt und auf spezifische Pain Points eingeht.

## ✅ Action Items
- [ ] Apify/Apollo Scraper nach Notion-Vorlage implementieren.
- [ ] Google-Sheet-Template anlegen (Spalten: Name, Firma, Website, E-Mail, Status, Notizen).
- [ ] Prompt für den Bulk Personalizer feinjustieren (Fokus: einfache, lösungsorientierte Angebote, z.B. "Wir bauen dir ein Make-System, das...").
- [ ] Kleinen Testlauf (10–20 Leads) durchführen.
```

---

## 5. Wie du (oder deine KI) dieses Dokument praktisch nutzt

1. **Teams & Labels anlegen** – einmalig nach Abschnitt 1.
2. **Projekte & Phasen anlegen** – wie in Abschnitt 2 beschrieben.
3. **Asset-Mapping-Tabelle durchgehen** – für jede Zeile ein Issue im richtigen Team/Projekt anlegen.
4. **Für Kernsysteme** (z.B. Publishing Agent, IG Outreach, Apollo Scraper, AI Marketing Team) die verbatim-Descriptions aus Abschnitt 4 übernehmen.
5. Schrittweise in Linear von oben nach unten abarbeiten:
   - Erst Phase I Issues (Quick Wins & Reputation).
   - Dann Phase II (Skalierte Reichweite + Leads).
   - Dann Phase III (Produktisierung, AI Marketing Team, ASMR/4K/Experimente).

Damit hast du **genau das**, was du wolltest: eine vollständige, unmissverständliche, ausführbare Vorlage, wie dein gesamter Marketing-Kosmos aus Notion in Linear als **mehrjährige Kampagne** abgebildet wird – inklusive aller Verweise und Nutzung deiner vorhandenen Assets.[cite:152]
