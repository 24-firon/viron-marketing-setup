# 80_skill_construction_law.md (Die 4-Pfeiler-Formel)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Erstellung und Refactoring von Agent-Skills

## 1. Die Struktur-Anforderung (Skill als Router)
Ein Skill ist kein passives Textbuch, er ist ein Token-sparender Router. Lade Informationen niemals direkt in die `SKILL.md`, wenn sie in Payloads oder Templates ausgelagert werden können, **DENN** überladene Skill-Dateien verursachen sofortige Rule-Fatigue und blockieren das Kontext-Fenster für die eigentliche Implementierung.

**Der zwingende Aufbau:**
1. **YAML-Header:** Kurz-Info zu Name, Zielgruppe, Lizenz.
2. **Context-Block:** Definition des "Wann" (Match-Check innerhalb der ersten 30 Zeilen).
3. **Bedingungs-Matrix:** Tabelle mit harten Konditionen: *WENN [Phase/Task] ➔ LIES [Datei]*.
4. **Sub-Action Prompts:** (Optional) Copy-Paste-Befehle für den User zur Skill-Auslösung.

## 2. Die 4-Pfeiler-Formel (Qualitätssicherung)
Erschaffe niemals einen Skill ohne diese vier Säulen, **DENN** das Fehlen physischer Referenzen zwingt nachfolgende Agenten zum Raten und zerstört die Reproduzierbarkeit der Output-Qualität im Viron-Netzwerk.

| Pfeiler | Zweck | Implementierung |
| :--- | :--- | :--- |
| **1. Examples** | Die "Definition of Done". | `examples/` Ordner mit fertigen Artefakten. |
| **2. Templates** | Das Scaffolding (Formatierung). | `templates/` Ordner mit exakten Markdown/JSON-Strukturen. |
| **3. Rollenzuweisung** | Mindset-Steuerung. | Im Context-Block definiert (z.B. Forensiker). |
| **4. Harte Ansagen** | Verhindert Raten. | Im Router: "Lese Datei Z, wenn du Aktion A ausführst." |

## 🔗 Light Router (Deep Knowledge)
- **WENN** du einen neuen Skill bauen musst ➔ **LIES** `80_skill_creation_checklist.md` (aktive Boot-Regel).
- **WENN** du die detaillierte Skill-Anatomie benötigst ➔ **LIES** `80_anatomy_of_complex_skill.md`.
