---
name: File Operation Safety — Edit vs. Write
description: Wann edit und wann write. Proof-of-Reading Pflicht. Anti-Kompression.
trigger: always_on
scope: alle
repo: all
---

# File Operation Safety

> **STATUS:** ALWAYS_ON
> **SCOPE:** Alle Datei-Operationen
> **BLOCK:** 10 — Safety & Zerstörungsschutz

## 1. Die goldene Regel

**Bestehende Dateien:** NUR das `edit`-Tool verwenden. NIEMALS `write`.
**Neue Dateien:** Nur wenn die Datei NICHT existiert, `write` verwenden.

`write` überschreibt die gesamte Datei und löscht stillschweigend Kommentare, Struktur oder Metadata, die nicht im neuen Inhalt enthalten sind. Das ist ein irreversibler Datenverlust-Vorfall.

## 2. Proof-of-Reading

Bevor du `edit` oder `write` nutzt, MUSST du die Datei ZUERST mit `read` geladen haben.

**Niemals:**
- Blind eine Datei überschreiben
- Ein `edit` absetzen ohne den aktuellen Inhalt zu kennen
- Annahmen über den Inhalt einer Datei treffen

**Immer:**
- `read` → Inhalt verstehen → `edit` (bei bestehenden Dateien)
- `read` (Prüfung) → `write` (nur bei neuen Dateien)

## 3. Diff-Integrität

`edit` erzeugt einen sauberen Diff der nur die tatsächliche Änderung zeigt. `write` zeigt die gesamte Datei als geändert — damit ist kein Review mehr möglich. Der Operator MUSS nachvollziehen können, was sich geändert hat. Bei `write` geht diese Nachvollziehbarkeit komplett verloren.

## 4. Anti-Kompression

Wenn du eine bestehende Datei mit `edit` änderst, bewahre den ursprünglichen Formulierungsstil und die Präzision. Agenten neigen zur Kompression von "gut genug" erscheinenden Inhalten — dabei gehen unmissverständliche Formulierungen verloren, die über Monate entwickelt wurden.

## 4. Keine Skripte für Datei-Inhalte

Kein `sed`, `awk`, `PowerShell-Replace` oder `Bash-Script` für Änderungen an Datei-Inhalten. Skripte sind kontextblind und zerstören die Satz-Semantik. Dateien werden mit der Pinzette editiert.
