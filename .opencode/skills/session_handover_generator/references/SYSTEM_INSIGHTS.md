<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Rollen-Definition: Hauptsession vs. SubAgents, Operator vs. Orchestrator
> - Modell-Rotation (🔴🟡🟢⚡) mit HARD STOP bei Wechsel
> - Lebendige Dateien pflegen (6 Dateien nach jedem Meilenstein)
> - SubAgent-Spawn-Protokoll (4 Säulen, STOPP-Punkte)
> - User-Kommunikations-Protokoll
>
> - **Bundle-Verwendung:** Diese Datei wird NICHT in die Arbeitskopie kopiert — sie ist systemisch.
<!-- TEMPLATE-EXPLANATION-END -->

# SYSTEMVERSTAENDNIS — Wer macht was, Model-Rotation, lebendige Dateien

> **Wann lesen:** Beim SubAgent-Spawn, bei Modell-Wechsel, bei Pflege der lebendigen Dateien.

## 1. Wer macht was?

### Hauptsession (Session-Architect)
- Plant die Übergabe
- Schreibt Berichte
- Füllt Handover aus
- Pflegt lebendige Dateien
- Entscheidet Modus/Report-Typen
- **Hat Veto-Recht** über SubAgent-Outputs

### Operator (Ausführer, schwaches Modell)
- Führt die Schritte ATOMAR aus (jeder Befehl einzeln, kein `&&`)
- Zeigt immer letzte 3-5 Zeilen Output als Beweis
- Schreibt Reports nach `DESK/reports/`
- Erstellt KEINE Pläne, ändert NICHT den Plan
- Macht STOPP wenn der Plan STOPP sagt

### Orchestrator (Planer, starkes Modell)
- Analysiert die Lage (Pre-Flight Radar)
- Erstellt Pläne (Linear, Stopp für Stopp)
- Schreibt Operator-Prompts (klar, konkret, mit Leseliste)
- Führt KEINE Befehle aus, editiert KEINE Dateien direkt
- Löst Probleme wenn der Operator stuck ist

### SubAgents (gespawnt von Hauptsession)
- **General Agent:** Führt komplexe, mehrstufige Aufgaben aus (z.B. Bundle-Restrukturierung)
- **Explorer Agent:** Liest/analysiert große Datenmengen (z.B. 100 Dateien scannen)
- **Read-Only Agent:** Stellt Fakten zusammen, schreibt keine Dateien

**Wichtig:** IMMER STOPP für Modell-Wechsel VOR SubAgent-Spawn.

## 2. Model-Rotation (IMMER einplanen)

**🛑 HARTER STOPP bei JEDEM Modell-Wechsel.** Das System darf niemals die Ausführung fortsetzen, ohne "Go" vom Operator — selbst wenn das geforderte Modell angeblich schon geladen ist.

| Phase | Modell | Zweck |
|:---|:---|:---|
| **P00** (Bootstrap) | 🔴 STARK | Comprehension — Fragen beantworten, Verständnis prüfen |
| **P01** (Leseliste) | ⚡ LIGHT | Nur lesen — viele Dateien iterieren |
| **P02** (Session Init) | 🔴 STARK | Planung, Meilensteine definieren |
| **M1-M5** (Ausführung) | 🟢 STANDARD | Befehle ausführen |
| **STOPPs** (Meilenstein-Berichte) | 🔴 STARK | Report, Evidence bewerten |
| **Session-Abschluss** | ⚡ LIGHT | Cleanup, todowrite, git status |
| **SubAgent-Tasks** | 🟢 STANDARD | Code-Generierung, Task-Scope |
| **Reviews** | 🟡 MITTEL | Code-Review, Skill-Scan |

**Regel:** Niemals alles mit demselben Modell machen. Modell-Rotation ist Pflicht.
**Harte Regel:** Nach JEDEM Modell-Wechsel: STOPP, User-Bestätigung abwarten.

## 3. Lebendige Dateien (HD-7)

**Definition:** Dateien, die WÄHREND der Session aktiv gepflegt werden, nicht nur am Ende.

| Datei | Wann aktualisieren | Format |
|:---|:---|:---|
| `task.md` | nach jedem Task-Abschluss | Checkboxen [ ] / [x] |
| `implementation_plan.md` | nach jedem Meilenstein | Status: ✅ / 🟡 / ❌ |
| `walkthrough.md` | nach jedem Meilenstein | Eintrag mit Datum + Typ |
| `decision_log.md` | bei jeder Architektur-Entscheidung | Kontext / Entscheidung / Konsequenzen |
| `current_tasklist.md` | bei Task-Hinzufügung/Entfernung | Silo-Struktur mit Prioritäten |

**Pflege-Zeitpunkt:** NACH Meilenstein, NICHT erst am Session-Ende.
**Begründung:** Konservierungs-Gesetz 3 (BEWEISPFLICHT) — wer nicht dokumentiert, hat nicht gearbeitet.

## 4. SubAgent-Spawn-Protokoll

### Vor dem Spawn
1. **STOPP** für Modell-Wechsel (Operator-Permission)
2. **SubAgent-Typ wählen** (General / Explorer / Read-Only)
3. **TASK_ENVELOPE** mit 4 Säulen erstellen:
   - **A) MISSION** — Warum gibt es diese Aufgabe?
   - **B) CONTEXT** — Welche Dateien MUSS der SubAgent lesen?
   - **C) SCOPE** — Was darf er anfassen, was ist Tabu?
   - **D) ATOMARE SCHRITTE** — Exakte Tool-Calls

### Nach dem SubAgent-Report
1. **STOPP** — Bericht lesen
2. **Bewertung** (🔴 STARK Modell) — passt das Ergebnis?
3. **Integration** — SubAgent-Output in lebendige Dateien einarbeiten
4. **ERST DANN:** GO für nächsten Schritt

### Was SubAgents NICHT dürfen
- Andere SubAgents spawnen (Sub-Sub-Agent-Verbot)
- Dateien außerhalb des definierten SCOPE anfassen
- Haupt-Entscheidungen treffen (Modus-Wechsel, User-Kommunikation)
- Ohne STOPP-Punkt weitermachen

## 5. User-Kommunikations-Protokoll

**Wann User kontaktieren:**
- Vor Cross-Cutting-Entscheidungen (Modus, Report-Typen, Architektur)
- Nach jedem Meilenstein (Status-Bericht)
- Bei STOPP-Punkten (GO-Anfrage)
- Bei Token-Budget-Warnung (Schwarz-Status)
- Bei SubAgent-Output-Bewertung (auffällige Ergebnisse)

**Wann User NICHT kontaktieren:**
- Bei atomaren SubAgent-Tasks
- Bei reinen Lese-Operationen
- Bei Cache-/Performance-Optimierungen (kein Architektur-Impact)
- Bei Standard-Wartung (z.B. `.tmp`-Cleanup)

## 6. Verbindung zu INSTRUCTIONS.md

- **Modus-Entscheidung** → INSTRUCTIONS.md Abschnitt 3.2 (Fragenkatalog)
- **Token-Fenster-Logik** → INSTRUCTIONS.md Abschnitt 2
- **Session-Titel-Logik** → SESSION_TITEL_SCHEMA.md
- **Konservierungs-Gesetze** → KONSERVIERUNGS_GESETZE.md
