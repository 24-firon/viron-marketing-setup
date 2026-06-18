# P99 — Session Abschluss (Kompakt)

<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Session-Abschluss-Prompt mit 6 Schritten (Report → Handover → Tasks → Walkthrough → Ritual → P00-Fragen)
> - Wird als NACHRICHT im Chat ausgelöst, nicht als Template kopiert
> - Nur für Modus 2 (Normal) und Modus 3 (Ausführlich)
>
> - **Bundle-Verwendung:** Template-Quelle: `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/`. Arbeitskopie: `DESK/HANDOVER.md`. P99 wird NICHT nach DESK kopiert — es ist ein PROMPT, kein Template. Nicht alle Bundle-Dateien müssen genutzt werden.
<!-- TEMPLATE-EXPLANATION-END -->

> **AM ENDE jeder Session.** Führe alle 6 Schritte aus, **DENN** ohne sauberen Abschluss startet der nächste Agent bei Null.

## 6 SCHRITTE

### Schritt 0: README.md lesen
Lies `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/README.md`. Die README erklärt die 3 Modi (Schnell/Normal/Ausführlich). P99 macht NUR den Abschluss. Die README ist der Einstieg.

### 1. REPORT SCHREIBEN
Pfad: `DESK/reports/[SESSION-NAME]_[YYYY-MM-DD].md`

Struktur (9 Sektionen, forensisch):
- Systemlage (1-3 Absätze: Ausgangslage)
- Architektur-Entscheidungen (was + warum)
- Geänderte Dateien (Pfad + Was)
- Nicht-Änderungen (was bewusst nicht angefasst)
- Diagnostik (VERIFIZIERT / WAHRSCHEINLICH / OFFEN)
- Risiken (Beschreibung + Auswirkung + Wahrscheinlichkeit)
- Handover (was nächster Agent tun soll)
- Kurzfazit (1 Satz)

### 2. HANDOVER BEFÜLLEN
Pfad: `DESK/HANDOVER.md`

Pflicht-Felder:
- BLUF (1 Satz)
- Projektspezifische Daten (IPs, Ports, Configs — was NIERGENDS anders steht)
- Erledigte Arbeit
- Offene Tasks
- Bekannte Probleme + Workarounds
- Nächste Schritte

### 3. CURRENT_TASKLIST AKTUALISIEREN
Pfad: `DESK/TASKS/active/CURRENT_TASKLIST.md` (oder wo auch immer)

- Erledigte Tasks abhaken
- Neue Tasks hinzufügen (falls in dieser Session entstanden)
- DoD pro Silo aktualisieren

### 4. WALKTHROUGH ERGÄNZEN
Pfad: `DESK/WALKTHROUGH.md` (oder wo auch immer)

Neuer Eintrag:
```
## [Datum] — [Session-Typ]

### Was wurde gemacht
- [Schritt] → [Ergebnis]

### Geänderte Dateien
- `[Pfad]` — [Was]

### Entscheidungen
- [Entscheidung] — [Begründung]
```

### 5. SESSION-RITUAL ABARBEITEN
5 Säulen, alle GRÜN:

| Säule | Verifikation |
|:---|:---|
| 1. todowwrite | Keine pending Tasks |
| 2. Cleanup | Keine .tmp/.log Files im Workspace |
| 3. Report | `DESK/reports/[SESSION].md` existiert |
| 4. Git-Status | `git status` clean oder staged |
| 5. Abschluss-Marker | Bestätigung an Operator |

### 6. P00-FRAGEN FÜR NÄCHSTEN AGENTEN
Schreibe 3-5 neue Fragen in `P00_BOOTSTRAP.md` Section „7 FRAGEN" oder in die HANDOVER-Datei.

**Gute Fragen** testen ANWENDUNG:
- "Was passiert wenn du diese Datei ignorierst?"
- "Welche Konsequenzen hat ein Fehler hier?"

**Schlechte Fragen** testen RECALL:
- "Was steht in dieser Datei?" (zu leicht)
- "Wie heißt die Regel?" (zu mechanisch)

## BESTÄTIGUNG

> "P99 abgeschlossen. Report unter [Pfad]. HANDOVER.md abgelegt. Tasks clean. Workspace clean. P00-Fragen geschrieben."

⏸️ **STOPP** — Nächstes Modell: ⚡ LIGHT. Warte auf GO vom Operator.
