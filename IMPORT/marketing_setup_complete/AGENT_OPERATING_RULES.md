# AGENT_OPERATING_RULES.md — marketing-setup

## Zweck
Diese Datei ist die verbindliche Betriebsanweisung für jeden KI-Agenten, der in diesem Repository arbeitet. Sie gilt unabhängig davon, welches Modell, welche IDE oder welches Framework verwendet wird.

---

## Pflicht-Ablauf bei jeder Arbeitssitzung

### Schritt 1: Kontext laden
1. `CONTEXT.md` vollständig lesen.
2. `MILESTONES.md` prüfen — welcher Meilenstein ist aktiv?
3. `DECISIONS.md` prüfen — gibt es bereits eine Entscheidung zur aktuellen Aufgabe?
4. Aktives Linear-Issue aus CONTEXT.md identifizieren.
5. Falls Hintergrundwissen nötig: verlinktes Notion-Dokument oder `/research/swipe/` konsultieren.

### Schritt 2: Aufgabe ausführen
- Im Scope des aktiven Meilensteins bleiben.
- Bestehende Entscheidungen aus DECISIONS.md respektieren.
- Keine neuen Architekturentscheidungen treffen, ohne einen ADR-Eintrag in DECISIONS.md zu erstellen.

### Schritt 3: State aktualisieren
1. `CONTEXT.md` → "Active work" und "Last completed items" aktualisieren.
2. `MILESTONES.md` → Checkbox des abgeschlossenen Tasks setzen.
3. Commit mit Referenz auf Linear Issue ID erstellen (z.B. `feat(copy): add cold-outreach template [MAR-14]`).

---

## Systemgrenzen
- **Du schreibst NICHT direkt in Notion.** Nur n8n übernimmt Notion-Syncs im Hintergrund.
- **Du brichst NICHT den LiteLLM-Router.** Alle LLM-Calls gehen über den Proxy-Endpoint.
- **Du verlässt NICHT den Repo-Scope.** Keine Änderungen in anderen Repos ohne explizite Anweisung.
- **Du kopierst NICHT ungeprüfte Notion-Freebies direkt als Output.** Freebies sind Rohmaterial, kein fertiges Produkt.

---

## Output-Standards
- Sprache: Deutsch für DACH-Content, Englisch für technische Doku.
- Ton: Professionell, direkt, keine Bullshit-Formulierungen. Zielgruppe sind technisch versierte Entscheider.
- Copy-Länge: Kürzer ist besser. Wenn eine Aussage in einem Satz gemacht werden kann, nicht drei Sätze schreiben.
- Dateinamen: lowercase-kebab-case, beschreibend (z.B. `kaltakquise-email-it-dienstleister.md`).

---

## Fehlerverhalten
- Wenn CONTEXT.md nicht vorhanden ist: STOP, Datei anlegen, dann weitermachen.
- Wenn n8n-Sync fehlt: manuell in CONTEXT.md dokumentieren, weitermachen.
- Wenn Linear-Issue unklar ist: in CONTEXT.md markieren als `⚠️ NEEDS_CLARIFICATION`, nicht raten.
- Wenn Notion-Freebie-Qualität unklar ist: Quality-Flag im Metadaten-Header auf `C` setzen, weiterarbeiten.
