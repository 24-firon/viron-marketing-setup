<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - DoD-Referenz für Session-Titel-Vergabe
> - Standard-Format `[PROJEKT]_[TYP]_[KURZTHEMA]_V[N]`
> - Edge-Case `-TO-` bei Themenwechsel
> - V1/V2-Logik für Folgesession
>
> - **Bundle-Verwendung:** Diese Datei wird NICHT in die Arbeitskopie kopiert — sie ist systemisch.
<!-- TEMPLATE-EXPLANATION-END -->

# EXAMPLE_SESSION_TITLE — Definition of Done

> **Zweck:** DoD-Referenz für Session-Titel-Vergabe. Agent vergleicht seinen Vorschlag mit diesen Beispielen.

---

## 1. Standard-Format

```
[PROJEKT]_[TYP]_[KURZTHEMA]_V[N]
```

**Beispiele (gültig):**

| Session-Titel | Bedeutung |
|:---|:---|
| `CDS_BUNDLE_REPAIR_V1` | Context-Dispatcher-System, Bundle-Reparatur, V1 |
| `WEBAPP_AUTH_IMPL_V1` | Web-App, Auth-Implementation, V1 |
| `DOCS_RESTRUCT_V3` | Docs-Restrukturierung, V3 (dritte Iteration) |
| `MOBILE_OFFLINE_MODE_V1` | Mobile-App, Offline-Mode, V1 |
| `BACKEND_REFACTORING_V2` | Backend, Refactoring, V2 |

## 2. Edge-Case: Themenwechsel innerhalb der Session

**Wenn sich das Thema drastisch geändert hat:**

```
[VORHER]_-TO-[NEU]_V[N]
```

**Beispiele:**

| Session-Titel | Bedeutung |
|:---|:---|
| `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1` | Startete als Handover-Bundle-Repair, wurde zu CDS-Skill-Generierung |
| `WEBAPP_AUTH_V1-TO-PERFORMANCE_TUNING_V1` | Startete als Auth, wechselte zu Performance |
| `CDS_RESTRUCTURING_V1-TO-CDS_RESTRUCTURING_V2` | Versionierung + Themenwechsel kombiniert |

**Faustregel:** `-TO-` nur verwenden, wenn das NEUE Thema mindestens 30% der Session ausgemacht hat.

## 3. V1/V2-Logik (Folgesession)

| Aktueller Titel | Folgesession-Titel |
|:---|:---|
| `CDS_BUNDLE_REPAIR_V1` | `CDS_BUNDLE_REPAIR_V2` |
| `WEBAPP_AUTH_IMPL_V3` | `WEBAPP_AUTH_IMPL_V4` |
| `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V1` | `HANDOVER_BUNDLE_REPAIR-TO-CDS_BUNDLE_SKILL_GEN_V2` |

**Wenn KEIN Titel vorhanden:** Leite aus Repo-Identität (AGENTS.md, README.md) ab.

## 4. Selbstprüfung

**Gültig wenn:**
- snake_case
- ≤ 60 Zeichen
- Keine Sonderzeichen außer `-`
- PROJEKT-Kurzname (max. 8 Zeichen)
- TYP beschreibt Aktivität (REFACTOR, IMPL, REPAIR, DOCS, etc.)
- KURZTHEMA prägnant (max. 3-5 Wörter)
- V[N] immer am Ende

**Ungültig wenn:**
- Mehr als 80 Zeichen
- CamelCase oder Leerzeichen
- Generische Namen (SESSION, WORK, STUFF)
- Mehrfache Versionen (V1V2, V1.5)

## 5. Verifikation mit User

**Bevor Titel final festgelegt wird, präsentiere User 2-3 Optionen:**

> "Ich schlage vor: `[VORSCHLAG_1]`. Alternative: `[VORSCHLAG_2]`. Welcher passt?"

**Default wenn User nicht antwortet:** Agent wählt + dokumentiert im Bericht.

## 6. Speicherorte (HD-4 + Redundanz)

1. `HANDOVER.md` — YAML-Header
2. Report-Dateiname — `[SESSION]_V[N]_[REPORT-TYP].md`
3. Walkthrough-Eintrag — `## [DATUM] — [SESSION]_V[N]`
4. Commit-Message (Git) — Prefix
5. INSTRUCTIONS.md Cross-References
