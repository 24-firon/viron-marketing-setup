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
| 1 | `CONTEXT.md` | Repo-Status, aktuelle Phase, Blocker |
| 2 | `AGENTS.md` | VIRON-Identität, Tool-Stack, Regeln |
| 3 | `HANDOVER/HANDOVER.md` | Active Session-Handover (Daten für nächste Session) |
| 4 | `DESK/TASKS/implementation_plan.md` | Linearer Bauplan für diese Session |

**Nach Batch 1 (5-10 Zeilen Notiz):**
- "Was ist die KERN-ARCHITEKTUR?"
- "Was ist die Mission dieser Session?"
- "Was blockiert den nächsten Schritt?"

### BATCH 2 — Das Fundament (Regeln + Constraints)

| # | Datei | Warum |
|:--|:------|:------|
| 5 | `CLAUDE.md` | VIRON OS Master-Context, Regeln, Constraints |
| 6 | `.opencode/rules/00_flow_and_session_hygiene.md` | Session-Start-Sequenz, DoD-Protokoll |
| 7 | `.opencode/rules/sub-agents.md` | 4-Pfeiler-Briefing, Report-First-Tracking |
| 8 | `.opencode/rules/file_operation_safety.md` | Edit vs Write, Anti-Kompression |

**Nach Batch 2 (5-10 Zeilen Notiz):**
- "Welche REGELN gelten für diese Session?"
- "Welche vergangenen FEHLER sind hier relevant?"
- "Gibt es WIDERSPRÜCHE zwischen alten und neuen Regeln?"

### BATCH 3 — Das Material (Arbeitsmaterial)

| # | Datei | Warum |
|:--|:------|:------|
| 9 | `DOCS/brand-voice.md` | Tone, Stil, verbotene Formulierungen |
| 10 | `DOCS/icp-summary.md` | Zielgruppe, Pain Points, Anti-ICP |
| 11 | `TASKS.md` | Aktive Tasks, Welle 4 Status |
| 12 | `STORAGE/INDEX.md` | Payload-Index, Tool-Decisions |

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
| `STORAGE/skill-creation-knowledge.md` | Wenn Skills erstellt/optimiert werden |
| `.opencode/rules/marketing_routing_stops.md` | Wenn Model-Routing entschieden werden muss |
| `.opencode/rules/marketing_batching.md` | Wenn Content in Batches produziert wird |
| `.opencode/rules/marketing_workflow_dod.md` | Wenn Definition-of-Done geprüft wird |
| `STORAGE/TOOLS/tool-decisions.md` | Wenn Tool-Evaluationen nötig |
| `DESK/REPORTS/dach-custom-skills.md` | Wenn DACH-Skills gebaut werden (dsgvo-lead-capture etc.) |

**REGEL:** DOCS-Dateien sind auto-injiziert und gehören NICHT in Tier-2. Nur STORAGE-Dateien und task-spezifische Dateien werden geladen.

---

## TIER 3 — SKIP

| Datei | Warum Skip |
|:------|:------|
| `ARCHIVE/` | Historische Skills, nicht für aktive Arbeit |
| `IMPORT/` | Importierte Referenz-Materialien, nur bei explizitem Bedarf |
| `VIRON_Full_Package_v2/` | Alte Linear-Setup-Skripte, archiviert |
| `SCRATCH/` | Temporäre Notizen, nicht persistent |
| `.git/` | Git-Metadaten |

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
