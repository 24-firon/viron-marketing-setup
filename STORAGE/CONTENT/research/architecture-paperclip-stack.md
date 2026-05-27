
# Paperclip-basierte AI-Agenten-Infrastruktur 2026

## Zielbild und Kontext

Dieses Dokument beschreibt eine praxisnahe Architektur, in der Paperclip als Orchestrierungsschicht über mehreren Agent-Runtimes (z.B. OpenClaw, Claude Code, Codex) läuft und in eine selbstgehostete Infrastruktur mit Traefik, OpenBao/Vault, Postgres und externen LLM-APIs eingebettet ist.[web:1][web:3][web:4][web:6][web:9][web:15]

## Kernkomponenten

| Ebene | Komponente | Rolle |
|-------|-----------|-------|
| Orchestrierung | Paperclip Server (Node.js) | Modelliert Agenten als "Company", verwaltet Org-Chart, Budgets, Governance, Ticketing und Kosten-Tracking.[web:1][web:3][web:4][web:9] |
| Agent-Runtimes | OpenClaw, Claude Code, Codex, Bash/HTTP-Connectoren | Führen die eigentliche Arbeit aus (Code-Ausführung, API-Calls, Dateisystemzugriffe).[web:1][web:3][web:4][web:9][web:13] |
| Persistenz | Postgres (embedded oder extern) | Speichert Tickets, Runs, Agent-Definitionen, Budget-Events und Audit-Logs.[web:1][web:3][web:4][web:6][web:9] |
| Netzwerk/Ingress | Traefik | Reverse-Proxy für Paperclip-UI/API und ggf. selbstgehostete Modellendpunkte, TLS-Termination.[web:2][web:8][web:11] |
| Secrets & Policies | OpenBao/Vault | Verwaltung von API-Keys (LLM-Provider, Git, SaaS), Rotationen und Zugriffspolicies für Agent-Runtimes.[web:2][web:8] |
| Externe LLM-APIs | z.B. Gemini (Vertex AI), Bedrock, OpenAI, Anthropic | Hochwertige Modelle für komplexe Aufgaben; werden von Agent-Runtimes via API genutzt.[web:2][web:5][web:9][web:13] |

## Laufzeit-Flows

1. Ein Benutzer oder ein nachgelagerter Automations-Trigger erstellt ein Ticket im Paperclip-Board (z.B. "Baue Landing-Page für neuen Kunden").[web:1][web:3][web:4][web:9]
2. Paperclip routet dieses Ticket anhand des Org-Charts an passende Agenten (z.B. "CTO-Agent", "Marketing-Agent"), inklusive Budget-Limits und Deadlines.[web:1][web:3][web:4][web:6][web:9]
3. Die Agenten laufen typischerweise auf OpenClaw/Claude-Code-Runtimes, holen sich Kontext aus Repos, Datenbanken und APIs und interagieren mit LLM-Backends.[web:1][web:3][web:4][web:6][web:9][web:13]
4. Paperclip trackt Kosten pro Run und pro Ticket; bei Budget-Überschreitung wird der Agent automatisch pausiert und muss manuell wieder freigegeben werden.[web:1][web:3][web:4][web:6][web:9]
5. Ergebnisse werden als Kommentare im Ticket abgelegt; nachgelagerte Automationen (CI/CD, Webhooks, n8n) können anhand Ticket-Status reagieren.[web:1][web:3][web:4][web:9]

## Synergien und Abhängigkeiten

- Traefik bündelt HTTPS-Zugriff auf Paperclip-UI, interne Admin-Tools und selbstgehostete Modellendpunkte; die Konfiguration kann Labels aus Docker-Compose nutzen.[web:2][web:8][web:11]
- Vault/OpenBao fungiert als zentraler Secret-Store; Paperclip-Agenten greifen auf kurzlebige Tokens zu, um LLM-APIs und interne Systeme sicher anzusprechen.[web:2][web:8]
- Externe LLM-APIs liefern qualitativ hochwertige Modelle für komplexe Reasoning-Aufgaben; Self-Hosted-Modelle eignen sich eher für spezialisierte, hochfrequente Tasks.[web:2][web:5][web:14]

