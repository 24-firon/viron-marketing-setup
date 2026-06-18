# P00 — Bootstrap (Kompakt)

> **READ-ONLY.** Beantworte zuerst die Fragen, dann prüfe was via `opencode.jsonc` geladen ist. **DENN** wer die Regeln nicht durchdrungen hat, wird in der ersten Session scheitern.

## 7 FRAGEN (testen ANWENDUNG, nicht RECALL)

Beantworte jede Frage. Wenn du eine nicht beantworten kannst: STOPP und nachladen.

**1. Skill-Vorgaben befolgen**
Du sollst den `session_handover_generator` Skill ausführen. Der Skill sagt: kopiere Templates aus `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/`, dann lesen, dann aussortieren, dann bearbeiten. Was passiert, wenn du direkt eine eigene Handover-Datei schreibst ohne die Templates zu kopieren?

**2. Sub-Schritt-GO**
Operator sagt „GO für P01". P01 hat 3 Sub-Schritte (P0.1, P0.2, P0.3). Du startest alle 3 stillschweigend in einem Rutsch. Was ist das Problem? Wie hättest du vorgehen sollen?

**3. Spec-Drift markieren**
Du baust einen Skill und die Spec sagt nichts zur PostgreSQL-Schema-Struktur. Du halluzinierst Tabellennamen (`public.mkt_leads`, `public.mkt_lead_events`) und schreibst sie in die SKILL.md. Was sollte stattdessen passieren?

**4. Edit vs. Write bei Bestand**
Du hast eine bestehende SKILL.md und willst 3 Sektionen chirurgisch korrigieren. Du nutzt `write` und überschreibst die ganze Datei. Was geht dabei verloren?

**5. Trigger-Phrasen-Pflege**
Eine Skill-YAML-description listet 12 Trigger-Phrasen. Im Body wiederholst du die gleichen 12 Phrasen als separate Sektion. Was ist das Problem? Wie solltest du es lösen?

**6. Git-Push-Token-Persistenz**
Du willst `git push` machen. Der `gh auth status` zeigt `Viron-Agency` als active. Der Push schlägt 403 fehl, weil `24-firon` der Repo-Owner ist. Was tust du? Was ist der dauerhafte Fix?

**7. Session-Handover-Workflow**
Du willst am Session-Ende einen Handover schreiben. Du schreibst direkt eine Datei in `DESK/HANDOVER/sessions/`. Der Nutzer sagt: „Falsch. Der Skill sagt: kopiere, lies, sortiere aus, bearbeite die Templates aus `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` und lege sie in `HANDOVER/[SESSION]/` ab." Was war dein Fehler? Wie hättest du vorgehen sollen?

---

## OPENCODE.JSONC CHECK (Comprehension Gate Step A)

**Nach den Fragen, BEVOR du P01 betrittst, prüfe was via `opencode.jsonc` in deinem Kontext ist:**

1. **Lies** `opencode.jsonc` im Repo-Root
2. **Zähle** alle Dateien im `instructions`-Array
3. **Prüfe** ob jede Datei physisch in deinem Kontext ist (nicht nur ob sie existiert)
4. **Wenn eine Datei fehlt:** Lade sie SOFORT mit `read` und **melde dem User**: "Datei [NAME] fehlte, wurde nachgeladen."
5. **Erst wenn alle injizierten Dateien verarbeitet sind:** bestätige den Check

**BEWEIS:** "Ich habe [X] injizierte Dateien verarbeitet. [Y] Dateien fehlten und wurden nachgeladen."

---

## 3 KONTEXT-SCHICHTEN

Identifiziere pro Schicht was du hast:

| Schicht | Mechanik | Beispiel |
|:---|:---|:---|
| **DOCS** | Permanent injiziert | AGENTS.md, LESSONS_LEARNED |
| **STORAGE** | On-demand via Router | `STORAGE/[topic].md` |
| **SKILLS** | On-demand via `skill()` | `.opencode/skills/*/SKILL.md` |

## BESTÄTIGUNG

> "P00 bestanden. 7/7 Fragen beantwortet, [X] Dateien im opencode.jsonc-Check bestätigt, 3 Schichten verstanden. Bereit für P01."

⏸️ **STOPP** — Warte auf GO vom Operator. Nächstes Modell: ⚡ LIGHT.
