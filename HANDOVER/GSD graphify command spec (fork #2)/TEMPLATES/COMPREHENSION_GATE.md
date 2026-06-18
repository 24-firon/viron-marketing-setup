# COMPREHENSION GATE (Kompakt)

> 3-Schritte-Check der verhindert dass Agenten handeln bevor sie gelesen haben. **DENN** Agenten ignorieren optionale Anweisungen — ein HARD STOP funktioniert.

## DIE 3 SCHRITTE

### Schritt A: Injizierten Kontext sichten
- Lies was in `opencode.jsonc` → `instructions` steht — das sind die Dateien die automatisch da sind
- Fasse mental zusammen: Was sind die 3 kritischsten Lücken im aktuellen Wissen?
- **BEWEIS:** "Ich habe die injizierten Dateien verarbeitet. Meine 3 kritischsten Lücken sind: [1] [2] [3]"
- **Anwendung Session 2026-06-17:** 16 Dateien injiziert via `opencode.jsonc` (AGENTS.md, CLAUDE.md, TASKS.md, 4× DOCS/, 8× Regeln, 3× DACH-Skills-Trigger). 3 kritischsten Lücken: (a) Git-Cred-Status nicht in injizierten Dateien, (b) Spec-Drift-Regel nicht explizit formuliert, (c) Sub-Schritt-GO-Konvention nicht dokumentiert.

### Schritt B: Task-spezifische Dateien lesen
- `DESK/TASKS/active/task.md` — der aktuelle Auftrag
- `DESK/TASKS/active/implementation_plan.md` — der Bauplan
- Alle Tier-1-Dateien aus `P01_LESELISTE.md` physisch laden (NICHT nur prüfen ob sie existieren)
- **BEWEIS:** "Ich habe [X] Dateien gelesen. Inhalt: [Kurze Zusammenfassung pro Datei]"
- **Anwendung Session 2026-06-17:** Implementation Plan (`DESK/TASKS/implementation_plan.md`) gelesen. Task-Envelope (`DESK/TASKS/dach-p0-skills/PROMPT_INITIAL.md`) gelesen. DACH-Spec (`DESK/REPORTS/dach-custom-skills.md`) gelesen. 7 weitere Dateien (Spec-Quelle, Brand-Voice, ICP, Product-Marketing) gelesen. Tier-1-Dateien aus P01 physisch geladen, nicht nur Existenz geprüft.

### Schritt C: Bestätigung
Der Agent MUSS diese Bestätigung im Chat abgeben:

> "Comprehension Gate bestanden. [X] Dateien injiziert kontextualisiert, [Y] Tier-1-Dateien gelesen. Bereit für operative Arbeit."

## WAS PASSIERT WENN DAS GATE FEHLSCHLÄGT?

- Der Agent darf KEINE Edits machen
- Der Agent darf KEINE Bash-Befehle ausführen
- Der Agent darf KEINE Sub-Agenten spawnen
- Der Agent MUSS die fehlenden Dateien laden
- Erst DANACH darf die operative Arbeit beginnen

## WANN WIRD DAS GATE VERWENDET?

- Immer zwischen `P01_LESELISTE.md` (Lesen) und `P02_SESSION_INIT.md` (Arbeit)
- Immer wenn ein neuer Task startet
- Immer nach einer Session-Unterbrechung
- Immer nach einem Modell-Wechsel

## GOLDENE REGEL

**„Inhalt erfassen" heißt NICHT „prüfe ob Datei existiert".** Es heißt: Lies den Inhalt und verstehe was drin steht.
