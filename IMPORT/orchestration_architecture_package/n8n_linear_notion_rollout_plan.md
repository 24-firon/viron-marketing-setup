# n8n Rollout Plan for Linear and Notion

## Zweck
Diese Datei beschreibt einen bewusst kleinen, robusten n8n-Einstieg, der nicht sofort in eine komplexe Vollsynchronisation kippt.

## Grundprinzip
Nur unidirektionale, nachvollziehbare Flows zuerst. Keine bidirektionale Vollsynchronisation am Anfang.

## Zielreihenfolge
1. Nichts blockieren.
2. Nur wertstiftende Hintergrundautomatisierung hinzufügen.
3. Bruchstellen früh sichtbar halten.
4. Agenten nicht von erfolgreicher Automation abhängig machen.

## Phase A: Noch ohne n8n leben
Bevor n8n integriert wird, muss das operative System schon funktionieren. Das bedeutet:
- Linear-Issues sind nutzbar.
- Notion enthält den Wissenskontext.
- Repo-Dateien tragen den aktuellen Arbeitszustand.

Wenn das nicht funktioniert, löst n8n das Problem nicht, sondern maskiert es nur.

## Phase B: Erster n8n-Workflow

### Workflow 1: Linear Done -> Notion Archive Entry
**Zweck:** Erzeugt automatisch einen sauberen Wissenseintrag, wenn ein Ticket abgeschlossen wurde.

### Trigger
- Linear issue updated
- Filter: Status wechselt auf Done

### Schritte
1. Linear Trigger empfängt Issue-Änderung.
2. Filter prüft, ob neuer Zustand wirklich Done ist.
3. Optional Code-Node oder Set-Node formatiert relevante Felder.
4. Notion Create Page oder Database Item schreibt Archiv-/Logeintrag.
5. Optional Slack/Telegram/Email Benachrichtigung.

### Gespeicherte Felder in Notion
- Linear issue ID
- Titel
- Statuswechselzeitpunkt
- Projekt
- Labels
- assignee
- Zusammenfassung der Arbeit
- Repo-Link
- Commit-/PR-Link falls vorhanden

## Phase C: Zweiter n8n-Workflow

### Workflow 2: Notion Intake -> Linear Draft Issue
**Zweck:** Aus ausgewählten Notion-Einträgen werden gezielt neue Linear-Issues.

### Prinzip
Nur Einträge mit explizitem Freigabefeld erzeugen Tickets. Keine automatische Massenübernahme.

### Schritte
1. Notion Trigger oder Polling auf Datenbank.
2. Filter auf `ready_for_linear = true`.
3. Mapping in Linear Issue Fields.
4. Rückschreiben der erzeugten Issue-ID nach Notion.

## Nicht empfohlen in der Startphase
- bidirektionale Vollsyncs
- automatische Statusrücksynchronisierung in mehrere Richtungen
- aggressive Content-Summarization auf jeder kleinen Änderung
- komplexe Multi-Repo-Verzweigungen
- automatische Änderungen an Repo-Dateien aus n8n heraus

## Warum der Start klein bleiben sollte
Mit jedem zusätzlichen Sync wächst die Zahl möglicher Inkonsistenzen. Der Solo-Operator-Vorteil ist, dass du starke Standards setzen kannst. Nutze das. Lass n8n Buchhaltung übernehmen, nicht Kernlogik.

## MCP-Bezug kritisch betrachtet
n8n MCP verbessert den Umgang mit MCP-Servern, aber die Reife hängt vom Zielsystem und vom konkreten Auth-Flow ab. In Community-Beiträgen war OAuth bei MCP in n8n noch ein Thema, obwohl Support für OAuth2 mit Dynamic Client Registration in Version 1.119.0 genannt wurde. Gleichzeitig berichten Nutzer für Notion-MCP weiter von Workarounds mit permanenten Client-IDs, Refresh-Token-Handling und Token-Injektion. Daraus folgt: MCP ist interessant, aber für deine Startarchitektur nicht als einzige tragende Säule einplanen.

## Minimaler Success Path
- Workflow 1 bauen.
- Einige Done-Issues validieren.
- Feldmapping prüfen.
- Erst dann Workflow 2 ergänzen.

## Kontrollfragen vor Aktivierung
- Ist klar, welches System bei welchem Feld führend ist?
- Ist das Fehlerbild im n8n-Run leicht nachvollziehbar?
- Kann der Agent weiterarbeiten, wenn n8n ausfällt?
- Gibt es nur eine Quelle für den aktuellen Implementierungsstatus?

## Synergien
- Linear erzeugt saubere Abschlussereignisse.
- Notion wächst als archivierte Wissensbasis weiter.
- n8n liefert Sichtbarkeit und Debugbarkeit.
- Repo-Dateien bleiben unabhängig funktionsfähig.
