# VIRON Orchestration System — Vollständiges Betriebshandbuch
**Version:** 2.0 | **Stand:** 19.03.2026 | **Owner:** Inspektor (Operator)

---

## WICHTIG: WER LIEST DIESES DOKUMENT?

Dieses Dokument richtet sich an drei Lesertypen gleichzeitig:

1. **Externe KI-Agents** (Gemini, GPT-4, Llama, etc.) die Content produzieren sollen — sie brauchen vollständigen Kontext über Ziel, Zielgruppe, Ton und Regeln
2. **Claude-Sessions** (Haiku, Sonnet, Opus) die das System in einem neuen Chat weiterbetreiben — sie brauchen den aktuellen Status und die nächsten Schritte
3. **Der Operator (Inspektor)** selbst — als Nachschlagewerk und Entscheidungsgrundlage

Wenn du ein KI-Agent bist: Lies dieses Dokument vollständig, bevor du irgendeinen Content erstellst. Fang keine Task an, die nicht hier drin steht.

---

## 1. WAS IST VIRON UND WAS MACHT GROUND-ZERO AGENCY?

Ground-Zero Agency Infrastructure ist eine **Solo-KI-Automatisierungsagentur** mit Sitz in Deutschland. Der einzige Mensch dahinter ist Inspektor (der Operator). Die Agentur hat noch keine großen Außenauftritte — sie befindet sich in der Aufbauphase.

**Was wird verkauft:**
- Maßgeschneiderte Automatisierungs-Workflows für kleine und mittlere Unternehmen (KMU)
- Konkret: n8n-Workflows, KI-Agenten, CRM-Integrationen, Lead-Qualifizierung, Content-Automatisierung
- Nicht verkauft: generische KI-Beratung, Prompt-Engineering-Kurse, Tool-Tutorials ohne Umsetzung

**An wen wird verkauft (ICP = Ideal Customer Profile):**
- Unternehmen mit 5–50 Mitarbeitern im DACH-Raum (Deutschland, Österreich, Schweiz)
- Branchen-Schwerpunkte: Lokaler Einzelhandel (Boutiquen, Concept Stores) & Premium-Dienstleister (Consultants, Agenturen, Therapeuten). Budget-Bereitschaft: 5.000–15.000 €.
- Schmerzpunkte der Kunden: Website generiert keine Leads (Website als "toter Prospekt"), Termin-Ping-Pong, unstrukturierte Daten, kein funktionierendes CRM, manuelles Inventar/Onboarding-Chaos. Sie wollen eine "Website als 24/7 Verkäufer" und Automatisierung für ihren größten operativen Engpass.
- Psychografie des Entscheiders: Geschäftsführer, 35–55 Jahre, pragmatisch. Weiß, dass er 5k-15k € investieren muss. Fragt nicht "Was ist KI?" sondern "Wie macht diese Website/Automatisierung mein Leben leichter und bringt Leads?"

**Was VIRON NICHT ist:**
- Kein SaaS-Produkt
- Kein Coaching-Angebot
- Keine Agentur für große Konzerne
- Kein OpenAI-Reseller (OpenAI ist im gesamten System verboten)

---

## 2. DER TOOL-STACK (BINDEND — KEINE ABWEICHUNGEN)

Alle Agents müssen diese Entscheidungen respektieren. Begründung steht dahinter.

| Tool | Verwendung | Warum? |
|------|-----------|--------|
| **n8n (self-hosted, Hetzner)** | ALLE Workflows, Automatisierungen | Open-Source, kostenlos, volle Kontrolle. Zapier ist VERBOTEN als primäres Tool. Zapier darf nur in externem KMU-Content als "Einsteigeralternative (teurer)" erwähnt werden. |
| **Gemini / Vertex AI** | Standard-LLM für Bulk-Content-Generierung | $300 Credits vorhanden, kostengünstigste Option. Fallback: Claude Haiku. |
| **Claude Haiku** | Interne Factory-Arbeit, Scans, Recycling | Günstig, schnell. Nicht für strategische Arbeit. |
| **Claude Sonnet** | QA-Checks, strategische Artikel, Planung | Qualität wo es drauf ankommt. |
| **Claude Opus** | Nur One-Shot-Reviews, Architektur-Entscheidungen | Teuer. Sparsam einsetzen. Nur wenn explizit vom Operator angefragt. |
| **PostgreSQL 16 (Hetzner)** | Hauptdatenbank | Keine anderen DBs als Primary. Tägliche Backups. |
| **Airtable** | Visual Review-Queue für Content | MAX 1.000 Records. Nur Thumbnails + URLs speichern, KEINE File-Attachments. Archivieren ab 700 Records. |
| **Linear** | Projekt-Management, Source of Truth | Alle Tasks haben ein Linear-Issue. Alle Agents updaten Linear nach Task-Abschluss. |
| **Notion** | Dokumentation, Wissensbasis | READ-ONLY für alle Agents. Nur der Operator schreibt in Notion. |
| **Python 3.11** | Alle Scripts und Custom-Logik | NICHT 3.12. Docker-Images: FROM python:3.11-slim |
| **Metricool (GROUND0-6 Webhook)** | Social Media Publishing (IG, LinkedIn, TikTok, YT) | Triggerung via n8n. |

**ABSOLUT VERBOTEN (kein Verhandlungsspielraum):**
- ❌ OpenAI in irgendeiner Form (auch nicht als Beispiel in internem Code)
- ❌ Zapier als primäre Empfehlung
- ❌ Python 3.12 Features
- ❌ Proprietäre Modellnamen in Prompts hardcoden (kein "benutze Imagen 3")
- ❌ Dateien in Airtable als Attachment hochladen

---

## 3. DAS CONTENT-SYSTEM (WARUM WIR CONTENT MACHEN UND WIE)

Ground-Zero hat noch keinen Kundenstamm. Der Plan: Über Inbound-Marketing auf LinkedIn und Instagram qualifizierte Leads anziehen, die bereits verstehen was KI-Automatisierung ist und bereit sind zu investieren. Content ist die einzige Marketing-Aktivität in Phase 1.

### Die Content-Pyramide

```
         ▲
    [4 Mega-Guides]
    Tiefgehende, SEO-optimierte Artikel (3.000–7.000 Wörter)
    Ziel: Google-Ranking, Autorität aufbauen, Evergreen-Traffic

         │
   [16 Pillar-Artikel]
   Kürzere Artikel (800–1.500 Wörter) die aus den Mega-Guides entstehen
   Ziel: Longtail-Keywords, internes Linking, Content-Recycling-Basis

         │
  [~450 Social Content Pieces]
  LinkedIn-Posts, Instagram-Carousels, Reel-Scripts, TikTok
  Ziel: Tägliche Sichtbarkeit, Engagement, direkte Lead-Generierung
         ▼
```

**Wichtig zum Verständnis:** Die 450 Social Pieces sind kein heiliges Ziel. Qualität schlägt Quantität. 80 hochwertige, spezifische Posts über Handwerker-Automatisierung konvertieren besser als 400 generische KI-Posts.

### Was bereits produziert wurde (Stand 19.03.2026)

| Kategorie | Fertig | Ziel | Status |
|-----------|--------|------|--------|
| Mega-Guides | 4 | 4 | ✅ Abgeschlossen |
| Pillar-Artikel | 67 | 16 | ✅ Überproduktion (SEO-wertvoll) |
| LinkedIn-Posts | ~35 | ~180 | ⏳ ~19% |
| IG Carousels | 8 | ~80 | ⏳ 10% |
| Reel Scripts | 8 | ~80 | ⏳ 10% |
| TikTok Scripts | 0 | ~80 | ❌ Nicht gestartet |

**Vorhandene Dateien (alle unter `/Work-Lab/Content/`):**
- `MG-1_KI-Automatisierung-KMUs.md` — 3.868 Wörter. HINWEIS: Enthält Zeile ~443 eine OpenAI-Referenz die gefixt werden muss.
- `MG-2_Content-Produktion-mit-KI.md` — 4.473 Wörter. Sauber.
- `MG-3_KI-Landing-Pages.md` — 6.636 Wörter. Sauber.
- `MG-4_KI-Strategie-90-Tage.md` — 4.416 Wörter. Sauber.
- `Pillars-MG-1.md` — 4 Pillar-Artikel. HINWEIS: Zapier oft als gleichwertiges Tool erwähnt. Framing anpassen: n8n = Standard, Zapier = teuerere Einsteigeralternative.
- `Pillars-MG-2.md` — 4 Pillar-Artikel. Sauber.
- `Pillars-MG-3.md` — 4 Pillar-Artikel. QA-Check fehlt noch.
- `Pillars-MG-4.md` — 4 Pillar-Artikel. QA-Check fehlt noch.
- `Social-Content-Batch-1.md` — 15 LinkedIn + 8 IG Carousels + 8 Reel Scripts
- `Social-Content-Batch-2.md` — 10 LinkedIn Posts
- `Social-Content-Batch-3.md` — ~20 weitere Social Pieces (noch nicht im INVENTAR)
- `Prompt-Templates.md` — 9 wiederverwendbare Prompt-Templates für n8n

---

## 4. DER CONTENT-STIL (BINDEND FÜR ALLE AGENTS DIE CONTENT SCHREIBEN)

Dies ist nicht optional. Jeder Agent der für Ground-Zero Content schreibt, muss diese Regeln befolgen.

**Ton:**
- Direkt, professionell, kein Marketing-Bullshit
- Keine fluffigen Einleitungen wie "In der heutigen schnelllebigen Geschäftswelt..."
- Kein "Hallo zusammen" am Anfang von LinkedIn-Posts
- Keine Emojis außer maximal einem am Ende eines Posts
- Nicht predigen, nicht belehren — Fakten und Zahlen sprechen lassen

**Sprache:**
- Deutsch (primär). Vereinzelt englische Fachbegriffe sind okay (n8n, Workflow, CRM, ROI)
- Kein Denglisch wie "das ist sehr convenient" oder "wir leveragen das"

**Struktur (Hook-Rehook-Payoff für Social Content):**
- **Hook:** Erste Zeile. Zahl, konträres Statement oder konkreter Schmerz. Erzwingt "Mehr anzeigen"
- **Rehook:** 1–2 Sätze. Baut Spannung auf, gibt Kontext ohne die Auflösung zu verraten
- **Payoff:** 3–5 Sätze. Konkreter Wert, Zahlen, Handlungsempfehlung
- **CTA:** Frage am Ende die echte Kommentare provoziert (nicht "Was denkst du?" — zu generisch)

**Konkrete Beispiele für gute Hooks (nachgewiesen hohe Performance 2026):**
- "50 Stunden. Jede Woche. So viel Zeit verliert ein 10-Mann-Handwerksbetrieb durch manuelle Dokumentation."
- "Unpopular opinion: ChatGPT ist für die meisten kleinen Unternehmen reine Zeitverschwendung. Hier ist warum:"
- "Wir haben bei unserem letzten Kunden-Onboarding 40 Stunden verschwendet. Die Lektion war teuer, aber sie rettet deinen Prozess:"
- "Ist es klug oder fahrlässig, Kunden-E-Mails von einer KI beantworten zu lassen?"

**Was LinkedIn 2026 algorithmisch belohnt:**
- Document-Posts (Carousels) und Videos werden priorisiert
- Saves sind die wichtigste Metrik — wenn jemand speichert, erscheint der nächste Post mit 90% Wahrscheinlichkeit wieder in seinem Feed
- Die "Golden Hour" dauert 90 Minuten — wer nach dem Posten offline geht verliert drastisch Reichweite
- Rein KI-generiert wirkende Texte werden um bis zu 90% in der Reichweite gedrosselt → immer menschlich klingende Sprache
- LinkedIn Newsletter haben gerade +124% Reichweite für substanzielle Inhalte
- Externe Links im Post: schaden der Reichweite → Links in den ersten Kommentar

---

## 5. DAS AGENT-SYSTEM (WER MACHT WAS)

### Rollenverteilung

```
INSPEKTOR (Operator / Mensch)
├── Einziger strategischer Entscheider
├── Gibt Approvals für neue Richtungen
├── Führt externe Agents (Perplexity Pro, Gemini, Open Code + Nvidia API)
├── Bewertet finalen Content und gibt "Go" für Publishing
└── Schreibt NICHT selbst Content — delegiert alles

CLAUDE OPUS (interner Architekt — sparsam einsetzen!)
├── Nur für One-Shot-Reviews und strategische Planung
├── Liest alles, bewertet, gibt priorisierten Plan zurück
├── Schreibt KEINEN Content direkt
└── Trigger: explizite Anfrage vom Operator

CLAUDE SONNET (interner Qualitäts-Agent)
├── QA-Checks auf Haiku-Output
├── Schreibt strategische Dokumente (wie dieses hier)
├── Liest alle Kontext-Files zu Beginn jeder Session
├── Gibt dem Operator Copy-Paste-Prompts für externe Agents
└── Bereitet Opus-Briefings vor

CLAUDE HAIKU (interne Factory — die Arbeitstiere)
├── Haiku One (Scout): Filesystem-Scans, INVENTAR.md aktualisieren, Wörter zählen
├── Haiku Two (Factory): Content-Recycling, Batches schreiben, Formatierung
└── Haiku Three (Inspector): QA-Checks nach Checkliste, Link-Validierung

EXTERNER SCHWARM (vom Operator direkt gesteuert)
├── Perplexity Pro: Deep Research, Quellenrecherche mit Links
├── Gemini 2.1 Pro / Open Code + Nvidia API: Bulk-Content-Drafts (50+ Pieces)
└── Diese Agents bekommen fertige Prompts (unten in Abschnitt 7) vom Sonnet-Agent
```

### Wann welches Modell?

| Aufgabe | Modell | Begründung |
|---------|--------|------------|
| 50+ Social Posts am Stück schreiben | Gemini / Extern | Kostenlos, schnell, für repetitive Arbeit |
| Einzelnen hochwertigen Pillar-Artikel schreiben | Claude Sonnet | Qualität wichtiger als Speed |
| QA-Check: Entspricht das unseren Regeln? | Claude Sonnet oder Haiku Three | Checkliste abarbeiten |
| Research: Was machen Konkurrenten? | Perplexity Pro | Quellenverifizierung wichtig |
| Filesystem-Scan: Was haben wir schon? | Claude Haiku One | Günstig, nur lesen |
| Strategische Entscheidung: Welchen Kanal zuerst? | Claude Opus (One-Shot) | Nur wenn explizit vom Operator |
| Linear-Issues anlegen / updaten | Claude Sonnet | Als Teil des Standard-Task-Abschlusses |

---

## 6. WAS WIR AUS DER RESEARCH WISSEN (Welle 1 bis 4)

Alle Research-Files liegen unter `/Handover/research/`. Hier die Erkenntnisse (inklusive Welle 4 Update).

### WELLE 4 (April 2026): Legacy-Falle, AI-Act & Fake-Agenturen
*(Quelle: `Handover/research/Welle-3/AI-Powered Online Marketing 2026  GEO, Agents, and Autonomous Funnels.md`)*
- **Die Legacy-Falle:** Der DACH-Einzelhandel leidet massiv unter veralteten POS-Systemen (Vectron, Sage), die nicht mit Shopify synchronisieren. Dienstleister kämpfen mit fehlendem Kalender-Sync bei Treatwell und Doctolib. Dies sind unsere primären Ansatzpunkte für n8n-Architektur.
- **Die Fake-Agenturen:** Der Markt ist voll von "KI-Agenturen", die ChatGPT-Workshops für 3.000 € oder überteuerte Zapier/Make-Lösungen verkaufen (die durch Volumengebühren extrem teuer werden). VIRON grenzt sich durch "Infrastructure as a Service" (n8n auf Hetzner) ab.
- **EU AI-Act (August 2026):** Der AI Act tritt am 2. August 2026 voll in Kraft. US-Tools (OpenAI, Zapier) für automatisierte Kundenkommunikation oder Lead-Scoring werden zum massiven Compliance-Risiko (Schatten-IT). Dies ist unser stärkstes Verkaufsargument für selbstgehostete Lösungen.
- **Outbound Trigger:** Jobportale sind voll von Stellenanzeigen ("Datenpflege in Excel", "Systemabgleich"), die eigentlich fehlende APIs beschreiben. Google Reviews klagen über Doppelbuchungen und Fehlbestände. Dies sind Trigger für kaltes Outbound.

### Wettbewerber-Landschaft (aus Marketing-research.md, 54KB)
- 15 Competitor-Profile analysiert
- Alle verwenden ähnliche Themen: "KI für KMU", "Automatisierung spart Zeit"
- 4 identifizierte Content-Gaps die Konkurrenten NICHT abdecken:
  1. **Build-in-Public** (eigene Workflows zeigen, screen recordings)
  2. **Mitarbeiter-KI-Onboarding** (wie bringt man einem 55-jährigen Buchhalter KI bei?)
  3. **Interaktive Lead-Magneten** (statt PDFs: echte Interaktivität)
  4. **Nischen-Monopolisierung** (spezifisch DACH: Handwerk, Immobilien, Steuern — nicht "KMU allgemein")

### KMU-Schmerzpunkte nach Branche (konkrete Zahlen, direkt verwendbar in Posts)

**Handwerksbetriebe (5–20 Mitarbeiter):**
- 76% klagen über Bürokratie als Hauptproblem
- 50 Stunden/Woche verloren durch Dokumentensuche pro 10-Mann-Betrieb
- 10 Stunden/Woche durch händische Zeiterfassung auf Zetteln
- ROI bei Automatisierung: 1.800 €/Monat allein durch digitale Zeiterfassung
- Hauptblocker: 96% haben IT/Datenschutzbedenken, 69% scheuen Investitionskosten

**Immobilienmakler (Solo bis 10 Mitarbeiter):**
- Leads die nicht innerhalb 5 Minuten kontaktiert werden: 21× geringere Konversionsrate
- 15 Stunden/Woche verloren durch manuelle Beantwortung von Standard-Portalanfragen
- ROI bei Automatisierung: 3.000 €/Monat + 15% mehr Abschlüsse
- Hauptblocker: Angst, die persönliche Beziehung zum Kunden zu verlieren; Altdaten-Migration

**Steuerkanzleien (3–15 Mitarbeiter):**
- 20 Stunden/Woche pro 5-Mann-Kanzlei für manuelles Belege-Abtippen
- 15 Stunden/Woche durch Hinterhertelefonieren wegen fehlender Unterlagen
- ROI bei Automatisierung: 4.800 €/Monat in Fachkräfte-Kapazität freigesetzt
- Hauptblocker: DSGVO + § 203 StGB Steuergeheimnis, DATEV-Ökosystem-Lock-in

### LinkedIn-Algorithmus 2026 (360-Brew)
- Organische Reichweite global um ~50% eingebrochen seit dem Update
- **Saves** sind die wichtigste Metrik. 1 Save = 90% Wahrscheinlichkeit dass der nächste Post auch erscheint
- **Golden Hour** = 90 Minuten (nicht 60 wie vorher). "Post & Ghost" bestraft
- Document-Posts (Carousels) und Videos werden vom Algorithmus bevorzugt
- Rein KI-generiert erkannte Texte: bis zu 90% Reichweitenverlust
- LinkedIn Newsletter haben gerade +124% Reichweite für substanzielle Inhalte
- Posting-Zeiten DACH B2B: Di–Do, 07:30–08:30 und 10:00–11:30 und 15:30–17:00
- Absolute Peaks: Mittwoch 09:00 und Donnerstag 16:00

### Faceless Video (wichtige Erkenntnis für MKT-4)
- 65% der Top-Brands haben "Pure Faceless" aufgegeben — zu viel Vertrauensverlust
- Beste Lösung für B2B: **"Hook-and-Hold"** — 3 Sekunden Gesicht im Frame (+44% Engagement), dann switchen zu Screen-Recording mit KI-Voiceover
- Optimale Länge für Educational Content: 15–30 Sekunden
- 83% der Reel-Nutzer schauen ohne Ton → visueller Hook muss ohne Audio funktionieren
- Tech-Stack für Faceless-Automation: n8n + ElevenLabs + Shotstack + Cloudinary + Blotato

### 10 bewährte Hook-Formeln (datenbasiert, direkt verwendbar)

**Für LinkedIn:**
1. Datengetriebene Fallstudie: "[X% Verbesserung/Einsparung] — ohne [erwartete Methode]."
2. Konträrer Mythos: "Unpopular opinion: [gängige KI-Weisheit] ist schlechter Rat. Warum:"
3. Schmerzhafter Fehler: "Ich habe [X Stunden/€] verschwendet. Die Lektion spart dir..."
4. Entweder-Oder-Frage: "Ist es klug oder fahrlässig, [Prozess] zu automatisieren?"
5. Versteckte Realität: "Hör auf, [populärer Trend] zu machen. Ernsthaft. Lies das zuerst:"

**Für Reels/Videos:**
6. Stop-Scrolling Leak: "Stop. [Zielgruppe] verbrennt gerade [Ressource] mit [Prozess]."
7. Build-in-Public Beweis: "So automatisierst du [Prozess] in n8n in unter 60 Sekunden."
8. Behind the Scenes: "Was dir keine KI-Agentur über Automatisierung im Mittelstand sagt."
9. Asset-Drop (triggert Saves stark): "Ich habe [wertvolles Tool/Template] gebaut (und verschenke es)."
10. Vorher/Nachher: "Vorher: [manueller Prozess]. Nachher: [automatisiert]. Das ist der Unterschied."

---

## 7. EXTERNE AGENT-PROMPTS (FERTIG ZUM COPY-PASTE)

Diese Prompts können direkt in Perplexity Pro, Gemini oder Open Code eingegeben werden.

### Basis-Kontext-Block (immer als Einleitung anhängen)

```
KONTEXT FÜR DIESEN TASK:
Du arbeitest als Spezialist-Agent für Ground-Zero Agency Infrastructure, eine deutsche
KI-Automatisierungsagentur (Solo-Betrieb). Wir verkaufen maßgeschneiderte
Automatisierungs-Workflows (n8n, KI-Agenten, CRM-Integrationen) an KMU in DACH.

Unsere Zielgruppe: Geschäftsführer von Betrieben mit 5–50 Mitarbeitern.
Branchen-Fokus: Lokaler Einzelhandel, Premium-Dienstleister.
Ton: Direkt, professionell, keine Marketing-Floskeln, keine Emojis.
Sprache: Deutsch.
Keine Erwähnungen von OpenAI. n8n = primäres Automatisierungstool.
```

### PROMPT A — Nischen-ROI-Content (Priorität: HOCH)

```
[KONTEXT-BLOCK OBEN EINFÜGEN]

AUFGABE: Erstelle Social Content für 2 Branchen basierend auf diesen verifizierten Zahlen.

LOKALER EINZELHANDEL / RETAIL:
- Chaos zwischen Online-Shop (Shopify) und Kassen-System (POS)
- "Website als toter Prospekt" vs. "Website als 24/7 Verkäufer"
- ROI-Beispiel: 2.500 €/Monat gerettet durch automatisierte Inventar-Synchronisation und Retargeting verlassener Warenkörbe
- Haupteinwände: "Wir haben keine IT-Abteilung" (90%), Investitionsangst vor 5-15k € Projekten

PREMIUM-DIENSTLEISTER (Agenturen, Consultants, Therapeuten):
- 20 Stunden/Woche verloren durch Termin-Ping-Pong und manuelles Onboarding
- Leads, die nicht in 5 Minuten kontaktiert werden, sind 21x wahrscheinlicher tot
- ROI-Beispiel: 4.800 €/Monat freigesetzt durch automatisiertes Lead-Scoring, Auto-Booking und asynchrones Onboarding
- Haupteinwände: "Wir brauchen den persönlichen Touch", Angst vor standardisiertem "Roboter-Gefühl"

PRO BRANCHE ERSTELLE:
1. Fünf LinkedIn-Posts (je 150–250 Wörter)
   - Jeder Post mit einer der Formeln: Datengetriebene Fallstudie / Konträrer Mythos / Schmerzhafter Fehler
   - Hook mit konkreter Zahl starten, nicht mit "Hallo zusammen"
   - CTA am Ende: Frage die Diskussion auslöst
2. Zwei Reel-Scripts (je 15–30 Sekunden Sprechzeit)
   - Format: Vorher/Nachher-Visual + KI-Voiceover
   - Erste Zeile = Text-Overlay der ohne Ton funktioniert
3. Ein Carousel-Outline (5 Slides: Slide-Titel + 1-Satz-Inhalt pro Slide)

GESAMT: 10 LinkedIn Posts + 4 Reels + 2 Carousels = 16 Pieces

OUTPUT FORMAT: Strukturiertes Markdown. Pro Branche ein Abschnitt mit klarer Überschrift.
Jeden Post mit Kennung beginnen: [LI-Retail-01], [REEL-Services-01], etc.
```

### PROMPT B — Hook-Bibliothek Massenproduktion

```
[KONTEXT-BLOCK OBEN EINFÜGEN]

AUFGABE: Erstelle 30 LinkedIn-Post-Drafts nach 5 bewährten Hook-Formeln.
Pro Formel 6 Posts, je 150–200 Wörter. Sprache: Deutsch.

FORMEL 1 — Datengetriebene Fallstudie (6 Posts):
Format: "[Konkretes Resultat] — [überraschende Einschränkung/Methode]."
Themen: Lokaler Einzelhandel, Premium-Dienstleister, n8n-Workflow, Lead-Qualifizierung, E-Commerce-Sync

FORMEL 2 — Konträrer Mythos (6 Posts):
Format: "Unpopular opinion: [bekannte KI-Behauptung] ist schlechter Rat."
Themen: ChatGPT für KMU, Prompt-Engineering-Kurse, persönliche Beratung stirbt aus, Tool-Hype allgemein

FORMEL 3 — Schmerzhafter Fehler (6 Posts):
Format: "Wir haben [X Stunden/€] bei [Prozess] verbrannt. Was wir gelernt haben:"
Themen: Falsche Tool-Auswahl, schlechtes Onboarding, Daten-Chaos zwischen Shopify und POS, Termin-Ping-Pong

FORMEL 4 — Entweder-Oder-Frage (6 Posts):
Format: "Ist es [positiv] oder [negativ], [KI-Prozess] einzusetzen?"
Themen: KI im Kundenkontakt, automatisierte Terminbuchung, KI-Buchhaltung, Lead-Scoring

FORMEL 5 — Versteckte Realität (6 Posts):
Format: "Hör auf, [populäres Verhalten] zu machen. Ernsthaft. Lies das zuerst:"
Themen: Website als Visitenkarte nutzen, jedes Tool selbst einrichten, Leads erst morgen anrufen, manuelle Rechnungen schreiben

REGELN:
- Kein "Hallo zusammen"
- Hooks müssen zum Klick auf "Mehr anzeigen" zwingen
- Jeder Post endet mit einer Frage
- Keine Emojis außer maximal einem am Ende
- Kein OpenAI erwähnen

OUTPUT: Alle 30 Posts in einem Markdown-Dokument. Jeder mit Kennung [LI-F1-01] etc.
```

### PROMPT C — LinkedIn Algorithm-Serie (5 Posts)

```
[KONTEXT-BLOCK OBEN EINFÜGEN]

AUFGABE: Erstelle 5 LinkedIn-Posts über den LinkedIn 2026 Algorithmus.
Diese Posts zeigen, dass wir den Algorithmus verstehen — und bauen so Expertise auf.

POST 1 — Saves als Super-Metrik:
Fakten: 1 Save = 90% Wahrscheinlichkeit dass der nächste Post erscheint. Likes zählen kaum noch.
Frage am Ende: Was machst du konkret damit Leute deinen Post speichern?

POST 2 — Golden Hour 90 Minuten:
Fakten: Wer nach dem Posten 90 Minuten online bleibt und kommentiert, gewinnt 30–40% mehr Reichweite.
"Post & Ghost" wurde von 60 auf 90 Minuten ausgeweitet.

POST 3 — LinkedIn Newsletter Revival:
Fakten: +124% Reichweite für substanzielle Inhalte. Algorithmus pusht Newsletters für "Deep Dive"-Content.
Empfehlung: Mega-Guide als Newsletter-Artikel veröffentlichen.

POST 4 — KI-Content-Penalty:
Fakten: Rein KI-generiert wirkende Texte verlieren bis zu 90% Reichweite.
Empfehlung: Menschliche Handschrift in den Text einbauen (Fehler, persönliche Meinung, Zahlen aus eigener Erfahrung).

POST 5 — Mobile-First-Pflicht:
Fakten: 65% der LinkedIn-Nutzer sind mobil. Durchschnittliche Session: 1,27 Minuten.
Empfehlung: Keine Textblöcke ohne visuelle Struktur. Kurze Absätze. Hook muss in 2 Sekunden zünden.

FORMAT: Je Post 180–220 Wörter, Hook-Rehook-Payoff-Struktur, Kennungen [LI-ALGO-01] bis [LI-ALGO-05].
```

### PROMPT D — Pillar-zu-Post Recycling

```
[KONTEXT-BLOCK OBEN EINFÜGEN]

Du bekommst einen langen Artikel (Pillar oder Mega-Guide). Deine Aufgabe:
Zerlege den Artikel in 8 LinkedIn-Posts (je 150–200 Wörter) und 3 Carousel-Outlines.

Regeln:
- Jeder Post muss auch ohne den Artikel verständlich sein (eigenständiger Wert)
- Jeder Post muss eine der 5 Hook-Formeln verwenden (Fallstudie / Mythos / Fehler / Frage / Realität)
- Carousels: 5 Slides je, Slide-Titel + 2 Sätze Inhalt
- Am Ende jeden Posts: 1 Frage für Kommentare

[ARTIKEL HIER EINFÜGEN]

OUTPUT: 8 Posts mit Kennungen [RECYCLED-01] etc. + 3 Carousel-Outlines.
```

---

## 8. QUALITÄTSSICHERUNG — CHECKLISTE FÜR JEDEN CONTENT-PIECE

Jeder Haiku- oder extern generierte Content muss diese Punkte erfüllen, bevor er freigegeben wird:

```
QA-CHECKLISTE (abhaken oder mit FAIL markieren):

[ ] Hook: Startet mit Zahl, konträren Statement oder konkretem Schmerz? (kein "Hallo zusammen")
[ ] Ton: Direkt, kein Fluff, keine Marketing-Klischees?
[ ] ROI-Relevanz: Konkrete Zahlen, Einsparungen oder Ergebnisse erwähnt?
[ ] LinkedIn-Compliance: Kein externer Link im Post selbst? (Links in ersten Kommentar)
[ ] Saves-Trigger: Gibt es einen Grund den Post zu speichern? (Checkliste, Formel, Stat)
[ ] CTA: Frage am Ende die echte Kommentare provoziert? (nicht "Was denkst du?")
[ ] Keine Verbote verletzt: Kein OpenAI, Zapier nicht als primäre Empfehlung
[ ] Sprache: Kein Denglisch, kein KI-Kauderwelsch ("leveragen", "synergien")
[ ] Länge: 150–250 Wörter (LinkedIn), 15–30 Sek Sprechzeit (Reels)
[ ] KI-erkennbar: Klingt der Text menschlich oder generisch? (falls generisch: überarbeiten)
```

---

## 9. OFFENE PUNKTE (Backlog, nach Priorität)

| Prio | Aufgabe | Wer | Status |
|------|---------|-----|--------|
| 🔴 HOCH | MG-1 Zeile ~443: OpenAI-Referenz entfernen | Sonnet | Pending |
| 🔴 HOCH | Nischen-ROI-Content (18 Pieces, Prompt A) | Operator → Extern | Pending |
| 🟡 MITTEL | Zapier-Framing in Pillars-MG-1 angleichen | Haiku Two | Pending |
| 🟡 MITTEL | Pillars-MG-3 + MG-4 QA-Check | Sonnet / Haiku Three | Pending |
| 🟡 MITTEL | Social-Content-Batch-3 in INVENTAR.md einpflegen | Haiku One | Pending |
| 🟢 NIEDRIG | Hook-Bibliothek (30 Posts, Prompt B) | Operator → Extern | Geplant |
| 🟢 NIEDRIG | LinkedIn-Algo-Serie (5 Posts, Prompt C) | Haiku Two | Geplant |
| 🟢 NIEDRIG | Pillar → Post Recycling für MG-3 + MG-4 (Prompt D) | Extern | Geplant |

---

## 10. WIE EINE NEUE SESSION STARTEN SOLL

Dieser Block ist für Claude-Agents die diesen Chat von vorne aufnehmen.

```
START-SEQUENZ (zwingend in dieser Reihenfolge):

Schritt 1: Lies /Work-Lab/CLAUDE.md vollständig (Kontext-Bibel)
Schritt 2: Lies /Work-Lab/Content/INVENTAR.md (aktueller Content-Stand)
Schritt 3: Lies /Work-Lab/Handover/ORCHESTRATION_SYSTEM.md (diese Datei)
Schritt 4 (optional): Lies neue Files in /Work-Lab/Handover/research/ wenn vorhanden
Schritt 5: Melde dich beim Operator mit kurzem Status:
  - Was haben wir? (1 Satz)
  - Was sind die offenen Punkte? (Top 3 aus Abschnitt 9)
  - Was schlägst du als nächsten Schritt vor? (1 Empfehlung)
Schritt 6: Warte auf Operator-Approval bevor du irgendwas ausführst
```

---

*Zuletzt aktualisiert: 19.03.2026 von Claude Sonnet*
*Nächste Pflicht-Review: Nach Abschluss von Backlog-Prio-🔴 Punkten*
