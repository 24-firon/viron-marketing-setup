# KOMPAKT TEMPLATES — Die 4. Staffel

<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Bundle-Übersicht mit 4-Staffel-System, Datei-Inventar und Modus-Erklärung
> - Erklärung der 3 Modi (Schnell/Normal/Ausführlich) und wann welcher Modus greift
>
> - **Bundle-Verwendung:** Template-Quelle: `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/`. Arbeitskopie: `DESK/HANDOVER.md`. P99 wird NICHT nach DESK kopiert — es ist ein PROMPT, kein Template. Nicht alle Bundle-Dateien müssen genutzt werden.
<!-- TEMPLATE-EXPLANATION-END -->

> **17 Dateien. 30-80 Zeilen pro Datei. Selbst-erklärende Platzhalter. Leicht zu benutzen.**

## 4-STAFFEL-SYSTEM

Du arbeitest in einer von 4 Template-Staffeln. Wähle die richtige:

| Staffel | Wo | Zeilen/Dat. | Für wen |
|:---|:---|:---:|:---|
| **SLIM** | `STORAGE/TEMPLATES/BUNDLE_SLIM/` | 7-22 | Token-arme Modelle, Quick-Reference, minimale Bedienung |
| **KOMPAKT** ← **DU BIST HIER** | `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` | 30-80 | Standard-Sessions, mittel-komplex, **leicht zu benutzen** |
| **KONSOLIDIERT** | `STORAGE/TEMPLATES/BUNDLE_KONSOLIDIERT/` | 50-100 | Multi-Phase Projekte, mehrere Varianten pro Kategorie |
| **VOLLSTÄNDIG** | `STORAGE/TEMPLATES/BUNDLE_VOLLSTAENDIG/` | 100-300 | Komplexe Enterprise-Projekte, vollständige Dokumentation |

**Goldene Regel:** Nimm die KOMPAKT-Staffel wenn du nicht sicher bist. Sie ist die goldene Mitte zwischen Schnelligkeit und Vollständigkeit.

## WAS IST ANDERS ALS SLIM?

| Aspekt | SLIM | KOMPAKT |
|:---|:---|:---|
| Platzhalter | leer `[Schritt 1]` | **selbst-erklärend** `[konkrete Aktion mit Befehl oder Tool-Call]` |
| Erklärungen | keine | **Mini-Erklärungen pro Sektion** |
| Beispiele | keine | **Beispiele wo sinnvoll** |
| Zeilen pro Datei | 7-22 | 30-80 |
| Benutzbar ohne Doku? | NEIN — man muss raten | **JA** — Platzhalter erklären sich selbst |

## WAS IST ANDERS ALS KONSOLIDIERT?

KOMPAKT hat **eine** saubere Variante pro Template. KONSOLIDIERT hat **zwei Varianten** (Master + Alternative). Wenn du unsicher bist welche die richtige ist, nimm KOMPAKT.

## DATEI-INVENTAR (17 Dateien)

| # | Datei | Zweck |
|:--|:---|:---|
| 1 | `P00_BOOTSTRAP.md` | Bootstrap mit 7 Fragen + 3 Schichten (ANWENDUNG-getestet) |
| 2 | `P01_LESELISTE.md` | Leseliste mit 3 Batches + Notiz-Templates |
| 3 | `P02_SESSION_INIT.md` | Session Init mit Comprehension Gate + Meilensteine + Modell-Rotation |
| 4 | `P99_HANDOFF.md` | Session-Abschluss mit 6 Schritten + P00-Fragen-Generierung |
| 5 | `HANDOVER.md` | Datenübergabe mit BLUF + projektspezifische Daten + 7 Sektionen |
| 6 | `IMPLEMENTATION_PLAN.md` | Linearer Plan mit M1-M3 + Abbruch-Bedingungen + Verifikation |
| 7 | `CURRENT_TASKLIST.md` | Silo-Struktur mit [ ] Status + Prioritäten + Blockiert-Tracking |
| 8 | `WORKSPACE_WALKTHROUGH.md` | Topology + Reading List + Tabu-Liste |
| 9 | `SESSION_HANDOVER.md` | Forensischer Bericht (9 Sektionen, kalt + präzise) |
| 10 | `SESSION_RITUAL.md` | 5-Säulen-Abschluss-Check mit Verifikation pro Säule |
| 11 | `TASK_ENVELOPE.md` | 4-Säulen SubAgent-Briefing mit Vorlage + Beispiel |
| 12 | `OPERATOR_WORKFLOW.md` | Ausführer-Rolle mit atomarer Ausführung + Evidence-Beispiel |
| 13 | `ORCHESTRATOR_WORKFLOW.md` | Planer-Rolle mit Pre-Flight Radar + Operator-Prompt-Beispiel |
| 14 | `TIER_MEMORY.md` | 4-Tier-Shrink mit Archive-First-Regel + Vorher/Nachher |
| 15 | `COMPREHENSION_GATE.md` | 3-Schritte-Hard-Stop mit Wann-Anwendung |
| 16 | `KONSERVIERUNGS_MANIFEST.md` | 4 Gesetze mit Beispielen + CDS-Konkretisierung |
| 17 | `README.md` | Diese Datei (Staffel-Erklärung) |

## REIHENFOLGE BEIM LESEN (für den Agent)

1. **Dieses README** — du bist hier
2. `P00_BOOTSTRAP.md` — Stress-Test bestehen
3. `P01_LESELISTE.md` — Was lesen, Notizen machen
4. `P02_SESSION_INIT.md` — Comprehension Gate, Meilensteine
5. `[arbeite]`
6. `P99_HANDOFF.md` — Session-Abschluss
7. `HANDOVER.md` — Daten für nächsten Agent

## WANN NUTZEN?

✅ **KOMPAKT nutzen wenn:**
- Standard-Session (1-3 Meilensteine)
- Mittel-komplexe Aufgaben
- Du willst benutzbare Templates ohne Overhead
- Der nächste Agent ist nicht erfahren (klare Anleitung nötig)

❌ **KOMPAKT NICHT nutzen wenn:**
- Multi-Phase Enterprise-Projekt (nimm KONSOLIDIERT)
- Du brauchst 2 Varianten zum Vergleichen (nimm KONSOLIDIERT)
- Token-budget ist extrem knapp (nimm SLIM)

## AUSLIEFERUNG (DEPLOYMENT)

| Was | Quelle | Ziel |
|:---|:---|:---|
| Bundle | `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` | `DESK/` |
| P99_PROMPT | NICHT kopieren — wird im Chat als Nachricht ausgelöst | — |
| Handover | `HANDOVER.md` aus Bundle | `DESK/HANDOVER.md` |
| Task-Envelope | `TASK_ENVELOPE.md` aus Bundle | `DESK/TASKS/[ID]/PROMPT_INITIAL.md` |
| Reports | — | `DESK/reports/Session-reports/` |

**Regeln:**
1. P99 wird NICHT nach DESK kopiert — es wird als Nachricht im Chat ausgelöst
2. Verwende nur die Dateien, die du brauchst — nicht das gesamte Bundle muss genutzt werden
3. Arbeitskopien gehören auf DESK/, nicht in DIRECTOR/

## 4 GESETZE (aus KONSERVIERUNGS_MANIFEST)

1. KEINE LÖSCHUNG — Archivieren
2. KEINE REDUKTION — 100% Erhalt
3. BEWEISPFLICHT — Physische Artefakte
4. INTEGRATION — Korrekturen an die richtige Stelle
