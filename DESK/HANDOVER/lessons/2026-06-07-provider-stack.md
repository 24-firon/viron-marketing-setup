# LESSON — Provider-Stack (2026-06-07)

> **Status:** Immutable (No-Touch nach Erstellung). Spätere Änderungen nur als neue Datei mit Datum.
>
> **Zweck:** Dokumentiert die finale Entscheidung zum LLM-Provider-Stack für VIRON Marketing-Setup. Verhindert, dass zukünftige Sessions wieder versehentlich Anthropic-Modelle (Opus/Haiku/Sonnet) vorschlagen oder referenzieren.

---

## 1. ENTSCHEIDUNG

**Drei Provider sind verfügbar und authorisiert:**

| Provider | ENV-Variable | Charakter | Use-Case |
|:---------|:-------------|:----------|:---------|
| **NVIDIA NIM** | `NVIDIA_NIM_API_KEY` | Multi-Model (flexibel) | Universell einsetzbar, Fallback |
| **OpenCode Go** | `OPENCODE_GO` | Schnell, günstig | Standardtasks, Research, Evals |
| **OpenCode ZEN** | (intern, via OpenCode) | Stark, teurer | Strategie, SKILL.md-Schriften, Qualität |

**Explizit ausgeschlossen:** Anthropic-Modelle (Opus, Haiku, Sonnet) — auch wenn sie in CLAUDE.md §2 noch referenziert werden. Die Realität im `.env.local` ist NVIDIA NIM + OpenCode Go + OpenCode ZEN. CLAUDE.md ist veraltet und sollte bei nächstem Refresh angepasst werden.

---

## 2. KONTEXT

- `CLAUDE.md` (Stand 2026-03-14) erwähnt Claude Haiku als Orchestrator und Claude Sonnet für Specialized Agents.
- `.env.local` (Stand 2026-06-07) enthält KEINEN `ANTHROPIC_API_KEY` — nur `OPENROUTER_API_KEY`, `NVIDIA_NIM_API_KEY`, `VERTEX_*`, `OPENCODE_GO`.
- OpenRouter ist in `.env.local` vorhanden, aber nicht als primärer Provider für VIRON-Agenten etabliert. Bleibt als Notfall-Backup.
- User-Preference (2026-06-07): "Wir nutzen kein Anthropic."

---

## 3. TOKEN-MAPPING FÜR MCPs

```
Notion:  NOTION_TOKEN        ← {env:VIRON-OpenCode-ReadOnly}    (read-only)
Linear:  LINEAR_API_TOKEN    ← {env:LINEAR_API_KEY}              (read+write)
```

**Konfiguration in:** `opencode.jsonc` → `mcp.<server>.environment`

**Naming-Mismatch beachten:** `.env.local` heißt `LINEAR_API_KEY` (vom User gesetzt), `@tacticlaunch/mcp-linear` erwartet aber `LINEAR_API_TOKEN`. Mapping passiert in `opencode.jsonc`.

---

## 4. MCP-TIMEOUT

`mcp.*.timeout: 60000` (60 Sekunden) — der default von 10s reicht nicht für den ersten `npx -y`-Download der MCP-Pakete (`@notionhq/notion-mcp-server` ist 68k weekly downloads, ~80MB).

---

## 5. SUBAGENT-MODEL-EMPFEHLUNGEN

| Task-Typ | Empfehlung | Warum |
|:---------|:-----------|:------|
| Strukturiert, Research, Evals | OpenCode Go | Schnell, günstig, ausreichend |
| Schreib-Tasks, Qualität, Strategie | OpenCode ZEN | Qualität entscheidend |
| Live-MCP-Calls (Linear/Notion lesen) | egal | MCP-Calls kosten kein Model-Token, nur Context-Slots |
| Fallback wenn Go/ZEN nicht verfügbar | NVIDIA NIM | Multi-Model, flexibel |

**Escalation-Pattern:** Wenn SubAgent qualitativ schwach → eine Stufe hoch (Go → ZEN). Wenn zu langsam → eine Stufe runter (ZEN → Go).

---

## 6. SUBAGENT-HEADER-CONVENTION

```
model: opencode-zen    # Schreib-Tasks
model: opencode-go     # Standardtasks
model: nim             # Fallback
```

**Forbidden in jedem SubAgent-Prompt:** "FORBIDDEN: TodoWrite, Anthropic-Modelle (Opus/Haiku/Sonnet), scope-violation"

---

## 7. FOLLOW-UPS

- [ ] CLAUDE.md §2 bei nächstem Refresh von Anthropic-Refs bereinigen
- [ ] DECISIONS.md ADR-005 als kanonische Referenz (siehe dort)
- [ ] Bei Provider-Wechsel: neue Datei `DESK/HANDOVER/lessons/<datum>-provider-stack-v2.md` anlegen, diese Datei NICHT überschreiben

---

> **Erstellt:** 2026-06-07 | **No-Touch:** ab Erstellung
