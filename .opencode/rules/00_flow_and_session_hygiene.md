# Flow & Session Hygiene

## Session-Start (zwingend)

Vor jedem Task in dieser Reihenfolge:

1. **CLAUDE.md** lesen — VIRON AI OS, Tool-Stack, Regeln
2. **Docs/skill-router.md** lesen — welcher Skill für die Aufgabe
3. **Relevante Linear-Issues** prüfen auf aktiven Kontext
4. **ORCHESTRATION_SYSTEM.md** bei Content-Aufgaben lesen
5. **Plan (3-7 Schritte)** skizzieren
6. **Operator-Approval** einholen

## Task-Abschluss (zwingend)

1. Code/Config getestet (Error-Handling ok?)
2. Linear Issue updaten (Link, Status, Kontext)
3. Outputs dokumentieren
4. Keine OpenAI/Zapier verwendet?
5. Python 3.11, nicht 3.12?

## Token-Effizienz

- Prägnant, fokussiert auf Essentials
- Code-Snippets nur wenn load-bearing
- KEINE ausschweifenden Erklärungen
- KEINE Wiederholung bekannter Infos

## Verboten

- OpenAI in irgendeiner Form
- Zapier als primäre Lösung
- Python 3.12 Features
- Proprietäre Modellnamen hardcoden
- Notion schreiben (read-only für Agenten)
- Tasks ohne Plan beginnen
