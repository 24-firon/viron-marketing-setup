> **Für den Agenten der dieses Bundle etabliert:** Infoblöcke
> 
> **Was in dieser Datei steht:**
> 
> - REINE DATENÜBERGABE — keine Fragen, keine Verifikation
> - Projekt-spezifische Daten (IPs, Configs, Endpunkte) die NIRGENDS anders stehen
> - Wird während der Session aktiv genutzt und am Ende befüllt
> - Unterschied zu P02: HANDOVER = Daten, P02 = Forensischer Report
> 
> **Ort:** Wird auf DESK/ (Arbeitstisch) abgelegt, nicht in DIRECTOR/.
> 
> GILT FÜR ALLE TEMPLATES:
> 
> - Diese Erbauer-Info-Blöcke zum Bundle etablieren werden bei Auslieferung gelöscht. Die anderen Info-Blöcke bleiben bestehen. 
> 
> - Alle verlinkten Dateien in den Templates müssen auf Existenz geprüft werden. Falls sie nicht vorhanden sind, werden sie bein OPERATOR erfragt. 

# MASTER-README — HANDOVER BUNDLE (Konsolidierte Version)

> **Stand:** 2026-06-05
> **Quellen:** Viron-agency-stack, Context-Dispatcher-System
> **Version:** Konsolidiert aus 46 Original-Dateien → 30 finale Dateien

---

## 1. WAS IST DAS?

Dieses Bundle ist die **finalisierte, konsolidierte Version** aller Session-Übergabe-Templates. Es enthält 30 kuratierte Dateien in 17 thematischen Ordnern — bereit für den Export in ein neues Repo oder für den direkten Einsatz im CDS.

**Zweck:** Ein Agent kann mit diesem Bundle:

- Eine Session korrekt **starten** (P00 → P01 → P02)
- Eine Session korrekt **durchführen** (Plan, Tasks, Handover, Sub-Agents)
- Eine Session korrekt **beenden** (P99, Ritual, Report)

**Was es NICHT ist:** Kein vollständiges SSoT-Template, keine Rules, keine Skills. Das sind die **Prompts und Templates** die ein Agent braucht um die SSoT-Mechanik zu nutzen.

---

## 2. DIE 3 MODI — Wie der Operator das Bundle nutzt

Der Operator sagt dem Agent einen von drei Modi. Folge EXAKT dem passenden Modus.

### 🔵 MODUS 1: SCHNELLER SESSIONWECHSEL (3 Dateien)

**Wenn der Operator sagt:** "Mach einen schnellen Sessionwechsel"

**Du brauchst nur diese 3 Dateien:**

- `01_P00_BOOTSTRAP/VARIANTE_A.md` — kurz durchlesen, Stress-Test bestehen
- `06_IMPLEMENTATION_PLAN/VARIANTE_A.md` — kopieren, für deine Session befüllen
- `05_HANDOVER/VARIANTE_A.md` — kopieren, mit deinen Daten befüllen

**Nicht verwenden:** P01, P02, P99, KONSERVIERUNGS_MANIFEST, SESSION_RITUAL, alle anderen Templates.

---

### 🟡 MODUS 2: NORMALER SESSIONWECHSEL (10 Dateien)

**Wenn der Operator sagt:** "Mach einen normalen Sessionwechsel"

**Du brauchst:**

| #   | Datei                                    | Zweck                                            |
|:--- |:---------------------------------------- |:------------------------------------------------ |
| 1   | `01_P00_BOOTSTRAP/VARIANTE_A.md`         | Stress-Test                                      |
| 2   | `02_P01_LESELISTE/VARIANTE_A.md`         | Leseliste (Tier 1-3)                             |
| 3   | `03_P02_SESSION_INIT/VARIANTE_A.md`      | Session Init (Comprehension Gate + Meilensteine) |
| 4   | `06_IMPLEMENTATION_PLAN/VARIANTE_A.md`   | Plan-Vorlage                                     |
| 5   | `07_CURRENT_TASKLIST/VARIANTE_A.md`      | Task-Tracker                                     |
| 6   | `05_HANDOVER/VARIANTE_A.md`              | Übergabe-Daten                                   |
| 7   | `08_WORKSPACE_WALKTHROUGH/VARIANTE_A.md` | Topology + Reading List                          |
| 8   | `09_SESSION_HANDOVER/VARIANTE_A.md`      | Forensischer Report                              |
| 9   | `10_SESSION_RITUAL/VARIANTE_A.md`        | 5-Säulen-Checkliste                              |
| 10  | `04_P99_HANDOFF/VARIANTE_A.md`           | Session-Abschluss-Workflow                       |

**Nicht verwenden:** TASK_ENVELOPE, OPERATOR_WORKFLOW, ORCHESTRATOR_WORKFLOW, TIER_MEMORY, KONSERVIERUNGS_MANIFEST.

---

### 🟢 MODUS 3: AUSFÜHRLICHER SESSIONWECHSEL (16+ Dateien)

**Wenn der Operator sagt:** "Mach einen ausführlichen Sessionwechsel"

**Du brauchst ALLES aus Modus 2 PLUS:**

| #   | Datei                                      | Zweck                                  |
|:--- |:------------------------------------------ |:-------------------------------------- |
| 11  | `11_TASK_ENVELOPE/VARIANTE_A.md`           | Sub-Agents briefen                     |
| 12  | `12_OPERATOR_WORKFLOW/VARIANTE_A.md`       | Ausführer-Modus                        |
| 13  | `13_ORCHESTRATOR_WORKFLOW/VARIANTE_A.md`   | Planer-Modus                           |
| 14  | `14_TIER_MEMORY/VARIANTE_A.md`             | Handover-Shrink                        |
| 15  | `16_KONSERVIERUNGS_MANIFEST/VARIANTE_A.md` | 4 Gesetze der Persistenz               |
| 16  | `15_COMPREHENSION_GATE/VARIANTE_A.md`      | HARD STOP zwischen Lesen und Ausführen |

**Plus Optional (Spezialfälle):**

- `17_FORK/P03_RESERVED.md` — Security Audit, Deep Research, Incident Response
- `17_FORK/HANDOVER_BUNDLE_README.md` — Diese DREI-MODI-Übersicht als Referenz

---

## 3. DATEI-ÜBERSICHT (30 Dateien in 17 Ordnern)

### PROMPTS (was der Agent LIEST um zu wissen was zu tun ist)

| Ordner                  | Datei A                                         | Datei B                                        | Modus  |
|:----------------------- |:----------------------------------------------- |:---------------------------------------------- |:------ |
| **01_P00_BOOTSTRAP**    | VARIANTE_A (Universal, 11 Fragen, 15 Rules)     | VARIANTE_B (Viron-spezifisch, 11 Fragen split) | 🔵🟡🟢 |
| **02_P01_LESELISTE**    | VARIANTE_A (3-Batch-Logik, Comprehension Gate)  | VARIANTE_B (Viron, Platzhalter)                | 🟡🟢   |
| **03_P02_SESSION_INIT** | VARIANTE_A (Universal, 5 Meilensteine, 🔴🟡🟢⚡) | VARIANTE_B (Viron, Task-Verständnis)           | 🟡🟢   |
| **04_P99_HANDOFF**      | VARIANTE_A (6-Schritte Workflow)                | VARIANTE_B (Viron, 7-Schritte)                 | 🟡🟢   |

### TEMPLATES (was der Agent KOPIERT und BEFÜLLT)

| Ordner                       | Datei A                               | Datei B                              | Modus  |
|:---------------------------- |:------------------------------------- |:------------------------------------ |:------ |
| **05_HANDOVER**              | VARIANTE_A (Reine Daten, 7 Sektionen) | VARIANTE_B (Mit P00-Verifikation)    | 🔵🟡🟢 |
| **06_IMPLEMENTATION_PLAN**   | VARIANTE_A (Universal-Template)       | VARIANTE_B (Viron V6 Instanz)        | 🔵🟡🟢 |
| **07_CURRENT_TASKLIST**      | VARIANTE_A (Universal-Template)       | VARIANTE_B (Viron V6 Instanz)        | 🟡🟢   |
| **08_WORKSPACE_WALKTHROUGH** | VARIANTE_A (Universal-Template)       | VARIANTE_B (Viron V6 Instanz)        | 🟡🟢   |
| **09_SESSION_HANDOVER**      | VARIANTE_A (Universal-Template)       | VARIANTE_B (Viron V6 Instanz)        | 🟡🟢   |
| **10_SESSION_RITUAL**        | VARIANTE_A (Universal, 5 Säulen)      | VARIANTE_B (Viron, mit Stopp)        | 🟡🟢   |
| **11_TASK_ENVELOPE**         | VARIANTE_A (Universal, 4-Säulen)      | VARIANTE_B (Viron, mit CDS-Beispiel) | 🟢     |

### WORKFLOWS & ROLLEN

| Ordner                       | Datei A                           | Datei B                       | Modus |
|:---------------------------- |:--------------------------------- |:----------------------------- |:----- |
| **12_OPERATOR_WORKFLOW**     | VARIANTE_A (Universal, Ausführer) | VARIANTE_B (Viron, Ausführer) | 🟢    |
| **13_ORCHESTRATOR_WORKFLOW** | VARIANTE_A (Universal, Planer)    | VARIANTE_B (Viron, Planer)    | 🟢    |

### SUPPORTING

| Ordner                         | Datei A                               | Datei B              | Modus |
|:------------------------------ |:------------------------------------- |:-------------------- |:----- |
| **14_TIER_MEMORY**             | VARIANTE_A (mit TEMPLATE-EXPLANATION) | VARIANTE_B (kompakt) | 🟢    |
| **15_COMPREHENSION_GATE**      | VARIANTE_A (allein)                   | —                    | 🟢    |
| **16_KONSERVIERUNGS_MANIFEST** | VARIANTE_A (allein)                   | —                    | 🟢    |

### SONDERKATEGORIEN (17_FORK)

| Datei                       | Zweck                                           |
|:--------------------------- |:----------------------------------------------- |
| `HANDOVER_BUNDLE_README.md` | 3-Modi-Übersicht (diese Doku)                   |
| `P03_RESERVED.md`           | Spezial-Sessions (Security, Research, Incident) |

### AUSGESONDERT (99_AUSGESONDERT)

14 Dateien, die im Konsolidierungsprozess aussortiert wurden. Begründung im Dateinamen (`_GRUND_ORIGINALNAME.md`).

---

## 4. REIHENFOLGE BEIM LESEN (für den Agent)

```
🔵 Modus 1 (3 Dateien):
   01_P00_BOOTSTRAP/VARIANTE_A.md
   → 06_IMPLEMENTATION_PLAN/VARIANTE_A.md
   → 05_HANDOVER/VARIANTE_A.md

🟡 Modus 2 (10 Dateien):
   01_P00_BOOTSTRAP/VARIANTE_A.md
   → 02_P01_LESELISTE/VARIANTE_A.md
   → 15_COMPREHENSION_GATE/VARIANTE_A.md (nach Lesen)
   → 03_P02_SESSION_INIT/VARIANTE_A.md
   → [arbeite]
   → 09_SESSION_HANDOVER/VARIANTE_A.md (am Ende)
   → 10_SESSION_RITUAL/VARIANTE_A.md
   → 04_P99_HANDOFF/VARIANTE_A.md

🟢 Modus 3 (16+ Dateien):
   Modus 2 + zusätzlich:
   → 11_TASK_ENVELOPE/VARIANTE_A.md (wenn Sub-Agents)
   → 12_OPERATOR_WORKFLOW/VARIANTE_A.md (als Operator)
   → 13_ORCHESTRATOR_WORKFLOW/VARIANTE_A.md (als Planer)
   → 14_TIER_MEMORY/VARIANTE_A.md (wenn Shink nötig)
   → 16_KONSERVIERUNGS_MANIFEST/VARIANTE_A.md (IMMER gültig)
```

---

## 5. WICHTIGE REGELN — Die 4 Gesetze der Persistenz

Diese 4 Gesetze sind IMMER gültig — in allen 3 Modi:

| #   | Gesetz              | Was es bedeutet                                                     |
|:--- |:------------------- |:------------------------------------------------------------------- |
| 1   | **KEINE LÖSCHUNG**  | Archivieren, nicht löschen. Konservierungs-Manifest.                |
| 2   | **KEINE REDUKTION** | Berichte und Handovers sind vollständig. Keine `//...`-Abkürzungen. |
| 3   | **BEWEISPFLICHT**   | Jede Aussage hat einen Beweis. Reports unter `DESK/reports/`.       |
| 4   | **INTEGRATION**     | Korrekturen an die richtige Stelle, nicht ans Ende appended.        |

**Quelle:** `16_KONSERVIERUNGS_MANIFEST/VARIANTE_A.md`

---

## 6. WANN GELTEN DIE VARIANTEN B vs. A?

In den meisten Kategorien gibt es eine **Master-Variante (A)** und eine **Alternative (B)**.

**VARIANTE_A = Master:**

- Universell, export-fähig
- Modell-Routing mit 🔴🟡🟢⚡ wo anwendbar
- TEMPLATE-EXPLANATION-Blöcke (Meta-Doku für den Bundle-Etablierer)
- Bestes Format für ein NEUES Repo

**VARIANTE_B = Alternative:**

- Viron-spezifisch (falls vorhanden)
- Kompakter/kürzer (falls vorhanden)
- Mit konkretem Beispiel (z.B. CDS-REGISTRY_SYNC)
- Anders formuliert aber gleichwertig

**Wann welche nutzen?**

- **Neues Repo, sauberer Start:** VARIANTE_A
- **Bestehender Viron-Stack:** VARIANTE_B
- **Lernen durch Beispiel:** VARIANTE_B (hat das konkrete CDS-Beispiel)

---

## 7. BEI MODUS-WAHL UNSICHER?

Frag den Operator:

> "Brauchst du einen kurzen Switch, einen Standard-Switch oder den vollen Forensic-Switch?"

Antwort → entsprechenden Modus wählen. Nicht raten.

---

## 8. MODELL-ROUTING REFERENZ

| Tag           | Modell            | Einsatz                   |
|:------------- |:----------------- |:------------------------- |
| `🔴 STARK`    | Starkes Reasoning | P00, Planung, Forensik    |
| `🟡 MITTEL`   | Mittleres Modell  | Reviews, Skill-Erstellung |
| `🟢 STANDARD` | Standard-Modell   | Code, Tests, Bash         |
| `⚡ LIGHT`     | Leichtgewichtig   | Lesen, Grep, Status       |

**🛑 HARD STOP** bei jedem Modell-Wechsel. Warte auf "GO" vom Operator.

---

## 9. SESSION-LEBENSZYKLUS

```
[AGENT liest Master-README, Operator wählt Modus]
     ↓
[AGENT liest P00] → Stress-Test bestehen
     ↓
[AGENT liest P01 + Tier-1 Dateien]
     ↓
[Comprehension Gate] → HARD STOP bis bestanden
     ↓
[AGENT liest P02] → Plan erstellen
     ↓
[AGENT arbeitet (M1-M5)]
     ↓
[AGENT nutzt P99] → Session-Abschluss
     ↓
[AGENT liefert ab: HANDOVER.md, PLAN, TASKLIST, WALKTHROUGH]
     ↓
[OPERATOR übergibt diese Dateien an nächsten Agent]
```

---

## 10. VERSIONS-HINWEIS

- **Konsolidiert am:** 2026-06-05
- **Quellen:** Viron-agency-stack (Original), Context-Dispatcher-System (Instanz)
- **Konsolidierungs-Pass:** 2 (MOVE-PASS → 46 Dateien, KONSOLIDIERUNGS-PASS → 30 finale Dateien)
- **Exportierbar:** Ja, alle Dateien sind Repo-agnostisch (außer VARIANTE_B mit Viron-Bezug)
- **Vorgänger:** `TEMP_HANDOVER_MERGE/01-17` (sortierte Originale), `TEMP_HANDOVER_MERGE/_AUSGESONDERT` (9 Duplikate)
