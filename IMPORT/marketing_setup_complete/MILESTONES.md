# MILESTONES.md — marketing-setup

## Meilenstein-Übersicht

| Meilenstein | Status | Ziel-Outcome | Blocker | Erfolgskriterium |
|---|---|---|---|---|
| M1: Struktur & Basis | ✅ In Arbeit | Repo-Struktur steht, erste Templates vorhanden | — | Alle Ordner angelegt, min. 5 Templates in `/templates/copy/` |
| M2: Notion-Import | 🔲 Geplant | Alle relevanten Freebies als Markdown im Repo | Manuelle Sichtung nötig | Min. 20 portierte Dokumente in `/research/swipe/` |
| M3: Prompts & LLM-Workflows | 🔲 Geplant | Stabile LLM-Prompts für Copy-Generation | M1 muss abgeschlossen sein | Reproduzierbare Outputs für 3 Copy-Formate |
| M4: n8n-Integration | 🔲 Geplant | Automatischer Sync Linear → Notion-Archiv | n8n-Setup auf Server | Mindestens 1 funktionierender Workflow |
| M5: Erste Kampagne live | 🔲 Geplant | Eine vollständige Kampagne (Brief → Copy → Asset) im Repo | M3 muss abgeschlossen sein | Kampagne deployed, Ergebnisse dokumentiert |

---

## Aktiver Meilenstein: M1 — Struktur & Basis

### Ziel
Ein vollständig strukturiertes Repo mit standardisierten Vorlagen, das ein Agent ohne externe Orientierung benutzen kann.

### Scope
- Alle Ordner gemäß Zielstruktur aus CONTEXT.md anlegen.
- Mindestens 5 Copy-Templates in `/templates/copy/` (E-Mail, LinkedIn, Cold-Outreach, Ad, Landing-Page-Teaser).
- `docs/brand-voice.md` ausfüllen.
- `docs/icp-summary.md` ausfüllen.
- `AGENT_OPERATING_RULES.md` finalisieren.

### Ausgeschlossen aus M1-Scope
- n8n-Integration (das ist M4).
- Vollständige Notion-Portierung (das ist M2).
- Live-Kampagnen (das ist M5).

### Dependencies
- Zugriffsrechte auf Notion-Workspace.
- Linear-Projekt "Marketing" muss existieren und Issues müssen angelegt sein.

### Erfolgskriterien
- [ ] Alle Ordner vorhanden.
- [ ] Min. 5 Templates in `/templates/copy/` als ausfüllbare Markdown-Dateien.
- [ ] `brand-voice.md` enthält: Tonalität, verbotene Formulierungen, Beispielsätze.
- [ ] `icp-summary.md` enthält: Zielbranche, Unternehmensgröße, Entscheiderprofil, Hauptschmerzpunkte.
- [ ] Agent kann Repo öffnen und sofort mit einer Aufgabe beginnen, ohne externe Rückfragen.

### Aktuelle Blocker
- (hier eintragen, wenn vorhanden)

### Verknüpfte Linear Issues
- (Bitte aktuelle Issue-IDs aus Linear eintragen)

---

## Zukünftiger Meilenstein: M2 — Notion-Import

### Ziel
Alle relevanten Notion-Freebies sind als durchsuchbare, strukturierte Markdown-Dateien im Repo verfügbar.

### Scope
- Alle Notion-Freebies sichten und nach Relevanz bewerten (behalten / ablegen / verwerfen).
- Relevante Dokumente als Markdown in `/research/swipe/` mit Metadaten-Header portieren.

### Metadaten-Header-Standard für Swipe-Dateien
```markdown
---
source: [Name des Freebies / Creators]
category: [email | linkedin | seo | framework | strategy | ads]
language: [de | en]
quality: [A | B | C]
imported: [Datum]
linear_issue: [Issue-ID]
---
```

### Erfolgskriterien
- [ ] Min. 20 portierte Dokumente mit vollständigem Metadaten-Header.
- [ ] Alle Dateien nach Kategorie in Unterordnern sortiert.
- [ ] Index-Datei `/research/swipe/INDEX.md` mit Übersicht aller Dokumente.
