# DECISIONS.md — marketing-setup

## Entscheidungslog

---

### ADR-001: Markdown-first statt Notion-native Dokumentation

- **Datum:** 2026-05
- **Status:** Akzeptiert
- **Kontext:** Alle gesammelten Marketing-Ressourcen (Freebies, Templates, SOPs) lagen bisher in Notion. KI-Agenten können Notion-Seiten nur über API oder MCP lesen, was eine externe Abhängigkeit erzeugt. Im Repo selbst als Markdown sind sie sofort verfügbar, versionierbar und diff-bar.
- **Entscheidung:** Alle operativ genutzten Templates und Referenzdokumente werden als Markdown ins Repo portiert. Notion bleibt als Recherche- und Sammelort, aber nicht als primäre Wahrheitsquelle für aktive Workflows.
- **Verworfene Alternative:** Alles in Notion lassen und Agent über n8n-Webhook immer bei Bedarf anfragen.
- **Warum Markdown gewonnen:** Schneller, zuverlässiger, kein API-Roundtrip bei einfachen Lookups, versionierbar, kein Single Point of Failure.
- **Tradeoffs:** Manuelle Portierung von Notion → Markdown nötig. Doppelter Pflegeaufwand, wenn beide Systeme synchron gehalten werden sollen (wird vorerst vermieden: Notion ist readonly-Referenz).
- **Folgen:** Agent muss immer `/research/swipe/` und `/templates/` prüfen, bevor er Notion fragt.

---

### ADR-002: LiteLLM als LLM-Router, kein direkter API-Zugriff

- **Datum:** 2026-05
- **Status:** Akzeptiert
- **Kontext:** Marketing-Workflows erfordern verschiedene LLM-Qualitätsstufen: Hochwertige Copy braucht Claude Sonnet oder Opus, Klassifikation und Tagging sind auch mit günstigeren Modellen lösbar.
- **Entscheidung:** Alle LLM-Calls aus Marketing-Workflows gehen über LiteLLM-Proxy. Kein direkter Anthropic- oder OpenAI-API-Call aus dem Marketing-Repo heraus.
- **Verworfene Alternative:** Direkte API-Calls je nach Kontext mit hartkodiertem Modellnamen.
- **Warum LiteLLM gewonnen:** Zentrale Kostenkontrolle, einfacher Modellwechsel, Retry-Logik, Fallbacks konfigurierbar.
- **Tradeoffs:** LiteLLM-Proxy muss laufen. Wenn er down ist, blockiert das alle Marketing-LLM-Workflows.
- **Folgen:** In allen LLM-Prompt-Skripten (`/workflows/prompts/`) wird ausschließlich der LiteLLM-Proxy-Endpoint referenziert. Kein hartkodierter Modellname in Templates.

---

### ADR-003: Linear als Execution-Layer, kein vollständiges Wissensarchiv

- **Datum:** 2026-05
- **Status:** Akzeptiert
- **Kontext:** Versuchung bestand, alle Architekturdokumente, Templates und Strategiepapiere auch in Linear zu verlinken, um alles an einem Ort zu haben.
- **Entscheidung:** Linear enthält nur konkrete ausführbare Aufgaben (Issues) mit klaren Status-Übergängen. Kein Freitext-Wissensarchiv in Linear. Tickets verlinken auf CONTEXT.md, Notion oder spezifische Repo-Dateien.
- **Verworfene Alternative:** Linear als Hybrid-Tool für Tasks UND Dokumentation.
- **Warum diese Entscheidung:** Linear-Issues werden heiß und alt. Wenn Architekturdokumentation in veralteten Issues steckt, führt das zu Konfusion. Docs gehören ins Repo.
- **Tradeoffs:** Agent muss zwei Orte kennen (Linear für Tasks, Repo für Kontext).
- **Folgen:** Jedes aktive Linear-Issue muss in der `CONTEXT.md` des Repos referenziert werden, damit der Agent den Bezug herstellen kann.

---

### ADR-004: n8n nur für Hintergrund-Sync, kein kritischer Pfad

- **Datum:** 2026-05
- **Status:** Akzeptiert
- **Kontext:** n8n ist noch im Aufbau. Die Versuchung bestand, sofort eine vollautomatische Linear-Notion-Sync-Pipeline zu bauen.
- **Entscheidung:** n8n-Workflows in diesem Repo sind Hintergrund-Convenience, kein kritischer Pfad. Wenn n8n ausfällt oder noch nicht eingerichtet ist, muss der Agent trotzdem vollständig arbeitsfähig bleiben.
- **Verworfene Alternative:** n8n als Haupt-Orchestrator, Agent hängt von n8n-Responses ab.
- **Warum diese Entscheidung:** Solo-Betrieb. Kein Ops-Team, das n8n-Ausfälle sofort behebt. Robustheit vor Eleganz.
- **Tradeoffs:** Manueller Mehraufwand bei Status-Updates solange n8n nicht läuft.
- **Folgen:** Agenten-Prompts enthalten explizit die Anweisung, bei fehlendem n8n-Sync den Status manuell in CONTEXT.md zu dokumentieren.
