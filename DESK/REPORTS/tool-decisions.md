# VIRON Tool-Entscheidungen — Implementierungs-Report

**Stand:** Mai 2026 | **Referenz:** IMPORT/06_Tool_Kategorien_Evaluierung.md

---

## A) Buffer vs Metricool — Social Scheduling

### Entscheidungsmatrix

| Kriterium | Buffer | Metricool |
|-----------|--------|-----------|
| Posting-Zuverlaessigkeit | Besser, weniger Bugs | Bekannte Instagram-Reel-Probleme, TikTok-Caption-Issues, API-Rate-Limiting bei Bulk-Uploads |
| Analytics/Reporting | Weniger umfangreich | PDF/PPT-Export, Competitor Tracking (bis 100 Profile), Hashtag-Analyse |
| Kosten | Free (3 Kanäle), Essentials $6/Kanal/Mo, Team $12/Kanal/Mo | Free (1 Brand/11 Kanäle, 50 Posts), Premium $18/Mo (5 Brands), Custom $45/Mo (15 Brands) |
| Agent-Freundlichkeit | API verfügbar | Webhook via n8n integrierbar |
| DSGVO | ✅ EU-Server, DSGVO-konform | ✅ EU-basiert (Spanien), DSGVO-konform |
| Lernkurve | Schnellstes Setup, intuitive UI | Steiler als Buffer |
| Support | Schneller als Metricool | Langsamer |

### Aktueller Zustand

Metricool Free-Plan ist aktiv und ausreichend (1 Brand, 50 Posts/Monat).

### Trigger fuer Entscheidung

- Metricool >50 Posts/Monat ODER >1 Brand betreut → Buffer-Evaluierung triggern
- Instagram-Reel-Fehler treten mehrfach bei Kunden auf → Sofort Buffer testen

### Hybrid-Ansatz (Zukunft)

- **Buffer:** Operatives Publishing (Zuverlaessigkeit)
- **Metricool:** Analytics, Reporting, Competitor Tracking
- **Integration:** N8N sync: Buffer Post → Metricool Analytics

### Empfehlung

Metricool jetzt nutzen (Free reicht). Buffer evaluieren wenn >1 Brand betreut wird ODER Instagram-Reel-Fehler haeufen.

---

## B) Cal.com Self-Hosted — Terminbuchung

### Warum

Keine automatisierte Terminbuchung vorhanden. Leads werden manuell per E-Mail terminiert → Zeitverlust, 21x geringere Conversion wenn nicht in 5 Minuten reagiert.

### Vergleich: Optionen im Stack

| Kriterium | Calendly | SavvyCal | Cal.com Self-Hosted |
|-----------|----------|----------|---------------------|
| Lizenz | Proprietär | Proprietär | MIT (Open Source) |
| Free Tier | ✅ (1 Event Type) | ❌ Kein Free Tier | ✅ (Unlimited Bookings) |
| Preis (Pro) | $10/Mo | $20/Mo | $0 (Self-hosted) |
| DSGVO | ✅ (US-basiert) | ✅ | ✅✅✅ Volle Datenhoheit |
| Self-Hosting | ❌ | ❌ | ✅ |
| Integrationen | Bester Oekosystem | Klein | Moderat |
| UX | Gut | Beste (Calendar Overlay) | Gut |
| N8N-Anbindung | API/Webhook | API/Webhook | API/Webhook |

### Setup

- **Stack:** Cal.diy (MIT-lizenziert) via Coolify Docker Compose auf Hetzner VPS
- **Voraussetzungen:** PostgreSQL (vorhanden), Docker, Domain (z.B. meet.viron.ai)
- **Technologie:** Next.js, TypeScript, Prisma – moderne Architektur, wartbar

### DSGVO

Self-hosted auf Hetzner (deutsches Rechenzentrum) = volle Datenhoheit, keine US-Cloud, DSGVO-konform ohne Zusatzaufwand.

### Trigger fuer Entscheidung

- Naechster Kunde mit Terminbedarf ODER LinkedIn-Profil auf Buchung ausrichten
- Oder: Interne Terminabstimmung wird zum Bottleneck (>5 manuelle Buchungen/Woche)

### Empfehlung

Cal.com self-hosted als erste Terminbuchung implementieren. DSGVO-Sicherheit ohne laufende Kosten. Bei Kunden mit hohem Vertrauensbedarf in bekannte Marken: Calendly als Client-facing Fallback mit einplanen.

---

## C) Exa AI Search — Neural/Semantic Web Search

### Was

Exa AI ist eine KI-native Websuche, die Inhalte nach Bedeutung (Vektorähnlichkeit) statt nach Keywords findet. Speziell fuer LLMs und AI-Agenten entwickelt.

### Tools (via MCP-Server)

| Tool | Funktion |
|------|----------|
| `web_search_exa` | Semantische Websuche mit Embedding-Matching |
| `web_fetch_exa` | Content-Extraktion aus URLs (clean text) |
| `web_search_advanced_exa` | Parametrisierte Suche (Datum, Domain-Filter, Autocorrect) |

### Use Cases fuer VIRON

| Use Case | Beschreibung | Beispiel |
|----------|-------------|---------|
| Content Research | Semantisch relevante Quellen fuer Pillar-Artikel finden | "Welche neuen Studien gibt es zu KI-Automatisierung im Einzelhandel?" |
| Competitor Discovery | Wettbewerber identifizieren, die aehnliche Dienstleistungen anbieten | "Finde DACH-Agenturen mit Fokus auf n8n + KMU" |
| Audience Research | Communities und Diskussionen zu Schmerzpunkten finden | "Wo beschweren sich KMU-Inhaber ueber Termin-Chaos?" |
| Trend Detection | Aufstrebende Themen im DACH-KI-Markt identifizieren | "Neue EU-Regularien zu KI im Marketing 2026" |

### Vorteile gegenüber Google/SparkToro

| Dimension | Google | SparkToro | Exa AI |
|-----------|--------|-----------|--------|
| Suchmodus | Keyword | Audience Graph | Semantisch (Embedding) |
| Agent-kompatibel | ❌ (Captcha, HTML) | ❌ (Web-UI, kein API) | ✅ (MCP, OAuth) |
| Kosten | $0 | $50/Mo (Starter) | Pay-per-use |
| Frische | Echtzeit | Index-basiert | Echtzeit |

### Integration

- **Protokoll:** Remote MCP URL `https://mcp.exa.ai/mcp`
- **Auth:** OAuth (kein API-Key noetig)
- **Abhaengigkeit:** N8N-MCP muss stehen (GROUND0-Infrastruktur)

### Trigger fuer Entscheidung

N8N-MCP-Server ist deployed und lauffaehig → Exa MCP kann eingebunden werden.

### Empfehlung

Exa AI als Agent-native Research-Engine in den Stack aufnehmen, sobald N8N-MCP steht. Bis dahin: SparkToro Free (5 Suchen/Monat) und Google Trends fuer manuelle Research nutzen.

---

## Zusammenfassung: Entscheidungs-Timeline

| Prio | Entscheidung | Status | Trigger | Blockiert durch |
|------|-------------|--------|---------|-----------------|
| 1 | Metricool Free weiternutzen | ✅ Aktiv | >1 Brand oder >50 Posts/Mo | — |
| 2 | Cal.com self-hosten | ⏳ Geplant | Naechster Kunde / LinkedIn-Profil | Docker + Domain |
| 3 | Exa AI MCP integrieren | ⏳ Geplant | N8N-MCP steht | GROUND0 MCP-Deployment |
| 4 | Buffer evaluieren | 🔮 Zukunft | >1 Brand betreut | — |
