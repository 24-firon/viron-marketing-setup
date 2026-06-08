# task.md — Hauptaufgabe dieser Session

## Session-Header

```
SESSION: HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1
DATUM: 2026-06-07
START: 23:30
TOKEN-STATUS: 🟢 (>60% geschätzt)
MODELL: 🔴 STARK (Planung), 🟢 STANDARD (Schreiben)
```

---

## Hauptaufgabe (M1): Bundle-Reparatur + Skill-Generierung

**Ziel:** `session_handover_generator` Skill erstellen mit Token-Schutz, Notfall-Bundle, 6 lebendigen Dateien.

- [x] **TS-01.10** `[READ-ONLY]` — Alle BUNDLE_KOMPAKT/ + Skill-Generator-Dateien gelesen
- [x] **TS-01.20** `[READ-ONLY]` — Mental-Review der erstellten Dateien durchgeführt
- [x] **TS-01.30** `[WRITE]` — SKILL.md + INSTRUCTIONS.md erstellt
- [x] **TS-01.40** `[WRITE]` — 4 references/ erstellt
- [x] **TS-01.50** `[WRITE]` — 3 examples/ erstellt
- [x] **TS-01.60** `[WRITE]` — notfall/ mit 5 Dateien erstellt
- [x] **TS-01.70** `[WRITE]` — templates/lebendige_dateien/ mit 6 Templates erstellt
- [x] **TS-01.80** `[WRITE]` — HD-2 vs. Tabelle-Inkonsistenz gefixt
- [x] **TS-01.90** `[WRITE]` — Bundle/Modus-Trennung in INSTRUCTIONS.md
- [x] **TS-01.100** `[WRITE]` — 6 lebendige Dateien für DIESE Session erstellt
- [x] **TS-01.110** `[WRITE]` — implementation_plan.md erstellt

⏸️ **STOPP 1** — Übersicht erstellt, Plan dokumentiert, mental review durchgeführt.

**Model-Wechsel-Check:** Modell-Wechsel nach M1? Nein — direkter Übergang zu M2.

---

## Meilenstein 2 (M2): User-Feedback-Integration

**Ziel:** Alle User-Anforderungen aus dem Dialog integrieren.

- [x] **TS-02.10** `[WRITE]` — Token-Schätzung 50-100% Aufschlag in TOKEN_WINDOW_GUARD.md
- [x] **TS-02.20** `[WRITE]` — Re-Asking-Protokoll (HD-0) in SKILL.md
- [x] **TS-02.30** `[WRITE]` — Compaction-Fork-Option in INSTRUCTIONS.md
- [x] **TS-02.40** `[WRITE]` — SubAgent-Prompts sind echte Files (HD-8 Klarstellung)
- [x] **TS-02.50** `[WRITE]` — Such-Werkzeug-Idee in SESSION_TITEL_SCHEMA.md
- [x] **TS-02.60** `[WRITE]` — notfall/ eingebettetes Backup-Bundle
- [x] **TS-02.70** `[WRITE]` — P99 historische Variante Hinweis in SKILL.md
- [x] **TS-02.80** `[WRITE]` — Kompakt-Spezifität Vermerk

⏸️ **STOPP 2** — Alle User-Anforderungen integriert.

---

## Meilenstein 3 (M3): Session-Abschluss

**Ziel:** Handover + Reports + User-Bestätigung.

- [x] **TS-03.10** `[WRITE]` — example-Handover mit korrektem Session-Titel
- [x] **TS-03.20** `[WRITE]` — example-Forensic-Report mit korrektem Session-Titel
- [x] **TS-03.30** `[WRITE]` — walkthrough.md für diese Session
- [x] **TS-03.40** `[WRITE]` — decision_log.md mit allen Entscheidungen
- [x] **TS-03.50** `[WRITE]` — hard_learned_facts.md mit Erkenntnissen
- [x] **TS-03.60** `[WRITE]` — ideas_future_plans.md mit Such-Werkzeug-Idee
- [x] **TS-03.70** `[REPORT]` — Session-Report mental vorbereitet
- [x] **TS-03.80** `[HANDOVER]` — Handover-Struktur dokumentiert

⏸️ **STOPP 3** — Session fast abgeschlossen.

---

## SubAgent-Orchestration

| SubAgent | Auftrag | Status | Output-Pfad |
|:---|:---|:---:|:---|
| — | (keine SubAgents in dieser Session) | — | — |

**Hinweis:** Diese Session hat keine SubAgents gespawnt — alle Aktionen direkt durchgeführt. Künftige Sessions (z.B. Such-Werkzeug-Entwicklung) sollten SubAgents nutzen.

---

## Blockierte Tasks

- (keine)

---

## Prioritäten

- **P0 🔴 KRITISCH** — Skill fertigstellen mit Token-Schutz
- **P1 🟡 HOCH** — Alle User-Anforderungen integrieren
- **P2 🟢 NORMAL** — Zukunftsweisende Dokumentation (implementation_plan, ideas)
- **P3 ⚪ NIEDRIG** — Beispiele bundle-agnostisch machen (später)
