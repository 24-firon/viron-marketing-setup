---
name: Skill-Erstellung — 4-Pfeiler-Formel
description: Erstellung und Refactoring von Agent-Skills. Struktur-Anforderung und Qualitätssicherung.
trigger: always_on
scope: alle
repo: marketing-setup
---

# 80_skill_construction_law.md (Die 4-Pfeiler-Formel)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Erstellung und Refactoring von Agent-Skills

## 1. Die Struktur-Anforderung (Skill als Router)

Ein Skill ist kein passives Textbuch, er ist ein Token-sparender Router. Lade Informationen niemals direkt in die `SKILL.md`, wenn sie in Payloads oder Templates ausgelagert werden können, **DENN** überladene Skill-Dateien verursachen sofortige Rule-Fatigue und blockieren das Kontext-Fenster für die eigentliche Implementierung.

**Der zwingende Aufbau:**
1. **YAML-Header:** `name` + `description` (Pflicht). Keine anderen Felder.
2. **Context-Block:** Definition des "Wann" (Match-Check innerhalb der ersten 10-20 Zeilen).
3. **Bedingungs-Matrix:** Tabelle mit harten Konditionen: *WENN [Phase/Task] ➔ LIES [Datei]*.
4. **Sub-Action Prompts:** (Optional) Copy-Paste-Befehle für den User zur Skill-Auslösung.

## 2. Die 4-Pfeiler-Formel (Qualitätssicherung)

Erschaffe niemals einen Skill ohne diese vier Säulen, **DENN** das Fehlen physischer Referenzen zwingt nachfolgende Agenten zum Raten und zerstört die Reproduzierbarkeit der Output-Qualität.

| Pfeiler | Zweck | Implementierung |
|:--|:--|:--|
| **1. Examples** | Die "Definition of Done". | `examples/` Ordner mit fertigen Artefakten. |
| **2. Templates** | Das Scaffolding (Formatierung). | `templates/` Ordner mit exakten Markdown/JSON-Strukturen. |
| **3. Rollenzuweisung** | Mindset-Steuerung. | Im Context-Block definiert (z.B. Forensiker). |
| **4. Harte Ansagen** | Verhindert Raten. | Im Router: "Lese Datei Z, wenn du Aktion A ausführst." |

**Eiserne Regel:** Wenn du einen Skill erstellst und den `examples/`-Ordner vergisst, hast du komplett versagt.

## 3. Verbotene YAML-Felder

| Verboten | Warum |
|:--|:--|
| `first_read` | Jedes System parsed YAML anders. OpenCode ignoriert es, Claude Code crasht. |
| `read_lines` | Siehe oben. Nur `name` und `description` sind erlaubt. |
| `toC_line` | Siehe oben. |

**Die Description ist der einzige Trigger.** Claude Code/OpenCode zeigt dem Agenten `available_skills` mit name + description. Der Agent entscheidet anhand der Description ob er den Skill lädt. Sei also spezifisch bezüglich Trigger-Kontexten.

## 4. Vendor-Skills patchen

Vendor-Skills (von `npx skills`) werden regelmäßig aktualisiert. Wenn du sie lokal patchst, gehen deine Patches beim nächsten Update verloren.

**Die Lösung — STORAGE-Separation:**
- Vendor-Skills bleiben unverändert (update-safe)
- Proprietäres Wissen lebt in `STORAGE/` oder wird über den `references/`-Ordner des Skills referenziert
- Der Skill routet bei Bedarf auf Storage-Wissen

**Beispiel:** Der `skill-creator` Skill bleibt wie er ist. Das Dispatcher-spezifische Wissen über Regel-Formulierung, Präfix-Systeme und YAML-Standards lebt in `STORAGE/skill-creation-knowledge.md`.

## 5. Scan-Depth definieren

Jeder neue Skill muss in `DOCS/SKILL_INDEX.md` eingetragen werden mit:
- **Zeilen** — Gesamtzahl Zeilen der SKILL.md
- **Refs** — Anzahl Referenz-Dateien
- **Scan-Depth** — Exakte Zeilenangabe welche Sektionen gelesen werden müssen

**DENN:** Ohne Scan-Definition lädt der nächste Agent blind und verschwendet Tokens.

## 🔗 Light Router
- **Scan-Depth pro Skill** → `DOCS/SKILL_INDEX.md`
- **Skill-Anatomie** → `80_anatomy_of_complex_skill.md`
- **Vollständiges Skill-Wissen** → `STORAGE/skill-creation-knowledge.md`
- **VIRON-spezifische Ergänzungen** → `80_skill_routing_viron.md`
