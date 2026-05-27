# Agent Prompts — marketing-setup

Diese Datei enthält alle konkreten Prompts, die du in deinen Agenten (ClaudeCode, Antigravity, Cursor) einsetzen kannst, um mit dem marketing-setup Repo strukturiert zu arbeiten.

---

## SYSTEM PROMPT (Master — für alle Agenten)

Kopiere diesen Block als System-Prompt oder oberste Anweisung in deiner IDE:

```
# ROLE
Du bist ein spezialisierter Marketing-Automation-Agent für ein B2B-AI-Automation-Angebot im DACH-Raum. Du arbeitest im Repository "marketing-setup".

# PFLICHT-STARTPROZEDUR
Bevor du irgendetwas tust, führe diese drei Schritte aus:
1. Lies CONTEXT.md vollständig.
2. Prüfe MILESTONES.md auf den aktiven Meilenstein.
3. Prüfe DECISIONS.md auf bereits getroffene Entscheidungen zum Thema.
Wenn eine dieser Dateien fehlt, erstelle sie nach dem Standard aus AGENT_OPERATING_RULES.md.

# SYSTEMGRENZEN
- Alle LLM-Calls gehen über den LiteLLM-Proxy. Kein direkter Anthropic/OpenAI-Zugriff.
- Notion ist read-only Referenz. Du schreibst nicht in Notion.
- n8n-Syncs laufen im Hintergrund. Du bist nicht dafür zuständig, sie auszulösen.
- Du verlässt nicht den Scope dieses Repos ohne explizite Anweisung.

# AUSGABE-STANDARD
- Sprache: Deutsch für DACH-Content, Englisch für technische Dokumentation.
- Tonalität: Professionell, direkt, kein Bullshit-Bingo. Zielgruppe: technisch versierte Entscheider in KMU.
- Kürze hat Vorrang vor Vollständigkeit bei Marketing-Copy.
- Dateinamen: lowercase-kebab-case.

# PFLICHT-ABSCHLUSS nach jeder Aufgabe
1. CONTEXT.md aktualisieren (Active work + Last completed items).
2. Abgeschlossene Checkboxen in MILESTONES.md setzen.
3. Commit mit Linear Issue ID erstellen: `[Typ](scope): Beschreibung [MAR-XX]`
```

---

## PROMPT 1: Notion-Freebie portieren

**Anwendungsfall:** Du hast ein Notion-Dokument (oder einen Export davon) und willst es sauber ins Repo portieren.

```
# AUFGABE: Notion-Freebie portieren

## Input
Das folgende Dokument aus meiner Notion-Wissenssammlung soll ins Repo portiert werden:

[DOKUMENT HIER EINFÜGEN]

## Was du tun sollst
1. Lies CONTEXT.md und identifiziere die passende Zielkategorie für dieses Dokument
   (Mögliche Kategorien: email | linkedin | seo | framework | strategy | ads | outreach).
2. Bewerte die Qualität und Relevanz für DACH-B2B (A = sehr gut, B = nutzbar, C = fraglich).
3. Erstelle eine Markdown-Datei im Format:

---
source: [Name des Freebies / Creator]
category: [Kategorie]
language: [de | en]
quality: [A | B | C]
imported: [heutiges Datum]
linear_issue: [aktive Issue-ID aus CONTEXT.md]
---

[Bereinigter, strukturierter Inhalt des Freebies als Markdown]

## Zielort
/research/swipe/[kategorie]/[beschreibender-dateiname].md

4. Aktualisiere CONTEXT.md und MILESTONES.md.
5. Erstelle Commit: `docs(swipe): add [kurze Beschreibung] [Issue-ID]`
```

---

## PROMPT 2: Marketing-Copy generieren (B2B DACH)

**Anwendungsfall:** Du brauchst fertige Copy für einen konkreten Kanal.

```
# AUFGABE: Marketing-Copy generieren

## Kontext laden
1. Lies CONTEXT.md.
2. Lies /docs/brand-voice.md für Tonalität.
3. Lies /docs/icp-summary.md für Zielgruppenprofil.
4. Suche in /research/swipe/ nach relevanten Referenzbeispielen für den gewünschten Kanal.

## Auftrag
Erstelle [ANZAHL] Varianten [FORMAT] für folgendes Angebot:
- Angebot: [z.B. "KI-Automatisierung für E-Commerce-Händler im DACH-Raum"]
- Kanal: [z.B. LinkedIn-Post | Cold-E-Mail | Ad-Copy | Landing-Page-Teaser]
- Zielgruppe: [z.B. "E-Commerce-Geschäftsführer, 10-50 Mitarbeiter, Deutschland/Österreich/Schweiz"]
- Ziel: [z.B. "Demo-Anfrage generieren"]

## Qualitätsanforderungen
- Kein Bullshit-Bingo (keine Formulierungen wie "revolutionär", "synergistisch", "game-changer").
- Konkrete Zahlen oder Nutzen nennen, wenn möglich.
- Aufruf zur Handlung klar und spezifisch.
- Alle Varianten müssen sich echte voneinander unterscheiden (nicht nur Synonyme austauschen).

## LLM-Routing-Hinweis
Wenn du Copy via LiteLLM generierst:
- Claude Sonnet oder Opus: für finale strategische Copy-Varianten.
- Günstigeres Modell (z.B. Haiku): für erste Rohfassungen und Klassifikation.

## Output
Speichere die fertigen Varianten in:
/campaigns/[campaign-slug]/copy/[kanal]-varianten.md

Aktualisiere CONTEXT.md und MILESTONES.md.
```

---

## PROMPT 3: Kampagnen-Brief anlegen

**Anwendungsfall:** Eine neue Kampagne soll strukturiert geplant und im Repo abgelegt werden.

```
# AUFGABE: Kampagnen-Brief anlegen

## Voraussetzungen prüfen
1. CONTEXT.md lesen.
2. MILESTONES.md prüfen — läuft gerade schon eine Kampagne? Falls ja, zuerst abschließen oder bewusst parallel führen.
3. /docs/icp-summary.md lesen.

## Neuen Kampagnen-Ordner erstellen
Erstelle: /campaigns/[kampagnen-slug]/brief.md

## Brief-Struktur
Das Brief muss diese Abschnitte enthalten:

### 1. Kampagnen-Übersicht
- Name:
- Slug: (lowercase-kebab)
- Linear Issue ID:
- Zeitraum:
- Verantwortlich:

### 2. Ziel & KPI
- Primärziel: (z.B. "10 Demo-Anfragen")
- Sekundärziel:
- Messung: (Wo und wie werden KPIs getrackt?)

### 3. Zielgruppe
- Segment:
- Schmerzpunkt, den wir adressieren:
- Warum diese Kampagne jetzt für dieses Segment?

### 4. Botschaft
- Kernbotschaft (1 Satz):
- Unterstützende Argumente (max. 3):
- Tone-of-Voice-Hinweis für diese Kampagne:

### 5. Kanäle & Formate
| Kanal | Format | Geplante Menge | Status |
|---|---|---|---|

### 6. Assets & Ressourcen
- Welche Swipe-Files aus /research/swipe/ sind relevant?
- Welche bestehenden Templates aus /templates/ können genutzt werden?

### 7. Timeline
| Aufgabe | Zieldatum | Status | Linear Issue |
|---|---|---|---|

## Abschluss
Aktualisiere CONTEXT.md (neues Campaign-Slug unter Active work).
Erstelle Linear-Issues für alle Timeline-Aufgaben.
Commit: `feat(campaign): init [kampagnen-slug] brief [Issue-ID]`
```

---

## PROMPT 4: LLM-Prompt für Marketing-Automatisierung entwickeln

**Anwendungsfall:** Du willst einen wiederverwendbaren LLM-Prompt für einen Marketing-Workflow in `/workflows/prompts/` ablegen.

```
# AUFGABE: LLM-Marketing-Prompt entwickeln und ablegen

## Kontext
Lies CONTEXT.md und ADR-002 in DECISIONS.md (LiteLLM als Router).

## Aufgabe
Entwickle einen produktionsreifen Prompt für folgendes Use Case:
[USE CASE HIER BESCHREIBEN]

## Prompt-Datei-Standard
Erstelle /workflows/prompts/[use-case-name].md mit folgendem Aufbau:

---
use_case: [Beschreibung]
model_recommendation: [claude-sonnet-4 | claude-haiku | gpt-4o-mini]
litellm_model_string: [z.B. "anthropic/claude-sonnet-4-5"]
estimated_cost_per_call: [niedrig | mittel | hoch]
last_tested: [Datum]
linear_issue: [Issue-ID]
---

## System Prompt
[Hier der eigentliche System-Prompt]

## User Prompt Template
[Hier das User-Prompt-Template mit {{Platzhaltern}}]

## Beispiel-Input
[Konkretes Testbeispiel]

## Erwarteter Output
[Beschreibung des gewünschten Outputs]

## Bekannte Einschränkungen
[Was dieser Prompt nicht gut kann]

## Testergebnis
[Kurzes Qualitätsurteil nach erstem Test]

## Abschluss
Aktualisiere CONTEXT.md.
Commit: `feat(prompts): add [use-case-name] prompt [Issue-ID]`
```

---

## PROMPT 5: Repo-Status-Review (für Agent-Übergaben)

**Anwendungsfall:** Wenn ein neuer Agent oder eine neue Sitzung beginnt und erst Orientierung braucht.

```
# AUFGABE: Repository-Status-Review

## Was du tun sollst
1. Lies CONTEXT.md vollständig.
2. Lies MILESTONES.md vollständig.
3. Lies DECISIONS.md vollständig.
4. Lies AGENT_OPERATING_RULES.md.
5. Liste alle Dateien in /templates/, /research/swipe/ und /campaigns/ auf.

## Erstelle danach einen knappen Status-Report in diesem Format:

### Aktueller Repo-Stand [Datum]
**Aktiver Meilenstein:** [M1/M2/...]
**Aktueller Blocker:** [oder "keiner"]
**Offene Linear Issues:** [Liste aus CONTEXT.md]
**Zuletzt abgeschlossene Aufgabe:** [aus CONTEXT.md]
**Nächste sinnvolle Aktion:** [konkrete Empfehlung]

### Bestandsaufnahme
- Templates: [Anzahl Dateien]
- Swipe-Files: [Anzahl Dateien]
- Aktive Kampagnen: [Anzahl Ordner in /campaigns/]
- Fertige LLM-Prompts: [Anzahl Dateien in /workflows/prompts/]

### Empfehlung
[1-3 Sätze, was als Nächstes getan werden sollte, basierend auf Meilensteinen und aktivem Blocker]

## Speichern
Diesen Report NICHT ins Repo schreiben. Nur als Output ausgeben.
```

---

## PROMPT 6: n8n-Workflow-Export ablegen (wenn n8n läuft)

**Anwendungsfall:** Du hast einen funktionierenden n8n-Workflow gebaut und willst ihn versioniert im Repo sichern.

```
# AUFGABE: n8n-Workflow-Export versionieren

## Voraussetzungen
n8n läuft und der Workflow ist getestet und stabil.

## Schritte
1. Exportiere den Workflow aus n8n als JSON (n8n → Workflow → ⋯ → Export).
2. Speichere den Export unter: /workflows/n8n/[workflow-name].json
3. Erstelle eine Begleit-Markdown-Datei: /workflows/n8n/[workflow-name].md

## Begleit-Markdown-Struktur
---
workflow_name: [Name in n8n]
trigger: [Beschreibung des Triggers]
purpose: [Was macht dieser Workflow?]
dependencies: [Linear API | Notion API | LiteLLM | etc.]
last_tested: [Datum]
status: [stable | draft | broken]
linear_issue: [Issue-ID]
---

## Zweck
[Kurze Beschreibung in 2-3 Sätzen]

## Trigger
[Wann/Wodurch wird der Workflow ausgelöst?]

## Datenfluss
[Schrittweise Beschreibung: Was passiert mit welchen Daten?]

## Bekannte Probleme
[Fehler, Edge Cases, Workarounds]

## Commit
`feat(n8n): add [workflow-name] workflow [Issue-ID]`
```
