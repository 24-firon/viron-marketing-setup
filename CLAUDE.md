# CLAUDE.md — VIRON AI Operating System Context & Guidelines

**Status:** Active | **Last Updated:** 2026-03-14 | **Version:** 1.0

---

## 1. PROJEKT-IDENTITÄT

### Was ist VIRON?
VIRON ist ein **AI Operating System** für eine KI-Automatisierungsagentur (Ground-Zero Agency Infrastructure), die spezialisierte Automatisierungslösungen für kleine und mittlere Unternehmen (KMU) im deutschsprachigen Raum (DACH) baut.

**Kernleistungen:**
- Custom n8n-Workflows (Open-Source RPA)
- KI-Agenten & AI-Orchestrierung
- CRM-Integrationen (HubSpot, Pipedrive, etc.)
- Content-Systeme und Marketing-Automatisierung
- Lead-Qualifizierung & Sales-Enablement

**Target ICP (Ideal Customer Profile):**
- Unternehmen: 5–50 Mitarbeiter im DACH-Raum
- Branchen: KMU, Handwerk, Dienstleistungen, Tech-Startups
- Schmerzpunkte: manuelle Prozesse, unstrukturierte Daten, Zeit-Ineffizienz, fehlende CRM-Nutzung

**Operatoren:**
- **Operator (Mensch):** Inspektor — technisch versiert, Zeitdruck, kein Fluff, lösungsorientiert
- **Orchestrator (KI):** Claude Haiku — schnell, kostengünstig, Koordination
- **Specialized Agents (KI):** Claude Sonnet — hochwertige Inhalte, Strategie, Komplexes

---

## 2. ARCHITEKTUR-ÜBERBLICK

### 5 Säulen (Pillars) von VIRON

```
┌─────────────────────────────────────────────────────────────┐
│                    VIRON OS (Orchestrator)                  │
├─────────────────────────────────────────────────────────────┤
│  GRO (GROWTH)   │  MKT (MARKETING)  │  SAL (SALES)          │
│  Infrastructure │  Content Engine   │  Lead Qual.           │
│  Server         │  Social/SEO       │  Outreach             │
│  MCP Stack      │  Campaigns        │  CRM                  │
├─────────────────────────────────────────────────────────────┤
│  FUL (FULFILLMENT)    │  OPS (OPERATIONS)                   │
│  Customer Projects    │  Finanzen                           │
│  Onboarding          │  Reporting                          │
│  Delivery            │  Interne Prozesse                   │
└─────────────────────────────────────────────────────────────┘
```

### Agent-Hierarchie

```
Operator (Mensch — Inspektor)
    │
    └── Orchestrator (Claude Haiku)
            │
            └── Content Engine (Claude Sonnet)
                    │
                    ├── VIDEO SPECIALIST
                    │   ├── MKT-4: Organic Faceless Video Engine
                    │   └── CCE: Ad Creative Engine (v1.0)
                    │
                    └── COPY SPECIALIST
                        ├── Mega-Guide Generator
                        ├── Pillar Article Generator
                        └── Social Content Generator
```

### Tool-Stack (STRIKT & BINDEND)

| **Layer** | **Tool** | **Use Case** | **Constraints** |
|-----------|----------|-------------|-----------------|
| **Orchestrierung** | n8n (self-hosted Hetzner) | Alle Workflows, Automatisierung | STANDARD. Immer. Keine Alternativen. |
| **LLM-Routing** | Gemini/Vertex AI (DEFAULT) | Erste Wahl, $300 Credit, kosteneffizient | Fallback: Claude Haiku / Sonnet |
| **Datenbank** | PostgreSQL 16 (Hetzner) | Produktivdaten, Workflows, Logs | Primary DB. Persistenz. Backups täglich. |
| **Metadaten** | Supabase (Free Tier) | Metadata-Sync, ggf. Realtime-Events | Optional, nicht kritisch. |
| **Review-Interface** | Airtable (Free Tier) | Visual Review, Content-Staging | Max 1.000 Records pro Base. Archivierungsregeln bei 700+. |
| **Publishing** | Metricool (Webhook: GROUND0-6) | Social Media Distribution (IG, LinkedIn, TikTok, YT) | Trigger via n8n. |
| **Projektmanagement** | Linear | Source of Truth für alle Tasks, Estimates, Blocked-by-Chains | Alle Agenten updaten Linear. |
| **Dokumentation** | Notion | Wissensbasis, Architecture Docs, Foundation Blocks | Lesen, nicht updaten (nur Operator). |
| **Code-Runtime** | Python 3.11 + Docker | Scripts, Custom-Logik in n8n | NICHT 3.12. Immer Docker-ready. |
| **MCP-First** | Model Context Protocol Server Stack | Zentrale Kommunikation zwischen Agenten | Zentraler Koordinationspunkt. |

**ABSOLUT VERBOTEN:**
- ❌ OpenAI (Claude only für Komplexes)
- ❌ Zapier (n8n is standard)
- ❌ Proprietäre LLMs hardcoden
- ❌ Manuelle Datei-Transfers

---

## 3. STRIKTE REGELN (NICHT VERHANDELBAR)

### MUSS-Regeln (Must)

1. **Kein Hardcoding von Modellnamen**
   - ❌ `"use Imagen 3"`, `"use Veo 3"` fest schreiben
   - ✅ `"Provider-agnostischer Prompt → n8n wählt Provider basierend auf VIRON_TOOL_STACK"`

2. **Linear ist Source of Truth**
   - Alle Tasks müssen in Linear sein (MKT, SAL, FUL, OPS, GROUND0 Teams)
   - Jeden Task-Abschluss mit Linear Issue verlinken
   - Blocked-by-Chains nicht brechen

3. **Notion ist Read-Only (für Agent)**
   - Lesen: VIRON OS Master Index, VIRON_AGENT_BLUEPRINT, VIRON_TOOL_STACK, VIRON_CONTEXT_v1, Foundation Blocks
   - Schreiben: Nur Operator updatet Notion

4. **Airtable-Daten nicht vollmüllen**
   - NUR Thumbnails + URLs speichern, keine Base64-Bilder
   - Max 1.000 Records pro Base (Archivierung ab 700)
   - Review-Interface sauber halten

5. **Provider-Agnostik in Prompts**
   - Prompts müssen mit Vertex AI, Gemini, Claude, Llama funktionieren
   - Input/Output-Formate standardisieren (JSON, Markdown, CSV)

6. **Python 3.11 zwingend**
   - Keine 3.12-Features
   - Alle Docker-Images: `FROM python:3.11-slim`

7. **Code = Production-Ready**
   - Testbar, dokumentiert, Error-Handling
   - Keine Wegwerf-Scripts

### VERBOTEN-Regeln (Forbidden)

- ❌ Ohne CLAUDE.md + Notion Context arbeiten
- ❌ Tasks ohne Plan skizzieren (→ 3-7 Steps vor Exec)
- ❌ Architektur-Entscheidungen ohne Operator-Approval
- ❌ Airtable mit File-Attachments füllen
- ❌ OpenAI/Zapier vorschlagen
- ❌ Token-Verschwendung durch zu ausführliche Antworten
- ❌ Linear vergessen zu updaten

---

## 4. TOOL-ENTSCHEIDUNGSMATRIX

**Wann welches Tool nutzen?**

### Content-Produktion

| **Task** | **Primary Tool** | **Secondary** | **Review** |
|----------|-----------------|---------------|-----------|
| Content Generator starten | n8n Workflow | Vertex AI / Gemini | Airtable |
| Prompt verfeinern | Claude Sonnet (this session) | — | — |
| Video-Thumbnail generieren | n8n → Vertex AI | — | Airtable |
| Social Posts schedulen | n8n → Metricool Webhook | — | Metricool Dashboard |
| Kampagnen-Tracking | n8n → PostgreSQL | Supabase Sync (optional) | Linear Reports |

### Datenbank-Operationen

| **Task** | **Use** | **Constraints** |
|----------|--------|-----------------|
| Live-Daten speichern | PostgreSQL 16 | Primary DB, tägliche Backups |
| Realtime-Events | Supabase (optional) | Nur Metadata, nicht kritisch |
| Airtable Review-Queue | Airtable API via n8n | Max 1.000 Records, archivieren ab 700 |

### Dokumentation & Knowledge

| **Task** | **Use** | **Permissions** |
|----------|--------|-----------------|
| Architektur verstehen | VIRON_CONTEXT_v1 (Notion) | Read-only |
| Agent-Prompts nachschlagen | VIRON_AGENT_BLUEPRINT (Notion) | Read-only |
| Tool-Stack entscheidungen | VIRON_TOOL_STACK (Notion) | Read-only |
| Foundation Blocks (F1-F5) | Notion Pages | Read-only |
| Projekt-Status | Linear Issues + Boards | Read + Update |

---

## 5. LLM-ROUTING (Wann welches Modell?)

**Entscheidungsalgorithmus:**

```
Task kommt rein
    │
    ├─ Einfach + schnell nötig? → Gemini (Free $300 Credit)
    │    │
    │    ├─ Bulk-Content-Gen (100+ Posts)? → Vertex AI
    │    │
    │    └─ Echtzeit-Scheduling? → Claude Haiku
    │
    ├─ Strategisch + komplex? → Claude Sonnet
    │    │
    │    ├─ Mega-Guides schreiben? → Sonnet + n8n
    │    │
    │    ├─ System-Prompt verfeinern? → Sonnet (lokal)
    │    │
    │    └─ Video-Skripte? → Sonnet
    │
    └─ Ultra-schnelle Orchestrierung? → Claude Haiku
         │
         └─ Workflow-Koordination
         └─ Task-Delegation

→ NIEMALS: OpenAI hardcoden
→ FALLBACK: Wenn Gemini-Credit aufgebraucht → Haiku
```

### Modell-Profile

| **Modell** | **Use Case** | **Speed** | **Quality** | **Cost** |
|-----------|------------|---------|----------|----------|
| **Gemini/Vertex** | Bulk Content Gen, Media Gen | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $0 (Credit) |
| **Claude Sonnet** | Strategy, Writing, Complex Logic | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $$ (geplant) |
| **Claude Haiku** | Orchestrierung, Quick Tasks | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | $ (günstig) |

---

## 6. KONTEXT-QUELLEN (Wo Infos holen?)

### Notion (Read-Only für Agent)

**Must-Read beim Start:**
1. **VIRON OS Master Index** — Navigation Hub, Überblick aller Systeme
2. **VIRON_CONTEXT_v1** — Master Knowledge File, alle Fakten
3. **VIRON_AGENT_BLUEPRINT** — System Prompts, Agent-Definitionen
4. **VIRON_TOOL_STACK** — Tool-Matrix, Entscheidungsregeln
5. **Foundation Blocks (F1-F5)**
   - F1: Brand Identity
   - F2: ICP Definition
   - F3: Master System Prompt
   - F4: Content-Strategie pro Kanal
   - F5: Asset-Bibliothek

**Optional:**
- CCE Architektur-Page (Creative Content Engine)
- Marketing Launch Masterplan (Content-Pyramide)

### Linear (Source of Truth)

**Teams & Projekte:**
- **MKT** — Marketing (Creative, Content, SEO)
- **SAL** — Sales (Lead Gen, Outreach, CRM)
- **FUL** — Fulfillment (Kundenprojekte, Delivery)
- **OPS** — Operations (Finanzen, Reporting)
- **GROUND0** — Infrastructure, System (MCP, n8n, Deployment)

**Labels:** `#build`, `#core-system`, `#research`, `#content`

**Aktuell Active Issues:**
- MKT-4: Organic Faceless Video Engine
- MKT-35 bis MKT-39: Creative Content Engine (5-Layer Pipeline)
- MKT-1: Auto-Moderation Make Blueprint

### Lokale Dateien (Work-Lab/)

| **Pfad** | **Inhalt** | **Update-Freq** |
|----------|-----------|-----------------|
| `Work-Lab/Content/` | Produzierte Mega-Guides, Pillar-Artikel, Social Content | Täglich |
| `Work-Lab/Handover/` | Research, z.B. `Marketing-research.md` (54KB Competitor-Analyse) | Nach Research |
| `Work-Lab/VIRON_Full_Package_v2/` | GOD_MODE_Report, Linear_Verbatim_Blueprint | Selten |
| `Work-Lab/AGENTS.md` | Agent-Setup-Dokumentation | Nach Agent-Update |
| `Work-Lab/TASKS.md` | Quick-Reference aktueller Tasks | Täglich |
| `Work-Lab/CLAUDE.md` | **Diese Datei** — Kontext für Agenten | Nach System-Änderung |

---

## 7. KOMMUNIKATIONSREGELN

### Sprache & Ton

- **Sprache:** Deutsch (Hauptsprache), formell-professionell
- **Stil:** Direkt, lösungsorientiert, kein Fluff
- **Haltung:** Motivierend aber skeptisch-hinterfragend (Challenge assumptions)
- **Struktur:** Code > Theorie. Production-Ready vor Discussion.

### Response-Format

**Plan vor Execution:**
1. Problem-Space verstehen (3-5 Fragen klären falls nötig)
2. 3-7 Steps skizzieren
3. **Operator-Approval einholen**
4. Execute & Verify
5. Linear updaten

**Output-Struktur:**
```
## Problem
[Kurz: Was ist zu tun?]

## Analyse
[Wo liegen die Daten? Welche Systeme betroffen?]

## Plan (3-7 Steps)
1. [Step]
2. [Step]
...

## Approval benötigt
[Was muss der Operator freigeben?]

---

## Execution (Nach Approval)
[Code, Commands, Updates]

## Verification
[Was wurde überprüft?]

## Linear Update
[Link zur Issue, Status-Update]
```

### Token-Effizienz

- ✅ Prägnant, fokussiert auf Essentials
- ✅ Code-Snippets nur wenn load-bearing
- ❌ Ausschweifung, Theorie ohne Kontext
- ❌ Wiederholung von bereits bekannten Infos

---

## 8. AKTUELLE PROJEKTE & STATUS

### CCE (Creative Content Engine) — MKT-35 bis MKT-39

**Status:** v1.0 aktiv, Layer 1-5 implementiert

**5-Layer Pipeline:**
1. **Input** → Airtable (Content Brief, Format, Target Audience)
2. **Prompt** → Agent generiert optimierte Prompts (Provider-agnostisch)
3. **Generation** → n8n ruft Vertex AI/Gemini auf
4. **Review** → Airtable (nur Thumbnails + URL, kein Upload)
5. **Publishing** → n8n → Metricool Webhook

**Aktueller Stand:**
- ✅ Layer 1-5 konfiguriert
- ✅ Airtable Review-Base läuft
- ✅ n8n Workflows produktiv
- ⏳ Optimization der Prompt-Qualität ongoing

**Zuständige Issues:**
- MKT-35: CCE Architecture
- MKT-36: Layer-1-Input-Validierung
- MKT-37: Provider-Selection-Logic
- MKT-38: Airtable-Review-Automation
- MKT-39: Metricool-Publishing-Chain

---

### Marketing Launch Masterplan

**Status:** Block 2-4 abgeschlossen (März 2026)

**Content-Pyramide:**
```
        ▲
       [4 Mega-Guides]
      (Top of Funnel)
        │
      [8 Pillar-Artikel]
   (Mid-funnel Education)
        │
    [~450 Social Content Pieces]
  (Bottom-funnel Engagement)
        ▼
```

**Abgeschlossene Blöcke:**
- ✅ **Block 1:** Foundation Research (Competitor-Analyse, Hook-Formeln, ICP-Definition)
- ✅ **Block 2:** 2x Mega-Guides geschrieben
- ✅ **Block 3:** 8x Pillar-Artikel produziert
- ✅ **Block 4:** 31x Social Content Pieces generated

**Research-Files:**
- `Work-Lab/Handover/Marketing-research.md` (54KB) — 15 Competitor-Profile, 4 Content-Gaps, 60 Hook-Formeln

**Content-Gaps identifiziert:**
1. Build-in-Public Content (Agenten-Trainings zeigen)
2. Mitarbeiter-KI-Onboarding (für KMU-Teams)
3. Interaktive Lead-Magneten (vs. PDFs)
4. Nischen-Monopolisierung (spezifisch DACH-Probleme)

**LinkedIn 2026 Insights:**
- 360-Brew-Modell dominant (Fokus auf Netzwerk-Dynamik)
- Thematischer Fit > Reichweite
- Kommentar-Tiefe > Likes
- ⚠️ Unternehmensseiten konvertieren nicht (nur Personal Brands)

---

## 9. ANTI-PATTERNS (Was vermeiden?)

### Code-Anti-Patterns

❌ **Provider-spezifische Modelle hardcoden**
```python
# FALSCH:
prompt = "use Imagen 3 to generate image"
model = "gpt-4-turbo"

# RICHTIG:
prompt = "Generate high-quality image. Model selection via n8n config."
# n8n entscheidet dann: Vertex AI vs. Claude vs. Gemini
```

❌ **Airtable mit File-Attachments füllen**
```python
# FALSCH:
airtable.attach_file("thumbnail.png", record_id)

# RICHTIG:
airtable.update_record(record_id, {
    "Thumbnail_URL": "https://cdn.example.com/thumb.png",
    "Generation_Status": "ready_for_review"
})
```

❌ **Python 3.12 Features verwenden**
```python
# FALSCH:
match task_type:
    case "video": ...

# RICHTIG:
if task_type == "video":
    ...
```

### Prozess-Anti-Patterns

❌ **Linear nicht updaten**
- Immer: Task anfangen → Linear "In Progress" setzen
- Immer: Task finish → Linear Issue mit Kontext + Links updaten

❌ **Ohne Approval arbeiten**
- 3-7 Step Plan skizzieren BEVOR Code geschrieben wird
- Approval einholen, DANN execute

❌ **Notion updaten (Agent)**
- Notion ist Read-Only für Agenten
- Nur Operator schreibt Notion
- Agent liest Notion für Kontext

❌ **Stichpunkte ohne Erklärung**
- ❌ "1. n8n Workflow\n2. Airtable\n3. Metricool"
- ✅ "n8n Workflow triggert Airtable-Review mit Thumbnails, nach Approval publiziert Metricool via Webhook"

❌ **Über Modelle reden statt arbeiten**
- ❌ "Sollen wir Gemini oder Claude nehmen?"
- ✅ "Gemini ist cheaper, Sonnet für Qualität — welche Metrik ist wichtiger für diesen Task?"

---

## 10. WORKFLOW-REGELN (Tasks bearbeiten)

### Standard Task-Workflow

```
1. Task aus Linear holen
   └─ Issue lesen, Acceptance Criteria klären
   └─ Abhängigkeiten checken (Blocked-by-Chain)

2. Kontext laden (falls neu)
   └─ CLAUDE.md lesen (diese Datei)
   └─ Relevante Notion-Pages lesen (VIRON_CONTEXT_v1, etc.)
   └─ Lokale Files checken (Work-Lab/Handover/, Content/)

3. Problem-Space analysieren
   └─ Welche Systeme betroffen? (n8n, Airtable, PostgreSQL, etc.)
   └─ Welche Daten nötig?
   └─ Welche Abhängigkeiten? (Andere Tasks, Provider-APIs, etc.)

4. PLAN skizzieren (3-7 Steps)
   └─ Kurze Step-Beschreibung
   └─ Tools pro Step
   └─ Risks & Mitigations
   └─ Success Criteria

5. APPROVAL einholen (vom Operator)
   └─ "Sollen wir so vorgehen?"
   └─ Warten auf Freigabe

6. EXECUTE
   └─ Code schreiben / Konfigurieren
   └─ Tests laufen lassen
   └─ Error-Handling implementieren
   └─ Logs produzieren

7. VERIFY
   └─ Hat's funktioniert?
   └─ Acceptance Criteria erfüllt?
   └─ Keine Regressions?

8. LINEAR UPDATE
   └─ Issue: "In Progress" → "Done" (oder "In Review")
   └─ Comment mit Links (Notion, Local Files, n8n Workflows)
   └─ Nächste blockedbys freigeben wenn applicable

9. HANDOFF (falls nächster Agent)
   └─ Dokumentation updaten (Work-Lab/Handover/)
   └─ Outputs speichern (Content/, etc.)
   └─ Linear Issue mit all context linken
```

### Task-Templates nach Typ

#### Content-Generierung (z.B. MKT-35)
```
1. Airtable Brief laden
2. Provider-agnostischen Prompt bauen
3. n8n Workflow triggern (Vertex AI/Gemini)
4. Output in Airtable speichern (URL only, kein Upload)
5. Thumbnail für Review produzieren
6. Linear Issue mit Workflow-URL + Airtable-Link updaten
```

#### Workflow-Konfiguration (z.B. GROUND0-* Tasks)
```
1. n8n Interface öffnen, Workflow-Node analysieren
2. Environment Variables / Secrets prüfen (PostgreSQL, API Keys)
3. Änderungen implementieren
4. Test-Run durchführen (mit Test-Daten)
5. Logs prüfen, Error-Handling bestätigen
6. PostgreSQL-Schema-Changes dokumentieren (falls relevant)
7. Linear Issue mit Workflow-ID + Run-Logs updaten
```

#### Research & Analysis (z.B. MKT-1)
```
1. Anforderung verstehen (Competitor Analysis? Content Gaps?)
2. Daten sammeln (Web, Notion, Linear Insights)
3. Analyse durchführen (Patterns, Recommendations)
4. Markdown-Report schreiben
5. Work-Lab/Handover/ speichern
6. Linear Issue mit Findings + File-Path updaten
7. Key Insights als Notion-Comment posten (falls relevant)
```

---

## 11. N8N WORKFLOWS — HÄUFIGE PATTERNS

### Workflow-Benennung
```
[TEAM]-[TASK]-[VERSION]
Beispiel: MKT-CCE-Layer1-v2.0
```

### Standard-Node-Struktur
```
Trigger
  └─ Input Validation (Airtable / PostgreSQL)
  └─ Provider Selection (Logic basierend auf VIRON_TOOL_STACK)
  └─ API Call (Gemini / Vertex AI / Claude)
  └─ Output Transform (Standardformat)
  └─ Database Update (PostgreSQL / Airtable)
  └─ Webhook Trigger (falls Publishing nötig, z.B. Metricool)
  └─ Error Handler & Logging
```

### Credential Management
- Secrets in **Hetzner Environment** speichern (NICHT in n8n JSON)
- PostgreSQL-Connections: Pool-Management (Max 20 Connections)
- API-Keys für Gemini/Vertex: Rotation alle 90 Tage

---

## 12. DATENBANK-RICHTLINIEN (PostgreSQL 16)

### Schema-Naming
```
public.{team}_{resource}
Beispiel: public.mkt_content_queue, public.sal_leads
```

### Backup-Policy
- **Frequency:** Täglich um 02:00 UTC
- **Retention:** 30 Tage (Hetzner Automated)
- **Recovery Test:** Monatlich

### Connection Pooling
```
Max Connections: 20
Idle Timeout: 300s
```

---

## OFFENE FRAGEN AN OPERATOR

Für eine noch vollständigere CLAUDE.md bitte folgende Punkte klären:

### Technische Infrastruktur
1. **Hetzner-Setup:** Welche VPS/Bare-Metal-Spezifikation? (CPU, RAM, Storage)
2. **n8n-Deployment:** Docker Compose oder Bare-Metal? Load-Balancer dahinter?
3. **PostgreSQL-Backups:** Wo werden Backups gespeichert? (Hetzner Storage Box? S3?)
4. **MCP-Server:** Welche MCP-Server sind aktuell konfiguriert? Welche sind geplant?
5. **CI/CD:** Gibt es GitHub Actions / GitLab CI für automatisierte Deployments?
6. **SSL/TLS:** Zertifikats-Management (Let's Encrypt Auto-Renewal)?

### Code-Organisation
7. **Git-Repos:** Wo liegen die Code-Repos? (GitHub, GitLab, Gitea?)
8. **Branching-Model:** Welches Git-Workflow? (trunk-based, feature-branches, release-branches?)
9. **Code-Review-Prozess:** Wer reviewed Pull Requests vor merge zu main/production?
10. **Docker-Registry:** Wo werden Images gepusht? (Docker Hub, Hetzner Registry, Self-Hosted?)

### Datenquellen & APIs
11. **Notion-Integration:** Gibt es eine Notion API v2 Connection in n8n? Falls ja, authentifiziert mit welchem Token?
12. **Airtable-Integration:** Personal Access Token? Welche Bases sind aktuell connected?
13. **Linear-Integration:** API-Key konfiguriert? Welche Team-IDs / Project-IDs sind relevant?
14. **Metricool-Webhook:** Wo exakt ist der Webhook registriert? (n8n URL pattern?)
15. **PostgreSQL-Connection String:** Template für neue Workflows? (Pooling, SSL mode, etc.)

### Skalierung & Monitoring
16. **Logging:** Wo landen n8n Logs? (Hetzner Syslog? PostgreSQL? External Service?)
17. **Error-Handling:** Wer wird benachrichtigt bei Workflow-Failures? (Slack, Email, Linear Issue?)
18. **Monitoring Dashboard:** Gibt es ein Live-Dashboard für n8n Health? (Grafana? Datadog?)
19. **Alerting-Thresholds:** Bei welcher Fehlerquote wird automatisch eskaliert?

### Sicherheit & Secrets
20. **Secrets-Management:** Wie werden API-Keys, DB-Passwords gespeichert? (.env-Vorlage vorhanden?)
21. **Rotation-Policy:** Wie oft müssen Credentials rotiert werden?
22. **Access Control:** Wer hat Zugriff auf n8n Admin Panel? Linear API? Airtable?
23. **Audit Logs:** Werden alle Agent-Aktionen geloggt (n8n Run-History)?

### Notion-Architektur
24. **Notion-Workspace-ID:** Für MCP-Integrations-Tests nötig?
25. **Database-IDs:** Welche Notion-Datenbanken sind für Agenten read-relevant?
26. **Archivierungs-Strategy:** Wann werden alte Notion-Pages archiviert? (Nach 6 Monaten inaktiv?)
27. **Permission-Model:** Unterschiedliche Access-Levels pro Agent notwendig?

### Linear-Struktur
28. **Team-IDs:** Exakte IDs für MKT, SAL, FUL, OPS, GROUND0?
29. **Workflow-Labels:** Gibt es weitere Labels außer #build, #core-system, #research, #content?
30. **Cycle-Planning:** Welche Cycles sind aktuell aktiv? (2-Week Sprints? Continuous Flow?)
31. **Issue-Templates:** Welche Templates für verschiedene Task-Typen? (CCE-Content? Sales-Lead? etc.)

### Content & Assets
32. **Asset-Versionierung:** Wo werden finalisierte Assets gespeichert? (CDN? Hetzner Storage?)
33. **Content-Calendar:** Wo ist der authoritative Content-Kalender? (Linear? Notion? Airtable?)
34. **Video-Storage:** Wo landen produzierte Videos? (AWS S3? Hetzner? YouTube Direct?)

### Qualitätssicherung
35. **Acceptance-Criteria:** Für CCE — wann ist ein Generated Content "ready for review"?
36. **Test-Data:** Wo sind Test-Datensets für n8n Workflow-Testing?
37. **Performance-Baselines:** Welche Metriken? (Response Time, Token Usage, Cost per Content Piece?)

### Rollout & Deployment
38. **Staging-Environment:** Existiert ein Staging-n8n oder nur Production?
39. **Feature-Flags:** Nutzt VIRON Feature-Flags für A/B-Testing?
40. **Rollback-Procedure:** Was tun, falls ein n8n Workflow bricht? (Manual Intervention? Automated Rollback?)

---

## QUICK REFERENCE CHECKLIST

**Vor jedem Task starten:**
- [ ] CLAUDE.md (diese Datei) gelesen
- [ ] Linear Issue gelesen & verstanden
- [ ] Relevante Notion-Pages gelesen (VIRON_CONTEXT_v1 mindestens)
- [ ] Dependencies gecheckt (Blocked-by-Chain)
- [ ] Tool-Stack für diesen Task entschieden (n8n? Airtable? PostgreSQL?)
- [ ] Plan (3-7 Steps) skizziert
- [ ] Operator-Approval eingeholt (falls Decision Point)

**Nach Task-Completion:**
- [ ] Code / Konfiguration getestet (Error-Handling OK?)
- [ ] Linear Issue updated (Done / In Review)
- [ ] Outputs dokumentiert (Work-Lab/ relevante Folder)
- [ ] Next Blocked-by Tasks freigegeben?
- [ ] Keine OpenAI / Zapier verwendet?
- [ ] Python 3.11 code, nicht 3.12?

---

**Status:** Ready | **Next Review:** 2026-04-14 | **Owner:** Operator (Inspektor)
