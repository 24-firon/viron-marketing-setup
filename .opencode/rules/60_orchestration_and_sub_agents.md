# 60_orchestration_and_sub_agents.md (Die Kunst der Delegation)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Delegation von Aufgaben an Sub-Agenten

## 1. Das 4-Pillar Briefing (Delegations-Mandat)
Statte jeden Sub-Agenten beim Spawnen zwingend mit diesen vier Säulen aus, **DENN** Sub-Agenten starten ohne Kontext und richten ohne präzise Grenzen ("Scope Boundary") massiven Schaden an oder verfallen in redundante Such-Schleifen.
*   **A) Mission:** Kristallklare Definition der Aufgabe ("Why > What").
*   **B) Context Injection:** Essenzielle Verhaltensregeln für die spezifische Rolle.
*   **C) Scope Boundary:** Exakte Dateipfade des "Spielfelds" (z.B. `src/frontend/`).
*   **D) Report-Struktur:** Anweisung zur Ablage der Ergebnisse in Markdown-Tabellen im `REPORTS/` Verzeichnis.

## 2. Rauschfreie Kommunikation & asynchroner Flow
Leite Sub-Agenten an, Diffs und Logs ausschließlich in `REPORTS/` zu sammeln, anstatt den Haupt-Chat zu fluten. Schreite erst zum nächsten Schritt voran, wenn der aktuelle physisch als `✅ DONE` markiert ist, **DENN** ein rauschfreier Kanal schützt den Fokus des Orchestrators und ermöglicht eine fehlerfreie Überwachung des Fortschritts.

## 3. Blocker Integrity (Transparenz statt Workarounds)
Friere den Prozess bei Tool-Errors oder fehlenden Berechtigungen sofort ein und melde den Blocker dem Operator, anstatt im Verborgenen unreflektierte Workarounds zu versuchen, **DENN** transparente Telemetrie beschleunigt die Lösungsfindung und verhindert korrumpierte Systemstände durch "Ghost-Fixes".

## 🔗 Light Router (Deep Knowledge & Skills)
- **WENN** du komplexe Multi-Agent-Systeme entwirfst oder koordinierst ➔ **STARTE** den Skill `.opencode/skills/multi-agent-orchestration/`.
- **WENN** du das vollständige Orchestrierungs-Handbuch als Heavy Payload benötigst ➔ **LIES** `DOCS/architecture/concepts/opencode_knowledge/70_orchestration_and_sub_agents.md`.
