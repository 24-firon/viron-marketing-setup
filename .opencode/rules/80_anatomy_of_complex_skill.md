---
name: Anatomie komplexer Skills
description: Strukturanalyse & Navigation. Komplexe vs. simple Skills unterscheiden.
trigger: always_on
scope: alle
repo: marketing-setup
---

# 80_anatomy_of_complex_skill.md (Strukturanalyse & Navigation)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Handhabung und Verständnis von Agent-Skills

## 1. Realitäts-Check: Komplex vs. Simpel

Prüfe vor der Nutzung, ob ein Skill eine komplexe Struktur (Ordner mit `references/`, `templates/`, `examples/`) oder eine simple Struktur (nur eine `SKILL.md`) aufweist. Behandle einfache Skills als monolithische Anweisung, **DENN** eine unnötige Suche nach Routern in simplen Skills verschwendet Token und Zeit.

## 2. Die Anatomie komplexer Skills

Lade bei komplexen Skills niemals den gesamten Inhalt blind. Nutze die `SKILL.md` als Router, **DENN** das ungefilterte Laden von Templates und Examples flutet das Kontext-Fenster mit irrelevantem Rauschen und provoziert Rule-Fatigue.

**Die Struktur (bei komplexen Skills):**
```
.agents/skills/<skill-name>/
├── SKILL.md                    ← DER ROUTER
├── examples/                   ← "Definition of Done" Referenzen
├── templates/                  ← Scaffolding (Vorlagen)
├── references/                 ← Referenz-Dokumente, Guides
└── scripts/                    ← Automatisierung
```

## 3. Der Navigations-Workflow

Folge bei komplexen Skills strikt diesem Pfad:

1. **SKILL_INDEX.md lesen** — Scan-Depth-Spalte sagt exakt welche Zeilen
2. **SKILL.md** scannen (YAML + definierte Zeilen)
3. **Phase** identifizieren
4. **Referenz** (`references/`) lesen, BEVOR du schreibst
5. **Template** befüllen und Ergebnis mit Referenz validieren

**DENN:** Dieser phasenbasierte Zugriff minimiert die Kontext-Last und garantiert, dass du die exakte 'Definition of Done' kennst, bevor du minderwertige Artefakte produzierst.

## 🔗 Light Router
- **Scan-Depth pro Skill** → `DOCS/SKILL_INDEX.md`
- **Lesedisziplin** → `80_skill_routing_reading.md`
- **Skill-Erstellung** → `80_skill_construction_law.md`
