# AGENTS.md – VIRON Linear Setup

## 1. Build / Lint / Test Befehle

### Python-Ausführung
```bash
# Hauptskript ausführen (erfordert LINEAR_API_KEY)
python VIRON_Full_Package_v2/viron_linear_setup.py
```

### Einzelne Funktion ausführen
```bash
# Python REPL starten und Funktion importieren
python -c "
import sys
sys.path.insert(0, 'VIRON_Full_Package_v2')
from viron_linear_setup import get_organization_id
get_organization_id()
"
```

### Linting (falls installiert)
```bash
# Black Formatierung
black VIRON_Full_Package_v2/

# Flake8 Prüfung
flake8 VIRON_Full_Package_v2/

# isort Import-Sortierung
isort VIRON_Full_Package_v2/
```

### Testen
```bash
# Keine Tests vorhanden. Bei Bedarf pytest verwenden:
pytest tests/
pytest tests/test_file.py::test_function  # Einzelner Test
```

---

## 2. Codestil Richtlinien

### Imports
- Standardbibliothek → Third-Party → Lokale Module
- Immer `import os`, `import json` etc. (keine Kurzformen)
- Alphabetisch sortieren innerhalb jeder Gruppe

### Formatierung
- **4 Leerzeichen** für Einrückung (keine Tabs)
- Maximale Zeilenlänge: **100 Zeichen**
- Leerzeilen: 2 zwischen Top-Level-Definitionen, 1 zwischen Methoden
- Keine trailing whitespaces

### Typen
- Python 3.x (type hints empfohlen für neue Funktionen)
- Bei GraphQL: Klar dokumentierte Query/Mutation-Strings
- Konstanten: UPPER_SNAKE_CASE
- Variablen/Funktionen: snake_case

### Namenskonventionen
| Element | Konvention | Beispiel |
|---------|------------|----------|
| Dateien | snake_case | `viron_linear_setup.py` |
| Funktionen | snake_case | `def get_organization_id()` |
| Klassen | PascalCase | `class LinearClient:` |
| Konstanten | UPPER_SNAKE_CASE | `API_KEY`, `HEADERS` |
| Variablen | snake_case | `team_id`, `created_teams` |

### Fehlerbehandlung
- `try/except` mit spezifischen Exceptions
- Immer Fehlermeldung ausgeben: `print(f"⚠️  Fehler: {e}")`
- GraphQL Errors: `raise Exception(f"GraphQL Error: {data['errors']}")`
- `r.raise_for_status()` bei HTTP-Requests

### GraphQL
- Queries/Mutations als Triple-String-Variablen oben im Modul
- Descriptive Kommentare bei komplexen Queries
- Variablen als Dictionary übergeben

### Allgemeine Regeln
- Deutsche Kommentare für deutsche Projektdokumentation
- Englische Funktionsnamen (API-bezogen)
- Keine magic numbers – als Konstanten definieren
- ENV-Variablen mit Defaults: `os.environ.get("VAR", "default")`

---

## 3. Projektstruktur

```
Work-Lab/
├── VIRON_Full_Package_v2/
│   └── viron_linear_setup.py   # Hauptskript (946 Zeilen)
├── *.md                        # Dokumentation
└── *.xlsx                      # Daten/Export
```

---

## 4. Wichtige ENV-Variablen

| Variable | Beschreibung | Erforderlich |
|----------|--------------|--------------|
| `LINEAR_API_KEY` | Linear API Token | Ja |

---

## 5. Nützliche Hinweise

- Das Skript nutzt die **Linear GraphQL API** (`https://api.linear.app/graphql`)
- API-Dokumentation: https://developers.linear.app/docs/graphql/working-with-the-graphql-api
- Vor Ausführung: `export LINEAR_API_KEY="dein_key"`

---

## 6. Code-Beispiele

### GraphQL Query ausführen
```python
from viron_linear_setup import gql, HEADERS, URL

query = """
query {
  organization {
    id
    name
  }
}
"""
result = gql(query)
print(result)
```

### HTTP-Request mit Fehlerbehandlung
```python
import requests

try:
    r = requests.post(URL, headers=HEADERS, json=payload)
    r.raise_for_status()
    data = r.json()
except requests.exceptions.RequestException as e:
    print(f"⚠️  HTTP Fehler: {e}")
except Exception as e:
    print(f"⚠️  Unerwarteter Fehler: {e}")
```

### ENV-Variablen sicher abrufen
```python
import os

API_KEY = os.environ.get("LINEAR_API_KEY")
if not API_KEY:
    raise ValueError("LINEAR_API_KEY nicht gesetzt")
```

---

## 7. Wichtige Funktionen

| Funktion | Beschreibung | Zeile |
|----------|--------------|-------|
| `gql(query, variables)` | Führt GraphQL-Request aus | 18 |
| `get_organization_id()` | Holt Workspace-ID | 32 |
| `create_teams()` | Erstellt Teams | 66 |
| `create_labels()` | Erstellt Labels | - |
| `create_issues()` | Erstellt Issues | - |

---

## 8. Debugging Tipps

- **API-Key prüfen:** `echo $LINEAR_API_KEY` (Linux/Mac) oder `echo %LINEAR_API_KEY%` (Windows)
- **Response debuggen:** `print(r.text)` nach einem Request
- **GraphQL Playground:** https://api.linear.app/graphql (mit API-Key Header)
- **Rate Limits:** Linear hat Rate Limits – bei Fehlern Pausen einbauen

---

## 9. Wartung

- Regelmäßig API-Version prüfen: https://developers.linear.app/changelog
- Bei Änderungen an der Linear-GraphQL-API: Skript entsprechend anpassen
- Backup der existierenden Teams/Labels vor Neuerstellung machen
