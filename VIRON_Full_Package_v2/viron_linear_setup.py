# VIRON LINEAR SETUP SCRIPT
# Ziel: Vollständigen Linear-Workspace für VIRON aufbauen
# Ausführung: Claude Code / AntiGravity Agent / direkt als Python-Script
# Voraussetzung: LINEAR_API_KEY als ENV-Variable gesetzt
# API Docs: https://developers.linear.app/docs/graphql/working-with-the-graphql-api

import os
import json
import requests

API_KEY = os.environ.get("LINEAR_API_KEY", "YOUR_KEY_HERE")
HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}
URL = "https://api.linear.app/graphql"

def gql(query, variables=None):
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    r = requests.post(URL, headers=HEADERS, json=payload)
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise Exception(f"GraphQL Error: {data['errors']}")
    return data["data"]

# ─────────────────────────────────────────────
# STEP 0: Workspace-ID holen
# ─────────────────────────────────────────────
def get_organization_id():
    q = """
    query {
      organization {
        id
        name
      }
    }
    """
    result = gql(q)
    org = result["organization"]
    print(f"✅ Workspace: {org['name']} | ID: {org['id']}")
    return org["id"]

# ─────────────────────────────────────────────
# STEP 1: Teams anlegen
# ─────────────────────────────────────────────
TEAMS = [
    {"name": "GROUND ZERO",        "key": "GRO", "description": "Engineering, R&D, n8n, MCP, GraphRAG, Agenten-Bau"},
    {"name": "Marketing",          "key": "MKT", "description": "Content Creation, Video, Social Media, Freebies, Branding"},
    {"name": "Sales & Outreach",   "key": "SAL", "description": "Lead Scraping, Cold Email, IG/LinkedIn DM Automation"},
    {"name": "Fulfillment",        "key": "FUL", "description": "Kundenprojekte, Webdesign, Service Delivery"},
    {"name": "Operations",         "key": "OPS", "description": "Backoffice, Task Management, Finanzen, Onboarding"},
]

CREATE_TEAM = """
mutation CreateTeam($input: TeamCreateInput!) {
  teamCreate(input: $input) {
    success
    team { id name key }
  }
}
"""

def create_teams():
    created = {}
    for t in TEAMS:
        try:
            result = gql(CREATE_TEAM, {"input": {
                "name": t["name"],
                "key": t["key"],
                "description": t["description"]
            }})
            team = result["teamCreate"]["team"]
            created[t["key"]] = team["id"]
            print(f"  ✅ Team [{t['key']}] {t['name']} → {team['id']}")
        except Exception as e:
            print(f"  ⚠️  Team [{t['key']}] bereits vorhanden oder Fehler: {e}")
    return created

# ─────────────────────────────────────────────
# STEP 2: Globale Labels anlegen (je Team)
# ─────────────────────────────────────────────
LABELS = [
    {"name": "#build",        "color": "#4A90D9", "description": "Aufbau / Implementierung"},
    {"name": "#learn",        "color": "#F5A623", "description": "Recherche / Tutorial durcharbeiten"},
    {"name": "#use",          "color": "#7ED321", "description": "Wiederkehrende operative Nutzung"},
    {"name": "#freebie",      "color": "#BD10E0", "description": "Lead Magnet / Freebie Produktion"},
    {"name": "#core-system",  "color": "#D0021B", "description": "Kritische Infrastruktur"},
    {"name": "#experiment",   "color": "#9B9B9B", "description": "Tests, A/B, Prototypen"},
]

CREATE_LABEL = """
mutation CreateLabel($input: IssueLabelCreateInput!) {
  issueLabelCreate(input: $input) {
    success
    issueLabel { id name }
  }
}
"""

def create_labels(team_ids):
    label_map = {}
    for team_key, team_id in team_ids.items():
        label_map[team_key] = {}
        for lbl in LABELS:
            try:
                result = gql(CREATE_LABEL, {"input": {
                    "name": lbl["name"],
                    "color": lbl["color"],
                    "description": lbl["description"],
                    "teamId": team_id
                }})
                lid = result["issueLabelCreate"]["issueLabel"]["id"]
                label_map[team_key][lbl["name"]] = lid
                print(f"  ✅ Label [{team_key}] {lbl['name']} → {lid}")
            except Exception as e:
                print(f"  ⚠️  Label {lbl['name']} in {team_key}: {e}")
    return label_map

# ─────────────────────────────────────────────
# STEP 3: Projekte anlegen
# ─────────────────────────────────────────────
PROJECTS = [
    {
        "name": "Marketing Engine Phase I – Fundament & Quick Wins",
        "description": "Reputation sichern, Freebies bauen, erste IG/Social Leads. Zeitraum: Q2–Q3 2026.",
        "team_key": "MKT",
    },
    {
        "name": "Marketing Engine Phase II – Scale & Skalierung",
        "description": "Vollständige Video-Engine, Virality OS, LinkedIn Brand Engine, Apollo Outbound. Zeitraum: Q4 2026 – 2027.",
        "team_key": "MKT",
    },
    {
        "name": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "description": "AI Marketing Team als Kundenprodukt, AI Clone Creator, Longform, 4K. Zeitraum: 2027–2028.",
        "team_key": "MKT",
    },
    {
        "name": "Sales & Outreach Engine 2026–2028",
        "description": "Inbound (IG Outreach) + Outbound (Apollo + Cold Email + LinkedIn DM).",
        "team_key": "SAL",
    },
    {
        "name": "Ground0 Engineering Setup",
        "description": "AntiGravity, n8n, MCP, GraphRAG, Hetzner/Coolify Infrastruktur.",
        "team_key": "GRO",
    },
]

CREATE_PROJECT = """
mutation CreateProject($input: ProjectCreateInput!) {
  projectCreate(input: $input) {
    success
    project { id name }
  }
}
"""

GET_TEAMS = """
query {
  teams {
    nodes { id key }
  }
}
"""

def create_projects(team_ids):
    project_map = {}
    for p in PROJECTS:
        team_id = team_ids.get(p["team_key"])
        if not team_id:
            print(f"  ⚠️  Team {p['team_key']} nicht gefunden, Projekt übersprungen.")
            continue
        try:
            result = gql(CREATE_PROJECT, {"input": {
                "name": p["name"],
                "description": p["description"],
                "teamIds": [team_id]
            }})
            pid = result["projectCreate"]["project"]["id"]
            project_map[p["name"]] = pid
            print(f"  ✅ Projekt: {p['name']} → {pid}")
        except Exception as e:
            print(f"  ⚠️  Projekt {p['name']}: {e}")
    return project_map

# ─────────────────────────────────────────────
# STEP 4: Issues anlegen
# ─────────────────────────────────────────────
# Jedes Issue hat: title, description (Markdown), team_key, project_name, labels, priority
# priority: 0=None, 1=Urgent, 2=High, 3=Medium, 4=Low

ISSUES = [
    # ── Phase I – Fundament ──────────────────────────────
    {
        "title": "[BUILD] Auto-Moderation: Negative Kommentare sofort löschen",
        "team_key": "MKT",
        "project": "Marketing Engine Phase I – Fundament & Quick Wins",
        "labels": ["#build", "#freebie"],
        "priority": 2,
        "description": """## Ziel
Sicherung der Brand-Reputation durch einen automatisierten Make-Workflow, der negative Kommentare auf IG/FB filtert und löscht. Dient gleichzeitig als erstes einfaches Freebie für KMU-Kunden.

## Notion Asset
https://www.notion.so/2849129c75bf8196aa3ecac1fb92761c

## Action Items
- [ ] Make.com Workflow nach Notion-Vorlage aufbauen
- [ ] Sentiment-Analyse (OpenAI Node) für "toxisch/negativ" kalibrieren
- [ ] Test-Run auf VIRON Test-Account
- [ ] Flow als JSON exportieren → Freebie in Notion verpacken"""
    },
    {
        "title": "[BUILD] IG Idea Scraper für Content-Recycling",
        "team_key": "MKT",
        "project": "Marketing Engine Phase I – Fundament & Quick Wins",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
Automatisches Scrapen von IG-Posts aus der Ziel-Nische zur Ideengenerierung. Füttert den Content-Kalender und den Faceless Video Creator.

## Notion Asset
https://www.notion.so/2849129c75bf81fa8865ca1210e5e02b

## Action Items
- [ ] Apify Actor oder Make-Scenario nach Vorlage konfigurieren
- [ ] Output in Google Sheet / Airtable schreiben
- [ ] Filter für Relevanz / Engagement setzen"""
    },
    {
        "title": "[USE] YouTube Content Strategist – wöchentliche Themenliste",
        "team_key": "MKT",
        "project": "Marketing Engine Phase I – Fundament & Quick Wins",
        "labels": ["#use", "#learn"],
        "priority": 3,
        "description": """## Ziel
Regelmäßige (wöchentliche) Nutzung des YouTube Content Strategist Flows, um Themen und Keywords für die nächste Video-Produktion zu identifizieren.

## Notion Asset
https://www.notion.so/2849129c75bf8126b4defb72117b17bf

## Action Items
- [ ] Flow einmalig konfigurieren
- [ ] Jeden Montag ausführen → Output-Liste in Notion-Kalender übertragen"""
    },
    # ── Phase II – Scale ─────────────────────────────────
    {
        "title": "[BUILD] Faceless POV Video Engine",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#core-system"],
        "priority": 1,
        "description": """## Ziel
Aufbau der automatisierten Produktion von Faceless POV-Videos (B-Roll, Reels, Shorts) ohne manuellen Schnitt.

## Notion Asset
https://www.notion.so/2849129c75bf810d808bca0dd9e00b9e

## Blocked By
- [BUILD] Auto-Moderation: Negative Kommentare (Reputation erst sichern)

## Action Items
- [ ] n8n/Make-Flow nach Vorlage importieren
- [ ] API-Keys (Gemini / Runway / Sora) hinterlegen
- [ ] Hook-Logik aus Video-Hook Training einbauen
- [ ] 3 Test-Videos produzieren und QA"""
    },
    {
        "title": "[BUILD] Veo3 High-End Video Pipeline",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#core-system"],
        "priority": 2,
        "description": """## Ziel
Hochwertige Video-Ad und B-Roll-Produktion via Veo3 AI. Ergänzt den Faceless Creator für Premium-Inhalte.

## Notion Assets
- Generator: https://www.notion.so/2849129c75bf81238d3beb278fe14461
- Automation System: https://www.notion.so/2849129c75bf81a183a8d7bf296605bf

## Action Items
- [ ] Veo3 API-Zugang einrichten
- [ ] Automatisierungs-System aufbauen (Queue → Render → Output)
- [ ] Output direkt in Publishing Agent übergeben"""
    },
    {
        "title": "[BUILD] Video Analyzer für Hook- & Performance-Auswertung",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
Analyse bestehender Videos auf Hook-Qualität, Retention-Pattern und Engagement. Liefert Input für bessere Skripte.

## Notion Asset
https://www.notion.so/2849129c75bf816d876fef4f488bec6f

## Action Items
- [ ] Flow aufbauen
- [ ] Benchmark-Daten aus YouTube/TikTok Viral Searcher einspeisen
- [ ] Output als Skript-Briefing formatieren"""
    },
    {
        "title": "[BUILD] YouTube Viral Content Radar",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
Automatisches Monitoring viraler YouTube-Videos in der Nische (KI, Automatisierung, Solopreneur) zur Themen- und Format-Inspiration.

## Notion Asset
https://www.notion.so/2849129c75bf81b7a444d288e503d772

## Action Items
- [ ] Scraper konfigurieren (Keywords, Kanal-Filter, Min. Views)
- [ ] Output täglich in Airtable/Notion schreiben"""
    },
    {
        "title": "[BUILD] TikTok Viral Trend Radar",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
TikTok-spezifisches Monitoring für virale Trends in der Ziel-Nische. Füttert den Virality OS Workflow #1.

## Notion Asset
https://www.notion.so/2849129c75bf81e299bcedbd858da00c

## Action Items
- [ ] TikTok Scraper (Apify) konfigurieren
- [ ] Trend-Filter nach Engagement-Rate setzen
- [ ] Output täglich an Virality OS übergeben"""
    },
    {
        "title": "[BUILD] Instagram Viral Trend Radar",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
Instagram-spezifisches Trend-Monitoring zur Identifikation viraler Reels und Posts.

## Notion Asset
https://www.notion.so/2849129c75bf818d909edda5aceb6221

## Action Items
- [ ] IG Scraper einrichten
- [ ] Output in gemeinsames Trend-Dashboard schreiben"""
    },
    {
        "title": "[BUILD] AI Ad Content Creator (100 Varianten aus 1 Asset)",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#core-system"],
        "priority": 2,
        "description": """## Ziel
Skalierung eines einzelnen Inhalts (Video, Bild, Text) in 10–100 Ad-Varianten für verschiedene Plattformen und Zielgruppen.

## Notion Asset
https://www.notion.so/2849129c75bf81adb37de3305ae8dd66

## Action Items
- [ ] Flow nach Notion-Vorlage bauen
- [ ] Output-Formate definieren: FB, IG, LinkedIn, YT Pre-Roll
- [ ] A/B-Test-Logik einbauen"""
    },
    {
        "title": "[BUILD] Facebook Ad Creative Generator",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
Automatisierte Erstellung von Facebook Ad Creatives (Text, Bild, Headline-Varianten).

## Notion Asset
https://www.notion.so/2849129c75bf81a685d3c936ec73d268

## Action Items
- [ ] Generator-Flow aufbauen
- [ ] Swipe-File aus Facebook Ad Spy System als Trainings-Input nutzen"""
    },
    {
        "title": "[BUILD] Facebook Ad Spy & Swipe-File Automation",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#learn"],
        "priority": 3,
        "description": """## Ziel
Automatisches Sammeln erfolgreicher Facebook Ads der Nische als Inspirations-Datenbank.

## Notion Asset
https://www.notion.so/2849129c75bf816f9f77c0e256de8074

## Action Items
- [ ] FB Ad Library Scraper einrichten
- [ ] Output nach Kategorie (Hook, CTA, Format) strukturieren
- [ ] In Notion Swipe-File schreiben"""
    },
    {
        "title": "[BUILD] Product Ad Generator (Multi-Format)",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
Produkt-Ad-Generierung für verschiedene Formate (Static, Video, Story) aus einem einfachen Produkt-Input.

## Notion Asset
https://www.notion.so/2849129c75bf812d9310e88784bb6555

## Action Items
- [ ] Flow nach Vorlage aufbauen
- [ ] Anbindung an Auto Graphic Design System"""
    },
    {
        "title": "[BUILD] Auto Graphic Design Engine (Posts & Thumbnails)",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 2,
        "description": """## Ziel
Automatische Erstellung von Social Media Posts, Thumbnails und Carousel-Grafiken ohne manuelle Design-Arbeit.

## Notion Asset
https://www.notion.so/2849129c75bf81bbbd97da26ab50d5f0

## Action Items
- [ ] Canva API oder Bannerbear/Placid integrieren
- [ ] Templates für VIRON Brand Voice erstellen
- [ ] Output direkt in Carousel Auto-Poster übergeben"""
    },
    {
        "title": "[BUILD] Carousel Auto-Posting (IG + LinkedIn)",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#use"],
        "priority": 3,
        "description": """## Ziel
Automatisches Planen und Posten von Carousels auf Instagram und LinkedIn.

## Notion Asset
https://www.notion.so/2849129c75bf8102930ce5e54d59ab23

## Action Items
- [ ] Scheduling-Logik (Wochentage/Uhrzeiten) definieren
- [ ] API-Verbindungen zu IG und LinkedIn einrichten
- [ ] Test-Run mit 3 Beispiel-Carousels"""
    },
    {
        "title": "[BUILD] LinkedIn Brand Engine Rollout",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#core-system"],
        "priority": 2,
        "description": """## Ziel
Aufbau eines konsistenten, automatisierten LinkedIn-Profil-Managements für maximale Founder-Sichtbarkeit.

## Notion Asset
https://www.notion.so/2849129c75bf8183ac57e34d598176b9

## Action Items
- [ ] Posting-Frequenz und Content-Mixtur festlegen
- [ ] Auto-Posting Flow einrichten
- [ ] LinkedIn Performance Analyzer verknüpfen"""
    },
    {
        "title": "[BUILD] LinkedIn Performance Analyzer",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#use"],
        "priority": 3,
        "description": """## Ziel
Wöchentliche Analyse der LinkedIn-Post-Performance. Identifiziert Top-Formate und Optimierungspotenziale.

## Notion Asset
https://www.notion.so/2849129c75bf813596b2fd8a156f0014

## Action Items
- [ ] LinkedIn Analytics API anbinden
- [ ] Automatisierten Weekly Report bauen"""
    },
    {
        "title": "[BUILD] AI SEO Writer für Blogartikel",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
KI-basierte Erstellung SEO-optimierter Blogartikel aus einem Keyword-Input. Füttert den SEO Blog Automation Flow.

## Notion Asset
https://www.notion.so/2849129c75bf8138b4f0dd58eee8bfd4

## Action Items
- [ ] Keyword → Outline → Artikel Pipeline bauen
- [ ] Interno-Link-Logik einbauen
- [ ] Output direkt in CMS (z.B. WordPress) publishen"""
    },
    {
        "title": "[BUILD] SEO Blog Automation Engine",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#core-system"],
        "priority": 2,
        "description": """## Ziel
Kompletter End-to-End Funnel: Keyword-Recherche → KI-Artikel → SEO-Optimierung → Auto-Publish.

## Notion Asset
https://www.notion.so/2849129c75bf81eeac6bfc76ace8c6db

## Blocked By
- [BUILD] AI SEO Writer für Blogartikel

## Action Items
- [ ] Ahrefs/SEMrush oder kostenlose Alternative für Keyword-Daten anbinden
- [ ] Publishing Pipeline (WordPress/Ghost API) konfigurieren
- [ ] Monitoring: Rankings via Google Search Console tracken"""
    },
    {
        "title": "[BUILD] Viral Shorts Generator (Template-Engine)",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build"],
        "priority": 2,
        "description": """## Ziel
Automatisches Erzeugen viraler Short-Form-Videos aus bestehendem Longform-Content (Blog, Podcast, Video).

## Notion Asset
https://www.notion.so/2849129c75bf81129279de475538b588

## Action Items
- [ ] Input-Quellen definieren (Blog, YT-Video, Podcast)
- [ ] KI-Schnitt-Logik konfigurieren
- [ ] Output: 60s Shorts für TikTok/IG/YT"""
    },
    {
        "title": "[BUILD] Ultimate Publishing Agent (Rollout)",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#core-system"],
        "priority": 1,
        "description": """## Ziel
Zentrale Distributions-Maschine. Nimmt fertigen Content aus allen Produktions-Flows und verteilt ihn vollautomatisch auf alle Plattformen.

## Notion Asset
https://www.notion.so/2459129c75bf80868be1d5f05c8270b1

## Blocked By
- [BUILD] Faceless POV Video Engine
- [BUILD] Veo3 High-End Video Pipeline
- [BUILD] Carousel Auto-Posting (IG + LinkedIn)

## Action Items
- [ ] N8N/Make Workflow nach Notion-Vorlage aufbauen
- [ ] API-Verbindungen: IG, TikTok, LinkedIn, YouTube
- [ ] Caption-Generator (KI) pro Plattform anpassen
- [ ] Error-Logging via Notion oder Slack Channel
- [ ] Testlauf: 3 Videos, alle Plattformen"""
    },
    {
        "title": "[BUILD] Virality OS – TikTok, IG, YT Multi-Channel Radar",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#build", "#core-system"],
        "priority": 2,
        "description": """## Ziel
Inbetriebnahme des 7-stufigen AI-Content Virality OS. Scannt permanent TikTok, IG, YT auf Trends und generiert automatisch Viral Playbooks.

## Notion Asset
- Root: https://www.notion.so/2249129c75bf80d9a7b1c1471d23c0c3
- Workflow #1 (TikTok): https://www.notion.so/2249129c75bf807a9e50e401882a24e1

## Blocked By
- [BUILD] TikTok Viral Trend Radar
- [BUILD] YouTube Viral Content Radar
- [BUILD] Instagram Viral Trend Radar

## Action Items
- [ ] Airtable-Base nach Notion-Doku aufsetzen
- [ ] n8n Workflows 1–7 importieren und verknüpfen
- [ ] Testlauf: Viral Playbook für Nische "KI Automatisierung" generieren
- [ ] Scraping-Limits definieren (Anti-Ban-Schutz)"""
    },
    {
        "title": "[LEARN] Marketing Advanced Prompts – Prompt-Bank aufbauen",
        "team_key": "MKT",
        "project": "Marketing Engine Phase II – Scale & Skalierung",
        "labels": ["#learn"],
        "priority": 4,
        "description": """## Ziel
Systematisches Durcharbeiten und Kuratieren der Marketing Advanced Prompts als interne Prompt-Bibliothek für ROI-Analysen, Kampagnenplanung und Content-Generierung.

## Notion Asset
https://www.notion.so/17e9129c75bf801c8491c066f52f064a

## Action Items
- [ ] Alle Prompts kategorisieren (Kampagne, Content, ROI, Analyse)
- [ ] Beste Prompts in VIRON Prompt-Library (Notion) übernehmen"""
    },
    # ── Phase III – Dominanz ──────────────────────────────
    {
        "title": "[BUILD] Newsletter Automation Engine",
        "team_key": "MKT",
        "project": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "labels": ["#build", "#core-system"],
        "priority": 2,
        "description": """## Ziel
Vollautomatisierter Newsletter-Flow: News scrapen → KI kuratiert → personalisiert → verschickt.

## Notion Asset
https://www.notion.so/2849129c75bf81deac28d24a52fc5a5a

## Action Items
- [ ] Themen-Quellen definieren (RSS, Perplexity, Twitter/X)
- [ ] KI-Zusammenfassungs-Flow bauen
- [ ] Versand über Mailerlite/Brevo API automatisieren"""
    },
    {
        "title": "[BUILD] AI Marketing Team (Kundenprodukt)",
        "team_key": "MKT",
        "project": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "labels": ["#build", "#core-system"],
        "priority": 1,
        "description": """## Ziel
Verpackung aller internen Marketing-Automations (Video Engine, Publishing Agent, Virality OS) als einfaches, kundentaugliches Produkt. Der Kunde kriegt eine Oberfläche (Notion Dashboard oder Make-Scenario) und sieht nie die Komplexität dahinter.

## Notion Asset
https://www.notion.so/2849129c75bf81d5b2afc5044e919aca

## Action Items
- [ ] Minimales Kunden-Dashboard entwerfen (Notion oder Softr)
- [ ] Input-Formular: Branche, Keywords, Tone of Voice
- [ ] Output: fertige Social Posts, Captions, Videos
- [ ] Pricing-Tier definieren (MRR Modell)"""
    },
    {
        "title": "[BUILD] AI Clone Creator (Personal Brand Cloning)",
        "team_key": "MKT",
        "project": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "labels": ["#build", "#experiment"],
        "priority": 3,
        "description": """## Ziel
Klonierung des eigenen Content-Stils (Sprache, Ton, Format) für vollautomatisierte Content-Produktion im persönlichen Brand-Voice.

## Notion Asset
https://www.notion.so/2849129c75bf81de926cdafbce472a41

## Action Items
- [ ] Fine-Tuning Daten aus bisherigem Content aufbereiten
- [ ] KI-Modell trainieren / System Prompt verfeinern
- [ ] Output: Posts, Scripts, Emails im Clone-Voice"""
    },
    {
        "title": "[BUILD] YouTube Long Form Generator",
        "team_key": "MKT",
        "project": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "labels": ["#build"],
        "priority": 3,
        "description": """## Ziel
Vollautomatisierte Produktion langer YouTube-Videos (10–30 Min.) aus einem Themen-Input.

## Notion Asset
https://www.notion.so/2849129c75bf81b38b80e09c04b96db7

## Action Items
- [ ] Skript-Generator (Research → Outline → Script) bauen
- [ ] Voiceover (ElevenLabs) + B-Roll automatisieren
- [ ] Auto-Upload via YouTube API"""
    },
    {
        "title": "[BUILD] 4K Video Creator Setup",
        "team_key": "MKT",
        "project": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "labels": ["#build", "#experiment"],
        "priority": 4,
        "description": """## Ziel
Premium 4K-Video-Produktion für hochwertige Brand-Inhalte, Showreel und Premium-Ad-Creatives.

## Notion Asset
https://www.notion.so/2849129c75bf81d09329f5bf20948d48

## Action Items
- [ ] Render-Pipeline konfigurieren (GPU auf Hetzner oder Runpod)
- [ ] Test mit 1 Premium-Video"""
    },
    {
        "title": "[EXPERIMENT] ASMR Shorts Generator aktivieren",
        "team_key": "MKT",
        "project": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "labels": ["#experiment", "#build"],
        "priority": 4,
        "description": """## Ziel
Nischen-Experiment: ASMR-Formate als viraler Hook für Aufmerksamkeit in sättigenden Feeds testen.

## Notion Asset
https://www.notion.so/2849129c75bf81159be0c43d07d4eaf9

## Action Items
- [ ] 5 Test-Videos produzieren
- [ ] Performance vs. Standard Shorts vergleichen
- [ ] Entscheidung: skalieren oder verwerfen"""
    },
    {
        "title": "[EXPERIMENT] Seedance AI Video Generator Test",
        "team_key": "MKT",
        "project": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "labels": ["#experiment"],
        "priority": 4,
        "description": """## Ziel
Evaluation von Seedance AI als alternative Video-KI. Kostenvergleich mit Veo3.

## Notion Asset
https://www.notion.so/2849129c75bf810c8f7fca59323d9ba3

## Action Items
- [ ] Account anlegen
- [ ] 3 Test-Videos produzieren
- [ ] Qualitäts- und Kostenvergleich mit Veo3 dokumentieren"""
    },
    {
        "title": "[LEARN] 365+ Automation Templates sichten & clustern",
        "team_key": "MKT",
        "project": "Marketing Engine Phase III – Dominanz & Produktisierung",
        "labels": ["#learn", "#experiment"],
        "priority": 4,
        "description": """## Ziel
Systematisches Durchgehen der 365+ Templates zur Identifikation neuer Produkt- und Automatisierungsideen.

## Notion Asset
https://www.notion.so/2319129c75bf801e8821ea90182db4a3

## Action Items
- [ ] Templates nach Kategorie clustern
- [ ] Top 10 Ideen für neue Kundenprodukte herausfiltern"""
    },
    # ── SAL Team Issues ───────────────────────────────────
    {
        "title": "[BUILD] Instagram Outreach System (Inbound Lead Konvertierung)",
        "team_key": "SAL",
        "project": "Sales & Outreach Engine 2026–2028",
        "labels": ["#build", "#core-system"],
        "priority": 1,
        "description": """## Ziel
Automatische Konvertierung von IG-Kommentaren und Interaktionen in qualifizierte Leads per DM.

## Notion Asset
https://www.notion.so/1c39129c75bf80769a52f731d3b29ffb

## ⚠️ Risiken
- Instagram ist empfindlich gegenüber Automatisierungen → Residential Proxies PFLICHT

## Action Items
- [ ] Proxy-Infrastruktur einrichten (wie im Notion-Dokument beschrieben)
- [ ] Trigger-Keyword-Logik konfigurieren (z.B. "SYSTEM", "FREEBIE", "INFO")
- [ ] Auto-DM: Freebie senden + Konversation starten
- [ ] Lead-Daten (Name, Handle, E-Mail) ins CRM/Google Sheet schreiben
- [ ] Test mit eigenem Account (KEIN Kundenaccount!)"""
    },
    {
        "title": "[BUILD] Apollo Lead Scraper (Free Stack via Apify)",
        "team_key": "SAL",
        "project": "Sales & Outreach Engine 2026–2028",
        "labels": ["#build", "#core-system"],
        "priority": 1,
        "description": """## Ziel
B2B Lead-Scraping ohne teures Apollo-Vollabo. Zielgruppe: Webdesigner, Agenturen, Solopreneure in DACH.

## Notion Asset
https://www.notion.so/2849129c75bf8113825dfe78d013c55a

## Action Items
- [ ] Apify Apollo Actor konfigurieren
- [ ] Google Sheet Template anlegen: Name, Firma, Website, E-Mail, Status, Notizen
- [ ] Filter setzen: Branche, Region (DACH), Mitarbeiteranzahl (1–10)
- [ ] Test-Run: 50 Leads scrapen"""
    },
    {
        "title": "[BUILD] Cold Email Bulk Personalizer (OpenAI + Perplexity)",
        "team_key": "SAL",
        "project": "Sales & Outreach Engine 2026–2028",
        "labels": ["#build", "#core-system"],
        "priority": 1,
        "description": """## Ziel
Hyper-personalisierte Kaltmails in großem Maßstab. Die KI scannt die Website des Leads und schreibt eine auf seinen spezifischen Pain Point zugeschnittene Email.

## Notion Asset
https://www.notion.so/2849129c75bf81dfa05dcc9c69017cda

## Blocked By
- [BUILD] Apollo Lead Scraper (Free Stack via Apify)

## Prompt-Kernlogik (für den Email-Generator)
> "Du bist ein freundlicher, lösungsorientierter Outreach-Spezialist für VIRON.
> Schreibe eine kurze, persönliche Cold-Email (max. 5 Sätze) an [Name] von [Firma].
> Deren Website zeigt: [Website-Zusammenfassung].
> Fokus: Wir können ihnen [konkretes Problem] mit einem einfachen Make-Automatisierungs-System lösen.
> Kein generisches Blabla. Keine Buzzwords. Echte Relevanz."

## Action Items
- [ ] n8n/Make Flow: Lead aus Sheet → Website scrapen → Prompt befüllen → Email generieren
- [ ] Email-Versand via Gmail API / Mailerlite / Instantly konfigurieren
- [ ] A/B Test: 2 verschiedene Prompt-Varianten"""
    },
    {
        "title": "[BUILD] LinkedIn Cold Email Machine",
        "team_key": "SAL",
        "project": "Sales & Outreach Engine 2026–2028",
        "labels": ["#build"],
        "priority": 2,
        "description": """## Ziel
Kombination von LinkedIn-Profildaten mit Cold-Email-Personalisierung für maximale Relevanz.

## Notion Asset
https://www.notion.so/2849129c75bf810e9731c812e402f22f

## Action Items
- [ ] LinkedIn-Scraper (Apify / PhantomBuster) anbinden
- [ ] Email-Anreicherung via Hunter.io oder Apollo
- [ ] Personalisierungs-Flow bauen"""
    },
    {
        "title": "[BUILD] LinkedIn DM Automation System",
        "team_key": "SAL",
        "project": "Sales & Outreach Engine 2026–2028",
        "labels": ["#build"],
        "priority": 2,
        "description": """## Ziel
Halbautomatisierte LinkedIn-DM-Sequenz für Warmakquise nach Content-Interaktionen.

## Notion Asset
https://www.notion.so/2849129c75bf8104a019dde9de5fedaa

## ⚠️ Risiken
- LinkedIn ist sehr sensitiv bei Automatisierungen → max. 20–30 DMs/Tag, menschliche Delays

## Action Items
- [ ] Trigger: Profil hat Post geliked oder kommentiert
- [ ] DM-Sequenz: 3 Nachrichten über 7 Tage (kein Spam)
- [ ] CRM-Integration: Status je Lead tracken"""
    },
    # ── GRO Team Issues ───────────────────────────────────
    {
        "title": "[BUILD] AntiGravity & n8n DeepResearch Infrastruktur",
        "team_key": "GRO",
        "project": "Ground0 Engineering Setup",
        "labels": ["#build", "#core-system"],
        "priority": 1,
        "description": """## Ziel
Aufbau der deterministischen KI-Agenten-Infrastruktur. Basis für alle anderen Systeme.

## Notion Assets
- AntiGravity Master Prompt: https://www.notion.so/2ee9129c75bf809bb69fdc5ad6f7ceb6
- n8n DeepResearch: https://www.notion.so/1ad9129c75bf80cab4f0c553aa490def
- N8N MCP: https://www.notion.so/2719129c75bf81d99b8dfe360feecd57
- GraphRAG + N8N: https://www.notion.so/2719129c75bf819dbeeccb41d58064d4

## Action Items
- [ ] Hetzner Server (ARM64) via Coolify bereitstellen
- [ ] n8n Self-Hosted deployen
- [ ] MCP-Server konfigurieren (Notion + Linear Anbindung)
- [ ] B.L.A.S.T.-Protokoll im Agenten-System Prompt implementieren
- [ ] GraphRAG-Architektur für interne Knowledge Base aufsetzen"""
    },
]

CREATE_ISSUE = """
mutation CreateIssue($input: IssueCreateInput!) {
  issueCreate(input: $input) {
    success
    issue { id title identifier }
  }
}
"""

def get_existing_teams():
    result = gql(GET_TEAMS)
    return {t["key"]: t["id"] for t in result["teams"]["nodes"]}

def create_issues(team_ids, project_map, label_map):
    for issue in ISSUES:
        team_id = team_ids.get(issue["team_key"])
        if not team_id:
            print(f"  ⚠️  Team {issue['team_key']} nicht gefunden: {issue['title'][:50]}")
            continue
        project_id = project_map.get(issue.get("project"))
        label_ids = [
            label_map.get(issue["team_key"], {}).get(lbl)
            for lbl in issue.get("labels", [])
            if label_map.get(issue["team_key"], {}).get(lbl)
        ]
        payload = {
            "teamId": team_id,
            "title": issue["title"],
            "description": issue.get("description", ""),
            "priority": issue.get("priority", 3),
        }
        if project_id:
            payload["projectId"] = project_id
        if label_ids:
            payload["labelIds"] = label_ids
        try:
            result = gql(CREATE_ISSUE, {"input": payload})
            i = result["issueCreate"]["issue"]
            print(f"  ✅ Issue {i['identifier']}: {i['title'][:60]}")
        except Exception as e:
            print(f"  ⚠️  Issue fehler: {issue['title'][:50]} → {e}")

# ─────────────────────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🚀 VIRON LINEAR SETUP START\n" + "="*50)

    print("\n[0] Organisation...")
    get_organization_id()

    print("\n[1] Teams anlegen...")
    try:
        team_ids = create_teams()
    except Exception:
        print("  Fallback: Bestehende Teams laden...")
        team_ids = get_existing_teams()

    if not team_ids:
        team_ids = get_existing_teams()

    print(f"  Teams verfügbar: {list(team_ids.keys())}")

    print("\n[2] Labels anlegen...")
    label_map = create_labels(team_ids)

    print("\n[3] Projekte anlegen...")
    project_map = create_projects(team_ids)

    print("\n[4] Issues anlegen...")
    create_issues(team_ids, project_map, label_map)

    print("\n" + "="*50)
    print("✅ VIRON LINEAR SETUP ABGESCHLOSSEN")
    print("="*50)
