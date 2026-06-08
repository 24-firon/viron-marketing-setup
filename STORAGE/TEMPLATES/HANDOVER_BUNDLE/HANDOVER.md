<!-- TEMPLATE-EXPLANATION-START -->
> **Für den Agenten der dieses Bundle etabliert:**
>
> **Was in dieser Datei steht:**
> - REINE DATENÜBERGABE — keine Fragen, keine Verifikation
> - Projekt-spezifische Daten (IPs, Configs, Endpunkte) die NIRGENDS anders stehen
> - Wird während der Session aktiv genutzt und am Ende befüllt
> - Unterschied zu P02: HANDOVER = Daten, P02 = Forensischer Report
>
> **Ort:** Wird auf DESK/ (Arbeitstisch) abgelegt, nicht in DIRECTOR/.
>
> **Adaptiert aus:** Viron-agency-stack HANDOVER.md (93Z)
<!-- TEMPLATE-EXPLANATION-END -->

# HANDOVER — DATENÜBERGABE (Master-Variante)

> **Was ist das?** Eine Knowledge-Datei (temporär) die projektspezifische Daten für die nächste Session enthält. Wird während der Session aktiv genutzt und am Ende befüllt.
>
> **Zweck:** Diese Datei enthält projekt- und task-spezifische Daten die nirgendwo anders stehen. IP-Adressen, Konfigurationen, Workarounds, bekannte Bugs. Reine Informationsweitergabe — keine Fragen, keine Verifikation.
>
> **Wann nutzen:** Während der Session nachschauen, am Session-Ende ausfüllen, dem nächsten Agenten übergeben.

---

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
| [z.B. Vault-Status] | [z.B. Sealed nach Reboot] | [z.B. Operator muss manuell entsiegeln] |

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

Diese Datei enthält **reine Daten**. Fragen, Verifikationen und P00-Tests gehören in `P02_HANDOFF.md` (Forensischer Report) oder in `P00_BOOTSTRAP_DISPATCHER.md` (Stress-Test-Fragen).

**Adaptiert aus:** Viron-agency-stack HANDOVER.md (93Z, P00-Fragen entfernt)
