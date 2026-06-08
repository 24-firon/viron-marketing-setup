# ideas_future_plans.md — Ideen und Zukunftspläne

## Status-Legende

- 🔴 **HEUTE** — Idee, die in der aktuellen Session umgesetzt werden könnte
- 🟡 **NÄCHSTE SESSION** — Idee für V2 / V[N+1]
- 🟢 **SPÄTER** — Idee für zukünftige Sessions
- ⚪ **ARCHIV** — Idee, die verworfen oder auf unbestimmte Zeit verschoben wurde

---

### 2026-06-07 — Such-Werkzeug für Reports

**Status:** 🟡 NÄCHSTE SESSION (V2)

**Idee:** HTML-Tool / Windows-Popup, das Reports nach Session-Titel im INHALT durchsucht (YAML-Header, Überschriften). Erlaubt kurze Report-Dateinamen bei langen Session-Titeln.

**Warum relevant?** Aktuell sind Report-Dateinamen unhandlich lang, weil sie als Such-Schlüssel dienen. Mit Inhalts-Suche wären kurze Namen möglich.

**Aufwand:** 4-8 Stunden (SubAgent-Auftrag)

**Voraussetzungen:**
- Reports haben YAML-Header mit `session_title` (gegeben)
- Reports liegen an konsistenten Pfaden (gegeben)
- SubAgent-Skill für Tool-Entwicklung vorhanden (zu prüfen)

**Mögliche Umsetzung:**
- SubAgent (General Agent) spawnt → Tool in Python oder HTML+JS
- Smart-Search: case-insensitive, ignoriert `_`, `-`, Leerzeichen
- Optional: Windows-Popup-Integration via PowerShell
- Eingabefeld: Session-Titel (z.B. `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN`)
- Trefferliste mit Pfad + Snippet (erste 200 Zeichen)

---

### 2026-06-07 — Bundle-Migration: flach → KOPIERPAKET/REPORT_GEN

**Status:** 🟡 NÄCHSTE SESSION (V2)

**Idee:** 18 Dateien aus flacher BUNDLE_KOMPAKT-Struktur in `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/{KOPIERPAKET,REPORT_GEN,reports}/` migrieren.

**Warum relevant?** Routing-Matrix im Skill verweist auf diese Struktur. Ohne Migration funktionieren die Pfade nicht.

**Aufwand:** 2-4 Stunden (SubAgent-Auftrag)

**Voraussetzungen:**
- Originale bleiben als Vorlage in `BUNDLE_KOMPAKT/` (User-Vorgabe)
- SubAgent-Auftrag mit klarer SCOPE-Definition (nur verschieben, nicht editieren)
- STOPP-Punkte nach jeder Phase

**Mögliche Umsetzung:**
- General Agent verschiebt Dateien
- P00-P02 + 11 Templates → `KOPIERPAKET/`
- REPORT_GENERATOR + zukünftige → `REPORT_GEN/`
- `additional/` für SubAgent-Prompts
- Verifikation: `ls STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` zeigt neue Struktur

---

### 2026-06-07 — BUNDLE_VOLLSTAENDIG analog anpassen

**Status:** 🟢 SPÄTER (V3 oder V4)

**Idee:** Gleiche Skill-Struktur für VOLLSTÄNDIG-Bundle (100-300 Zeilen Templates, komplexer).

**Warum relevant?** VOLLSTÄNDIG ist das "Enterprise"-Bundle. User will es später haben.

**Aufwand:** 8-16 Stunden (mehrere SubAgents)

**Voraussetzungen:**
- KOMPAKT-Version ist stabil + User-getestet
- VOLLSTÄNDIG-Bundle ist analysiert (Unterschiede zu KOMPAKT verstanden)
- Templates aus BUNDLE_VOLLSTAENDIG/ als Vorlage vorhanden

**Mögliche Umsetzung:**
- General Agent: Templates aus BUNDLE_VOLLSTAENDIG/ in `STORAGE/.../BUNDLE_VOLLSTAENDIG/{KOPIERPAKET,REPORT_GEN}/` migrieren
- Skill-Struktur: Multi-Bundle-Skill (ein Skill-Ordner, mehrere Bundle-Profile)
- Beispiele bundle-agnostisch formulieren (siehe Kompakt-Spezifität-Vermerk)

---

### 2026-06-07 — BUNDLE_SLIM analog anpassen

**Status:** 🟢 SPÄTER (V3 oder V4)

**Idee:** Minimalversion mit 7-22 Zeilen Templates. Für token-arme Modelle und Quick-Reference.

**Warum relevant?** SLIM ist die "Quick-Reference" für Edge-Cases. User will es später haben.

**Aufwand:** 4-8 Stunden

**Voraussetzungen:**
- KOMPAKT-Version stabil
- SLIM-Bundle analysiert (welche Dateien sind in SLIM enthalten?)

**Mögliche Umsetzung:**
- General Agent: Reduzierte Templates (jede Datei 7-22 Z.)
- notfall-Variante: minimal (P99 + HANDOVER + REPORT in je 1 Datei)
- Eigener Skill-Ordner ODER Multi-Bundle-Skill mit Profil-Auswahl

---

### 2026-06-07 — BUNDLE_MYCHOICE analog anpassen

**Status:** 🟢 SPÄTER

**Idee:** Custom-Bundle, vom User konfigurierbar. Eigene Templates als Bausteine.

**Warum relevant?** MYCHOICE ist die "individuelle" Variante. User will sie später.

**Aufwand:** 8-16 Stunden (Custom-Logik komplex)

**Voraussetzungen:**
- KOMPAKT + VOLLSTÄNDIG + SLIM existieren
- User-Wahl-Logik im Vordergrund

**Mögliche Umsetzung:**
- General Agent: Templates als Bausteine
- User wählt pro Element: ja/nein/wie
- Skill mit Custom-Builder-Logik

---

### 2026-06-07 — KOMPAKT-Definition formalisieren

**Status:** 🟡 NÄCHSTE SESSION (V2)

**Idee:** Klare, formale Definition, was KOMPAKT von VOLLSTÄNDIG/SLIM/MYCHOICE unterscheidet.

**Warum relevant?** Ohne Definition sind die Beispiele "KOMPAKT-spezifisch" ohne klaren Grund. Spätere Bundle-Adaptionen brauchen die Definition.

**Aufwand:** 1-2 Stunden (User + Agent gemeinsam)

**Mögliche Definition:**
- KOMPAKT: 30-80 Zeilen Templates, Standard-Sessions, mittel-komplex
- VOLLSTÄNDIG: 100-300 Zeilen, Enterprise, komplex
- SLIM: 7-22 Zeilen, Quick-Reference, minimal
- MYCHOICE: User-definiert, variabel

**Festzulegen durch:** User (basierend auf tatsächlichem Use)

---

### 2026-06-07 — SubAgent-Prompts in additional/ ausarbeiten

**Status:** 🟢 SPÄTER

**Idee:** `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/KOPIERPAKET/additional/` mit echten SubAgent-Prompts befüllen.

**Warum relevant?** Aktuell sind nur TASK_ENVELOPE, OPERATOR_WORKFLOW, ORCHESTRATOR_WORKFLOW in KOPIERPAKET/. Weitere SubAgent-Prompts fehlen (z.B. für spezifische Tasks).

**Aufwand:** 4-8 Stunden (User-Beispiele aus anderen Repos extrahieren)

**Voraussetzungen:**
- KOPIERPAKET/additional/ existiert (kommt mit Bundle-Migration)
- User hat Beispiele in anderen Repos

**Mögliche Umsetzung:**
- General Agent: User-Repos nach SubAgent-Prompts scannen
- Extrahieren, ggf. anonymisieren
- In `additional/` ablegen
- DoD: Mindestens 3 weitere SubAgent-Prompts vorhanden

---

### 2026-06-07 — Token-Drop-Test in echtem Compaction

**Status:** 🟢 SPÄTER (P3)

**Idee:** Test-Session, die Token-Budget bewusst in Schwarz treibt und Notfall-Protokoll validiert.

**Warum relevant?** Notfall-Protokoll ist theoretisch. Echte Validierung braucht reales Compaction.

**Aufwand:** 2-4 Stunden (Test-Session)

**Voraussetzungen:**
- Große Dateien zum Laden (z.B. mehrere Bundles gleichzeitig)
- Bereitschaft, eine Session "zu opfern"

**Mögliche Umsetzung:**
- General Agent: Test-Session mit progressiver Token-Belastung
- Beobachten: Wann greift Notfall? Wie verhält sich der Agent?
- Lessons Learned dokumentieren

---

### 2026-06-07 — Konsolidierungs-Zyklus für LDFs

**Status:** 🟢 SPÄTER (regelmäßig, alle 5-10 Sessions)

**Idee:** Regelmäßig durchgehen: welche Einträge in decision_log, hard_learned_facts, ideas haben sich zu Regeln/Skills verfestigt?

**Warum relevant?** Lebendige Dateien sind Rohmaterial. Ohne Konsolidierung wachsen sie unendlich.

**Aufwand:** 1-2 Stunden pro Zyklus

**Voraussetzungen:**
- Mehrere abgeschlossene Sessions
- LDFs mit erkennbaren Mustern

**Mögliche Umsetzung:**
- User-Review: Welche Erkenntnisse sind regel-würdig?
- General Agent: Entwurf der Regel/des Skills
- Integration in `.opencode/rules/` oder `.opencode/skills/`

---

### 2026-06-07 — Multi-Bundle-Skill-Konzept

**Status:** ⚪ ARCHIV (vorerst verworfen, später ggf. wieder aufgegriffen)

**Idee:** Ein einziger Skill-Ordner, der ALLE Bundles unterstützt. User wählt Bundle-Profil zur Laufzeit.

**Warum archiviert?** Aktuell sind die Bundles sehr unterschiedlich (Größe, Tiefe, Inhalt). Ein Multi-Bundle-Skill wäre zu komplex für den Anfang. Erst wenn 2-3 Bundles stabil sind, lohnt sich die Konsolidierung.

**Mögliche spätere Umsetzung:**
- `session_handover_generator/` mit Bundle-Profil-Auswahl
- Profile: `kompakt.json`, `vollstaendig.json`, `slim.json`
- Skill lädt Profil basierend auf Q-A-Antwort

---

## Konsolidierungs-Hinweis

> Decision Log, Hard-Learned Facts, Ideas werden gesammelt und später in Regeln, Task-Dateien, Skills und ähnliches konsolidiert.
>
> **Konsolidierungs-Zyklus:** alle 5-10 Sessions durchgehen und prüfen, welche Einträge sich zu Regeln/Skills verfestigt haben.
>
> **Beispiel-Pfad:**
> 1. `hard_learned_facts.md` enthält "LLM schätzt Tokens 50-100% zu niedrig"
> 2. Erkenntnis wiederholt sich in mehreren Sessions
> 3. Wird zu `.opencode/rules/00_token_estimation.md` als Regel
> 4. Aus `hard_learned_facts.md` wird auf die Regel verwiesen
