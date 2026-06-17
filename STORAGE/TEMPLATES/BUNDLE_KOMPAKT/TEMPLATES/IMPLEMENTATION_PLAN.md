# IMPLEMENTATION PLAN (Kompakt)

> **Linearer Plan** mit Meilensteinen. M1 → STOPP → M2 → STOPP → M3. **DENN** der Operator braucht Haltepunkte zur Freigabe.

## KOPFZEILE

```
TASK-ID: [z.B. MIGRATE_01]
PHASE: [z.B. Phase A → B]
RISIKO: [🟢 Low / 🟡 Medium / 🔴 High]
GESCHÄTZTE DAUER: [z.B. ~30 Min]
```

## M1: [Titel der ersten Phase]

**Ziel:** [Was ist erreicht wenn M1 fertig ist?]

### Schritte
- [ ] **Schritt 1.1** `[READ-ONLY]` — [konkrete Aktion, z.B. "Scanne apps/ rekursiv nach siteConfig-Imports"]
- [ ] **Schritt 1.2** `[WRITE]` — [konkrete Aktion, z.B. "Erstelle FOLDER.md für apps/web/"]
- [ ] **Schritt 1.3** `[TEST]` — [z.B. "pnpm build muss clean durchlaufen"]

### DoD (Definition of Done)
- [Was muss erreicht sein damit M1 als fertig gilt?]

⏸️ **STOPP 1** — Berichte Ergebnis. Zeige letzte 5 Zeilen Output. Warte auf GO.

---

## M2: [Titel der zweiten Phase]

**Ziel:** [Was ist erreicht wenn M2 fertig ist?]

### Schritte
- [ ] **Schritt 2.1** `[WRITE]` — [konkrete Aktion]
- [ ] **Schritt 2.2** `[WRITE]` — [konkrete Aktion]
- [ ] **Schritt 2.3** `[VERIFY]` — [z.B. "Vergleiche: alle Dateien vorhanden, kein Inhalt verloren"]

### DoD
- [Was muss erreicht sein damit M2 als fertig gilt?]

⏸️ **STOPP 2** — Berichte Ergebnis. Warte auf GO.

---

## M3: [Titel der dritten Phase]

**Ziel:** [Was ist erreicht wenn M3 fertig ist?]

### Schritte
- [ ] **Schritt 3.1** `[TEST]` — [z.B. "End-to-End-Smoke-Test"]
- [ ] **Schritt 3.2** `[COMMIT]` — [z.B. "Git commit mit conventional commit message"]
- [ ] **Schritt 3.3** `[REPORT]` — [z.B. "Session-Report schreiben"]

### DoD
- [Was muss erreicht sein damit M3 als fertig gilt?]

⏸️ **STOPP 3** — Abschluss. Vorbereitung für P99.

---

## ABBRUCH-BEDINGUNGEN

Stopp SOFORT und Operator informieren wenn:
- Mehr als [X] Dateien betroffen sind als geplant
- Eine externe Abhängigkeit (API, Service) nicht erreichbar
- Konflikt mit existierender Architektur erkannt
- Mehr als [X] STOPPs ohne klares Ergebnis durchlaufen

## VERIFIKATIONS-PLAN

Pro Meilenstein definieren:
- [Was] wird verifiziert
- [Wie] (z.B. "ls zeigt Datei", "grep findet 0 Treffer", "pnpm test läuft clean")
- [Wer] ist verantwortlich (Agent vs. Operator)
