# decision_log.md — Chronologische Entscheidungen dieser Session

---

### 2026-06-07 23:30 — Skill-Name: `session_handover_generator`

**Kontext:** User brauchte einen selbst-erklärenden Skill-Namen, der die Funktion klar macht und alle Bundles später einschließt.

**Entscheidung:** Skill heißt `session_handover_generator` (nicht `bundle-kompakt`).

**Begründung:** "session_handover_generator" beschreibt die FUNKTION (Session-Übergabe-Generierung), nicht ein einzelnes Bundle. So können später VOLLSTÄNDIG, SLIM, MYCHOICE unter demselben Skill-Label laufen.

**Reversibel?** Ja — kann umbenannt werden, aber dann müssen alle Cross-References aktualisiert werden.

**Konsequenzen:** Skill-Pfad heißt `session_handover_generator/`, alle YAML-Header, Routing-Matrizen und Dokumentation referenzieren diesen Namen.

---

### 2026-06-07 23:35 — 3-Ebenen-Token-Bloat-Schutz

**Kontext:** Standard-Skills mergen alles in SKILL.md → Token-Verschwendung. User wollte explizit Token-Bloat vermeiden.

**Entscheidung:** 3-Ebenen-Struktur: YAML-Header (Trigger) → SKILL.md (Router, ≤180 Z.) → INSTRUCTIONS.md (Detail, ≥500 Z.).

**Begründung:** Agent sieht nur YAML, dann Inhaltsverzeichnis (25 Z.), entscheidet dann ob Match. Erst bei Match wird INSTRUCTIONS.md geladen.

**Reversibel?** Ja — Ebenen können zusammengelegt werden, aber Token-Effizienz sinkt.

**Konsequenzen:** Alle Workflows in INSTRUCTIONS.md, alle Trigger in SKILL.md. Keine Doppelung.

---

### 2026-06-07 23:40 — SubAgent-Prompts als echte Files, nicht Platzhalter

**Kontext:** Ich hatte SubAgent-Prompts als "Platzhalter" bezeichnet. User wies darauf hin, dass TASK_ENVELOPE, OPERATOR_WORKFLOW, ORCHESTRATOR_WORKFLOW echte Dateien in STORAGE sind.

**Entscheidung:** SubAgent-Prompts = echte Dateien in `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/KOPIERPAKET/`. HD-8 dokumentiert das explizit.

**Begründung:** Konsistenz mit CDS-Architektur. Storage enthält die operativen Dateien, Skill die systemische Logik.

**Reversibel?** Ja — falls in Zukunft anders organisiert.

**Konsequenzen:** INSTRUCTIONS.md verweist auf TASK_ENVELOPE, OPERATOR_WORKFLOW, ORCHESTRATOR_WORKFLOW. Q-D in Fragenkatalog klärt, welche SubAgent-Prompts in welcher Tiefe.

---

### 2026-06-07 23:45 — Bundle vs. Modus getrennt

**Kontext:** Q-A in INSTRUCTIONS.md vermischte Bundle-Wahl (SLIM/KOMPAKT/VOLLSTÄNDIG/MYCHOICE) mit Modus (SCHNELL/NORMAL/AUSFÜHRLICH).

**Entscheidung:** Klare Trennung. Q-A = Bundle, Modus = Smart-Mix (Agent entscheidet).

**Begründung:** Bundle = kompletter Template-Satz. Modus = Nutzungsprofil innerhalb eines Bundles. Verschiedene Entscheidungsebenen.

**Reversibel?** Ja.

**Konsequenzen:** User wählt Bundle in Q-A. Agent wählt Modus basierend auf Task + Kontext. 3 Modi-Definition jetzt in eigenem Abschnitt.

---

### 2026-06-07 23:50 — HD-2 mit Token-Guard-Tabelle konsistent

**Kontext:** HD-2 sagte "< 30% keine examples/", Token-Guard-Tabelle sagte "< 60% keine examples/". Widerspruch.

**Entscheidung:** HD-2 angepasst an Tabelle: "< 60% keine examples/".

**Begründung:** Konsistenz. Token-Tabelle ist die "Source of Truth".

**Reversibel?** Ja.

**Konsequenzen:** Bei Gelb (30-60%) werden keine examples/ geladen, nur SKILL.md + INSTRUCTIONS.md + max. 2 references/.

---

### 2026-06-07 23:55 — HD-0 als ERSTE Aktion

**Kontext:** Token-Fenster-Frage war in INSTRUCTIONS.md, aber nicht als Hard Directive. Agent könnte sie überspringen.

**Entscheidung:** HD-0 in SKILL.md: "ALS ERSTES IMMER — Frage User nach Token-Fenster-Status".

**Begründung:** Compaction-Prävention ist kritisch. User-Schätzung + 50-100% Aufschlag = sicheres Budget.

**Reversibel?** Ja.

**Konsequenzen:** Jeder Skill-Workflow startet mit Token-Frage. Re-Asking-Protokoll bei Nicht-Antwort.

---

### 2026-06-07 00:00 — 50-100% Aufschlag auf Token-Schätzungen

**Kontext:** User-Erfahrung: LLM schätzt Tokens 50-100% zu niedrig. 50KB-Datei → LLM sagt 10-15K, real 20-25K.

**Entscheidung:** Realitäts-Aufschlag in TOKEN_WINDOW_GUARD.md dokumentiert. Alle Token-Berechnungen mit +50% (Grün) bis +100% (Rot) Aufschlag.

**Begründung:** User hat das empirisch erfahren. Realismus > Optimismus bei Token-Budgets.

**Reversibel?** Ja — wenn bessere Schätz-Tools verfügbar werden.

**Konsequenzen:** Konservativere Planung. Token-Frage wird wichtiger.

---

### 2026-06-07 00:05 — notfall/ eingebettetes Backup-Bundle

**Kontext:** User wollte ein Backup, das IMMER verfügbar ist, ohne STORAGE-Abhängigkeit.

**Entscheidung:** `notfall/` Ordner im Skill mit 5 Dateien (README, P99_MINIMAL, HANDOVER_MINIMAL, REPORT_MINIMAL, CHECKLIST_MINIMAL).

**Begründung:** Token 🔴/⚫ ODER Storage leer → notfall/ greift. "Standard-mäßig, mittelmäßig" — nicht zu reduziert, nicht zu ausführlich.

**Reversibel?** Ja.

**Konsequenzen:** Skill hat ein eingebettetes Backup. Funktioniert auch offline / ohne Storage-Zugriff.

---

### 2026-06-07 00:10 — 6 lebendige Dateien als Templates

**Kontext:** User definierte 6 lebendige Dateien (task, implementation_plan, walkthrough, decision_log, hard_learned_facts, ideas_future_plans) mit spezifischen Strukturen.

**Entscheidung:** Templates in `templates/lebendige_dateien/` des Skills, ausgefüllte Instanzen in PLAYGROUND-Root für DIESE Session.

**Begründung:** Templates gehören in den Skill (wiederverwendbar). Instanzen gehören in die jeweilige Session (kontext-spezifisch).

**Reversibel?** Ja.

**Konsequenzen:** 6 Templates + 6 Instanzen erstellt. Strukturen sind verbindlich, aber flexibel befüllbar.

---

### 2026-06-07 00:15 — Such-Werkzeug für Reports (Idee)

**Kontext:** Session-Titel lang, Report-Dateinamen evtl. kurz. User brauchte eine Lösung, um Reports nach Inhalt zu finden.

**Entscheidung:** Idee in `ideas_future_plans.md` dokumentiert. Umsetzung als P2-Task mit SubAgent-Auftrag.

**Begründung:** Aktuell lange Dateinamen OK, aber Such-Werkzeug würde Handhabung verbessern.

**Reversibel?** Ja.

**Konsequenzen:** HTML-Tool / Windows-Popup, das YAML-Header + Inhalt durchsucht. Case-insensitive, ignoriert `_`, `-`, Leerzeichen.

---

### 2026-06-07 00:20 — P99 historische Variante, README → INSTRUCTIONS

**Kontext:** Alte Bundles hatten P99_HANDOFF.md als Trigger und README als Doku. User wollte darauf hinweisen, dass die Migration in den Skill passiert ist.

**Entscheidung:** Historischer Hinweis in SKILL.md: "P99-Logik → SKILL.md, README → INSTRUCTIONS.md".

**Begründung:** User-Erwartung: jemand fragt nach "wo ist die P99?" — Hinweis gibt Antwort.

**Reversibel?** Ja.

**Konsequenzen:** SKILL.md hat einen kurzen historischen Marker.

---

### 2026-06-07 00:25 — Kompakt-Spezifität vermerkt

**Kontext:** Aktuell sind die Beispiele KOMPAKT-spezifisch. User sagte: "Im Moment passt es, weil ich mit KOMPAKT arbeite. Merke ich mir, schreib es bitte in den Plan."

**Entscheidung:** Vermerk in INSTRUCTIONS.md Abschnitt 7 (CDS-Kontext), dass Beispiele später bundle-agnostisch formuliert werden müssen.

**Begründung:** User-Vorgabe. Andere Bundles folgen später.

**Reversibel?** Ja.

**Konsequenzen:** Beispiele bleiben vorerst KOMPAKT-spezifisch. Plan dokumentiert, dass Generalisierung später erfolgt.

---

### 2026-06-07 00:30 — Compaction-Fork-Option

**Kontext:** User erwähnte die Option, vor Compaction ein Handover-Bundle zu erstellen und es nach Compaction zu laden.

**Entscheidung:** Dokumentiert in INSTRUCTIONS.md und TOKEN_WINDOW_GUARD.md als Krisen-Option, nicht Standard-Workflow.

**Begründung:** Nützlich in Notsituationen, aber Vorgänger-Session geht verloren. Nur mit Fork sinnvoll.

**Reversibel?** Ja.

**Konsequenzen:** Skill dokumentiert die Option, User kann sie in Extremsituationen wählen.
