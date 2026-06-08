# storage/ — Verweis auf globales STORAGE

> **Wichtig:** Dieser `storage/`-Ordner im Skill ist NICHT das operative Storage. Er enthält nur diesen Verweis.

## Globales STORAGE-Verzeichnis

Das operative `STORAGE/`-Verzeichnis liegt im **Root jedes Repos** und folgt der CDS-Konvention:

```
[REPO-ROOT]/
├── STORAGE/
│   └── TEMPLATES/
│       ├── BUNDLE_KOMPAKT/
│       │   ├── TEMPLATES/        ← Templates zum Kopieren
│       │   ├── PROMPTS/         ← Report-/Research-Prompts
│       │   └── reports/            ← dauerhafte Berichte
│       ├── BUNDLE_VOLLSTAENDIG/    (zukünftig)
│       ├── BUNDLE_SLIM/            (zukünftig)
│       └── BUNDLE_MYCHOICE/        (zukünftig)
├── HANDOVER/
│   └── TASK_[SESSION]_V[N]/        ← temporär, pro Session
├── REPORTS/                        ← dauerhaft, repo-weit
└── _ARCHIVE/                       ← Gesetz 2: Archive-First
```

## Warum diese Trennung?

- **Skill (session_handover_generator):** Enthält die **systemische Logik** (Router, Hard Directives, Token-Guard, Wer-macht-was). Liegt NICHT in STORAGE, weil Logik ≠ Template.
- **STORAGE (global):** Enthält die **allgemein gültigen Templates und Prompts** (P00, P01, P02, PROMPTSERATOR, HANDOVER.md-Template). Liegt im Root, weil jedes Repo dieselbe Struktur braucht.

## Wie Skill auf STORAGE verweist

Im SKILL.md (Routing-Matrix) zeigt jede Phase auf einen Pfad im globalen STORAGE. Beispiel:

| Phase | Datei |
|:---|:---|
| Session-Start (Stress-Test) | `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/P00_BOOTSTRAP.md` |
| Forensischer Bericht | `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/PROMPTS/FORENSIC_PROMPTSERATOR.md` |
| Handover-Output | `HANDOVER/TASK_[SESSION]_V[N]/HANDOVER.md` |

## Bundle-Status (Juni 2026)

| Bundle | Status |
|:---|:---|
| **KOMPAKT** | ✅ Initial — diese Session |
| VOLLSTÄNDIG | 🟡 Später (P1 in Handover) |
| SLIM | ⚪ Später (P2) |
| MYCHOICE | ⚪ Später (P2) |

## Pflege

- **STORAGE/ ändert sich nur wenn:** Templates geändert werden oder neue Bundles dazukommen
- **Skill/ ändert sich nur wenn:** System-Logik sich ändert (neue Modi, neue Hard Directives, etc.)
- **Reports/ wächst kontinuierlich** mit jeder Session (Konservierungs-Gesetz 3)
