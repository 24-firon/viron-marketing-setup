# VIRON: Technical Infrastructure Blueprint 2026

## 1. Hosting & Orchestration
*   **Provider:** Hetzner Cloud (ARM64 oder x86 High-Performance Instanzen). Unschlagbares Preis-Leistungs-Verhältnis für KMU-Budgets.
*   **Orchestration:** Coolify. (Dein privates Vercel). Ersetzt teure PaaS-Lösungen. Hier deployst du Docker-Container mit einem Klick.
*   **Automation Engine:** n8n (Self-Hosted via Coolify). Keine Task-Limits, keine monatlichen Zapier-Kosten.

## 2. Database & Storage
*   **Relational/Vector:** PostgreSQL mit `pgvector`. (Ersetzt teure Vektordatenbanken wie Pinecone).
*   **Knowledge Graph:** Neo4j (für GraphRAG-Implementierungen bei Kunden).

## 3. AI & Context Management
*   **Protokoll:** MCP (Model Context Protocol). Jeder Agent (Claude Code, AntiGravity) verbindet sich via MCP mit n8n, Linear und Notion.
*   **Modelle:** Open-Source-Fokus für Kunden (Llama-3, DeepSeek v3) um API-Kosten zu minimieren, OpenAI/Anthropic für komplexe interne R&D.

## 4. Security & Error Handling
*   **SIGTERM-Handling:** Sauberes Herunterfahren von n8n-Workern in Fargate/Hetzner, um Datenverlust zu verhindern.
*   **Proxies:** Residential Proxies für alle Social-Scraping und Outreach-Workflows, um Account-Bans (z.B. Instagram Outreach System) zu verhindern.
