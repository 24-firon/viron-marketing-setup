<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Workflow-Details für Session-Wechsel
> - Entscheidungsmatrix: Welche Datei wann, welcher Modus, welche Reports
> - Bundle-Übersicht und Modi-Definition
>
> - **Bundle-Verwendung:** Quelle: `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/`. Arbeitskopie: `HANDOVER/TASK_[SESSION]_V[N]/`. Diese Datei wird NICHT in die Arbeitskopie kopiert.
<!-- TEMPLATE-EXPLANATION-END -->

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

**WENN User keine Antwort gibt:** 1× nachfragen, dann mit Default weiter (SCHNELL, FORENSIC, Agent-Vorschlag, keine).

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
| **SCHNELL** | 7 Mindestdateien | Kurze Übergabe |
| **NORMAL** | 10-12 Dateien | Standard-Sessions |
| **AUSFÜHRLICH** | 17+ Dateien | Multi-Phase |

**Agent hat Entscheidungsfreiheit.** Modi sind Empfehlung.

---

## 4. Die 6 Schritte (Detail)

### Schritt 1: Session-Report
Schreibe forensischen Bericht. Speichere unter `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/HANDOVER.md` (Vorlage kopieren) und befülle. Struktur: Was, Was nicht, Evidence, Geändert, Offen, Nächste.

### Schritt 2: HANDOVER.md
Befülle `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/HANDOVER.md`. 7 Sektionen: BLUF, Projektdaten, Erledigt, Entscheidungen, Offen, Probleme, Nächste.

### Schritt 3: Task-Liste
Aktualisiere `task.md` mit erledigten Tasks. Struktur: M1/M2/M3 mit Checkboxen.

### Schritt 4: Walkthrough
Ergänze `walkthrough.md` mit chronologischer Protokollierung. Format: Datum, Kontext, Was, Geändert, Entscheidungen, Verifikation.

### Schritt 5: Session-Ritual
Führe die 5 Säulen aus: Buchhaltung (todowrite), Artefakt-Hygiene, Beweissicherung, Git-Status, Abschluss-Marker.

### Schritt 6: P00-Fragen
Schreibe 3-5 neue Fragen in `P00_BOOTSTRAP.md` für die nächste Session. Teste ANWENDUNG, nicht RECALL.

---

## 5. Cross-References

| Frage | Datei |
|:---|:---|
| Modell-Rotation? | `references/SYSTEM_INSIGHTS.md` |
| Token-Budget-Details? | `references/TOKEN_WINDOW_GUARD.md` |
| Konservierungs-Gesetze? | `references/KONSERVIERUNGS_GESETZE.md` |
| Session-Titel-Schema? | `references/SESSION_TITEL SCHEMA.md` |
| Handover-Vorlage? | `examples/EXAMPLE_HANDOVER.md` |
| Forensic-Vorlage? | `examples/EXAMPLE_FORENSIC_REPORT.md` |
| SubAgent-Protokoll? | `examples/EXAMPLE_SUBAGENT_REPORT.md` |
| HANDOVER Pflichtfelder? | `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/HANDOVER.md` |

---

## 6. Konservierungs-Gesetze (IMMER gültig)

1. **KEINE LÖSCHUNG** — Archivieren in `ARCHIVE/`, nicht löschen
2. **KEINE REDUKTION** — Code bleibt 100%, keine `//...`-Abkürzungen
3. **BEWEISPFLICHT** — Jede Aussage braucht physisches Artefakt (Report, Diff)
4. **INTEGRATION** — Korrekturen an die richtige Stelle, nicht als Append

Details: `references/KONSERVIERUNGS_GESETZE.md`

---

## 7. SubAgent-Spawn (Kurz)

**VOR Spawn:** STOPP für Modell-Wechsel.

**4 Säulen im Briefing:** MISSION, CONTEXT, SCOPE, ATOMARE SCHRITTE.

**Report-Pflicht:** SubAgent MUSS Protokoll schreiben mit 6 Sektionen (Was/Nicht/Evidence/Geändert/Offen/Nächste).

Details: `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/PROMPTS/SUBAGENT_PROMPT.md` und `examples/EXAMPLE_SUBAGENT_REPORT.md`
