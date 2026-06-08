---
name: session-handover-generator-instructions
description: Detaillierter Workflow für Session-Wechsel. Wird von SKILL.md geladen. Trigger: SKILL.md sagt "Lade INSTRUCTIONS.md".
---

# INSTRUCTIONS — Workflow-Details

> **Lade diese Datei** wenn du die 6 Schritte aus SKILL.md umsetzen willst. Hier steht WIE, nicht WAS.

---

## 1. User-Intention (4 Pflichtfragen)

Bevor du die 6 Schritte startest, kläre mit dem User:

| # | Frage | Wofür |
|:--|:---|:---|
| Q-A | **Was für ein Session-Wechsel?** Schnell / Normal / Ausführlich / Forensisch | Bestimmt Tiefe und Umfang |
| Q-B | **Welche Reports?** Forensik / Decision Log / Hard-Learned Facts / Incident | Bestimmt Outputs |
| Q-C | **Welche Handover-Dateien?** (Agent schlägt vor, User bestätigt) | Bestimmt Lieferumfang |
| Q-D | **SubAgent-Prompts im Bundle?** alle / nur TASK_ENVELOPE / keine | Bestimmt Tiefe der SubAgent-Nutzung |

**WENN User keine Antwort gibt:** 1× nachfragen, dann Default: SCHNELL, FORENSIC, Agent-Vorschlag, keine.

---

## 2. Bundle-Auswahl

Du arbeitest in einer von 4 Template-Staffeln:

| Bundle | Pfad | Größe | Für wen |
|:---|:---|:---:|:---|
| **SLIM** | `STORAGE/TEMPLATES/BUNDLE_SLIM/` | 7-22 Z. | Token-arme Modelle |
| **KOMPAKT** ← | `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` | 30-80 Z. | Standard-Sessions |
| KONSOLIDIERT | `STORAGE/TEMPLATES/BUNDLE_KONSOLIDIERT/` | 50-100 Z. | Multi-Phase |
| VOLLSTÄNDIG | `STORAGE/TEMPLATES/BUNDLE_VOLLSTAENDIG/` | 100-300 Z. | Enterprise |

**Default:** KOMPAKT (nimm es wenn unsicher).

---

## 3. Modi (Nutzungsprofile)

| Modus | Dateien | Wann |
|:---|:---|:---|
| **SCHNELL** | 7 Mindestdateien | kurze Tasks, schnelle Übergabe |
| **NORMAL** | 10-12: SCHNELL + CURRENT_TASKLIST + SESSION_RITUAL + WORKSPACE_WALKTHROUGH | Standard-Sessions |
| **AUSFÜHRLICH** | alle 17 + TASK_ENVELOPE + OPERATOR + ORCHESTRATOR + TIER_MEMORY | komplexe Multi-Phase |

**Agent hat Entscheidungsfreiheit:** Modi sind Empfehlung, nicht Zwang.

---

## 4. Die 6 Schritte (Detail)

### Schritt 1: Session-Report
Schreibe forensischen Report. Nutze `templates/lebendige_dateien/implementation_plan.md` als Struktur (M1-M4). Speichere unter `DESK/reports/[SESSION]_V[N].md`.

Struktur: Was wurde gemacht, Was wurde NICHT gemacht, Beweise (letzte 3-5 Zeilen Output), Geänderte Dateien, Offene Punkte, Nächste Schritte.

### Schritt 2: HANDOVER.md
Kopiere `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/HANDOVER.md` nach `HANDOVER/TASK_[SESSION]_V[N]/HANDOVER.md` und befülle alle 7 Sektionen:
1. BLUF (Bottom Line Up Front)
2. PROJEKT-SPEZIFISCHE DATEN
3. ABGESCHLOSSENE ARBEIT
4. ENTSCHEIDUNGEN
5. OFFENE TASKS
6. BEKANNTE PROBLEME & WORKAROUNDS
7. NÄCHSTE SCHRITTE

### Schritt 3: Task-Liste
Aktualisiere `templates/lebendige_dateien/task.md` mit erledigten Tasks. Struktur: M1/M2/M3 mit Checkboxen.

### Schritt 4: Walkthrough
Ergänze `templates/lebendige_dateien/walkthrough.md` mit chronologischer Protokollierung. Format: Datum, Kontext, Was, Geändert, Entscheidungen, Verifikation.

### Schritt 5: Session-Ritual
Führe 5 Säulen aus:
1. Buchhaltung (todowrite) — alle Tasks auf completed/cancelled
2. Artefakt-Hygiene — temporäre Dateien löschen
3. Beweissicherung — Report existiert physisch
4. Git-Status — clean oder staged
5. Abschluss-Marker — Bestätigung an Operator

### Schritt 6: P00-Fragen
Schreibe 3-5 neue Fragen für `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/P00_BOOTSTRAP.md`. Teste ANWENDUNG, nicht RECALL.

---

## 5. Cross-References

| Frage | Datei |
|:---|:---|
| Modell-Rotation? | `references/SYSTEM_INSIGHTS.md` |
| Token-Budget-Details? | `references/TOKEN_WINDOW_GUARD.md` |
| Konservierungs-Gesetze? | `references/KONSERVIERUNGS_GESETZE.md` |
| Session-Titel-Schema? | `references/SESSION_TITEL_SCHEMA.md` |
| Handover-Vorlage? | `examples/EXAMPLE_HANDOVER.md` |
| Forensic-Vorlage? | `examples/EXAMPLE_FORENSIC_REPORT.md` |
| SubAgent-Protokoll? | `examples/EXAMPLE_SUBAGENT_REPORT.md` |
| HANDOVER Pflichtfelder? | `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/HANDOVER.md` |

---

## 6. Konservierungs-Gesetze (IMMER)

1. **KEINE LÖSCHUNG** — Archivieren in `ARCHIVE/`, nicht löschen
2. **KEINE REDUKTION** — Code 100%, keine `//...`-Abkürzungen
3. **BEWEISPFLICHT** — Physische Artefakte (Reports, Diffs)
4. **INTEGRATION** — Korrekturen an der Stelle, nicht ans Ende

Details: `references/KONSERVIERUNGS_GESETZE.md`

---

## 7. SubAgent-Spawn (Kurz)

**VOR Spawn:** STOPP für Modell-Wechsel.

**4 Säulen im Briefing:** MISSION, CONTEXT, SCOPE, ATOMARE SCHRITTE.

**Report-Pflicht:** SubAgent MUSS Protokoll schreiben mit 6 Sektionen (Was/Nicht/Evidence/Geändert/Offen/Nächste).

Details: `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/PROMPTS/SUBAGENT_PROMPT.md` und `examples/EXAMPLE_SUBAGENT_REPORT.md`
