<!-- TEMPLATE-EXPLANATION-START -->
> **Für den Agenten der dieses Bundle etabliert:**
>
> **Was in dieser Datei steht:**
> - REINE DATENÜBERGABE — keine Fragen, keine Verifikation
> - Projekt-spezifische Daten (IPs, Configs, Endpunkte) die NIRGENDS anders stehen
> - Wird während der Session aktiv genutzt und am Ende befüllt
> - Unterschied zu P02: HANDOVER = Daten, P02 = Forensischer Report
>
> **Ort:** Wird auf DESK/ (Arbeitstisch) abgelegt, nicht in DIRECTOR/.
>
> **Adaptiert aus:** Viron-agency-stack HANDOVER.md (93Z)
<!-- TEMPLATE-EXPLANATION-END -->

# HANDOVER — DATENÜBERGABE (Master-Variante)

> **Was ist das?** Eine Knowledge-Datei (temporär) die projektspezifische Daten für die nächste Session enthält. Wird während der Session aktiv genutzt und am Ende befüllt.
>
> **Zweck:** Diese Datei enthält projekt- und task-spezifische Daten die nirgendwo anders stehen. IP-Adressen, Konfigurationen, Workarounds, bekannte Bugs. Reine Informationsweitergabe — keine Fragen, keine Verifikation.
>
> **Wann nutzen:** Während der Session nachschauen, am Session-Ende ausfüllen, dem nächsten Agenten übergeben.

---

## 1. BLUF (Bottom Line Up Front)

> **Diese Session (jetzt):** Linear + Notion MCPs in OpenCode live geschaltet, ENV-Loader gebaut, AGENTS.md-Doku aktualisiert. MCPs verifiziert: beide `✓ connected`.
>
> **Nächste Session (2 Stunden, frischer Context):** 2 Marketing-Skills bauen via SubAgent-Orchestrierung — `brand-voice-guardian` + `brief-to-campaign`. Provider-Mix: NVIDIA NIM / OpenCode Go / OpenCode ZEN. Pro SubAgent ein Copy-Paste-Prompt mit Mission, Scope, Constraints, Steps, Report-Pfad.
>
> **Wichtig — kein Anthropic:** Provider sind ausschließlich NVIDIA NIM, OpenCode Go, OpenCode ZEN. Keine Erwähnung von Opus/Haiku/Sonnet in SubAgent-Prompts.

---

## 2. PROJEKT-SPEZIFISCHE DATEN

Diese Informationen stehen nirgendwo anders. Sie müssen dem nächsten Agenten explizit mitgegeben werden.

| Schlüssel | Wert | Beschreibung |
|:----------|:-----|:-------------|
| **MCP-Status** | `notionApi` ✓ + `linear` ✓ connected | `opencode mcp list` muss beide als connected zeigen BEVOR Task startet |
| **Token-Quelle** | `.env.local` (nicht in Git, mit Bindestrich-Escapes) | NIEMALS direkt in `opencode.jsonc` hardcoden — immer `{env:...}` |
| **OpenCode-Startbefehl** | `pwsh -NoProfile -File scripts/start-opencode.ps1` | Lädt ENV automatisch, dann TUI. Manuell: `. .\scripts\load-env.ps1; opencode` |
| **Notion-Policy** | **READ-ONLY** (enforced via Integration-Capability "Read content") | Notion-MCP-Token in `.env.local` heißt `VIRON-OpenCode-ReadOnly` (nicht `NOTION_API_KEY`) |
| **Linear-Policy** | Voller Zugriff (read+write) | Token in `.env.local` heißt `LINEAR_API_KEY`. Schreibrechte gewollt — Issue-Erstellung nötig |
| **Skills-Pfad** | `.agents/skills/` (aktiv) — NICHT `ARCHIVE/skills/` | Neue Skills IMMER in `.agents/skills/<name>/SKILL.md` |
| **3-Zonen-Modell** | Brain → `_wip/` → Final | SubAgents schreiben NUR in `STORAGE/CONTENT/_wip/`. Final erst nach Operator-Approval |
| **ENV-Var-Mapping MCP** | Notion: `NOTION_TOKEN` ← `{env:VIRON-OpenCode-ReadOnly}`; Linear: `LINEAR_API_TOKEN` ← `{env:LINEAR_API_KEY}` | Mapping passiert in `opencode.jsonc` `mcp.<server>.environment` |
| **MCP-timeout** | 60000ms | 10s reicht nicht für ersten npx-Download der Pakete |
| **Aktiver Content-Strang** | Welle 4 (Hustle Marketing) | Siehe `TASKS.md` § Welle 4. Echtes Material: Fake-Agency Takedown, AI-Act Reels |
| **Aktiver Meilenstein** | M2 P0-DACH-Skills (in Bau) | `dsgvo-lead-capture`, `linkedin-dach-b2b`, `local-seo-gbp` — laufen parallel, nicht Teil dieser Session |

---

## 3. ABGESCHLOSSENE ARBEIT

| Was | Status | Beschreibung |
|:----|:------:|:-------------|
| `opencode.jsonc` um MCP-Block erweitert | ✅ | `mcp.notionApi` (@notionhq/notion-mcp-server v2.2.1, local, NOTION_TOKEN) + `mcp.linear` (@tacticlaunch/mcp-linear, local, LINEAR_API_TOKEN) |
| `scripts/load-env.ps1` neu | ✅ | Lädt `.env.local` in Process-Scope mit Shell-Unescape (`\_` → `_`) |
| `scripts/start-opencode.ps1` neu | ✅ | Wrapper: lädt ENV, startet TUI |
| `AGENTS.md` Start-Sektion ergänzt | ✅ | Sektion 0: OpenCode TUI starten + MCP-Status-Prüfung |
| `.env.local` unescape-Fix | ✅ | Token-Werte haben Shell-Escapes (`lin\_api\_...`); Loader strippt Backslashes, sonst JSONC-Parse-Fehler |
| MCPs verifiziert | ✅ | `opencode mcp list` zeigt beide `✓ connected` |

---

## 4. ENTSCHEIDUNGEN

| Entscheidung | Begründung | Reversibel? |
|:-------------|:-----------|:------------:|
| Linear-MCP: `@tacticlaunch/mcp-linear` | Modernste Option (v1.1.2, MCP-native resources+prompts, 27k weekly downloads). Konkurrenten: `@mseep` (älter), `linear-mcp` by dvcrn (basic) | Ja — 1-Zeilen-Wechsel in `opencode.jsonc` |
| Notion-MCP: `@notionhq/notion-mcp-server` v2.2.1 (lokal) | Offiziell, 68k weekly downloads, Notion-Version 2025-09-03 mit Data-Source-API. Remote-MCP würde OAuth brauchen, Overkill für jetzt | Ja — `type: "remote"` + OAuth-URL |
| Notion READ-ONLY-Token verwenden | CLAUDE.md §3 + User-Präferenz: Templates nicht überschreiben lassen | Nein — bewusste Policy |
| Timeout auf 60s (nicht 10s default) | Erster `npx -y`-Download von @notionhq/notion-mcp-server braucht >10s | Ja |
| Token via `{env:...}` in opencode.jsonc, NICHT inline | Sicherheit: keine Klartext-Tokens in Git-tracked Config | Nein — Best Practice |
| SubAgent-Modelle: OpenCode Go (Research/Evals) + OpenCode ZEN (Writing) | Per `marketing_routing_stops.md` adaptiert: Research → Go, Copy → ZEN, Strategie → ZEN (nur Orchestrator). KEIN Anthropic | Ja — pro SubAgent-Prompt überschreibbar |
| `.env.local` parsen mit PowerShell-Regex + Unescape | `.env.local` hat bash-style `KEY="value"` Format mit `\_`-Escapes. Python `dotenv` würde dasselbe tun | Ja — bei Bedarf auf `python-dotenv` migrieren |

---

## 5. OFFENE TASKS (für die 1-Stunden-Session)

| Task | Priorität | Status | Beschreibung |
|:-----|:---------:|:------|:-------------|
| **Skill: `brand-voice-guardian`** | P0 | OFFEN | Custom Skill in `.agents/skills/brand-voice-guardian/`. Prüft Content-Drafts gegen DOCS/brand-voice.md + DOCS/icp-summary.md (F1/F2 Foundation Blocks in Notion, read-only). Output: Score (1-10) + 3-5 konkrete Fix-Vorschläge |
| **Skill: `brief-to-campaign`** | P0 | OFFEN | Custom Skill in `.agents/skills/brief-to-campaign/`. Nimmt Notion-Brief oder Operator-Text → erstellt 4-6 strukturierte Linear-Issues (MKT/SAL/FUL) mit allen Properties (Priority, Labels, Estimate, F-Block-Ref, Acceptance Criteria) |
| **Integration-Test auf Welle-4-Material** | P1 | OFFEN | **Combo-Material (G-5 + G-4):** G-5 AI-Act Lead-Magnet "Ist euer US-Lead-Scoring ab August illegal?" als zentraler Brief, G-4 5 LinkedIn-Takedown-Posts gegen GPT-Bastler-Agenturen als Distribution-Layer. brand-voice-guardian scored alle 5 G-4-Posts, brief-to-campaign expandiert G-5 zu ~10 Linear-Issues (1 Pillar + 5 LinkedIn + 3 Reels + 1 Lead-Magnet). Beste Test-Abdeckung pro Zeit. |
| **Commit + SKILL_INDEX Update** | P1 | OFFEN | Beide Skills in `DOCS/SKILL_INDEX.md` mit Scan-Depth eintragen. Commit mit Message nach Repo-Convention |

---

## 6. BEKANNTE PROBLEME & WORKAROUNDS

| Problem | Workaround | Fix geplant? |
|:--------|:-----------|:------------:|
| PowerShell kann Bindestriche in env-Var-Namen nicht ohne `${}` parsen (`$env:VIRON-Foo` wird als `$env:VIRON` minus `Foo` gelesen) | Immer Scripts/Loader nutzen, nie inline `bash`-One-Liner mit `-` in env-Var-Namen | Nein — Script-Pattern ist sauberer |
| `.env.local`-Werte haben Shell-Escapes (`lin\_api\_...`) | Loader-Script macht `Regex.Replace(raw, '\\(.)', m => m.Groups[1].Value)` | Nein — Loader ist die Single Source of Truth |
| `opencode mcp list` zeigt beim ersten Start "Operation timed out after 10000ms" | Timeout in `opencode.jsonc` auf 60000 erhöht | Nein — npx-Download braucht Zeit |
| SubAgent-Prompts ohne Report-Anweisung führen zu Phantom-Arbeit (Lesson af4f17a, 2026-02-18) | JEDER SubAgent-Prompt MUSS enthalten: "Du bist FORBIDDEN von step N+1 bevor step N als ✅ DONE im Report-File markiert ist" | Nein — Pattern ist gelernt |
| OpenCode `bash`-Tool erlaubt `cd` nicht direkt im Inline-Befehl | `workdir`-Parameter am `bash`-Tool nutzen, nicht `cd` im Befehl | Nein — Workdir ist Best Practice |
| Linear-MCP-Backend unterstützt keine Notion-Data-Source-Schema-Migration | Bei v2→v3 Breaking Changes: Tool-Liste re-discoveren, alte Tool-Names meiden | Bei v3-Release, nicht jetzt |
| Notion-Integration teilt nur Pages die explizit connected wurden | Operator muss in Notion-UI pro Page "Connect to integration" machen | Einmalig, danach statisch |

---

## 7. NÄCHSTE SCHRITTE — SubAgent-Orchestrierungs-Plan (2 Stunden, 6 Milestones)

> **Operator-Aktion VOR Session-Start:** OpenCode TUI starten via `pwsh -NoProfile -File scripts/start-opencode.ps1`. Provider-Auswahl pro SubAgent im Header (siehe §8). Starkes Model für Orchestrator, OpenCode Go für Standardtasks, OpenCode ZEN für Schreib-Tasks.

### Zeit-Budget (2h = 120 min)

| Phase | Dauer | Inhalt |
|:------|:------|:-------|
| M0 Setup + Verify | 10 min | ENV laden, MCP-verify, Model-Confirm, Report-File anlegen |
| M1 Spec 1 | 15 min | SA-1: brand-voice-guardian Spec |
| M2 Build 1 | 25 min | SA-2 (ZEN) + SA-3 (Go) parallel |
| M3 Spec 2 | 15 min | SA-4: brief-to-campaign Spec |
| M4 Build 2 | 25 min | SA-5 (ZEN) + SA-6 (Go) parallel |
| M5 Integration | 10 min | SA-7: Live-Test auf Welle-4 Material (G-5 + G-4 Combo) |
| M6 Close | 5 min | Commit + SKILL_INDEX + HANDOVER-close |
| Operator-Gates | 14 min | 4 Approval-Stops (à 3-4 min) nach M1, M2, M4, M5 |
| **Total** | **119 min** | **+1 min Puffer** |

### Report-File-Skeleton (zu Beginn anlegen)

`DESK/REPORTS/option-bc-build.md` mit initialer Tabelle (alle ⏳ PENDING). Jeder SubAgent MUSS nach jedem seiner internen Steps die entsprechende Zeile auf ✅ DONE setzen. Hard Condition (sub-agents.md §6).

Initial-Tabelle:
```markdown
| SubAgent | Task | Status |
|:---------|:-----|:------:|
| SA-1 | brand-voice-guardian Spec | ⏳ PENDING |
| SA-2 | brand-voice-guardian SKILL.md | ⏳ PENDING |
| SA-3 | brand-voice-guardian Evals | ⏳ PENDING |
| SA-4 | brief-to-campaign Spec | ⏳ PENDING |
| SA-5 | brief-to-campaign SKILL.md | ⏳ PENDING |
| SA-6 | brief-to-campaign Evals | ⏳ PENDING |
| SA-7 | Integration Test | ⏳ PENDING |
```

---

### Copy-Paste SubAgent-Prompts

> **Anwendung:** Jeder Block unten ist ein vollständiger SubAgent-Prompt. Kopiere in ein neues Task-/SubAgent-Tool, ersetze `<PLATZHALTER>`, ergänze Model-Header, schicke ab.

#### SA-1 — Brand-Voice-Guardian Spec

**Model-Header:** `model: opencode-go` (oder `nim-small` als Alternative)

```
MISSION: Spezifikation für einen Quality-Gate-Skill, der Content-Drafts gegen VIRON-Brand-Voice prüft (Score 1-10 + konkrete Fixes).

CONTEXT-INJECTION:
- Du bist Brand-Voice-Auditor für VIRON (DACH KI-Automatisierungsagentur, KMU-Fokus, 5-50 MA).
- Voice: direkt, deutsch, kein Buzzword, kurze Sätze, konkrete Zahlen. Siehe DOCS/brand-voice.md.
- ICP: Geschäftsführer 35-55, pragmatisch, skeptisch. Siehe DOCS/icp-summary.md.

SCOPE:
- LESEN: DOCS/brand-voice.md, DOCS/icp-summary.md, .agents/product-marketing.md
- SCHREIBEN: NUR DESK/REPORTS/brand-voice-guardian-spec.md UND DESK/REPORTS/option-bc-build.md (Status-Update)
- VERBOTEN: Schreiben in .agents/skills/, STORAGE/, ARCHIVE/

GOAL: Markdown-Spec mit 5 Check-Kategorien (Tone, Vocabulary, ICP-Fit, Hook, Format/Länge), Forbidden-Phrasen-Liste verbatim aus brand-voice.md, Scorecard-Template (Markdown-Tabelle), 3 Beispiel-Scorecards (1 OK, 1 mit Fixes, 1 Reject).

CONSTRAINTS:
- FORBIDDEN: TodoWrite, scope-violation, Model-Wechsel
- Keine "Annahme" — wenn Info fehlt, in Spec explizit als "TODO: Operator-Input" markieren
- Score-Kategorien MÜSSEN aus brand-voice.md ableitbar sein, nicht erfunden
- KEIN Anthropic-Modell (Opus/Haiku/Sonnet) — nutze OpenCode Go oder vergleichbar

STEPS (atomic, sequentiell):
1. Lese alle 3 Input-Files (read-Tool, 1 Aufruf pro File)
2. Update DESK/REPORTS/option-bc-build.md Zeile SA-1 auf ⏳ IN PROGRESS
3. Identifiziere 5 Check-Kategorien aus brand-voice.md (Tone, Vocabulary, ICP-Fit, Hook, Format/Länge)
4. Extrahiere Forbidden-Phrasen-Liste verbatim aus brand-voice.md
5. Entwirf Scorecard-Template (Markdown-Tabelle mit Spalten: Kategorie, Score 1-10, Beispiel, Fix)
6. Erstelle 3 Beispiel-Scorecards anhand von (a) gutem Sample aus .agents/product-marketing.md, (b) erfundenem Bad-Sample, (c) Grenzfall
7. Update Report auf ✅ DONE
8. Output-File schreiben

INPUT-FILES:
- C:\Workspace\Repos\Marketing-Setup\DOCS\brand-voice.md
- C:\Workspace\Repos\Marketing-Setup\DOCS\icp-summary.md
- C:\Workspace\Repos\Marketing-Setup\.agents\product-marketing.md

OUTPUT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\brand-voice-guardian-spec.md

REPORT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\option-bc-build.md
```

**Operator-Gate nach SA-1:** Spec reviewen, GO für M2 geben.

---

#### SA-2 — Brand-Voice-Guardian SKILL.md

**Model-Header:** `model: opencode-zen` (oder `nim-large` als Alternative)

```
MISSION: Production-Ready SKILL.md für brand-voice-guardian bauen, das 4-Pfeiler-Formel von 80_skill_construction_law.md erfüllt.

CONTEXT-INJECTION:
- Du bist Skill-Architekt. Befolge 80_skill_construction_law.md (4-Pfeiler-Formel: Examples, Templates, Rollenzuweisung, Harte Ansagen).
- Nutze 80_anatomy_of_complex_skill.md für Struktur (SKILL.md als Router, examples/ separat).
- Befolge 71_skill_routing.md §2 (Viron-Overrides: shadcn/tailwind/framer-motion nicht relevant, aber Conflict-Resolution-Pattern anwenden).

SCOPE:
- LESEN: DESK/REPORTS/brand-voice-guardian-spec.md (SA-1 Output), DOCS/brand-voice.md, .opencode/rules/80_skill_construction_law.md, .opencode/rules/80_anatomy_of_complex_skill.md, .agents/skills/copy-editing/SKILL.md (Pattern-Referenz)
- SCHREIBEN: NUR .agents/skills/brand-voice-guardian/SKILL.md UND ~/.config/opencode/skills/brand-voice-guardian/SKILL.md (Mirror-Pflicht), UND DESK/REPORTS/option-bc-build.md
- VERBOTEN: Schreiben in DOCS/, STORAGE/, ARCHIVE/, examples/, evals/

GOAL: SKILL.md ≤ 250 Zeilen mit YAML-Header (name, description), Context-Block (Match-Check), Bedingungs-Matrix (5 Check-Phasen → Lade X), klare Workflow-Steps, Verweis auf SA-3-Evals.

CONSTRAINTS:
- FORBIDDEN: TodoWrite, scope-violation, Model-Wechsel
- YAML-Header: NUR name + description (kein first_read, kein read_lines, kein toC_line)
- 4-Pfeiler-Formel MUSS erfüllt sein: Examples-Ordner anlegen (auch wenn leer mit TODO-Markierung), Templates-Verweis, Rollenzuweisung im Context-Block, Harte Ansagen
- KEIN Anthropic-Modell

STEPS (atomic, sequentiell):
1. Lese SA-1 Spec, brand-voice.md, 80_skill_construction_law.md, copy-editing/SKILL.md (Pattern-Referenz)
2. Update Report auf ⏳ IN PROGRESS
3. Lege Verzeichnis an: .agents/skills/brand-voice-guardian/ UND ~/.config/opencode/skills/brand-voice-guardian/
4. Schreibe SKILL.md (YAML-Header + Context-Block + Bedingungs-Matrix + Workflow-Steps)
5. Lege examples/.gitkeep mit TODO-Markierung an (SA-3 füllt später)
6. Mirror nach ~/.config/opencode/skills/brand-voice-guardian/SKILL.md
7. Update Report auf ✅ DONE

INPUT-FILES:
- C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\brand-voice-guardian-spec.md
- C:\Workspace\Repos\Marketing-Setup\DOCS\brand-voice.md
- C:\Workspace\Repos\Marketing-Setup\.opencode\rules\80_skill_construction_law.md
- C:\Workspace\Repos\Marketing-Setup\.opencode\rules\80_anatomy_of_complex_skill.md
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\copy-editing\SKILL.md

OUTPUT-FILE: C:\Workspace\Repos\Marketing-Setup\.agents\skills\brand-voice-guardian\SKILL.md (Mirror: C:\Users\bachl\.config\opencode\skills\brand-voice-guardian\SKILL.md)

REPORT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\option-bc-build.md
```

---

#### SA-3 — Brand-Voice-Guardian Evals

**Model-Header:** `model: opencode-go`

```
MISSION: 6 Eval-Testfälle für brand-voice-guardian als evals/evals.json erstellen.

CONTEXT-INJECTION:
- Du bist Eval-Designer. Evals testen ob ein Skill korrekte Scorecards liefert.
- Format: JSON-Array mit Objekten {id, input, expected_score_range, expected_categories_flagged, notes}.

SCOPE:
- LESEN: DESK/REPORTS/brand-voice-guardian-spec.md, .agents/skills/brand-voice-guardian/SKILL.md (SA-2 Output), DOCS/brand-voice.md
- SCHREIBEN: NUR .agents/skills/brand-voice-guardian/evals/evals.json UND DESK/REPORTS/option-bc-build.md
- VERBOTEN: Andere Dateien

GOAL: 6 Testfälle: 2 OK (Score 8-10, keine Major-Fixes), 2 mit Fixes (Score 5-7, 2-4 konkrete Fixes), 2 Reject (Score 1-4, fundamentale Voice-Verletzung).

CONSTRAINTS:
- FORBIDDEN: TodoWrite, scope-violation
- Testfälle MÜSSEN realistische DACH-Marketing-Texte sein (LinkedIn-Posts, Lead-Magnet-Auszüge, Pillar-Snippets)
- Expected-Felder aus SA-1-Spec ableitbar, nicht erfunden
- KEIN Anthropic-Modell

STEPS:
1. Lese SA-1 Spec, SA-2 SKILL.md
2. Update Report auf ⏳ IN PROGRESS
3. Entwirf 2 OK-Testfälle (saubere VIRON-Voice)
4. Entwirf 2 Fix-Testfälle (1-2 konkrete Voice-Verletzungen)
5. Entwirf 2 Reject-Testfälle (Buzzword-Flut, falsche ICP)
6. Schreibe evals/evals.json
7. Update Report auf ✅ DONE

INPUT-FILES:
- C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\brand-voice-guardian-spec.md
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\brand-voice-guardian\SKILL.md

OUTPUT-FILE: C:\Workspace\Repos\Marketing-Setup\.agents\skills\brand-voice-guardian\evals\evals.json

REPORT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\option-bc-build.md
```

**Operator-Gate nach M2:** Beide Outputs reviewen, GO für M3.

---

#### SA-4 — Brief-to-Campaign Spec

**Model-Header:** `model: opencode-go`

```
MISSION: Spezifikation für einen Skill, der 1 Marketing-Brief zu 4-6 fertigen Linear-Issues expandiert (Multi-Channel-Campaign-Plan).

CONTEXT-INJECTION:
- Du bist Campaign-Architect. Verstehe Linear-API-Schema (Teams, Labels, Priority, Estimate, Parent/Sub-Issues).
- Befolge 60_orchestration_and_sub_agents.md (4-Pillar Briefing).

SCOPE:
- LESEN: TASKS.md (Welle 4: G-1 bis G-6), DESK/REPORTS/dach-custom-skills.md (PROMPT_INITIAL-Pattern), .opencode/rules/60_orchestration_and_sub_agents.md, .agents/skills/ (für Inspiration: launch, content-strategy, social)
- MCP-NUTZUNG: use linear list_issues mit Filter team=MKT, status!=Done (aktuelle Welle-4-Issues lesen) — NUR LESEN, keine Mutations
- SCHREIBEN: NUR DESK/REPORTS/brief-to-campaign-spec.md UND DESK/REPORTS/option-bc-build.md
- VERBOTEN: live-Mutationen in Linear, Schreiben in .agents/skills/

GOAL: Spec mit Input-Format (Notion-Page-URL ODER Operator-Paste-Text), Output-Schema (Linear-Issue-JSON mit title, description, team, priority, labels, estimate, parentId, acceptanceCriteria), Multi-Channel-Expansion-Regeln (1 Brief → 4-6 Issues über Kanäle: Pillar, LinkedIn, Reels, Lead-Magnet, Email-Sequence, etc.), 2 fertige Beispiel-Mappings (z.B. G-5 AI-Act → 5-7 Issues).

CONSTRAINTS:
- FORBIDDEN: TodoWrite, scope-violation, Model-Wechsel
- MCP-Calls limitiert: maximal 3 list-Calls, keine create_issue
- KEIN Anthropic-Modell

STEPS:
1. Lese TASKS.md, dach-custom-skills.md, 60_orchestration_and_sub_agents.md
2. use linear list_issues (1x) — merke aktive Welle-4-Issues
3. Update Report auf ⏳ IN PROGRESS
4. Definiere Input-Format (JSON-Schema)
5. Definiere Output-Schema (Linear-Issue-Properties)
6. Entwirf Multi-Channel-Expansion-Regeln (welche Kanäle wann?)
7. Erstelle 2 Beispiel-Mappings (G-5 + G-4)
8. Update Report auf ✅ DONE

INPUT-FILES:
- C:\Workspace\Repos\Marketing-Setup\TASKS.md
- C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\dach-custom-skills.md
- C:\Workspace\Repos\Marketing-Setup\.opencode\rules\60_orchestration_and_sub_agents.md
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\launch\SKILL.md (Pattern-Referenz)
- Live: Linear MCP list_issues

OUTPUT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\brief-to-campaign-spec.md

REPORT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\option-bc-build.md
```

**Operator-Gate nach SA-4:** Spec reviewen, GO für M4.

---

#### SA-5 — Brief-to-Campaign SKILL.md

**Model-Header:** `model: opencode-zen`

```
MISSION: Production-Ready SKILL.md für brief-to-campaign bauen.

CONTEXT-INJECTION:
- Skill-Architekt (wie SA-2). Befolge 80_skill_construction_law.md + 80_anatomy_of_complex_skill.md.
- Pattern-Referenzen: launch/SKILL.md, content-strategy/SKILL.md.

SCOPE:
- LESEN: DESK/REPORTS/brief-to-campaign-spec.md (SA-4 Output), .agents/skills/launch/SKILL.md, .agents/skills/content-strategy/SKILL.md, .opencode/rules/80_skill_construction_law.md
- SCHREIBEN: NUR .agents/skills/brief-to-campaign/SKILL.md + Mirror, UND DESK/REPORTS/option-bc-build.md
- VERBOTEN: Beispieldaten schreiben, evals/ (SA-6 macht das)

GOAL: SKILL.md ≤ 300 Zeilen mit YAML-Header, Context-Block, Bedingungs-Matrix (Brief-Format → Output-Schritte), Workflow-Steps mit linearem MCP-Aufrufen (use linear create_issue), Acceptance Criteria pro Output-Issue.

CONSTRAINTS:
- FORBIDDEN: TodoWrite, scope-violation
- KEIN Anthropic-Modell
- Workflow-Steps MÜSSEN lineare MCP-Calls enthalten mit `use linear create_issue {args}` Pattern (aus SA-4-Spec)

STEPS:
1. Lese SA-4 Spec, launch/SKILL.md, content-strategy/SKILL.md
2. Update Report auf ⏳ IN PROGRESS
3. Lege Verzeichnis an: .agents/skills/brief-to-campaign/ + Mirror
4. Schreibe SKILL.md mit Workflow-Steps
5. Lege examples/.gitkeep an (SA-6 füllt)
6. Mirror nach ~/.config/opencode/skills/brief-to-campaign/SKILL.md
7. Update Report auf ✅ DONE

INPUT-FILES:
- C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\brief-to-campaign-spec.md
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\launch\SKILL.md
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\content-strategy\SKILL.md
- C:\Workspace\Repos\Marketing-Setup\.opencode\rules\80_skill_construction_law.md

OUTPUT-FILE: C:\Workspace\Repos\Marketing-Setup\.agents\skills\brief-to-campaign\SKILL.md (Mirror: C:\Users\bachl\.config\opencode\skills\brief-to-campaign\SKILL.md)

REPORT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\option-bc-build.md
```

---

#### SA-6 — Brief-to-Campaign Evals

**Model-Header:** `model: opencode-go`

```
MISSION: 5 Eval-Testfälle für brief-to-campaign.

CONTEXT-INJECTION:
- Eval-Designer (wie SA-3). Format: JSON-Array.
- Testfälle prüfen Issue-Anzahl, korrekte Channel-Mix, Linear-Properties-Validität.

SCOPE:
- LESEN: DESK/REPORTS/brief-to-campaign-spec.md, .agents/skills/brief-to-campaign/SKILL.md
- SCHREIBEN: NUR .agents/skills/brief-to-campaign/evals/evals.json UND Report

GOAL: 5 Testfälle: 1 minimal-Brief (3-4 Issues), 2 standard-Briefs (5-7 Issues), 1 maximal-Brief (10+ Issues), 1 Edge-Case (leerer Brief → Fehler-Behandlung).

CONSTRAINTS:
- Testfälle aus realen Welle-4-Briefs (G-5, G-4, G-1) abgeleitet
- KEIN Anthropic-Modell

STEPS:
1. Lese SA-4 Spec, SA-5 SKILL.md
2. Update Report auf ⏳ IN PROGRESS
3. Entwirf 5 Testfälle (1 minimal, 2 standard, 1 maximal, 1 edge-case)
4. Schreibe evals/evals.json
5. Update Report auf ✅ DONE

INPUT-FILES:
- C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\brief-to-campaign-spec.md
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\brief-to-campaign\SKILL.md

OUTPUT-FILE: C:\Workspace\Repos\Marketing-Setup\.agents\skills\brief-to-campaign\evals\evals.json

REPORT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\option-bc-build.md
```

**Operator-Gate nach M4:** Beide Outputs reviewen, GO für M5.

---

#### SA-7 — Integration Test (Live auf echtem Material)

**Model-Header:** `model: opencode-zen`

```
MISSION: Beide Skills auf echtem Welle-4-Material testen. Output: Score + 4-6 Linear-Issues als JSON.

CONTEXT-INJECTION:
- Du bist Integration-Tester. Führe beide Skills auf echtem Material aus, dokumentiere Ergebnis.
- Echtes Material: G-5 (AI-Act Lead-Magnet) + G-4 (5 LinkedIn-Takedown-Posts gegen GPT-Bastler).
- Ziel: Beweise dass Skills funktionieren, identifiziere Schwächen.

SCOPE:
- LESEN: .agents/skills/brand-voice-guardian/SKILL.md, .agents/skills/brief-to-campaign/SKILL.md, TASKS.md (G-5 + G-4), .agents/skills/brand-voice-guardian/evals/evals.json
- SCHREIBEN: NUR DESK/REPORTS/pipeline-integration-test.md UND Report
- KEIN Linear/Notion-Mutation (außer explizit freigegeben vom Operator)
- VERBOTEN: Schreiben in .agents/skills/

GOAL: Markdown-Report mit (a) brand-voice-guardian Scores für alle 5 G-4-Posts (Tabelle), (b) brief-to-campaign Expansion von G-5 in 6-10 Linear-Issues als JSON, (c) 3 konkrete Verbesserungs-Vorschläge für beide Skills.

CONSTRAINTS:
- FORBIDDEN: TodoWrite, scope-violation
- KEIN Anthropic-Modell
- KEINE live create_issue-Calls — Issues als JSON im Report, Operator submitted manuell

STEPS:
1. Lese beide SKILL.md, TASKS.md (G-5 + G-4)
2. Update Report auf ⏳ IN PROGRESS
3. Wende brand-voice-guardian Workflow an auf alle 5 G-4-Posts (TASK: simuliere das Material falls Posts noch nicht geschrieben — nutze Brief-Beschreibungen aus TASKS.md)
4. Wende brief-to-campaign Workflow an auf G-5
5. Generiere Issue-JSON-Liste (6-10 Issues)
6. Identifiziere 3 Schwächen pro Skill
7. Schreibe Report
8. Update Report auf ✅ DONE

INPUT-FILES:
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\brand-voice-guardian\SKILL.md
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\brief-to-campaign\SKILL.md
- C:\Workspace\Repos\Marketing-Setup\TASKS.md
- C:\Workspace\Repos\Marketing-Setup\.agents\skills\brand-voice-guardian\evals\evals.json

OUTPUT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\pipeline-integration-test.md

REPORT-FILE: C:\Workspace\Repos\Marketing-Setup\DESK\REPORTS\option-bc-build.md
```

**Operator-Gate nach SA-7:** Report reviewen, GO für M6.

---

### M6 — Commit & Handover-Close (5 min, stärkstes verfügbares Model)

1. **DOCS/SKILL_INDEX.md** updaten: beide neuen Skills mit Scan-Depth eintragen (brand-voice-guardian: ~250 Zeilen, YAML + Bedingungs-Matrix + Beispiele; brief-to-campaign: ~300 Zeilen, YAML + Multi-Channel-Workflow)
2. **TASKS.md** updaten: G-5 + G-4 Status auf "in_progress mit Skills-Tooling" o.ä.
3. **Final-Commit** mit Message: `feat(skills): add brand-voice-guardian + brief-to-campaign (Welle 4 tooling)`
4. **HANDOVER.md** per `edit` (NICHT `write`) auf "abgeschlossen"-Status — Status-Block oben ergänzen mit ✅ DONE-Liste

---

## 8. MODEL-ORCHESTRIERUNG-MATRIX

**Verfügbare Provider (laut `.env.local`, KEIN Anthropic):**

| Provider | ENV-Var | Charakter | Use-Case |
|:---------|:--------|:----------|:---------|
| **NVIDIA NIM** | `NVIDIA_NIM_API_KEY` | Multi-Model (flexibel) | Universell einsetzbar |
| **OpenCode Go** | `OPENCODE_GO` | Schnell, günstig | Standardtasks, Research, Evals |
| **OpenCode ZEN** | (intern) | Stark, teurer | Strategie, SKILL.md-Schriften, Qualität |

**SubAgent-Zuweisung:**

| SubAgent | Task | Provider | Warum |
|:---------|:-----|:---------|:------|
| SA-1 | brand-voice-guardian Spec | OpenCode Go | Strukturiert, Recherche-lastig |
| SA-2 | brand-voice-guardian SKILL.md | OpenCode ZEN | Qualität entscheidend, Skill-Architektur |
| SA-3 | brand-voice-guardian Evals | OpenCode Go | Strukturiert, repetitiv |
| SA-4 | brief-to-campaign Spec | OpenCode Go | Strukturiert + MCP-Calls |
| SA-5 | brief-to-campaign SKILL.md | OpenCode ZEN | Qualität entscheidend, Workflow-Komplexität |
| SA-6 | brief-to-campaign Evals | OpenCode Go | Strukturiert, repetitiv |
| SA-7 | Integration Test | OpenCode ZEN | Beide Skills gleichzeitig, braucht Tiefe |
| Orchestrator | Strategie, Gates | OpenCode ZEN | Übersicht + Approval-Gates |

**Operator-Hinweis:** Wenn SubAgent qualitativ schwach → eine Stufe hoch (Go → ZEN). Wenn zu langsam → eine Stufe runter (ZEN → Go). NIM als Fallback-Provider wenn Go/ZEN nicht verfügbar.

**Naming-Convention für SubAgent-Header (im Task-Tool):**
```
model: opencode-zen    # Schreib-Tasks
model: opencode-go     # Standardtasks
model: nim             # Fallback (NIM-small oder NIM-large je nach Bedarf)
```

---

## 9. WORKFLOW-REGELN (zwingend einzuhalten)

Per `marketing_workflow_dod.md` und `sub-agents.md`:

1. **JEDER SubAgent-Prompt** muss enthalten: "Du bist FORBIDDEN von step N+1 bevor step N als ✅ DONE im Report-File markiert ist"
2. **JEDER SubAgent-Prompt** muss enthalten: "FORBIDDEN: TodoWrite, Anthropic-Modelle (Opus/Haiku/Sonnet), scope-violation"
3. **JEDER SubAgent-Prompt** muss SCOPE explizit nennen (welche Dateien lesen/schreiben)
4. **Report-First-Tracking**: `DESK/REPORTS/option-bc-build.md` ist die zentrale Tracking-Datei
5. **Operator-Approval-Gates** nach M1, M2, M3, M4 (SubAgent-Outputs reviewen bevor weiter)
6. **3-Zonen-Modell**: SubAgents schreiben NUR in `STORAGE/CONTENT/_wip/` oder Skills-Verzeichnisse — nie direkt in `STORAGE/CONTENT/` (Final)
7. **Notion READ-ONLY**: SubAgent darf `use notionApi` zum Lesen, aber Outputs gehen in Files, nicht zurück nach Notion
8. **Linear-MCP-Nutzung**: SubAgent darf `use linear` für live Issue-Reads, aber NEUE Issues nur nach Operator-Approval in M5/M6

---

## 10. ERFOLGSKRITERIEN (Definition of Done)

Diese Session ist ✅ DONE wenn:
- [ ] `.agents/skills/brand-voice-guardian/SKILL.md` existiert + `evals/evals.json` (6 Testfälle)
- [ ] `.agents/skills/brief-to-campaign/SKILL.md` existiert + `evals/evals.json` (5 Testfälle)
- [ ] `DESK/REPORTS/pipeline-integration-test.md` zeigt Score + 4-6 Linear-Issues für echtes Welle-4-Material
- [ ] `DOCS/SKILL_INDEX.md` enthält beide neuen Skills mit Scan-Depth
- [ ] `TASKS.md` ist aktualisiert (Option B + C auf DONE)
- [ ] Git-Commit existiert mit aussagekräftiger Message
- [ ] MCPs funktionieren weiterhin (`opencode mcp list` zeigt beide connected)
- [ ] HANDOVER.md wurde per `edit` (nicht `write`) aktualisiert auf "abgeschlossen"

**Wenn eines davon fehlt → Session nicht abgeschlossen. Handover in neuen HANDOVER.md-Zyklus mit Lücken.**

---

> **Handover abgeschlossen.** Warte auf nächsten Operator-Auftrag.

---

## WICHTIG: KEINE FRAGEN IN HANDOVER

Diese Datei enthält **reine Daten**. Fragen, Verifikationen und P00-Tests gehören in `P02_HANDOFF.md` (Forensischer Report) oder in `P00_BOOTSTRAP_DISPATCHER.md` (Stress-Test-Fragen).

**Adaptiert aus:** Viron-agency-stack HANDOVER.md (93Z, P00-Fragen entfernt)
