---
name: session-handover-generator
description: Session-Wechsel zwischen Haupt- und Folgesession. Erzeugt Übergabe-Templates und Handover. Trigger: "Sessionwechsel", "Handover", "Übergabe", "schließe Session ab". Lade INSTRUCTIONS.md für Workflow.
---

# session_handover_generator

> **Was dieser Skill tut:** Erzeugt die Übergabe zwischen zwei Sessions. Die 6 Schritte dazu stehen in INSTRUCTIONS.md. SKILL.md selbst erklärt nur WAS und WARUM.

---

## User-Intention zuerst (IMMER vor allem anderen)

Bevor du irgendetwas tust, kläre mit dem User:

1. **Was** will er? (Session-Wechsel, Bericht, Handover-Bearbeitung, ...)
2. **Wie umfangreich?** (Schnell / Normal / Ausführlich / Forensisch)
3. **Erst dann:** Token-Status, Modi, Bundle.

> **Ohne klare User-Intention: Keine Skill-Aktion.** Lieber einmal nachfragen als hundert Annahmen treffen.

---

## Die 6 Schritte (Zusammenfassung, Details in INSTRUCTIONS.md)

1. Session-Report schreiben
2. HANDOVER.md befüllen
3. Task-Liste aktualisieren
4. Walkthrough ergänzen
5. Session-Ritual ausführen
6. P00-Fragen für nächste Session schreiben

> **Historischer Kontext:** Diese 6 Schritte waren früher als `P99_HANDOFF.md` ein separates Konzept. Jetzt sind sie Teil dieses Skills (SKILL.md = Erklärung, INSTRUCTIONS.md = Details).

---

## Wenn das Token-Budget knapp wird

Die Token-Farbe schränkt das LADEN ein, **nicht die Aktion**.

- 🟢 > 60%: Alles erlaubt
- 🟡 30-60%: Beim Laden vorsichtig — bevorzuge INSTRUCTIONS.md, einzelne references
- 🔴 < 30%: Nur das Nötigste laden
- ⚫ < 15%: Notfall-Modus — warnen, ggf. Session verschieben

**Wichtig:** Wenn die User-Intention klar ist (Session-Wechsel gewünscht), führe ihn aus — auch wenn das Token-Budget knapp ist. Warne, aber blockiere nicht.

---

## Was dieser Skill NICHT ist

- ❌ Keine technische Anleitung (→ INSTRUCTIONS.md)
- ❌ Keine Token-Berechnungen (→ INSTRUCTIONS.md)
- ❌ Keine Bundle-Details (→ INSTRUCTIONS.md)
- ❌ Keine SubAgent-Spawn-Logik (→ INSTRUCTIONS.md + PROMPTS/)

---

## Datei-Inventar (Kurz-Übersicht)

```
session_handover_generator/
├── SKILL.md           ← diese Datei (Erklärung, kurz)
├── INSTRUCTIONS.md    ← Workflow-Details
├── examples/          ← 10 ausgefüllte Beispiele
├── references/        ← 5 Detail-Dateien
├── templates/         ← 6 leere Schablonen
├── notfall/           ← 5 Backup-Dateien
└── storage/           ← Verweis auf globales STORAGE
```

> **Quelle:** `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/`. Arbeitskopie: `HANDOVER/TASK_[SESSION]_V[N]/`. SKILL.md wird NICHT kopiert — systemisch.
