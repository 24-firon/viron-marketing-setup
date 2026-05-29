# 80_anatomy_of_complex_skill.md (Strukturanalyse & Navigation)

> **STATUS:** ALWAYS_ON
> **SCOPE:** Handhabung und Verständnis von Agent-Skills

## 1. Realitäts-Check: Komplex vs. Simpel
Prüfe vor der Nutzung, ob ein Skill eine komplexe Struktur (Ordner mit `templates/`, `examples/`) oder eine simple Struktur (nur eine `SKILL.md`) aufweist. Behandle einfache Skills als monolithische Anweisung, **DENN** eine unnötige Suche nach Routern in simplen Skills verschwendet Token und Zeit.

## 2. Die Anatomie komplexer Skills
Lade bei komplexen Skills niemals den gesamten Inhalt blind. Nutze die `SKILL.md` als Router, **DENN** das ungefilterte Laden von Templates und Examples flutet das Kontext-Fenster mit irrelevantem Rauschen und provoziert Rule-Fatigue.

**Die Struktur (Bei komplexen Skills):**
```
.opencode/skills/<skill-name>/
├── SKILL.md                    ← DER ROUTER
├── examples/                   ← "Definition of Done" Referenzen
├── templates/                  ← Scaffolding (Vorlagen)
├── scripts/                    ← Automatisierung
└── schemas/                    ← Daten-Validierung
```

## 3. Der Navigations-Workflow
Folge bei komplexen Skills strikt diesem Pfad:
1. **SKILL.md** scannen (YAML & Matrix).
2. **Phase** identifizieren.
3. **Beispiel** (`examples/`) lesen, BEVOR du schreibst.
4. **Template** befüllen und Ergebnis mit Beispiel validieren.
**DENN:** Dieser phasenbasierte Zugriff minimiert die Kontext-Last und garantiert, dass du die exakte 'Definition of Done' kennst, bevor du minderwertige Artefakte produzierst.

## 🔗 Light Router (Deep Knowledge & Skills)
- **WENN** du die detaillierte anatomische Aufschlüsselung als Heavy Payload benötigst ➔ **LIES** `DOCS/architecture/concepts/opencode_knowledge/81_anatomy_of_complex_skill.md`.
- **WENN** du die ressourcenschonende Lesedisziplin vertiefen willst ➔ **LIES** `DOCS/architecture/concepts/opencode_knowledge/87_skill_routing_reading.md`.
- **WENN** du einen neuen Skill bauen musst ➔ **LIES** `80_skill_creation_checklist.md` und **STARTE** den Skill `skill-creator`.
