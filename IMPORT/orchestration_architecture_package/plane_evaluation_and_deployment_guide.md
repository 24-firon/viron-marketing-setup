# Plane Evaluation and Deployment Guide

## Zweck
Diese Datei ist die ausführliche Bewertungs- und Einführungsgrundlage für Plane im Kontext einer Solo-Entwickler-Arbeitsumgebung mit laufendem Serveraufbau, Postgres, Workern, Agentenframeworks, n8n und mehreren Repositories.

## Executive framing
Plane ist nicht einfach nur ein weiteres PM-Tool. Es kombiniert Work Management mit integrierten Pages/Wiki-Funktionen und bietet zusätzlich einen offiziellen MCP-Server. Das macht Plane potenziell attraktiv für agentenfreundliche Arbeitsweisen. Gleichzeitig bedeutet Self-Hosting nicht "ein Container und fertig", sondern zusätzliche Infrastrukturabhängigkeiten, die sauber bewertet werden müssen.

## Was Plane strukturell ist
Plane stellt mehrere Ebenen bereit:
- Workspace-Ebene.
- Workspace-Wiki.
- Projekte.
- Projekt-Pages.
- Work Items.
- Cycles.
- Modules.
- Milestones.
- Initiatives.
- Intake.

Wichtig ist dabei: Nicht alles muss aktiviert sein. Laut Plane-Wiki sind Features standardmäßig aus und können bei Bedarf eingeschaltet werden. Das ist für Solo-Setups relevant, weil du die Komplexität klein halten kannst.

## Warum Plane für Agenten interessant ist
Plane bietet einen offiziellen MCP-Server und dokumentiert mehrere Transportmodi:
- HTTP mit OAuth.
- HTTP mit PAT Token.
- Local stdio.
- SSE legacy.

Außerdem wird dokumentiert, dass der MCP-Server über 100 Tools in 20 Modulen bereitstellt. Für Agenten bedeutet das: Sie können Projekte, Work Items, Cycles, Pages und weitere Plane-Objekte standardisiert ansprechen, statt nur über rohe API-Skripte zu arbeiten.

## Kritische Realität hinter dem AI-Vorteil
Der MCP-Vorteil ist real, aber nur dann praktisch relevant, wenn:
- Auth sauber funktioniert.
- das Zielsystem stabil erreichbar ist.
- der Arbeitsstil wirklich Plane-zentriert aufgebaut ist.
- du nicht parallel zu viele konkurrierende Truth-Sources pflegst.

Plane ersetzt also nicht automatisch die Notwendigkeit klarer Repo-Kontexte. Auch mit Plane profitieren Agenten davon, wenn das Repo eine knappe operative Steuerdatei enthält.

## Plane-Komponenten im konkreten Arbeitsmodell

### Workspace
Der globale Container für dein Gesamtsetup.

### Workspace Wiki
Geeignet für:
- globale Standards
- SOPs
- Infrastrukturübersichten
- gemeinsame Referenzdokumente
- unternehmensweite oder systemweite Wissenseinträge

### Projects
Sinnvoll nach Repo oder Produktdomäne zu schneiden, nicht nach jeder Kleinigkeit.
Beispiele:
- marketing
- orchestration
- backend-core
- workers
- agent-runtime

### Project Pages
Diese sind für projektspezifische Specs und Umsetzungspläne sinnvoll. Das ist einer der stärksten Unterschiede zu Linear, weil Dokumentation enger am Projekt hängt.

### Work Items
Die operative Einheit für Aufgaben, Bugs, Features, Chores oder Epics.

### Cycles
Sprints oder Zeitfenster. Für Solo-Arbeit nur aktivieren, wenn du wirklich timeboxed planst.

### Modules
Thematische Bündelung. Besonders nützlich, wenn mehrere Work Items zu einer größeren Funktion oder Integrationswelle gehören.

### Initiatives
Workspace-weite strategische Ziele über mehrere Projekte hinweg.

### Intake
Praktisch, wenn du viele lose Eingänge hast und nicht jeden Input sofort in die operative Liste kippen willst.

## Offizielle Self-Hosting-Abhängigkeiten kritisch validiert
Für Coolify dokumentiert Plane explizit:
- `coolify-compose.yml` aus dem Release beziehen.
- Version `v1.8.2` oder höher.
- Externe `DATABASE_URL`.
- Externe `REDIS_URL`.
- Externe `AMQP_URL` für RabbitMQ.

Das ist die zentrale Korrektur gegenüber vereinfachten Darstellungen: Für eine belastbare Produktionsbewertung ist Plane nicht nur Postgres + Web-App. Offiziell werden zusätzlich Redis und RabbitMQ als erforderliche Umgebungsvariablen im Coolify-Setup genannt.

## Konsequenzen für dein laufendes Server-Setup
Wenn du bereits ein laufendes Postgres-System hast, hilft das, aber reicht nicht allein. Du musst zusätzlich entscheiden:
- Wo läuft Redis?
- Wo läuft RabbitMQ?
- Wie werden Backups gehandhabt?
- Welche Domain/Subdomain bekommt Plane?
- Gibt es Object Storage für Attachments und spätere Dateinutzung?
- Wie trennt sich interner von öffentlichem Zugriff?

## Aufwandseinschätzung ehrlich

### Niedriger Aufwand, wenn bereits vorhanden
- Coolify ist vorhanden.
- Externe Postgres-Instanz ist vorhanden.
- Redis ist vorhanden.
- RabbitMQ ist vorhanden oder schnell bereitstellbar.
- Domainrouting ist Routine.

### Mittlerer bis hoher Aufwand, wenn noch nicht vorhanden
- RabbitMQ neu einführen.
- Redis neu einführen.
- Storage-Konzept festlegen.
- Backup-Konzept anpassen.
- MCP-Zugriffskonzept für IDEs standardisieren.

## Plane als Architekturfit für deine Umgebung

### Gute Fit-Signale
- Du willst Open Source perspektivisch.
- Du willst Projekte und Doku näher zusammenführen.
- Du willst MCP-fähige agentische Nutzung.
- Du baust vieles gerade neu auf.
- Du kannst einen Agenten ein klaren Rollout-Plan abarbeiten lassen.

### Schlechte Fit-Signale
- Du brauchst in den nächsten 48 Stunden sofort stabile Output-Produktion.
- Du willst keinerlei zusätzliche Infra-Komponenten einführen.
- Du möchtest kein neues Arbeitsmodell lernen.
- Du hast gerade keine Zeit für Evaluations- und Verifikationsschleifen.

## Empfohlenes Evaluationsmodell
Plane nicht sofort als Vollersatz einführen, sondern als kontrollierte Parallelspur.

### Stufe 1
- Plane deployen.
- Nur ein bis zwei interne Projekte anlegen.
- Workspace Wiki und Project Pages testen.
- MCP-Zugriff aus deiner bevorzugten IDE oder Claude Code testen.

### Stufe 2
- Ein kleines nicht geschäftskritisches Repo spiegeln.
- Prüfen, ob Agenten mit Work Items + Pages wirklich schneller arbeiten.
- Prüfen, ob die Übersicht tatsächlich besser ist als Linear + Repo-Dateien.

### Stufe 3
- Erst dann Entscheidung über Migration weiterer Projekte.

## Vorschlag für initiale Plane-Struktur
| Ebene | Vorschlag |
|---|---|
| Workspace | dein gesamtes System / Unternehmen |
| Wiki | globale SOPs, Infra, Architektur, Prompt- und Operating Standards |
| Project 1 | orchestration |
| Project 2 | backend-core |
| Project 3 | marketing |
| Project Pages | Spezifikationen, Runbooks, Umsetzungspläne je Projekt |
| Modules | z. B. LiteLLM routing, n8n automation, worker runtime |
| Intake | lose Ideen und Inputs |

## Agenten-Workflow mit Plane
1. Agent verbindet sich über MCP oder API.
2. Agent holt Projekt- und Work-Item-Kontext.
3. Agent liest die zugehörigen Pages.
4. Agent arbeitet im Repo.
5. Agent aktualisiert Work Item, Kommentar und ggf. Page.

## Was Plane gut ersetzen kann
- ein Teil der Notion-Projektdokumentation
- ein Teil der Linear-Planung
- verstreute projektspezifische Spezifikationen

## Was Plane nicht automatisch löst
- schlechte Repo-Struktur
- fehlende Operating Standards für Agenten
- chaotische Naming-Konventionen
- fehlende Backups
- Infra-Überforderung durch zu viele neue Dienste

## Synergiepotenziale
- Plane Pages + Work Items reduzieren Medienbrüche.
- MCP-Anbindung an IDEs kann operative Reibung stark senken.
- Workspace Wiki kann Notion-Teile mit stark technischer Natur absorbieren.
- Parallelbetrieb mit Linear ist möglich, solange nur eine aktive Truth-Source pro Arbeitsbereich definiert wird.

## Kritische Empfehlung
Ja, es kann sinnvoll sein, Plane jetzt bereits als Teil des Server-Deployments mitzunehmen, aber nicht als sofortige Gesamtmigration. Als Evaluationspfad passt es gut zu deinem aktuellen Aufbauzustand. Als sofortiger Totalersatz ist es riskanter als der konservative Linear-first-Weg.
