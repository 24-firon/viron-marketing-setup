---
name: Skill-Philosophie & Workflow
description: Skills sind Router, nicht Archive. Phasenbasierte Navigation schützt das Kontext-Fenster.
trigger: always_on
scope: alle
repo: marketing-setup
---

# 80_skill_philosophy_and_workflow.md (Skills als Router)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Grundverständnis und korrekte Anwendung von Agent-Skills

## 1. Die Grundwahrheit: Router statt Archiv
Ein Skill ist kein Lehrbuch und kein statisches Archiv, sondern eine intelligente Navigations-Weiche (Router). Er sagt dir: *"Wenn du X tun willst, lies Datei Y"*, **DENN** das ungefilterte Laden von Inhalten (Templates, Examples) in den Haupt-Kontext führt zu sofortiger Rule-Fatigue und kognitiver Demenz bei komplexen Tasks.

## 2. Rules vs. Skills

| Aspekt | Rules | Skills |
|:--|:--|:--|
| **Ort** | `.opencode/rules/` | `.opencode/skills/` |
| **Laden** | Via `opencode.jsonc` → `instructions` (immer injiziert) | Via Description-Matching in `available_skills` |
| **Zweck** | Permanente Constraints, immer aktiv | Strukturierte Multi-Step-Workflows, on demand |
| **Struktur** | Einzelne `.md`-Datei mit YAML-Header | SKILL.md + Ordner (examples, templates, references) |
| **Token-Kosten** | Immer geladen → muss kompakt sein | Nur bei Trigger geladen → darf detailliert sein |

## 3. Die 3 Fehler die Agenten machen

| Falsch | Richtig |
|:--|:--|
| Alles in SKILL.md mergen | SKILL.md ist ein Router, Templates/Examples bleiben getrennt |
| Von oben nach unten lesen | Bedingungs-Matrix folgen, nur Nötiges laden |
| Examples ignorieren | Examples als "Definition of Done" behandeln |
| Ergebnis raten | Ergebnis mit Example vergleichen |
| "Fertig" sagen | "Mein Ergebnis erfüllt die Kriterien des Examples" |

## 4. Der korrekte Workflow (Phasen-Navigation)
Folge bei der Nutzung komplexer Skills ausnahmslos diesen Schritten:
1. **Initial-Scan:** Lies nur die ersten 10-20 Zeilen der `SKILL.md` (YAML-Header, Beschreibung). Brich sofort ab, wenn der Skill nicht zur Aufgabe passt.
2. **Matrix-Check:** Identifiziere deine aktuelle Phase in der Bedingungs-Matrix.
3. **Selektives Lesen:** Lies NUR die Dateien (Example/Template), die für deine aktuelle Phase geroutet sind.
4. **Verifizierung:** Vergleiche dein Zwischenergebnis mit dem geladenen Example, bevor du zur nächsten Phase in der Matrix springst.
**DENN:** Dieser phasenbasierte Ansatz schont das Kontext-Fenster und sichert die Einhaltung des Framework-Standards ohne blinden One-Shot-Bias.

## 5. Skill-Sequenzen

Wenn Skills in einer Sequenz aufeinander aufbauen (siehe SKILL_INDEX.md §8), gelten:
- **Starte mit dem ersten Skill der Kette**
- **Arbeite sequentiell** — nicht mehrere gleichzeitig laden
- **Nutze die Output-Dateien des vorherigen Skills als Input für den nächsten**

**Beispiel:** "Neuen Skill erstellen" = `skill-creator` → `skill-scanner` → `skill-constructor`. Nicht alle drei gleichzeitig laden, sondern nacheinander abarbeiten. Der `skill-scanner` braucht das Ergebnis des `skill-creator`, und der `skill-constructor` braucht das Ergebnis des `skill-scanner`.

**DENN:** Gleichzeitiges Laden aller Skills einer Sequenz verschwendet Token und verhindert, dass die Ergebnisse des einen Skills als Input für den nächsten dienen können.

## 🔗 Light Router
- **WELCHER Skill für WELCHEN Task** → `DOCS/SKILL_INDEX.md` (Decision Matrix mit Scan-Depth)
- **Vollständige Skill-Philosophie** → `STORAGE/skill-creation-knowledge.md`
- **Lesedisziplin** → `80_skill_routing_reading.md`
- **Skill-Anatomie** → `80_anatomy_of_complex_skill.md`
- **VIRON-spezifische Ergänzungen** → `80_skill_routing_viron.md`

