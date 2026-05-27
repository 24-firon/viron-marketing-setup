# DECISIONS.md — VIRON Marketing-Setup

**Stand:** 2026-05-25

---

## Entscheidungslog (Architecture Decision Records)

---

### ADR-001: Skills-Priorisierung — 14 aktiv, 19 archiviert, 7 aussortiert

- **Titel:** Selektive Übernahme der marketingskills v2.0.1
- **Datum:** 2026-05-22
- **Status:** Akzeptiert
- **Kontext:** Das Upstream-Repo `coreyhaines31/marketingskills` (v2.0.1, 29.875 Stars) bietet 40 kuratierte Marketing-Skills. VIRON als AI Automation Agency (kein SaaS) kann nicht alle Skills nutzen. 7 Skills sind für VIRON strukturell irrelevant (aso, paywalls, churn-prevention, community-marketing, co-marketing, referrals — existieren nicht im VIRON-Geschäftsmodell).
- **Entscheidung:** Von 40 Skills werden 33 übernommen. Davon 14 aktiv in `.agents/skills/` (häufig genutzte Kernkompetenzen: copywriting, cro, social, content-strategy, pricing, etc.) und 19 inaktiv in `ARCHIVE/skills/` (SEO/Analytics/Ads — aktuell nicht benötigt, aber jederzeit aktivierbar). 7 Skills (aso, paywalls, churn-prevention, community-marketing, co-marketing, referrals, marketing-ideas) ersatzlos aussortiert.
- **Verworfene Alternative:** Alle 40 Skills aktiv installieren.
- **Warum diese Entscheidung:** Token-Budget-Schonung (nur 14 Skills auto-injiziert via opencode.jsonc, 19 on-demand im Archiv). VIRON-spezifische Filterung verhindert Fehleinsätze (z.B. paywalls-Skill ist für SaaS, nicht für Agentur).
- **Tradeoffs:** Bei Bedarf muss ein archivierter Skill manuell aktiviert werden (Datei aus ARCHIVE/skills/ nach .agents/skills/ kopieren + skill-router.md updaten). Upstream-Änderungen an archivierten Skills werden nicht automatisch erkannt.
- **Folgen:** `DOCS/skill-router.md` definiert den Routing-Algorithmus. `skills-lock.json` trackt 32 Skills. Agent muss vor Skill-Nutzung skill-router.md konsultieren.

---

### ADR-002: opencode.jsonc Struktur — 15 instructions, .agents/skills statt .opencode

- **Titel:** Zentrale Agent-Konfiguration in opencode.jsonc
- **Datum:** 2026-05-22
- **Status:** Akzeptiert
- **Kontext:** Das Repo benötigt eine klare Agent-Konfiguration, die festlegt, welche Kontextdateien bei Session-Start geladen werden und wo Skills liegen. opencode.jsonc ist das native Konfigurationsformat für opencode.
- **Entscheidung:** `opencode.jsonc` enthält 15 instructions in dieser Reihenfolge:
  1. `./AGENTS.md` — Build/Lint/Test-Befehle, Codestil
  2. `./CLAUDE.md` — VIRON AI OS Context & Guidelines (Primärreferenz)
  3. `./DOCS/skill-router.md` — Skill-Routing-Matrix
  4. `./DOCS/storage-router.md` — Payload-Routing
  5. `./DOCS/brand-voice.md` — Brand Voice Guidelines
  6. `./DOCS/icp-summary.md` — ICP Definition
  7. `./TASKS.md` — Aktive Task-Liste
  8. `./.opencode/rules/00_flow_and_session_hygiene.md`
  9. `./.opencode/rules/design.md`
  10. `./.opencode/rules/marketing_amnesia_drift.md`
  11. `./.opencode/rules/marketing_batching.md`
  12. `./.opencode/rules/marketing_funnel_design.md`
  13. `./.opencode/rules/marketing_routing_stops.md`
  14. `./.opencode/rules/marketing_workflow_dod.md`
  15. `./.opencode/rules/sub-agents.md`

  Skills-Pfad: `.agents/skills` (nicht `.opencode/skills`). Watcher ignoriert: .git, .claude, .cursor, .agents, .agent, STORAGE/, DESK/, ARCHIVE/, IMPORT/, Binärdateien.

- **Verworfene Alternative:** Alle Kontextdateien manuell pro Session laden oder direkt in CLAUDE.md einbetten.
- **Warum diese Entscheidung:** Auto-Injection verhindert, dass Agenten Kontext vergessen. Trennung von Foundation (DOCS/ → immer geladen) und Payload (STORAGE/ → on-demand) spart Tokens. 7 operative Regeln in .opencode/rules/ zentralisieren das Regelwerk.
- **Tradeoffs:** Bei 15 instructions steigt der initiale Token-Verbrauch pro Session. DOCS/-Dateien sind redundant (skill-router.md enthält auch Regeln, die in CLAUDE.md stehen). Spätere Optimierung nötig.
- **Folgen:** Agent muss DOCS/ NICHT manuell lesen — sie werden automatisch injiziert. STORAGE/ muss on-demand geladen werden (via storage-router.md). ARCHIVE/Skills sind nicht Teil der Auto-Injection.

---

### ADR-003: Repo-Architektur — DOCS/, STORAGE/, ARCHIVE/, DESK/

- **Titel:** 4-Zonen-Architektur für Agent-Kontext und Payload
- **Datum:** 2026-05-22
- **Status:** Akzeptiert
- **Kontext:** Das Repo muss Wissen in verschiedenen Granularitätsstufen vorhalten: Immer verfügbarer Kontext (DOCS/), bei Bedarf ladbare Payloads (STORAGE/), inaktive aber erhaltene Ressourcen (ARCHIVE/), und temporäre Arbeitsbereiche für SubAgents (DESK/).
- **Entscheidung:** Vier Zonen mit klaren Zuständigkeiten:
  - **DOCS/** — Auto-injizierte Foundation-Dokumente (Brand Voice, ICP, Skill Router, Storage Router). Immer geladen. Kurz und präzise (je <100 Zeilen).
  - **STORAGE/** — Payload-Wissen, on-demand geladen. Enthält: Integrationsberichte (44 KB), inaktive Skills im Unterordner `archive/skills/`, Tool-Evaluationen, Content-Backups. Nicht in opencode-Watcher.
  - **ARCHIVE/** — Vollständig deaktivierte Ressourcen. 19 Skills in `ARCHIVE/skills/`, die bei Bedarf nach `.agents/skills/` kopiert werden können. Nicht im Watcher.
  - **DESK/** — WIP-Zone für SubAgent-Outputs. HANDOVER/ (Session-Logs), REPORTS/ (SubAgent-Reports), TASKS/ (Envelopes für Batch-Ausführung). Nicht im Watcher.
- **Verworfene Alternative:** Alles in DOCS/ oder alles in STORAGE/ (flache Struktur).
- **Warum diese Entscheidung:** Token-Effizienz (nur DOCS/ wird auto-injiziert). Klare Trennung zwischen "immer lesen", "bei Bedarf laden" und "nie laden". SubAgents arbeiten isoliert in DESK/ ohne das Haupt-Repo zu verschmutzen.
- **Tradeoffs:** Mehrere Verzeichnisse erhöhen die kognitive Last für den Operator. Archivierte Skills müssen manuell gepflegt werden (keine Auto-Updates vom Upstream). DESK/-Dateien sind nicht versioniert (ignored in Watcher).
- **Folgen:** `DOCS/storage-router.md` definiert die Load-Regeln für STORAGE/. `ARCHIVE/`-Skills haben kein SKILL.md im Root — der Pfad ist `ARCHIVE/skills/<name>/SKILL.md`. DESK/-Reports müssen regelmäßig ausgewertet und danach archiviert werden.

---

### ADR-004: Marketingskills v2.0.1 Upgrade — Breaking Changes dokumentiert

- **Titel:** Upgrade von marketingskills v1.x auf v2.0.1 mit 17 Renames und 1 Consolidation
- **Datum:** 2026-05-22
- **Status:** Akzeptiert
- **Kontext:** Das Upstream-Repo `coreyhaines31/marketingskills` hat am 19. Mai 2026 Version 2.0.1 veröffentlicht. Dieses Release enthält signifikante Breaking Changes: 17 Skill-Renames (z.B. `page-cro` → `cro`, `form-cro` → `cro` merged, `signup-flow-cro` → `signup`, `onboarding-cro` → `onboarding`, `popup-cro` → `popups`, `email-sequence` → `emails`, `social-content` → `social`, `paid-ads` → `ads`, `pricing-strategy` → `pricing`, `product-marketing-context` → `product-marketing`, `ab-test-setup` → `ab-testing`, `analytics-tracking` → `analytics`, `schema-markup` → `schema`, `competitor-alternatives` → `competitors`, `free-tool-strategy` → `free-tools`, `launch-strategy` → `launch`) und 1 Consolidation (`form-cro` merged in `cro`, `page-cro` → `cro`). Dazu kommen neue v2.0-Skills ohne v1-Entsprechung: `marketing-psychology`, `competitor-profiling`, `directory-submissions`, `launch`, `image`, `video`.
- **Entscheidung:** Vollständiges Upgrade auf v2.0.1. Alle v1.x-Skills aus `.agents/skills/` und `.claude/skills/` entfernt. Neue v2.0-Skills installiert (33 von 40). `skills-lock.json` mit v2.0-Namen aktualisiert. `DOCS/skill-router.md` auf v2.0-Namen umgeschrieben (Mapping-Tabelle v1→v2 enthalten). Alle Breaking Changes im Integrationsbericht (`STORAGE/marketingskills-integration-bericht.md`) dokumentiert.
- **Verworfene Alternative:** Auf v1.x bleiben oder nur selektiv einzelne Skills upgraden.
- **Warum diese Entscheidung:** Upstream-Support für v1.x endet. Neue v2.0-Skills (marketing-psychology, competitor-profiling, image, video) sind für VIRON hochrelevant. Konsolidierung von `page-cro` + `form-cro` → `cro` reduziert Redundanz.
- **Tradeoffs:** Alle internen Referenzen und Workflows mussten auf v2.0-Namen umgestellt werden. Kurze Downtime während des Upgrades. skills-lock.json enthält noch v1.x-Hashes (32 Einträge, teils mit v1-Namen) — muss bereinigt werden.
- **Folgen:** `DOCS/skill-router.md` enthält Mapping-Tabelle v1→v2 für zukünftige Referenzen. Bei erneutem Upstream-Upgrade muss der Integrationsbericht als Vergleich herangezogen werden. Keine v1.x-Skills mehr im Repo (weder aktiv noch archiviert).

---

## Entscheidungsvorlage

Neue ADRs werden nach folgendem Schema angelegt:

```markdown
### ADR-XXX: Kurzer Titel

- **Titel:** Beschreibender Titel der Entscheidung
- **Datum:** YYYY-MM-DD
- **Status:** [Vorgeschlagen | Akzeptiert | Verworfen | Überholt]
- **Kontext:** Welches Problem soll gelöst werden? Welche Randbedingungen gelten?
- **Entscheidung:** Was wurde entschieden? Wie lautet die neue Regel/Architektur?
- **Verworfene Alternative:** Welche andere Option wurde ernsthaft in Betracht gezogen?
- **Warum diese Entscheidung:** Kurze Begründung der Abwägung.
- **Tradeoffs:** Welche Nachteile werden bewusst in Kauf genommen?
- **Folgen:** Was muss sich jetzt ändern? Welche Dateien/Prozesse sind betroffen?
```
