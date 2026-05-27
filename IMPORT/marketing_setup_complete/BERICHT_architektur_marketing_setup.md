# Marketing-Setup Architektur: Vollständiger Bericht

> **Zweck dieses Dokuments:** Dieser Bericht erklärt im Prosa-Format, was das marketing-setup-Repository ist, warum es so aufgebaut wurde, wie die einzelnen Komponenten zusammenarbeiten, welche Abhängigkeiten kritisch sind, wo die Risiken liegen und welche Synergiepotenziale existieren. Er ergänzt die spezialisierten Dateien (CONTEXT.md, MILESTONES.md, DECISIONS.md, AGENT_PROMPTS.md), ohne deren Inhalte zu wiederholen.

---

## 1. Was dieses Repository überhaupt ist

Das `marketing-setup`-Repository ist kein klassisches Code-Repository. Es ist ein **operativer Arbeitsraum** für einen Solo-Entwickler, der gleichzeitig als Operator eines B2B-AI-Automation-Angebots im DACH-Raum fungiert. Die Herausforderung ist keine rein technische: Es geht darum, wie eine Person mit KI-Agenten schnell hochwertige Marketing-Outputs produzieren kann, ohne in den typischen Fallen zu landen — zu viele unstrukturierte Ressourcen, zu viele Tools ohne klare Zuständigkeit, zu viele nicht-integrierte Systeme.

Das Repository löst dieses Problem, indem es den Arbeitsraum des Agenten klar definiert. Wenn ein Agent (egal ob ClaudeCode, Antigravity oder ein zukünftiges Framework) dieses Repo öffnet, soll er ohne externe Rückfragen wissen: Was ist der aktuelle Stand? Was ist die nächste sinnvolle Aufgabe? Welche Entscheidungen sind bereits getroffen? Welche Ressourcen stehen zur Verfügung?

---

## 2. Das Informationsmodell: Warum Markdown im Repo und nicht Notion

Die naheliegende Frage ist: Warum werden Informationen nicht einfach in Notion gelassen, wo sie bereits gesammelt wurden? Die Antwort liegt in der Arbeitsweise von KI-Agenten.

Ein Agent, der in einer IDE oder über ein Framework mit einem Repository arbeitet, hat direkten, sofortigen Zugriff auf Dateien im Filesystem. Das kostet keine API-Tokens, erzeugt keine Latenz und schlägt keinen extra Auth-Flow vor. Notion-Inhalte hingegen erfordern entweder einen manuellen Copy-Paste-Schritt oder eine API-Integration. Solange n8n noch im Aufbau ist und keine stabile Notion-API-Brücke existiert, wäre jedes System, das stark auf Notion als Echtzeit-Wissensquelle angewiesen ist, fragil.

Die strategische Entscheidung lautet daher: **Notion ist ein Recherche- und Sammelort, das Repository ist der operative Arbeitsraum.** Relevante Inhalte aus Notion werden einmalig portiert (als Markdown-Dateien mit Metadaten-Header) und leben dann im Repo weiter. Notion bleibt erhalten für neue Sammlungen, aber nicht als Single Source of Truth für laufende Agenten-Arbeit.

Diese Entscheidung hat einen Preis: Es gibt einen manuellen Portierungsaufwand (Meilenstein M2 im Repository). Dieser Aufwand ist bewusst akzeptiert, weil er einmalig und steuerbar ist, während die Alternative — ein fragiler API-Roundtrip bei jedem Agenten-Kontext-Load — ein dauerhaftes Stabilitätsproblem wäre.

---

## 3. Das Dreischichten-Modell der Informationsorganisation

Das System basiert auf drei klar getrennten Informationsschichten, die unterschiedliche Aufgaben übernehmen.

### Schicht 1: Repository-Filesystem (Operativer Kern)
Das Repository ist der primäre Arbeitsraum des Agenten. Hier liegen alle Informationen, die für die unmittelbare Ausführung benötigt werden: Steuerdateien (`CONTEXT.md`, `MILESTONES.md`, `DECISIONS.md`), Templates, portierte Swipe-Files, Campaign-Briefs, LLM-Prompts und n8n-Workflow-Exports. Diese Schicht ist immer verfügbar, versionierbar und diffbar. Selbst wenn alle externen Tools ausfallen, kann ein Agent auf Basis dieser Schicht weiterarbeiten.

### Schicht 2: Linear (Execution-Tracking)
Linear dient ausschließlich als Task-Management-System. Es enthält konkrete, abgegrenzte Aufgaben mit klaren Status-Übergängen und Prioritäten. Was nicht in Linear gehört: vollständige Langform-Dokumentation, unstrukturierte Research-Sammlungen, strategische Grundsatzdokumente. Die Verbindung zwischen den Schichten wird durch eine einfache Konvention hergestellt: Jede aktive Linear-Issue-ID wird in `CONTEXT.md` referenziert, und jeder Commit enthält die Issue-ID in der Commit-Message. Das ermöglicht Rückverfolgbarkeit, ohne bidirektionale Synchronisationskomplexität zu erzeugen.

### Schicht 3: Notion (Wissensarchiv)
Notion bleibt der langfristige Wissenspool. Hier landen neue Freebies, Recherchen, Strategiepapiere und gesammelte Inspirationen. Es ist kein operatives Tool für den Agenten, sondern eine Ressource, aus der bei Bedarf Inhalte in das Repository portiert werden. Die Portierung ist ein bewusster, manueller Schritt (oder zukünftig via n8n automatisiert), kein Echtzeit-Sync.

---

## 4. Die Rolle von n8n: Multiplikator, kein Fundament

n8n ist im aktuellen Setup noch nicht vollständig eingerichtet, und das ist bewusst so. Der häufigste Fehler beim Aufbau von Automatisierungssystemen besteht darin, die Automatisierung als Fundament zu behandeln, bevor das manuelle System stabil ist. n8n wird dann zum Debuggen-Objekt statt zum Hebel.

Die geplante Rolle von n8n ist präzise definiert: Es übernimmt **Hintergrund-Syncs**, die wertschöpfend sind, aber nicht geschäftskritisch. Der erste geplante Workflow ist ein einseitiger Sync: Wenn ein Linear-Issue auf "Done" gesetzt wird, erstellt n8n automatisch einen Archiv-Eintrag in einer Notion-Datenbank — mit Issue-Titel, Abschlussdatum, Projekt, Labels und einem Link zum relevanten Repo-Pfad. Das ist kein sexy Workflow, aber er schafft über Zeit eine wertvolle Wissensbasis darüber, was tatsächlich gemacht wurde.

Der zweite geplante Workflow läuft in die andere Richtung: Ausgewählte Notion-Einträge (die explizit mit einem "ready_for_linear"-Flag versehen wurden) werden automatisch zu Linear-Drafts. Das Schlüsselwort ist "ausgewählt" — keine automatische Massenübernahme, die Linear mit unkuratiertem Rauschen flutet.

Warum noch kein n8n-Start? Weil es Abhängigkeiten gibt: Linear und Notion müssen mit ihren APIs verbunden werden, Credential-Management muss stehen, und die Feldmappings müssen exakt definiert sein, bevor ein Workflow stabil läuft. Dieser Aufwand lohnt sich — aber erst wenn das manuelle System bewiesen hat, dass die Logik stimmt.

---

## 5. LiteLLM als Marketing-Hebel

LiteLLM ist in diesem Setup nicht nur ein technisches Routing-Tool, sondern ein **strategischer Kostenhebel** für Marketing-Automation. Marketing-Aufgaben haben sehr unterschiedliche LLM-Qualitätsanforderungen, und diese Unterschiede direkt in Kosten umzurechnen ist entscheidend für wirtschaftlich sinnvolle Automatisierung.

Strategische Copy — E-Mail-Sequenzen, Landing-Page-Texte, Positionierungsstatements — erfordert hohe Modellqualität. Hier wird Claude Sonnet oder Opus via LiteLLM genutzt. Die Kosten sind höher, aber der Output direkt wertschöpfend.

Klassifikation, Tagging und erste Rohfassungen sind hingegen ideal für günstigere Modelle. Wenn ein Agent einen Swipe-File kategorisieren oder einen ersten Entwurf für eine Social-Post-Variante erstellen soll, ist ein günstiges Modell ausreichend und deutlich kosteneffizienter.

LiteLLM ermöglicht genau diese Differenzierung — zentral, ohne dass in jedem Prompt-Skript ein hartkodierter Modellname steckt. Die Modellauswahl kann geändert werden, ohne alle Prompts anzufassen. Das ist besonders relevant in einem Markt, wo sich Modellqualitäten und -preise in Monaten, nicht Jahren, verschieben.

---

## 6. Die Bedeutung von brand-voice.md und icp-summary.md

Zwei Dateien in `/docs/` haben eine besondere Stellung, die nicht sofort offensichtlich ist: `brand-voice.md` und `icp-summary.md`. Sie sind keine gewöhnliche Dokumentation — sie sind der **Persönlichkeitsanker** für alle LLM-generierten Outputs.

Ohne eine explizite Brand-Voice-Beschreibung tendieren LLM-generierte Marketing-Texte zu einem generischen, AI-typischen Stil: Buzzword-lastig, vorsichtig formuliert, ohne echten Charakter. Eine `brand-voice.md`, die konkret beschreibt, was erlaubt ist (z.B. "direkter Klartext, konkrete Zahlen, technische Kompetenz zeigen") und was verboten ist (z.B. "revolutionär, synergistisch, game-changing"), gibt dem Agenten einen echten Filter.

Die `icp-summary.md` erfüllt eine ähnliche Funktion für die Zielgruppe. Ein Prompt, der nur sagt "schreibe für B2B-Kunden", produziert andere Outputs als ein Prompt, der auf ein konkretes Profil verweist: "IT-Entscheider in Unternehmen mit 10-50 Mitarbeitern in der DACH-Region, die Prozesse automatisieren wollen, aber kein Budget für einen Vollzeit-IT-Mitarbeiter haben."

Diese beiden Dateien sind daher nicht optional — sie sind die erste Priorität in Meilenstein M1, noch vor dem Template-Aufbau.

---

## 7. Die Commit-Konvention als Buchführung

Die Commit-Message-Konvention `[Typ](scope): Beschreibung [Issue-ID]` ist keine kosmetische Maßnahme. Sie ist die einzige Echtzeit-Verbindung zwischen dem Repository-Zustand und dem Linear-Tracking-System, solange n8n noch nicht läuft.

Wenn ein Agent einen Commit mit `feat(copy): add cold-outreach template for IT-Dienstleister [MAR-14]` erstellt, entsteht dadurch eine Spur: Das Issue MAR-14 in Linear wird über die Commit-History mit dem konkreten Output verknüpft. Das ermöglicht späteren Agenten (oder dir als Mensch) nachzuvollziehen, was für ein bestimmtes Issue tatsächlich gemacht wurde — ohne eine vollständige Synchronisationsinfrastruktur.

Diese Konvention kostet nichts und schafft Wert sofort. Sie ist daher einer der wenigen "sofort umzusetzenden" Standards in diesem Setup.

---

## 8. Kritische Abhängigkeiten und ihre Risiken

### Abhängigkeit 1: Linear-API-Stabilität
Linear ist das operative Execution-System. Wenn Linear ausfällt oder sich API-Spezifikationen ändern, verliert der Agent seinen Task-Tracker. **Mitigierung:** Das Repo selbst trägt über CONTEXT.md genug operativen Kontext, dass Arbeit auch ohne Linear-Zugriff kurzfristig fortgesetzt werden kann. Alle aktiven Issues werden in CONTEXT.md gespiegelt.

### Abhängigkeit 2: LiteLLM-Proxy-Verfügbarkeit
Alle LLM-generierten Marketing-Outputs gehen über den LiteLLM-Proxy. Wenn dieser nicht läuft, können keine automatisierten Copy-Generierungen stattfinden. **Mitigierung:** Für dringende Fälle können Agenten direkt über IDE-eigene LLM-Integrationen arbeiten — das ist eine bewusste Rückfallebene, auch wenn sie ineffizienter ist.

### Abhängigkeit 3: Notion-Qualität der Freebies
Die gesammelten Notion-Freebies haben unterschiedliche Qualität und Relevanz. Einige sind hochwertig, andere sind veraltete oder markt-irrelevante Templates. **Mitigierung:** Das Qualitätsbewertungssystem (A/B/C) im Metadaten-Header der Swipe-Files schafft Transparenz. Der Agent behandelt C-Dokumente immer als Rohmaterial, das überarbeitet werden muss, nicht als fertige Ressource.

### Abhängigkeit 4: n8n noch nicht aktiv
Solange n8n nicht läuft, gibt es keinen automatischen Sync zwischen Linear-Status und Notion-Archiv. **Mitigierung:** Die CONTEXT.md-Pflicht nach jedem Task stellt sicher, dass der operative Zustand dokumentiert bleibt — auch ohne automatische Archivierung.

---

## 9. Synergiepotenziale im Gesamtbild

Das eigentliche Synergiepotenzial dieses Setups liegt nicht in einem einzelnen Tool, sondern in der **Verstärkung durch Kombination**. Wenn alle Schichten sauber zusammenspielen, entsteht ein Arbeitsmodell, das für einen Solo-Operator einzigartig effizient ist:

**LiteLLM + Prompts-Bibliothek** bedeutet, dass neue Marketing-Anforderungen in Minuten mit erprobten Prompts bearbeitet werden können, ohne jedes Mal neu zu formulieren. Die Prompts-Bibliothek in `/workflows/prompts/` ist eine Investition, die mit jedem neuen Eintrag Compound-Interesse erzeugt.

**Swipe-Files + Brand Voice + ICP** bedeutet, dass Agenten nicht im Vacuum generieren. Sie haben Referenzbeispiele, Persönlichkeitsregeln und Zielgruppenprofile als konkreten Kontext. Das verbessert Output-Qualität bei gleichzeitig weniger Review-Aufwand.

**Kampagnen-Ordner-Struktur** bedeutet, dass jede Kampagne ein vollständiges Paket ist: Brief, Copy-Varianten, Assets, Ergebnisse. Das ermöglicht Retrospektiven und systematisches Lernen über Kampagnen hinweg — auch wenn man als Solo-Operator keine dedizierte Analyse-Zeit hat.

**n8n + Linear + Notion** (zukünftig) bedeutet schließlich, dass das gesamte operative Wissen, das durch Ausführung entsteht, automatisch archiviert wird. Das Unternehmen lernt durch Arbeit, ohne dass Lernen als separater Prozess eingeplant werden muss.

---

## 10. Was als Nächstes getan werden sollte

Die wichtigste Erkenntnis aus der Architektur dieses Setups ist: **Infrastruktur vor Automation.** Bevor irgendetwas automatisiert wird, muss das manuelle System funktionieren.

Das bedeutet konkret:

Erstens, die Repo-Steuerdateien (CONTEXT.md, MILESTONES.md, DECISIONS.md) vollständig ausfüllen. Nicht als Pflichtübung, sondern weil der Agent ohne diese Informationen schlechte Outputs produziert.

Zweitens, `brand-voice.md` und `icp-summary.md` in `/docs/` mit echten, spezifischen Inhalten füllen. Diese beiden Dateien haben den größten Hebel auf Output-Qualität aller LLM-generierten Inhalte.

Drittens, mit einem einzigen, kleinen LLM-Prompt beginnen — vielleicht die Kaltakquise-E-Mail-Sequenz — und diesen von Ende zu Ende testen: Prompt formulieren, in LiteLLM schicken, Output reviewen, Prompt iterieren, Ergebnis ablegen. Dieser kleine Kreislauf, einmal vollständig durchgeführt, zeigt schnell, wo die echten Reibungspunkte sind.

Alles andere — n8n-Integration, vollständige Notion-Portierung, Plane-Migration — kommt danach, wenn das Fundament steht.
