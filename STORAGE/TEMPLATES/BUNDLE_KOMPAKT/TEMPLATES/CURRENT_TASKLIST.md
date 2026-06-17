# CURRENT TASKLIST (Kompakt)

> Task-Tracker mit Silo-Struktur. [ ] = offen, [x] = erledigt, [!] = blockiert. **DENN** ohne klare Status-Übersicht weiß der nächste Agent nicht was noch zu tun ist.

## KOPFZEILE

```
SPRINT: [z.B. 2026-W22]
STAND: [YYYY-MM-DD]
ZÄHLER: offen / erledigt / blockiert
```

## SILO 01: [Name, z.B. AUDIT]

**DoD für Silo 01:** [Was muss am Ende dieses Silos erreicht sein?]

- [ ] **TS-01.10** `[READ-ONLY]` — [konkrete Aufgabe, z.B. "Scanne apps/ rekursiv"]
- [ ] **TS-01.20** `[READ-ONLY]` — [konkrete Aufgabe]
- [ ] **TS-01.30** `[DOC]` — [z.B. "Ergebnisse in FOLDER_MAP.md dokumentieren"]

## SILO 02: [Name, z.B. REFACTORING]

**DoD für Silo 02:** [Definition of Done]

- [ ] **TS-02.10** `[WRITE]` — [konkrete Aufgabe, z.B. "Refactor HeroSection.tsx"]
- [ ] **TS-02.20** `[WRITE]` — [konkrete Aufgabe]
- [ ] **TS-02.30** `[TEST]` — [z.B. "pnpm build clean durchläuft"]

## SILO 03: [Name, z.B. SECURITY/AUTH]

**DoD für Silo 03:** [Definition of Done]

- [ ] **TS-03.10** `[WRITE]` — [konkrete Aufgabe, z.B. "Supabase Auth Middleware einbinden"]
- [ ] **TS-03.20** `[TEST]` — [z.B. "Curl ohne Bearer-Token → 401"]

## SILO 04: VERIFICATION & DOC

**DoD für Silo 04:** [Definition of Done]

- [ ] **TS-04.10** `[TEST]` — [z.B. "End-to-End-Test der 3D-UI"]
- [ ] **TS-04.20** `[DOC]` — [z.B. "Finalen Abschlussbericht generieren"]

## BLOCKIERTE TASKS

- [!] **[Task-Name]** — blockiert durch: [Grund], WORKAROUND: [Workaround]

## PRIORITÄTEN

- **P0 🔴 KRITISCH** — Sofort, blockiert alles andere
- **P1 🟡 HOCH** — Diese Session, wichtig
- **P2 🟢 NORMAL** — Nächste Session
- **P3 ⚪ NIEDRIG** — Irgendwann
