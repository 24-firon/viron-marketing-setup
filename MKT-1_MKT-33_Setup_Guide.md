# VIRON – Setup Guide
## Track A: MKT-1 Auto-Moderation | Track B: MKT-33 Apollo Lead Scraper

---

## 🔴 TRACK A – MKT-1: Auto-Moderation (Make.com)

**File:** `MKT-1_AutoModeration_Make_Blueprint.json`
**Zeitaufwand Setup:** ~30 min
**APIs:** Instagram Graph API, OpenAI (gpt-4o-mini), Google Sheets

### Voraussetzungen
- Make.com Account (Free reicht für <1000 Ops/Monat)
- Instagram Business/Creator Account mit Facebook Page verknüpft
- OpenAI API Key (Kosten: ~$0.01 pro 500 Kommentare)
- Google Sheets für das Lösch-Log

### Setup-Schritte

**1. Blueprint importieren**
- Make.com → Scenarios → Create a new scenario
- Rechtsklick → Import Blueprint → `MKT-1_AutoModeration_Make_Blueprint.json` hochladen

**2. Connections einrichten**
- **Instagram:** Meta Business App → Instagram Graph API Webhook konfigurieren
  - Permissions benötigt: `instagram_manage_comments`, `instagram_basic`
  - Webhook-Feld: `comments`
- **OpenAI:** API Key aus platform.openai.com eintragen
- **Google Sheets:** Google-Account verbinden, Sheet anlegen

**3. Google Sheet anlegen (Lösch-Log)**
Spalten: `Datum | Kommentar | Autor | Kategorie | Confidence | Post-ID | Aktion`

**4. Variablen ersetzen**
```
{{DEIN_INSTAGRAM_WEBHOOK_ID}}  → Webhook-ID aus Make.com
{{DEIN_IG_ACCOUNT_ID}}         → Instagram Account ID (aus Meta Developer Console)
{{DEIN_GOOGLE_SHEET_ID}}       → Sheet-ID aus der URL
```

**5. Confidence-Schwellwert kalibrieren**
Im Router (Schritt 4): Filter `confidence > 0.75` anpassen je nach Bedarf.
- Empfehlung: Start mit 0.75, nach 1 Woche auf Basis der Logs anpassen
- Zu viele False Positives? → 0.85 setzen
- Zu lasch? → 0.65 setzen

**6. Test-Run**
- Scenario aktivieren (Toggle = ON)
- Auf VIRON Test-Account einen Test-Kommentar mit Beleidigung posten
- Erwartetes Ergebnis: Kommentar gelöscht, Eintrag im Log

### OpenAI System Prompt (kalibriert)
```
Du bist ein Moderations-Assistent für Social Media.
Analysiere den folgenden Kommentar und antworte NUR mit einem JSON-Objekt:
{"toxic": true/false, "category": "spam|hate|insult|threat|neutral", "confidence": 0.0-1.0}

Werte 'toxic: true' wenn:
- Beleidigungen, Schimpfwörter, Hassrede
- Spam oder Werbung in Kommentaren
- Bedrohungen oder Einschüchterungen
- Stark negative Markenerwähnungen mit Aufruf zum Boykott

Werte 'toxic: false' bei:
- Konstruktiver Kritik ohne Beleidigungen
- Fragen oder positivem Feedback
- Neutralen Meinungen
```

### Freebie-Paket (für KMU-Kunden)
Nach erfolgreichem Test:
1. Scenario als JSON exportieren → in Notion unter "Freebies" ablegen
2. Kurzes Loom-Video aufnehmen (5 min): Setup-Demo
3. Preis-Vorschlag: €49/Monat als Managed Service oder €149 einmalig als Setup

### Kosten-Kalkulation
- Make.com: €0 (Free Plan) bis €9/Monat (Basic)
- OpenAI: ~€0.50–2.00/Monat (je nach Kommentar-Volumen)
- **Gesamtkosten:** < €11/Monat für bis zu 10 Kunden-Accounts

---

## 🔵 TRACK B – MKT-33: Apollo Lead Scraper (n8n + Apify)

**File:** `MKT-33_Apollo_Lead_Scraper.xlsx` (Google Sheet Template)
**Template n8n Flow:** [flow.json herunterladen](https://drive.google.com/uc?export=download&id=17iIu7-FO5RK2BVdnKITem_YQYe8WfaaM&filename=flow.json)
**Tutorial:** https://www.youtube.com/watch?v=GNw0fWkekEI
**Zeitaufwand Setup:** ~45 min
**APIs:** Apify, OpenAI (optional), Google Sheets

### Voraussetzungen
- n8n (self-hosted auf Ground-Zero oder n8n.cloud)
- Apify Account (Free Plan: $5 Guthaben = ~500 Leads)
- Google Sheets Account

### Setup-Schritte

**1. n8n Flow importieren**
- n8n → Workflows → Import from URL/File
- [flow.json von Google Drive herunterladen](https://drive.google.com/uc?export=download&id=17iIu7-FO5RK2BVdnKITem_YQYe8WfaaM&filename=flow.json)
- In n8n importieren und Credentials eintragen

**2. Apify konfigurieren**
- Apify Console → Actors → `apify/apollo-io-scraper` öffnen
- Input konfigurieren:
```json
{
  "searchUrl": "https://app.apollo.io/#/people?personTitles[]=Owner&personTitles[]=CEO&personTitles[]=Founder&contactEmailStatus[]=verified&organizationNumEmployeesRanges[]=1%2C10&organizationIndustryTagIds[]=5567cd4773696439b10b0000",
  "maxPeoplePerSearch": 50,
  "exportPersonalEmails": false
}
```
- Für DACH-Filter: Regions `DE`, `AT`, `CH` in Apollo UI setzen, dann URL kopieren

**3. Google Sheet einrichten**
- `MKT-33_Apollo_Lead_Scraper.xlsx` als Google Sheet hochladen (Drive → Datei hochladen → Als Google Sheet öffnen)
- Sheet-ID aus URL kopieren → in n8n eintragen
- Alternativ: Sheet-ID direkt in der Config-Tabelle des Sheets eintragen

**4. Variablen in n8n setzen**
```
APIFY_API_TOKEN      → Apify Console → Settings → API Tokens
GOOGLE_SHEET_ID      → Aus der Google Sheets URL
OPENAI_API_KEY       → platform.openai.com (optional, für E-Mail-Personalisierung)
```

**5. Test-Run: 50 Leads scrapen**
- n8n Workflow manuell starten
- Erwartetes Ergebnis: 50 Leads im Google Sheet (Tab "Leads")
- Qualitäts-Check: Sind E-Mails vorhanden? Stimmt die Region?

**6. Ziel-Filter (DACH, 1–10 MA)**
Die wichtigsten Apollo-Filter für das Ziel-ICP:
- Job Titles: Owner, Inhaber, CEO, Founder, Geschäftsführer
- Company Size: 1–10 Mitarbeiter
- Industry: Marketing & Advertising, Web Design, IT Services
- Regions: Germany, Austria, Switzerland
- Email Status: Verified

### Google Sheet Aufbau (MKT-33_Apollo_Lead_Scraper.xlsx)
- **Tab "Leads":** Alle gescrapten Kontakte mit Status, Priorität, Score
- **Tab "Dashboard":** Live-Statistiken (Anzahl pro Status, Ø Score, Hoch-Priorität)
- **Tab "Config":** Apify & n8n Konfigurationsparameter

### Nächster Schritt: MKT-34 (Cold Email)
Nach erfolgreichem Test mit 50 Leads → MKT-34 (Cold Email Bulk Personalizer) wird freigeschaltet (aktuell blocked by MKT-33).

### Kosten-Kalkulation Apify
- Free Plan: $5 Guthaben initial
- Apollo Scraper: ~$0.01 pro Lead
- 50 Leads/Woche = ~$2/Monat
- 500 Leads/Monat = ~$5 → Apify Starter $49/Monat nötig

---

## ✅ DONE-CHECKLIST

### MKT-1
- [ ] Blueprint importiert in Make.com
- [ ] Instagram Webhook konfiguriert
- [ ] OpenAI Connection aktiv
- [ ] Google Sheets Log eingerichtet
- [ ] Test-Run erfolgreich (1 Kommentar gelöscht)
- [ ] → Linear: MKT-1 auf "Done" setzen → MKT-4 wird freigeschaltet

### MKT-33
- [ ] n8n Flow importiert
- [ ] Apify API Token eingetragen
- [ ] Google Sheet hochgeladen & ID eingetragen
- [ ] Test-Run: 50 Leads gescrapt
- [ ] Leads in Sheet überprüft (E-Mail-Qualität, Region)
- [ ] → Linear: MKT-33 auf "Done" setzen → MKT-34 wird freigeschaltet

---

*VIRON Ground-Zero Agency | MKT-1 + MKT-33 | 2026-03-12*
