---
name: linkedin-dach-b2b
description: "When the user wants to plan or execute a LinkedIn B2B strategy in the DACH region. Also use when the user mentions 'LinkedIn Strategie DACH,' 'LinkedIn B2B Deutschland,' 'LinkedIn Post auf Deutsch,' 'Social Selling DACH,' 'LinkedIn Content Kalender,' 'LinkedIn Thought Leadership,' 'LinkedIn Reichweite erhöhen,' 'LinkedIn Ads KMU,' 'LinkedIn Creator Mode,' 'XING Alternative LinkedIn,' '360-Brew LinkedIn,' or 'Kommentare statt Likes LinkedIn.' Use this for any LinkedIn-specific work targeting German, Austrian, or Swiss B2B audiences."
metadata:
  version: 1.0.0
---

# LinkedIn DACH B2B

You design and execute LinkedIn strategies for DACH-region B2B KMU. The US playbook does not transfer cleanly — German B2B buyers expect substance over hype, formality over casualness, and Thought Leadership over product pitching.

VIRON differentiator: **Personal Brand vor Unternehmensseite** — Personal Brands konvertieren, Unternehmensseiten nicht. Wir bauen Strategien für Entscheider-Personas, nicht für Logo-Posts.

## Workflow

### Step 1: Decide Personal Brand vs. Unternehmensseite

Default: **Personal Brand** for the decision-maker (Geschäftsführer/Inhaber).

Reasoning:
- LinkedIn-Algorithmus 2026 priorisiert Personal Profiles in Feed
- B2B-Entscheider folgen Personen, nicht Logos
- DACH-Personal Brands haben 5–10x höhere Engagement-Raten als Unternehmensseiten
- Comment-driven Engagement funktioniert nur auf Personal Profiles sinnvoll

Use Unternehmensseite **nur zusätzlich** für: Company Updates, Job-Posts, Event-Promotion. Nie als primärer Thought Leadership Kanal.

### Step 2: Define Sie/Du-Tone-of-Voice

Default für DACH-B2B: **"Sie"** (formell).

Decision matrix:
- **B2B, etablierte Branche, 40+ Zielgruppe**: Sie
- **B2B, Startup/Scale-up, Tech-affin**: Du möglich
- **B2C, junge Zielgruppe**: Kontext-abhängig, meist Du
- **Mischformen**: User fragen — niemals raten

Einmal entschieden, **überall** konsistent — LinkedIn-Posts, Kommentare, DMs, Newsletter. Tone-of-Voice-Wechsel verwirrt.

Reference: `DOCS/brand-voice.md` für die VIRON-eigene Brand-Stimme (Direkt, deutsch, kein Bullshit).

### Step 3: Build the Content-Kalender

DACH-spezifische Posting-Zeiten (MEZ):
- **Morgens**: 08:00–09:00 (vor Meeting-Marathon)
- **Abends**: 17:00–18:00 (nach Feierabend-Reflexion)
- **Vermeide**: 12:00–14:00 (Mittagspause, niedrigere B2B-Engagement)
- **Wochenende**: Samstag 09:00–11:00 möglich, Sonntag fast nie

Content-Typ-Matrix für DACH:
- **Text-Posts (150–250 Wörter)**: Hook → Rehook → Payoff → CTA (siehe `DOCS/brand-voice.md`)
- **Carousels (5–10 Slides)**: Sparen triggern, Checklisten, Frameworks
- **Video (90 Sek. max)**: Persönliche Insights, kein Hochglanz-Production
- **Document Posts (PDF)**: Whitepaper-Auszüge, Case Studies
- **Polls**: Selten, nur für echte Decision-Fragen

Cadence: (TODO — Spec nennt keine konkrete Frequenz; Vorschlag aus 360-Brew-Adaption: 3–4 Posts/Woche + 5–10 substanzielle Kommentare/Tag, **vor Operator-Approval nicht als fixe Vorgabe nutzen**). Mehr ist nicht besser.

### Step 4: Adapt the 360-Brew-Algorithmus

Das 360-Brew-Modell funktioniert auch in DACH, mit Anpassungen:

| 360-Brew Phase | US-Variante | DACH-Anpassung |
|---|---|---|
| Brew (Beitrag erstellen) | Casual Hook, Emoji | Substanzieller Hook, keine Emoji-Spam |
| Stir (Interaktion triggern) | Frage am Ende, "Thoughts?" | Konkrete Decision-Frage, kontrovers aber fair |
| Pour (Antworten) | Kurze Dankes-Kommentare | Lange substanzielle Antworten mit neuer Info |
| Sip (Likes geben) | Massen-Likes | Selektive Likes + immer mit Kommentar |
| Share (Reposten) | Sofort teilen | Nur wenn echte Mehrwert, mit eigenem Kommentar |

Kommentar-Tiefe schlägt Likes-Anzahl in DACH. Substanz schlägt Hype.

### Step 5: Optionale Paid Amplification

LinkedIn Ads für DACH:
- **Zielgruppen**: Job-Title (Geschäftsführer, Inhaber), Branchen, Firmengröße 5–50
- **Sprache**: Deutsch für DACH, Englisch nur bei explizitem International-Fokus
- **Lead-Gen Forms**: DSGVO-konform — siehe `dsgvo-lead-capture` Skill
- **Budget**: Minimum (TODO — Spec nennt keinen Wert; Vorschlag aus DACH-Ad-Best-Practices: 50€/Tag für statistisch relevante Daten, **vor Operator-Approval nicht als fixe Vorgabe nutzen**)

Targeting-Ergänzungen:
- **XING-Integration**: Für 40+ Zielgruppen in DE noch relevant (DACH-Granularität)
- **LinkedIn Sales Navigator**: Für direkte Outreach-Sequenzen (nicht für Anzeigen)

---

## Core Principles

### Substanz > Reichweite

Deutscher B2B-Buyer folgt dir wegen deiner Insights, nicht deiner Follower-Zahl. 500 echte Kommentare schlagen 50.000 Impressionen ohne Resonanz.

### Personal Brand konvertiert

Wenn der Entscheider dein Gesicht kennt, deine Meinung respektiert und deine Expertise sieht — dann kauft er bei dir, nicht bei der anonymen "Agentur X". VIRON-Service-Pitch: "Wir bauen deine LinkedIn-Personal-Brand, die Kunden anzieht statt umwirbt."

### Siezen als Respekt, nicht als Distanz

"Sie" ist in DACH-B2B die Norm. Wer duzt ohne Aufforderung, wirkt entweder respektlos (bei Älteren) oder bemüht locker (bei Etablierten). Beides schadet.

### Kommentare > Likes

Ein guter Kommentar auf einem fremden Profil eines Branchen-Kollegen bringt mehr Sichtbarkeit als der eigene Post. 30 Minuten/Tag für strategische Kommentare = beste Reichweiten-Investition.

---

## Trigger-Phrasen

Siehe YAML-Frontmatter (`description`) — alle Trigger-Phrasen sind dort zentral gepflegt.

---

## Dependencies

1. **Foundation**: `.agents/product-marketing.md` — ICP und Pain Points fließen in Hooks und Content-Pillars
2. **Brand Voice**: `DOCS/brand-voice.md` — Hook-Formeln, Tone-of-Voice, Verbotene Formulierungen
3. **ICP**: `DOCS/icp-summary.md` — Buyer-Persona, Schmerzpunkte, Buyer-Language
4. **Social Skill**: `social` (siehe `DOCS/skill-router.md`) — für plattform-übergreifende Patterns und Post-Templates
5. **DSGVO**: `dsgvo-lead-capture` — für LinkedIn Lead-Gen Forms und Audience-Targeting-Compliance

## NOT Dependencies

- LinkedIn Sales Navigator Account (separates Tool, separat lizensieren)
- LinkedIn Premium (Creator Mode ist kostenlos)

---

## Output Format

When you complete a LinkedIn DACH B2B task, deliver:

1. **Content-Strategie** — Pillars, Posting-Cadence, Tone-of-Voice-Entscheidung
2. **Hook-Library** — 20+ DACH-spezifische Hooks nach Pattern aus `DOCS/brand-voice.md`
3. **30-Tage Content-Kalender** — Posts + geplante Kommentar-Cluster
4. **Kommentar-Templates** — 5 Templates für substanzielle Antworten auf Fremd-Posts
5. **Optional: Ad-Setup-Skizze** — Zielgruppen, Creative-Briefs, Budget-Allokation

---

## Anti-Patterns (Vermeide diese)

- ❌ Unternehmensseite als primärer Thought Leadership Kanal (konvertiert nicht in DACH)
- ❌ "Thoughts?" oder "Was meint ihr?" als CTA (zu generisch, kein Engagement-Trigger)
- ❌ Duzen ohne explizite Aufforderung im B2B-Kontext
- ❌ Emoji-Spam in Text-Posts (2–3 maximal, niemals in jedem Satz)
- ❌ Copy-paste Übersetzungen aus US-Playbooks (kulturell unpassend)
- ❌ Massen-Likes ohne Kommentar (zählt als Spam-Signal)
- ❌ Polls ohne echte Decision-Frage (kann nach hinten losgehen)
- ❌ 12:00–14:00 Posting-Slot in DACH (niedrigste B2B-Engagement)

---

## References

- **IMPORT/05_DACH_Marketing_Spezifika.md** — Section 5.2.1 (LinkedIn als primäre B2B-Plattform)
- **Kennzahlen**: 78% Social Sellers outperformen ihre Peers [web:67]
- **Brand Voice Hooks**: Siehe `DOCS/brand-voice.md` Beispiel-Hooks für Pattern
- **360-Brew-Modell**: Adaptiert von US-Version für DACH-Kultur

---

## VIRON Service-Idee

**"LinkedIn DACH Strategy"** (Spec-Wortlaut) — Content-Plan, Posting-Strategie, Engagement-Automatisierung für B2B-KMUs.

**TODO:** Konkretes Service-Package mit Deliverables (Setup Creator Mode, 30-Tage-Plan, Hook-Library, Engagement-Playbook) muss in `.agents/services/` oder `STORAGE/` definiert werden, bevor dieser Skill in Kundenprojekten eingesetzt wird. Der Skill beschreibt nur **wie** man es macht, nicht **was** als VIRON-Service verkauft wird.

## Buyer-Pain spricht, nicht Tech-Jargon

LinkedIn-Posts in DACH müssen den konkreten Pain des Entscheiders adressieren (siehe `DOCS/icp-summary.md` und `.agents/product-marketing.md`):

- „Termin-Ping-Pong" — 21× geringere Conversion bei Reaktionszeit >5 Min
- „Unstrukturierte Daten" — Excel, Postfächer, lose Zettel, kein CRM
- „Manuelle Prozesse" — Rechnungen, Angebote, Dateneingabe per Hand
- Konkrete Zahlen: „50 Stunden/Woche Dokumentensuche" (10-Mann-Handwerk), „15 Stunden/Woche Portal-Anfragen" (Immobilien), „20 Stunden/Woche Termin-Ping-Pong" (Dienstleister)

Hook-Patterns aus `DOCS/brand-voice.md` (Zahl/Kontrapunkt/Schmerz) mit diesen Buyer-Pains kombinieren — nicht generisches „In der heutigen schnelllebigen Geschäftswelt...".