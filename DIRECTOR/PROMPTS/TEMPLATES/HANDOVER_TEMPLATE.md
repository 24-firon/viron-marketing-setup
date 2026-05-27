# HANDOVER — SESSION ABSCHLUSS & ÜBERGABE

> **BLUF (Bottom Line Up Front):** [Ein Satz: Was wurde in dieser Session erreicht?]

---

## 1. ABGESCHLOSSENE BATCHES (Was wurde getan)

| Batch | Status | Beschreibung |
|:------|:------:|:-------------|
| P0.1 | ✅ | [Kurzbeschreibung] |
| P0.2 | ✅ | [Kurzbeschreibung] |
| P0.3 | ✅ | [Kurzbeschreibung] |
| ... | ... | ... |

---

## 2. OFFENE TASKS & KNOWN ERRORS

| Task | Priorität | Status | Beschreibung | Nächster Schritt |
|:-----|:---------:|:------:|:-------------|:-----------------|
| [Task] | P0 🔴 | OFFEN | [Beschreibung] | [Nächster Aktionsschritt] |
| [Task] | P1 🟡 | OFFEN | [Beschreibung] | [Nächster Aktionsschritt] |
| [Bug] | P1 🟡 | BEKANNT | [Bug-Beschreibung & Workaround] | [Fix-Plan] |

---

## 3. ZUSTAND DER DATEIEN (Dateibaum)

Nur geänderte/erstellte Dateien auflisten:

```
DIRECTOR/Prompts/Templates/
├── P00_BOOTSTRAP.md              [NEU] — Kognitiver Stresstest
├── P01_SESSION_INIT.md           [NEU] — Session-Init-Template
├── HANDOVER_TEMPLATE.md           [NEU] — Dieses Template
├── P02_HANDOFF.md                [GEPLANT]
├── P03_RESERVED.md               [GEPLANT]
├── IMPLEMENTATION_PLAN_TEMPLATE.md [GEPLANT]
└── TASK_ENVELOPE_TEMPLATE.md     [GEPLANT]
```

---

## 4. NÄCHSTE SCHRITTE (Für den nächsten Agenten)

1. **[Schritt 1]** — [Konkrete Aktion, inkl. Pfad und Befehl]
2. **[Schritt 2]** — [Konkrete Aktion]
3. **[Schritt 3]** — [Konkrete Aktion]

---

## 5. P00-VERIFIKATION (Kontextprüfung für den nächsten Agenten)

Der nächste Agent muss diese Kernfragen korrekt beantworten, bevor er weiterarbeitet:

1. **Was ist das 2-Prompt-System?** P00 = Kognitiver Stresstest (I/O-Lock, READ-ONLY). P01 = Execution (nach Director-Freigabe). NIE P01 vor P00.
2. **Archive-First:** Bevor etwas gelöscht wird, kommt es ins ARCHIVE. Keine Löschung ohne Operator-Freigabe.
3. **Semantische Links:** `[[Konzept]]` statt `[[datei.md]]` — konzept-basiert, umzugsfest.
4. **Copy-Ketten:** Windows " - Copy"-Suffixe sind eigenständige Session-Versionen, keine Duplikate.
5. **Stopp-Pflicht:** Nach jedem P0.x Meilenstein stoppen, Bericht erstatten, auf GO warten.

---

> **Session sauber abgeschlossen. Alle Artefakte gesichert, Workspace ist clean.** Warte auf nächsten Director-Auftrag.
