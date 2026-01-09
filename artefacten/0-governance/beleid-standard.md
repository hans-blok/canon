# Beleid — Standard Repository

**Repository**: standard  
**Versie**: 1.9.0  
**Status**: Active  
**Last Updated**: 2026-01-07  
**Eigenaar**: Architecture & AI Enablement

---

## 1. Context en Doel

De **standard** repository bevat alle governance-documenten, agent-charters, fase-charters en templates die de basis vormen voor gestructureerde en consistente AI-agent-ontwikkeling binnen het **Agent Eco-systeem**.

### Agent Eco-systeem Architectuur

Dit beleid is onderdeel van een **centraal agent eco-systeem** met de volgende architectuur:

```
┌─────────────────────────────────────────────────────────────┐
│  Agent Eco-systeem (Centraal)                               │
│  ├── standards/          — Governance, charters, templates  │
│  ├── agent-capabilities/ — PowerShell scripts, tooling      │
│  └── [andere centrale repos]                                │
└─────────────────────────────────────────────────────────────┘
                          ↓ aanroepen
┌─────────────────────────────────────────────────────────────┐
│  Project-Workspaces (Lokaal, "schoon")                      │
│  └── /artefacten/        — Alle gegenereerde artefacten     │
│      ├── a.trigger/                                          │
│      ├── b.architectuur/                                     │
│      ├── c.specificatie/                                     │
│      └── ...                                                 │
│  GEEN .github/agents/, GEEN .github/prompts/                │
└─────────────────────────────────────────────────────────────┘
```

**Kernprincipes**:
- **Centraal beheer**: Alle agents, charters en governance blijven in centrale repositories
- **Schone project-workspaces**: Project-repositories bevatten GEEN agents of prompts
- **Scheiding van verantwoordelijkheden**: Agent-definitie (centraal) vs. artefact-generatie (lokaal)

Dit beleid beschrijft de specifieke regels en werkwijzen die gelden binnen deze repository en die aanvullend zijn op de algemene constitutie.

---

## 2. Taalgebruik

**Alle documentatie, charters en communicatie binnen deze repository gebeuren in het Nederlands.**

- Technische termen mogen in het Engels blijven indien er geen gangbare Nederlandse vertaling bestaat
- Code, identifiers en bestandsnamen volgen internationale conventies (Engels)
- Agents communiceren in het Nederlands op taalniveau B1
- Bij twijfel geldt: helderheid en begrijpelijkheid boven formaliteit

---

## 3. Governance-structuur

Deze repository wordt beheerd volgens de principes en werkwijze zoals vastgelegd in:

**`agent.charters/std.agent.charter.moeder.md`**

De Moeder Agent is verantwoordelijk voor:
- Het ontwerpen en creëren van nieuwe agents
- Het valideren en verbeteren van agent-charters
- Het waarborgen van consistentie en kwaliteit in het agent-landschap
- Het voorkomen van scope-overlap en conflicten tussen agents

Alle agent-ontwikkeling, charter-wijzigingen en governance-besluiten volgen de principes en werkwijze zoals beschreven in het charter van de Moeder Agent.

---
### 3.1 Git Beperkingen
Agents hebben **strikte beperkingen** op Git-operaties:

- ❌ **Geen push naar GitHub**: Agents mogen NOOIT direct pushen naar GitHub repositories
- ✅ **Lokaal werken**: Agents mogen alleen lokale bestanden creëren en wijzigen
- ✅ **Git add/commit**: Agents mogen lokaal committen (optioneel, alleen indien expliciet gevraagd)
- ❌ **Geen remote operaties**: Geen push, pull, fetch zonder menselijke tussenkomst
- ✅ **Menselijke controle**: Alle wijzigingen moeten door een mens worden gereviewd en gepushed

**Rationale**: 
- Kwaliteitscontrole door menselijke review voordat code naar remote gaat
- Voorkomen van ongewenste of foutieve wijzigingen in gedeelde repositories
- Behoud van traceerbaarheid en verantwoordelijkheid

## 4. Documentstructuur

De repository hanteert de volgende standaard-structuur:

```
governance/           — Constitutie, beleid, kwaliteitseisen, frameworks
agent.charters/       — Volledige agent-charters
phase.charters/       — Fase-specifieke charters (SAFe)
templates/            — Herbruikbare templates voor charters
desc-agents/          — Beknopte agent-beschrijvingen (overzicht)
```

---

## 5. Artefact-creatie en Project-structuur

### 5.1 PowerShell Scripts Locatie
Alle PowerShell scripts voor het realiseren van artefacten bevinden zich in de repository **agent-capabilities**.

### 5.2 Artefact-locatie: Lokale Project-Workspaces
Alle artefacten die door agents worden gegenereerd, worden aangemaakt in de **lokale project-workspace**, niet in de standards repository.

**Project-Workspace Principes**:
- **Schone workspace**: Project-workspaces bevatten GEEN `.github/agents/` of `.github/prompts/` folders
- **Alleen artefacten**: Project-workspaces bevatten uitsluitend gegenereerde artefacten en applicatiecode
- **Centraal agent-beheer**: Alle agents blijven in het centrale agent eco-systeem (standards repository)
- **Input via project-pad**: Agents ontvangen als input het **project-pad** (lokale workspace waar gewerkt wordt)
- **Output naar project**: Artefacten worden gegenereerd in de project-specifieke locatie

### 5.3 Bestandsnaamconventies conform Delivery Framework
Alle artefacten worden in de **artefacten** folder geplaatst conform het **Delivery Framework** zoals beschreven in `governance/delivery-framework.md`.

**Artefact-structuur in projectrepositories**:
```
<project-root>/
└── artefacten/
    ├── a.business-case.md           — Fase A: Business cases
    ├── a.founding-hypothesis.md     — Fase A: Founding hypothesis
    ├── b.adr-001-service-arch.md    — Fase B: Architecture Decision Records
    ├── b.cdm.md                     — Fase B: Conceptueel Datamodel
    ├── c.feature-login.md           — Fase C: Feature specificaties
    ├── c.ldm.md                     — Fase C: Logisch Datamodel
    ├── d.api-orders.md              — Fase D: API designs
    ├── d.tdm.md                     — Fase D: Technisch Datamodel
    ├── e.src/                       — Fase E: Code, scripts, implementatie
    ├── f.test-rapport.md            — Fase F: Test rapporten, validatie
    ├── g.release-notes.md           — Fase G: Release notes
    └── u.tooling.md                 — Fase U: Ondersteunende tools
```

**Naamgevingsconventie**:
- Alle artefacten hebben prefix: `<fase letter lowercase>.<artefact-naam>`
- Voorbeelden: `a.business-case.md`, `b.adr-001.md`, `c.feature-login.md`, `d.api-spec.md`
- **Geen fase-folders**: Artefacten worden direct in `/artefacten/` geplaatst met fase-prefix
- **Rationale**: Prefixes zijn voldoende voor organisatie, folders zijn overbodig

### 5.4 Automatische Artefacten Folder-creatie
**Wanneer de artefacten folder niet bestaat in de projectrepository, wordt deze automatisch aangemaakt door de agent.**

**Werkwijze**:
1. Agent ontvangt project-pad als input
2. Agent bepaalt fase (a t/m g of u) op basis van eigen charter
3. Agent controleert of `artefacten/` folder bestaat
4. Indien niet: agent creëert folder `artefacten/`
5. Agent genereert artefact met fase-prefix in `artefacten/`

**Voorbeeld**:
- Agent `std.c.requirements-writer` werkt in fase C (Specificatie)
- Agent ontvangt input: project-pad = `C:\projects\myapp`
- Agent controleert of `C:\projects\myapp\artefacten\` bestaat
- Indien niet: agent creëert folder `artefacten/`
- Agent genereert requirements in `C:\projects\myapp\artefacten\c.requirements.md` (met fase-prefix `c.`)

---

## 6. Charter-eisen

Alle agents in dit ecosysteem:
- Hebben een volledig ingevuld charter conform `templates/agent.charter.template.md`
- Voldoen aan de principes uit de constitutie
- Hebben een eenduidige, niet-overlappende scope
- Documenteren expliciete inputs, outputs en samenwerkingspatronen
- Benoemen anti-patterns en verboden gedrag

### 6.1 Scripts en Normbesef
**Scripts hebben geen intrinsiek normbesef**

Scripts zijn deterministisch en uitvoerend van aard. Ze hebben geen ingebouwd begrip van normen, waarden of beleid.

**Wat scripts WEL doen**:
- ✅ **Controleren op randvoorwaarden**: Scripts valideren of vereiste artefacten aanwezig zijn
- ✅ **Structurele checks**: Bestaan beleid, constitutie en charter-bestanden?
- ✅ **Formaat-validatie**: Zijn benodigde secties aanwezig in documenten?
- ✅ **Dependency-verificatie**: Zijn afhankelijkheden beschikbaar?

**Wat scripts NIET doen**:
- ❌ **Inhoudelijke kwaliteitsbeoordeling**: Scripts beoordelen niet of content "goed" of "juist" is
- ❌ **Normatieve beslissingen**: Scripts nemen geen beslissingen over wat "hoort" of "mag"
- ❌ **Contextueel begrip**: Scripts begrijpen niet de betekenis van content

**Voorbeelden van randvoorwaarden-controles**:
```powershell
# Controleer of governance-documenten aanwezig zijn
if (-not (Test-Path "governance/constitutie.md")) {
    throw "Constitutie niet gevonden"
}
if (-not (Test-Path "artefacten/0-governance/beleid-standard.md")) {
    throw "Beleid niet gevonden"
}

# Controleer of agent-charter bestaat
if (-not (Test-Path "charters.agents/$agentPath")) {
    throw "Agent charter niet gevonden"
}
```

**Rationale**:
- Scripts zijn tools, geen decision-makers
- Kwaliteitsbewaking gebeurt door mensen en LLM-agents, niet door scripts
- Scripts garanderen structuur, niet inhoud

### 6.2 Prompts als Contracten
**Prompts zijn contracten, geen proza**

We benaderen prompts als formele contracten met duidelijke specificaties, niet als vrije tekst of verhalen.

**Wanneer worden prompts geschreven?**
- ✅ **Agents die het LLM raadplegen**: Voor deze agents worden prompts geschreven
- ❌ **Agents die puur deterministisch zijn**: Voor deze agents worden GEEN prompts geschreven (zij hebben geen LLM-interactie)

**Prompt-structuur volgens Yourdan-achtige specificatie**:

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  INPUT                                          │
│  ├── Verplichte parameters                     │
│  ├── Optionele parameters                      │
│  └── Context-informatie                        │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  PROCESSING RULES                               │
│  ├── Validatieregels                           │
│  ├── Transformatielogica                       │
│  ├── Business rules                            │
│  └── Invarianten (wat altijd waar moet zijn)   │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  OUTPUT FORMAT                                  │
│  ├── Schema-definitie                          │
│  ├── Verplichte velden                         │
│  ├── Optionele velden                          │
│  └── Formaat-specificaties                     │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Contract-elementen**:

1. **Input-specificatie**
   - Wat moet de agent ontvangen?
   - Welke formaten zijn toegestaan?
   - Wat zijn de constraints?

2. **Processing Rules**
   - Welke validaties moeten uitgevoerd worden?
   - Welke transformaties zijn vereist?
   - Welke business rules gelden?
   - **Invarianten**: Eigenschappen die altijd waar moeten zijn (pre-condities, post-condities)

3. **Output Format**
   - Welke structuur heeft de output?
   - Welke velden zijn verplicht/optioneel?
   - Wat zijn de formaat-eisen?

**API Contract Schema + Invarianten + Voorbeelden**:

```yaml
# Voorbeeld: Feature Analist Agent Contract

input:
  required:
    - project_path: string
    - feature_description: string
  optional:
    - existing_features: array<string>

processing_rules:
  invariants:
    - "Output bevat altijd acceptance criteria"
    - "Feature ID is uniek binnen project"
    - "Feature is traceerbaar naar business waarde"
  validations:
    - "project_path moet bestaan"
    - "feature_description minimaal 50 karakters"
  transformations:
    - "Converteer feature_description naar gestructureerd feature document"
    - "Genereer uniek feature ID op basis van timestamp"

output:
  schema:
    feature_id: string (format: FEAT-YYYYMMDD-NNN)
    title: string
    description: string
    acceptance_criteria: array<string>
    business_value: string
  required_fields:
    - feature_id
    - title
    - acceptance_criteria
  format:
    - Markdown document
    - Conform feature.template.md

quality_gates:
  - "Feature heeft minimaal 3 acceptance criteria"
  - "Business waarde is expliciet benoemd"
  - "Acceptance criteria zijn testbaar (given-when-then)"
  - "Feature past binnen scope zoals gedefinieerd in charter"

examples:
  - input:
      project_path: "/projects/myapp"
      feature_description: "Als gebruiker wil ik kunnen inloggen met mijn email en wachtwoord"
    output:
      feature_id: "FEAT-20260107-001"
      title: "Gebruiker login met email en wachtwoord"
      acceptance_criteria:
        - "Given ik ben op de login-pagina, When ik vul geldig email en wachtwoord in, Then word ik doorgestuurd naar dashboard"
        - "Given ik vul ongeldig wachtwoord in, When ik klik op login, Then zie ik foutmelding"
        - "Given ik klik op 'wachtwoord vergeten', When ik vul mijn email in, Then ontvang ik reset-link"
```

**Quality Gates**:

Elke prompt-contract definieert expliciet:
- ✅ **Wat is een succesvolle output?**
- ✅ **Welke kwaliteitseisen gelden?**
- ✅ **Hoe wordt validatie uitgevoerd?**
- ✅ **Wat zijn de acceptance criteria?**

**Rationale**:
- Prompts als contracten dwingen tot precisie en volledigheid
- Yourdan-structuur (input-processing-output) maakt verwachtingen expliciet
- API-achtige schema's maken integratie en validatie mogelijk
- Invarianten waarborgen consistent gedrag
- Voorbeelden verduidelijken verwachtingen en dienen als test-cases
- Quality gates maken kwaliteit meetbaar en controleerbaar
- Contracten zijn versioneerbaar, testbaar en onderhoudbaar

### 6.3 Charter-toegang en Synchronisatie
**Voordat een agent zijn eigen charter leest, moet deze eerst de laatste versie ophalen:**

```powershell
git pull https://github.com/hans-blok/standard.git
```

**Werkwijze**:
1. Agent start en heeft charter-informatie nodig
2. Agent voert eerst `git pull` uit op standards repository
3. Agent leest vervolgens het charter uit lokale repository
4. Agent gebruikt charter-informatie voor uitvoering

**Rationale**:
- Waarborgt dat agents altijd met de meest recente charter-versie werken
- Voorkomt inconsistenties door verouderde charter-informatie
- Centrale bron van waarheid wordt gegarandeerd
- Handmatige synchronisatie-fouten worden voorkomen

**Uitzonderingen**:
- Deze regel geldt NIET voor agents die deterministisch werken zonder charter-raadpleging
- Deze regel geldt NIET tijdens ontwikkeling/testing wanneer expliciet lokale wijzigingen getest worden

### 6.4 Naming Conventions voor Agent Identifiers

**Principe**: Agent identifiers gebruiken ALTIJD afkortingen voor beknoptheid en foutreductie.

**Structuur**:
```
std.agent.<fase>.<afkorting>
```

**Voorbeelden**:
- `std.agent.c.ldm` (Logisch Data Modelleur)
- `std.agent.d.tdm` (Technisch Data Modelleur)
- `std.agent.b.cdm` (Conceptueel Data Modelleur)
- `std.agent.a.fho` (Founding Hypothesis Owner)
- `std.agent.c.fa` (Feature Analist)

**Bestandsnamen blijven voluit**:
- Bestandsnaam: `std.agent.charter.c.logisch-data-modelleur.md`
- Agent Identifier daarin: `std.agent.c.ldm`

**Rationale**:
- Codes zijn minder foutgevoelig bij typen en verwijzingen
- Kortere identifiers verbeteren leesbaarheid in code en configuratie
- IT kent twee kampen: voluit (bestandsnamen) en codes (identifiers) — beide hebben hun plaats
- Bestandsnamen voluit zorgen voor vindbaarheid in filesysteem
- Identifiers als codes zorgen voor efficiëntie in gebruik

---

## 7. Wijzigingsproces

### Governance-documenten
- **Constitutie**: Alleen inhoudelijke wijzigingen door mens; redactionele wijzigingen door Logos Agent
- **Beleid**: Wijzigingen via expliciet updateproces en versiebeheer
- **Kwaliteitseisen en frameworks**: Wijzigingen na review door architect

### Agent-charters
- Nieuwe charters via Moeder Agent en Charter Writer Agent
- Wijzigingen aan bestaande charters via gecontroleerd proces
- Alle wijzigingen worden gedocumenteerd in de Change Log van het charter

---

## 8. Kwaliteitsnormen

Alle artefacten in deze repository voldoen aan:
- **Volledigheid**: Geen ontbrekende secties of impliciete informatie
- **Consistentie**: Terminologie en structuur zijn uniform
- **Traceerbaarheid**: Beslissingen zijn herleidbaar naar bron
- **Helderheid**: Begrijpelijk op B1-niveau
- **Evolutie**: Versiebeheersing en change logs

---

## 9. Agent-gedrag binnen Agent Eco-systeem

### 9.1 Agents in Centrale Repository (standards)
Agents die binnen deze repository werken:
1. Lezen eerst alle governance-documenten (constitutie, beleid, relevante charters)
2. Handelen conform hun charter en binnen hun scope
3. Escaleren bij scope-overlap of conflicten
4. Documenteren aannames expliciet
5. Leveren alleen complete, gevalideerde outputs

### 9.2 Agents Werkend op Project-Workspaces
Agents die artefacten genereren in project-workspaces:
1. Worden aangeroepen vanuit de **centrale agent eco-systeem repository**
2. Ontvangen als input het **project-pad** van de lokale workspace
3. Genereren artefacten in fase-folders binnen de project-workspace
4. Creëren automatisch benodigde folder-structuur indien deze niet bestaat
5. Plaatsen **GEEN** agent-definities of prompts in de project-workspace
6. Houden project-workspaces "schoon" en gefocust op artefacten
7. **Pushen GEEN code naar GitHub repositories** — agents mogen wijzigingen doorvoeren in de lokale workspace, maar het pushen naar remote repositories (git push) is niet toegestaan

---

## 10. Relatie tot Constitutie

Dit beleid is ondergeschikt aan `governance/constitutie.md`.

Bij conflict tussen dit beleid en de constitutie geldt altijd de constitutie.

---

## 11. Change Log

| Datum | Versie | Wijziging | Auteur |
|------|--------|-----------|--------|  
| 2025-12-14 | 1.0.0 | Initiële versie | Moeder Agent |
| 2025-12-30 | 1.1.0 | Toegevoegd: Artefact-creatie beleid (§5) — PowerShell scripts in agent-capabilities, artefacten in lokale repos, folder-structuur conform Delivery Framework, automatische folder-creatie | Moeder Agent |
| 2025-12-30 | 1.2.0 | Toegevoegd: Agent Eco-systeem architectuur (§1) — Centraal agent-beheer, schone project-workspaces zonder agents/prompts, scheiding verantwoordelijkheden; Uitgebreid: Agent-gedrag (§9.2) | Moeder Agent |
| 2025-12-30 | 1.3.0 | Toegevoegd: Verbod op git push door agents (§9.2.7) — agents mogen geen code pushen naar GitHub repositories | Human |
| 2025-12-30 | 1.4.0 | Gewijzigd: Folder-structuur (§5.3, §5.4) — alle artefacten in centrale "artefacten" folder met naamgevingsconventie `<fase letter lowercase>.<fase naam>` | Human |
| 2026-01-05 | 1.5.0 | Toegevoegd: Prompts voor Agents (§6.1) — prompts alleen voor LLM-raadplegende agents, niet voor puur deterministisch agents | Charter Schrijver |
| 2026-01-06 | 1.6.0 | Toegevoegd: Charter-toegang en Synchronisatie (§6.2) — agents moeten git pull uitvoeren uit https://github.com/hans-blok/standard.git voordat ze hun charter lezen | Moeder Agent |
| 2026-01-06 | 1.7.0 | Toegevoegd: Naming Conventions voor Agent Identifiers (§6.4) — altijd afkortingen in identifiers, bestandsnamen voluit | Moeder Agent |
| 2026-01-07 | 1.9.0 | Gewijzigd: Artefact-structuur (§5.3, §5.4) — verwijderd fase-folders, alleen fase-prefixes in bestandsnamen (bijv. `a.business-case.md`, `b.adr-001.md`); rationale: prefixes zijn voldoende, folders zijn overbodig | Human |
| 2026-01-07 | 1.8.0 | Toegevoegd: Scripts en Normbesef (§6.1) — scripts hebben geen intrinsiek normbesef maar controleren wel randvoorwaarden; Gewijzigd: Prompts als Contracten (§6.2) — prompts zijn contracten met Yourdan-achtige specificatie (input-processing-output), API contract schema + invarianten + voorbeelden, en quality gates; Hernummering secties 6.2→6.3, 6.3→6.4 | Human |

