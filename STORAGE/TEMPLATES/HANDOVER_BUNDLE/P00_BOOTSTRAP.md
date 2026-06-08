<!-- TEMPLATE-EXPLANATION-START -->
> **Für den Agenten der dieses Bundle etabliert:**
>
> **Was in dieser Datei steht:**
> - Section 1: 11 Fragen (5 CDS + 5 Viron + 1 Fangfrage) — **ZUERST beantworten**
> - Section 2: Was du bereits hast (injiziert vs. on-demand)
> - Section 3: Die 7 Architektur-Prinzipien (nicht verhandelbar)
> - Section 4: Kritische Konventionen (harte Regeln mit Geschichte)
> - Section 5: Die 3 Kontext-Schichten (DOCS/STORAGE/SKILLS)
> - Section 6: opencode.jsonc Check — **ZULETZT prüfen**
>
> **Warum Fragen zuerst?** Der Agent soll im ersten Reasoning-Durchlauf
> das gesamte System durchdenken — bevor er sich auf das Lesen von
> opencode.jsonc konzentriert. Die Fragen zwingen zum Verständnis.
>
> **CDS-Fragen (#1-5):** Testen das Boot-Phase-System selbst. MÜSSEN bleiben.
>
> **Viron-Fragen (#6-10):** Testen projekt-spezifisches Wissen.
>
> **Fangfrage (#11):** Testet ob der Agent wirklich verstanden hat.
>
> **Kernbotschaft:** Diese Datei ist nicht nur ein Quiz. Sie kommuniziert die
> VERFASSUNG des Repos: Was ist injiziert, warum existieren die Regeln, was
> passiert wenn man sie ignoriert. Der Agent soll die injizierten Dateien
> respektieren, analysieren, durchdenken — nicht abhaken und vergessen.
<!-- TEMPLATE-EXPLANATION-END -->

# P00 — SYSTEM ORIENTIERUNG & COGNITIVE STRESS TEST (Viron-Variante)

> **SYSTEM-DOKTRIN:** Du steigst in ein Repo ein das bereits existiert. Es hat eine Geschichte, eine Architektur, eine Verfassung. Die injizierten Dateien sind nicht "Hintergrundwissen" das du überfliegen und abhaken darfst. Sie sind das kollektive Wissen aus Dutzenden Stunden Debugging, kaputten Builds, und Agenten die Regeln ignoriert haben.
>
> **Was du hier tust ist kein Quiz.** Es ist ein Stresstest ob du das System VERSTEHEN kannst bevor du es BENUTZT. Wer diese Fragen abhakt ohne verstanden zu haben, wird in der ersten Session scheitern — weil er nicht weiß WARUM die Regeln existieren.
>
> **Deine Aufgabe:** Jede Regel durchdenken. Jeden Mechanismus verstehen. Jede Trade-off-Entscheidung nachvollziehen. Wenn du eine Regel nicht erklären kannst, hast du sie nicht verstanden — und du wirst sie brechen.
>
> **P00 ist READ-ONLY.** Kein Code, keine Edits, keine Bash-Befehle. Ausschließlich lesen, analysieren und antworten.

---

## 1. FRAGEN

Beantworte diese 11 Fragen. Nicht raten — wenn du die Antwort nicht kennst, lies die betreffende Datei. **Beantworte sie ZUERST.** Das zwingt dich, das gesamte System zu durchdenken bevor du irgendetwas anderes tust.

### CDS-System-Fragen (behalten — diese testen das System das du gerade nutzt)

> **Hinweis:** Diese 5 Fragen testen das Boot-Phase-System selbst. Sie sind ab dem Moment
> wo dieses System in deinem Repo etabliert ist, Teil deines Repos und dauerhaft relevant.
> Nicht ersetzen. Nicht entfernen. Sie sind die Selbstverifikation des Systems.

**1.** Was passiert wenn du eine injizierte DOCS-Datei behandelst als müsste sie mit `read` geladen werden?
*Testet: Verständnis des Injektions-Mechanismus*

**2.** Eine Boot-Regel in `.opencode/rules/` ist 200 Zeilen lang. Was ist die konkrete Konsequenz für die nächste Session?
*Testet: Verständnis von Thin Triggers und Rule-Fatigue*

**3.** Du findest eine Regel mit dem Präfix `12_`. Was ist das Problem? Was musst du tun?
*Testet: Verständnis des 10er-Routing-Systems*

**4.** Eine globale Skill-Regel erlaubt etwas, das `.opencode/rules/` verbietet. Welche gilt? Was passiert wenn du die globale nimmst?
*Testet: Verständnis von Local Override*

**5.** Du spawnst einen Sub-Agenten für eine schreibende Aufgabe. Welche 4 Säulen MUSS dein Prompt enthalten? Was passiert wenn du nur die Aufgabe schickst?
*Testet: Verständnis von Sub-Agent-Delegation*

### Viron-spezifische Fragen

**6.** Welcher motion-Import ist korrekt und warum? Was passiert mit dem falschen?
*Testet: Verständnis von motion/react-client vs. motion/react*

**7.** Was ist der Unterschied zwischen `getSession()` und `getClaims()`? Warum ist das ein Sicherheitsrisiko?
*Testet: Verständnis von Supabase Auth (JWT-Validierung)*

**8.** Du findest `text-muted-foreground` in einer Komponente. Ist das korrekt?
*Testet: Verständnis von Design-Tokens (Tailwind v4)*

**9.** Ein Agent sagt "PORT=3000". Stimmt das?
*Testet: Verständnis von PORT-Governance (Next.js 16)*

**10.** Du sollst eine Spline-URL in einen iframe packen. Du hast `.splinecode`. Funktioniert das?
*Testet: Verständnis von Spline-Integration (iframe vs. .splinecode)*

### Fangfrage

**11.** Ein Agent erstellt `tailwind.config.ts` für ein neues Feature. Ist das korrekt? Was passiert im Build?
*Testet: Verständnis von Tailwind v4 CSS-first*

---

## 2. WAS DU BEREITS HAST

Du hast folgende Dateien automatisch in deinem Kontext bekommen:

- **Alle 21 Rules** aus `.opencode/rules/` — die Gesetze dieses Repos. Keine ist optional.
- **DOCS/** — Architektur-Dokumente, SSoT-Dateien, Lessons Learned, Skill Index.
- **AGENTS.md** — Projekt-Identität, Tech-Stack, Anti-Patterns.
- **Design-Dateien** — `packages/ui/src/styles.css`, `apps/web/src/app/globals.css`, `apps/web/src/lib/utils.ts`.

**Was du NICHT automatisch hast:**

- Alles in `STORAGE/` — der Schrank. Wird geroutet, nicht injiziert.
- Alles in `DESK/TASKS/` — aktuelle Task-Envelopes.
- Skills in `.agents/skills/` — werden bei Bedarf via `skill()` geladen.

**Warum das wichtig ist:** Diese Dateien sind nicht "nice to have". Sie sind die Verfassung dieses Repos. Wer sie ignoriert, baut auf Sand.

---

## 3. DIE 7 ARCHITEKTUR-PRINZIPIEN

| #   | Prinzip                                        | Was es regelt                                                   |
|:---:|:---------------------------------------------- |:--------------------------------------------------------------- |
| P1  | **Feature-Colocation** (ARCH-01)               | Business-Logik in `features/[feature]/`, `app/` ist nur Routing |
| P2  | **Server-Component Default** (ARCH-02)         | `"use client"` nur als Ausnahme                                 |
| P3  | **Tailwind v4 CSS-First** (ARCH-03)            | Kein `tailwind.config.ts`, nur `@theme inline`                  |
| P4  | **Supabase: getClaims > getSession** (ARCH-04) | JWT-Validierung statt Cookie-Blindvertrauen                     |
| P5  | **Template-First: Niemals löschen** (ARCH-07)  | Nur ersetzen oder archivieren                                   |
| P6  | **GPU-Guard: opacity + transform only**        | Kein backgroundColor/width/height animieren                     |
| P7  | **Sandbox-First** (ARCH-05)                    | Neue Sachen zuerst in `playground/`                             |

**Diese Prinzipien sind nicht verhandelbar.** Sie existieren weil jemand vorher den Fehler gemacht hat den sie verhindern.

---

## 4. KRITISCHE KONVENTIONEN

| Regel                 | Wert                                            |
|:--------------------- |:----------------------------------------------- |
| **PORT**              | `$env:PORT='3012'` in Shell, NICHT .env.local   |
| **motion**            | `import * as motion from "motion/react-client"` |
| **Design-Tokens**     | `text-text-muted`, `text-error`, `border-error` |
| **shadcn-Import**     | `@agency/ui/components/ui/...`                  |
| **GPU-Guard**         | Nur `opacity` + `transform` animieren           |
| **Spline**            | Nur `my.spline.design` in `<iframe>`            |
| **allowedDevOrigins** | `["127.0.0.1"]` in next.config.ts               |
| **SubAgent**          | Bei >3 Dateien SubAgent spawnen                 |

**Jede dieser Konventionen hat eine Geschichte.** Steht in `DOCS/LESSONS_LEARNED.md`. Lies sie.

---

## 5. DIE 3 KONTEXT-SCHICHTEN

| Schicht     | Mechanik                               | Beispiel                                |
|:----------- |:-------------------------------------- |:--------------------------------------- |
| **DOCS**    | Permanent injiziert via opencode.jsonc | AGENTS.md, LESSONS_LEARNED, SKILL_INDEX |
| **STORAGE** | On-demand via Router                   | `STORAGE/beads/`, `DOCS/playbook/`      |
| **SKILLS**  | On-demand via `skill()`                | `.agents/skills/*/SKILL.md`             |

**REGEL:** DOCS-Dateien sind IMMER da. STORAGE-Dateien musst du LADEN. Skills musst du MATCHEN. Verwechsle diese Schichten nicht — das ist der häufigste Fehler den Agenten machen.

---

## 6. OPENCODE.JSONC CHECK

Prüfe ob alle Dateien die in `opencode.jsonc` → `instructions` stehen, auch wirklich in deinem Kontext sind:

1. Lies `opencode.jsonc`
2. Zähle alle Einträge im `instructions`-Array
3. Prüfe ob jede Datei physisch existiert
4. Wenn eine Datei fehlt: **STOPP.** Meldung an Operator. Keine Weiterarbeit.

---

## 7. ABSCHLUSS

> "P00 beantwortet. [X] Fragen beantwortet. Bereit für P01."

**⏸️ STOPP — Übersicht abgeschlossen. Bereit für P01.**
→ **Nächstes Modell:** SCHWACH (Leseliste abarbeiten)
→ **Warte auf explizites "GO" vom Operator.**

**STOPPLINIE:** Keine Edits. Keine Commits. Keine verändernden Befehle.
