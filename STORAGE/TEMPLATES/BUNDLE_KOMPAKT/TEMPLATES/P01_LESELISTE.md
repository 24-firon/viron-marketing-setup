# P01 — Leseliste (Kompakt)

> **LESE-MODUS.** Lade alle Tier-1-Dateien physisch und mach dir pro Datei eine 3-5 Zeilen Notiz. **DENN** der nächste Schritt (P02) verlangt nachweisbares Verständnis.

## VOR DEM START

Bestätige Comprehension Gate 1:
> "Ich habe die P00-Antworten verinnerlicht. Ich beginne jetzt mit dem Lesen."

## TIER 1 — PFLECHT (3 Batches)

### BATCH 1: Das Herzstück
- [ ] `AGENTS.md` oder `README.md` — Repo-Identität, Zonen, Verfassung
- [ ] `RULE_REGISTRY.md` oder `.opencode/rules/` Index — Welche Regeln existieren
- [ ] Aktiver Task-Envelope (`DESK/TASKS/active/task.md`) — Scope, DoD, Blocker

**Notiz (5 Zeilen):** Was ist die Mission? Was blockiert? Was sind die 3 Kern-Constraints?

### BATCH 2: Das Fundament
- [ ] `LESSONS_LEARNED.md` — bekannte Fehler die nicht wiederholt werden
- [ ] `DECISION_LOG.md` — vergangene Architektur-Entscheidungen
- [ ] Letzte `HANDOVER.md` — Status der vorherigen Session (falls vorhanden)

**Notiz (5 Zeilen):** Welche Fehler sind hier relevant? Welche Entscheidungen sind getroffen? Wo ist der Stand?

### BATCH 3: Das Material
- [ ] `implementation_plan.md` — der Bauplan
- [ ] `tasklist.md` oder `CURRENT_TASKLIST.md` — die aktuelle Task-Liste
- [ ] Domain-spezifische SSoT (z.B. `ARCHITECTURE.md`, `STYLE_GUIDE.md`)

**Notiz (5 Zeilen):** Was ist der IST-Zustand? Was ist das SOLL? Welche Dateien sind betroffen?

## TIER 2 — BEI BEDARF

| Datei | Wann lesen |
|:---|:---|
| `STORAGE/[topic].md` | Wenn spezifisches Wissen gebraucht |
| `IMPORT/[topic].md` | Wenn externes Wissen aus anderen Repos relevant |
| `docs/[feature]/...` | Wenn Feature-spezifische Doku gebraucht |

## WAS DU NICHT LIEST (SKIP)

- `node_modules/`, `.next/`, `dist/`, `build/` — Build-Artefakte
- `.git/` — Git-Metadaten
- `_ARCHIVE/` — Historisch
- `DELIVERY/` — Bundles, nicht für internes Verständnis

## BESTÄTIGUNG

> "P01 gelesen. [X]/[X] Dateien. 3 Notizen erstellt. Bereit für P02."

⏸️ **STOPP** — Nächstes Modell: 🔴 STARK.
