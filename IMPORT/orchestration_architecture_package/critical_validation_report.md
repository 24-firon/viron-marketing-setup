# Kritischer Validierungsbericht

## Zweck
Dieser Bericht korrigiert, präzisiert und kontextualisiert die vorherigen Aussagen. Er enthält nur übergreifende Bewertung, Abhängigkeiten, Widersprüche, Risiken und Synergien. Detaillierte Umsetzungsvorlagen stehen in den spezialisierten Dateien und werden hier nicht wiederholt.

## Ausgangslage
Die Kernfrage ist nicht nur "Linear oder Plane", sondern welches Orchestrierungsmuster für eine Solo-Entwickler-Umgebung mit parallelem Infrastrukturaufbau den höchsten Hebel bei geringstem Einführungsrisiko bringt.

## Korrigierte Sachlage
Eine frühere vereinfachte Darstellung von Plane als quasi leichtgewichtiges Self-Hosting-Tool ohne wesentliche Zusatzdienste wäre zu optimistisch. Die offizielle Coolify-Dokumentation nennt für produktionsnahe Nutzung klar externe Verbindungen für Datenbank, Redis und RabbitMQ. Das verschiebt die Bewertung deutlich in Richtung "machbar, aber nicht trivial".

## Offizielle Doku vs. operative Realität

### Offizielle Doku claimt
- Plane ist über Coolify deploybar.
- Plane bietet integriertes Wiki und Project Pages.
- Plane stellt einen offiziellen MCP-Server bereit.
- Plane lässt sich mit mehreren IDEs und Agent-Clients integrieren.

### Operative Realität zeigt
- Self-Hosting bedeutet zusätzliche Infra-Komponenten und laufende Verantwortung.
- Der eigentliche Nutzen entsteht erst mit sauberem Informationsmodell.
- MCP ist ein Hebel, aber kein Ersatz für gute Operating Standards.
- Wenn mehrere Truth-Sources parallel aktiv bleiben, verliert auch Plane einen Teil seines Vorteils.

## Kritische Abhängigkeitsmatrix
| Bereich | Linear-first | Plane-Evaluation parallel | Plane als sofortiger Hauptpfad |
|---|---|---|---|
| Einrichtungszeit | niedrig | mittel | mittel bis hoch |
| Infra-Komplexität | niedrig | mittel | hoch |
| Sofortige Produktivität | hoch | mittel bis hoch | unsicher |
| Agentenfreundlichkeit langfristig | mittel | hoch | hoch |
| Migrationsrisiko | niedrig | niedrig bis mittel | hoch |
| Open-Source-Passung | niedrig | hoch | hoch |

## Strategische Lesart
Wenn du gerade viel neu aufbaust, kann der Zeitpunkt tatsächlich günstig sein, Plane mit in die Architektur zu ziehen. Das ist ein valider Gedanke. Der Knackpunkt ist aber, ob Plane in deinem Fall ein beschleunigender Systemanker wird oder ein weiterer Baustellenmultiplikator.

## Wann Plane synergetisch wirkt
Plane entfaltet den größten Synergieeffekt, wenn mehrere sonst getrennte Ebenen zusammenlaufen:
- Projektdokumentation näher an Work Items.
- Agenten greifen standardisiert über MCP zu.
- IDE-übergreifende Konfiguration wird vereinheitlicht.
- Notion wird selektiv entlastet.
- Der Overhead von selbstgebauten Brücken sinkt.

## Wann Linear weiterhin synergetischer ist
Linear ist kurzfristig synergetischer, wenn:
- bereits aktive Verknüpfungen existieren.
- du in den nächsten Tagen schnelle Ausführung brauchst.
- du keine zusätzlichen Infra-Dienste operationalisieren willst.
- du zuerst Standards für Agentenverhalten etablieren willst.

## Eigentliche Schlüsselvariable
Die wichtigste Variable ist nicht das PM-Tool, sondern die Frage, wo der operative Arbeitskontext für Agenten lebt. Wenn dieser Kontext sauber im Repo oder sauber in Plane-Pages/Work-Items organisiert ist, funktionieren Agenten. Wenn der Kontext über fünf halbfertige Systeme verteilt ist, versagt jede Lösung.

## Empfehlung als Entscheidungsgabel

### Pfad A: konservativ
- Linear als aktiver Execution-Layer beibehalten.
- Repo-first-Kontext standardisieren.
- n8n klein anfangen.
- Plane erst nach stabilisiertem Aufbau testen.

### Pfad B: opportunistisch, aber kontrolliert
- Plane jetzt deployen.
- Nicht migrieren, sondern evaluieren.
- Ein bis zwei nichtkritische Projekte dort modellieren.
- Entscheidung datenbasiert nach echter Agentenpraxis treffen.

## Belastbare Kernaussage
Deine Intuition ist plausibel: Es **kann** weniger aufwendig sein, Plane kontrolliert gegen deine Architektur zu testen, als früh komplexe Linear-Notion-n8n-Brücken auszubauen. Aber dieser Vorteil gilt nur, wenn Plane nicht sofort zur neuen alleinigen Hauptplattform erklärt wird.

## Priorisierte nächste Schritte
1. Operatives Kontextmodell je Repo standardisieren.
2. Linear für laufende Arbeit stabil halten.
3. Plane als Evaluationsdeployment parallel aufsetzen.
4. Erst nach echter Nutzung über Migration entscheiden.
