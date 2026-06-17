---
name: local-seo-gbp
description: "When the user wants to improve local SEO or Google Business Profile visibility in the DACH region. Also use when the user mentions 'Google Business Profile optimieren,' 'Local SEO Deutschland,' 'Google Maps Ranking verbessern,' 'Branchenverzeichnis eintragen,' 'Lokale Keywords recherchieren,' 'Review-Management Google,' 'GBP Posts erstellen,' 'Gelbe Seiten Eintrag,' 'Hreflang de-de de-at de-ch,' 'LocalBusiness Schema,' 'Regionale Sichtbarkeit KMU,' or 'Google Q&A beantworten.' Use this for any local search, Google Maps, or regional SEO work for German, Austrian, or Swiss KMU."
metadata:
  version: 1.0.0
---

# Local SEO & Google Business Profile (DACH)

You build local SEO foundations and Google Business Profile strategies for DACH-KMUs (lokal verwurzelte Geschäfte, Boutiquen, Concept Stores, Handwerksbetriebe, lokale Dienstleister). 46% aller Google-Suchen haben lokalen Intent — und für KMUs ist das der höchste Impact-Kanal überhaupt.

VIRON differentiator: **GBP als living asset, nicht als Branchenverzeichnis-Eintrag** — wir behandeln GBP wie eine aktive Content-Plattform, nicht wie eine Visitenkarte.

## Workflow

### Step 1: Audit der aktuellen Local-Visibility

Bevor du etwas baust, miss den Ist-Stand:

1. **GBP-Status**: Ist das Profil überhaupt vorhanden? Verifiziert? Claimed? (Prüfe GBP-Dashboard oder google.com/business)
2. **NAP-Konsistenz**: Stimmen Name, Adresse, Telefon über alle Verzeichnisse überein? (Eine Inkonsistenz kostet Ranking)
3. **Aktuelle Local-Rankings**: Für welche 10–20 Suchanfragen sollte der Kunde ranken? Wo steht er heute?
4. **Branchenverzeichnis-Coverage**: Welche DACH-Verzeichnisse sind gepflegt? Welche fehlen?
5. **Review-Profil**: Wie viele Reviews? Welcher Durchschnitt? Antwort-Rate?

Tools: Google Business Profile Manager, localo (DE), Yext (für Verzeichnis-Sync), manuelle Suche.

### Step 2: GBP-Profil auf Vollständigkeit bringen

GBP-Ranking-Faktoren 2026:

- **Vollständigkeit aller Felder**: Stunden, Telefon, Website, Beschreibung (max. 750 Zeichen), Kategorien (Hauptkategorie + 5–9 Nebenkategorien), Services, Attribute
- **Geographische Nähe** zum Suchenden (nicht beeinflussbar, aber bewusst)
- **Review-Volumen + Durchschnitt + Antwort-Rate**
- **Posting-Aktivität**: GBP-Posts mindestens 1–2x/Woche
- **Foto-Updates**: Mindestens 1x/Monat neue Fotos (Produkte, Team, Räumlichkeiten)
- **Q&A**: Mindestens 5 eigene Q&A-Paare selbst anlegen
- **Produkte/Services**: Vollständig eingepflegt mit Beschreibungen + Preisen wo möglich

### Step 3: Lokale Keyword-Strategie aufbauen

Pattern: **"[Dienstleistung] + [Stadt/Region]"**

Beispiele:
- "Marketing Automation Frankfurt"
- "KI-Beratung München"
- "Steuerberater Köln Ehrenfeld"
- "Friseur Berlin Mitte"

Recherchequellen:
- Google Autocomplete (kostenlos, echt)
- Google Keyword Planner (kostenlos mit Google Ads Account)
- localo oder Ubermetrics für DACH-Granularität
- Semrush / Ahrefs für Wettbewerbs-Analyse

Pro Standort: 10–15 Long-Tail-Keywords definieren. Diese landen in:
- GBP-Beschreibung
- GBP-Posts
- Local Landing Pages auf der Website
- Branchenverzeichnis-Einträgen
- Meta-Titles und H1 der Hauptseiten

### Step 4: DACH-Branchenverzeichnisse bespielen

Pflicht-Verzeichnisse für DE/AT/CH:

**Deutschland**:
- Google Business Profile (P0)
- Apple Maps (P0)
- Gelbe Seiten (P1)
- Das Örtliche (P1)
- 11880.com (P1)
- Bing Places (P1, **TODO M2b — Spec listet Bing nicht, P1 selbst definiert**)
- Facebook Business Page (P1, **TODO M2b — Spec listet FB nicht als Verzeichnis, P1 selbst definiert**)

**Österreich**:
- Herold.at (P0 für AT)
- Google Business Profile (P0)
- Apple Maps (P0)

**Schweiz**:
- local.ch (P0 für CH)
- search.ch (P1, **TODO M2b — Spec listet nur local.ch; search.ch selbst ergänzt**)
- Google Business Profile (P0)
- Apple Maps (P0)

Für jedes Verzeichnis:
- NAP konsistent halten
- Kategorie präzise wählen
- Beschreibung mit lokalen Keywords
- Logo + Cover-Foto hochladen
- Öffnungszeiten identisch zur Website

### Step 5: Review-Management-System einrichten

Reviews sind für lokales Ranking der zweitwichtigste Faktor nach Proximity. Default-Strategie:

**Reviews akquirieren**:
- Nach jedem Service/Kauf: personalisierte E-Mail mit direktem Review-Link
- QR-Code auf Kassenbon / Rechnung
- Follow-up 7 Tage nach Lieferung (Timing matters)
- Niemals: Incentives für Reviews (Google Penalty)

**Reviews beantworten**:
- **Positiv (4–5 Sterne)**: Dank + persönliche Note + Hinweis auf nächstes Service
- **Neutral (3 Sterne)**: Dank + proaktive Lösung + Offline-Kontakt anbieten
- **Negativ (1–2 Sterne)**: Niemals öffentlich diskutieren. Sachliche Antwort, Lösung anbieten, Offline-Eskalation. Max. 2–3 Sätze.

Antwort-Zeit: (TODO — Spec nennt keinen Wert; Vorschlag aus GBP-Best-Practices: 24–48 Stunden, **vor Operator-Approval nicht als fixe Vorgabe nutzen**).

### Step 6: GBP als Content-Kanal nutzen

GBP-Posts sind 2026 der unterschätzte Hebel. Drei Post-Typen:

- **What's New**: Neue Produkte, Services, Events (mindestens 1x/Woche)
- **Offers**: Aktionen, Rabatte, saisonale Angebote
- **What's Happening**: Hinter-den-Kulissen, Team-News, Veranstaltungen

Jeder Post: 150–300 Wörter + Bild + CTA (Anrufen, Route, Website).

### Step 7: Schema Markup für LocalBusiness

Auf der Hauptseite und allen Standort-Seiten:

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "...",
  "address": {...},
  "telephone": "...",
  "openingHoursSpecification": [...],
  "geo": {"latitude": ..., "longitude": ...},
  "url": "...",
  "image": "..."
}
```

Plus: `Service` Schema für Dienstleistungen, `FAQPage` für lokale Q&A.

Reference: `STORAGE/archive/skills/schema/SKILL.md` für Schema-Tiefe.

### Step 8: Hreflang für DACH-Multi-Region

Wenn der Kunde in DE/AT/CH aktiv ist:

```html
<link rel="alternate" hreflang="de-DE" href="https://example.com/de-de/" />
<link rel="alternate" hreflang="de-AT" href="https://example.com/de-at/" />
<link rel="alternate" hreflang="de-CH" href="https://example.com/de-ch/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/" />
```

Selbst-Check: jede Sprachversion muss eigenständig wertvoll sein, nicht nur übersetzt.

---

## Core Principles

### GBP ist eine Plattform, kein Eintrag

Ein GBP mit gepflegten Posts, Fotos und Q&A rankt 2–3x besser als ein "hingeschmissenes" Profil. 30 Minuten/Woche für GBP-Pflege rechnen sich ab dem 3. Monat.

### NAP-Konsistenz schlägt Verzeichnis-Vielfalt

10 Verzeichnisse mit inkonsistenten Daten schaden mehr als 3 perfekt konsistente Einträge. Erst NAP aufräumen, dann Verzeichnisse skalieren.

### Reviews-Antwort ist Service, nicht SEO

Kunden lesen, wie du auf negative Reviews antwortest. Eine professionelle Antwort auf einen 1-Stern-Review konvertiert mehr als 10 positive Reviews unbeantwortet zu lassen.

### Lokales Hosting für lokales Ranking

Server in DE/AT/CH = Page-Speed-Vorteil für lokale Suchende. Cloudflare oder Hetzner mit EU-Standort empfohlen. US-Hosting kostet DACH-Traffic.

---

## Trigger-Phrasen

Siehe YAML-Frontmatter (`description`) — alle Trigger-Phrasen sind dort zentral gepflegt.

---

## Dependencies

1. **Foundation**: `.agents/product-marketing.md` — Standorte, Service-Gebiet, ICP-Schmerzpunkte
2. **Technisch**: Zugriff auf GBP-Account des Kunden (Owner-Berechtigung), Website-Zugriff für Schema + Hreflang
3. **SEO-Tiefe**: `STORAGE/archive/skills/schema/SKILL.md` für LocalBusiness/Service/FAQ-Schema-Details
4. **Brand Voice**: `DOCS/brand-voice.md` für Review-Antworten-Tone

## NICHT Dependencies

- Google Ads (separater Kanal; lokale Ads kommen zusätzlich, aber GBP-Optimierung ist organisch)

---

## Output Format

When you complete a local-SEO-GBP task, deliver:

1. **GBP-Audit-Report** — Ist-Stand mit Lücken-Liste
2. **Vervollständigungs-Plan** — Welche Felder/Posts/Q&A fehlen, mit Beispielen
3. **Local-Keyword-Liste** — 10–15 Keywords pro Standort
4. **Verzeichnis-Submissions-Liste** — DE/AT/CH priorisiert
5. **Review-Management-Playbook** — Akquise-Templates, Antwort-Schablonen
6. **Schema-Markup-Snippets** — LocalBusiness, Service, FAQ
7. **Optional: 12-Wochen-Pflegeplan** — GBP-Posts, Foto-Updates, Q&A, Reviews

---

## Anti-Patterns (Vermeide diese)

- ❌ GBP nur anlegen und nie updaten (Algorithmus bestraft Inaktivität)
- ❌ Kategorie-Spam (Hauptkategorie + passende Nebenkategorien, nicht 15 irrelevante)
- ❌ Keyword-Stuffing in GBP-Beschreibung (kostet Ranking, sieht unprofessionell aus)
- ❌ Reviews kaufen oder mit Incentives triggern (Google Penalty = Profile-Löschung)
- ❌ Negative Reviews öffentlich diskutieren oder löschen lassen wollen
- ❌ NAP-Inkonsistenz ignorieren (jede Variante kostet Ranking-Power)
- ❌ Verzeichnis-Spam in 50+ irrelevanten Verzeichnissen (Low-Quality-Links)
- ❌ Hreflang falsch implementieren (z.B. alle Regionen auf eine Seite zeigen)

---

## References

- **IMPORT/05_DACH_Marketing_Spezifika.md** — Section 5.2.2 (Local SEO & Google Business Profile)
- **Kennzahlen**: 46% aller Google-Suchen haben lokalen Intent [web:19]
- **Schema-Tiefe**: `STORAGE/archive/skills/schema/SKILL.md`
- **DSGVO-Schnittstelle**: GBP-Lead-Formulare → `dsgvo-lead-capture` Skill

---

## VIRON Service-Idee

**"Local Visibility Booster"** (Spec-Wortlaut) — GBP-Optimierung, Local Keyword-Strategie, Branchenverzeichnis-Submissions.

**TODO:** Konkretes Service-Package mit Deliverables (Audit, Vervollständigung, Review-Setup, 12-Wochen-Pflegeplan) muss in `.agents/services/` oder `STORAGE/` definiert werden, bevor dieser Skill in Kundenprojekten eingesetzt wird. Der Skill beschreibt nur **wie** man es macht, nicht **was** als VIRON-Service verkauft wird.

## Buyer-Pain spricht, nicht SEO-Jargon

Lokale Sichtbarkeit adressiert bei DACH-KMUs konkrete Geschäftsführer-Pains (siehe `DOCS/icp-summary.md` und `.agents/product-marketing.md`):

- „Website als toter Prospekt" — generiert keine Leads, ist statisch
- „Termin-Ping-Pong" — Kunden buchen per E-Mail hin und her
- „Keine IT-Abteilung" — 90% der 5–50 MA Unternehmen

GBP-Posts und Local-Content müssen zeigen: „Wir sind lokal ansässig, erreichbar, antworten schnell". Das ist für KMU-Entscheider (35–55, pragmatisch) der entscheidende Trust-Signal — nicht Keyword-Dichte oder Backlink-Count.