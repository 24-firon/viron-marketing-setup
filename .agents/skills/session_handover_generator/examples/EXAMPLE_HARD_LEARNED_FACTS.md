# hard_learned_facts.md — Chronologische Erkenntnisse dieser Session

---

### 2026-06-07 23:30 — CDS-Konvention: STORAGE im Root

**Was ist passiert?** Beim Versuch, STORAGE-Pfade zu definieren, hatte ich sie zuerst im Skill-Ordner.

**Was war die Erkenntnis?** STORAGE liegt im Root jedes Repos (CDS-Konvention). Skill liegt SEPARAT.

**Warum war das wichtig?** Verwechslung hätte dazu geführt, dass Templates im Skill statt im Repo-Root liegen. Andere Repos hätten dann keinen Zugriff.

**Anwendung in Zukunft:** STORAGE-Pfade immer als `[REPO-ROOT]/STORAGE/...` schreiben, nicht relativ zum Skill.

---

### 2026-06-07 23:35 — 4-Pfeiler-Formel: examples/ ist PFLICHT

**Was ist passiert?** Ich hatte zunächst `examples/` nicht explizit im Plan.

**Was war die Erkenntnis?** "Wenn du einen Skill erstellst und den examples/-Ordner vergisst, hast du komplett versagt." (4-Pfeiler-Formel)

**Warum war das wichtig?** Ohne examples/ kann der Agent nicht prüfen, ob sein Output der "Definition of Done" entspricht. Quality-Drift.

**Anwendung in Zukunft:** JEDER Skill braucht `examples/` als DoD-Referenz. Sofort mitplanen, nicht nachreichen.

---

### 2026-06-07 23:40 — SubAgent-Prompts sind echte Files

**Was ist passiert?** Ich hatte SubAgent-Prompts als "Platzhalter" bezeichnet.

**Was war die Erkenntnis?** TASK_ENVELOPE, OPERATOR_WORKFLOW, ORCHESTRATOR_WORKFLOW existieren bereits in STORAGE als echte Templates.

**Warum war das wichtig?** Falsche Annahme hätte zu unnötigen Platzhaltern geführt, statt vorhandene Dateien zu nutzen.

**Anwendung in Zukunft:** Vor jeder "Platzhalter"-Annahme prüfen, ob die Datei schon existiert.

---

### 2026-06-07 23:45 — LLM schätzt Tokens 50-100% zu niedrig

**Was ist passiert?** User wies explizit darauf hin, dass LLM-Schätzungen systematisch zu niedrig sind.

**Was war die Erkenntnis?** 50KB Datei → LLM sagt 10-15K, real 20-25K Tokens.

**Warum war das wichtig?** Ohne diese Erkenntnis hätte ich Token-Budgets ständig überschätzt und in Compaction geraten.

**Anwendung in Zukunft:** Immer konservativ planen mit +50% Aufschlag. Token-Frage als ERSTE Aktion (HD-0).

---

### 2026-06-07 23:50 — Skill-Trigger: YAML-Header, nicht Datei-Inhalt

**Was ist passiert?** User sagte: "Wenn man die Skill-Trigger-Bedingungen in die Instructions legt, dann ist es ein bisschen zu spät."

**Was war die Erkenntnis?** Trigger-Bedingungen MÜSSEN in den YAML-Header, nicht in INSTRUCTIONS.md.

**Warum war das wichtig?** YAML-Header ist der einzige Teil, der IMMER im Context ist. INSTRUCTIONS.md wird nur geladen, wenn der Skill bereits triggert — zu spät für die Trigger-Entscheidung.

**Anwendung in Zukunft:** Trigger-Keywords, Zeilen-Anzahl-Hinweis und Use-Cases in YAML-Header. INSTRUCTIONS.md für Workflow-Details.

---

### 2026-06-07 23:55 — Lebendige Dateien NICHT als Bonus, sondern Pflicht

**Was ist passiert?** User kritisierte, dass ich die Task-Dateien für meine eigene Arbeit NICHT erstellt hatte.

**Was war die Erkenntnis?** "Deine Aufgabe war als Erstes einen Implementation-Plan zu schreiben" — ich hatte es mehrfach ERWÄHNT aber nie GEMACHT.

**Warum war das wichtig?** Ohne lebendige Dateien verliert die Session-Architektur ihren eigenen SSoT. Inkonsistenz zwischen Plan und Ausführung.

**Anwendung in Zukunft:** Bei jeder Session mit mehreren Sub-Tasks: SOFORT task.md + implementation_plan.md erstellen, BEVOR ich mit der Arbeit beginne.

---

### 2026-06-07 00:00 — notfall/ ist BACKUP, nicht Standard

**Was ist passiert?** User erwähnte die Idee eines "Notfall-Bundle für Code Black".

**Was war die Erkenntnis?** Es soll nicht die "krass reduzierte Notfall-Version" sein, sondern eine "Standard-mäßige, mittelmäßige Version, die auch als Notfall-Backup vorhanden ist".

**Warum war das wichtig?** "Krass reduziert" hätte bedeutet: 2-Zeilen-Skelett, kaum nutzbar. "Mittelmäßig" bedeutet: funktional, aber nicht perfekt — als Backup OK.

**Anwendung in Zukunft:** Backup-Varianten sollten "funktional OK" sein, nicht "minimal funktional".

---

### 2026-06-07 00:05 — Compaction-Fork-Option: Nützlich, aber riskant

**Was ist passiert?** User erklärte die Option, vor Compaction ein Bundle zu erstellen und nach Compaction zu laden.

**Was war die Erkenntnis?** Nützlich in Krisen, aber Vorgänger-Session geht verloren. Nur mit Fork (parallele Session) sinnvoll.

**Warum war das wichtig?** Ohne Fork ist der Kontext-Verlust zu groß. Mit Fork bleibt der Kontakt erhalten.

**Anwendung in Zukunft:** Compaction-Fork-Option als Krisen-Werkzeug dokumentieren, nicht als Standard-Workflow empfehlen.

---

### 2026-06-07 00:10 — 6 lebendige Dateien = 1 Skill-Pflicht + 5 Hygiene

**Was ist passiert?** User definierte 6 lebendige Dateien (task, implementation_plan, walkthrough, decision_log, hard_learned_facts, ideas_future_plans).

**Was war die Erkenntnis?** Diese 6 sind NICHT optional. task.md + implementation_plan.md sind Pflicht für jede Multi-Task-Session. Die anderen 4 sind Hygiene für Session-Kontinuität.

**Warum war das wichtig?** "Erst planen, dann arbeiten" ist die Grundregel. task.md zwingt zur Atomisierung, implementation_plan.md zwingt zur Linearisierung.

**Anwendung in Zukunft:** Bei JEDER Session mit > 3 Schritten: task.md + implementation_plan.md ZUERST. Andere 4 nach Bedarf.

---

### 2026-06-07 00:15 — Konsolidierung von LDFs in Regeln/Skills

**Was ist passiert?** User erwähnte: "Decision Log, Hard Learned Facts, Ideas und ähnliches werden gesammelt und später in Regeln, Task-Dateien, Skills und ähnliches konsolidiert."

**Was war die Erkenntnis?** Lebendige Dateien sind KEIN Endprodukt, sondern Rohmaterial für SSoT-Verfestigung. Alle 5-10 Sessions durchgehen und prüfen, was zu Regeln/Skills geworden ist.

**Warum war das wichtig?** Ohne Konsolidierung wachsen die lebendigen Dateien unendlich. Mit Konsolidierung entstehen aus Erfahrungen stabile Regeln.

**Anwendung in Zukunft:** Konsolidierungs-Zyklus einplanen. Nicht jede Erkenntnis bleibt ewig in hard_learned_facts.md.

---

### 2026-06-07 00:20 — "Kompakt-Spezifisch" noch nicht definiert

**Was ist passiert?** User fragte: "Kompaktspezifisch, wie meinst du das genau, was unterscheidet Kompakt von anderen?"

**Was war die Erkenntnis?** Ich habe keine klare Definition, was KOMPAKT von VOLLSTÄNDIG/SLIM/MYCHOICE unterscheidet. Die Beispiele sind KOMPAKT-spezifisch formuliert, ohne dass ich den Unterschied klar gemacht habe.

**Warum war das wichtig?** Beim späteren Adaptieren auf andere Bundles müssen die Beispiele ggf. generalisiert werden. Aber ohne klare KOMPAKT-Definition ist das schwierig.

**Anwendung in Zukunft:** KOMPAKT-Definition in implementation_plan.md ergänzen. Beispiele ggf. mit "[KOMPAKT-spezifisch]" markieren, damit klar ist, was bundle-agnostisch ist.
