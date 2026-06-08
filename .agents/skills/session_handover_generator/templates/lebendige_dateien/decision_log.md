<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Chronologische Sammlung wichtiger Entscheidungen
> - Pro Eintrag: Kontext, Entscheidung, Begründung, Reversibilität, Konsequenzen
>
> - **Wann pflegen:** Bei jeder Architektur-Entscheidung (Konservierungs-Gesetz 4)
> - **Bundle-Verwendung:** Diese Datei wird nach `HANDOVER/TASK_[SESSION]_V[N]/` kopiert. Sie ist ein TEMPLATE zum Ausfüllen.
<!-- TEMPLATE-EXPLANATION-END -->

# decision_log.md — Template für chronologische Entscheidungs-Sammlung

> **Zweck:** Chronologische Sammlung wichtiger Entscheidungen mit Begründung.
> **Wann pflegen:** Bei jeder Architektur-Entscheidung (HD-7 + Konservierungs-Gesetz 4: INTEGRATION).

---

## Format pro Entscheidung

```
### [YYYY-MM-DD HH:MM] — [Kurzer Titel]

**Kontext:** [Was war die Situation? Welche Optionen gab es?]

**Entscheidung:** [Was wurde entschieden?]

**Begründung:** [Warum diese Option? Welche Alternative wurde verworfen?]

**Reversibel?** [Ja / Nein / Teilweise] — [Falls nicht: warum nicht?]

**Konsequenzen:** [Was ändert sich durch diese Entscheidung?]
```

---

## Beispiel-Eintrag

```
### 2026-06-07 14:30 — Token-Fenster-Frage als HD-0

**Kontext:** User hatte mehrere Male Token-Budget falsch eingeschätzt. Compaction-Risiko während Handover war real.

**Entscheidung:** Token-Fenster-Frage als ERSTE Aktion in jedem Skill-Workflow erzwingen (HD-0).

**Begründung:** Handover in Compaction = System kompromittiert. User-Schätzung + 50-100% Aufschlag gibt sicheren Korridor.

**Reversibel?** Ja — kann später zu HD-2 degradiert werden wenn Token-Schätzungen verlässlicher werden.

**Konsequenzen:** Skill-Workflow hat eine zusätzliche Eingabe-Tür. User wird öfter nach Token-Status gefragt. Bessere Sicherheit gegen Compaction.
```

---

## [Erste echte Entscheidung hier eintragen]

```
### [DATUM ZEIT] — [TITEL]

**Kontext:** ...

**Entscheidung:** ...

**Begründung:** ...

**Reversibel?** ...

**Konsequenzen:** ...
```
