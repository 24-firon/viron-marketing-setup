<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - DoD-Referenz (ausgefülltes Beispiel) für forensische Berichte
> - 9 Sektionen: Systemlage, Architektur-Entscheidungen, Dateien, Diagnostik, Hygiene, Risiken, Research, Handover, Kurzfazit
> - Fortgeschritten: VERIFIZIERT/WAHRSCHEINLICH/OFFEN
>
> - **Bundle-Verwendung:** Diese Datei wird NICHT in die Arbeitskopie kopiert — sie ist systemisch.
<!-- TEMPLATE-EXPLANATION-END -->

# EXAMPLE_FORENSIC_REPORT — Definition of Done

> **Zweck:** DoD-Referenz für forensische Berichte. Agent vergleicht seinen Output mit diesem Beispiel.
> **Wann lesen:** VOR dem Schreiben eines Berichts (Token-Budget grün erforderlich).

---

```markdown
---
session_title: HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1
report_type: FORENSIC
date: 2026-06-07
---

# SESSION REPORT — HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1

**Datum:** 2026-06-07
**Projekt/Repo:** Context-Dispatcher-System
**Scope:** Bundle-Struktur, Skill-Architektur
**Session-Modus:** Build

---

## 1. Systemlage

Die bestehende BUNDLE_KOMPAKT-Struktur (17 Dateien flach) wurde als unübersichtlich identifiziert. P99 als separate Datei widersprach der CDS-Philosophie der Token-Ökonomie. Es fehlte eine einheitliche Architektur für Session-Übergänge, die Token-Bloat-Schutz und 3-Ebenen-Loading berücksichtigt.

## 2. Architektur-Entscheidungen

- **SKILL.md + INSTRUCTIONS.md Trennung:** Token-Bloat-Schutz durch 3 Ebenen. YAML-Header triggert, INSTRUCTIONS.md nur bei Match geladen.
  *Warum:* User-Insight "wenn Agent fälschlicherweise lädt, darf keine Riesenladung kommen"
- **Token-Fenster-Frage als ERSTE Aktion (HD-0):** Compaction-Prävention während Handover-Workflow.
  *Warum:* Handover in Compaction = System kompromittiert. 50-100% Aufschlag auf LLM-Schätzungen.
- **3 Modi (SCHNELL/NORMAL/AUSFÜHRLICH) als Empfehlung, nicht Zwang:** Agent hat Entscheidungsfreiheit.
  *Warum:* User-Vorgabe "Aufweichen" + Agent-Übersicht über Projekt
- **notfall/ eingebettetes Minimal-Bundle:** Backup wenn Token-Budget kritisch oder STORAGE leer.
  *Warum:* User-Vorgabe "Notfall-Bundle für Code Black" + Automatisierbarkeit
- **6 lebendige Dateien als Templates:** task.md, walkthrough.md, decision_log.md, hard_learned_facts.md, ideas_future_plans.md.
  *Warum:* User-Vorgabe "Diese müssen auch mitgeliefert werden und gepflegt werden nach jedem Meilenstein"
- **Bundle vs. Modus getrennt:** Q-A = Bundle-Wahl, Modus = Smart-Mix.
  *Warum:* Bisher vermischt → User-Unklarheit

## 3. Dateien, Pfade & Konfigurationen

### Geändert (im Skill)
- `SKILL.md` — HD-2 angepasst, HD-0 hinzugefügt, Inventar aktualisiert
- `INSTRUCTIONS.md` — Bundle/Modus-Trennung, Compaction-Fork-Option, SubAgent-Klarstellung
- `references/TOKEN_WINDOW_GUARD.md` — Realitäts-Aufschlag 50-100%, Re-Asking-Protokoll
- `references/SESSION_TITEL_SCHEMA.md` — Such-Werkzeug-Sektion hinzugefügt
- `examples/EXAMPLE_HANDOVER.md` — Session-Titel korrigiert
- `examples/EXAMPLE_FORENSIC_REPORT.md` — Session-Titel korrigiert

### Neu angelegt (im Skill)
- `templates/lebendige_dateien/` (6 Templates)
- `notfall/` (5 Minimal-Dateien)
- `implementation_plan.md` (im Workdir)
- `task.md` (im Workdir)
- `walkthrough.md` (im Workdir)
- `decision_log.md` (im Workdir)
- `hard_learned_facts.md` (im Workdir)
- `ideas_future_plans.md` (im Workdir)

### Nicht verändert
- `BUNDLE_KOMPAKT/` (18 Dateien) — bleiben als Vorlage
- `STORAGE/TEMPLATES/` (global) — Migration noch offen (V2-Aufgabe)

## 4. Diagnostik, Tests & Beweislage

- **Verifiziert:** Skill-Ordner wurde erstellt mit `mkdir`
- **Verifiziert:** Alle Dateien erstellt mit `write`
- **Verifiziert:** YAML-Header enthält "Read 25 lines" als Trigger-Hinweis
- **Verifiziert:** HD-2 in SKILL.md konsistent mit Token-Guard-Tabelle
- **Verifiziert:** Session-Titel in allen Beispielen einheitlich `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1`
- **Offen:** Token-Budget-Verhalten in echtem Compaction noch nicht getestet
- **Offen:** Such-Werkzeug für Reports noch nicht implementiert

## 5. Repository-Hygiene

- Alte Bundle-Dateien bleiben als Vorlage (kein Verlust)
- Neue Struktur ist sauber getrennt (systemisch vs. templates vs. lebendige Dateien)
- Naming-Konvention snake_case durchgängig
- Templates/Examples-Ordner erfüllen 4-Pfeiler-Formel

## 6. Risiken, Technical Debt

- **Risiko:** Token-Budget-Schätzung basiert auf User-Aussage, nicht Messung
  *Auswirkung:* Agent könnte sich verschätzen
  *Wahrscheinlichkeit:* Mittel-Hoch (Erfahrungswert: 50-100% Aufschlag nötig)
  *Empfohlene Absicherung:* Test-Session mit echtem Token-Drop, Re-Asking-Protokoll
- **Risiko:** STORAGE-Migration noch nicht durchgeführt, Pfade inkonsistent
  *Auswirkung:* Routing-Matrix verweist auf nicht-existente Pfade
  *Wahrscheinlichkeit:* Hoch
  *Empfohlene Absicherung:* Bundle-Migration in V2 (P1)
- **Risiko:** Such-Werkzeug für Reports fehlt
  *Auswirkung:* Lange Dateinamen nötig, unhandlich
  *Wahrscheinlichkeit:* Mittel
  *Empfohlene Absicherung:* SubAgent-Auftrag für HTML-Tool (P2)
- **Risiko:** Smart-Mix-Logik ohne Decision-Trees
  *Auswirkung:* Agent rät bei unklaren Entscheidungen
  *Wahrscheinlichkeit:* Mittel
  *Empfohlene Absicherung:* Erste echte Session dokumentiert ausführen, lernen

## 7. Research, Einordnung & Denkfehler-Korrektur

- **Annahme korrigiert:** P99 als eigene Datei ist NICHT nötig — Logik in SKILL.md reicht
- **Annahme korrigiert:** LLM schätzt Tokens — Realität ist 50-100% höher
- **Annahme korrigiert:** SubAgent-Prompts sind ECHTE Dateien in STORAGE, keine Platzhalter
- **Beste Practice bestätigt:** Token-Bloat-Schutz durch 3-Ebenen-Laden (YAML → SKILL.md → INSTRUCTIONS.md)
- **Beste Practice bestätigt:** Compaction-Fork-Option als Krisen-Werkzeug (nicht Standard-Workflow)
- **Architekturwahrheit:** Systemische Logik in Skill, Templates in STORAGE — die Trennung ist konsequent

## 8. Handover für den nächsten Agenten

### Aktueller belastbarer Zustand
- `session_handover_generator/` ist erstellt und konsistent
- YAML-Trigger funktioniert syntaktisch
- Token-Guard ist dokumentiert mit Realitäts-Aufschlag, aber nicht in echtem Compaction getestet
- 6 lebendige Dateien als Templates vorhanden (Struktur-Schablonen)

### Verbotene Aktionen
- KEINE Edits am bestehenden `BUNDLE_KOMPAKT/` (bleibt Vorlage)
- KEIN Verschieben von STORAGE (bleibt im Root)
- KEIN Hinzufügen von SubAgent-Prompts ohne User-Vorgabe
- KEINE Rate-Antworten bei Token-Frage (User nachfragen ist Pflicht)

### Nächste logische Schritte
1. HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V2 starten — User kopiert P00 aus neuem Handover-Ordner
2. Bundle-Migration durchführen (P1) — TEMPLATES/PROMPTS-Struktur anlegen
3. BUNDLE_VOLLSTAENDIG nach gleichem Muster anpassen (P1)
4. Such-Werkzeug entwickeln (P2) — SubAgent-Auftrag

### Falls sofort weitergearbeitet wird
- Lade: `SKILL.md` (erste 25 Z.) → Token-Check (HD-0) → INSTRUCTIONS.md Abschnitt 3
- Pfad: `HANDOVER/TASK_HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V2/`
- **WICHTIG:** Bundle-Pfade prüfen, ob Migration erfolgt ist

## 9. Kurzfazit

Bundle-Reparatur + Skill-Generierung abgeschlossen — `session_handover_generator` mit 3-Ebenen-Token-Schutz, Token-Fenster-Frage als HD-0, eingebettetem Notfall-Bundle und 6 lebendigen Dateien-Templates ist die neue Architektur; Migration der STORAGE-Pfade steht aus.

---

**[FORENSIC SESSION REPORT ERSTELLT]**
```

---

## DoD-Kriterien (Selbstprüfung)

- [ ] YAML-Header mit `session_title`, `report_type`, `date`
- [ ] 9 Sektionen in exakter Reihenfolge (Systemlage → Kurzfazit)
- [ ] Architektur-Entscheidungen mit Warum
- [ ] Dateien-Tabelle mit "Geändert/Neu/Nicht verändert"
- [ ] Diagnostik mit VERIFIZIERT/WAHRSCHEINLICH/OFFEN
- [ ] Risiken mit Auswirkung + Wahrscheinlichkeit + Absicherung
- [ ] Handover für nächsten Agenten mit verbotenen Aktionen
- [ ] Kurzfazit in 1 Satz
- [ ] KEINE erfundenen Fakten — wenn nicht geprüft, steht "OFFEN" dabei
