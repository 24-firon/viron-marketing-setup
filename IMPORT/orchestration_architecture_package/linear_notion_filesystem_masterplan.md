# Linear + Notion + Filesystem Masterplan

## Zweck
Diese Datei definiert eine belastbare Übergangsarchitektur für einen Solo-Entwickler mit mehreren Repositories, mehreren IDEs, LiteLLM-Routing, n8n im Aufbau und bereits aktivem Linear/Notion-Kontext. Der Fokus liegt auf schneller Einsatzfähigkeit, minimalem Integrationsrisiko und maximaler Agenten-Steuerbarkeit.

## Geltungsbereich
Diese Architektur ist bewusst kein monolithisches "alles synchronisiert mit allem"-System. Sie trennt:
- Execution-Tracking in Linear.
- Wissensspeicherung und Langform-Kontext in Notion.
- Agenten-Arbeitskontext im Repository-Dateisystem.
- Spätere optionale Automatisierung in n8n.

## Entscheidungsprinzipien
1. Bestehende aktive Systeme nicht sofort umbauen.
2. Agenten sollen ohne fragile Tool-Ketten arbeitsfähig sein.
3. Neue Integrationen nur dort, wo der Nutzen höher ist als der Wartungsaufwand.
4. Das Repo bleibt der robusteste Kontextträger für Implementierungsarbeit.
5. Linear dient als Ausführungs- und Priorisierungslayer, nicht als vollständiger Wissensspeicher.
6. Notion dient als Wissens-, Recherche- und Referenzlayer, nicht als Primary Source für aktuelle Implementierungszustände.

## Zielbild
Der Agent arbeitet primär aus dem Repository heraus. Vor jedem Task liest er die Steuerdateien im Repo, findet dort die aktive Arbeitslage, springt bei Bedarf in Linear für konkrete Arbeitspakete und in Notion für längere Hintergrunddokumente. Dadurch entsteht ein System, das auch dann weiter funktioniert, wenn n8n noch gar nicht oder nur teilweise eingerichtet ist.

## Kernarchitektur

### Layer 1: Repo als operative Wahrheitsquelle
Jedes aktive Repository erhält standardisierte Steuerdateien:
- `CONTEXT.md`
- `MILESTONES.md`
- `DECISIONS.md`
- optional `SYSTEM_MAP.md`

Diese Dateien beschreiben nur das operative Projektwissen, das ein Agent für Umsetzung und Orientierung braucht.

### Layer 2: Linear als Execution-Layer
Linear wird verwendet für:
- konkrete Aufgaben
- Prioritäten
- Status
- Abhängigkeiten zwischen Arbeitspaketen
- schnelle operative Planung

Linear wird zunächst nicht mit allen Architekturdokumenten überladen. Stattdessen verweist Linear auf Repo-Dateien und Notion-Seiten.

### Layer 3: Notion als Knowledge-Layer
Notion wird verwendet für:
- gesammelte Freebies
- Research
- SOPs
- Marketingwissen
- längere Strategiedokumente
- Sammelstellen für Framework- und Tool-Evaluationen

Notion bleibt zunächst lose gekoppelt, damit die Arbeitsgeschwindigkeit nicht durch Integrationsaufwand sinkt.

### Layer 4: n8n als optionaler Hintergrund-Orchestrator
n8n wird nicht als sofort notwendige Basiskomponente angenommen. Es ist ein späterer Multiplikator für:
- Synchronisationen
- Archivierung
- Trigger-basierte Zusammenfassungen
- Statusübernahmen
- eventuelle Benachrichtigungen

## Warum dieser Ansatz aktuell sinnvoll ist
Du befindest dich im Aufbau. In dieser Phase ist Systemstabilität wichtiger als elegante Vollintegration. Eine vollautomatische Linear-Notion-n8n-Verkettung klingt attraktiv, erzeugt aber früh im Aufbau mehr Fehlersuche als Hebel. Ein Filesystem-first-Ansatz senkt die Komplexität, weil Agenten direkt im Arbeitsraum operieren.

## Arbeitsweise des Agenten

### Standardablauf
1. Repository öffnen.
2. `CONTEXT.md` lesen.
3. `MILESTONES.md` und `DECISIONS.md` prüfen.
4. Aktives Linear-Issue identifizieren.
5. Falls Hintergrundwissen nötig ist, die verlinkte Notion-Seite lesen.
6. Umsetzung durchführen.
7. Repo-Steuerdateien aktualisieren.
8. Commit mit Referenz auf Linear-Issue erstellen.
9. Optional spätere Sync-Mechanismen n8n überlassen.

### Warum nicht nur PM-Tool-Kontext
PM-Tools sind für Menschen gut, aber Agenten brauchen knappe, strukturierte, versionierbare und lokal verfügbare Steuerinformation. Markdown im Repo ist robuster, diffbar und unmittelbar im Arbeitskontext vorhanden.

## Minimaler Strukturstandard pro Repository

### `CONTEXT.md`
- Projektname
- Zweck des Repos
- aktueller Status
- aktive Workstreams
- aktive Linear-Issues
- relevante Notion-Dokumente
- technische Randbedingungen
- bekannte Risiken
- nächster sinnvoller Schritt

### `MILESTONES.md`
- aktuelle Meilensteine
- Zustand je Meilenstein
- Blocker
- Erfolgskriterien

### `DECISIONS.md`
- Architekturentscheidungen
- verworfene Alternativen
- Begründungen
- Folgen für spätere Arbeit

### `SYSTEM_MAP.md` optional
- Services
- Datenflüsse
- Ports
- Datenbanken
- externe Systeme
- Ownership pro Komponente

## Was in Linear gehört
- klar abgegrenzte Aufgaben
- Bugs
- Integrationsschritte
- Prioritäten
- Terminierung
- Statusübergänge
- Teilaufgaben bei konkreter Umsetzung

## Was nicht in Linear gehört
- vollständige Langform-Architekturdokumentation
- unsortierte Research-Sammlungen
- große Prompt-Bibliotheken
- Marketing-Freebie-Archive
- breit angelegte Wissenssammlung ohne unmittelbaren Ausführungsbezug

## Was in Notion gehört
- Sammlungen externer Ressourcen
- Marketing-Playbooks
- SOPs
- längere Vergleichs- und Research-Dokumente
- Wissensarchive
- Strategieseiten

## Verlinkungsregeln
- Jede `CONTEXT.md` enthält die wichtigsten Links nach außen.
- Jedes aktive Linear-Issue verweist zurück auf das Repo und auf die primäre Repo-Steuerdatei.
- Notion-Seiten verlinken nur auf stabile Zielartefakte, nicht auf jede einzelne operative Kleinigkeit.

## Konkreter Rollout in drei Phasen

### Phase 1: Sofort nutzbar, ohne n8n
- Repo-Dateien anlegen.
- Lineare Arbeitsweise standardisieren.
- Notion nur referenzieren.
- Agentenprompt auf Repo-first ausrichten.

### Phase 2: Leichte Automatisierung
- n8n nur für 1 bis 2 robuste Flows einsetzen.
- Beispiel: wenn Issue in Linear auf Done geht, dann Zusammenfassung in Notion-Archiv schreiben.
- Beispiel: aus Notion-Ideen manuell selektierte Tickets in Linear erzeugen.

### Phase 3: Ausbau
- Rücksynchronisationen.
- Periodische Digest-Erstellung.
- Eventuelle Slack/Telegram/Email Benachrichtigungen.
- KPI-Ansichten.

## Risiken
| Risiko | Beschreibung | Gegenmaßnahme |
|---|---|---|
| Tool-Sprawl | Zu viele Systeme gleichzeitig | Repo-first, n8n später |
| Fragile Syncs | Bidirektionale Automatisierungen brechen leicht | Erst unidirektional beginnen |
| Kontextzerfall | Wissen verteilt sich unkontrolliert | Pflichtstruktur je Repo |
| Agent drift | Agent schreibt in falsche Systeme | Harte Operating Procedure |
| Review-Aufwand | Zu viel Blindflug bei Code-only Automation | Sichtbare Steuerdateien und visuelle Tools nur gezielt |

## Synergiepotenziale
- Linear bleibt sofort produktiv für operative Arbeit.
- Notion verliert nicht seinen Wert als Wissensspeicher.
- Repo-Dateien machen Agentenführung präziser und auditierbar.
- n8n kann später schrittweise Mehrwert liefern, ohne Basissystem zu blockieren.
- Eine spätere Migration zu Plane bleibt möglich, weil die Logik nicht hart in n8n codiert wird.

## Entscheidung
Für die nächsten Tage und Wochen ist dieser Ansatz der risikoärmste und zugleich skalierbarste Weg. Er bewahrt bestehende aktive Arbeitsabläufe, reduziert die Einrichtungszeit und schafft eine klare Vorstufe für eine spätere Plane-Evaluation.
