# OPUS ONE-SHOT BRIEFING
**Zweck:** Vollständiger Kontext für einen einzigen, fokussierten Opus-Review.
**Erwarteter Output:** Strategischer Bewertungsbericht + priorisierter Execution-Plan.
**Danach:** Opus gibt dieses Dokument zurück. Sonnet setzt um.

---

## DEINE ROLLE

Du bist Claude Opus im VIRON-System. Deine Aufgabe ist NICHT Content zu schreiben.
Deine Aufgabe ist:
1. Den aktuellen Stand des Systems zu bewerten (was läuft gut, was ist falsch priorisiert?)
2. Die 5 neuen Research-Erkenntnisse einzuordnen (was davon hat echten strategischen Wert?)
3. Einen priorisierten Plan für die nächsten 30 Tage zu liefern
4. Klar zu sagen was der Operator JETZT tun soll und was er delegieren soll

Du schreibst KEINEN Content. Du liest, denkst, bewertest, planst. Das ist alles.

---

## DAS UNTERNEHMEN

**Ground-Zero Agency Infrastructure** ist eine Solo-KI-Automatisierungsagentur in Deutschland.
Betreiber: Inspektor (technisch versiert, Zeitdruck, lösungsorientiert).
Verkauft: Maßgeschneiderte n8n-Workflows, KI-Agenten, CRM-Integrationen an KMU im DACH-Raum.
Phase: Aufbau. Noch kein Kundenstamm. Marketing ist der einzige Akquise-Kanal gerade.

**Zielkunde:** Geschäftsführer von Betrieben mit 5–50 Mitarbeitern.
Prioritäre Branchen: Handwerksbetriebe, Immobilienmakler, Steuerkanzleien.
Schmerzpunkte: Zeitverlust durch manuelle Prozesse, kein funktionierendes CRM, zu wenig Kapazität für Digitalisierung.

**Tool-Regeln die du kennen musst:**
- n8n = primäres Automatisierungstool (kein Zapier als Primary)
- OpenAI = VERBOTEN in jedem Kontext
- Python 3.11 (nicht 3.12)
- Notion = read-only für Agents
- Linear = Source of Truth für alle Tasks

---

## DER CONTENT-PLAN (KONTEXT)

Die Agentur hat eine Content-Pyramide als Marketing-Strategie:
- 4 Mega-Guides (tiefe Artikel, 3.000–7.000 Wörter) → Google-Traffic, Autorität
- 16 Pillar-Artikel (800–1.500 Wörter) → Longtail, Recycling-Basis
- ~450 Social Pieces (LinkedIn, IG, Reels, TikTok) → tägliche Sichtbarkeit, Leads

**Aktueller Stand:**
- Mega-Guides: 4/4 ✅ fertig
- Pillar-Artikel: 67/16 ✅ massiv überproduktiv (SEO-wertvoll, aber kein akutes Problem)
- Social Pieces: ~41/450 ⏳ (9%) — das ist die Hauptbaustelle

**Bekannte Qualitätsprobleme:**
- MG-1 enthält eine OpenAI-Referenz (Zeile ~443) — muss gefixt werden
- Pillars-MG-1 hat Zapier als gleichwertiges Tool beschrieben statt als Fallback
- Pillars-MG-3 + MG-4 haben noch keinen QA-Check bekommen
- Social-Content-Batch-3 ist nicht im INVENTAR erfasst

---

## DIE 5 RESEARCH-ERKENNTNISSE (WELLE 2)

Diese Erkenntnisse kommen aus Perplexity-Recherchen die der Operator durchgeführt hat.

### 1. LinkedIn-Algorithmus 2026 (360-Brew Update)
- Organische Reichweite global um ~50% eingebrochen
- **Saves** sind die neue Leitwährung. 1 Save = 90% Wahrscheinlichkeit künftiger Sichtbarkeit
- "Golden Hour" = 90 Minuten (wer nach Post offline geht verliert Reichweite)
- Rein KI-generierte Texte: bis zu 90% Reichweitenverlust
- LinkedIn Newsletter: +124% Reichweite für substanzielle Inhalte
- Document-Posts (Carousels) + Videos werden algorithmisch bevorzugt
- Externe Links im Post schaden der Reichweite
- DACH-Peaks: Di–Do, 07:30–08:30 und 10:00–11:30

### 2. KMU-Schmerzpunkte (konkrete Zahlen, verwendbar in Posts)
- **Handwerk:** 50h/Woche Dokumentenverlust pro 10-MA-Betrieb, ROI bei Automatisierung: 1.800€/Monat
- **Immobilien:** Leads 21× wahrscheinlicher wenn <5 Min Reaktion, ROI: 3.000€/Monat
- **Steuerberater:** 20h/Woche Belege abtippen, ROI: 4.800€/Monat (DATEV-DSGVO Kontext)

### 3. Faceless Video B2B-Realität
- 65% der Top-Brands haben "Pure Faceless" aufgegeben → Vertrauensverlust
- Lösung: "Hook-and-Hold" — 3 Sek Gesicht (+44% Engagement), dann Screen-Recording
- Optimale Länge: 15–30 Sekunden
- 83% schauen ohne Ton → visueller Text-Overlay ist Pflicht

### 4. 10 datenbasierte Hook-Formeln (LinkedIn + Reels)
Fünf LinkedIn-Formeln: Datengetriebene Fallstudie, Konträrer Mythos, Schmerzhafter Fehler, Entweder-Oder-Frage, Versteckte Realität. Alle mit DACH-Beispielen vorhanden.
Fünf Reel-Formeln: Stop-Scrolling Leak, Build-in-Public, Behind-the-Scenes, Asset-Drop (Saves!), Vorher/Nachher.

### 5. BAFA-Förderung als Content-Angle (ACHTUNG: Kontext wichtig)
**Was es ist:** BAFA = deutsches Bundesamt für Wirtschaft. Fördert KMU bei KI-Projekten.
- Bundesebene: max. 2.800€ nur für Beratung (nicht technische Umsetzung)
- Bayern: bis 30.000€ für technische KI-Umsetzung durch externe Dienstleister
- NRW: bis 15.000€ für externe Implementierung
- Konkurrenten benutzen das bereits eingestellte "go-digital"-Programm noch als Lead-Magnet (obwohl es seit 31.12.2024 nicht mehr existiert)

**Relevanz für Ground-Zero:** Zwei mögliche Winkel:
  A) Content-Marketing: "Wir erklären KMUs wie sie ihre KI-Projekte fördern lassen" → qualifizierter Lead-Magnet
  B) Business-Modell: BAFA-Akkreditierung als Berater → Kunden können Beratungshonorare fördern lassen

**Problem:** Der Operator hat dieses Thema NICHT aktiv initiiert — es kam aus dem Research. Der Operator hat Bedenken ob BAFA für ihn relevant ist. Er ist nicht akkreditiert und will das nicht unbedingt ändern. Deine Bewertung: Ist der reine Content-Winkel (A) es wert ohne Akkreditierung? Oder ist das verlorene Energie?

---

## DAS AGENT-SYSTEM

```
Inspektor (Operator) — orchestriert extern: Perplexity Pro, Gemini 2.1 Pro, Open Code + Nvidia
Claude Opus (du) — One-Shot Review + Strategie
Claude Sonnet — QA, strategische Docs, gibt Operator externe Agent-Prompts
Claude Haiku — Factory: Scans, Content-Batches, Recycling
```

**Wichtig:** Der Operator hat eigene externe Agents (Open Code + Nvidia, Gemini 2.1 Pro) für Bulk-Content. Das bedeutet: Interne Claude-Agents sollen nicht Bulk-Content schreiben — dafür gibt es externe Kapazität. Interne Agents = Strategie + QA + Orchestrierung.

---

## DEINE AUFGABE (Opus)

Erstelle einen strukturierten Review-Bericht mit diesen 5 Abschnitten:

### Abschnitt 1: System-Bewertung
Bewertet den aktuellen Stand der Content-Pyramide. Was läuft gut? Was ist falsch gewichtet?
Ist die 450-Social-Pieces-Zahl realistisch und sinnvoll? Oder gibt es einen besseren Fokus?

### Abschnitt 2: Research-Bewertung
Für jede der 5 Research-Erkenntnisse: Wie hoch ist der strategische Wert für Ground-Zero konkret?
Ranking von 1–5 (5 = sofort umsetzen, 1 = vernachlässigen).
Speziell: BAFA — Content-Winkel ohne Akkreditierung: ja oder nein? Begründung.

### Abschnitt 3: Content-Strategie-Empfehlung
Was ist der schärfste Content-Fokus für die nächsten 30 Tage?
Konkrete Empfehlung: Welche 3 Content-Serien soll Ground-Zero priorisieren?
Warum diese 3 und nicht andere?

### Abschnitt 4: Delegations-Plan
Was macht der Operator selbst (externe Agents starten)?
Was macht Sonnet intern?
Was macht Haiku intern?
Klare Zuordnung, keine Überschneidungen.

### Abschnitt 5: Kritische Fragen an den Operator
Maximal 5 Fragen die du für strategisch relevant hältst und die du ohne Operator-Input nicht beantworten kannst. Priorisiert, mit kurzer Begründung warum diese Frage wichtig ist.

---

## FORMAT DEINES OUTPUTS

- Strukturiertes Markdown
- Klare Abschnittsüberschriften
- Keine ausschweifenden Erklärungen — kurz, präzise, operativ
- Am Ende: Eine einzige "Nächste-Aktion"-Empfehlung (was soll der Operator als ERSTES tun, heute noch?)
- Geschätzte Zeitinvestition pro empfohlenen Schritt

**Scope:** Nur Analyse und Plan. Schreibe keinen Content, erstelle keine Social-Posts, keine Artikel.
