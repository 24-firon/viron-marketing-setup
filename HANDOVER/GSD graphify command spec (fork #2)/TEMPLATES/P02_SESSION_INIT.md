# P02 — Session Init (Kompakt)

> **EXECUTION-MODE.** Comprehension Gate, dann Meilensteine abarbeiten. **DENN** ohne Hard-Stop springt der Agent blind zu Aktionen.

## COMPREHENSION GATE 2 (HARD STOP)

BEVOR du mit der Arbeit beginnst, alle 3 Schritte:

### Schritt A: Injizierten Kontext sichten
- Welche 16 Dateien sind injiziert via `opencode.jsonc`? (AGENTS.md, CLAUDE.md, TASKS.md, 4× DOCS/, 8× Regeln, 3× DACH-Skills-Trigger)
- Welche Architektur-Konzepte sind aktiv? (4-Zonen-Architektur DOCS/STORAGE/ARCHIVE/DESK, 3-Modi Schnell/Normal/Ausführlich, Provider-Stack OpenCode ZEN/Go/NVIDIA NIM)
- **BEWEIS:** "Ich habe die injizierten Dateien verarbeitet. 3 kritischste Lücken: (a) 7 Spec-TODOs aus Build-Report ungelöst, (b) M3 N8N-Integration blockiert durch Hetzner, (c) Git-Cred-Persistenz nicht gefixt"

### Schritt B: Task-spezifische Dateien lesen
- Alle Tier-1-Dateien aus P01 (physisch geladen — siehe P01_LESELISTE.md)
- Domain-spezifische Context-Dateien: `HANDOVER/GSD graphify command spec (fork #2)/TEMPLATES/HANDOVER.md`, `SESSION_HANDOVER.md`, `CURRENT_TASKLIST.md`, `IMPLEMENTATION_PLAN.md`, `WORKSPACE_WALKTHROUGH.md`
- DACH-Spec: `DESK/REPORTS/dach-custom-skills.md`
- Build-Report: `DESK/REPORTS/dach-p0-skills-build.md`

### Schritt C: Bestätigung
> "Comprehension Gate bestanden. 16 injizierte Dateien, 11 Tier-1-Dateien gelesen (3 Batches + 3 Domain-Files + 4 Handover-Templates). Bereit für operative Arbeit."

**Ohne Bestätigung: KEINE EDITS. KEINE BASH-BEFEHLE. KEINE SUB-AGENTS.**

## REGEL-AKTIVIERUNG (vor jedem Schritt)

| Schritt | Regel-Zitat | Zweck |
|:---|:---|:---|
| Datei lesen | "Gemäß Forensisches Lese-Primat lese ich..." | Beweis vor Behauptung |
| Datei vergleichen | "Gemäß Zero-Assumption vergleiche ich..." | Keine Annahmen |
| Datei erstellen | "Gemäß Pre-Flight Radar verschaffe ich mir Lagebild" | Sicherheit vor Aktion |
| Evidence zeigen | "Gemäß Evidence-Based Execution zeige ich Output" | Keine Erfolgs-Behauptung |

## MEILENSTEINE (anpassen für deine Session)

### M1: 7 Spec-TODOs auflösen
- [ ] Schritt 1: Jeden TODO einzeln mit Operator durchgehen (Spec erweitern oder bewusste Lücke)
- [ ] Schritt 2: Entscheidungen in `DESK/REPORTS/dach-custom-skills.md` oder in Spec-Quelle integrieren
- [ ] Schritt 3: Skills bei Bedarf mit `edit` updaten, Commits erstellen

⏸️ **STOPP 1** — Berichte Entscheidungen pro TODO. Warte auf GO für M2.

### M2: Git-Cred-Persistenz fixen
- [ ] Schritt 1: SSH-Key generieren und zu GitHub hinzufügen, ODER `gh auth switch -u 24-firon` in `scripts/load-env.ps1` aufnehmen
- [ ] Schritt 2: Test-Push durchführen
- [ ] Schritt 3: Dokumentation in `AGENTS.md` oder README aktualisieren

⏸️ **STOPP 2** — Berichte gewählte Lösung. Warte auf GO für M3.

### M3: M3 N8N-Integration starten (wenn Hetzner-Deployment steht)
- [ ] Schritt 1: Hetzner VPS bereitstellen (CX22+)
- [ ] Schritt 2: docker-compose.yml für n8n + PostgreSQL erstellen
- [ ] Schritt 3: n8n deployen, per HTTPS erreichbar machen
- [ ] Schritt 4: n8n-nodes-mcp Community Node installieren
- [ ] Schritt 5: "VIRON Test Ping" Workflow erstellen

⏸️ **STOPP 3** — Abschluss. Vorbereitung für P99.

## MODELL-ROTATION (Eisenhart)

**🛑 HARTER STOPP bei JEDEM Modell-Wechsel.** Das System darf nicht ohne explizites "Go" vom Operator weitermachen.

| Phase | Modell | Zweck |
|:---|:---|:---|
| Planung (M1-Vorbereitung) | 🔴 STARK | Reasoning |
| Ausführung (M1-M3) | 🟢 STANDARD | Code, Bash |
| Status-Checks (zwischendurch) | ⚡ LIGHT | Grep, Logs |
| STOPP-Berichte | 🔴 STARK | Evidence-Bewertung |

## MINDSET-BLOCK

- **Surgical Precision:** Ändere Dateien nur nativ (`edit` / `write`)
- **Evidence-Based Execution:** Traue keinem `exit 0` — liefere Output
- **Linearer Gehorsam:** Schritte nacheinander, nicht parallelisieren
- **Approval-Gates:** Kritische Aktionen brauchen "GO" vom Operator
- **Lab-First:** Neue Ideen erst im eigenen Workspace testen, dann in `src/rules/` promoten
- **Skill-Vorgaben exakt befolgen:** Nicht interpretieren, nicht eigenmächtig abweichen (Lektion aus Session 2026-06-17)

## 4 GESETZE DER PERSISTENZ

1. **KEINE LÖSCHUNG** — Archivieren, nicht löschen
2. **KEINE REDUKTION** — 100% Code-Erhalt, keine `//...`-Abkürzungen
3. **BEWEISPFLICHT** — Physische Artefakte (Reports, Diffs), nicht Chat-Text
4. **INTEGRATION** — Korrekturen an die richtige Stelle, nicht ans Ende

## BESTÄTIGUNG

> "P02 initialisiert. Gate bestanden. 3 Meilensteine definiert (Spec-TODOs, Git-Cred-Fix, M3 N8N-Integration). Bereit für Ausführung."

⏸️ **STOPP** — Nächstes Modell: 🟢 STANDARD.
