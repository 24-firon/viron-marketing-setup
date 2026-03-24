> **Regel-Zweck:** Erzwingt kosteneffizientes Modell-Routing und einen obligatorischen Stopp bei Wechsel des LLM-Modells zur Bestätigung durch den Operator.

## 1. DIE HARTE TRENNUNG (Kosten-Disziplin)
Es ist strikt VERBOTEN, teure Modelle (Opus / Gemini High) für Basis-Research oder das massenhafte Lesen von Logs/Airtable-Dumps zu verwenden.

- **Research & Katalogisierung:** IMMER auf `⚡ GEMINI LOW` (oder Haiku).
- **Copy-Writing & Kampagnen-Logik:** IMMER auf `🟢 SONNET`.
- **Strategie-Review & Master-Orchestrierung:** Exklusiv für `🔴 OPUS`.

## 2. DER HARTE STOPP (Modell-Wechsel)
Blindflug beim Modellwechsel führt zu Token-Tod.
- **Regel:** Wenn du (Opus) entscheidest, dass ein Task an einen Sub-Agenten mit einem anderen Modell geht, MUSST du pausieren.
- **Protokoll:** "🛑 HARTER STOPP: Wechsel auf [MODELL] für Task [NAME] erforderlich. Gib Go."
- **Verbot:** Starten eines neuen Task-Blocks ohne explizite Bestätigung des Operators für das gewählte Modell.