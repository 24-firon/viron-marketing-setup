# implementation_plan.md — Bundle-Reparatur + Skill-Generierung (VOLLSTÄNDIG)

```
TASK-ID: HANDOVER_BUNDLE_REPAIR_001
PHASE: V1 (Vollständige Funktionalität)
RISIKO: 🟡 Medium (viele Datei-Änderungen, Token-kritisch)
GESCHÄTZTE DAUER: ~2 Stunden
SUBAGENTS-EINGESETZT: 0 (direkte Umsetzung)
MODELL-WECHSEL-PUNKTE: 3 (nach Phase 4, nach Phase 8, nach Phase 10)
```

---

## KRITISCHE LÜCKEN-ANALYSE (warum dieser Plan jetzt entsteht)

**Was schiefgelaufen war:**
1. SKILL.md und INSTRUCTIONS.md wurden von NULL geschrieben, ohne die alten P99_HANDOFF.md (94Z) und README.md (106Z) zu integrieren
2. Die 7 Fragen aus P00_BOOTSTRAP.md wurden NICHT in den Skill übernommen
3. Die 3 Batches aus P01_LESELISTE.md wurden NICHT übernommen
4. Die Comprehension Gate Schritte A/B/C aus P02_SESSION_INIT.md wurden nur erwähnt, nicht integriert
5. Die 7 Sektionen aus HANDOVER.md wurden durch ein anderes Format ersetzt
6. Die Info-Blöcke `<!-- TEMPLATE-EXPLANATION -->` wurden nicht übernommen
7. 18 Templates liegen flach in BUNDLE_KOMPAKT/, keine wurde nach STORAGE/ kopiert
8. Der Skill verweist auf nicht-existente Pfade (KOPIERPAKET/, REPORT_GEN/)

**Lehre:** "Ohne Plan vergisst man Dateien" — User-Kritik zu Recht. Jetzt: vollständiger Plan.

---

## PHASE 0: VORBEREITUNG (5 Min) — 🔴 STARK

**Ziel:** Alle Quelldateien lesen, Inhalte dokumentieren, Übernahme-Plan erstellen.

### Schritte
- [ ] **P0.1** `[READ]` — LIES `BUNDLE_KOMPAKT/P99_HANDOFF.md` (94Z) — extrahiere 6 Schritte-Formulierungen
- [ ] **P0.2** `[READ]` — LIES `BUNDLE_KOMPAKT/README.md` (106Z) — extrahiere 4-Staffel-Tabelle + WAS IST ANDERS-Sektionen
- [ ] **P0.3** `[READ]` — LIES `BUNDLE_KOMPAKT/P00_BOOTSTRAP.md` (50Z) — extrahiere 7 Fragen + 3 Schichten
- [ ] **P0.4** `[READ]` — LIES `BUNDLE_KOMPAKT/P01_LESELISTE.md` (52Z) — extrahiere 3 Batches + Skip-Liste
- [ ] **P0.5** `[READ]` — LIES `BUNDLE_KOMPAKT/P02_SESSION_INIT.md` (82Z) — extrahiere Comprehension Gate + Meilensteine
- [ ] **P0.6** `[READ]` — LIES `BUNDLE_KOMPAKT/HANDOVER.md` (59Z) — extrahiere 7 Sektionen
- [ ] **P0.7** `[READ]` — LIES `BUNDLE_KOMPAKT/COMPREHENSION_GATE.md` (40Z) — extrahiere Wann-Sektion
- [ ] **P0.8** `[READ]` — LIES `BUNDLE_KOMPAKT/KONSERVIERUNGS_MANIFEST.md` (49Z) — extrahiere 4 Gesetze
- [ ] **P0.9** `[READ]` — LIES `BUNDLE_KOMPAKT/SESSION_HANDOVER.md` (82Z) — extrahiere 9 Sektionen
- [ ] **P0.10** `[READ]` — LIES `BUNDLE_KOMPAKT/SESSION_RITUAL.md` (60Z) — extrahiere 5 Säulen
- [ ] **P0.11** `[READ]` — LIES `BUNDLE_KOMPAKT/IMPLEMENTATION_PLAN.md` (75Z) — extrahiere M1-M3-Struktur
- [ ] **P0.12** `[READ]` — LIES `BUNDLE_KOMPAKT/CURRENT_TASKLIST.md` (52Z) — extrahiere Silo-Struktur
- [ ] **P0.13** `[READ]` — LIES `BUNDLE_KOMPAKT/WORKSPACE_WALKTHROUGH.md` (45Z) — extrahiere 4 Sektionen
- [ ] **P0.14** `[READ]` — LIES `BUNDLE_KOMPAKT/TASK_ENVELOPE.md` (99Z) — extrahiere 4-Säulen + Vorlage
- [ ] **P0.15** `[READ]` — LIES `BUNDLE_KOMPAKT/OPERATOR_WORKFLOW.md` (90Z) — extrahiere 7-Schritte-Workflow
- [ ] **P0.16** `[READ]` — LIES `BUNDLE_KOMPAKT/ORCHESTRATOR_WORKFLOW.md` (78Z) — extrahiere 9-Schritte-Workflow
- [ ] **P0.17** `[READ]` — LIES `BUNDLE_KOMPAKT/TIER_MEMORY.md` (58Z) — extrahiere 4-Tier-Shrink
- [ ] **P0.18** `[READ]` — LIES `BUNDLE_KOMPAKT/REPORT_GENERATOR.md` (364Z) — extrahiere 9 Sektionen
- [ ] **P0.19** `[WRITE]` — Erstelle Übernahme-Mapping (welcher Inhalt geht wohin)

### DoD Phase 0
- Alle 18 Quelldateien gelesen
- Übernahme-Mapping dokumentiert in `walkthrough.md` (Phase 0 Abschnitt)
- Welche Formulierung → welche Skill-Datei

### STOPP 0 — Berichte Ergebnis, zeige Übernahme-Mapping, warte auf GO

---

## PHASE 1: STORAGE-MIGRATION (10 Min) — 🟢 STANDARD

**Ziel:** 18 Templates von BUNDLE_KOMPAKT/ nach STORAGE/TEMPLATES/BUNDLE_KOMPAKT/ kopieren.

### Schritte
- [ ] **P1.1** `[WRITE]` — Erstelle `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` Ordner
- [ ] **P1.2** `[WRITE]` — Erstelle `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/KOPIERPAKET/` Unterordner
- [ ] **P1.3** `[WRITE]` — Erstelle `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/REPORT_GEN/` Unterordner
- [ ] **P1.4** `[WRITE]` — Erstelle `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/reports/` Unterordner
- [ ] **P1.5** `[WRITE]` — Erstelle `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/KOPIERPAKET/additional/` Unterordner
- [ ] **P1.6** `[COPY]` — Kopiere P00_BOOTSTRAP.md → STORAGE/KOPIERPAKET/
- [ ] **P1.7** `[COPY]` — Kopiere P01_LESELISTE.md → STORAGE/KOPIERPAKET/
- [ ] **P1.8** `[COPY]` — Kopiere P02_SESSION_INIT.md → STORAGE/KOPIERPAKET/
- [ ] **P1.9** `[COPY]` — Kopiere IMPLEMENTATION_PLAN.md → STORAGE/KOPIERPAKET/
- [ ] **P1.10** `[COPY]` — Kopiere CURRENT_TASKLIST.md → STORAGE/KOPIERPAKET/
- [ ] **P1.11** `[COPY]` — Kopiere HANDOVER.md → STORAGE/KOPIERPAKET/
- [ ] **P1.12** `[COPY]` — Kopiere SESSION_HANDOVER.md → STORAGE/KOPIERPAKET/
- [ ] **P1.13** `[COPY]` — Kopiere SESSION_RITUAL.md → STORAGE/KOPIERPAKET/
- [ ] **P1.14** `[COPY]` — Kopiere TASK_ENVELOPE.md → STORAGE/KOPIERPAKET/
- [ ] **P1.15** `[COPY]` — Kopiere OPERATOR_WORKFLOW.md → STORAGE/KOPIERPAKET/
- [ ] **P1.16** `[COPY]` — Kopiere ORCHESTRATOR_WORKFLOW.md → STORAGE/KOPIERPAKET/
- [ ] **P1.17** `[COPY]` — Kopiere TIER_MEMORY.md → STORAGE/KOPIERPAKET/
- [ ] **P1.18** `[COPY]` — Kopiere WORKSPACE_WALKTHROUGH.md → STORAGE/KOPIERPAKET/
- [ ] **P1.19** `[COPY]` — Kopiere README.md → STORAGE/KOPIERPAKET/
- [ ] **P1.20** `[COPY]` — Kopiere COMPREHENSION_GATE.md → STORAGE/KOPIERPAKET/additional/
- [ ] **P1.21** `[COPY]` — Kopiere KONSERVIERUNGS_MANIFEST.md → STORAGE/KOPIERPAKET/additional/
- [ ] **P1.22** `[COPY]` — Kopiere REPORT_GENERATOR.md → STORAGE/REPORT_GEN/FORENSIC_REPORT_GENERATOR.md
- [ ] **P1.23** `[VERIFY]` — `ls STORAGE/TEMPLATES/BUNDLE_KOMPAKT/KOPIERPAKET/` zeigt 17 Dateien
- [ ] **P1.24** `[VERIFY]` — `ls STORAGE/TEMPLATES/BUNDLE_KOMPAKT/REPORT_GEN/` zeigt 1 Datei
- [ ] **P1.25** `[VERIFY]` — `ls STORAGE/TEMPLATES/BUNDLE_KOMPAKT/reports/` zeigt 0 Dateien (leer, OK)

### SubAgent-Orchestration Phase 1
- Keine SubAgents. Direkte Copy-Operationen.

### Model-Wahl Phase 1
- 🟢 STANDARD (Copy-Operationen sind mechanisch)

### DoD Phase 1
- 17 Dateien in KOPIERPAKET/
- 2 Dateien in additional/
- 1 Datei in REPORT_GEN/ (umbenannt)
- Alle Quelldateien aus BUNDLE_KOMPAKT/ noch vorhanden (Vorlage bleibt)

### STOPP 1 — Berichte Migrations-Status, warte auf GO

---

## PHASE 2: P99-FORMULIERUNGEN IN SKILL.md (20 Min) — 🔴 STARK

**Ziel:** Die 6 Schritte aus P99_HANDOFF.md (94Z) mit konkreten Formulierungen in SKILL.md integrieren.

### Schritte
- [ ] **P2.1** `[READ]` — LIES BUNDLE_KOMPAKT/P99_HANDOFF.md (94Z, schon in Phase 0 gelesen)
- [ ] **P2.2** `[READ]` — LIES aktuelle session_handover_generator/SKILL.md
- [ ] **P2.3** `[WRITE]` — Übernimm P99-Schritt 0-Formulierung in SKILL.md: "Lies `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/KOPIERPAKET/README.md`"
- [ ] **P2.4** `[WRITE]` — Übernimm P99-Schritt 1 "REPORT SCHREIBEN" mit Pfad `DESK/reports/[SESSION-NAME]_[YYYY-MM-DD].md` und 9 Sektionen
- [ ] **P2.5** `[WRITE]` — Übernimm P99-Schritt 2 "HANDOVER BEFÜLLEN" mit Pflicht-Feldern (BLUF, Daten, Erledigt, Entscheidungen, Offen, Probleme, Nächste)
- [ ] **P2.6** `[WRITE]` — Übernimm P99-Schritt 3 "CURRENT_TASKLIST AKTUALISIEREN"
- [ ] **P2.7** `[WRITE]` — Übernimm P99-Schritt 4 "WALKTHROUGH ERGÄNZEN" mit Format-Vorlage
- [ ] **P2.8** `[WRITE]` — Übernimm P99-Schritt 5 "SESSION-RITUAL ABARBEITEN" mit 5 Säulen
- [ ] **P2.9** `[WRITE]` — Übernimm P99-Schritt 6 "P00-FRAGEN FÜR NÄCHSTEN AGENTEN" mit Beispielen
- [ ] **P2.10** `[WRITE]` — Übernimm P99-Bestätigungs-Formel: "P99 abgeschlossen. Report unter [Pfad]. HANDOVER.md abgelegt. Tasks clean. Workspace clean. P00-Fragen geschrieben."
- [ ] **P2.11** `[WRITE]` — Übernimm P99 "STOPP" am Ende

### SubAgent-Orchestration Phase 2
- Keine SubAgents. Direktes Edit.

### Model-Wahl Phase 2
- 🔴 STARK (Reasoning für sinnvolle Integration)

### DoD Phase 2
- SKILL.md enthält alle 6 P99-Schritte mit konkreten Formulierungen
- P99-Bestätigungs-Formel übernommen
- P99-STOPP übernommen

### STOPP 2 — Berichte Integration, warte auf GO

---

## PHASE 3: README-STRUKTUR IN INSTRUCTIONS.md (15 Min) — 🔴 STARK

**Ziel:** 4-Staffel-Tabelle + WAS IST ANDERS-Sektionen aus BUNDLE_KOMPAKT/README.md (106Z) in INSTRUCTIONS.md übernehmen.

### Schritte
- [ ] **P3.1** `[READ]` — LIES BUNDLE_KOMPAKT/README.md (106Z, schon in Phase 0)
- [ ] **P3.2** `[WRITE]` — Übernimm 4-Staffel-Tabelle in INSTRUCTIONS.md (SLIM / KOMPAKT / KONSOLIDIERT / VOLLSTÄNDIG)
- [ ] **P3.3** `[WRITE]` — Übernimm "WAS IST ANDERS ALS SLIM?" Tabelle
- [ ] **P3.4** `[WRITE]` — Übernimm "WAS IST ANDERS ALS KONSOLDIERT?" Sektion
- [ ] **P3.5** `[WRITE]` — Übernimm DATEI-INVENTAR (17 Dateien) in INSTRUCTIONS.md
- [ ] **P3.6** `[WRITE]` — Übernimm REIHENFOLGE BEIM LESEN (7 Schritte)
- [ ] **P3.7** `[WRITE]` — Übernimm WANN NUTZEN / WANN NICHT NUTZEN Sektionen
- [ ] **P3.8** `[WRITE]` — Übernimm AUSLIEFERUNG (DEPLOYMENT) Tabelle mit korrigierten Pfaden

### SubAgent-Orchestration Phase 3
- Keine SubAgents.

### Model-Wahl Phase 3
- 🔴 STARK (Reasoning)

### DoD Phase 3
- INSTRUCTIONS.md enthält 4-Staffel-Tabelle
- INSTRUCTIONS.md enthält 17-Datei-Inventar
- INSTRUCTIONS.md enthält DEPLOYMENT-Tabelle

### STOPP 3 — Berichte Integration, warte auf GO

---

## PHASE 4: INFO-BLÖCKE IN SKILL-DATEIEN (10 Min) — 🟢 STANDARD

**Ziel:** `<!-- TEMPLATE-EXPLANATION-START -->` Blöcke in alle Skill-Dateien einfügen.

### Schritte
- [ ] **P4.1** `[WRITE]` — Füge Info-Block in SKILL.md ein (oberhalb Inhaltsverzeichnis)
- [ ] **P4.2** `[WRITE]` — Füge Info-Block in INSTRUCTIONS.md ein
- [ ] **P4.3** `[WRITE]` — Füge Info-Block in references/TOKEN_WINDOW_GUARD.md ein
- [ ] **P4.4** `[WRITE]` — Füge Info-Block in references/SESSION_TITEL_SCHEMA.md ein
- [ ] **P4.5** `[WRITE]` — Füge Info-Block in references/KONSERVIERUNGS_GESETZE.md ein
- [ ] **P4.6** `[WRITE]` — Füge Info-Block in references/SYSTEMVERSTAENDNIS.md ein
- [ ] **P4.7** `[WRITE]` — Füge Info-Block in examples/EXAMPLE_HANDOVER.md ein
- [ ] **P4.8** `[WRITE]` — Füge Info-Block in examples/EXAMPLE_FORENSIC_REPORT.md ein
- [ ] **P4.9** `[WRITE]` — Füge Info-Block in examples/EXAMPLE_SESSION_TITLE.md ein

### Format Info-Block
```markdown
<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - [Kurzbeschreibung Inhalt]
> - [Wann nutzen]
> - [Wo abgelegt im Storage]
>
> - **Bundle-Verwendung:** Template-Quelle: `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/[PFAD]`. Arbeitskopie: `HANDOVER/TASK_[SESSION]_V[N]/`. Diese Datei wird NICHT in die Arbeitskopie kopiert — sie ist systemisch.
<!-- TEMPLATE-EXPLANATION-END -->
```

### SubAgent-Orchestration Phase 4
- Keine SubAgents.

### Model-Wahl Phase 4
- 🟢 STANDARD (mechanisches Einfügen)

### DoD Phase 4
- 9 Info-Blöcke eingefügt
- Konsistentes Format

### 🛑 **STOPP FÜR MODELL-WECHSEL** — Bestätigung Operator. Nächstes Modell: 🔴 STARK für Phase 5-7.

---

## PHASE 5: HANDOVER.md SEKTIONEN IN EXAMPLE_HANDOVER.md (15 Min) — 🔴 STARK

**Ziel:** Die 7 Sektionen aus BUNDLE_KOMPAKT/HANDOVER.md (59Z) in examples/EXAMPLE_HANDOVER.md übernehmen.

### Schritte
- [ ] **P5.1** `[READ]` — LIES BUNDLE_KOMPAKT/HANDOVER.md (59Z, schon in Phase 0)
- [ ] **P5.2** `[WRITE]` — Übernimm 1. BLUF (Bottom Line Up Front) Format
- [ ] **P5.3** `[WRITE]` — Übernimm 2. PROJEKT-SPEZIFISCHE DATEN Tabelle
- [ ] **P5.4** `[WRITE]` — Übernimm 3. ERLEDIGTE ARBEIT Tabelle
- [ ] **P5.5** `[WRITE]` — Übernimm 4. ENTSCHEIDUNGEN Tabelle (mit Reversibilität)
- [ ] **P5.6** `[WRITE]` — Übernimm 5. OFFENE TASKS Tabelle
- [ ] **P5.7** `[WRITE]` — Übernimm 6. BEKANNTE PROBLEME & WORKAROUNDS Tabelle
- [ ] **P5.8** `[WRITE]` — Übernimm 7. NÄCHSTE SCHRITTE (Konkret) Liste
- [ ] **P5.9** `[WRITE]` — Übernimm "WICHTIG: KEINE FRAGEN IN HANDOVER" Hinweis
- [ ] **P5.10** `[WRITE]` — Übernimm Bestätigungs-Formel "Handover abgeschlossen. Warte auf nächsten Operator-Auftrag."

### SubAgent-Orchestration Phase 5
- Keine SubAgents.

### Model-Wahl Phase 5
- 🔴 STARK

### DoD Phase 5
- EXAMPLE_HANDOVER.md enthält alle 7 Sektionen im korrekten Format
- Konsistenz mit BUNDLE_KOMPAKT/HANDOVER.md gewahrt

### STOPP 5 — Berichte Integration, warte auf GO

---

## PHASE 6: P00/P01/P02 KONKRETE PLATZHALTER (20 Min) — 🔴 STARK

**Ziel:** 7 Fragen aus P00, 3 Batches aus P01, Comprehension Gate aus P02 in Skill-Templates übernehmen.

### Schritte für P00
- [ ] **P6.1** `[READ]` — LIES BUNDLE_KOMPAKT/P00_BOOTSTRAP.md (50Z)
- [ ] **P6.2** `[WRITE]` — Erstelle `STORAGE/KOPIERPAKET/P00_TEMPLATE.md` (Kopie + minimale Vereinfachung)
  - "Fragen ZUERST, nicht weiter hinten"
  - "Prüfe opencode.jsonc geladen"
  - "Comprehension Gate RAUS (geht nach P02)"
  - Behalte 7 konkrete Fragen als Pflicht
  - Behalte 3 Kontext-Schichten
  - Behalte Bestätigungs-Formel

### Schritte für P01
- [ ] **P6.3** `[READ]` — LIES BUNDLE_KOMPAKT/P01_LESELISTE.md (52Z)
- [ ] **P6.4** `[WRITE]` — Erstelle `STORAGE/KOPIERPAKET/P01_TEMPLATE.md` (Kopie + Verschlankung)
  - 3 Batches bleiben (Heart/Foundation/Material)
  - Comprehension Gate RAUS
  - Skip-Liste bleibt
  - Bestätigungs-Formel bleibt

### Schritte für P02
- [ ] **P6.5** `[READ]` — LIES BUNDLE_KOMPAKT/P02_SESSION_INIT.md (82Z)
- [ ] **P6.6** `[READ]` — LIES BUNDLE_KOMPAKT/COMPREHENSION_GATE.md (40Z)
- [ ] **P6.7** `[WRITE]` — Erstelle `STORAGE/KOPIERPAKET/P02_TEMPLATE.md` (Kopie + Erweiterung)
  - Comprehension Gate 2 (3 Schritte A/B/C) aus P02
  - "Wann anwenden?" aus COMPREHENSION_GATE.md
  - System-Erklärung NEU hinzugefügt: Wer-macht-was, Model-Rotation, lebendige Dateien
  - Meilensteine M1-M3 bleiben
  - Mindset-Block bleibt
  - 4 Gesetze Verweis auf KONSERVIERUNGS_MANIFEST

### SubAgent-Orchestration Phase 6
- Keine SubAgents. Direktes Edit + Create.

### Model-Wahl Phase 6
- 🔴 STARK

### DoD Phase 6
- 3 neue Dateien in STORAGE/KOPIERPAKET/ (oder Edits an existierenden Kopien)
- P00: Fragen zuerst, kein Gate
- P01: Nur Leseliste, kein Gate
- P02: Gate + System-Erklärung
- Konsistenz mit alten Formulierungen gewahrt

### STOPP 6 — Berichte Integration, warte auf GO

---

## PHASE 7: CROSS-REFERENCES FIXEN (15 Min) — 🔴 STARK

**Ziel:** Alle Pfad-Verweise in Skill zeigen auf existierende Dateien.

### Schritte
- [ ] **P7.1** `[WRITE]` — Fixe SKILL.md Routing-Matrix (alle Pfade auf STORAGE verweisen)
- [ ] **P7.2** `[WRITE]` — Fixe INSTRUCTIONS.md alle Pfade
- [ ] **P7.3** `[WRITE]` — Fixe references/TOKEN_WINDOW_GUARD.md Cross-References
- [ ] **P7.4** `[WRITE]` — Fixe references/SESSION_TITEL_SCHEMA.md Cross-References
- [ ] **P7.5** `[WRITE]` — Fixe references/KONSERVIERUNGS_GESETZE.md Cross-References
- [ ] **P7.6** `[WRITE]` — Fixe references/SYSTEMVERSTAENDNIS.md Cross-References
- [ ] **P7.7** `[WRITE]` — Fixe examples/EXAMPLE_*.md Cross-References
- [ ] **P7.8** `[WRITE]` — Fixe templates/lebendige_dateien/*.md Cross-References
- [ ] **P7.9** `[WRITE]` — Fixe notfall/*.md Cross-References
- [ ] **P7.10** `[VERIFY]` — `grep -r "STORAGE/" session_handover_generator/` zeigt konsistente Pfade
- [ ] **P7.11** `[VERIFY]` — `grep -r "HANDOVER/" session_handover_generator/` zeigt konsistente Pfade
- [ ] **P7.12** `[VERIFY]` — `grep -r "DESK/" session_handover_generator/` zeigt konsistente Pfade

### SubAgent-Orchestration Phase 7
- Keine SubAgents.

### Model-Wahl Phase 7
- 🔴 STARK (Reasoning für Pfad-Konsistenz)

### DoD Phase 7
- Alle Cross-References zeigen auf existierende Dateien
- 3 grep-Verifikationen bestanden
- Keine "nicht-existente"-Pfade mehr

### STOPP 7 — Berichte Verifikation, warte auf GO

---

## PHASE 8: ARCHIV-BLOCK IN ALTE DATEIEN (10 Min) — 🟢 STANDARD

**Ziel:** `HANDOVER/Prompts/Templates/` mit ARCHIV-Block markieren.

### Schritte
- [ ] **P8.1** `[READ]` — LIES HANDOVER/Prompts/Templates/ (6 alte Dateien)
- [ ] **P8.2** `[WRITE]` — Füge ARCHIV-Block in HANDOVER/Prompts/Templates/HANDOVER_TEMPLATE.md
- [ ] **P8.3** `[WRITE]` — Füge ARCHIV-Block in HANDOVER/Prompts/Templates/IMPLEMENTATION_PLAN_TEMPLATE.md
- [ ] **P8.4** `[WRITE]` — Füge ARCHIV-Block in HANDOVER/Prompts/Templates/P00_BOOTSTRAP.md
- [ ] **P8.5** `[WRITE]` — Füge ARCHIV-Block in HANDOVER/Prompts/Templates/P01_SESSION_INIT.md
- [ ] **P8.6** `[WRITE]` — Füge ARCHIV-Block in HANDOVER/Prompts/Templates/P02_HANDOFF.md
- [ ] **P8.7** `[WRITE]` — Füge ARCHIV-Block in HANDOVER/Prompts/Templates/P03_RESERVED.md
- [ ] **P8.8** `[WRITE]` — Füge ARCHIV-Block in HANDOVER/Prompts/Templates/TASK_ENVELOPE_TEMPLATE.md

### Format ARCHIV-Block
```markdown
<!-- ARCHIV-MARKER-START -->
> ⚠️ **ARCHIV — Veraltet seit 2026-06-07**
> Diese Datei wird nicht mehr gepflegt.
> Aktuelle Version: `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/[DATEINAME]`
> Konservierungs-Gesetz 1: KEINE LÖSCHUNG — Datei bleibt zu Auditzwecken.
<!-- ARCHIV-MARKER-END -->
```

### SubAgent-Orchestration Phase 8
- Keine SubAgents.

### Model-Wahl Phase 8
- 🟢 STANDARD

### DoD Phase 8
- 7 ARCHIV-Blöcke eingefügt
- Konsistentes Format

### 🛑 **STOPP FÜR MODELL-WECHSEL** — Bestätigung Operator. Nächstes Modell: 🔴 STARK für Phase 9-10.

---

## PHASE 9: FORENSISCHE PRÜFUNG (15 Min) — 🔴 STARK

**Ziel:** End-to-End-Verifikation, dass der Skill fehlerfrei funktioniert.

### Schritte
- [ ] **P9.1** `[VERIFY]` — `ls STORAGE/TEMPLATES/BUNDLE_KOMPAKT/KOPIERPAKET/` — erwarte ≥17 Dateien
- [ ] **P9.2** `[VERIFY]` — `ls STORAGE/TEMPLATES/BUNDLE_KOMPAKT/REPORT_GEN/` — erwarte 1 Datei
- [ ] **P9.3** `[VERIFY]` — LIES SKILL.md YAML-Header, prüfe "Read 25 lines first" vorhanden
- [ ] **P9.4** `[VERIFY]` — LIES SKILL.md HD-0 (Token-Frage als erste Aktion)
- [ ] **P9.5** `[VERIFY]` — LIES INSTRUCTIONS.md alle 6 P99-Schritte vorhanden
- [ ] **P9.6** `[VERIFY]` — LIES INSTRUCTIONS.md 4-Staffel-Tabelle
- [ ] **P9.7** `[VERIFY]` — LIES examples/EXAMPLE_HANDOVER.md 7 Sektionen
- [ ] **P9.8** `[VERIFY]` — LIES Info-Blöcke in 9 Skill-Dateien
- [ ] **P9.9** `[VERIFY]` — `grep -r "STORAGE/TEMPLATES/BUNDLE_KOMPAKT/KOPIERPAKET/" session_handover_generator/` zeigt Cross-References
- [ ] **P9.10** `[VERIFY]` — `grep -r "ARCHIV" HANDOVER/Prompts/Templates/` zeigt 7 Treffer
- [ ] **P9.11** `[VERIFY]` — `grep -r "Read 25 lines" session_handover_generator/SKILL.md` zeigt 1 Treffer
- [ ] **P9.12** `[VERIFY]` — `grep -r "HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN" session_handover_generator/examples/` zeigt konsistente Session-Titel

### SubAgent-Orchestration Phase 9
- Keine SubAgents.

### Model-Wahl Phase 9
- 🔴 STARK (Reasoning für Verifikation)

### DoD Phase 9
- Alle 12 Verifikationen bestanden
- Keine gebrochenen Cross-References
- Alle P99-Formulierungen integriert

### STOPP 9 — Berichte Verifikation, warte auf GO

---

## PHASE 10: DOKUMENTATION & ABSCHLUSS (10 Min) — 🟡 MITTEL

**Ziel:** task.md, walkthrough.md, decision_log.md, hard_learned_facts.md aktualisieren.

### Schritte
- [ ] **P10.1** `[WRITE]` — Aktualisiere task.md mit allen abgeschlossenen Phasen
- [ ] **P10.2** `[WRITE]` — Aktualisiere walkthrough.md mit chronologischer Protokollierung
- [ ] **P10.3** `[WRITE]` — Aktualisiere decision_log.md mit allen Entscheidungen
- [ ] **P10.4** `[WRITE]` — Aktualisiere hard_learned_facts.md mit Erkenntnissen
- [ ] **P10.5** `[WRITE]` — Aktualisiere implementation_plan.md mit Status
- [ ] **P10.6** `[WRITE]` — Bestätigungs-Formel an User

### SubAgent-Orchestration Phase 10
- Keine SubAgents.

### Model-Wahl Phase 10
- 🟡 MITTEL (klare Sprache für User-Kommunikation)

### DoD Phase 10
- Alle 6 lebendigen Dateien aktualisiert
- Bestätigungs-Formel an User

### 🛑 **FINAL-STOPP** — Bestätigung Operator. Bereit für Session-Abschluss.

---

## GESAMT-ÜBERSICHT

| Phase | Ziel | Modell | Dauer | SubAgents |
|:---|:---|:---:|:---:|:---:|
| 0 | Alle Quelldateien lesen | 🔴 STARK | 5 Min | 0 |
| 1 | STORAGE-Migration | 🟢 STANDARD | 10 Min | 0 |
| 2 | P99 in SKILL.md | 🔴 STARK | 20 Min | 0 |
| 3 | README in INSTRUCTIONS.md | 🔴 STARK | 15 Min | 0 |
| 4 | Info-Blöcke | 🟢 STANDARD | 10 Min | 0 |
| **STOPP 1** | **Model-Wechsel zu 🔴 STARK** | | | |
| 5 | HANDOVER-Sektionen | 🔴 STARK | 15 Min | 0 |
| 6 | P00/P01/P02 | 🔴 STARK | 20 Min | 0 |
| 7 | Cross-References | 🔴 STARK | 15 Min | 0 |
| 8 | ARCHIV-Blöcke | 🟢 STANDARD | 10 Min | 0 |
| **STOPP 2** | **Model-Wechsel zu 🔴 STARK** | | | |
| 9 | Forensische Prüfung | 🔴 STARK | 15 Min | 0 |
| 10 | Dokumentation | 🟡 MITTEL | 10 Min | 0 |
| **GESAMT** | | | **~2.5 Stunden** | 0 |

---

## ABBRUCH-BEDINGUNGEN

Stopp SOFORT und Operator informieren wenn:
- Token-Budget fällt unter 30% während Phase 5-7
- Verstoß gegen Konservierungs-Gesetze (1-4) erkannt
- Mehr als 3 STOPPs ohne klares Ergebnis
- Phase 1 (STORAGE-Migration) schlägt fehl → STOPP, User fragen

---

## VERIFIKATIONS-PLAN (gesamt)

- **Phase 1:** `ls` zeigt 17+2+1 Dateien
- **Phase 2-3:** `grep` zeigt alle P99-Schritte + 4-Staffel-Tabelle
- **Phase 4:** `grep` zeigt 9 Info-Blöcke
- **Phase 5-7:** Verifikation der Cross-References
- **Phase 8:** `grep` zeigt 7 ARCHIV-Blöcke
- **Phase 9:** 12 Verifikationen bestanden
- **Phase 10:** Alle 6 lebendigen Dateien aktualisiert

---

## BEMERKUNG

Dieser Plan wurde NACHTRÄGLICH erstellt, nachdem der User zu Recht kritisierte, dass ich ohne Plan gearbeitet und Dateien vergessen habe. Die Phasen 2-7 sind KRITISCH und müssen in der angegebenen Reihenfolge durchgeführt werden. Jede Phase hat ein explizites DoD und einen STOPP-Punkt.
