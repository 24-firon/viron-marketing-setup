<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Session-Titel-Format: `[PROJEKT]_[TYP]_[KURZTHEMA]_V[N]`
> - Edge-Case: `[VORHER]-TO-[NEU]_V[N]` bei Themenwechsel
> - V1/V2-Logik für Folgesession
> - Report-Dateinamen-Logik (kurz/lang + Such-Tool)
>
> - **Bundle-Verwendung:** Diese Datei wird NICHT in die Arbeitskopie kopiert — sie ist systemisch.
<!-- TEMPLATE-EXPLANATION-END -->

# SESSION_TITEL_SCHEMA — Vergabe-Logik für Session-Namen

> **Wann lesen:** BEIM Schreiben des Handover (HD-4). Pflicht-Referenz für jeden Session-Architect.

## 1. Standard-Format

```
[PROJEKT]_[TYP]_[KURZTHEMA]_V[N]
```

**Bestandteile:**
- **PROJEKT** — Repo- oder Projekt-Kurzname (z.B. `CDS`, `WEBAPP`, `MOBILE`)
- **TYP** — Session-Typ (z.B. `BUNDLE_REPAIR`, `AUTH_IMPL`, `DOCS_RESTRUCT`)
- **KURZTHEMA** — Was war das Thema (z.B. `SLIM_TO_KOMPAKT`, `SUBAGENT_PROMPTS`)
- **V[N]** — Versionsnummer (V1, V2, V3...)

## 2. Edge-Case: Thema hat sich drastisch geändert

**WENN** sich das Thema in der aktuellen Session komplett geändert hat (z.B. von Bundle-Reparatur zu Skill-Generierung), DANN erweiterte Form:

```
[VORHER]_-TO-[NEU]_V[N]
```

**Beispiele:**

| Session-Titel | Bedeutung |
|:---|:---|
| `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1` | Startete als Handover-Bundle-Repair, wurde zu CDS-Skill-Generierung |
| `WEBAPP_AUTH_V1-TO-PERFORMANCE_TUNING_V1` | Startete als Auth, wechselte zu Performance |
| `CDS_RESTRUCTURING_V1-TO-CDS_RESTRUCTURING_V2` | Versionierung + Themenwechsel kombiniert |

**Begründung:** Der Themenwechsel ist relevant für die Folgesession — sie muss wissen, was SIE anders machen soll.

**Faustregel:** `-TO-` nur verwenden, wenn das NEUE Thema mindestens 30% der Session ausgemacht hat.

## 3. V1/V2-Logik (Folgesession)

**Wenn Session-Titel aus Session-Start vorhanden:**

| Aktueller Titel | Folgesession-Titel |
|:---|:---|
| `CDS_BUNDLE_REPAIR_V1` | `CDS_BUNDLE_REPAIR_V2` |
| `WEBAPP_AUTH_IMPL_V3` | `WEBAPP_AUTH_IMPL_V4` |
| `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1` | `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V2` |

**Wenn KEIN Session-Titel vorhanden:**

1. LIES `AGENTS.md`, `README.md`, `HANDOVER.md` der vorherigen Session
2. Extrahiere PROJEKT-Kurzname aus Repo-Identität
3. Wähle TYP basierend auf dominanter Aktivität (z.B. "BUNDLE_REPAIR" wenn Datei-Verschiebungen)
4. KURZTHEMA: prägnant (max. 3-5 Wörter)
5. Setze V1

## 4. Speicherorte für Session-Titel

**Schreibe Session-Titel an ALLEN dieser Stellen (HD-4 + Redundanz):**

1. `HANDOVER.md` — Header-Feld (YAML)
2. Report-Dateiname — `[KURZNAME]_V[N]_[REPORT-TYP].md` ODER mit Langtitel
3. Walkthrough-Eintrag — `## [DATUM] — [SESSION]_V[N]`
4. Commit-Message (falls Git) — Prefix
5. INSTRUCTIONS.md Referenz — bei Cross-References

## 5. Reports: Lange Namen vs. Kurze Dateinamen

**Dilemma:** Session-Titel sind lang und beschreibend. Report-Dateinamen sollten eher kurz sein (besser handhabbar).

**Lösung:** Reports tragen den **Langtitel im YAML-Header**, der **Dateiname kann kurz sein** — aber NUR wenn ein Such-Werkzeug existiert.

### 5.1 Mit Such-Werkzeug (gewünscht)

- **Dateiname:** `forensic_v1.md` (kurz)
- **YAML-Header:** `session_title: HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1`
- **Suche:** Tool durchsucht YAML-Header + Inhalt nach Session-Titel
- **Intelligenz:** case-insensitive, ignoriert `_`, `-`, Leerzeichen

### 5.2 Ohne Such-Werkzeug (Status quo)

- **Dateiname:** `[SESSION]_V[N]_[REPORT-TYP].md` (lang, aber eindeutig)
- **YAML-Header:** `session_title: [LANGNAME]_V[N]`
- **Suche:** nur über Dateinamen, kein Inhalts-Match
- **Nachteil:** Lange Dateinamen unhandlich

### 5.3 Empfehlung

**Aktuell:** Lange Dateinamen verwenden (Such-Werkzeug fehlt noch).

**Ziel:** Such-Werkzeug entwickeln (HTML-Tool, Windows-Popup, SubAgent-Auftrag). Details in `ideas_future_plans.md` und `implementation_plan.md`.

## 6. Beispiele (gültig vs. ungültig)

**Gültig:**
- `CDS_BUNDLE_REPAIR_V1` ✓
- `WEBAPP_AUTH_IMPL_V2` ✓
- `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1` ✓
- `DOCS_RESTRUCT_V3` ✓

**Ungültig (zu generisch):**
- `SESSION_1` ✗
- `WORK_V1` ✗
- `STUFF_V2` ✗

**Ungültig (zu lang):**
- `CDS_BUNDLE_KOMPAKT_SESSION_REPAIR_UND_REFACTORING_MIT_SUBAGENT_INTEGRATION_V1` ✗ (> 80 Zeichen, unhandlich)

**Faustregel:** ≤ 60 Zeichen, snake_case, keine Sonderzeichen außer `-`.

## 7. Verifikation mit User

**Bevor Titel final festgelegt wird, präsentiere User 2-3 Optionen:**

> "Ich schlage vor: `[VORSCHLAG_1]`. Alternative: `[VORSCHLAG_2]`. Welcher passt?"

**Default wenn User nicht antwortet:** Agent wählt + dokumentiert im Bericht.

## 8. Verbindung zu Konservierungs-Gesetzen

- **Gesetz 3 (BEWEISPFLICHT):** Session-Titel IST der Beweis, welche Session was gemacht hat. Ohne Titel = Arbeit nicht zuordenbar.
- **Gesetz 4 (INTEGRATION):** Titel muss in HANDOVER.md UND Report UND Walkthrough identisch sein, nicht drei verschiedene.
