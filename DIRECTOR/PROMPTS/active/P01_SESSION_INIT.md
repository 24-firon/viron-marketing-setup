# P01 — SESSION INIT: MARKETING-SETUP EXECUTION

> **P00 BESTANDEN.** Du hast den kognitiven Stresstest bestanden. Jetzt beginnt die operative Arbeit.
>
> **P01 ist EXECUTION-MODE.** Lesen, Schreiben, Bash — alles erlaubt, aber diszipliniert. Kein Blindflug.

---

## 1. VORGESCHICHTE

Du übernimmst eine laufende VIRON Marketing-Setup Session. Der Director hat dir bereits den Kontext freigegeben. Deine Aufgabe ist in diesem Dokument exakt spezifiziert. Arbeite linear, Stopp für Stopp.

**Aktueller Phasenstand:** Phase 2 (Task-Checklisten) — fast abgeschlossen
**Letzter Meilenstein:** M2 (Reports erstellt, Steuerdateien angelegt)

---

## 2. SSoT-LESELISTE (Wissensladung — priorisiert)

Lade diese Dateien in EXAKT dieser Reihenfolge in deinen aktiven Kontext. Überspringe keine.

| Priorität | Datei | Warum |
|:----------|:------|:------|
| **P0** | `CONTEXT.md` | Repo-Status, aktuelle Phase, Blocker |
| **P1** | `MILESTONES.md` | Aktiver Meilenstein, Erfolgskriterien |
| **P2** | `TASKS.md` | Aktive Tasks, Prioritäten |
| **P3** | `DECISIONS.md` | Warum ist was wie entschieden |
| **P4** | `DESK/TASKS/implementation_plan.md` | Linearer Bauplan für diese Session |
| **P5** | `DESK/HANDOVER/sessions/session-2026-05-25.md` | Letztes Handover — was wurde gemacht |

---

## 3. ABSOLUTE PRIORITÄTSKETTE (P0 First)

Arbeite exakt in dieser Reihenfolge. Nach jedem Meilenstein: **STOPPEN, Berichten, auf GO warten.**

### P0.1: DACH-P0-Skills bauen
- **Ziel:** 3 DACH-spezifische Marketing-Skills in .agents/skills/ installiert
- **Task-Envelope:** `DESK/TASKS/dach-p0-skills/PROMPT_INITIAL.md`
- **Schritte:** SKILL.md + evals/ erstellen, spiegeln, Router updaten

### P0.2: MILESTONES.md aktualisieren
- **Ziel:** M2-Kriterien final abhaken
- **Schritte:** Erfolgskriterien prüfen, Status setzen

### P0.3: Commit erstellen
- **Ziel:** Alle Änderungen sauber committen
- **Schritte:** git add, git commit mit Linear-Referenz

---

## 4. MINDSET-BLOCK

- **Templater, nicht Codierer:** Du schreibst keine Python-Logik, wenn der Task Prompt-Arbeit ist.
- **Surgical Precision:** Ändere Dateien nur nativ (`edit` / `write`). Kein Blindflug mit `sed`.
- **Evidence-Based Execution:** Traue keinem `exit 0`. Liefere immer die letzten 5 Zeilen des echten Terminal-Outputs.
- **Linearer Gehorsam:** Führe die Schritte im Plan nacheinander aus.
- **Approval-Gates:** Kritische Aktionen (`rm`, `reset`, `drop`, `deploy`) brauchen explizites "GO" vom Director.

---

## 5. STOPP-PUNKTE

| Stopp | Nach P0.x | Aktion |
|:------|:----------|:-------|
| Stopp 1 | P0.1 | Berichte Ergebnis, zeige Evidence (erste 20 Zeilen SKILL.md) |
| Stopp 2 | P0.2 | Berichte Ergebnis, zeige MILESTONES.md Diff |
| Stopp 3 | P0.3 | Berichte Commit-Hash und Zusammenfassung |
| Final | Letzter P0.x | Berichte Abschluss, bereite Handover vor |

Nach jedem Stopp: **Warte auf explizites "GO" vom Director, bevor du den nächsten Schritt beginnst.**

---

## 6. FINALER START-BEFEHL

> **Starte jetzt mit Schritt P0.1: DACH-P0-Skills bauen.** Lies die SSoT-Dateien, bestätige den Erhalt des Auftrags, und führe den ersten Schritt aus.
