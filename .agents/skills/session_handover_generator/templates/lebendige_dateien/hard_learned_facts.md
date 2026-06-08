<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Chronologische Sammlung wichtiger Learnings
> - Pro Eintrag: Was ist passiert, Erkenntnis, warum wichtig, Anwendung in Zukunft
>
> - **Wann pflegen:** Bei Fehlern, "Aha-Momenten", neuen Erkenntnissen
> - **Bundle-Verwendung:** Diese Datei wird nach `HANDOVER/TASK_[SESSION]_V[N]/` kopiert. Sie ist ein TEMPLATE zum Ausfüllen.
<!-- TEMPLATE-EXPLANATION-END -->

# hard_learned_facts.md — Template für chronologische Learning-Sammlung

> **Zweck:** Chronologische Sammlung wichtiger Learnings — was funktioniert hat, was nicht, was war überraschend.
> **Wann pflegen:** Bei Fehlern, Erkenntnissen, "Aha-Momenten" (HD-7).

---

## Format pro Fact

```
### [YYYY-MM-DD HH:MM] — [Kurzer Titel]

**Was ist passiert?** [Situation beschreiben]

**Was war die Erkenntnis?** [Was haben wir gelernt?]

**Warum war das wichtig?** [Welche Konsequenz hat diese Erkenntnis?]

**Anwendung in Zukunft:** [Wie nutzen wir das in folgenden Sessions?]
```

---

## Beispiel-Eintrag

```
### 2026-06-07 15:00 — LLM schätzt Tokens 50-100% zu niedrig

**Was ist passiert?** Wir haben ein 50KB Dokument auf 10-15K Tokens geschätzt, real waren es 20-25K.

**Was war die Erkenntnis?** LLM-Token-Schätzungen sind systematisch zu niedrig. Die wahre Token-Zahl ist deutlich höher als LLM-Schätzungen.

**Warum war das wichtig?** Ohne diese Erkenntnis hätten wir unsere Token-Budgets ständig überschritten und in Compaction geraten.

**Anwendung in Zukunft:** Immer konservativ planen mit +50% Aufschlag. Token-Frage in jedem Skill-Workflow als erste Aktion (HD-0).
```

---

## [Erstes echtes Fact hier eintragen]

```
### [DATUM ZEIT] — [TITEL]

**Was ist passiert?** ...

**Was war die Erkenntnis?** ...

**Warum war das wichtig?** ...

**Anwendung in Zukunft:** ...
```
