<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Chronologische Protokollierung erledigter Task-Punkte
> - Pro Eintrag: Kontext, Was-wurde-gemacht, Entscheidungen, SubAgent-Einsatz, Token-Status
> - Session-Ende mit Final-Status
>
> - **Wann pflegen:** Nach jedem Meilenstein (HD-7)
> - **Bundle-Verwendung:** Diese Datei wird nach `HANDOVER/TASK_[SESSION]_V[N]/` kopiert. Sie ist ein TEMPLATE zum Ausfüllen.
<!-- TEMPLATE-EXPLANATION-END -->

# walkthrough.md — Template für chronologische Session-Protokollierung

> **Zweck:** Chronologische Ablage erledigter Task-Punkte in Prosa. Strukturell wie task.md + implementation_plan.md, aber reduziert.
> **Wann pflegen:** Nach jedem Meilenstein (HD-7).

---

## Session-Header

```
SESSION: [PROJEKT]_[TYP]_[KURZTHEMA]_V[N]
DATUM: [YYYY-MM-DD]
START: [HH:MM]
ENDE: [HH:MM]
TOKEN-STATUS: [🟢/🟡/🔴/⚫]
```

---

## [YYYY-MM-DD HH:MM] — [Session-Typ / Meilenstein]

### Kontext
[1-2 Sätze: Was war die Ausgangslage? Welcher Task steht an?]

### Was wurde gemacht

- **[Schritt 1]** → [Ergebnis, z.B. "Bundle-Migration gestartet, 4 Verzeichnisse angelegt"]
- **[Schritt 2]** → [Ergebnis]
- **[Schritt 3]** → [Ergebnis]

### Geänderte Dateien

- `[Pfad/Datei]` — [Was wurde geändert?]
- `[Pfad/Datei]` — [Was wurde geändert?]

### Entscheidungen (während dieses Abschnitts)

- [Entscheidung] — [Begründung]
- [Entscheidung] — [Begründung]

### Verifikation

- [Output / Test-Result / Git-Diff]
- [Beweis für Erfolg]

### SubAgent-Einsatz (falls vorhanden)

- SubAgent: [Typ] — [Auftrag] → [Output-Pfad]
- STOPP davor: ✅ | STOPP danach: ✅
- Integration: [Was wurde aus SubAgent-Output übernommen?]

### Token-Status nach diesem Abschnitt

- [🟢/🟡/🔴/⚫] — [Restbudget-Schätzung]
- Maßnahme: [Wenn kritisch: User informieren, Handover kürzen, etc.]

### Nächster Schritt

[Nächster konkreter Schritt, der ansteht]

---

## [YYYY-MM-DD HH:MM] — [Nächster Meilenstein]

### Kontext
[Ausgangslage]

### Was wurde gemacht
- ...

### Geänderte Dateien
- ...

### Entscheidungen
- ...

### Verifikation
- ...

### SubAgent-Einsatz
- ...

### Token-Status
- ...

### Nächster Schritt
- ...

---

## [Datum] — Session-Ende

### Final-Status

- Berichte: [Pfade]
- Handover: [Pfad]
- Nächste Session: [Session-Titel V2]

### Bestätigungs-Formel

> "Session-Wechsel abgeschlossen. [Details]."
