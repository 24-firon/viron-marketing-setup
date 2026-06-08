---
name: session-handover-generator
description: Session-Wechsel zwischen Haupt- und Folgesession. Erzeugt Übergabe-Templates, Handover-Daten, forensische Berichte. Pflegt 6 lebendige Dateien. Trigger: "Sessionwechsel", "Handover", "Übergabe", "schließe Session ab". Lade INSTRUCTIONS.md für Details.
---

# session_handover_generator

> **Was dieser Skill tut:** Erzeugt die Übergabe zwischen einer laufenden Session und der nächsten. Liefert alle Templates, Prompts, Referenzen. Orchestriert den Workflow via INSTRUCTIONS.md.

> **Typische Auslöser:** "Sessionwechsel", "Handover", "Übergabe", "schließe Session ab", "Bereite nächste Session vor".

---

## Was dieser Skill ist (Kurz)

Dieser Skill liefert **alle Templates, Prompts, Referenzen** für einen sauberen Session-Wechsel. Er ersetzt das alte `P99_HANDOFF.md` und bündelt alles in einem Skill.

**Was er liefert:**
- 10 ausgefüllte Beispiele (`examples/`) — DoD-Referenzen
- 6 leere Templates (`templates/lebendige_dateien/`) — für die laufende Session
- 5 Referenz-Dateien (`references/`) — Token-Guard, Session-Titel, Konservierungs-Gesetze, System-Verständnis, Tier-Memory
- 5 Backup-Dateien (`notfall/`) — für Token-Krisen
- 6 Workflow-Prompts (`PROMPTS/`) — Report, SubAgent, Operator, Orchestrator

---

## Was dieser Skill NICHT tut

- ❌ Er schreibt keine Berichte (→ INSTRUCTIONS.md)
- ❌ Er führt keine Git-Kommandos aus (→ INSTRUCTIONS.md)
- ❌ Er spawn't keine SubAgents selbst (→ INSTRUCTIONS.md + PROMPTS/)
- ❌ Er macht keine Token-Berechnungen selbst (→ INSTRUCTIONS.md + TOKEN_WINDOW_GUARD.md)

---

## Der Ablauf (Kurz)

1. **User-Intention klären** — Was für ein Session-Wechsel? (Schnell / Normal / Ausführlich / Forensisch)
2. **INSTRUCTIONS.md lesen** — dort steht der komplette Workflow
3. **Die 6 Schritte ausführen** — Report, Handover, Tasks, Walkthrough, Ritual, P00-Fragen

> **WICHTIG:** Ohne klare User-Antwort auf "Was für ein Session-Wechsel?" → **Keine Aktion**. Lieber einmal nachfragen als hundert Annahmen treffen.

---

## Schritt 1: User-Intention klären (SOFORT)

**Bevor du irgendetwas tust, frage den User:**

> "Was für ein Session-Wechsel soll das sein?
> - **Schnell** (7 Dateien, ~5 Min)
> - **Normal** (10-12 Dateien, Standard)
> - **Ausführlich** (alle 17 Dateien, tief)
> - **Forensisch** (9-Sektionen-Report, tiefste Analyse)"

> **Ohne Antwort: KEINE Aktion.** Lieber nachfragen als raten.

---

## Schritt 2: INSTRUCTIONS.md lesen

Sobald die User-Intention klar ist:

> **Lade jetzt `INSTRUCTIONS.md` und arbeite die 6 Schritte ab.**

Die INSTRUCTIONS.md enthält:
- Die 4 Fragen-Katalog (Bundle, Reports, Handover-Dateien, SubAgent-Prompts)
- Die 4 Staffeln (SLIM/KOMPAKT/KONSOLIDIERT/VOLLSTÄNDIG)
- Die 3 Modi (SCHNELL/NORMAL/AUSFÜHRLICH)
- Die 6 detaillierten Schritte
- Cross-References zu allen Referenz-Dateien
- Konservierungs-Gesetze, SubAgent-Protokoll, Modell-Rotation

---

## Was dieser Skill NICHT tut

- ❌ Er schreibt keine Berichte (→ INSTRUCTIONS.md)
- ❌ Er führt keine Git-Kommandos aus (→ INSTRUCTIONS.md)
- ❌ Er spawn't keine SubAgents selbst (→ INSTRUCTIONS.md + PROMPTS/)
- ❌ Er macht keine Token-Berechnungen selbst (→ INSTRUCTIONS.md + TOKEN_WINDOW_GUARD.md)

---

## Datei-Inventar (Kurz)

```
session_handover_generator/
├── SKILL.md           ← diese Datei (Übersicht, Einstieg)
├── INSTRUCTIONS.md    ← kompletter Workflow
├── examples/          ← 10 ausgefüllte Beispiele
├── references/        ← 5 Detail-Dateien
├── templates/         ← 6 leere Schablonen
├── notfall/           ← 5 Backup-Dateien
└── storage/           ← Verweis auf globales STORAGE
```

> **Quelle:** `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/`. Arbeitskopie: `HANDOVER/TASK_[SESSION]_V[N]/`. SKILL.md wird NICHT kopiert — sie ist systemisch.
