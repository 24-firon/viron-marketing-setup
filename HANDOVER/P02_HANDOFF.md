<!-- TEMPLATE-EXPLANATION-START -->
> **Für den Agenten der dieses Bundle etabliert:**
>
> **Was in dieser Datei steht:**
> - Section 1: Task-Verständnis (Fragen ZUR P01-Leseliste — KEINE Leseliste!)
> - Section 2: Meilensteine (Platzhalter — werden pro Task definiert)
> - Section 3: Modell-Rotation (STARK→SCHWACH→STARK→MITTEL/SCHWACH/STARK)
> - Section 4: Mindset-Block
>
> **KEINE Leseliste in P02.** Die steht in P01. P02 verarbeitet das was in P01 gelesen wurde.
> **KEINE Regelaktivierung in P02.** Regeln sind auto-injiziert (P00-Thema).
>
> **Task-spezifische Fragen:** Werden vom Vorgängersessionagenten oder vom Orchestrator befüllt. Sie testen ob der Agent das Gelesene wirklich verstanden hat.
>
> **Meilensteine:** Sind Platzhalter. Das Ziel-Repo definiert eigene Meilensteine. Ein gutes Beispiel:
> - M1: DOCS-Infrastruktur (9 Dateien erstellen)
> - M2: DESK-Struktur (7 Dateien + Ordner)
> - M3: DIRECTOR-Struktur (5 Ordner + Templates)
<!-- TEMPLATE-EXPLANATION-END -->

# P02 — SESSION INIT & EXECUTION (Viron-Variante)

> **P01 GELESEN.** Du hast die Dateien gelesen. Jetzt prüfst du ob du sie verstanden hast und planst die Ausführung.
>
> **P02 ist PLAN-MODUS.** Fragen beantworten, Pläne schreiben, Meilensteine definieren. Kein Editieren.

---

## 1. TASK-VERSTÄNDNIS (Fragebogen)

Die task-spezifischen Fragen stehen IN DIESER DATEI. Sie wurden vom Vorgängersessionagenten oder vom Orchestrator erstellt und beim Session-Übergabe in diese Datei geschrieben.

Die Fragen betreffen den spezifischen Task-Context — Reports, Research-Dateien, alle Dateien die zur Task gehören. Sie sind INDIVIDUELL und ändern sich von Task zu Task.

| # | Frage | Antwort |
|:--|:------|:--------|
| 1 | Was ist die Mission dieser Session? Was ist das Endergebnis? | [Deine Antwort] |
| 2 | Welche Dateien hast du gelesen? Was war der wichtigste Erkenntnis? | [Deine Antwort] |
| 3 | Was sind die 3 goldenen Regeln für diese Session? | [Deine Antwort] |
| 4 | [Frage steht hier — wurde vom Orchestrator/Vorgänger hier reingeschrieben] | [Deine Antwort] |
| 5 | [Frage steht hier] | [Deine Antwort] |

**REGEL:** Beantworte die Fragen basierend auf dem was du aus der P01-Leseliste verstanden hast. NICHT raten — wenn du die Antwort nicht kennst, lade die betreffende Datei nach.

---

## 2. MEILENSTEINE

### M1: [Deine erste Phase]
- [ ] [Schritt 1 — konkrete Aktion mit Befehl oder Tool-Call]
- [ ] [Schritt 2 — konkrete Aktion mit Befehl oder Tool-Call]

**⏸️ STOPP 1 — Berichte Ergebnis, zeige Evidence (letzte 5 Zeilen Output).**

### M2: [Deine zweite Phase]
- [ ] [Schritt 1 — konkrete Aktion mit Befehl oder Tool-Call]
- [ ] [Schritt 2 — konkrete Aktion mit Befehl oder Tool-Call]

**⏸️ STOPP 2 — Berichte Ergebnis, zeige Evidence.**

### M3: [Deine dritte Phase]
- [ ] [Schritt 1 — konkrete Aktion mit Befehl oder Tool-Call]
- [ ] [Schritt 2 — konkrete Aktion mit Befehl oder Tool-Call]

**⏸️ STOPP 3 — Berichte Abschluss.**

---

## 3. MODELL-ROTATION

| Phase | Modell | Zweck |
|:------|:-------|:------|
| **P00** | STARK | Comprehension — Verständnisfragen beantworten |
| **P01** | SCHWACH | Nur lesen — viele Dateien iterieren |
| **P02** | STARK | Planung — Fragen beantworten, Pläne schreiben |
| **Ausführung** | MITTEL/SCHWACH/STARK | Befehle ausführen — je nach Schritt wechselnd |
| **STOPPs** | STARK | Report schreiben, Evidence bewerten |

**Regel:** Niemals alles mit demselben Modell machen. Modell-Rotation ist Pflicht.

---

## 4. MINDSET-BLOCK

- **Surgical Precision:** Ändere Dateien nur nativ (`edit` / `write`).
- **Evidence-Based Execution:** Traue keinem `exit 0`. Liefere Output.
- **Linearer Gehorsam:** Führe Schritte nacheinander aus.
- **Approval-Gates:** Kritische Aktionen brauchen "GO" vom Operator.

---

## ABSCHLUSS

> "P02 geplant. [X] Meilensteine definiert. Bereit für Ausführung."

**⏸️ STOPP — P02 geplant. [X] Meilensteine definiert. Bereit für Ausführung.**
→ **Nächstes Modell:** MITTEL/SCHWACH/STARK (Befehle ausführen — je nach Schritt wechselnd)
→ **Warte auf explizites "GO" vom Operator.**

**STOPPLINIE:** Kein Editieren. Nur planen. Warte auf GO vom Operator.
