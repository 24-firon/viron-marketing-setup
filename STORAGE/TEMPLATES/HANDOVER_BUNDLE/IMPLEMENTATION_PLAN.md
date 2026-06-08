# 🗺️ ENTERPRISE IMPLEMENTATION PLAN: [PROJEKT-NAME] (Master-Template)

> **System Architecture:** [Kernsystem Version]
> **Current Phase:** [Phase A → Phase B Transition]
> **Infrastructure Target:** [Ziel-Umgebung / Cloud / Bare-Metal]
> **Status:** 🛠️ ACTIVE DEVELOPMENT (Session Hand-Off State)

---

## 1. STRATEGIC OBJECTIVE & ARCHITECTURAL SHIFT
[Kurze Beschreibung des Architektur-Shifts — was war das Problem, was ist die Lösung]

### Core Target Metrics:
*   **Context Window Optimization:** [Quantifiziertes Ziel — z.B. Token-Reduktion in %]
*   **Tenant Isolation:** [Mandantentrennung — welche Mechanismen]
*   **Gateway Reliability:** [API-Gateway — welche Absicherungen]

---

## 2. HARD SYSTEM STATE & PRE-REQUISITES
Bevor der nächste Agent operativen Code anfasst, MÜSSEN folgende Systemzustände verifiziert sein:
1.  **Environment Variables:** [Welche Env-Vars müssen gesetzt sein]
2.  **Package Manager:** [Welcher PM in welcher Version — keine Leichen]
3.  **Local Services:** [Welche lokalen Services müssen laufen]

---

## 3. MILESTONE MATRIX & DEPENDENCY GRAPH

```

[M1: Audit & Discovery] ──> [M2: Refactoring Layer] ──> [M3: Schema/Type Enforcement]
│
└──> [M4: E2E Verification]

```

| Milestone ID | Definition of Done (DoD) | Target Path | Risk Level |
| :--- | :--- | :--- | :--- |
| **M1: Audit** | [Was ist das Audit-Ergebnis?] | `[Pfad/Context-Map]` | 🟢 Low |
| **M2: Refactor** | [Was ist der Refactor-Erfolg?] | `[Pfad/Components]` | 🟡 Medium |
| **M3: Gateway** | [Was ist der Gateway-Erfolg?] | `[Pfad/API-Routes]` | 🔴 High |
| **M4: Deploy** | [Was ist der Deploy-Erfolg?] | `[Pfad/Config]` | 🟡 Medium |

---

## 4. LINEAR RUNBOOK & EXECUTION STEPS

### MEILENSTEIN 1: [Audit-Name]
*   **Step 1.1 [READ-ONLY]:** [Suche / Analyse-Pattern]
*   **Step 1.2 [DOCUMENTATION]:** [Dokumentations-Schritt]
*   *⏸️ INTERRUPTION GATEWAY 1:* [Wann stoppt der Agent]

### MEILENSTEIN 2: [Refactor-Name]
*   **Step 2.1 [WRITE]:** [Konkrete Edit-Anweisung]
*   **Step 2.2 [WRITE]:** [Konkrete Edit-Anweisung]
*   **Step 2.3 [WRITE]:** [Konkrete Edit-Anweisung]

### MEILENSTEIN 3: [Enforcement-Name]
*   **Step 3.1 [WRITE]:** [Konkrete Edit-Anweisung]
*   **Step 3.2 [WRITE]:** [Konkrete Edit-Anweisung]
*   **Step 3.3 [BUGFIX]:** [Fehlerbehandlung]

---

## 5. TECHNICAL DEBT & RISK MITIGATION
*   **[Risiko 1]:** [Beschreibung]
    *   *Mitigation:* [Gegenmaßnahme]
*   **[Risiko 2]:** [Beschreibung]
    *   *Mitigation:* [Gegenmaßnahme]
