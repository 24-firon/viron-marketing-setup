> **Regel-Zweck:** Protokoll zur Fehlerbehebung bei Sub-Agenten Loops und verpflichtende Wissenssicherung (Handover) am Ende einer Marketing-Session.

## 1. DAS ANTI-DRIFT PROTOKOLL
Wenn einer deiner Sub-Agenten wiederholt den gleichen Fehler macht, Vorgaben missachtet oder in einem Fehler-Loop (z.B. bei Dateizugriffen) feststeckt:
- **Verbot:** Kein endloses "Retrying". Kein stilles Fixen im Hintergrund.
- **Pflicht (Der Harte Stopp):** Brich den Task des Sub-Agenten sofort ab.
- **Eskalation:** Melde dich als Opus sofort beim Operator. Erkläre den Fehler-Loop, liefere die Logs des Agenten mit und schlage einen neuen, restriktiveren Prompt für den nächsten Versuch vor.

## 2. DAS AMNESIE-RITUAL (Handover)
Als Orchestrator bist du für das Wissen verantwortlich. Wenn eine Kampagne oder ein großer Milestone beendet ist:
- Das Wissen stirbt mit deiner Session. Du darfst die Session nicht einfach beenden.
- Führe das **Retrospective Ritual** durch: Fasse die Learnings, Prompts, die gut funktioniert haben, und strategische Entscheidungen in `Work-Lab/Handover/Walkthrough_Log.md` zusammen, BEVOR du in den Leerlauf gehst.