# TASK ENVELOPE (Kompakt)

> 4-Säulen-Briefing für einen Sub-Agent. **DENN** ohne Briefing agiert der Sub-Agent blind, greift Tabu-Dateien an, und vernichtet Daten.

## DIE 4 SÄULEN (was JEDER Sub-Agent-Prompt enthalten MUSS)

| Säule | Was sie ist |
|:---|:---|
| **A) MISSION** | Das "Warum" — warum gibt es diese Aufgabe? Was passiert wenn sie nicht erledigt wird? |
| **B) CONTEXT** | Welche Dateien MUSS der Sub-Agent lesen? |
| **C) SCOPE** | Was darf er anfassen, was ist Tabu? |
| **D) ATOMARE SCHRITTE** | Exakte Schritt-für-Schritt-Anleitung mit Tool-Calls |

**Was passiert wenn du nur Säule A schickst?** Der Sub-Agent weiß WAS er tun soll, aber nicht WIE und DARF WAS. Ergebnis: Wildes Raten und Datenvernichtung.

## PROMPT_INITIAL VORLAGE

```markdown
# TASK: [TASK-ID] — [Kurzer Titel]

## A) MISSION (Warum?)
[Was passiert wenn diese Aufgabe nicht erledigt wird? 1-2 Sätze]
Beispiel: "Registry ist 80 Dateien hinter dem physikalischen Bestand. 
Sub-Agent muss die fehlenden Einträge ergänzen, sonst driften künftige 
Agenten in die falsche Richtung."

## B) CONTEXT (Was lesen?)
- `[Pfad 1]` — [Was steht da, z.B. "Aktuelle Registry-Einträge"]
- `[Pfad 2]` — [Was steht da, z.B. "Scan-Befund vom letzten Audit"]

## C) SCOPE (Was darf er?)

✅ **Darf:**
- `[Pfad/erlaubt]`
- `[Pfad/erlaubt]`

❌ **Tabu (NIEMALS anfassen):**
- `[Pfad/verboten]`
- `[Pfad/verboten]`

## D) ATOMARE SCHRITTE (Wie genau?)

1. [Schritt 1 — exakter Befehl/Tool-Call, z.B. "Lies src/rules/00_rule_registry.md"]
2. [Schritt 2 — exakter Befehl, z.B. "Vergleiche mit REPORTS/SRC-ANALYSE.md"]
3. [Schritt 3 — exakter Befehl]
4. [Schritt 4 — exakter Befehl]

## REPORT-ZWANG (EXAKTE VORGABE)

Du MUSST ein Protokoll deiner Arbeit als strukturierte Markdown-Datei ablegen:

**Ablage:** `DESK/reports/[TASK-ID]_[DATUM].md`

**EXAKTE Struktur (jede Sektion ist Pflicht):**

```markdown
# PROTOKOLL — [TASK-ID]

## 1. Was wurde gemacht
- [Bullet 1: Konkrete Aktion + Ergebnis]
- [Bullet 2: Konkrete Aktion + Ergebnis]

## 2. Was wurde NICHT gemacht
- [Grund, warum bestimmte Schritte nicht ausgeführt wurden]

## 3. Evidence (härtester Beweis)
Letzte 3-5 Zeilen Output:
```
[Terminal-Output / Tool-Output hier]
```

## 4. Geänderte Dateien
- `[Pfad]` — [Was wurde geändert/erstellt]

## 5. Offene Punkte
- [Was ist unklar, blockiert oder fehlgeschlagen]

## 6. Nächste Schritte (Empfehlung)
- [Schritt 1]
```

**WENN kein Schreibzugriff:** Gib das Protokoll im Chat aus in exakt dieser Struktur. KEINE Ausreden.

## STOPP-PUNKTE
| Stopp | Nach Schritt | Aktion |
|:---|:---|:---|
| Stopp 1 | Schritt 2 | Berichte Ergebnis, zeige Evidence (letzte 5 Zeilen) |
| Final | Schritt 4 | Berichte Abschluss + Protokoll-Pfad |

Nach jedem Stopp: **Warte auf explizites "GO" vom Director.**
```

## BEISPIEL: TASK_ENVELOPE FÜR REGISTRY-SYNC

```markdown
# TASK: REGISTRY_SYNC_01 — Registry mit physischem Bestand abgleichen

## A) MISSION
Die RULE_REGISTRY.md listet 17 Boot-Regeln, aber src/rules/ enthält 
82 Dateien. Die Registry ist de-synchronisiert und führt nachfolgende 
Agenten in die Irre. Der Sub-Agent muss die 82 Dateien scannen, 
die 17 Einträge prüfen, fehlende Einträge ergänzen.

## B) CONTEXT
- `src/rules/00_rule_registry.md` — aktuelle (unvollständige) Registry
- `REPORTS/SRC-ANALYSE.md` — Scan-Befund vom letzten Audit

## C) SCOPE
✅ Darf: `src/rules/00_rule_registry.md` bearbeiten
❌ Tabu: `DOCS/`, `.opencode/`, andere Dateien löschen/verschieben

## D) ATOMARE SCHRITTE
1. Lies `src/rules/00_rule_registry.md` (aktuelle 17 Einträge)
2. Lies `REPORTS/SRC-ANALYSE.md` (82 gefundene Dateien)
3. Vergleiche: Welche Dateien fehlen in der Registry?
4. Ergänze die fehlenden Einträge in `00_rule_registry.md`
5. Prüfe auf Duplikate und krumme Zahlen (11_, 12_, 85_)

## REPORT-ZWANG
`DESK/reports/REGISTRY_SYNC_01_[DATUM].md`
```

## WAS PASSIERT WENN DER SUB-AGENT DAS ENVELOPE IGNORIERT?

- Er greift Dateien an die Tabu sind
- Er liest nicht die Context-Dateien
- Er macht keine STOPP-Punkte
- Er schreibt keinen Report
- Ergebnis: Datenvernichtung und unstrukturierte Arbeit
