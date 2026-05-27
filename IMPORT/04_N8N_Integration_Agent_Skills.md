# VIRON Research Report #4
# N8N-Integration mit Agent Skills: MCP-Server, Workflows & Trigger-Architektur
# Technische Implementierungsleitfaden für Marketing-Automation

---

## Executive Summary

N8N hat 2025-2026 umfassende MCP (Model Context Protocol)-Integrationen erhalten, die es ermöglichen, AI Agents direkt mit Workflow-Automation zu verbinden [web:52][web:55]. Für VIRON bedeutet dies: Marketing-Skills können nicht nur Content erstellen, sondern über N8N direkt Kampagnen ausführen, Daten sammeln und Workflows orchestrieren.

Dieser Bericht dokumentiert alle verfügbaren MCP-Nodes, Integrations-Patterns und konkrete Marketing-Workflows für den VIRON-Stack.

---

## 4.1 MCP-Ökosystem in N8N: Übersicht

### 4.1.1 Verfügbare MCP-Nodes

| Node | Typ | Funktion | Status |
|------|-----|----------|--------|
| **MCP Client Tool** [web:52] | Tool Node | Nutzt externe MCP-Tools in AI Agents | ✅ Produktion |
| **MCP Client** [web:55] | Core Node | Direkte MCP-Tool-Nutzung in Workflows | ✅ Produktion |
| **MCP Server Trigger** [web:51] | Trigger Node | Exponiert N8N-Workflows als MCP-Server | ✅ Produktion |
| **n8n-nodes-mcp** [web:50] | Community Node | Custom Node für MCP-Integration | ✅ Community |
| **n8n-mcp-server** [web:45] | External | Bridge: AI Assistants ↔ N8N Workflows | ✅ Open Source |

---

### 4.1.2 MCP Client Tool Node (AI Agent Integration)

**Dokumentation:** https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp/

**Funktion:**
Ermöglicht AI Agents in N8N, externe MCP-Server zu nutzen (z.B. Brave Search, Notion, Google Drive, GitHub) [web:52].

**Transport-Modi:**
- **SSE (Server-Sent Events):** Für Remote MCP-Endpunkte über HTTP
- **STDIO (Command-line):** Für lokale MCP-Server

**Konfiguration:**
```json
{
  "transport": "sse",
  "url": "https://mcp-server.example.com/sse",
  "auth": {
    "type": "bearer",
    "token": "{{$env.MCP_API_KEY}}"
  }
}
```

**Use Case für VIRON:**
AI Agent mit `marketing-skills` analysiert Kundenanfrage → nutzt MCP Client Tool → triggert Notion-Page-Erstellung, Slack-Benachrichtigung und Buffer-Post gleichzeitig.

---

### 4.1.3 MCP Client Node (Direct Workflow Usage)

**Dokumentation:** https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpClient/

**Funktion:**
Direkte Nutzung von MCP-Tools als reguläre Workflow-Nodes, ohne AI-Agent-Wrapper [web:55].

**Vorteile gegenüber MCP Client Tool:**
- Kein AI-Agent-Overhead (weniger Tokens)
- Direktere Kontrolle über Tool-Aufrufe
- Besser für deterministische Workflows

**Use Case für VIRON:**
Workflow: "Täglicher Social Media Report" → MCP Client ruft GA4-MCP-Server → extrahiert Daten → formatiert Report → sendet Email.

---

### 4.1.4 MCP Server Trigger Node (N8N als MCP-Server)

**Dokumentation:** https://n8n.io/integrations/mcp-server-trigger/

**Funktion:**
Exponiert N8N-Workflows als MCP-Server, die von externen AI Agents (Claude Desktop, Cursor, etc.) genutzt werden können [web:51].

**Wichtige Eigenschaft:**
- Tag Workflows mit "mcp" für automatische Discovery [web:54]
- Subworkflow-Trigger mit Input Schema definieren
- Externe Agents erkennen verfügbare Tools dynamisch

**Use Case für VIRON:**
Claude Desktop mit `marketing-skills` → erkennt N8N MCP Server → ruft "Create Campaign Workflow" auf → N8N orchestriert Multi-Step-Kampagne.

---

### 4.1.5 Community-Node: n8n-nodes-mcp

**Repository:** https://github.com/ateeyak/n8n-nodes-mcp [web:50]

**Funktion:**
Custom Node mit erweiterten MCP-Funktionen:
- SSE und STDIO Transport
- Dynamische Tool Discovery
- Erweiterte Fehlerbehandlung

**Installation:**
```bash
npm install n8n-nodes-mcp
```

**Vorteil gegenüber Builtin-Nodes:**
- Mehr Konfigurationsoptionen
- Bessere Debugging-Fähigkeiten
- Aktiver Community-Support

---

## 4.2 N8N-MCP-Server (External Bridge)

### 4.2.1 leonardsellem/n8n-mcp-server

**Repository:** https://github.com/leonardsellem/n8n-mcp-server [web:45]

**Konzept:**
Bridge zwischen AI Assistants (Claude Desktop, etc.) und N8N Workflows via Natural Language [web:46].

**Installation:**
```bash
npm install -g @leonardsellem/n8n-mcp-server
```

**Docker-Setup:**
```yaml
version: '3.8'
services:
  n8n-mcp-server:
    image: leonardsellem/n8n-mcp-server:latest
    environment:
      - N8N_HOST=https://n8n.viron.de
      - N8N_API_KEY=${N8N_API_KEY}
      - MCP_PORT=3000
    ports:
      - "3000:3000"
```

**Funktionsweise:**
1. AI Assistant (Claude) sendet natürlichsprachliche Anfrage
2. MCP Server übersetzt in N8N-Workflow-Trigger
3. N8N führt Workflow aus
4. Ergebnis wird zurück an AI Assistant übermittelt

---

### 4.2.2 n8n als MCP-Server mit AI Agent als Tool

**Workflow-Template:** https://n8n.io/workflows/4475-mcp-server-with-ai-agent-as-a-tool-context-reducer/ [web:120]

**Architektur:**
```
Externer Agent → MCP Server Trigger → N8N Workflow
                                           │
                                           ▼
                                   [Set Context Node]
                                           │
                                           ▼
                                   [AI Agent (GitHub Specialist)]
                                           │
                                           ▼
                                   [MCP Server GitHub]
                                           │
                                           ▼
                                   [Clean Result → Externer Agent]
```

**Vorteil:**
Context Reducer Pattern – komplexe MCP-Operationen werden in dedizierten Agents ausgelagert, der Haupt-Agent erhält nur das Ergebnis [web:120].

---

## 4.3 Integrations-Patterns für VIRON

### 4.3.1 Pattern A: Agent Skills → N8N Webhook Trigger

**Architektur:**
```
Claude Code (marketing-skills)
  │
  ├──> Analysiert Kunden-Anfrage
  ├──> Entscheidet: "Kampagne erstellen"
  │
  ▼
N8N Webhook Node
  │
  ├──> Trigger: "Create Marketing Campaign"
  ├──> Payload: { client_id, campaign_type, budget, channels }
  │
  ▼
N8N Workflow Orchestration
  ├──> Node 1: Create Notion Project Page
  ├──> Node 2: Generate Content (via Gemini/Claude API)
  ├──> Node 3: Schedule Posts (Buffer/Metricool)
  ├──> Node 4: Setup GA4 Tracking
  ├──> Node 5: Send Slack Notification to Team
  │
  ▼
PostgreSQL (Logging & State)
```

**Vorteile:**
- Einfach zu implementieren (Webhook = universeller Trigger)
- Agent behält Kontrolle über Strategie
- N8N übernimmt Execution

**Nachteile:**
- Keine bidirektionale Kommunikation (Agent weiß nicht, ob Workflow erfolgreich war)
- Manueller Retry bei Fehlern

---

### 4.3.2 Pattern B: N8N MCP Server ←→ Claude Desktop

**Architektur:**
```
Claude Desktop (mit marketing-skills)
  │
  ├──> Erkennt: "Ich brauche N8N-Workflows"
  ├──> MCP Discovery: Listet verfügbare N8N-Tools
  │
  ▼
MCP Server Trigger (N8N)
  │
  ├──> Tool: "Create Social Campaign"
  ├──> Tool: "Generate Weekly Report"
  ├──> Tool: "Update Client Dashboard"
  │
  ▼
N8N Workflow Execution
  ├──> Autonome Ausführung
  ├──> Ergebnis-Rückmeldung via MCP
  │
  ▼
Claude Desktop
  ├──> Erhält Ergebnis
  ├──> Präsentiert Kunden-Ergebnis
```

**Vorteile:**
- Bidirektionale Kommunikation
- Dynamische Tool Discovery
- Natürlichsprachliche Steuerung

**Nachteile:**
- Komplexeres Setup
- Claude Desktop erforderlich (nicht Headless)

---

### 4.3.3 Pattern C: Multi-Agent mit N8N als Message Bus

**Architektur (aus N8N Community) [web:117]:**
```
Agent 1 (Content Strategist)
  │
  ├──> MCP Client Tool
  ├──> Sendet: "Neuer Content-Plan benötigt"
  │
  ▼
MCP Trigger (N8N Channel: "content-planning")
  │
  ├──> Weiterleitung an Agent 2
  │
  ▼
Agent 2 (Copywriter)
  ├──> Empfängt: Content-Plan
  ├──> Erstellt: Copy
  ├──> Sendet: "Copy fertig"
  │
  ▼
MCP Trigger (N8N Channel: "copy-review")
  │
  ▼
Agent 3 (Reviewer)
  ├──> Empfängt: Copy
  ├──> Review + Approval
  ├──> Sendet: "Approved"
  │
  ▼
MCP Trigger (N8N Channel: "publish")
  │
  ▼
N8N Publish Workflow
  ├──> Buffer API: Schedule Posts
  ├──> Notion: Update Status
  ├──> Slack: Team Notification
```

**Vorteile:**
- Echte Multi-Agent-Orchestrierung
- N8N als zentraler Message Bus
- Keine externen Broker nötig [web:117]

**Nachteile:**
- Komplexe Fehlerbehandlung
- Session-Management erforderlich

---

## 4.4 Konkrete Marketing-Workflows für VIRON

### 4.4.1 Workflow 1: Automated Content Pipeline

**Trigger:** AI Agent entscheidet "Content erstellen"

**N8N Workflow:**
```
[Webhook Trigger: Content Request]
  │
  ▼
[Set Node: Extract Parameters]
  ├──> topic, channel, tone, client_id
  │
  ▼
[HTTP Request: Gemini API]
  ├──> Generate Content Draft
  │
  ▼
[HTTP Request: Claude API (Fallback)]
  ├──> Quality Review & Refinement
  │
  ▼
[Buffer Node: Schedule Post]
  ├──> LinkedIn / X / Facebook
  │
  ▼
[Notion Node: Archive Content]
  ├──> Add to Content Calendar
  │
  ▼
[PostgreSQL Node: Log Entry]
  ├──> content_id, status, metrics
  │
  ▼
[Slack Node: Team Notification]
  ├──> "Content published: [Topic]"
```

**Ergebnis:**
End-to-End Content Creation und Publishing ohne manuelle Intervention.

---

### 4.4.2 Workflow 2: Competitor Monitoring & Alerting

**Trigger:** Schedule (täglich 08:00 Uhr)

**N8N Workflow:**
```
[Schedule Trigger: Daily 08:00]
  │
  ▼
[HTTP Request: SimilarWeb API]
  ├──> Competitor Traffic Data
  │
  ▼
[HTTP Request: SparkToro API]
  ├──> Competitor Audience Changes
  │
  ▼
[Function Node: Analyze Changes]
  ├──> Delta Detection (±10% Threshold)
  │
  ▼
[If Node: Significant Change?]
  ├──> Yes → Continue
  ├──> No → Stop
  │
  ▼
[Gemini Node: Generate Insights]
  ├──> "Competitor X traffic +15%, likely due to Y"
  │
  ▼
[Notion Node: Update Competitor DB]
  │
  ▼
[Slack Node: Alert Team]
  ├──> "🚨 Competitor Alert: [Details]"
  │
  ▼
[Linear Node: Create Ticket]
  ├──> "Review competitor strategy"
```

---

### 4.4.3 Workflow 3: GEO Content Optimization Pipeline

**Trigger:** AI Agent oder Schedule (wöchentlich)

**N8N Workflow:**
```
[Trigger: GEO Optimization Request]
  │
  ▼
[PostgreSQL Node: Fetch Underperforming Content]
  ├──> Pages with declining organic traffic
  │
  ▼
[HTTP Request: Perplexity API]
  ├──> "What questions does AI answer about [topic]?"
  │
  ▼
[Gemini Node: GEO Optimization]
  ├──> Restructure content for AI search
  ├──> Add FAQ schema
  ├──> Add conversational Q&A sections
  │
  ▼
[HTTP Request: Website CMS API]
  ├──> Update content
  │
  ▼
[PostgreSQL Node: Log Optimization]
  ├──> content_id, changes, date
  │
  ▼
[Slack Node: Notify Team]
  ├──> "GEO optimization complete for [X pages]"
```

---

### 4.4.4 Workflow 4: Lead Scoring & Routing

**Trigger:** Form Submission oder CRM-Event

**N8N Workflow:**
```
[Webhook Trigger: New Lead]
  │
  ▼
[PostgreSQL Node: Enrich Data]
  ├──> Firmographics, Behavior, Source
  │
  ▼
[Gemini Node: AI Lead Scoring]
  ├──> Score 0-100 basierend auf: Company Size, Job Title, 
  │     Website Activity, Email Engagement
  │
  ▼
[If Node: Score > 70?]
  ├──> Yes → [Cal.com Node: Book Meeting]
  ├──> No → [Email Node: Nurture Sequence]
  │
  ▼
[HubSpot/Notion Node: Update CRM]
  │
  ▼
[Slack Node: Sales Notification (nur High-Score)]
```

---

### 4.4.5 Workflow 5: UGC Video Generation & Publishing

**Trigger:** AI Agent Content-Plan

**N8N Workflow (basierend auf [web:98][web:101]):**
```
[Trigger: Video Campaign Request]
  │
  ▼
[Gemini Node: Script Generation]
  ├──> UGC-Style Script mit CTA
  │
  ▼
[HTTP Request: Veo3 / Kling / Sora 2 API]
  ├──> Video Generation
  │
  ▼
[HTTP Request: ElevenLabs API]
  ├──> Voiceover (German)
  │
  ▼
[FFmpeg Node: Video Assembly]
  ├──> Combine video + audio + subtitles
  │
  ▼
[Buffer/Metricool Node: Multi-Platform Publishing]
  ├──> TikTok, Instagram Reels, YouTube Shorts
  │
  ▼
[PostgreSQL Node: Campaign Log]
  │
  ▼
[Slack Node: "Video Campaign Live"]
```

---

## 4.5 DSGVO-konforme Implementierung

### 4.5.1 Data Flow Mapping

**Jeder Workflow muss dokumentieren:**
- Welche Daten werden verarbeitet? (Art. 30 DSGVO)
- Wo werden Daten gespeichert? (Hetzner = EU-Server ✅)
- Wer hat Zugriff? (Role-Based Access)
- Wie lange werden Daten aufbewahrt? (Retention Policies)

### 4.5.2 Technical Measures

| Measure | Implementation |
|---------|---------------|
| Encryption at Rest | PostgreSQL SSL, Hetzner Storage |
| Encryption in Transit | HTTPS/TLS für alle APIs |
| Access Control | N8N User Roles, API Key Rotation |
| Logging | Audit Trail in PostgreSQL |
| Data Minimization | Nur notwendige Felder verarbeiten |
| Right to Deletion | Automatisierte Lösch-Workflows |

### 4.5.3 N8N-Specific DSGVO Features

- **Execution Data:** Automatisch löschen nach X Tagen
- **Error Workflows:** Keine PII in Error Logs
- **Credentials:** Secure Storage in N8N Credential Vault
- **Webhook URLs:** Rotierende URLs mit Auth-Token

---

## 4.6 VIRON-MCP-Integrations-Roadmap

### Phase 1: Foundation (Woche 1-2)
- [ ] MCP Client Node in N8N aktivieren
- [ ] Verbindung zu Notion MCP Server testen
- [ ] Verbindung zu Slack MCP Server testen
- [ ] Ersten Webhook-Trigger-Workflow erstellen

### Phase 2: Core Workflows (Woche 3-4)
- [ ] Workflow 1 (Content Pipeline) implementieren
- [ ] Workflow 4 (Lead Scoring) implementieren
- [ ] PostgreSQL-Logging für alle Workflows einrichten

### Phase 3: Advanced Patterns (Monat 2)
- [ ] MCP Server Trigger Node aktivieren
- [ ] Claude Desktop ↔ N8N bidirektionale Verbindung testen
- [ ] Multi-Agent Pattern (Pattern C) prototypen

### Phase 4: Optimization (Monat 3)
- [ ] Performance-Monitoring für alle Workflows
- [ ] Error-Handling & Retry-Logic verfeinern
- [ ] Token-Cost-Tracking pro Workflow

---

## 4.7 Troubleshooting & Best Practices

### 4.7.1 Häufige Fehler

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| MCP Server nicht erreichbar | Port/URL falsch | SSE URL prüfen, Firewall-Regeln checken |
| Tool Discovery schlägt fehl | Auth-Problem | API Key/Token erneuern |
| Workflow hängt | Rate Limiting | Retry-Logic mit Exponential Backoff |
| Context zu groß | Zu viele Skills geladen | Lazy Loading implementieren |

### 4.7.2 Performance-Tuning

- **Batch Processing:** Mehrere Items in einem Workflow-Durchlauf verarbeiten
- **Code Node statt HTTP Request:** Für einfache Transformationen schneller
- **Connection Pooling:** PostgreSQL-Verbindungen wiederverwenden
- **Workflow Deactivation:** Ungenutzte Workflows deaktivieren

---

*Bericht generiert: Mai 2026*
