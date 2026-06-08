# LESSON — Template-Mismatch & Path-Konventionen (2026-06-07)

> **Status:** Immutable (No-Touch nach Erstellung). Spätere Änderungen nur als neue Datei mit Datum.
>
> **Zweck:** Dokumentiert (a) den Template-Mismatch-Vorfall in P01_LESELISTE.md, (b) die Lesson daraus, (c) die echten Path-Konventionen dieses Repos. Verhindert zukünftige Phantom-Pfade in HANDOVERs, Reports und SubAgent-Prompts.

---

## 1. VORFALL

P01_LESELISTE.md (Template aus Viron-agency-stack, 93Z-Architektur) enthielt **12 Fake-Paths** in TIER 1, 2 und 3. Keiner davon existierte in diesem Repo:

**TIER 1 (7 Fake-Paths):**
- `REPO_BRIEFING.md` ❌
- `RULE_ROUTER.md` ❌
- `DESK/TASKS/active/task.md` ❌
- `REPORTS/SRC-ANALYSE.md` ❌
- `REPORTS/UNINDEXED_FILES_REPORT.md` ❌
- `DELIVERY/Context_Dispatcher_V6_Init/SESSION_HANDOVER.md` ❌
- `REPORTS/DETOX_EXECUTION_LOG.md` ❌

**TIER 2 (4 Fake-Paths):**
- `IMPORT/System/welle3_boot_sequenz.csv` ❌
- `dispatcher/README_DISPATCHER.md` ❌
- `IMPORT/sub-agent-prompting.md` ❌
- `IMPORT/Brain_Surgeon_System.md` ❌

**TIER 3 (2 Fake-Paths):**
- `DELIVERY/` (Top-Level) ❌
- `_ARCHIVE/` (Top-Level) ❌
- `node_modules/` (Top-Level) ❌ (existiert in `.gitignore` aber nicht als Top-Level-Dir)

**Konsequenz:** Wer die Leseliste abgearbeitet hätte, wäre auf 12 tote Links gestoßen. User-Reaktion: "Bist du irgendwie so ein bisschen dumm oder so?"

---

## 2. LESSON: GLOB-FIRST BEI TEMPLATE-COPY

**Vor** dem Verwenden eines Templates (besonders wenn aus einem anderen Repo/Projekt übernommen):

1. **Glob die behaupteten Pfade** — z.B.:
   ```bash
   glob REPO_BRIEFING.md
   glob DESK/TASKS/active/task.md
   ```

2. **Bei 0 Treffern:** Pfad ist fake. Entweder:
   - **Adapting-Modus** (bevorzugt für produktive Templates): Ersetze durch echte Pfade aus dem aktuellen Repo
   - **Strip-Modus** (für unbenutzte Templates): Pfad komplett rausnehmen

3. **Grep am Ende** — sicherheitscheck:
   ```bash
   grep "REPO_BRIEFING|RULE_ROUTER|DESK/TASKS/active|REPORTS/SRC-ANALYSE|UNINDEXED_FILES|Context_Dispatcher_V6|REPORTS/DETOX" -r --include "*.md"
   ```

---

## 3. ECHTE PATH-KONVENTIONEN DIESES REPOS

### 3.1 Top-Level-Verzeichnisse (echt)

```
.agent/      .agents/      .claude/      .graphify/      .opencode/      .planning/
ARCHIVE/     DESK/         DIRECTOR/     DOCS/           HANDOVER/       IMPORT/
PLAYGROUND/  SCRATCH/      scripts/      STORAGE/        VIRON_Full_Package_v2/
```

### 3.2 Was NICHT existiert (häufige Verwechslungen)

| Behauptet | Realität |
|:----------|:---------|
| `Work-Lab/Content/_wip/` | **`STORAGE/CONTENT/_wip/`** (echt) |
| `Content/` (Top-Level) | existiert NICHT — echter Pfad: `STORAGE/CONTENT/` |
| `_ARCHIVE/` | **`ARCHIVE/`** (ohne Underscore) |
| `DELIVERY/` | existiert NICHT |
| `dispatcher/` | existiert NICHT |
| `node_modules/` (Top-Level) | existiert NICHT — nur in `.gitignore` und `package-lock.json` referenziert |

### 3.3 Wichtige Sub-Pfade

| Pfad | Inhalt |
|:-----|:-------|
| `.agents/skills/` | **14 aktive Skills** (v2.0.1) — `competitor-profiling`, `content-strategy`, `copy-editing`, `copywriting`, `cro`, `customer-research`, `directory-submissions`, `image`, `launch`, `marketing-psychology`, `pricing`, `product-marketing`, `social`, `video` |
| `ARCHIVE/skills/` | 19 inaktive Skills |
| `DESK/HANDOVER/sessions/` | Session-Handover (Format: `session-YYYY-MM-DD.md`) |
| `DESK/HANDOVER/ORCHESTRATION_SYSTEM.md` | Orchestrierungs-Playbook (Welle-3-Stand) |
| `DESK/HANDOVER/lessons/` | **Dieses Verzeichnis** — No-Touch-Insights |
| `DESK/HANDOVER/research/` | Research-Material (Welle 1-3) |
| `DESK/REPORTS/` | SubAgent-Reports + Tool-Decisions |
| `DESK/TASKS/dach-p0-skills/` | DACH-Skill-Envelopes (laufend) |
| `DOCS/` | Auto-injizierte Foundation (5 Dateien) |
| `HANDOVER/P01_LESELISTE.md` | Adaptierte Leseliste für dieses Repo |
| `STORAGE/TOOLS/tool-decisions.md` | Tool-Evaluationen (Metricool, Cal.com, Exa) |
| `STORAGE/CONTENT/_wip/` | **Echter WIP-Ordner** (NICHT `Work-Lab/Content/`) |
| `STORAGE/TEMPLATES/HANDOVER_BUNDLE/` | Master-Templates für HANDOVER-Erstellung |
| `DIRECTOR/PROMPTS/TEMPLATES/` | Master-Templates für P00-P03 Prompts |

### 3.4 Token-Mapping für MCPs (in `opencode.jsonc`)

```
Notion:  NOTION_TOKEN        ← {env:VIRON-OpenCode-ReadOnly}    (read-only)
Linear:  LINEAR_API_TOKEN    ← {env:LINEAR_API_KEY}              (read+write)
```

---

## 4. ANTI-PATTERN: PHANTOM-PFADE IN HANDOVERS

**Symptom:** SubAgent oder HANDOVER referenziert Dateien die nicht existieren.

**Ursache:** Copy-Paste aus Templates ohne Path-Validierung.

**Detection (vor Commit):**
```bash
# In der HANDOVER-Datei
grep -E "\.(md|json|ps1|sh)$" HANDOVER/HANDOVER.md

# Glob jedes Vorkommen
glob "pfad-aus-handover.md"
```

**Fix:**
1. Glob liefert 0 Treffer → Pfad ist fake
2. Ersetze durch echten Pfad oder entferne Referenz
3. Bei Template-Anpassung: Master-Template in `STORAGE/TEMPLATES/` ebenfalls fixen

---

## 5. FOLLOW-UPS

- [ ] Bei jedem Template-Copy zukünftig: glob-First-Check
- [ ] Master-Templates in `STORAGE/TEMPLATES/HANDOVER_BUNDLE/` und `DIRECTOR/PROMPTS/TEMPLATES/` regelmäßig auditieren
- [ ] Wenn neue Top-Level-Dirs hinzukommen: diese Datei aktualisieren ODER neue Datei `2026-XX-XX-paths-v2.md` anlegen

---

> **Erstellt:** 2026-06-07 | **No-Touch:** ab Erstellung
