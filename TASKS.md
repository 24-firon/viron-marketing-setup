# VIRON — Aktive Task-Liste
**Stand:** 2026-05-25 | **Pflege:** Täglich aktualisieren nach Task-Abschluss

> Zielgruppe per Operator-Pivot (01.04.) geändert von Handwerk/Immobilien/Steuerberater → Lokaler Einzelhandel & Premium-Dienstleister. Siehe ORCHESTRATION_SYSTEM.md für aktualisierte Prompts.

> Abgeschlossenes Archiv (Welle 1-3, Template-Library, Setup) → siehe unten.
> Diese Datei zeigt nur aktive und geplante Tasks der Welle 4 (Hustle-Marketing & Growth).

---

## 🚀 WELLE 4: HUSTLE MARKETING & GROWTH (NEU)

> **Kontext:** Wir haben das Enterprise-Fundament. Jetzt gehen wir in die Offensive. Wir brauchen verrückte, laute und hochkonvertierende Marketing-Hacks, um die Bude bekannt zu machen. Kein Standard-B2B-Content mehr.

### Serie 4: Die "Guerrilla Outbound" Kampagne

| # | Task | Assigned | Status | Output |
|---|------|----------|--------|--------|
| G-1 | 3 freche Outreach-Scripts für Jobportale (Fokus: Automatisierung vs. "Wir suchen eine Tippse") | Extern (Gemini) | ⏳ Pending | `Content/Outreach-Hacks.md` |
| G-2 | n8n-Workflow Konzept: Scraping von schlechten Google-Reviews (Terminchaos) als Trigger für kalte DMs | Sonnet | ⏳ Pending | `Content/n8n-Growth-Hacks.md` |

### Serie 5: Der "Fake-Agency Takedown"

| # | Task | Assigned | Status | Output |
|---|------|----------|--------|--------|
| G-3 | "Warum euer 3.000€ ChatGPT-Workshop nutzlos war" - Ein provokanter Pillar-Artikel | Sonnet | ⏳ Pending | `Content/Pillar-Takedown.md` |
| G-4 | 5 aggressive LinkedIn-Posts gegen die "Wir basteln dir ein GPT"-Agenturen | Haiku Two | ⏳ Pending | `Content/LI-Takedown-Posts.md` |

### Serie 6: Die AI-Act Panik-Welle (Compliance Marketing)

| # | Task | Assigned | Status | Output |
|---|------|----------|--------|--------|
| G-5 | "Ist euer US-Lead-Scoring ab August illegal?" - Compliance-Lead-Magnet (PDF/Checkliste) | Sonnet | ⏳ Pending | `Content/AI-Act-Leadmagnet.md` |
| G-6 | 3 Schock-Reels zum Thema EU AI Act & US-Tools | Haiku Two | ⏳ Pending | `Content/Reels-AI-Act.md` |

---

## 🔧 PHASE 2 INFRASTRUCTURE TASKS

> **Kontext:** Repo-Foundation steht (Phase 1). Jetzt: DACH-Skills bauen, Tools evaluieren, N8N-MCP vorbereiten. Reports in DESK/REPORTS/.

### DACH Custom Skills (P0 — sofort umsetzbar)

| # | Task | Assigned | Status | Output |
|---|------|----------|--------|--------|
| D-1 | dsgvo-lead-capture Skill bauen (SKILL.md + evals/) | SubAgent | ✅ Done (Commit 666a6a3, 80391bb — 7 Spec-TODOs offen, siehe `DESK/REPORTS/dach-p0-skills-build.md`) | `.agents/skills/dsgvo-lead-capture/` |
| D-2 | linkedin-dach-b2b Skill bauen (SKILL.md + evals/) | SubAgent | ✅ Done (Commit 666a6a3, 80391bb — Spec-TODOs zu Cadence/Budget) | `.agents/skills/linkedin-dach-b2b/` |
| D-3 | local-seo-gbp Skill bauen (SKILL.md + evals/) | SubAgent | ✅ Done (Commit 666a6a3, 80391bb — Spec-TODOs zu Verzeichnissen/Antwort-Zeit) | `.agents/skills/local-seo-gbp/` |
| D-4 | DOCS/skill-router.md um 3 neue Skills erweitern | SubAgent | ✅ Done (Commit 80391bb — neue Sektion „DACH Custom Skills" eingefügt) | `DOCS/skill-router.md` |

**Task-Envelope:** `DESK/TASKS/dach-p0-skills/` (PROMPT_INITIAL.md, STATE.md, SUMMARY.md)
**Spezifikation:** `DESK/REPORTS/dach-custom-skills.md`

### Tools & Integration (P1 — Trigger-basiert)

| # | Task | Trigger | Status | Output |
|---|------|---------|--------|--------|
| T-1 | N8N-MCP: MCP-Server in opencode.jsonc + Test-Workflow | n8n-Deployment auf Hetzner | ⏳ Blocked | `DESK/REPORTS/n8n-mcp-integration.md` |
| T-2 | Cal.com Self-Hosted: Coolify Docker Compose deployen | Erster Kunde mit Terminbedarf | ⏳ Trigger | `DESK/REPORTS/tool-decisions.md` |
| T-3 | Exa MCP: `https://mcp.exa.ai/mcp` in opencode.jsonc | N8N-MCP steht | ⏳ Blocked | `DESK/REPORTS/tool-decisions.md` |
| T-4 | Buffer vs Metricool evaluieren | >50 Posts/Mo oder >1 Brand | ⏳ Trigger | `DESK/REPORTS/tool-decisions.md` |

**Implementation Plan:** `DESK/TASKS/implementation_plan.md`

---

## 🔧 SYSTEM-TASKS (laufend)

| # | Task | Wann | Status |
|---|------|------|--------|
| S-1 | INVENTAR.md nach jedem Batch aktualisieren | Nach Batch | Ongoing |
| S-2 | Linear MKT-40 kommentieren nach Content-Milestones | Wöchentlich | Ongoing |
| S-3 | ORCHESTRATION_SYSTEM.md reviewen + updaten | Nach großen Änderungen | Ongoing |

---

## ✅ ARCHIV — Abgeschlossen

**Template-Bibliothek (T-1 bis T-6) (2026-04-02):** 
Alle Reaktions-Templates (Reels, LinkedIn, Carousel, TikTok, n8n-RSS) fertiggestellt.

**Nischen-ROI Content Serie 1-3 (2026-04-01):** 
10 Posts, 2 Pillar-Artikel, 15 Reel-Skripte und 30 Hook-Library-Posts für Retail & Services generiert. 

**Linear Setup (2026-03-12):** 
2 Teams, 5 Projekte, 35 Issues, 5 Dependencies. Vollständig dokumentiert in `/VIRON_Full_Package_v2/`.

**Content-Pyramide Block 2–4 (2026-03-14):** 
4 Mega-Guides + 67 Pillar-Artikel + 41 Social Pieces produziert. Dokumentiert in `/Content/INVENTAR.md`.
