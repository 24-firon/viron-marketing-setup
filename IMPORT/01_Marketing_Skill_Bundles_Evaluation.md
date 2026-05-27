# VIRON Research Report #1
# Alternatives & Supplementary Marketing Skill Bundles auf GitHub
# Recherche durchgeführt: Mai 2026

---

## Executive Summary

Corey Haines `coreyhaines31/marketingskills` ist das maßgebliche, am weitesten verbreitete Marketing-Skill-Repo im AI-Agent-Ökosystem (20K+ Stars, 40+ Skills) [web:1][web:107]. Im Februar 2026 erhielt es ein großes Update mit 26 neuen Skills und 29 Tool-Integrationen (GA4, Stripe, Mailchimp, Google Ads, Semrush, PostHog u.a.), was die Agenten in die Lage versetzte, nicht nur Tools zu empfehlen, sondern sie tatsächlich über APIs/MCP zu implementieren [web:109].

Für VIRON ist dieser Skill-Stack die solide Basis – doch es existieren mindestens 5 weitere Repositories, die entweder spezialisierte oder umfassendere Skill-Sets bieten und daher evaluiert werden müssen.

---

## 1.1 Das Baseline-Repo: coreyhaines31/marketingskills

**Repository:** https://github.com/coreyhaines31/marketingskills
**Website:** https://marketing-skills.com
**Aktueller Umfang (Stand Feb 2026):**
- 40+ Marketing-Skills (ursprünglich 43, laut Community-Tests) [web:107]
- 29 Tool-Integrationen mit API-Endpunkten und Auth-Guides [web:109]
- Version Tracking: Agent prüft Updates beim ersten Gebrauch [web:109]
- SkillKit-Support: Installation über Claude Code, Cursor, Copilot etc. [web:109]

**Fokusgebiete:**
- Conversion Optimization (CRO)
- Copywriting & Messaging
- SEO & Analytics
- Growth Engineering
- Marketing Psychology (50+ behavioral science models) [web:107]
- AI SEO Optimization (Princeton GEO Study Referenz) [web:107]
- Churn Prevention (dynamic cancellation flows) [web:107]
- Ad Creative mit generativer AI (Flux, Ideogram, Remotion, ElevenLabs) [web:107]

**Installation:**
```bash
npx skills add coreyhaines31/marketingskills
```

---

## 1.2 Primäre Alternativen – Tier 1 (Produktionsreif & Ergänzend)

### 1.2.1 whyashthakker/agent-skills-marketing

**Repository:** https://github.com/whyashthakker/agent-skills-marketing
**Veröffentlicht:** März 2026
**Umfang:** 50+ Skills

**Differenzierung gegenüber marketingskills:**
Dieses Bundle ist der direkteste Konkurrent und Ergänzung zu Haines' Repo. Es deckt Bereiche ab, die in marketingskills unterrepräsentiert oder nicht vorhanden sind:

- **GEO (Generative Engine Optimization):** Explizite Skills für AI-Search-Optimization, ein 2026 essentieller Trend [web:7]
- **Lifecycle Marketing:** Retention, Onboarding, Upsells, Reactivation Skills [web:7]
- **Creator Operations:** Influencer-Management, Creator Briefing, UGC-Coordination [web:7]
- **Campaign Execution:** End-to-End Kampagnenplanung und -ausführung mit Agent-Orchestrierung [web:7]
- **B2B-spezifische Frameworks:** Account-Based Marketing Skills, Enterprise Sales Enablement

**Empfehlung für VIRON:** **Hohe Priorität.** Installieren und mit marketingskills kombinieren. Insbesondere GEO und Lifecycle Marketing sind 2026 zentrale Service-Bereiche für DACH-KMUs.

---

### 1.2.2 realjaymes/marketingagentskills

**Repository:** https://github.com/realjaymes/marketingagentskills
**Veröffentlicht:** Februar 2026
**Umfang:** 27 AI Agent Skills

**Architektur:**
Jeder Skill ist eine eigenständige Markdown-Datei mit:
- Frameworks (Bewährte Marketing-Rahmenwerke)
- Best Practices (Branchenstandards)
- Task-Spezialisierung (konkrete Ausführungsanweisungen)

**Differenzierung:**
Fokus auf taktische, ausführbare Marketing-Tasks statt strategischer Overviews. Ideal für:
- Tägliche Agent-Tasks (Social Media Scheduling, Ad Copy Variationen)
- KMU-optimierte Workflows (weniger Enterprise, mehr pragmatisch)
- Performance Marketing Skills (Meta Ads, Google Ads Taktiken)

**Empfehlung für VIRON:** **Mittlere Priorität.** Als taktische Ergänzung zu Haines' strategischem Fokus nutzen. Besonders wertvoll für operative Social-Ads- und Content-Tasks.

---

### 1.2.3 robertbstillwell/marketing-skills

**Repository:** https://github.com/robertbstillwell/marketing-skills
**Umfang:** Curated Collection mit SKILL.md Files

**Architektur:**
Jeder Skill ist ein self-contained Directory mit:
- SKILL.md (Hauptanweisungen)
- Zusätzlichen Assets und Templates

**Differenzierung:**
- Strukturierter als flache Markdown-Sammlungen
- Fokus auf Growth Marketing (AARRR Framework, Pirate Metrics)
- Funnel-Optimization Skills
- Analytics & Tracking Setup (GA4, GTM, Mixpanel)

**Empfehlung für VIRON:** **Mittlere Priorität.** Die Directory-Struktur ist für VIRON als Inspiration für eigene Custom-Skills wertvoll.

---

### 1.2.4 SpillwaveSolutions/running-marketing-campaigns-agent-skill

**Repository:** https://github.com/SpillwaveSolutions/running-marketing-campaigns-agent-skill
**Veröffentlicht:** Dezember 2025
**Umfang:** Einzelner, aber umfassender Campaign-Skill

**Differenzierung:**
Dies ist kein Bundle, sondern ein einzelner, monolithischer Skill – jedoch mit einer Breite, die ein ganzes Repository ersetzt:

- Planung, Ausführung und Messung digitaler Marketingkampagnen
- Content, Social Media, Email, SEO, GEO
- Cross-Channel-Campaign-Orchestrierung
- Performance-Tracking und -Optimierung

**Empfehlung für VIRON:** **Niedrige Priorität.** Als Referenz für eigene Campaign-Skill-Entwicklung nützlich, aber nicht als Ersatz für modulare Bundles.

---

## 1.3 Meta-Repositories & Registries – Tier 2

### 1.3.1 VoltAgent/awesome-agent-skills

**Repository:** https://github.com/VoltAgent/awesome-agent-skills
**Umfang:** 1000+ Skills (gesamtes Ökosystem)

**Differenzierung:**
Kein eigenes Bundle, sondern eine Curated Collection aller verfügbaren Agent Skills aus:
- Official Dev Teams (Anthropics, Cursor, GitHub Copilot)
- Community Repositories
- Enterprise Contributions

**Empfehlung für VIRON:** **Wöchentlich scannen.** Neue Marketing-Skills werden hier zuerst gelistet.

---

### 1.3.2 heilcheng/awesome-agent-skills

**Repository:** https://github.com/heilcheng/awesome-agent-skills
**Veröffentlicht:** Dezember 2025
**Ansatz:** "Real-world Agent Skills von actual engineering teams"

**Differenzierung:**
Im Gegensatz zu bulk-generierten Repositories fokussiert sich diese Sammlung auf Skills, die in Produktionsumgebungen getestet wurden [web:4].

**Empfehlung für VIRON:** **Mittlere Priorität.** Für Best-Practice-Patterns in Skill-Strukturierung.

---

### 1.3.3 mcpservers.org Agent Skills Library

**Website:** https://mcpservers.org/de/agent-skills
**Sprache:** Deutsch verfügbar

**Differenzierung:**
Deutschsprachige Ressource für Agent Skills, kompatibel mit Claude Code, Codex und weiteren Agenten [web:110].

**Empfehlung für VIRON:** **Niedrige Priorität.** Als Referenz für DACH-spezifische Skill-Formulierungen.

---

## 1.4 Kommerzielle Skill-Bundles (Ungated / Freemium)

### 1.4.1 gui.marketing/skills/

**Website:** https://gui.marketing/skills/
**Umfang:** 85+ AI Agent Skills

**Fokusgebiete:**
- CRO, SEO, Google Ads, Meta Ads
- GTM, Design, Web Development
- Performance Marketing Taktiken

**Empfehlung für VIRON:** **Evaluieren.** Kommerzielle Qualität, aber unklar ob wirklich open source oder freemium.

---

### 1.4.2 lionelz.com – 70+ Free Claude Code Marketing Skills

**Website:** https://lionelz.com/en/blog/claude-code-marketing-skills-free-ungated/
**Umfang:** 70+ Free Skills

**Differenzierung:**
Vollständig ungated (keine Email-Capture, kein Paywall). Direkt kopierbar und anpassbar [web:121].

**Empfehlung für VIRON:** **Hohe Priorität.** Sofort scrapen und in eigenes Skill-Repository integrieren.

---

## 1.5 Zusammenfassung: Empfohlener Skill-Stack für VIRON

| Repository | Priorität | Installieren? | Nutzen |
|------------|-----------|---------------|--------|
| coreyhaines31/marketingskills | Basis | ✅ Bereits installiert | Strategisches Marketing, CRO, Psychology |
| whyashthakker/agent-skills-marketing | Hoch | ✅ Sofort | GEO, Lifecycle, Creator Ops |
| realjaymes/marketingagentskills | Mittel | ✅ In Q2 | Taktische Execution, Ads |
| lionelz.com (70+ Skills) | Hoch | ✅ Sofort (manuell kopieren) | Ungated, breite Abdeckung |
| robertbstillwell/marketing-skills | Mittel | ⚠️ Evaluieren | Growth Frameworks, Funnel |
| VoltAgent/awesome-agent-skills | Monitor | ❌ | Discovery neuer Skills |

---

## 1.6 Action Items

1. **Sofort:** `npx skills add whyashthakker/agent-skills-marketing` installieren
2. **Sofort:** lionelz.com 70+ Skills scrapen und in VIRON-Skill-Repo mergen
3. **Woche 1:** Gap-Analyse zwischen installierten 33 Skills und allen identifizierten Bundles
4. **Woche 2:** Custom VIRON-Skills erstellen (DACH-spezifisch, siehe Report #5)
5. **Monatlich:** VoltAgent/awesome-agent-skills auf neue Marketing-Skills scannen

---

*Bericht generiert: Mai 2026*
*Recherche basiert auf: GitHub Search, Community-Diskussionen (Reddit), technische Dokumentation*
