# STATE — DACH-P0

**Status:** IN BEARBEITUNG (Selbststop durch Operator-Kritik)
**Gestartet:** 2026-06-17 (P01-Freigabe)
**Letztes Update:** 2026-06-17

## Aktueller Fortschritt
- [x] Skill 1: dsgvo-lead-capture — SKILL.md erstellt (mit chirurgischen Korrekturen — Spec-Drift markiert)
- [x] Skill 1: dsgvo-lead-capture — evals/ erstellt (Eval #3 ersetzt wegen Spec-Drift)
- [x] Skill 1: dsgvo-lead-capture — gespiegelt nach .agent/ + .claude/
- [x] Skill 2: linkedin-dach-b2b — SKILL.md erstellt (mit TODO-Markierungen für Spec-Lücken)
- [x] Skill 2: linkedin-dach-b2b — evals/ erstellt (Eval #4 von Spec-Drift bereinigt)
- [x] Skill 2: linkedin-dach-b2b — gespiegelt nach .agent/ + .claude/
- [x] Skill 3: local-seo-gbp — SKILL.md erstellt (Verzeichnis-Liste mit TODO-Markierungen)
- [x] Skill 3: local-seo-gbp — evals/ erstellt (Eval #1 und #4 bereinigt)
- [x] Skill 3: local-seo-gbp — gespiegelt nach .agent/ + .claude/
- [x] DOCS/skill-router.md — neue Sektion „DACH Custom Skills" eingefügt (kein Edit-Schaden am Bestand)

## Verbleibende Schritte (für Approval-Block)
- [ ] STATE.md und SUMMARY.md finalisieren (nach Operator-Review der Skills)
- [ ] Build-Report `DESK/REPORTS/dach-p0-skills-build.md` schreiben
- [ ] Linear-Issue (M-XXX) aktualisieren mit Skill-Pfaden

## Offene Fragen an Operator
1. PostgreSQL-Schema-Namen für Lead-Capture: gibt es eine Quelle, oder TODO M2b?
2. Konkrete Cadence/Budget-Zahlen für LinkedIn DACH: Spec ergänzen oder TODO bleiben?
3. Service-Package-Definitionen (Deliverables pro Skill): wo sollen die hin (.agents/services/ oder STORAGE/)?
4. Verzeichnis-Priorisierung (Bing Places, Facebook, search.ch): Spec erweitern oder TODO lassen?
5. Soll ich nach diesen Korrekturen nochmal warten auf erneutes GO für weitere Iterationen, oder ist Stopp-Punkt erreicht?

## Notizen
- Operator hat iterative, langsame, qualitativ professionelle Arbeit gefordert — ich war zu schnell und zu erfinderisch.
- Korrektur-Modus war „edit" (chirurgisch), nicht „write" (komplett ersetzen) — File-Operation-Safety-Regel aus `.opencode/rules/file_operation_safety.md` befolgt.
- Spec-Drift wurde mit TODO-Markierungen kenntlich gemacht, nicht entfernt — damit Operator selbst entscheiden kann.
