# SESSION HANDOVER — Forensischer Bericht (Kompakt)

> Kurzer Forensik-Bericht am Session-Ende. 9 Sektionen, kalt und präzise. **DENN** jeder Satz ohne VERIFIZIERT/WAHRSCHEINLICH/OFFEN ist wertlos für Auditor und Nachfolger.

---

**Session-Titel:** [Titel]
**Datum:** [YYYY-MM-DD]
**Projekt/Repo:** [Name]
**Scope:** [Backend, Frontend, Auth, DB, DevOps, Research, Monorepo, Security]
**Session-Modus:** [Execution / Read-Only / Research / Debug / Mixed]
**Modell-Tag:** [🔴 STARK / 🟡 MITTEL / 🟢 STANDARD / ⚡ LIGHT]

---

## 1. SYSTEMLAGE

[1-3 dichte Absätze: Ausgangslage, was war kaputt/unklar/gefährlich, warum architektonisch relevant]

## 2. ARCHITEKTUR-ENTSCHEIDUNGEN

- **[Thema]:** [Harter Fakt]
  *Warum:* [Architekturgrund]
- **[Thema]:** [Harter Fakt]
  *Warum:* [Begründung]

Falls keine Änderungen: validierte Erkenntnisse dokumentieren.

## 3. DATEIEN, PFADE & KONFIGURATIONEN

### Geändert
- `[Pfad]` — [Was wurde geändert]

### Neu angelegt
- `[Pfad]` — [Zweck]

### Nicht verändert
- `[Pfad]` — [Warum bewusst nicht angefasst]

## 4. DIAGNOSTIK, TESTS & BEWEISLAGE

- **Verifiziert:** [Beobachtung / Test / Log-Befund]
- **Wahrscheinlich:** [Starker Verdacht, nicht final bewiesen]
- **Offen:** [Nicht geprüft / nicht validiert]

## 5. REPOSITORY-HYGIENE

- Altlasten reduziert: [was]
- Workarounds noch da: [was]
- Doppelte Zustände: [was]

## 6. RISIKEN, TECHNICAL DEBT

- **[Risiko]:** [Beschreibung]
  *Auswirkung:* [Was kann kaputtgehen?]
  *Wahrscheinlichkeit:* [Niedrig / Mittel / Hoch]
  *Empfehlung:* [Was tun?]

## 7. HANDOVER FÜR DEN NÄCHSTEN AGENTEN

### Aktueller belastbarer Zustand
- Funktioniert: [was]
- Teilweise abgesichert: [was]
- Ungeklärt: [was]

### Verbotene Aktionen
- [Was darf der nächste Agent NICHT blind tun?]

### Nächste logische Schritte
1. [Erster konkreter Schritt]
2. [Zweiter konkreter Schritt]
3. [Dritter konkreter Schritt]

## 8. KURZFAZIT

[Ein dichter Satz, der den Zustand der Session präzise auf den Punkt bringt]

---

**[SESSION REPORT ERSTELLT]**

**Ablage:** `DESK/reports/[YYYY-MM-DD]_[PROJEKT]_[TYP].md`
