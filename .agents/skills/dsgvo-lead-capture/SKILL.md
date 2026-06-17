---
name: dsgvo-lead-capture
description: "When the user wants to build DSGVO-compliant lead capture in the DACH region. Also use when the user mentions 'DSGVO-konformes Formular,' 'Consent-Management,' 'Cookie-Banner Alternative,' 'Server-Side-Tracking,' 'Lead-Erfassung Datenschutz,' 'Double Opt-in Lead Form,' 'GA4 Server-Side Setup,' 'Meta CAPI DSGVO-konform,' 'First-Party Data Capture,' or 'Progressive Profiling DSGVO.' Use this for any lead generation, consent management, cookie-consent, or privacy-safe tracking work targeting German, Austrian, or Swiss audiences."
metadata:
  version: 1.0.0
---

# DSGVO-Lead-Capture (DACH)

You design and implement DSGVO-compliant lead capture systems for DACH-region KMU (Germany, Austria, Switzerland). Every recommendation prioritizes privacy-by-design over marketing convenience — because in DACH, DSGVO-compliance is the baseline, not a feature.

VIRON differentiator: **DSGVO-by-Design as a service** — US agencies treat DSGVO as an afterthought. We design from the consent layer upward, with first-party data and server-side tracking as the default architecture.

## Workflow

### Step 1: Identify the Capture Surface

Ask or determine where the lead capture happens:

- **Website form** (Contact, Demo Request, Download)
- **Landing page** (Single conversion goal)
- **Lead magnet** (PDF, Tool, Template, Quiz, Calculator)
- **Newsletter signup** (Email-only)
- **WhatsApp / Phone** (requires explicit consent text)

Each surface triggers a different consent flow. Never reuse one form's consent logic for another without review.

### Step 2: Design the Consent Layer

Three components must always be present:

1. **Granular consent options** — never bundle. Separate checkboxes for:
   - Email marketing (with double opt-in)
   - Phone contact (with purpose)
   - Analytics tracking (anonymized vs. personalized)
   - Third-party sharing (which vendors, named explicitly)

2. **Easy withdrawal** — every email contains a one-click unsubscribe. Withdrawal confirmation is automated via N8N.

3. **Transparent purpose statement** — one sentence per consent option explaining what data is collected and why. No legalese beyond 12-word sentences.

Reference: `IMPORT/05_DACH_Marketing_Spezifika.md` section 5.3.1 for the framework.

### Step 3: Choose Capture Method

Prefer **value-first, first-party data capture**:

- **Interactive content**: Quizzes, Calculators (e.g. "Wie viel Zeit sparst du mit Automatisierung?"). High engagement, low friction.
- **Lead magnets with teeth**: PDF guides, Notion templates, swipe files — must be substantively useful, not generic.
- **Progressive profiling**: Capture email first, role/company later. Don't ask 8 fields upfront.
- **Never**: Aggressive popups, hidden pre-checked boxes, cookie walls that block content.

### Step 4: Architect the Tracking

Default architecture: **PostgreSQL-first, server-side tracking**.

- **GA4 Server-Side** via N8N as proxy — never client-side Google Tag Manager alone.
- **Meta CAPI** via N8N webhook — no browser pixel firing before consent.
- **LinkedIn Insight Tag** gated behind explicit consent (use cookie category).
- **All event data** stored in PostgreSQL (Schema-Namen TODO — wird in M2b mit Operator finalisiert; siehe `DESK/REPORTS/tool-decisions.md` für Architektur-Entscheidung) — queryable, portable, no vendor lock-in.

Reference: `DOCS/icp-summary.md` for ICP pain points around unstrukturierte Daten.

### Step 5: Document Compliance

Generate or update the customer's `Datenschutzerklärung` section for lead capture. Include:

- Which data is collected (per form field)
- Purpose and legal basis (Art. 6 Abs. 1 DSGVO)
- Retention period (default 24 months, configurable)
- Vendor list with data processing agreements (AVV)
- Contact for data subject requests

Use VIRON's reusable templates; never copy-paste from US-based generators.

---

## Core Principles

### Privacy over Personalization

DACH users will trade personalization for privacy. Default to **minimal data capture**. Capture only what the next sales conversation actually needs.

### Consent is Granular, Not Bundled

One "I agree" checkbox for everything is not DSGVO-compliant in DACH. Each purpose requires its own opt-in, even if it adds friction.

### Server-Side First, Browser Last

Client-side tracking is broken-by-default in DACH. Default to N8N-mediated server-side. Browser pixels only fire after explicit consent, and they pass server-side data when possible.

### Documentation is a Deliverable

Every lead-capture implementation ships with a 1-page compliance summary: what data, where stored, how long, who can access. Customers need this for their own Datenschutzerklärung.

**TODO M2b:** Konkrete Vorlage für die 1-Page-Compliance-Summary fehlt noch. Entweder als Template in `.agents/templates/` ablegen oder in `STORAGE/` referenzieren. Bis dahin: jede Lead-Capture-Implementierung erstellt das Summary ad-hoc, Output-Format bleibt aber dasselbe.

### Buyer-Pain spricht, nicht Tech-Jargon

DACH-KMU-Entscheider (siehe `DOCS/icp-summary.md`) denken in konkreten Verlusten, nicht in DSGVO-Artikeln. Lead-Capture-Copy muss den Pain adressieren:

- „Termin-Ping-Pong — 21× geringere Conversion wenn nicht in 5 Minuten reagiert" (aus ICP-Pain #2)
- „Unstrukturierte Daten in Excel, Postfächern, losen Zetteln — kein CRM" (ICP-Pain #3)
- „50 Stunden/Woche Dokumentensuche allein im 10-Mann-Betrieb" (aus `.agents/product-marketing.md`)

Diese Zahlen in Confirmation-Mails, Datenschutz-Hinweisen und Opt-in-Texten einsetzen — nicht „Wir verarbeiten Ihre Daten gemäß Art. 6 Abs. 1 lit. b DSGVO".

---

## Trigger-Phrasen

Siehe YAML-Frontmatter (`description`) — alle Trigger-Phrasen sind dort zentral gepflegt.

---

## Dependencies

1. **Foundation**: `.agents/product-marketing.md` — must exist; this skill reads ICP and pain points from there
2. **Brand Voice**: `DOCS/brand-voice.md` — for tone in consent text and confirmation emails
3. **ICP**: `DOCS/icp-summary.md` — for role-based consent defaults (B2B vs. B2C)
4. **Automation**: N8N deployed (M3 dependency) — for double opt-in flows, withdrawal automation, server-side proxy
5. **Database**: PostgreSQL access (Tabellennamen TODO — siehe Schema-Definition in M2b/`DESK/REPORTS/tool-decisions.md`)

## NOT Dependencies

- Cookie-Consent-Tool (Usercentrics, Cookiebot) — *can* be used but not required. Preference Center is the VIRON-recommended alternative.

---

## Output Format

When you complete a DSGVO-lead-capture task, deliver:

1. **Form spec** — fields, consent checkboxes, validation rules (JSON or YAML)
2. **Consent text** — granular, ≤12 words per option, in German
3. **N8N workflow sketch** — double opt-in trigger, withdrawal trigger, server-side event proxy
4. **Compliance summary** — 1-page Markdown, customer-ready
5. **Test cases** — minimum 3: valid signup, withdrawal flow, consent-declined flow

---

## Anti-Patterns (Vermeide diese)

- ❌ Pre-checked consent boxes (illegal in DACH, BGH 2020 ruling)
- ❌ One "I agree" for everything (Art. 7 DSGVO requires granular consent — siehe „Consent is Granular, Not Bundled")
- ❌ Client-side tracking before consent (even anonymized — Google has been fined for this)
- ❌ Generic US privacy policy copy-pasted and machine-translated
- ❌ Cookie wall that blocks content (regulator-friendly alternative: Preference Center)
- ❌ Capture-for-the-sake-of-it: if you don't need phone number, don't ask
- ❌ Vendor list in privacy policy without actual AVV (Auftragsverarbeitungsvertrag) signed

---

## References

- **IMPORT/05_DACH_Marketing_Spezifika.md** — Section 5.1.1 (DSGVO 2026 Verschärfungen), Section 5.3.1 (DSGVO-Compliant Lead Generation Framework)
- **Regulatorik**: DSGVO Art. 6, 7; E-Privacy-Verordnung; AI Act (KI-generierte Interaktionen)
- **N8N Workflow Patterns**: Server-side proxy, double opt-in, withdrawal automation (M3 dependency)
- **Brand Voice**: Direkt, deutsch, kein Bullshit — applies to consent text and confirmation emails

---

## VIRON Service-Idee

**"DACH DSGVO Lead Engine"** — Setup von Formularen, Consent-Layer, N8N-Server-Side-Tracking, Compliance-Dokumentation. Deliverable: laufende Lead-Generierung die einer Landesbeauftragten-Prüfung standhält.