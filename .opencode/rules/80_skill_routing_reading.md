# 80_skill_routing_reading.md (Token-Schutz & Lesedisziplin)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Ressourcenschonende Verarbeitung komplexer Anweisungen

## 1. Die 50-Zeilen-Logik (Initialer Scan)
Scanne beim Betreten eines komplexen Skills (`SKILL.md`) mit chirurgischer Präzision nur den YAML-Header und den Context-Block. Schließe die Datei sofort wieder, wenn der Kontext nicht exakt auf deine aktuelle Sekunde zutrifft, **DENN** blindes Weiterlesen bei einem "Mismatch" verschwendet wertvolle Token und fragmentiert deinen Fokus für die eigentliche Problemlösung.

## 2. Konditionales Lazy-Loading
Öffne referenzierte Payloads, `templates/` oder `examples/` ausschließlich dann, wenn die Bedingung der Routing-Matrix erfüllt ist. Widerstehe dem Impuls, ganze Skill-Verzeichnisse präventiv zu laden, **DENN** Lazy-Loading hält dein Kurzzeitgedächtnis frei für logische Operationen und verhindert den Absturz durch Kontext-Überladung.

## 3. Verankerung im Gold-Standard
Lade bei einem Routing-Treffer zwingend das zugehörige Example via `read` Tool, BEVOR du eigenen Code oder Text generierst, **DENN** diese physische Verankerung im "Gold Standard" des Frameworks garantiert eine fehlerfreie Umsetzung im ersten Versuch.

## 🔗 Light Router (Deep Knowledge & Skills)
- **WENN** du komplexe Workflows delegieren musst ➔ **LIES** `60_orchestration_and_sub_agents.md` (aktive Boot-Regel) und **STARTE** den Skill `.opencode/skills/multi-agent-orchestration/`.
- **WENN** du Code-Reconnaissance für Frameworks betreiben musst ➔ **NAVIGIERE** über das Layer-2-System: **LIES** den thematischen Router in `DOCS/architecture/skill_routers/<TYPE>-analyzers.md`, **DENN** Vorfilterung verhindert Rauschen.
- **WENN** du die detaillierte Lesedisziplin als Heavy Payload benötigst ➔ **LIES** `DOCS/architecture/concepts/opencode_knowledge/87_skill_routing_reading.md`.

