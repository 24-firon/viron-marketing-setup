# P02 — Session Init (Kompakt)

> **EXECUTION-MODE.** Comprehension Gate, dann Meilensteine abarbeiten. **DENN** ohne Hard-Stop springt der Agent blind zu Aktionen.

## COMPREHENSION GATE 2 (HARD STOP)

BEVOR du mit der Arbeit beginnst, alle 3 Schritte:

### Schritt A: Injizierten Kontext sichten
- Welche 15 Regeln sind injiziert? (siehe opencode.jsonc)
- Welche Architektur-Konzepte sind aktiv? (siehe P00 Section 4)
- **BEWEIS:** "Ich habe die injizierten Dateien verarbeitet. 3 kritischste Lücken: [1] [2] [3]"

### Schritt B: Task-spezifische Dateien lesen
- Alle Tier-1-Dateien aus P01 (physisch geladen)
- Domain-spezifische Context-Dateien

### Schritt C: Bestätigung
> "Comprehension Gate bestanden. [X] injizierte Dateien, [Y] Tier-1-Dateien gelesen. Bereit für operative Arbeit."

**Ohne Bestätigung: KEINE EDITS. KEINE BASH-BEFEHLE. KEINE SUB-AGENTS.**

## REGEL-AKTIVIERUNG (vor jedem Schritt)

| Schritt | Regel-Zitat | Zweck |
|:---|:---|:---|
| Datei lesen | "Gemäß Forensisches Lese-Primat lese ich..." | Beweis vor Behauptung |
| Datei vergleichen | "Gemäß Zero-Assumption vergleiche ich..." | Keine Annahmen |
| Datei erstellen | "Gemäß Pre-Flight Radar verschaffe ich mir Lagebild" | Sicherheit vor Aktion |
| Evidence zeigen | "Gemäß Evidence-Based Execution zeige ich Output" | Keine Erfolgs-Behauptung |

## MEILENSTEINE (anpassen für deine Session)

### M1: [Name der ersten Phase]
- [ ] Schritt 1: [konkrete Aktion mit Befehl oder Tool-Call]
- [ ] Schritt 2: [konkrete Aktion]

⏸️ **STOPP 1** — Berichte Ergebnis. Zeige letzte 5 Zeilen Output. Warte auf GO.

### M2: [Name der zweiten Phase]
- [ ] Schritt 1
- [ ] Schritt 2

⏸️ **STOPP 2** — Berichte Ergebnis. Warte auf GO.

### M3: [Name der dritten Phase]
- [ ] Schritt 1
- [ ] Schritt 2

⏸️ **STOPP 3** — Abschluss. Vorbereitung für P99.

## MODELL-ROTATION (Eisenhart)

**🛑 HARTER STOPP bei JEDEM Modell-Wechsel.** Das System darf nicht ohne explizites "Go" vom Operator weitermachen.

| Phase | Modell | Zweck |
|:---|:---|:---|
| Planung (M1-Vorbereitung) | 🔴 STARK | Reasoning |
| Ausführung (M1-M3) | 🟢 STANDARD | Code, Bash |
| Status-Checks (zwischendurch) | ⚡ LIGHT | Grep, Logs |
| STOPP-Berichte | 🔴 STARK | Evidence-Bewertung |

## MINDSET-BLOCK

- **Surgical Precision:** Ändere Dateien nur nativ (`edit` / `write`)
- **Evidence-Based Execution:** Traue keinem `exit 0` — liefere Output
- **Linearer Gehorsam:** Schritte nacheinander, nicht parallelisieren
- **Approval-Gates:** Kritische Aktionen brauchen "GO" vom Operator
- **Lab-First:** Neue Ideen erst im eigenen Workspace testen, dann in `src/rules/` promoten

## 4 GESETZE DER PERSISTENZ

1. **KEINE LÖSCHUNG** — Archivieren, nicht löschen
2. **KEINE REDUKTION** — 100% Code-Erhalt, keine `//...`-Abkürzungen
3. **BEWEISPFLICHT** — Physische Artefakte (Reports, Diffs), nicht Chat-Text
4. **INTEGRATION** — Korrekturen an die richtige Stelle, nicht ans Ende

## BESTÄTIGUNG

> "P02 initialisiert. Gate bestanden. [X] Meilensteine definiert. Bereit für Ausführung."

⏸️ **STOPP** — Nächstes Modell: 🟢 STANDARD.
