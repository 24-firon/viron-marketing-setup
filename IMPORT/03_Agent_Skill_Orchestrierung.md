# VIRON Research Report #3
# Agent-Skill-Orchestrierung: Best Practices für 30+ Skills
# Token-Optimierung, Architektur-Patterns & Produktions-Frameworks

---

## Executive Summary

Die Orchestrierung von 30+ Marketing-Skills erfordert ein durchdachtes Architektur-Design, um Token-Blowout zu vermeiden und maximale Agent-Effektivität zu gewährleisten. Dieser Bericht basiert auf Community-Erfahrungen, Microsoft Azure Architecture Patterns und Claude Code Best Practices aus Produktionsumgebungen [web:34][web:36][web:115].

---

## 3.1 Die Token-Realität: Zahlen & Kosten

### Baseline-Kosten pro Skill-Set

| Konfiguration | Relative Token-Kosten | Real-World Beispiel |
|--------------|----------------------|---------------------|
| Single Agent + 5 Skills | 1.0x Baseline | Standard Claude Code Session |
| Single Agent + 15 Skills | 5-7x Baseline | Vollständiges Marketing-Bundle |
| Multi-Agent (3 Agents) + 15 Skills | 15x Baseline | Coordinator + 2 Specialists |
| Multi-Agent (5 Agents) + 30 Skills | 25-35x Baseline | Full Campaign Team |

**Quelle:** Claude Code Community Benchmarks [web:38][web:44]

### Kostenimplikationen

Bei aktuellen API-Preisen (Claude Sonnet 4 $/Mio Input Tokens, 20 $/Mio Output Tokens):

- **30 Skills lazy loaded:** ~$0.50-1.50 pro Session
- **30 Skills eager loaded:** ~$3.00-8.00 pro Session
- **Multi-Agent (5x) eager loaded:** ~$15.00-40.00 pro Session

**Kritische Erkenntnis:** Token-Blowout ist kein theoretisches Problem – es kann die Kosten pro Kundeninteraktion um 10-20x steigern und Margen komplett eliminieren [web:38].

---

## 3.2 Architektur-Patterns für Skill-Orchestrierung

### 3.2.1 Hierarchisches Coordinator-Pattern (Empfohlen)

**Struktur:**
```
┌─────────────────────────────────────────┐
│         Coordinator Agent               │
│    (Planung, Routing, Quality Gates)    │
└──────────────┬──────────────────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
┌───▼───┐ ┌──▼────┐ ┌──▼────┐
│Content │ │Social │ │Analytics│
│ Agent  │ │ Agent │ │ Agent  │
└────────┘ └───────┘ └────────┘
```

**Regeln:**
- Coordinator entscheidet WELCHER Subagent aktiv wird
- Subagents erhalten NUR ihre spezialisierten Skills
- Subagents haben KEINEN Zugriff auf Coordinator-Kontext
- Coordinator führt Ergebnisse zusammen

**Token-Einsparung:** ~70% vs. flat loading aller Skills [web:36]

**Implementation:**
```yaml
# .agent.md Format (Claude Code)
name: marketing-coordinator
model: claude-sonnet-4
system: |
  You are a marketing coordinator. Your job is to:
  1. Analyze the user's request
  2. Select the appropriate specialist agent(s)
  3. Provide them with ONLY the relevant context
  4. Synthesize results into a cohesive strategy

agents:
  content:
    description: "Content creation, copywriting, SEO"
    skills: [copywriting, seo, content-strategy]
    model: claude-sonnet-4

  social:
    description: "Social media management and scheduling"
    skills: [social, content-strategy, image]
    model: claude-sonnet-4

  analytics:
    description: "Data analysis, reporting, CRO"
    skills: [cro, analytics, customer-research]
    model: claude-sonnet-4

handoff:
  user-invocable: false  # Only coordinator can invoke
```

---

### 3.2.2 Lazy Loading / Progressive Disclosure Pattern

**Problem:** 30 Skills mit Full Schemas = ~30.000-50.000 Tokens System Prompt

**Lösung:** Two-Step Discovery [web:35][web:44]

**Step 1: Skill Directory (Menu)**
```markdown
## Available Marketing Skills

1. **copywriting** - Ad copy, landing pages, email sequences
2. **seo** - Technical SEO, keyword research, content optimization  
3. **cro** - A/B testing, conversion optimization, funnel analysis
4. **social** - Social media strategy, content calendars, community management
5. **analytics** - GA4 setup, reporting, dashboard creation
... (30 skills total)
```
*Size: ~1.500 Tokens*

**Step 2: Full Schema (on demand)**
```markdown
## Skill: copywriting
### Full Instructions
[Complete skill schema with examples, parameters, output formats]
```
*Size: ~2.000-3.000 Tokens pro Skill*

**Token-Einsparung:** 5-10x bei Nicht-Nutzung aller Skills [web:35]

---

### 3.2.3 Context Reducer / MCP-Agent-Pattern

**Problem:** Externe MCP-Server (GitHub, Stripe, Notion) überladen den Agent mit Kontext [web:120].

**Lösung:** Dedizierter MCP-Agent [web:120]

```
User Request → Coordinator → Specialist Agent → MCP Client Tool
                                    │
                                    ▼
                           Dedicated MCP Agent
                           (GitHub / Stripe / Notion)
                                    │
                                    ▼
                           Clean Result zurück
```

**Vorteile:**
- Specialist Agent hat nur 1 Tool statt 10+ MCPs
- MCP-Agent spezialisiert sich auf API-Operations
- 80% Kontext-Reduktion bei komplexen Workflows [web:120]

---

### 3.2.4 State-Management Pattern

**Problem:** Agenten verlieren Kontext zwischen Sessions.

**Lösung:** Persistent State Files [web:33][web:36]

**File-Struktur:**
```
.viron/
├── AGENTS.md           # Alle Agents, ihre Skills, Interaktionsregeln
├── MEMORY.md           # Gesammelte Entscheidungen, Learnings
├── state.json          # Machine-readable Session State
├── skills/
│   ├── active/         # Aktuell geladene Skills
│   └── archive/        # Inaktive Skills
└── sessions/
    └── 2026-05-23/     # Session-spezifische Logs
```

**MEMORY.md Format:**
```markdown
# Marketing Decisions Log

## 2026-05-23: Brand Voice Definition
- Decision: Professional but approachable, German formal "Sie"
- Context: Client X prefers traditional German business tone
- Impact: All copywriting skills should use this voice

## 2026-05-23: SEO Strategy
- Decision: Focus on long-tail keywords first
- Context: Client Y has low domain authority
- Impact: seo skill prioritizes low-competition keywords
```

---

## 3.3 Token-Optimierung: Taktiken & Implementierung

### 3.3.1 Skill-Namespaces & Präfixe

**Anti-Pattern:**
```markdown
## send_message
## create_issue
## update_contact
```
*Agent kann nicht unterscheiden, welcher Service gemeint ist*

**Best Practice:**
```markdown
## slack_send_message
## jira_create_issue
## hubspot_update_contact
```
*Präfixe reduzieren Ambiguität und verhindern falsche Tool-Aufrufe [web:35]*

---

### 3.3.2 Conditional Instructions

**Anti-Pattern:**
```markdown
## Wenn du ein Bild erstellen musst, verwende DALL-E.
## Wenn du Daten analysieren musst, verwende Code Interpreter.
## Wenn du eine Rechnung erstellen musst, verwende Stripe API.
```
*Alle Instructions sind immer im Kontext, auch wenn nicht relevant*

**Best Practice:**
```markdown
## image skill
### Trigger: User requests visual content
### Instructions: [Nur laden wenn Trigger aktiv]

## analytics skill  
### Trigger: User requests data analysis
### Instructions: [Nur laden wenn Trigger aktiv]
```
*Lazy Loading durch explizite Trigger-Bedingungen [web:41]*

---

### 3.3.3 Prompt Caching Strategie

**Statische Teile an den Anfang:**
```markdown
[System Prompt - Static]
You are a marketing expert for DACH-KMUs.
Your tone is professional but approachable.
You always consider DSGVO compliance.

[Skills Menu - Semi-Static]  
Available skills: copywriting, seo, social...

[Dynamic Context]
Current client: VIRON
Current task: Write LinkedIn post about GEO

[User Message]
Write a LinkedIn post about GEO trends 2026.
```

**Caching-Regeln:**
- Statische Teile (System, Skills Menu) werden gecached
- Dynamische Teile (Context, User Message) sind uncached
- **Einsparung:** ~75% der Input-Token-Kosten für gecachte Teile [web:32]

---

### 3.3.4 Model Selection Strategy

**Nicht alle Tasks brauchen Claude Sonnet:**

| Task Type | Empfohlenes Model | Grund |
|-----------|------------------|-------|
| Routing & Planning | Claude Haiku | Einfache Logik, schnell |
| Content Drafting | Claude Sonnet | Kreativität + Qualität |
| Code/Technical SEO | Claude Opus | Komplexe Implementierung |
| Data Analysis | GPT-4o | Bester Code Interpreter |
| Image Analysis | Gemini Pro Vision | Multimodal Strength |

**Cost Optimization:** 28.4% Einsparung durch richtiges Model-Matching [web:36]

---

## 3.4 Produktions-Framework für VIRON

### 3.4.1 Empfohlene Agent-Architektur

**VIRON Marketing System (5 Agents):**

```yaml
# .viron/agents.yaml
agents:
  coordinator:
    name: "VIRON Marketing Coordinator"
    model: claude-sonnet-4
    skills: [project-management, client-briefing]
    role: "Analysiert Anfragen, routet zu Specialists, synthetisiert Ergebnisse"

  strategist:
    name: "VIRON Strategy Agent"
    model: claude-sonnet-4
    skills: [customer-research, competitor-profiling, content-strategy, pricing]
    role: "Entwickelt Marketing-Strategien, Research, Positionierung"

  creative:
    name: "VIRON Creative Agent"
    model: claude-sonnet-4
    skills: [copywriting, image, video, marketing-psychology, launch]
    role: "Erstellt Content, Copy, Creative Assets"

  performance:
    name: "VIRON Performance Agent"
    model: claude-sonnet-4
    skills: [cro, social, directory-submissions, seo]
    role: "Optimiert Kampagnen, Tracking, CRO, Social Media"

  technical:
    name: "VIRON Technical Agent"
    model: claude-opus-4
    skills: [analytics, geo, first-party-data, lifecycle-marketing]
    role: "Implementiert technische Lösungen, Tracking, Automation"
```

---

### 3.4.2 Skill-Lifecycle-Management

**Versionierung:**
```
skills/
├── v1.0/          # Stable, produktionsreif
│   ├── copywriting/
│   ├── seo/
│   └── cro/
├── v1.1-beta/     # In Entwicklung
│   ├── geo/       # Neue Skills
│   └── lifecycle/
└── archive/       # Deprecated
    └── old-social/
```

**Update-Prozess:**
1. Skills werden beim ersten Gebrauch auf Updates geprüft [web:109]
2. Agent informiert über verfügbare Updates
3. Manuelle Review vor Installation (kein Auto-Update in Produktion)

---

### 3.4.3 Quality Gates

**Vor jeder Kunden-Interaktion:**

```markdown
## Quality Checklist
- [ ] Relevante Skills sind geladen (nicht alle 33)
- [ ] Client-Kontext ist aktuell (MEMORY.md geprüft)
- [ ] DSGVO-Compliance ist aktiv
- [ ] Output Format ist definiert
- [ ] Review-Loop ist konfiguriert
```

**Nach jeder Session:**
```markdown
## Session Log
- Skills used: [List]
- Tokens consumed: [Count]
- Decisions made: [List]
- Errors encountered: [List]
- Improvements needed: [List]
```

---

## 3.5 Metriken & Monitoring

### 3.5.1 Token-Tracking

**Pro Session tracken:**
- Total Input Tokens
- Total Output Tokens
- Skills loaded (Anzahl)
- Lazy vs. Eager loaded ratio
- Kosten pro Task

**Ziel-KPIs:**
- Average Tokens per Task: < 15.000
- Lazy Load Ratio: > 80%
- Cost per Client Interaction: < $2.00
- Skill Utilization Rate: > 60% (nicht alle Skills idle)

---

### 3.5.2 Performance-Monitoring

**Agent-Effektivität:**
- Task Completion Rate
- Rework Rate (wie oft muss der Agent korrigiert werden)
- Client Satisfaction (manuelles Rating)
- Time to Completion

**Optimierungs-Loop:**
```
Monitor → Analyze → Optimize Skills → Test → Deploy
```

---

## 3.6 Zusammenfassung: Die 10 Goldenen Regeln

1. **Lazy Load Everything** – Skills nur laden wenn benötigt
2. **Namespace your Skills** – Präfixe für eindeutige Identifikation
3. **Use a Coordinator** – Hierarchische Architektur statt flat loading
4. **Cache Static Content** – System Prompts und Skills Menu gecacht halten
5. **Model Match Tasks** – Nicht jeder Task braucht Sonnet/Opus
6. **Persistent State** – MEMORY.md und AGENTS.md als Single Source of Truth
7. **Version your Skills** – Stabile vs. Beta-Skills trennen
8. **Quality Gates** – Vor und nach jeder Session prüfen
9. **Token Budgets** – Pro Kundeninteraktion ein Budget definieren
10. **Monitor & Optimize** – Kontinuierliche Metrik-Erfassung und Verbesserung

---

## 3.7 Action Items

1. **Sofort:** Skill-Namespace-System implementieren (`marketing_`, `technical_`, `creative_`)
2. **Woche 1:** Coordinator-Agent erstellen mit lazy loading für alle 33 Skills
3. **Woche 2:** MEMORY.md und AGENTS.md Templates erstellen
4. **Woche 3:** Token-Tracking pro Session implementieren (einfaches Logging)
5. **Monat 1:** Performance-Monitoring Dashboard (Notion oder einfache DB)
6. **Quartal 1:** Cost-per-Client-Interaction auf <$2.00 optimieren

---

*Bericht generiert: Mai 2026*
