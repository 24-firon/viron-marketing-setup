# TASK ENVELOPE — ATOMARE AUFGABE FÜR SUB-AGENT

> **Zweck:** Dieser Envelope enthält alle Informationen, die ein Sub-Agent für die fehlerfreie, isolierte Ausführung einer atomaren Aufgabe benötigt. Der Sub-Agent erhält KEINE Chat-Historie — nur diesen Umschlag.

---

## ENVELOPE-STRUKTUR

```
TASKS/[TASK-ID]_[Kurzbeschreibung]/
├── PROMPT_INITIAL.md     # Die wasserdichte Marschroute
├── context/              # Relevante Dokumente & API-Doku-Schnipsel
│   ├── referenz1.md
│   └── referenz2.md
├── STATE.md              # Temporärer Status — wird während der Arbeit aktualisiert
└── SUMMARY.md            # Finales Protokoll — wird NACH Abschluss befüllt
```

---

## PROMPT_INITIAL.md (Inhalt)

```markdown
# TASK: [TASK-ID] — [Titel]

## 1. MISSION
[Das "Warum": Kurze Erklärung des architektonischen Sinns der Aufgabe]

## 2. CONTEXT (SSoT-Wissen)
LIES diese Dateien zwingend VOR der Ausführung:
- [Pfad zu relevanter Datei 1]
- [Pfad zu relevanter Datei 2]

## 3. SCOPE (Die Handschellen)
Du darfst NUR folgende Dateien/Ordner modifizieren:
- [Erlaubter Pfad 1]
- [Erlaubter Pfad 2]

Du darfst NIEMALS folgende Dateien/Ordner anfassen:
- [Verbotener Pfad 1]
- [Verbotener Pfad 2]

## 4. ATOMAREN SCHRITTE
1. [Schritt 1 — exakter Befehl/Tool-Call]
2. [Schritt 2 — exakter Befehl/Tool-Call]
3. [Schritt 3 — exakter Befehl/Tool-Call]

## 5. REPORT-ZWANG
Deine Ergebnisse MÜSSEN als strukturierte Markdown-Datei abgelegt werden:
- `DESK/reports/[TASK-ID]_[datum].md`
```

---

## STATE.md (Während der Arbeit)

```markdown
# STATE — [TASK-ID]

**Status:** [WORKING / WAITING_APPROVAL / DONE / FAILED]
**Gestartet:** [Datum, Uhrzeit]
**Letztes Update:** [Datum, Uhrzeit]

## Aktueller Fortschritt
- [ ] Schritt 1 abgeschlossen
- [ ] Schritt 2 abgeschlossen
- [ ] Schritt 3 in Arbeit

## Notizen
[Freitext — Probleme, Entscheidungen, offene Fragen]
```

---

## SUMMARY.md (Nach Abschluss)

```markdown
# SUMMARY — [TASK-ID]

**Status:** [DONE / FAILED / PARTIAL]
**Abgeschlossen:** [Datum, Uhrzeit]

## Was wurde getan?
- [Ergebnis 1]
- [Ergebnis 2]

## Was wurde nicht getan?
- [Nicht erledigt + Grund]

## Evidence
```
[Terminal-Output / Git-Diff / Log-Auszug]
```

## Nächste Schritte
1. [Empfehlung für den Master-Orchestrator]
```

---

> **Envelope bereit für Sub-Agent-Spawn.** Alle Artefakte (PROMPT_INITIAL, context/, STATE.md, SUMMARY.md) sind definiert.
