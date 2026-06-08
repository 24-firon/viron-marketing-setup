# 🎯 PROMPT: FORENSIC SESSION REPORT GENERATOR — UNIVERSAL HANDOFF PROTOCOL

**Zweck:**  
Dieser Prompt erzwingt am Ende einer Session einen forensischen, architektonisch fundierten, operativ brauchbaren Übergabebericht.  
Er ist universell einsetzbar für Coding-, Debugging-, DevOps-, Architektur-, Datenbank-, Frontend-, Backend-, Monorepo-, Security-, Research- und Read-only-Sessions.

Der Report dient nicht der Selbstdarstellung des Agenten, sondern der **sauberen Wissenskonservierung für den nächsten Operator**.

**Einsatz:**  
Am Ende jeder Session, bevor der Agent die Übergabe an den nächsten Operator macht. Kann auch bei bewusster Unterbrechung einer Session (z.B. Timeout, Kontextwechsel) ausgelöst werden.

**Ablage:**  
`./DESK/reports/Session-reports/[YYYY-MM-DD]_[PROJEKT]_[TYP]_[KURZTHEMA].md`

Diese Session heißt [SESSIONNAME]

**Version:** v1.0 (2026-05-30)

---

## SYSTEM-DOKTRIN OVERRIDE: SESSION REPORTING

Deine Aufgabe in dieser Session ist abgeschlossen oder wird an dieser Stelle bewusst unterbrochen.  
Bevor du die Übergabe machst, MUSST du einen **forensischen Session Report** erzeugen.

Du dokumentierst nicht einfach, **was** passiert ist, sondern vor allem:

- **welcher technische oder architektonische Konflikt vorlag,**
- **welche Entscheidungen tatsächlich getroffen wurden,**
- **welche Dateien / Pfade / Konfigurationen / Services betroffen sind,**
- **welche Dinge absichtlich NICHT verändert wurden,**
- **welche Risiken, Widersprüche oder offenen Fragen verbleiben,**
- **und was der nächste Agent exakt als Erstes tun sollte.**

---

## 1) BERICHTS-DOKTRIN

### A. Stil & Tonfall

- Kalt, präzise, architektonisch fundiert.
- Kein freundlicher Fülltext.
- Keine Floskeln wie „Gerne“, „Ich hoffe“, „Hier ist dein Bericht“, „Ich habe verstanden“.
- Keine Selbstdarstellung.
- Keine Marketing-Sprache.
- Knappheit ist erlaubt, aber **Unterdokumentation ist verboten**.
- Lieber zu ausführlich als zu knapp.
- Prosa ist erlaubt, aber nur dort, wo sie hilft, den **technischen Grund**, den **Kompromiss** oder den **Systemkonflikt** zu erklären.

### B. Faktentreue

- Trenne sauber zwischen:
  - **VERIFIZIERT** = direkt beobachtet, geändert, getestet oder aus der Session eindeutig belegt
  - **WAHRSCHEINLICH** = starke Indizien, aber nicht final bewiesen
  - **OFFEN** = ungeklärt, nicht getestet, nicht validiert
- Nichts erfinden.
- Keine impliziten Annahmen als Fakten verkaufen.
- Wenn etwas nicht geprüft wurde, schreibe explizit, dass es nicht geprüft wurde.

### C. Operative Nützlichkeit

Der Report muss so geschrieben sein, dass ein neuer Agent oder Engineer:

1. den Zustand schnell versteht,
2. die Gefahren erkennt,
3. die letzten Entscheidungen nachvollziehen kann,
4. ohne erneutes Chaos weiterarbeiten kann.

---

## 2) WAS ZWINGEND IN DEN REPORT MUSS

### A. Architektur-Konflikt

Beschreibe den zentralen Konflikt der Session in 1–3 dichten Absätzen:

- Was war kaputt, widersprüchlich oder riskant?
- Warum war das Problem nicht trivial?
- Welche Systemgrenzen oder Architekturentscheidungen waren betroffen?

### B. Operative Änderungen

Liste präzise auf:

- welche Dateien geändert wurden,
- welche Verzeichnisse betroffen waren,
- welche Konfigurationen geändert wurden,
- welche Services / Container / Ports / Rollen / Policies / Endpunkte betroffen waren,
- welche UI-/Dashboard-Einstellungen gesetzt wurden,
- welche Branches / Worktrees / Deploy-Kontexte relevant waren.

### C. Nicht-Änderungen

Dokumentiere ausdrücklich:

- was absichtlich **nicht** angefasst wurde,
- welche Daten, Tabellen, Services, Policies, Dateien oder Deployments bewusst verschont blieben,
- welche destruktiven Maßnahmen ausdrücklich vermieden wurden.

### D. Diagnostik & Beweise

Falls vorhanden:

- relevante Logs,
- Health-Zustände,
- Response-Verhalten,
- Testresultate,
- Browser-Verhalten,
- API-Checks,
- Netzwerk-/Port-Zustände,
- Container-Status,
- Policy-/Permission-Ergebnisse.

Keine langen Roh-Logs dumpen.  
Nur die technisch entscheidenden Befunde.

### E. Entscheidungsgründe

Zu jeder wesentlichen Maßnahme gehört das **Warum**:

- Warum wurde diese Änderung gemacht?
- Welcher architektonische Konflikt wurde dadurch entschärft?
- Welche Alternative wurde bewusst verworfen?
- Welche Folgekosten oder Kompromisse wurden akzeptiert?

### F. Risiken & Restschuld

Dokumentiere:

- bekannte technische Schulden,
- verbleibende Risiken,
- UI-/DX-Probleme,
- unklare Zustände,
- fragwürdige Workarounds,
- fragile Stellen,
- alles, was bei der nächsten Session leicht wieder kaputtgehen könnte.

### G. Nächste Schritte

Nicht allgemein, sondern konkret:

- Was ist der **nächste logische Schritt**?
- Welche Reihenfolge ist sinnvoll?
- Welche Bereiche dürfen erst bearbeitet werden, wenn eine Vorbedingung erfüllt ist?
- Welche Teile sind blockiert?
- Welche Prüfungen müssen vor dem Weitermachen durchgeführt werden?

---

## 3) WAS AUSDRÜCKLICH DRAUSSEN BLEIBT

- Keine Roh-Code-Dumps.
- Keine unnötigen Standarderklärungen zu bekannten Tools oder Frameworks.
- Keine Entschuldigungen.
- Keine motivationalen Abschlusssätze.
- Keine Wiederholung derselben Information in 3 Varianten.
- Keine Behauptungen ohne Statuskennzeichnung.
- Keine vagen Aussagen wie „einige Dinge wurden verbessert“.
- Keine „Best Practices“-Predigten ohne Bezug zur konkreten Session.

---

## 4) AUSGABE-MODUS

Wenn Schreibzugriff vorhanden ist:

- speichere den Report unter dem unter **Ablage** definierten Pfad.
- Wenn kein Pfad vorgegeben wurde, schlage einen sinnvollen Pfad vor und gib den Report trotzdem vollständig aus.

Wenn kein Schreibzugriff vorhanden ist:

- gib den vollständigen Report im Chat aus.
- erwähne nicht lang, dass dir Schreibrechte fehlen. Ein kurzer Hinweis reicht.

---

## 5) VOLLSTÄNDIGKEITSREGEL

Der Report darf **nicht kurz** sein, wenn die Session komplex war.  
Wenn mehrere Systeme berührt wurden (z. B. Docker + DB + Frontend + Auth + CMS + Monorepo), dann muss der Bericht entsprechend ausführlich sein.

**Faustregel:**

- Kleine Session: kompakt, aber vollständig
- Mittlere Session: detailliert
- Komplexe Session: sehr ausführlich, mit klarer Trennung der Themenblöcke

Im Zweifel gilt: **Überdokumentation vor Unterdokumentation.**

---

## 6) GENERIERUNGSAUFTRAG

Generiere jetzt einen forensischen Session Report nach folgendem Markdown-Schema. Speichere ihn unter dem unter **Ablage** definierten Pfad ab. Falls kein Schreibzugriff besteht, gib ihn hier komplett aus.

```markdown
# 📄 SESSION REPORT: [Titel der Session]

**Datum:** [YYYY-MM-DD]  
**Projekt/Repo:** [Name oder Kontext]  
**Scope:** [z. B. Backend, Frontend, Auth, DB, DevOps, Research, Monorepo, CMS, Video, Security]  
**Session-Modus:** [Execution / Read-Only / Research / Debug / Advisory / Mixed]

***

## 1. SYSTEMLAGE

Beschreibe in 1–3 dichten Absätzen die tatsächliche Ausgangslage dieser Session.  
Kein Gelaber. Nur die operative Realität:
- Was war der Zustand?
- Was war kaputt, unklar oder gefährlich?
- Warum war die Lage architektonisch relevant?

***

## 2. ARCHITEKTUR-ENTSCHEIDUNGEN & REPARATUREN

Beschreibe die Kernentscheidungen dieser Session in operativ verwertbarer Form.

- **[Thema / Konflikt]:** [Harter Fakt, Änderung, Port, Pfad, Policy, UI-Setting, Verhalten]  
  *Warum:* [Architekturgrund / technischer Konflikt / verworfene Alternative]

- **[Thema / Konflikt]:** [Harter Fakt]  
  *Warum:* [Begründung]

- **[Thema / Konflikt]:** [Harter Fakt]  
  *Warum:* [Begründung]

Falls keine Änderungen durchgeführt wurden, dokumentiere stattdessen die validierten Erkenntnisse und warum bewusst nicht eingegriffen wurde.

***

## 3. DATEIEN, PFADE & KONFIGURATIONEN

Nur harte Fakten. Keine Codeblöcke.

### Geändert
- `[Pfad/Datei]` — [Was wurde geändert?]
- `[Pfad/Datei]` — [Was wurde geändert?]

### Neu angelegt
- `[Pfad/Datei]` — [Zweck]

### Verschoben / Umbenannt / Archiviert
- `[Altpfad]` -> `[Neupfad]` — [Grund]

### Nicht verändert
- `[Pfad/Datei/Systembereich]` — [Warum bewusst nicht angefasst]

### Relevante Konfigurationen / Zustände
- `[Variable / Setting / Policy / Port / Endpoint / Branch / Container / Rolle]` — [Aktueller Zustand]
- `[Variable / Setting / Policy / Port / Endpoint / Branch / Container / Rolle]` — [Aktueller Zustand]

***

## 4. DIAGNOSTIK, TESTS & BEWEISLAGE

Dokumentiere die relevanten Beobachtungen der Session.

- **Verifiziert:** [Beobachtung / Test / Log-Befund / HTTP-Verhalten / UI-Zustand]
- **Verifiziert:** [Beobachtung]
- **Wahrscheinlich:** [Starker Verdacht, aber nicht final bewiesen]
- **Offen:** [Nicht geprüft / nicht validiert / widersprüchlich]

Wenn eine frühere Annahme korrigiert wurde, dokumentiere das explizit:
- **Korrigierte Fehleinschätzung:** [Was wurde zunächst angenommen, was stellte sich als richtig heraus?]

***

## 5. REPOSITORY-HYGIENE & OPERATIVE ORDNUNG

Beschreibe, ob diese Session das Repo/systemisch sauberer oder fragiler gemacht hat.

- Welche Altlasten wurden reduziert?
- Welche temporären Workarounds existieren noch?
- Gibt es doppelte Zustände, Ghost-Dateien, versteckte Konfigurationsquellen, manuelle UI-Abhängigkeiten oder andere kognitive Fallen?

***

## 6. RISIKEN, TECHNICAL DEBT & SYSTEMISCHE BRUCHSTELLEN

Liste die Risiken ohne Beschönigung.

- **[Risiko]:** [Beschreibung]
  *Auswirkung:* [Was kann kaputtgehen?]
  *Wahrscheinlichkeit:* [Niedrig / Mittel / Hoch]
  *Empfohlene Absicherung:* [Was sollte als Nächstes passieren?]

- **[Risiko]:** [Beschreibung]
  *Auswirkung:* [...]
  *Wahrscheinlichkeit:* [...]
  *Empfohlene Absicherung:* [...]

***

## 7. RESEARCH, EINORDNUNG & KORREKTUR VON DENKFEHLERN

Dieser Abschnitt ist Pflicht, wenn die Session Research, externe Doku, Reports oder ältere Agentenannahmen berührt hat.

- Welche vorherigen Annahmen waren korrekt?
- Welche waren falsch oder veraltet?
- Welche Dokumentation / welcher Bericht war hilfreich?
- Welche „Best Practice“ erwies sich im konkreten Setup als irreführend?
- Welche Architekturwahrheit gilt jetzt stattdessen?

***

## 8. HANDOVER FÜR DEN NÄCHSTEN AGENTEN

Schreibe diesen Abschnitt so, dass der nächste Agent ohne erneute Eskalation ansetzen kann.

### Aktueller belastbarer Zustand
- [Was funktioniert sicher?]
- [Was ist nur teilweise abgesichert?]
- [Was ist ungeklärt?]

### Verbotene oder riskante Aktionen
- [Was darf der nächste Agent auf keinen Fall blind tun?]
- [Welche destruktiven Schritte sind tabu?]

### Nächste logische Schritte
1. [Erster konkreter Schritt]
2. [Zweiter konkreter Schritt]
3. [Dritter konkreter Schritt]

### Falls sofort weitergearbeitet wird
- [Welche Datei / welcher Service / welcher Screen / welcher Befehl ist der sinnvollste Einstiegspunkt?]

***

## 9. KURZFAZIT IN EINEM SATZ

[Ein einziger dichter Satz, der den Zustand der Session präzise auf den Punkt bringt.]

***

**[FORENSIC SESSION REPORT ERSTELLT]**
```

---

## 7) ZUSATZREGEL FÜR STARKE AGENTEN

Wenn die Session komplex war, füge stillschweigend zusätzliche Unterpunkte hinzu, anstatt Informationen wegzulassen.  
Struktur darf erweitert, aber nicht verwässert werden.

Wenn der Session-Kontext mehrere Domänen umfasst (z. B. Frontend + Backend + CMS + Auth + DevOps), dann trenne diese Domänen sauber innerhalb des Berichts.

Wenn während der Session kein Code geschrieben wurde, sondern nur analysiert, validiert oder geplant wurde, ist das **kein Grund für einen kurzen Report**. Dann muss der Schwerpunkt auf:

- Architektur,
- Beweislage,
- Risiken,
- Entscheidungslogik,
- und Handover-Klarheit liegen.

**Tiefenregel:**  
Wenn mehrere Systeme berührt wurden oder die Session eine Reparatur, Architekturentscheidung, Migration, Debugging-Eskalation oder Sicherheitsfrage beinhaltete, dann ist ein oberflächlicher Report unzulässig. Dokumentiere lieber zu viel als zu wenig.

---

## 8) AUSFÜHRUNG

Generiere den Report jetzt.
