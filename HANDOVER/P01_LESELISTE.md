<!-- TEMPLATE-EXPLANATION-START -->
> **Für den Agenten der dieses Bundle etabliert:**
>
> **Was in dieser Datei steht:**
> - P01 ist LESE-MODUS. Kein Planen, kein Editieren. Nur lesen und Kontext aufbauen.
> - Comprehension Gate 1 (Bestätigung P00-Antworten)
> - TIER 1 in 3 Batches (Herzstück → Fundament → Material) mit 5-10 Zeilen Notizen
> - TIER 2: Dateien die bei Bedarf gelesen werden
> - TIER 3: Skip-Liste
>
> **REGEL:** DOCS-Dateien gehören NICHT auf die Leseliste — sie werden automatisch injiziert. Nur DESK-Dateien und task-spezifische Dateien werden geladen.
<!-- TEMPLATE-EXPLANATION-END -->

# P01 — LESELISTE (Master-Variante)

> **P00 BESTANDEN.** Du hast die Fragen beantwortet. Jetzt liest du die Dateien die du für diese Task brauchst.
>
> **P01 ist LESE-MODUS.** Kein Planen, kein Editieren. Nur lesen und Kontext aufbauen. Jede Datei MUSS gelesen werden — nicht überfliegen, nicht abhaken.
>
> **Nächstes Modell:** ⚡ LIGHT (kein Reasoning nötig, nur iteratives Lesen)

---

## COMPREHENSION GATE 1

Bevor du mit der Leseliste beginnst, bestätige dass deine P00-Antworten korrekt waren:

> "Ich habe [X] Fragen in P00 beantwortet. Meine Antworten basieren auf dem was ich aus den injizierten Dateien verstanden habe. Ich habe nichts geraten. Ich habe jede Regel durchdacht. Ich habe die opencode.jsonc-Datei geprüft und alle injizierten Dateien bestätigt."

**Wenn diese Bestätigung fehlt:** STOPP. Zurück zu P00.

---

## TIER 1 — PFLECHT LESEN (3 Batches)

Diese Dateien MÜSSEN gelesen werden bevor mit der Task begonnen wird. Keine Ausnahme.

### BATCH 1 — Das Herzstück (Architektur + IST-Zustand)

| # | Datei | Warum |
|:--|:------|:------|
| 1 | `REPO_BRIEFING.md` | Repo-Identität, Zonen, 00-70 System, Verfassung |
| 2 | `RULE_ROUTER.md` | Task-basierte Navigation → welche Regel wohin |
| 3 | `DESK/TASKS/active/task.md` | Zentraler Task-Envelope mit Scope, DoD und Blockern |

**Nach Batch 1 (5-10 Zeilen Notiz):**
- "Was ist die KERN-ARCHITEKTUR?"
- "Was ist die Mission dieser Session?"
- "Was blockiert den nächsten Schritt?"

### BATCH 2 — Das Fundament (Regeln + Constraints)

| # | Datei | Warum |
|:--|:------|:------|
| 4 | `REPORTS/SRC-ANALYSE.md` | Registry de-synchronisiert, 82 Dateien in src/rules/ |
| 5 | `REPORTS/UNINDEXED_FILES_REPORT.md` | 2.089 Dateien im Repo, nur 80 injiziert — was fehlt? |
| 6 | `DELIVERY/Context_Dispatcher_V6_Init/SESSION_HANDOVER.md` | V6-Prinzipien: Sog-Prinzip, 6 Säulen, Context-Hack, XML-Reporting |

**Nach Batch 2 (5-10 Zeilen Notiz):**
- "Welche REGELN gelten für diese Session?"
- "Welche vergangenen FEHLER sind hier relevant?"
- "Gibt es WIDERSPRÜCHE zwischen alten und neuen Regeln?"

### BATCH 3 — Das Material (Arbeitsmaterial)

| # | Datei | Warum |
|:--|:------|:------|
| 7 | `REPORTS/DETOX_EXECUTION_LOG.md` | Was wurde bereits bereinigt (73 Dateien, 2026-04-08) |
| 8 | `DESK/TASKS/active/implementation_plan.md` | Linearer Ausführungsplan mit Meilensteinen |

**Nach Batch 3 (5-10 Zeilen Notiz):**
- "Was ist der IST-ZUSTAND?"
- "Was ist das SOLL?"
- "Welche Dateien sind BETROFFEN?"

**REGEL:** DOCS-Dateien gehören NICHT auf die Leseliste — sie werden automatisch injiziert. Nur DESK-Dateien und task-spezifische Dateien werden geladen.

**Aktion:** Lies alle Dateien komplett. Bestätige: "[X]/[X] gelesen. Notizen: [3 Zeilen]"

---

## TIER 2 — BEI BEDARF (nur wenn relevant)

| Datei | Wann lesen |
|:------|:-----------|
| `IMPORT/System/welle3_boot_sequenz.csv` | Wenn Boot-Sequenz-Vergleiche nötig |
| `dispatcher/README_DISPATCHER.md` | Wenn Rule-Builder verstanden werden muss |
| `IMPORT/sub-agent-prompting.md` | Wenn Sub-Agenten gespawnt werden |
| `IMPORT/Brain_Surgeon_System.md` | Wenn Session-Archivierung gebraucht wird |
| `STORAGE/skill-creation-knowledge.md` | Wenn Skills erstellt/optimiert werden |

**REGEL:** DOCS-Dateien (DECISION_LOG.md, VERSIONSABHAENGIG.md, etc.) sind auto-injiziert und gehören NICHT in Tier-2. Nur STORAGE-Dateien und task-spezifische Dateien werden geladen.

---

## TIER 3 — SKIP

| Datei | Warum Skip |
|:------|:-----------|
| `DELIVERY/` (alle 13 Stacks) | Delivery-Bundles, nicht für internes Verständnis |
| `_ARCHIVE/` | Historisch, nicht für aktuelle Arbeit |
| `.git/` | Git-Metadaten |
| `node_modules/` | Dependencies |

---

## ANPASSUNG DER BATCH-LOGIK

**Für kleine Sessions (< 10 Dateien):**
- Batches 1-3 zusammenfassen
- Notizen auf 2-3 Zeilen kürzen

**Für große Sessions (> 50 Dateien, > 100KB):**
- Strikt trennen
- Nach jedem Batch 5-10 Zeilen Notiz
- Phase 2 (Forensik) mit Vor-Analysen + Repo-Ist prüfen

---

## ABSCHLUSS

Wenn alle Tier-1-Dateien gelesen sind:

> "P01 gelesen. [X]/[X] Dateien verarbeitet. Batch-Notizen erstellt. Bereit für P01_SESSION_INIT."

**⏸️ STOPP — P01 gelesen. [X] Dateien verarbeitet. Bereit für P01_SESSION_INIT.**
→ **Nächstes Modell:** 🔴 STARK (Planung, Fragen beantworten, Meilensteine definieren)
→ **Warte auf explizites "GO" vom Operator.**

**STOPPLINIE:** Kein Planen. Kein Editieren. Nur lesen.
