<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - DoD-Referenz (ausgefülltes Beispiel) für die HANDOVER-Datenübergabe
> - 7 Sektionen: BLUF, Projektdaten, Erledigte Arbeit, Entscheidungen, Offene Tasks, Probleme, Nächste Schritte
> - Bestätigungs-Formel und "KEINE FRAGEN IN HANDOVER"-Hinweis
>
> - **Bundle-Verwendung:** Template-Quelle: `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/TEMPLATES/HANDOVER.md`. Arbeitskopie: `HANDOVER/TASK_[SESSION]_V[N]/`. Diese Datei wird NICHT in die Arbeitskopie kopiert — sie ist systemisch.
<!-- TEMPLATE-EXPLANATION-END -->

# EXAMPLE_HANDOVER — Definition of Done

> **Zweck:** DoD-Referenz für ausgefüllte HANDOVER.md. Agent vergleicht seinen Output mit diesem Beispiel.
> **Wann lesen:** VOR dem Schreiben des Handover (Token-Budget grün erforderlich).

---

```markdown
---
session_title: HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1
session_type: BUNDLE_REPAIR_SKILL_GEN
bundle: KOMPAKT
bundle_mode: AUSFÜHRLICH
date: 2026-06-07
next_session: HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V2
---

# HANDOVER — DATENÜBERGABE

> **Was ist das?** Eine Knowledge-Datei (temporär) die projektspezifische Daten für die nächste Session enthält. Reine Informationsweitergabe — keine Fragen, keine Verifikation.

## 1. BLUF (Bottom Line Up Front)

> [Ein Satz: Was wurde in dieser Session erreicht?]

---

## 2. PROJEKT-SPEZIFISCHE DATEN

Diese Informationen stehen nirgendwo anders. Sie müssen dem nächsten Agenten explizit mitgegeben werden.

| Schlüssel | Wert | Beschreibung |
|:----------|:-----|:-------------|
| [z.B. Server-IP] | [z.B. 123.456.789.0] | [z.B. Hetzner Root-Server, SSH-Zugriff via Key] |
| [z.B. Datenbank-Port] | [z.B. 5433] | [z.B. Nicht Standard-Port, SSH-Tunnel nötig] |
| [z.B. API-Endpunkt] | [z.B. http://127.0.0.1:8081] | [z.B. Viron Worker Health-Check] |

---

## 3. ABGESCHLOSSENE ARBEIT

| Was | Status | Beschreibung |
|:----|:------:|:-------------|
| [Aufgabe] | ✅ | [Was wurde getan] |
| [Aufgabe] | ✅ | [Was wurde getan] |

---

## 4. ENTSCHEIDUNGEN

| Entscheidung | Begründung | Reversibel? |
|:-------------|:-----------|:------------:|
| [Was wurde entschieden] | [Warum] | Ja/Nein |

---

## 5. OFFENE TASKS

| Task | Priorität | Status | Beschreibung |
|:-----|:---------:|:------:|:-------------|
| [Task] | P0/P1 | OFFEN | [Was muss noch getan werden] |

---

## 6. BEKANNTE PROBLEME & WORKAROUNDS

| Problem | Workaround | Fix geplant? |
|:--------|:-----------|:------------:|
| [Bug-Beschreibung] | [Workaround] | Ja/Nein |

---

## 7. NÄCHSTE SCHRITTE

1. **[Schritt 1]** — [Konkrete Aktion]
2. **[Schritt 2]** — [Konkrete Aktion]

---

> **Handover abgeschlossen.** Warte auf nächsten Operator-Auftrag.

---

## WICHTIG: KEINE FRAGEN IN HANDOVER

Diese Datei enthält reine Daten. Fragen, Verifikationen und P00-Tests gehören in andere Dateien.
```

---

## DoD-Kriterien (Selbstprüfung)

Bevor du Handover abgibst, prüfe:

- [ ] YAML-Header mit `session_title`, `session_type`, `bundle`, `bundle_mode`, `date`, `next_session`
- [ ] BLUF in 1-2 Sätzen (dicht, präzise)
- [ ] Entscheidungs-Tabelle mit Reversibilität
- [ ] Offene Tasks mit Priorität
- [ ] Bekannte Probleme mit Workaround
- [ ] Nächste Schritte sind KONKRET (nicht "weitermachen")
- [ ] Session-Titel für V2 ist genannt
- [ ] **KEINE Fragen im Handover** (Fragen gehören in P00 der Folgesession)
