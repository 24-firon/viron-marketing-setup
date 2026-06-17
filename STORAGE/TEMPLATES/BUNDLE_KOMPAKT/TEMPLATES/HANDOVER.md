# HANDOVER — Datenübergabe (Kompakt)

> **Reine Datenübergabe** an den nächsten Session-Agent. Keine Fragen, keine Verifikation. **DENN** diese Datei ist der „Erste Hilfe"-Koffer für den Nachfolger.

## 1. BLUF (Bottom Line Up Front)

> [Ein dichter Satz: Was wurde in dieser Session erreicht?]
> Beispiel: "Phase A (Read-only Scan) abgeschlossen, 47 Top-Level-Verzeichnisse dokumentiert. Phase B (FOLDER.md anlegen) noch offen."

## 2. PROJEKT-SPEZIFISCHE DATEN

Was NIERGENDS anders im Repo steht und der nächste Agent explizit braucht:

| Schlüssel | Wert | Warum wichtig |
|:---|:---|:---|
| `[z.B. Branch]` | `[z.B. feat/cds-and-graph]` | `[Welcher HEAD aktiv]` |
| `[z.B. Server-IP]` | `[z.B. 195.201.36.240]` | `[SSH-Zugang, Hetzner]` |
| `[z.B. Port]` | `[z.B. 3012]` | `[Next.js Dev-Server]` |
| `[z.B. Env-Var]` | `[z.B. OPENCODE_GO_KEY]` | `[API-Key-Quelle]` |

## 3. ERLEDIGTE ARBEIT

| Was | Status | Wann |
|:---|:---:|:---|
| `[Aufgabe 1]` | ✅ | `[Datum]` |
| `[Aufgabe 2]` | ✅ | `[Datum]` |

## 4. ENTSCHEIDUNGEN

| Entscheidung | Warum | Reversibel? |
|:---|:---|:---:|
| `[z.B. Inkrementelles Graph-Update]` | `[Bestehende 1075 Nodes sind wertvoll]` | Ja |
| `[z.B. vis-network nicht patchen]` | `[Pro-Aufruf statt Library-global]` | Ja |

## 5. OFFENE TASKS

| Task | Priorität | Was zu tun |
|:---|:---:|:---|
| `[Task]` | P0 🔴 | `[Konkret was noch fehlt]` |
| `[Task]` | P1 🟡 | `[Konkret was noch fehlt]` |

## 6. BEKANNTE PROBLEME & WORKAROUNDS

| Problem | Workaround | Fix geplant? |
|:---|:---|:---:|
| `[z.B. Port 5432 öffentlich]` | `[ssh-tunnel statt direkter Connect]` | Ja |
| `[z.B. SESSION-RITUAL fehlt 5. Säule]` | `[Manuell bestätigen]` | Nein |

## 7. NÄCHSTE SCHRITTE (Konkret)

1. **[Schritt 1]** — [Konkrete Aktion, z.B. "FOLDER.md für apps/web anlegen"]
2. **[Schritt 2]** — [Konkrete Aktion]
3. **[Schritt 3]** — [Konkrete Aktion]

---

> **Handover abgeschlossen.** Warte auf nächsten Operator-Auftrag.

**WICHTIG:** KEINE FRAGEN IN HANDOVER. Fragen gehören in `P00_BOOTSTRAP.md` Section „7 FRAGEN".
