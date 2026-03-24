# 👑 VIRON LINEAR BLUEPRINT: 100% VERBATIM EXECUTION GUIDE

Dieses Dokument ist die **exakte 1:1 Abbildung**, wie dein Linear-Workspace aufgebaut wird. Es enthält nicht nur Strategie, sondern den **wortwörtlichen Text (Markdown)**, der in die Linear-Tickets (Issues) kopiert wird – inklusive aller Notion-Links, Abhängigkeiten (Blocked By) und Labels. 

Jeder KI-Agent (oder du selbst) kann dieses Dokument nehmen und die Tickets per Copy & Paste oder API direkt in Linear einbrennen.

---

## 🏗️ TEIL 1: DIE LINEAR GRUNDSTRUKTUR (TEAMS & LABELS)

Bevor Tickets erstellt werden, muss das Fundament exakt so in Linear konfiguriert sein:

### 1. Teams (Die Säulen)
*   `[GRO]` **GROUND ZERO**: Engineering, R&D, Agenten-Bau.
*   `[MKT]` **Marketing**: Content, Video, Social Media, Freebies.
*   `[SAL]` **Sales & Outreach**: Lead Gen, Cold Email, DMs.
*   `[FUL]` **Fulfillment**: Kundenprojekte, Webdesign.
*   `[OPS]` **Operations**: Backoffice.

### 2. Globale Labels (Tags in Linear)
Lege diese Labels unter *Settings > Workspace > Labels* an:
*   `#build` (Umsetzung / Programmierung)
*   `#learn` (Recherche / Tutorial durcharbeiten)
*   `#use` (Operative Anwendung / Täglicher Task)
*   `#freebie` (Lead Magnet Erstellung)
*   `#core-system` (Kritische Infrastruktur)

---

## 🎯 TEIL 2: PROJEKT 1 - "Marketing Content Engine 2026"
**Team:** Marketing `[MKT]`
**Beschreibung:** Aufbau der vollautomatisierten Awareness- und Content-Maschine für VIRON. 
**Milestones:** 
1. `M1: Defensive & Quick Wins`
2. `M2: Video Factory`
3. `M3: Distribution & Virality`

Hier sind die exakten Issues, die in dieses Projekt gehören:

### ISSUE 1: Setup Social Media Reputation (Quick Win)
**Titel:** `[BUILD] Auto-Moderation: Negative Kommentare sofort löschen`
**Milestone:** `M1: Defensive & Quick Wins`
**Labels:** `#build`, `#freebie`
**Status:** `Todo`
**Verbatim Description (Exakt so in Linear einfügen):**
```markdown
# Ziel
Sicherung der Brand-Reputation auf Social Media durch einen automatisierten Make-Workflow, der negative Kommentare filtert und löscht. Gleichzeitig dient dieser Flow als unser erstes "Click-and-Play" Freebie für KMU-Kunden.

## 🔗 Source of Truth (Notion Asset)
* **Make-Tutorial / Notiz:** [Negative Kommentare sofort mit Automatisierung löschen](https://www.notion.so/Best-Marketing-Automations-2849129c75bf8196aa3ecac1fb92761c) *(Aus dem Make-Ordner)*

## ✅ Action Items (Sub-Issues)
- [ ] Make.com Workflow nach Vorlage aus Notion nachbauen.
- [ ] Sentiment-Analyse (OpenAI Node) für "negativ/toxisch" justieren.
- [ ] Anbindung an VIRON Instagram/Facebook Test-Account.
- [ ] Flow als JSON exportieren und als Download-Freebie in Notion verpacken.
```

### ISSUE 2: Setup Video Content Engine (Faceless & Veo3)
**Titel:** `[BUILD] Faceless POV & Veo3 Video Generator Pipeline`
**Milestone:** `M2: Video Factory`
**Labels:** `#build`, `#core-system`
**Status:** `Backlog`
**Blocked By:** Issue 1
**Verbatim Description:**
```markdown
# Ziel
Aufbau der automatisierten Video-Produktionsstraße für B-Roll, Shorts und Ads ohne manuellen Schnittaufwand.

## 🔗 Source of Truth (Notion Assets)
* **Faceless POV Creator:** [Notion Link](https://www.notion.so/2849129c75bf810d808bca0dd9e00b9e)
* **Veo3 AI Generator:** [Notion Link](https://www.notion.so/2849129c75bf81238d3beb278fe14461)
* **Video-Hook Training:** [Notion Link](https://www.notion.so/1b69129c75bf80b7aed4e3e57377f1fb)

## ✅ Action Items
- [ ] n8n-Templates für Faceless POV und Veo3 aus Notion herunterladen und in die GRO-Umgebung (Hetzner) importieren.
- [ ] API-Keys (Gemini/OpenAI) in n8n hinterlegen.
- [ ] Skript-Logik an das "Video-Hook Training" anpassen (Fokus: Organischer Feed-Hack, keine platten Ads).
- [ ] 3 Test-Videos generieren und QA (Quality Assurance) durchführen.
```

### ISSUE 3: Der Ultimative Publishing Agent
**Titel:** `[BUILD] Plattformübergreifendes Cross-Posting System`
**Milestone:** `M3: Distribution & Virality`
**Labels:** `#build`, `#core-system`
**Status:** `Backlog`
**Blocked By:** Issue 2
**Verbatim Description:**
```markdown
# Ziel
Verteilung der generierten Videos und Assets über alle Kanäle (IG, YT Shorts, LinkedIn) ohne manuellen Upload.

## 🔗 Source of Truth
* **Der Ultimative Publishing Agent:** [Notion Link](https://www.notion.so/2459129c75bf80868be1d5f05c8270b1)

## ✅ Action Items
- [ ] Agenten-Prompts ("Passe die Prompts im AI-Agent-Node bei Bedarf an") für die VIRON Brand-Voice überschreiben.
- [ ] Webhooks in n8n konfigurieren, um fertige Videos aus Issue 2 direkt in diesen Publishing-Flow zu leiten.
- [ ] API-Verbindungen zu LinkedIn und Instagram prüfen.
```

### ISSUE 4: The AI-Content Virality OS
**Titel:** `[LEARN & BUILD] Aktivierung des Virality OS (Multi-Channel Scraping)`
**Milestone:** `M3: Distribution & Virality`
**Labels:** `#learn`, `#build`, `#core-system`
**Status:** `Backlog`
**Verbatim Description:**
```markdown
# Ziel
Inbetriebnahme des massiven 7-stufigen Airtable/n8n Betriebssystems zur Trend-Identifikation. Dies ist das "Gehirn", das dem Video Generator sagt, *was* er produzieren soll.

## 🔗 Source of Truth
* **Virality OS Root:** [Notion Link](https://www.notion.so/2249129c75bf80d9a7b1c1471d23c0c3)
* **Workflow #1 (TikTok):** [Notion Link](https://www.notion.so/2249129c75bf807a9e50e401882a24e1)
* **Workflow #7 (Playbook):** [Notion Link](https://www.notion.so/2249129c75bf8011853ac6d8eb0ea24c)

## ✅ Action Items
- [ ] Airtable-Base anhand der Notion-Dokumentation ("Audience Intelligence") aufsetzen.
- [ ] n8n-Workflows 1-7 importieren und mit Airtable verknüpfen.
- [ ] Scraping-Limits (Social Channels) definieren, um API-Bans zu vermeiden.
- [ ] Testlauf: Generierung eines "Viral AI Playbooks" für die Nische "Solopreneur Automatisierung".
```

---

## 🦅 TEIL 3: PROJEKT 2 - "Sales & Akquise Maschine"
**Team:** Sales & Outreach `[SAL]`
**Beschreibung:** Conversion-Funnels, Lead-Scraping und DM-Automatisierung.
**Milestones:** 
1. `M1: Inbound Social`
2. `M2: Outbound Cold Traffic`

### ISSUE 5: Instagram Outreach System
**Titel:** `[BUILD] IG Lead Gen & Auto-DM Pipeline`
**Milestone:** `M1: Inbound Social`
**Labels:** `#build`, `#use`
**Status:** `Todo`
**Verbatim Description:**
```markdown
# Ziel
Konvertierung von Instagram-Traffic in warme Leads. Wenn User auf Reels (aus dem Marketing-Team) kommentieren, übernimmt dieses System.

## 🔗 Source of Truth
* **Instagram Outreach System:** [Notion Link](https://www.notion.so/1c39129c75bf80769a52f731d3b29ffb)

## ✅ Action Items
- [ ] Proxy-Infrastruktur aufsetzen (WICHTIG: Vermeidung von IP-Blocking, wie im Notion-Dokument referenziert).
- [ ] Manychat oder n8n-Trigger für Keyword-Erkennung (z.B. "SYSTEM") in Kommentaren konfigurieren.
- [ ] Lead-Daten (Company name, website, phone, email) automatisch aus DMs extrahieren und an das CRM übergeben.
```

### ISSUE 6: Free Apollo Lead Scraper & Cold Email
**Titel:** `[BUILD] B2B Outbound Scraping & Personalisierung`
**Milestone:** `M2: Outbound Cold Traffic`
**Labels:** `#build`, `#core-system`
**Status:** `Backlog`
**Blocked By:** Issue 5
**Verbatim Description:**
```markdown
# Ziel
Kosteneffizientes Scraping von B2B Leads ohne teures Apollo-Abo und anschließende hyper-personalisierte Kaltakquise.

## 🔗 Source of Truth
* **Free Apollo Lead Scraper:** [Notion Link](https://www.notion.so/2849129c75bf8113825dfe78d013c55a)
* **Cold Email Bulk Personalizer:** [Notion Link](https://www.notion.so/2849129c75bf81dfa05dcc9c69017cda)

## ✅ Action Items
- [ ] Apify-Scraper konfigurieren und mit Google Sheets verbinden.
- [ ] Perplexity/OpenAI Node in den "Bulk Personalizer" Flow integrieren.
- [ ] Prompt-Engineering: Die KI muss die gecrawlte Website des Leads lesen und eine Custom-Email schreiben (Fokus: "Wir bauen simple Make-Lösungen für KMUs").
- [ ] Testlauf mit 50 Dummy-Leads.
```

---

## ⚙️ TEIL 4: PROJEKT 3 - "Dev Hub Setup"
**Team:** GROUND ZERO `[GRO]`
**Beschreibung:** Interne Entwicklungsumgebung, RAG und MCP.

### ISSUE 7: AntiGravity & n8n DeepResearch
**Titel:** `[BUILD] Deterministische RAG-Pipeline (AntiGravity)`
**Labels:** `#build`, `#core-system`
**Status:** `Todo`
**Verbatim Description:**
```markdown
# Ziel
Aufbau der Master-Pipeline für tiefgreifende Recherche und fehlertolerante KI-Agenten.

## 🔗 Source of Truth
* **AntiGravity Master Prompt:** [Notion Link](https://www.notion.so/2ee9129c75bf809bb69fdc5ad6f7ceb6)
* **n8n DeepResearch:** [Notion Link](https://www.notion.so/1ad9129c75bf80cab4f0c553aa490def)
* **GraphRAG + N8N:** [Notion Link](https://www.notion.so/2719129c75bf819dbeeccb41d58064d4)

## ✅ Action Items
- [ ] Implementierung des B.L.A.S.T.-Protokolls im System-Prompt der Agenten.
- [ ] N8N MCP Server konfigurieren.
- [ ] GraphRAG Architektur für verlässliche Datenauswertung anlegen.
```
