<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Atomare Task-Verwaltung pro Session (M1/M2/M3)
> - Silo-Struktur mit Checkboxen und Prioritäten
> - SubAgent-Orchestration-Matrix
> - Model-Wechsel-Prüfpunkte pro Meilenstein
>
> - **Wann pflegen:** Nach jedem Task-Abschluss (HD-7)
> - **Bundle-Verwendung:** Diese Datei wird nach `HANDOVER/TASK_[SESSION]_V[N]/` kopiert. Sie ist ein TEMPLATE zum Ausfüllen.
<!-- TEMPLATE-EXPLANATION-END -->

# task.md — Template für Session-Task-Tracking

> **Zweck:** Atomare Task-Verwaltung pro Session. Haupt- und Unterpunkte, Meilensteine, Model-Wechsel-Prüfpunkte.
> **Wann pflegen:** Nach jedem Task-Abschluss, NICHT erst am Session-Ende (HD-7).

---

## Session-Header

```
SESSION: [PROJEKT]_[TYP]_[KURZTHEMA]_V[N]
DATUM: [YYYY-MM-DD]
START: [HH:MM]
TOKEN-STATUS: [🟢/🟡/🔴/⚫]
MODELL: [🔴 STARK / 🟡 MITTEL / 🟢 STANDARD / ⚡ LIGHT]
```

---

## Hauptaufgabe (M1)

**Ziel:** [Was ist das große Ziel dieser Session?]

- [ ] **TS-01.10** `[READ-ONLY]` — [atomare Aktion, z.B. "Scanne BUNDLE_KOMPAKT/"]
- [ ] **TS-01.20** `[READ-ONLY]` — [atomare Aktion]
- [ ] **TS-01.30** `[WRITE]` — [atomare Aktion]
- [ ] **TS-01.40** `[TEST]` — [Verifikation]

⏸️ **STOPP 1** — Berichte Ergebnis. Zeige letzte 5 Zeilen Output. Warte auf GO.

**Model-Wechsel-Check:** Modell-Wechsel nach M1? WENN ja → STOPP für Wechsel.

---

## Meilenstein 2 (M2)

**Ziel:** [Was wird in M2 erreicht?]

- [ ] **TS-02.10** `[WRITE]` — [atomare Aktion]
- [ ] **TS-02.20** `[WRITE]` — [atomare Aktion]
- [ ] **TS-02.30** `[VERIFY]` — [Verifikation]

⏸️ **STOPP 2** — Berichte Ergebnis. Warte auf GO.

**Model-Wechsel-Check:** Modell-Wechsel nach M2? WENN ja → STOPP für Wechsel.

---

## Meilenstein 3 (M3)

**Ziel:** [Was wird in M3 erreicht?]

- [ ] **TS-03.10** `[TEST]` — [Verifikation]
- [ ] **TS-03.20** `[DOC]` — [Dokumentation]
- [ ] **TS-03.30** `[REPORT]` — [Session-Report schreiben]

⏸️ **STOPP 3** — Abschluss. Vorbereitung für Session-Abschluss (6 Schritte).

---

## SubAgent-Orchestration

| SubAgent | Auftrag | Status | Output-Pfad |
|:---|:---|:---:|:---|
| [General Agent] | [z.B. "Bundle-Migration"] | ✅/🟡/❌ | [Pfad] |
| [Explorer] | [z.B. "Vergleiche 4 Bundles"] | ✅/🟡/❌ | [Pfad] |
| [Read-Only] | [z.B. "Zähle alle .md-Dateien"] | ✅/🟡/❌ | [Pfad] |

**Vor jedem SubAgent-Spawn:** STOPP für Modell-Wechsel (Operator-Permission).

**Nach jedem SubAgent-Report:** STOPP, Bewertung, Integration in lebendige Dateien.

---

## Blockierte Tasks

- [!] **[Task-Name]** — blockiert durch: [Grund], WORKAROUND: [Workaround]

---

## Prioritäten

- **P0 🔴 KRITISCH** — Sofort, blockiert alles andere
- **P1 🟡 HOCH** — Diese Session, wichtig
- **P2 🟢 NORMAL** — Nächste Session
- **P3 ⚪ NIEDRIG** — Irgendwann
