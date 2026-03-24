> **Regel-Zweck:** Definiert den Lifecycle von Content-Pieces über 3 Sicherheitszonen und legt die Bedingungen für den Task-Abschluss (DoD) fest.

## 1. DAS 3-ZONEN CONTENT-MODELL
Um zu verhindern, dass finale Ordner mit unfertigem Müll geflutet werden, gilt strikt:
- **Zone 1 (Dein Brain):** Hier planst du die Strategie. Kein Datei-Output.
- **Zone 2 (Drafts / WIP):** Sub-Agenten schreiben **ausschließlich** in `Work-Lab/Content/_wip/`.
- **Zone 3 (Final & Original):** Erst nach explizitem Approval des Operators darf Content in die Hauptordner verschoben oder an n8n/Airtable übergeben werden.

## 2. MARKETING "DEFINITION OF DONE"
Ein Linear-Task oder Content-Piece gilt erst dann als **✅ Erledigt**, wenn DREI Bedingungen erfüllt sind:
1. **Physische Existenz:** Der Text liegt im geforderten Format im `Content/`-Ordner ODER wurde via Airtable bereitgestellt.
2. **System-Sync:** Das entsprechende Linear-Issue wurde mit einem Link/Pfad zum Ergebnis aktualisiert.
3. **Operator-Freigabe:** Du hast den Operator (Inspektor) gefragt: "Bitte prüfe den Draft. Gib das Go für den Abschluss."
**Verbot:** Einen Task abhaken, nur weil der Text generiert, aber noch nicht in Airtable/Linear verknüpft wurde.