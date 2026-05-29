---
name: Skill Routing — Lesedisziplin & Token-Schutz
description: Konditionales Lazy-Loading von Skills. Scan-Depth pro Skill steht in SKILL_INDEX.md — exakt befolgen.
trigger: always_on
scope: alle
repo: marketing-setup
---

# 80_skill_routing_reading.md (Token-Schutz & Lesedisziplin)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Ressourcenschonende Verarbeitung komplexer Anweisungen

## 1. Erstes Lesen: EINSCHÄTZEN, nicht SPRINGEN

Beim Betreten einer Skill-Datei liest du zuerst:
1. **YAML-Header** (name, description, trigger) — 5-10 Zeilen
2. **Erste Beschreibung/Inhaltsverzeichnis** — 10-20 Zeilen

Das dient zum EINSCHÄTZEN: Was ist das? Wofür ist es? Wann brauche ich es?

**Dann entscheidest du anhand von Größe UND Struktur:**
- **Komplett lesen** — wenn der Großteil des Werts IN der SKILL.md steht (z.B. `find-bugs` mit 75 Zeilen: alles drin, 5 Phasen strukturiert; oder `cro` mit 187 Zeilen: fast alles in SKILL.md, nur 2 Referenz-Dateien)
- **YAML + Kern-Sektion** — wenn viel Payload in `references/` oder `examples/` ausgelagert ist (z.B. `security-review`: YAML + Scope + Confidence Levels, dann gezielt nach OWASP-Kategorie aus `references/`)
- **YAML + gezielt** — wenn der Skill sehr groß ist und nur spezifische Sektionen relevant sind (z.B. `multi-agent-orchestration`: YAML + Quick Start + Architecture Overview, Rest nur bei Bedarf)
- **Nur bei Bedarf** — wenn der Skill nur selten gebraucht wird und nicht präventiv geladen werden soll

**NICHT die Zeilenanzahl allein entscheidet**, sondern die Struktur: Wo steckt der Wert? Ist alles in SKILL.md oder ist es auf references/ verteilt? Welche Sektion brauche ich für meine aktuelle Aufgabe?

**NIEMALS** blind in Zeile 25 oder 50 springen. Jeder Skill hat eine andere Struktur — lies zuerst die Sektionsübersicht im SKILL_INDEX.md.

## 2. Scan-Depth pro Skill

Die konkrete Lesetiefe steht in `DOCS/SKILL_INDEX.md` — Scan-Depth-Spalte. Dort ist pro Skill genau festgelegt, welche Zeilen und Referenz-Dateien geladen werden müssen. **Nicht pauschal 30 Zeilen oder 30%.** Jeder Skill hat eine andere Struktur — `find-bugs` (150 Zeilen) wird anders gelesen als `multi-agent-orchestration` (579 Zeilen).

## 3. Konditionales Lazy-Loading

Öffne referenzierte Payloads, `references/` oder `templates/` ausschließlich dann, wenn die Bedingung der Routing-Matrix erfüllt ist. Widerstehe dem Impuls, ganze Skill-Verzeichnisse präventiv zu laden, **DENN** Lazy-Loading hält dein Kurzzeitgedächtnis frei für logische Operationen und verhindert den Absturz durch Kontext-Überladung.

## 4. Verankerung im Gold-Standard

Lade bei einem Routing-Treffer zwingend das zugehörige Example via `read` Tool, BEVOR du eigenen Code oder Text generierst, **DENN** diese physische Verankerung im "Gold Standard" des Frameworks garantiert eine fehlerfreie Umsetzung im ersten Versuch.

## 5. Sequenzen beachten

Wenn Skills in einer Sequenz aufeinander aufbauen (siehe SKILL_INDEX.md §8), starte mit dem ersten Skill der Kette. Lade nicht mehrere Skills gleichzeitig — arbeite sequentiell und nutze die Output-Dateien des vorherigen Skills als Input für den nächsten.

## 🔗 Light Router
- **WELCHER Skill für WELCHEN Task** → `DOCS/SKILL_INDEX.md` (Decision Matrix mit Scan-Depth)
- **WIE man Skills liest** → `80_skill_routing_reading.md` (diese Datei)
- **Skill-Philosophie** → `80_skill_philosophy_and_workflow.md`
- **Conflict Resolution** → `71_skill_routing.md`
- **VIRON-spezifische Ergänzungen** → `80_skill_routing_viron.md`

