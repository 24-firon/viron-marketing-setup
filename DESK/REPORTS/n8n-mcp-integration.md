# N8N-MCP-Integration — Implementierungs-Report

**Stand:** 2026-05-25 | **Status:** Planung (n8n nicht aktiv) | **Quelle:** IMPORT/04_N8N_Integration_Agent_Skills.md

---

## 1. Was: N8N-MCP in opencode.jsonc einbinden

### Definition

N8N hat 2025-2026 vollständige MCP (Model Context Protocol)-Integration erhalten. MCP ist das **Standardprotokoll für KI-Agenten-Tool-Anbindung** — vergleichbar mit USB-C für Peripheriegeräte, nur für KI-Werkzeuge.

Für VIRON bedeutet die N8N-MCP-Integration konkret:

- **N8N als MCP-Server:** Workflows werden als Tools für externe KI-Agenten bereitgestellt. Claude (als Orchestrator) kann Workflows direkt triggern, ohne manuelle Webhook-Konfiguration.
- **N8N als MCP-Client:** N8N-AI-Agent-Nodes können externe MCP-Tools nutzen (Notion, Slack, GitHub, Brave Search) und in automatisierte Workflows einbinden.
- **Bidirektionale Kommunikation:** Der Agent erhält Ergebnisse aus den Workflows zurück — kein "Fire and Forget" mehr.

### Warum das der Game-Changer für VIRON ist

| Vorher (ohne MCP) | Nachher (mit MCP) |
|---|---|
| Agent entscheidet → manuelles Erstellen eines Webhooks | Agent entdeckt Workflows automatisch via Tool Discovery |
| Keine Rückmeldung: "Wurde der Post eigentlich gepostet?" | Bidirektional: Workflow meldet Status + URL zurück |
| Pro Workflow: separater Webhook, separate Auth | Ein MCP-Endpunkt, alle Workflows, eine Auth |
| Kein Standard für den Stack | MCP ist der aufkommende Branchenstandard (Anthropic, OpenAI, Google) |

VIRONs Marketing-Skills werden von **Content-Produzenten** zu **Marketing-Ausführern**. Ein `marketing-skills` Agent erstellt nicht nur den Content, sondern publishiert, tracked und reportet — alles über N8N-MCP.

---

## 2. Voraussetzungen

### Hard Requirements

| Voraussetzung | Status | Anmerkung |
|---|---|---|
| **n8n läuft auf Hetzner** (self-hosted, Docker) | **Nicht aktiv** | n8n-Deployment muss VOR MCP-Integration stehen |
| **n8n API-Zugang** konfiguriert | **Nicht aktiv** | API-Key muss generiert und in `.env` hinterlegt sein |
| **HTTPS/SSL** für n8n-Instanz | **Nicht aktiv** | Let's Encrypt auf Hetzner. MCP-SSE erfordert HTTPS |
| **n8n-nodes-mcp** Community Node installiert | **Nicht aktiv** | `npm install n8n-nodes-mcp` im n8n-Container |
| **MCP Transport Mode** gewählt | **Offen** | Entscheidung: SSE vs. STDIO |

### Transport-Mode-Entscheidung

| Modus | Vorteile | Nachteile | Empfehlung für VIRON |
|---|---|---|---|
| **SSE** (HTTP/Server-Sent Events) | Remote-fähig, kein Command-line-Setup | Latenz bei 100+ Tools | **Primary** — Hetzner ↔ Remote-Agent |
| **STDIO** (Command-line) | Lokal, schnell, kein Netzwerk | Nur Localhost, Docker-Komplexität | **Fallback** — lokale Tests |

**Entscheidung:** SSE ist der Standard für VIRON, da n8n auf einem Remote-Hetzner-Server läuft und von mehreren Agenten gleichzeitig erreicht werden muss.

---

## 3. Konkrete Schritte (durchnummeriert)

### Schritt 1: opencode.jsonc mit MCP-Server konfigurieren

```jsonc
{
  // ... bestehende Konfiguration (permission, skills, instructions) ...

  "mcpServers": {
    "n8n-viron": {
      "type": "sse",
      "url": "https://n8n.viron.de/mcp/sse",
      "headers": {
        "Authorization": "Bearer ${N8N_API_KEY}"
      }
    }
  }
}
```

**Erklärung:**
- `n8n-viron` — Eindeutiger Name für den MCP-Server (referenzierbar in Skills)
- `type: "sse"` — Transport über Server-Sent Events (HTTP)
- `url` — MCP-SSE-Endpunkt der n8n-Instanz auf Hetzner
- `headers.Authorization` — API-Key aus Umgebungsvariable `${N8N_API_KEY}`
- Zusätzliche Server können parallel eingebunden werden (Notion, Slack, GitHub)

**Hinweis:** Die exakte URL hängt vom konfigurierten Pfad in der `n8n-mcp-server` Node ab. Standard: `https://<n8n-host>/mcp/sse`.

### Schritt 2: MCP Client Node in n8n installieren

Auf dem Hetzner-Server, im n8n-Docker-Container:

```bash
# Container betreten
docker exec -it n8n /bin/sh

# Community Node installieren
npm install n8n-nodes-mcp

# n8n neu starten
exit
docker restart n8n
```

Alternativ als Environment-Variable in `docker-compose.yml`:

```yaml
services:
  n8n:
    environment:
      - N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
      - N8N_NODES_INCLUDE=n8n-nodes-mcp
```

**Nach der Installation** erscheinen in der n8n-Node-Palette:
- **MCP Client Tool** (als Sub-Node unter AI Agent)
- **MCP Client** (als Core Node für direkte Nutzung)
- **MCP Server Trigger** (als Trigger Node)

### Schritt 3: Auth einrichten

#### 3a. n8n-API-Key generieren

In den n8n-Einstellungen (`https://n8n.viron.de/settings/api`):

1. Auf "Create an API Key" klicken
2. Key-Namen vergeben: `VIRON_MCP_INTEGRATION`
3. Berechtigungen: Workflow Execution + Read
4. Key kopieren und sicher speichern

#### 3b. Key in Umgebungsvariable hinterlegen

```bash
# Hetzner .env oder docker-compose.yml
N8N_API_KEY=n8n_api_live_xxxxxxxxxxxxxxxxxxxx
```

#### 3c. opencode Auth konfigurieren

Die `${N8N_API_KEY}`-Notation in der opencode.jsonc liest automatisch aus der System-Umgebung. Kein Hardcoding von Secrets in der Config.

### Schritt 4: Test-Workflow — Agent → MCP Client → n8n

**Ziel:** VIRON Orchestrator (Claude) erstellt einen LinkedIn-Post über ein gegebenes Thema und publishiert ihn automatisch.

#### 4a. N8N-Workflow erstellen: "VIRON LinkedIn Publisher"

```
[MCP Server Trigger: "publish_linkedin_post"]
  │  Input Schema: topic (string), tone (string), client_id (string)
  ▼
[Set Node: Parameter Extraction]
  │
  ▼
[HTTP Request: Gemini/Claude API]
  │  Prompt: "Schreibe einen LinkedIn-Post über {topic} im {tone}-Stil"
  │  Output: post_text (string)
  ▼
[HTTP Request: Buffer API / Metricool API]
  │  Publish post_text auf LinkedIn
  │  Output: post_url (string)
  ▼
[PostgreSQL Node: Log Entry]
  │  INSERT INTO public.mkt_content_log (content_id, topic, status, post_url)
  │
  ▼
[Return to Agent]
  │  Output: { status: "published", post_url: "...", post_text: "..." }
```

#### 4b. Tagging für MCP-Discovery

In den N8N-Workflow-Einstellungen:
- Tag `mcp` hinzufügen
- Tag `VIRON` hinzufügen
- Tag kann als Filter in opencode dienen (nur VIRON-Tools anzeigen)

#### 4c. Agent-Trigger

Nach der Konfiguration kann Claude (Orchestrator) den Workflow so auslösen:

```
Operator: "Erstelle einen LinkedIn-Post über DSGVO-konforme Automatisierung"
→ Claude entdeckt n8n-viron via MCP Tool Discovery
→ Claude ruft publish_linkedin_post(topic="DSGVO", tone="professional") auf
→ N8N generiert, publishiert, loggt
→ Claude erhält post_url und bestätigt dem Operator
```

---

## 4. Entscheidungsmatrix

### Wann umsetzen?

**→ Sobald n8n auf Hetzner produktiv läuft und API-Zugang konfiguriert ist.**

Voraussetzungskette:
```
n8n Docker Deployment (Hetzner)
  → HTTPS/SSL (Let's Encrypt)
  → n8n API Key generiert
  → MCP Community Node installiert
  → opencode.jsonc konfiguriert
  → Erster Test-Workflow
  → VIRON in Produktion
```

### Was muss VORHER stehen?

| Voraussetzung | Verantwortlich | Geschätzter Aufwand |
|---|---|---|
| 1. Hetzner VPS bereitstellen (CX22 oder höher) | Operator | 1 Tag |
| 2. n8n Docker-Deployment (docker-compose) | GROUND0 | 1 Tag |
| 3. PostgreSQL 16 Datenbank (n8n + VIRON) | GROUND0 | 0,5 Tage |
| 4. SSL/TLS mit Let's Encrypt | GROUND0 | 0,5 Tage |
| 5. API-Key + Credential-Management | Operator | 0,5 Tage |
| 6. n8n-nodes-mcp Installation | GROUND0 | 0,5 Tage |

**Gesamt-Vorlauf:** ~4 Tage (3-4 Tage bis MCP ready)

### Was hängt DAVON ab?

Die MCP-Integration ist **Gateway für alle automatisierten Marketing-Workflows**:

| Abhängiger Workflow | Typ | Ohne MCP | Mit MCP |
|---|---|---|---|
| **Content Pipeline** (LinkedIn, Buffer, Metricool) | Content | Manuell Webhook bauen | Automatisch via Skill |
| **Competitor Monitoring** (SparkToro, SimilarWeb) | Research | Manuell Daten abrufen | Scheduled + Alert |
| **GEO Content Optimization** (Perplexity API) | SEO | Händisch optimieren | Automatisiert + Tracking |
| **n8n RSS to Social** (Content Recycling) | Content | Manuell triggern | Scheduled durch Agent |
| **Hyperframes/Remotion Video** | Video | Separat triggern | In Pipeline integriert |
| **Email Campaign Triggers** | Outbound | N/A | Automatisch via CRM Events |

**Fazit:** Ohne MCP bleibt VIRON eine Sammlung manuell gestarteter Einzelskripte. Mit MCP wird daraus ein selbstorchestrierendes System.

---

## 5. Integrations-Patterns (aus IMPORT/04)

### Pattern 1: Agent Skills → N8N Webhook Trigger (Pattern A)

```
Claude (Orchestrator) → Webhook → N8N Workflow → Ausführung
```

- **Einfachste Variante**, keine MCP-Node nötig
- **Nur unidirektional** — kein Status-Rückkanal
- **Einsatz:** Schneller Prototyp, Proof-of-Concept
- **VIRON-Status:** Sobald n8n läuft, sofort einsetzbar

### Pattern 2: N8N MCP Server ←→ Claude (Pattern B)

```
Claude (Orchestrator) ↔ MCP ↔ N8N Workflows
```

- **Bidirektional** — Workflow-Ergebnis kommt zurück zum Agent
- **Tool Discovery** — Agent erkennt Workflows automatisch
- **Einsatz:** VIRON-Produktivbetrieb, Content-Erstellung + Publishing
- **VIRON-Status:** Erfordert MCP-Installation + opencode.jsonc-Konfiguration
- **Erfordert:** MCP Server Trigger Node in N8N

### Pattern 3: Multi-Agent via N8N Message Bus (Pattern C)

```
Agent A (Content Strategy) → MCP → [N8N Channel: content-planning]
  → Agent B (Copywriter) → MCP → [N8N Channel: copy-review]
    → Agent C (Reviewer) → MCP → [N8N Channel: publish]
      → N8N Workflow → Publish
```

- **Volle Orchestrierung** — Mehrere Agenten kommunizieren über N8N
- **N8N als Message Bus** — kein externer Broker nötig
- **Einsatz:** Skalierte VIRON-Produktion (5+ parallele Agenten)
- **VIRON-Status:** Phase 3 (Monat 2 nach MCP-Integration)

### Pattern-Empfehlung für VIRON

| Phase | Pattern | Zweck |
|---|---|---|
| **Jetzt (Planung)** | Pattern A via Webhook | n8n läuft, MCP noch nicht — trotzdem integrierbar |
| **Phase 1 (Woche 1-2)** | Pattern B (bidirektional) | Erster MCP-Test, Content-Pipeline-PoC |
| **Phase 2 (Woche 3-4)** | Pattern B (voll) | Core Workflows: Content, Lead Scoring, Alerts |
| **Phase 3 (Monat 2)** | Pattern C (Multi-Agent) | Skalierte Produktion mit Agenten-Kooperation |

---

## 6. DSGVO-Integration (aus IMPORT 4.5)

Die MCP-Integration muss von Anfang an DSGVO-konform sein:

### Datenfluss-Dokumentation (Art. 30 DSGVO)
- Welche Daten fließen über MCP? (Content-Texte, URLs, Zeitstempel)
- Verarbeitungszweck: Marketing-Automation (Art. 6 Abs. 1 lit. f DSGVO)
- Speicherort: Hetzner (Deutschland, EU) → ✅
- Löschfristen: Execution Data nach 30 Tagen (konfigurierbar in n8n)

### Technische Maßnahmen
- **Encryption at Rest:** PostgreSQL SSL, Hetzner Storage-Verschlüsselung
- **Encryption in Transit:** HTTPS/TLS auf allen MCP-Verbindungen
- **Access Control:** N8N API-Key Rotation alle 90 Tage
- **Data Minimization:** Nur notwendige Felder im MCP-Tool-Schema exponieren
- **Keine PII in Logs:** Error-Outputs filtern (keine personenbezogenen Daten)
- **Right to Deletion:** Automatisierter Lösch-Workflow für alte Daten

### MCP-Spezifisch
- API-Keys **niemals** im Klartext in Workflow-JSONs
- Immer `$env.N8N_API_KEY` oder Credential-Node verwenden
- SSE-Verbindungen mit Token-basierter Auth (nicht IP-basiert)

---

## 7. Nächste Aktion nach n8n-Start

### Unmittelbar nach n8n-Deployment (Tag 1-2)

1. **Ersten Test-Workflow definieren:**
   ```
   Name: "VIRON_Test_Ping"
   Trigger: MCP Server Trigger ("ping")
   Logic: Set Node → "PONG" → Return to Agent
   ```
   → Validiert: MCP-Verbindung, Auth, Rückkanal

2. **MCP-Verbindung validieren:**
   ```bash
   curl -X POST https://n8n.viron.de/mcp/sse \
     -H "Authorization: Bearer ${N8N_API_KEY}" \
     -H "Content-Type: application/json" \
     -d '{"method": "tools/list"}'
   ```
   → Erwartet: Liste aller getaggten VIRON-Workflows

3. **Automatisierte Content-Pipeline als Proof-of-Concept:**
   - Workflow: "VIRON LinkedIn Post" (Schritt 4 oben)
   - Eingabe: Topic + Tone
   - Ausgabe: Live-geposteter LinkedIn-Beitrag
   - Log: PostgreSQL `public.mkt_content_log`

4. **opencode.jsonc finalisieren:**
   - MCP-Konfiguration eintragen
   - `n8n-viron` als dauerhaften MCP-Server registrieren

### Nach erfolgreichem PoC (Tag 3-7)

- Workflow 2: Competitor Monitoring & Alerting (SparkToro API)
- Workflow 4: Lead Scoring & Routing (HubSpot/CRM Integration)
- PostgreSQL-Logging für alle Workflows standardisieren
- Slack-Notification-Node in kritische Workflows einbauen

### Meilenstein: "VIRON ist autonom"

Erreicht wenn: `Operator sagt "Poste das" → Claude → N8N → Live-Post → Claude meldet URL`

---

## 8. Zusammenfassung

| Aspekt | Status |
|---|---|
| **MCP-Protokoll** | ✅ Standard definiert, alle Nodes dokumentiert |
| **n8n-Bereitschaft** | ✅ n8n unterstützt MCP nativ (2025-2026) |
| **VIRON-Konfiguration** | ⏳ opencode.jsonc vorbereitet, muss nach Deployment aktiviert werden |
| **Auth-Setup** | ⏳ API-Key muss nach n8n-Start generiert werden |
| **n8n-Deployment** | ❌ Noch nicht aktiv auf Hetzner |
| **Blockiert durch** | Hetzner-Bereitstellung + n8n Docker-Deployment |
| **Nächster Schritt** | n8n auf Hetzner deployen → MCP Node installieren → opencode.jsonc aktivieren |
| **Zeithorizont** | ~1 Woche nach n8n-Start für vollständige Integration |

---

*Report basierend auf: IMPORT/04_N8N_Integration_Agent_Skills.md (Mai 2026)*
*Erstellt im Rahmen der VIRON GROUND0 Infrastructure-Planung*
