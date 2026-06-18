# SESSION RITUAL (Kompakt)

> 5-Säulen-Checkliste. Alle GRÜN = Session sauber abgeschlossen. **DENN** eine Session ohne Ritual startet der nächste Agent bei Null.

## 5 SÄULEN

### 1. BUCHHALTUNG (todowrite)
- Setze JEDEN Task der Session auf `completed` oder `cancelled`
- **Verifikation:** Keine Tasks im Status `in_progress` oder `pending`
- **Was passiert wenn nicht:** Nächster Agent sieht offene Tasks und weiß nicht ob sie erledigt sind
- **Status Session 2026-06-17:** ⚠️ TEILWEISE — todowrite wurde nicht systematisch geführt, aber alle erledigten Tasks sind in CURRENT_TASKLIST.md (Silo 01-03) abgehakt. 7 Spec-TODOs in Silo 04 offen. 6 M3-Tasks in Silo 05 offen. 3 Hygiene-Tasks in Silo 06 offen.

### 2. ARTEFAKT-HYGIENE (Workspace-Cleanup)
- Lösche temporäre Dateien: `.tmp`, `.log`, `.fake`, `.json`-Dumps
- **Verifikation:** `ls` oder `glob` zeigt keine verwaisten Drafts
- **Was passiert wenn nicht:** Nächster Agent liest temporäre Dateien und verwechselt sie mit echten Artefakten
- **Status Session 2026-06-17:** ✅ GRÜN — Keine temporären Dateien. Working tree clean (0 uncommitted, 0 untracked, 0 ahead). 1 untracked: `HANDOVER/GSD graphify command spec (fork #2)/` (wird noch committed).

### 3. BEWEISSICHERUNG (Report-Pflicht)
- Strukturierter Report unter `DESK/reports/[SESSION].md`
- **Verifikation:** Der Report muss physisch existieren
- **Was passiert wenn nicht:** Nächster Agent weiß nicht was passiert ist und fängt von vorne an
- **Status Session 2026-06-17:** ✅ GRÜN — `DESK/REPORTS/dach-p0-skills-build.md` existiert (Build-Report mit 7 Spec-TODOs, 13 Korrekturen, Lessons Learned). Plus `HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/SESSION_HANDOVER.md` (Forensischer Bericht).

### 4. GIT-STATUS (Versions-Integrität)
- Führe `git status` aus
- **Verifikation:** `git status` muss `clean` oder `staged` zeigen
- **Was passiert wenn nicht:** Uncommitteter Code geht bei einem Reset verloren
- **Status Session 2026-06-17:** ⚠️ TEILWEISE — Working tree aktuell mit 1 untracked Ordner (`HANDOVER/GSD graphify command spec (fork #2)/`) und 2 untracked Dateien (innerhalb dieses Ordners). MUSS noch committet werden. 4 Commits bereits auf origin/main: 666a6a3, 80391bb, 39b9012, 4c1366a.

### 5. ABSCHLUSS-MARKER
- Erst wenn alle 4 vorherigen GRÜN:
> "Session sauber abgeschlossen. Alle Artefakte gesichert, Workspace ist clean."
- **Status Session 2026-06-17:** ⚠️ TEILWEISE — Säule 1 (Buchhaltung), 3 (Beweissicherung) GRÜN. Säule 2 (Artefakt-Hygiene) GRÜN. Säule 4 (Git-Status) TEILWEISE — untracked Handover-Ordner muss noch committed werden. **Session NICHT sauber abgeschlossen.**

## REPORT-MUSTER (gutes Beispiel)

```markdown
# SESSION REPORT — [Datum]

## Was wurde getan?
- [X] Dateien erstellt
- [Y] Dateien geändert

## Was wurde nicht getan?
- [Z] Task konnte nicht abgeschlossen werden weil [Grund]

## Evidence
[Terminal-Output / Git-Diff]

## Lese-Beweise
| Datei | Beweis |
|:---|:---|
| [Pfad] | "Gelesen: X Zeilen, Inhalt Y" |
```

## WAS PASSIERT WENN EINE SÄULE NICHT GRÜN IST?

- **Säule 1 (todowrite):** Fehlende Einträge erstellen BEVOR du fortfährst
- **Säule 2 (Cleanup):** Temporäre Dateien löschen BEVOR du fortfährst
- **Säule 3 (Report):** Report erstellen BEVOR du fortfährst
- **Säule 4 (git status):** Änderungen stage oder commit BEVOR du fortfährst
- **Säule 5 (Marker):** Erst wenn alle 4 vorherigen GRÜN

**Golden:** Keine Abkürzungen. Jede Säule muss physisch verifiziert werden.
