# VIRON — Aktive Task-Liste
**Stand:** 2026-03-19 | **Pflege:** Täglich aktualisieren nach Task-Abschluss

> Abgeschlossenes Archiv (Linear Setup, bis 2026-03-12) → siehe unten.
> Diese Datei zeigt nur aktive und geplante Tasks.

---

## 🔴 DRINGEND — Blocker (sofort)

| # | Task | Assigned | Status | Notes |
|---|------|----------|--------|-------|
| QA-1 | MG-1: OpenAI-Referenz Zeile ~443 entfernen | Sonnet | ⏳ Pending Operator-Go | 10 Min |
| QA-2 | Pillars-MG-1: Zapier als Fallback framen (nicht gleichwertig) | Sonnet | ⏳ Pending Operator-Go | 20 Min |
| QA-3 | MG-3 + MG-4: QA-Check durchführen | Haiku Three | ⏳ Pending Operator-Go | 2–3h |
| QA-4 | INVENTAR.md: Social-Content-Batch-3 einpflegen | Haiku One | ⏳ Pending | 30 Min |

---

## 🟡 DIESE WOCHE — Content-Produktion

### Content-Serie 1: Nischen-ROI (Handwerk / Immobilien / Steuerberater)

| # | Task | Assigned | Status | Output |
|---|------|----------|--------|--------|
| C1-1 | 10 LinkedIn Posts mit ROI-Zahlen (je Branche 3–4) | Haiku Two | ⏳ Pending | `/Content/_wip/LI-Nischen-ROI.md` |
| C1-2 | 2 Pillar-Artikel: Handwerk + Immobilien ROI-Deep-Dive | Sonnet | ⏳ Pending | `/Content/_wip/Pillar-Nischen.md` |
| C1-3 | 3 Carousel-Outlines (je Branche 1, 5 Slides) | Haiku Two | ⏳ Pending | in C1-1 |

### Content-Serie 2: Faceless Reels

| # | Task | Assigned | Status | Output |
|---|------|----------|--------|--------|
| C2-1 | 15 Reel-Scripts (15–30 Sek, Faceless, Text-Overlay) | Haiku Two | ⏳ Pending | `/Content/_wip/Reel-Scripts-Batch1.md` |
| C2-2 | Reel-Template erstellen (Struktur, Platzhalter, Cue-Markers) | Sonnet | ⏳ Pending | `/Content/Templates/Reel-Template.md` |

### Content-Serie 3: Hook-Bibliothek

| # | Task | Assigned | Status | Output |
|---|------|----------|--------|--------|
| C3-1 | 30 LinkedIn-Post-Drafts (5 Formeln × 6 Posts) | Extern (Gemini/Open Code) | ⏳ Pending Operator | Prompt B aus ORCHESTRATION_SYSTEM.md |

---

## 🟢 BACKLOG — Template-Bibliothek (NEU)

> **Kontext:** Templates werden gebraucht damit spontaner/aktueller Content schnell umgesetzt werden kann — ohne jedes Mal von vorne zu planen. Trendinghemen, spontane Ideen oder Reaktionen auf aktuelle Ereignisse müssen in unter 15 Minuten in ein fertiges Format gebracht werden können.

| # | Task | Assigned | Status | Output |
|---|------|----------|--------|--------|
| T-1 | Reel-Template: Faceless (Screen-Recording + Text-Overlay) | Sonnet | ⏳ Backlog | `/Content/Templates/Reel-Faceless.md` |
| T-2 | Reel-Template: Trending-Topic (schnell befüllbar, <15 Min) | Sonnet | ⏳ Backlog | `/Content/Templates/Reel-Trending.md` |
| T-3 | LinkedIn-Post-Template: Fallstudie / Mythos / Fehler / Frage / Realität | Haiku Two | ⏳ Backlog | `/Content/Templates/LI-Post-Templates.md` |
| T-4 | Carousel-Template: 5-Slide-Struktur (Branche ausfüllbar) | Sonnet | ⏳ Backlog | `/Content/Templates/Carousel-Template.md` |
| T-5 | TikTok-Template: Trending-Sound-Hook (Platzhalter-basiert) | Haiku Two | ⏳ Backlog | `/Content/Templates/TikTok-Template.md` |
| T-6 | n8n Prompt-Template: Trending-Content-Generator (provider-agnostisch) | Sonnet | ⏳ Backlog | `/Content/Templates/n8n-Trending-Prompt.md` |

---

## 📅 CONTENT-KALENDER — Philosophie

**Startdatum:** Ab Montag 2026-03-23 (locker, kein Stress)

**Frequenz-Rampe:**
- **Woche 1–2:** 2–3x/Woche LinkedIn + 2x Reels (Warm-up, Qualität über Quantität)
- **Woche 3+:** Täglich 1 LinkedIn + 3–4 Reels/Woche (sobald Workflow läuft)
- **Ziel-Zustand:** Vollautomatisiert täglich, Operator reviewed + approved nur

**Kalender-Regeln:**
1. Kein festes Datum pro Video/Post. Wenn fertig → raus. Wenn verzögert → nächster Slot.
2. Zwischen geplante Batches können jederzeit Trending-Posts eingeschoben werden (dafür Templates T-1 bis T-5)
3. Trendinghemen haben Vorrang vor Evergreen wenn zeitkritisch
4. Niemals mehr als 3 Tage Pause auf einem Kanal

**Workflow:**
```
Idee (Trending oder Geplant)
  → Template aufmachen
  → Haiku/Extern befüllt in <15 Min
  → Sonnet QA (optional bei Trending, Pflicht bei Serie)
  → Operator Approve (kurz)
  → n8n → Metricool → Publishing
```

---

## 🔧 SYSTEM-TASKS (laufend)

| # | Task | Wann | Status |
|---|------|------|--------|
| S-1 | INVENTAR.md nach jedem Batch aktualisieren | Nach Batch | Ongoing |
| S-2 | Linear MKT-40 kommentieren nach Content-Milestones | Wöchentlich | Ongoing |
| S-3 | ORCHESTRATION_SYSTEM.md reviewen + updaten | Nach großen Änderungen | Ongoing |
| S-4 | Walkthrough_Log.md bei Session-Ende pflegen | Session-Ende | Pflicht |

---

## ✅ ARCHIV — Abgeschlossen

**Linear Setup (2026-03-12):** 2 Teams, 5 Projekte, 35 Issues, 5 Dependencies. Vollständig dokumentiert in `/VIRON_Full_Package_v2/`.

**Content-Pyramide Block 2–4 (2026-03-14):** 4 Mega-Guides + 67 Pillar-Artikel + 41 Social Pieces produziert. Dokumentiert in `/Content/INVENTAR.md`.

**Opus One-Shot Review (2026-03-19):** Strategie-Review + 30-Tage-Plan. Dokumentiert in `/Handover/OPUS_REVIEW_19032026.md`.

---

*Nächste Aktualisierung: Nach QA-Go vom Operator (QA-1 bis QA-4)*
