<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Eingebettetes Minimal-Bundle für Token-Knappheit oder Storage-Leerstand
> - Nicht der Standard — BACKUP wenn STORAGE nicht verfügbar ist
> - Enthält: P99_MINIMAL, HANDOVER_MINIMAL, REPORT_MINIMAL, CHECKLIST_MINIMAL
>
> - **Bundle-Verwendung:** Diese Datei wird NICHT in die Arbeitskopie kopiert — sie ist EINGEBETTET in den Skill.
<!-- TEMPLATE-EXPLANATION-END -->

# notfall/ — Eingebettetes Minimal-Bundle (Code Black)

> **Wann aktiv:** Token-Fenster 🔴/⚫ ODER STORAGE ist leer/leerst ODER User sagt "Mach einfach" / "Notfall" / "Black".
> **Zweck:** Standard-mäßige, mittelmäßige Vorlage als Backup, wenn das normale Bundle nicht verfügbar ist.
> **Inhalt:** 4-5 Minimal-Dateien, die JEDER Session-Architect sofort nutzen kann.

---

## README (diese Datei)

**Was ist das?**
Ein Backup-Bundle, das IMMER verfügbar ist — direkt im Skill, ohne STORAGE-Abhängigkeit. Nicht so krass reduziert wie ein "Notfall-2-Zeilen-Skelett", aber auch nicht so ausführlich wie das normale Bundle.

**Wann nutzen?**
- Token-Budget ist kritisch (< 30% Rest) → Beispiele in STORAGE sind zu teuer zum Laden
- STORAGE/TEMPLATES/ ist nicht verfügbar oder leer
- User möchte "einfach machen" ohne große Konfiguration
- Erste Hilfe bei einer kaputten Session-Struktur

**Was ist NICHT drin?**
- Keine echten Beispiele (zu platzraubend für Notfall)
- Keine Referenz-Dokumente (zu tief verschachtelt)
- Keine Cross-References zu STORAGE (nicht verfügbar)
- Keine SubAgent-Spawn-Logik (zu komplex für Notfall)

**Wofür ist es gut?**
- Schneller Start ohne Entscheidungs-Overhead
- Minimaler Token-Verbrauch
- Backup wenn alles andere fehlschlägt
- "Mittelmäßige" Qualität — kein Best-Practice, aber funktional

---

## P99_MINIMAL.md (Session-Trigger)

```markdown
# P99 NOTFALL — Session Abschluss

## 1. SCHREIBE BERICHT (kompakt, 5 Sektionen)

Speichere unter: `HANDOVER/TASK_[SESSION]_V[N]/report_minimal.md`

### Inhalt:
1. Was wurde gemacht (3-5 Bullets)
2. Geänderte Dateien (Liste)
3. Offene Probleme (1-2 Bullets)
4. Nächste Schritte (3 Bullets)
5. Datum + Session-Titel (Header)

## 2. FÜLLE HANDOVER (minimal, 5 Sektionen)

Speichere unter: `HANDOVER/TASK_[SESSION]_V[N]/HANDOVER.md`

### Inhalt:
1. BLUF (1 Satz)
2. Was wurde gemacht (3-5 Bullets)
3. Entscheidungen (1-3 Bullets)
4. Offene Tasks (3-5 Bullets)
5. Nächste Schritte (3 Bullets)

## 3. USER BESCHEID SAGEN

> "Session-Wechsel abgeschlossen. Handover unter [Pfad]. Bericht: [Pfad]. Nächste Session kann starten."

## Session-Titel
WENN vorhanden → nutze + V[N+1]
WENN nicht → V1 + beschreibender Name
```

---

## HANDOVER_MINIMAL.md (Datenübergabe-Vorlage)

```markdown
# HANDOVER (Minimal)

**Session:** [SESSION]_V[N]
**Datum:** [YYYY-MM-DD]

## 1. BLUF
[1 Satz: Was wurde erreicht?]

## 2. Was wurde gemacht
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

## 3. Entscheidungen
- [Entscheidung 1 — kurz]
- [Entscheidung 2 — kurz]

## 4. Offene Tasks
- [Task 1]
- [Task 2]
- [Task 3]

## 5. Nächste Schritte
1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]
```

---

## REPORT_MINIMAL.md (Bericht-Vorlage)

```markdown
# SESSION REPORT (Minimal)

**Session:** [SESSION]_V[N]
**Datum:** [YYYY-MM-DD]

## Was wurde gemacht
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

## Geänderte Dateien
- `[Pfad]` — [Was]

## Offene Probleme
- [Problem 1]
- [Problem 2]

## Nächste Schritte
- [Schritt 1]
- [Schritt 2]
- [Schritt 3]
```

---

## CHECKLIST_MINIMAL.md (Session-Ende-Check)

```markdown
# SESSION-ENDE-CHECKLIST (Notfall)

- [ ] Bericht geschrieben unter reports/
- [ ] HANDOVER.md geschrieben mit BLUF
- [ ] Offene Tasks dokumentiert
- [ ] Nächste Schritte konkret (nicht "weitermachen")
- [ ] Session-Titel in ALLEN Dateien konsistent
- [ ] User informiert mit Bestätigungs-Formel

→ Session sauber abgeschlossen. Workspace clean.
```

---

## Wichtiger Hinweis

Das notfall/-Bundle ist ein **BACKUP**, nicht der Standard. Im Normalfall immer die Templates aus `STORAGE/TEMPLATES/BUNDLE_KOMPAKT/` nutzen. Nur wenn diese nicht verfügbar sind (Token-Knappheit, Storage leer), auf `notfall/` zurückgreifen.
