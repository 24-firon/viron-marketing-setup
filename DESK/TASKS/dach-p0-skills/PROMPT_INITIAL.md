# TASK: DACH-P0 — DACH Custom Marketing Skills bauen

## 1. MISSION

Baue 3 DACH-spezifische Marketing-Skills in `.agents/skills/`. Diese Skills füllen Lücken die das US-zentrische marketingskills-Repo nicht abdeckt: DSGVO-Compliance, LinkedIn DACH B2B, Local SEO für Google Business Profile.

Jeder Skill muss:
- `SKILL.md` mit YAML-Frontmatter haben
- `evals/evals.json` mit 6 Testfällen haben
- In `.agent/skills/` und `.claude/skills/` gespiegelt sein
- In `DOCS/skill-router.md` eingetragen sein

## 2. CONTEXT (SSoT-Wissen)

LIES diese Dateien zwingend VOR der Ausführung:
- `DESK/REPORTS/dach-custom-skills.md` — Vollständige Skill-Spezifikationen (YAML, Trigger, Scope, Dependencies)
- `DOCS/brand-voice.md` — Brand Voice Guidelines (muss in Skills referenziert werden)
- `DOCS/icp-summary.md` — ICP Definition (muss in Skills referenziert werden)
- `.agents/product-marketing.md` — Produktkontext (Foundation für alle Skills)
- `IMPORT/05_DACH_Marketing_Spezifika.md` — DACH-spezifische Marketing-Techniken

## 3. SCOPE (Die Handschellen)

Du darfst NUR folgende Dateien/Ordner modifizieren:
- `.agents/skills/dsgvo-lead-capture/`
- `.agents/skills/linkedin-dach-b2b/`
- `.agents/skills/local-seo-gbp/`
- `.agent/skills/dsgvo-lead-capture/`
- `.agent/skills/linkedin-dach-b2b/`
- `.agent/skills/local-seo-gbp/`
- `.claude/skills/dsgvo-lead-capture/`
- `.claude/skills/linkedin-dach-b2b/`
- `.claude/skills/local-seo-gbp/`
- `DOCS/skill-router.md`

Du darfst NIEMALS folgende Dateien/Ordner anfassen:
- `CLAUDE.md`
- `CONTEXT.md`
- `MILESTONES.md`
- `DECISIONS.md`
- `opencode.jsonc`
- `STORAGE/`
- `ARCHIVE/`
- `IMPORT/`

## 4. ATOMARE SCHRITTE

### Skill 1: dsgvo-lead-capture
1. Lies `DESK/REPORTS/dach-custom-skills.md` Abschnitt "Skill 1"
2. Erstelle `.agents/skills/dsgvo-lead-capture/SKILL.md` mit:
   - YAML-Frontmatter (name, description)
   - Abschnitte: Trigger-Phrasen, Scope, Abhängigkeiten, Referenzen, Output-Format
   - Referenz auf `.agents/product-marketing.md`, `DOCS/brand-voice.md`, `DOCS/icp-summary.md`
3. Erstelle `.agents/skills/dsgvo-lead-capture/evals/evals.json` mit 6 Testfällen
4. Kopiere den kompletten Ordner nach `.agent/skills/` und `.claude/skills/`
5. **REPORT:** Zeige erste 20 Zeilen der SKILL.md

### Skill 2: linkedin-dach-b2b
1. Lies `DESK/REPORTS/dach-custom-skills.md` Abschnitt "Skill 2"
2. Erstelle `.agents/skills/linkedin-dach-b2b/SKILL.md`
3. Erstelle `.agents/skills/linkedin-dach-b2b/evals/evals.json`
4. Kopiere nach `.agent/skills/` und `.claude/skills/`
5. **REPORT:** Zeige erste 20 Zeilen der SKILL.md

### Skill 3: local-seo-gbp
1. Lies `DESK/REPORTS/dach-custom-skills.md` Abschnitt "Skill 3"
2. Erstelle `.agents/skills/local-seo-gbp/SKILL.md`
3. Erstelle `.agents/skills/local-seo-gbp/evals/evals.json`
4. Kopiere nach `.agent/skills/` und `.claude/skills/`
5. **REPORT:** Zeige erste 20 Zeilen der SKILL.md

### Skill-Router aktualisieren
1. Lies `DOCS/skill-router.md`
2. Füge die 3 neuen Skills in die entsprechenden Kategorien ein
3. **REPORT:** Zeige die neuen Einträge

## 5. REPORT-ZWANG

Deine Ergebnisse MÜSSEN als strukturierte Markdown-Datei abgelegt werden:
- `DESK/REPORTS/dach-p0-skills-build.md`

Format:
```markdown
# DACH-P0 Skills — Build Report

**Status:** [DONE / FAILED / PARTIAL]
**Abgeschlossen:** [Datum, Uhrzeit]

## Erstellte Skills
| Skill | SKILL.md | evals/ | .agent/ | .claude/ | Router |
|-------|----------|--------|---------|----------|--------|
| dsgvo-lead-capture | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| linkedin-dach-b2b | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| local-seo-gbp | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

## Evidence
[Erste 20 Zeilen jeder SKILL.md]

## Nächste Schritte
[Empfehlung für den Orchestrator]
```
