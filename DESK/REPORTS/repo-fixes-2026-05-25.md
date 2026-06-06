# Repo-Fixes — 2026-05-25

## Ausgeführte Änderungen

### 1. DIRECTOR/Prompts reorganisiert
| Von | Nach | Typ |
|-----|------|-----|
| DIRECTOR/PROMPTS/P00_BOOTSTRAP.md | DIRECTOR/PROMPTS/active/P00_BOOTSTRAP.md | Verschieben |
| DIRECTOR/PROMPTS/P01_SESSION_INIT.md | DIRECTOR/PROMPTS/active/P01_SESSION_INIT.md | Verschieben |
| DIRECTOR/PROMPTS/P02_HANDOFF.md | DIRECTOR/PROMPTS/active/P02_HANDOFF.md | Verschieben |
| DESK/HANDOVER/sessions/session-2026-05-25.md | DIRECTOR/SESSIONS/2026-05-25/HANDOVER.md | Kopie |

### 2. opencode.jsonc aktualisiert
- 15 → 19 instructions (+4 neue: P00, P01, P02, HANDOVER)
- Watcher: `DESK/**` → `DESK/REPORTS/**` (HANDOVER/ bleibt im git)
- Skills: unverändert `.agents/skills`

### 3. CONTEXT.md Strukturdiagramm ergänzt
- DIRECTOR/ mit PROMPTS/active/ + SESSIONS/2026-05-25/
- IMPORT/ mit allen 9 Dateien (7 Perplexity + SEO + GTM)
- STORAGE/TOOLS/ als neuer Eintrag
- ARCHIVE/ mit Unterstruktur

### 4. STORAGE/INDEX.md aktualisiert
- DIRECTOR/, DESK/, IMPORT/, ARCHIVE/ als externe Verzeichnisse dokumentiert
- Wichtigste Payloads als FAQ
- Auto-Injektions-Hinweise ergänzt

## Verifizierung

- [x] Alle Dateien am korrekten Ziel
- [x] opencode.jsonc: 19 instructions, watcher korrigiert
- [x] CONTEXT.md: Vollständiges Diagramm
- [x] STORAGE/INDEX.md: Vollständige Payload-Liste
- [x] Keine Dateien gelöscht
- [x] DESK/HANDOVER/sessions/ bleibt erhalten (Kopie, kein Move)
