# Beleid — standard workspace

**Constitutie**  
Bron van alle regels voor het eco-systeem.

- URL naar constitutie in standards:  
  `<url-naar-standards/governance/constitutie.md>`

**Value Stream**  
Welke waardestroom is primair van toepassing op deze workspace?

- Value stream: `niet van toepassing (agent-ecosysteem constitutie, boven de value streams)`

**Scope (domein / product)**  
Kern van het domein of product waar deze workspace over gaat.

- Scope: `centrale standaarden, doctrines, stage-charters en templates voor het agent-ecosysteem`

**Doctrine**  
Welke doctrine(s) zijn leidend voor het werk in deze workspace?

- Doctrine(s): `workspace-doctrine`, `doctrine-it-development`, `doctrine/value-streams`

**Taal**  
Taalafspraak voor deze workspace.

- Taal: `Nederlands (B1)`

**Aanvullend beleid**  
Eventuele aanvullende beleidsdocumenten specifiek voor deze workspace.

- Aanvullend beleid: `governance/beleid.md` (aanvullend beleid voor de standard workspace)

---

## 1. Context

De **standard** workspace is de centrale plek voor regels, standaarden en sjablonen voor het agent-ecosysteem.  
Deze workspace vormt de **agent-ecosysteem constitutie**: zij staat boven de value streams en is zelf geen value stream.

De constitutie en gedragscode zijn leidend.  
Dit beleid vult deze aan met korte afspraken specifiek voor deze workspace.

---

## 2. Scope

### 2.1 Binnen scope (wel)

- vastleggen en onderhouden van constitutie, gedragscode en doctrines;  
- vastleggen van de normering voor agent-charters (maar niet de agent-charters zelf);  
- beschrijven en beheren van fase-charters (stage-charters A t/m G en U) in deze workspace;  
- vastleggen van value streams en hun doctrines in de doctrine-folder;  
- beheren van templates voor charters, fase-charters en beleid;  
- publiceren van richtlijnen voor naamgeving en structuur van artefacten.

### 2.2 Buiten scope (niet)

- opstellen en beheren van individuele **agent-charters** (die horen in agent-services workspaces);  
- bouwen of draaien van applicatiecode;  
- project-specifieke procesafspraken of SLA’s;  
- technische implementatie van agents in agent-services;  
- team- of afdelingsspecifieke werkafspraken.

---

## 3. Niet in scope (expliciete uitsluitingen)

- wijzigen van de constitutie of gedragscode zelf (dit gebeurt via aparte governance-besluiten);  
- definiëren van cloudplatformen, CI/CD-omgevingen of tooling;  
- beschrijven van domeinmodellen voor specifieke producten of systemen.

---

## 4. Agent Werking

- in deze workspace zijn in de basis twee typen agents relevant: de Moeder-agent en per workspace één schrijvende agent die documenten zoals doctrines en beleid opstelt;  
- deze agents vallen bij uitzondering niet onder een value stream, maar onder de agent-ecosysteem constitutie;  
- de bron van agent-charters en prompts ligt in de centrale agent-services repositories, niet in deze workspace;  
- **voordat** agents een taak uitvoeren, lezen zij eerst de constitutie en waar nodig de gedragscode en relevante doctrines;  
- agents gebruiken deze workspace om normen, templates, doctrines en stage-charters te lezen en schrijven geen projectartefacten in deze repository.

---

## 5. Kwaliteitsnormen

- alle documenten in deze workspace zijn in het Nederlands en op B1-niveau;  
- documenten verwijzen naar doctrines en value streams via `artefacten/0-governance/doctrine/*.md`, niet via temp-bestanden;  
- afspraken over agents en stages zijn traceerbaar naar de relevante doctrines en, waar van toepassing, naar de bijbehorende value streams;  
- wijzigingen in doctrines, stage-charters of normering worden kort vastgelegd in de changelog of in de header van het betreffende document.

---

## 6. Samenvatting

- standard is de centrale governance-workspace en fungeert als agent-ecosysteem constitutie;  
- deze workspace valt zelf niet onder een value stream maar ligt erboven;  
- de focus ligt op constitutie, gedragscode, doctrines, stage-charters en templates, niet op individuele agent-charters;  
- alle agents lezen eerst de constitutie voordat zij taken uitvoeren;  
- documenten zijn kort, duidelijk en B1, met traceerbare verwijzingen naar doctrines en (waar relevant) value streams.
| 2025-12-30 | 1.1.0 | Toegevoegd: Artefact-creatie beleid (§5) — PowerShell scripts in agent-capabilities, artefacten in lokale repos, folder-structuur conform Delivery Framework, automatische folder-creatie | Moeder Agent |
| 2025-12-30 | 1.2.0 | Toegevoegd: Agent Eco-systeem architectuur (§1) — Centraal agent-beheer, schone project-workspaces zonder agents/prompts, scheiding verantwoordelijkheden; Uitgebreid: Agent-gedrag (§9.2) | Moeder Agent |
| 2025-12-30 | 1.3.0 | Toegevoegd: Verbod op git push door agents (§9.2.7) — agents mogen geen code pushen naar GitHub repositories | Human |
| 2025-12-30 | 1.4.0 | Gewijzigd: Folder-structuur (§5.3, §5.4) — alle artefacten in centrale "artefacten" folder met naamgevingsconventie `<fase letter lowercase>.<fase naam>` | Human |
| 2026-01-05 | 1.5.0 | Toegevoegd: Prompts voor Agents (§6.1) — prompts alleen voor LLM-raadplegende agents, niet voor puur deterministisch agents | Charter Schrijver |
| 2026-01-06 | 1.6.0 | Toegevoegd: Charter-toegang en Synchronisatie (§6.2) — agents moeten git pull uitvoeren uit https://github.com/hans-blok/standard.git voordat ze hun charter lezen | Moeder Agent |
| 2026-01-06 | 1.7.0 | Toegevoegd: Naming Conventions voor Agent Identifiers (§6.4) — altijd afkortingen in identifiers, bestandsnamen voluit | Moeder Agent |
| 2026-01-07 | 1.9.0 | Gewijzigd: Artefact-structuur (§5.3, §5.4) — verwijderd fase-folders, alleen fase-prefixes in bestandsnamen (bijv. `a.business-case.md`, `b.adr-001.md`); rationale: prefixes zijn voldoende, folders zijn overbodig | Human |
| 2026-01-07 | 1.8.0 | Toegevoegd: Scripts en Normbesef (§6.1) — scripts hebben geen intrinsiek normbesef maar controleren wel randvoorwaarden; Gewijzigd: Prompts als Contracten (§6.2) — prompts zijn contracten met Yourdan-achtige specificatie (input-processing-output), API contract schema + invarianten + voorbeelden, en quality gates; Hernummering secties 6.2→6.3, 6.3→6.4 | Human |

