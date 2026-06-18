# HANDOVER — Datenübergabe (Kompakt)

> **Reine Datenübergabe** an den nächsten Session-Agent. Keine Fragen, keine Verifikation. **DENN** diese Datei ist der „Erste Hilfe"-Koffer für den Nachfolger.

## 1. BLUF (Bottom Line Up Front)

DACH-P0-Skills (dsgvo-lead-capture, linkedin-dach-b2b, local-seo-gbp) gebaut, chirurgisch korrigiert, committet und gepusht. M2 formal abgeschlossen. 7 Spec-TODOs bewusst offen dokumentiert. 4 Commits auf main: 666a6a3, 80391bb, 39b9012, 4c1366a, c4ba10d.

## 2. PROJEKT-SPEZIFISCHE DATEN

| Schlüssel | Wert | Warum wichtig |
|:---|:---|:---|
| Branch | main | HEAD = c4ba10d, origin/main up to date |
| GitHub-Account | 24-firon | Viron-Agency hat keine Schreibrechte auf 24-firon/viron-marketing-setup |
| Repo-Pfad | C:\Workspace\Repos\Marketing-Setup | Working Directory |
| Session-Datum | 2026-06-17 | |
| Commit-Hashes | 666a6a3, 80391bb, 39b9012, 4c1366a, c4ba10d | Alle auf origin/main |
| Spec-Quelle DACH | DESK/REPORTS/dach-custom-skills.md | Kan. Spec für die 3 Skills |
| Build-Report | DESK/REPORTS/dach-p0-skills-build.md | Forensischer Build-Report mit 7 Spec-TODOs |

## 3. ERLEDIGTE ARBEIT

| Was | Status | Wann |
|:---|:---:|:---|
| Skill dsgvo-lead-capture (SKILL.md + evals.json) | ✅ | 2026-06-17 |
| Skill linkedin-dach-b2b (SKILL.md + evals.json) | ✅ | 2026-06-17 |
| Skill local-seo-gbp (SKILL.md + evals.json) | ✅ | 2026-06-17 |
| Spiegelung nach .agent/skills/ und .claude/skills/ | ✅ | 2026-06-17 |
| 13 chirurgische edit-Korrekturen (Spec-Drift markiert) | ✅ | 2026-06-17 |
| DOCS/skill-router.md: neue Sektion „DACH Custom Skills" | ✅ | 2026-06-17 |
| TASKS.md: D-1..D-4 Status auf Done | ✅ | 2026-06-17 |
| MILESTONES.md: M2 von „In Arbeit" auf „Abgeschlossen" | ✅ | 2026-06-17 |
| CONTEXT.md: Last completed items rotiert | ✅ | 2026-06-17 |
| 4 Commits auf main erstellt und gepusht | ✅ | 2026-06-17 |

## 4. ENTSCHEIDUNGEN

| Entscheidung | Warum | Reversibel? |
|:---|:---|:---:|
| Spec-Drift = TODO markieren, nicht stillschweigend füllen | Halluzinierte Tabellennamen/Cadence-Zahlen zerstören Spec-Treue bei SubAgent-Workflows | Ja |
| Trigger-Phrasen nur in YAML-Description, nicht im Body | Redundanz vermeiden, Token sparen, Konsistenz mit anderen Skills | Ja |
| Bestehende Dateien nur per `edit`, nie per `write` überschreiben | Konservierungs-Gesetz: Beweis vor Behauptung, Diff-Integrität | Ja |
| Sub-Schritt-GO explizit anfordern, nicht aus Phase-GO ableiten | Operator-Korrektur: iteratives Vorgehen, nicht stillschweigend alles in einem Rutsch | Ja |
| Git-Push nur mit 24-firon Account (nicht Viron-Agency, nicht 24Firon) | 403 Forbidden mit falschem Account, Token von 24Firon ist invalid | Ja |
| Session-Handover auf `DESK/HANDOVER/sessions/` | Bestehende M2-Konvention, nicht neuer Pfad im Root | Ja |

## 5. OFFENE TASKS

| Task | Priorität | Was zu tun |
|:---|:---:|:---|
| PostgreSQL-Schema für Lead-Capture (Tabellennamen) | P0 🔴 | Operator entscheidet: Spec erweitern oder TODO bleiben |
| LinkedIn Posting-Cadence (Posts/Woche + Kommentare/Tag) | P1 🟡 | Operator entscheidet: Spec erweitern oder TODO bleiben |
| LinkedIn Ads Mindestbudget | P1 🟡 | Operator entscheidet: Spec erweitern oder TODO bleiben |
| GBP Review-Antwort-Zeit | P1 🟡 | Operator entscheidet: Spec erweitern oder TODO bleiben |
| DACH-Verzeichnis-Priorisierung (Bing, Facebook, search.ch) | P1 🟡 | Operator entscheidet: Spec erweitern oder TODO bleiben |
| Service-Package-Definitionen (Deliverables pro Skill) | P1 🟡 | Wo ablegen: .agents/services/ oder STORAGE/? |
| Compliance-Summary 1-Page-Template | P1 🟡 | Vorlage erstellen oder ad-hoc lassen? |
| Git-Cred-Persistenz fixen | P2 🟢 | SSH-Key konfigurieren oder `gh auth switch` in Load-Script |
| M3 N8N-Integration starten | P0 🔴 | Wartet auf Hetzner-Deployment (blockiert) |

## 6. BEKANNTE PROBLEME & WORKAROUNDS

| Problem | Workaround | Fix geplant? |
|:---|:---|:---:|
| `gh auth` aktiv ist standardmäßig Viron-Agency, keine Schreibrechte | `gh auth switch -u 24-firon` vor jedem Push | Ja (Git-Cred-Persistenz) |
| 24Firon-Token ist invalid | Nicht verwenden, nur Viron-Agency oder 24-firon | Nein (alter Account) |
| Keine automatische Push-Token-Persistenz | Manueller `gh auth switch` Befehl vor jedem `git push` | Ja (Git-Cred-Persistenz) |
| Copy-Paste-Architektur über 3 Skills (identische Sektionsstruktur) | Alle 3 Skills funktionieren, nur ästhetisch maschinell | Optional, zukünftige Iterationen |

## 7. NÄCHSTE SCHRITTE (Konkret)

1. **7 Spec-TODOs auflösen** — Operator entscheidet pro TODO: Spec erweitern oder als bewusste Lücke akzeptieren
2. **M3 N8N-Integration vorbereiten** — Wartet auf Hetzner-Deployment. SubAgent-Prompts aus DESK/REPORTS/n8n-mcp-integration.md verwenden
3. **Git-Cred-Persistenz fixen** — SSH-Key oder `gh auth switch` in `scripts/load-env.ps1` aufnehmen
4. **Copy-Paste-Architektur aufbrechen** — Bei zukünftigen Skill-Erstellungen die Sektionsstruktur domain-adaptiert variieren

---

> **Handover abgeschlossen.** Warte auf nächsten Operator-Auftrag.

**WICHTIG:** KEINE FRAGEN IN HANDOVER. Fragen gehören in `P00_BOOTSTRAP.md` Section „7 FRAGEN".
