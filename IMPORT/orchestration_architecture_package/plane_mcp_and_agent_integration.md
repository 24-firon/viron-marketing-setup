# Plane MCP and Agent Integration

## Zweck
Diese Datei beschreibt, wie Plane mit KI-Agenten und IDEs zusammenarbeitet und wo die praktischen Vor- und Nachteile liegen.

## Offiziell dokumentierte MCP-Modi
Plane dokumentiert vier Transportmodi:
- HTTP with OAuth
- HTTP with PAT Token
- Local stdio
- SSE legacy

## Relevanz der Modi

### HTTP with OAuth
Gut für interaktive Nutzung in unterstützten Clients. Browserbasierter Flow, weniger Secret-Verteilung.

### HTTP with PAT Token
Gut für automatisierte Workflows und feste Team-Setups. Benötigt API-Key und Workspace-Slug in Headers.

### Local stdio
Stark für lokale Entwicklung oder self-hosted Nutzung. Credentials werden per Umgebungsvariablen gesetzt.

### SSE legacy
Nur für bestehende Altintegrationen sinnvoll.

## Dokumentierte Client-Ziele
Plane dokumentiert Konfigurationen für:
- Claude Desktop
- Claude Code
- Claude.ai Web
- Cursor
- VS Code
- Windsurf
- Zed

Das ist ein praktischer Vorteil, weil du mehrere IDEs nutzt.

## Wichtiges Identifikationsmodell
Plane unterscheidet zwischen:
- lesbaren Kennungen wie `ENG-42`
- UUIDs für Maschinenoperationen

Das ist für Agenten relevant, weil Menschen Tickets meist über lesbare IDs referenzieren, die Tools intern aber mit UUIDs arbeiten.

## Was der Agent praktisch tun kann
Laut Doku kann der MCP-Server unter anderem:
- Projekte listen und anlegen
- Work Items suchen, lesen, erstellen und ändern
- Status ändern
- Kommentare anlegen
- Links an Work Items hängen
- Beziehungen zwischen Work Items pflegen
- Cycles verwalten
- Modules verwalten
- Pages auf Workspace- und Projektebene anlegen und lesen
- Worklogs schreiben

## Warum das für deine Umgebung interessant ist
Du arbeitest verteilt über mehrere IDEs und Repos. Ein offizieller MCP-Server mit dokumentierten Client-Configs senkt den Integrationsaufwand gegenüber selbstgebauten Adaptern.

## Praktische Grenzen
- MCP löst nicht das Problem von unklarer Projektstruktur.
- MCP macht Toolzugriff einfach, aber nicht automatisch gute Planung.
- Zu viele freigeschaltete Features können auch für Agenten unnötigen Kontextballast erzeugen.

## Empfehlung für die Erstkonfiguration
- Wenige Projekte.
- Klare Identifier.
- Cycles am Anfang nur falls nötig.
- Modules nur für echte thematische Cluster.
- Workspace Wiki für globale Standards.
- Project Pages für ausführungsnahe Dokumente.

## Beispielhafte Denkweise
Statt "alles überall dokumentieren" sollte der Agent so arbeiten:
1. Finde Projekt.
2. Finde aktives Work Item.
3. Finde passende Page.
4. Arbeite im Repo.
5. Schreibe Abschlusskommentar.

## Warum Repo-Dateien trotzdem bleiben sollten
Auch mit Plane ist das Repo der direkteste Arbeitsraum. Eine knappe `CONTEXT.md` im Repo bleibt sinnvoll als lokaler Schnellzugriff, besonders wenn Plane temporär nicht erreichbar ist oder der Agent primär codezentriert arbeitet.
