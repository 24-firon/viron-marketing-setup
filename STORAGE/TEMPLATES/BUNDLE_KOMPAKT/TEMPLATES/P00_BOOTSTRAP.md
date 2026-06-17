# P00 — Bootstrap (Kompakt)

> **READ-ONLY.** Beantworte zuerst die Fragen, dann prüfe was via `opencode.jsonc` geladen ist. **DENN** wer die Regeln nicht durchdrungen hat, wird in der ersten Session scheitern.

## 7 FRAGEN (testen ANWENDUNG, nicht RECALL)

Beantworte jede Frage. Wenn du eine nicht beantworten kannst: STOPP und nachladen.

**1. Injektions-Mechanismus**
Du hast 80+ Dateien via `opencode.jsonc` injiziert bekommen. Was passiert, wenn du eine DOCS-Datei behandelst als müsstest du sie mit `read` laden?

**2. Thin Triggers**
Eine Boot-Regel in `.opencode/rules/` ist 200 Zeilen lang. Was ist die konkrete Konsequenz? Warum sollen Regeln 5-15 Zeilen sein?

**3. 10er-Routing**
Du findest eine Regel mit dem Präfix `12_`. Was ist das Problem? Wie lautet die korrekte Konvention?

**4. Local Override**
Globale Skill-Regel erlaubt X, `.opencode/rules/` verbietet X. Welche gilt? Was passiert wenn du die globale nimmst?

**5. Dispatcher-Rolle**
Eine Regel sagt: "Deploye niemals ohne Operator-Approval." Bist du als Dispatcher daran gebunden, oder gilt das nur für Sub-Agents?

**6. Skill-Routing**
Ein Skill hat 579 Zeilen. Was liest du zuerst? Was ist die 50-Zeilen-Regel?

**7. Sub-Agent-Briefing**
Du spawnst einen Sub-Agent für eine schreibende Aufgabe. Welche 4 Säulen MUSS dein Prompt enthalten? Was passiert, wenn du nur die Mission schickst?

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
