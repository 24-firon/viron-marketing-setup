<!-- TEMPLATE-EXPLANATION-START -->
> **Was in dieser Datei steht:**
>
> - Ausgefülltes Protokoll-Beispiel eines SubAgent-Auftrags
> - 6-Sektionen-Struktur gemäß REPORT-ZWANG aus SUBAGENT_PROMPT.md
> - Registriert den Output eines SubAgents als DoD-Referenz
>
> - **Bundle-Verwendung:** Dient als "Definition of Done" für SubAgent-Reports.
<!-- TEMPLATE-EXPLANATION-END -->

# EXAMPLE_SUBAGENT_REPORT — Definition of Done

> **Zweck:** DoD-Referenz für ausgefüllte SubAgent-Protokolle. Ein SubAgent-Abschlussbericht muss diese Struktur haben — inhaltlich, nicht nur formal.
> **Wann lesen:** Vor einem SubAgent-Spawn, damit du weißt was du erwarten darfst.

---

```markdown
# PROTOKOLL — REGISTRY_SYNC_01

## 1. Was wurde gemacht

- Registry `src/rules/00_rule_registry.md` gelesen (17 Boot-Regeln)
- `REPORTS/SRC-ANALYSE.md` gelesen (82 Dateien in `src/rules/`)
- Vergleich durchgeführt: 82 Dateien minus 17 registrierte = 65 fehlende
- 65 fehlende Einträge in die Registry eingefügt
- Duplikate und krumme Nummern geprüft (0 gefunden)

## 2. Was wurde NICHT gemacht

- Nicht geprüft ob alle 82 Dateien wirklich gültige Regel-YAML-Header haben
- Keine `.opencode/`-Dateien angetastet (tabu)

## 3. Evidence (härtester Beweis)

Letzte 5 Zeilen Tool-Output des Registry-Updates:
```
CRITICAL (82/82): 17 existent + 65 neu = 82 total.
Archiv: _ARCHIVE/REGISTRY_SYNC_01/00_rule_registry.md_backup
Keine Konflikte. Keine krummen Nummern.
Ergebnis: src/rules/00_rule_registry.md aktualisiert.
```

## 4. Geänderte Dateien

- `src/rules/00_rule_registry.md` — 65 Einträge ergänzt (von 17 auf 82)
- `_ARCHIVE/REGISTRY_SYNC_01/00_rule_registry.md_backup` — Original vor Änderung

## 5. Offene Punkte

- 1 Warnung in SRC-ANALYSE.md: Datei `99_deprecated.md` existiert, aber ohne gültigen YAML-Header → nicht registriert

## 6. Nächste Schritte (Empfehlung)

1. `00_rule_registry.md` auf alphabetische Sortierung prüfen
2. YAML-Header in `99_deprecated.md` reparieren oder Datei archivieren
3. SubAgent-Abschluss bestätigen und Ergebnis in Hauptsession integrieren
```

---

## DoD-Kriterien (Selbstprüfung)

Bevor du einen SubAgent-Abschluss akzeptierst, prüfe:

- [ ] Alle 6 Sektionen vorhanden (Was, Nicht, Evidence, Geändert, Offen, Nächste)
- [ ] Evidence-Sektion enthält Terminal-Output (letzte 3-5 Zeilen), keine leeren Behauptungen
- [ ] Geänderte Dateien mit Pfad + Beschreibung
- [ ] Offene Punkte sind ehrlich (kein "nichts")
- [ ] Nächste Schritte sind konkret (nicht "weitermachen")
