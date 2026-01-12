# Workspace Architectuur — Normering en Standaardisatie

**Versie**: 1.0.0  
**Status**: Actief  
**Datum**: 2026-01-09  
**Eigenaar**: Architecture & AI Enablement  
**Type**: Normerend Architectuurdocument

---

## 1. Inleiding en Doel

Dit document definieert de **verplichte architectuur en structuur** voor alle workspaces binnen het Agent Eco-systeem. Het beschrijft welke conventies, standaarden en structuren consistent moeten zijn om interoperabiliteit tussen agents, workspaces en het centrale eco-systeem te waarborgen.

### Karakter van dit Document

- **Normerend**: Dit document stelt verplichte eisen en standaarden vast
- **Architectonisch**: Beschrijft structurele principes en patterns
- **Workspace-overstijgend**: Geldt voor alle repositories en workspaces
- **Interoperabiliteit-gericht**: Waarborgt dat agents en systemen naadloos kunnen samenwerken

Dit is **geen handleiding of instructiedocument**, maar een architectuurnorm die:
- **Governance** licht (wat moet, wat mag niet)
- **Standaardisatie** definieert (uniforme structuren en conventies)
- **Interoperabiliteit** waarborgt (downstream agents weten wat ze kunnen verwachten)

---

## 2. Architectuurprincipes

### 2.1 Scheiding van Verantwoordelijkheden

**Principe**: Centrale definitie, lokale executie

Het eco-systeem bestaat uit drie categorieën repositories:

1. **Standards Repository** (governance & framework)
   - Bevat workspace-overstijgende standaarden en governance (artefacten/0-governance/)
   - Bevat meta-agent charters (moeder-standard, charter-schrijver, logos)
   - Bevat charter-templates en delivery framework
   - Is de single source of truth voor governance en standaarden
   
2. **Agent-Capabilities Repository** (agent implementaties)
   - Bevat charters van capability-agents (fase-specifieke agents)
   - Bevat agent-definities voor capability-agents (.github/agents/, .github/prompts/)
   - Is de single source of truth voor capability-agents
   
3. **Project Workspaces** (lokale ontwikkelprojecten)
   - Bevatten **alleen** gegenereerde artefacten en applicatiecode
   - Bevatten **geen** agent-definities of charters
   - Volgen de gestandaardiseerde workspace-structuur

**Onderscheid in Agent-Charters**:
- **Workspace-overstijgende standaarden** (artefacten/0-governance/ in standards): 
  - Definiëren wat agents moeten zijn (agent-charter-normering.md)
  - Definiëren workspace-structuur (workspace-architectuur.md)
  - Definiëren ontwikkelproces (delivery-framework.md)
  
- **Meta-agent charters** (governance/charters-agents/ in standards):
  - Charters van agents die het agent-landschap beheren
  - Moeder Standard, Charter Schrijver, Logos
  
- **Capability-agent charters** (governance/charters-agents/ in agent-capabilities):
  - Charters van agents die daadwerkelijk werk doen
  - Fase-specifieke agents (A1, B1, C1, etc.)

### 2.2 Voorspelbaarheid door Standaardisatie

**Principe**: Elke workspace volgt dezelfde structuur

Agents kunnen alleen effectief werken wanneer zij de locatie van inputs, outputs en artefacten kunnen voorspellen. Daarom is uniformiteit verplicht.

### 2.3 Traceerbaarheid en Transparantie

**Principe**: Alle artefacten zijn traceerbaar naar hun bron

Elke workspace moet helder maken:
- Welke artefacten zijn gegenereerd
- Door welke agent/fase
- Op basis van welke input

---

## 3. Verplichte Workspace Structuur

### 3.1 Top-level Structuur

Elke workspace **moet** minimaal de volgende structuur hebben:

```
<workspace-root>/
├── artefacten/              # VERPLICHT: Alle gegenereerde artefacten
├── docs/                    # VERPLICHT: Documentatie en diagrammen
├── logs/                    # STANDAARD: Logbestanden van agent-uitvoer (wordt genegeerd door Git)
├── scripts/                 # OPTIONEEL: Automatiseringsscripts
├── templates/               # OPTIONEEL: Project-specifieke templates
├── .github/                 # VERPLICHT (voor GitHub repos): GitHub-specifieke configuratie
├── .gitignore               # VERPLICHT: Git ignore regels
└── README.md                # VERPLICHT: Workspace documentatie
```

### 3.2 Artefacten Folder — `/artefacten/`

**Doel**: Alle door agents gegenereerde output

**Structuur**: Flat structure met fase-prefixes voor project workspaces; georganiseerd per categorie voor governance repositories

**Onderscheid per Repository-type**:

#### 3.2.1 Voor Project Workspaces

**Naamgevingsconventie**: `<fase>.<artefact-naam>.<extensie>`

**Voorbeelden**:
```
artefacten/
├── a1.founding-hypothesis.md          # Fase A: Trigger
├── a2.business-case.md                # Fase A: Trigger
├── b1.cdm.md                          # Fase B: Architectuur
├── b2.adr-001-service-arch.md         # Fase B: ADR
├── b3.adr-002-data-storage.md         # Fase B: ADR
├── c1.feature-login.md                # Fase C: Feature specificatie
├── c2.ldm.md                          # Fase C: Logisch datamodel
├── d1.api-orders.yaml                 # Fase D: API design
├── d2.tdm.sql                         # Fase D: Technisch datamodel
├── e1.implementation-plan.md          # Fase E: Implementatie
├── f1.test-rapport.md                 # Fase F: Validatie
├── g1.release-notes.md                # Fase G: Deployment
└── u01.tooling-config.yaml            # Utility artefacten
```

**Verplichte Conventies voor Project Workspaces**:
- ☑ **Fase-prefix**: Altijd `<faseletter><volgnummer>.`
- ☑ **Lowercase**: Alle bestandsnamen in lowercase
- ☑ **Kebab-case**: Woorden gescheiden door `-`
- ☑ **Betekenisvolle namen**: Naam beschrijft inhoud
- ☑ **Geen folders per fase**: Alle artefacten direct in `/artefacten/`

**Rationale**: 
- Fase-prefix geeft directe traceerbaarheid naar SAFe-fase
- Flat structure voorkomt diep geneste folders
- Volgnummer voorkomt naam-conflicten binnen fase

#### 3.2.2 Voor Standards Repository (Governance)

**Structuur**: Georganiseerd per categorie

```
artefacten/
├── 0-governance/                      # Workspace-overstijgende standaarden
│   ├── constitutie.md                 # Onveranderlijke basisregels
│   ├── workspace-architectuur.md      # Dit document
│   ├── beleid-standard.md             # Workspace-specifiek beleid (scope & out of scope)
│   ├── agent-charter-normering.md     # Normering voor agent-charters
│   ├── delivery-framework.md          # SAFe development value stream
│   ├── gedragscode.md                 # Gedragscode voor agents
│   └── wetten-it-ontwikkeling.md      # IT ontwikkeling principes
├── 1-charter-application/             # Application charters
│   └── application-charter.all-phases.md
└── 2-charters-fases/                  # SAFe fase charters
    ├── std.fase.charter.a.trigger.md
    ├── std.fase.charter.b.architectuur.md
    └── ...
```

**Rationale**:
- **0-governance/**: Workspace-overstijgende standaarden die voor alle repositories gelden
- **1-charter-application/**: Application-brede charters (cross-fase)
- **2-charters-fases/**: Fase-specifieke charters volgens SAFe

**Belangrijk Onderscheid**:
- **Governance-documenten** (0-governance/): Definiëren standaarden en principes
- **Agent-charters** (governance/charters-agents/): Definiëren gedrag van specifieke agents
- Governance-documenten zijn normatief en workspace-overstijgend
- Agent-charters zijn specifiek per agent en volgen de governance

**Beleid-bestanden (beleid-<workspace>.md)**:
- Elk workspace/repository heeft zijn eigen beleid-bestand
- **Verantwoordelijkheid**: Moeder Standard Agent creëert en beheert dit bestand
- **Inhoud**: Workspace scope, out of scope, specifieke regels en beleidslijnen
- **Input voor**: Founding Hypothesis Agent (Fase A) - dit is het begin van het begin
- **Format**: `beleid-<workspace-naam>.md` (bijv. `beleid-standard.md`, `beleid-agent-capabilities.md`)
- **Locatie**: Altijd in `artefacten/0-governance/`

#### 3.2.3 Voor Agent-Capabilities Repository

**Structuur**: Agent-specifieke governance

```
artefacten/
└── 0-governance/
    └── capabilities-beleid.md         # Agent-capabilities specifiek beleid
```

**Rationale**:
- Minimale governance; verwijst primair naar standards repository
- Specifieke beleidsregels voor agent-capabilities indien nodig

### 3.3 Documentatie Folder — `/docs/`

**Doel**: Mensgerichte documentatie en visualisaties

**Structuur**: Georganiseerd per type content

```
docs/
├── architectuur/                      # Architectuurdocumentatie
│   ├── context-diagram.png
│   ├── container-diagram.png
│   └── solution-overview.md
├── diagrammen/                        # Visuele diagrammen
│   ├── data-flow.drawio
│   ├── process-flow.bpmn
│   └── entity-relationship.png
├── handleidingen/                     # Gebruikersdocumentatie
│   ├── installatie.md
│   ├── configuratie.md
│   └── gebruikers-handleiding.md
└── beslissingen/                      # ADR's en beslissingsdocumentatie
    ├── adr-001-technology-stack.md
    └── adr-002-api-design.md
```

**Verplichte Conventies**:
- ☑ **Mensgerichte content**: Geen ruwe agent-output
- ☑ **Visuele diagrammen**: PNG, SVG, of bewerkbare formaten (drawio, plantuml)
- ☑ **Markdown voor tekst**: Waar mogelijk markdown gebruiken

### 3.4 Scripts Folder — `/scripts/`

**Doel**: Automatiseringsscripts en tooling

**Structuur**: Georganiseerd per taal/platform

```
scripts/
├── powershell/                        # PowerShell scripts
│   ├── deploy.ps1
│   └── setup-environment.ps1
├── bash/                              # Bash scripts
│   ├── build.sh
│   └── test.sh
└── python/                            # Python scripts
    ├── data-migration.py
    └── validation.py
```

**Verplichte Conventies**:
- ☑ **Platform-specifieke folders**: Gescheiden per taal/platform
- ☑ **Executable permissions**: Scripts zijn uitvoerbaar
- ☑ **Documentatie**: Elke script heeft header-commentaar met doel en gebruik

### 3.5 Templates Folder — `/templates/`

**Doel**: Project-specifieke templates

**Structuur**: Georganiseerd per type template

```
templates/
├── issue-templates/                   # GitHub issue templates
│   ├── bug-report.md
│   └── feature-request.md
├── document-templates/                # Document templates
│   ├── adr-template.md
│   └── feature-template.md
└── code-templates/                    # Code scaffolding templates
    ├── controller.template.cs
    └── service.template.cs
```

**Verplichte Conventies**:
- ☑ **Herbruikbaar**: Templates zijn generiek en parameterizeerbaar
- ☑ **Gedocumenteerd**: Elk template heeft instructies

---

## 4. GitHub-specifieke Structuur — `/.github/`

### 4.1 Centrale Repositories (standards, agent-capabilities)

**Doel**: Agent-definities en GitHub-configuratie voor centrale eco-systeem repositories

```
.github/
├── agents/                            # Agent-definities (prompts als contracten)
│   ├── std.agent.a1.founding-hypothesis-owner.md
│   ├── std.agent.a2.business-case-analyst.md
│   ├── std.agent.b1.cdm-architect.md
│   └── ...
├── prompts/                           # Lichtgewicht activatie-verwijzingen
│   ├── std.agent.a1.founding-hypothesis-owner.md
│   ├── std.agent.a2.business-case-analyst.md
│   └── ...
├── workflows/                         # GitHub Actions workflows
│   ├── validate-charter.yml
│   └── test-agent.yml
├── ISSUE_TEMPLATE/                    # Issue templates
│   ├── bug-report.md
│   └── feature-request.md
├── PULL_REQUEST_TEMPLATE.md           # PR template
└── CODEOWNERS                         # Code ownership
```

**Naamgevingsconventie Agents**: `std.agent.<fase><nummer>.<naam>.md`

**Voorbeelden**:
- `std.agent.a1.founding-hypothesis-owner.md` — Fase A, agent 1
- `std.agent.b1.cdm-architect.md` — Fase B, agent 1
- `std.agent.u01.workspace-moeder.md` — Utility agent 01
- `std.agent.u90.make-agent.md` — Ecosysteem-bouwer agent 90

### 4.2 Project Workspaces

**Doel**: Minimale GitHub-configuratie, **GEEN agent-definities**

```
.github/
├── workflows/                         # OPTIONEEL: Project-specifieke workflows
│   ├── build.yml
│   └── deploy.yml
├── ISSUE_TEMPLATE/                    # OPTIONEEL: Issue templates
│   └── bug-report.md
└── PULL_REQUEST_TEMPLATE.md           # OPTIONEEL: PR template
```

**Verboden in Project Workspaces**:
- ❌ **GEEN** `.github/agents/` folder
- ❌ **GEEN** `.github/prompts/` folder
- ❌ **GEEN** agent-definities

**Rationale**: 
- Agent-definities blijven centraal beheerd
- Project workspaces blijven "schoon" en gefocust op artefacten
- Voorkomt duplicatie en inconsistentie

---

## 5. Verplichte Conventies

### 5.1 Naamgevingsconventies

#### 5.1.1 Bestanden

**Algemene Regel**: `<context>.<naam>.<extensie>`

**Specifieke Regels**:

| Context | Pattern | Voorbeeld |
|---------|---------|-----------|
| Artefacten | `<fase><nr>.<naam>.<ext>` | `a1.founding-hypothesis.md` |
| Beleid | `beleid-<workspace>.<ext>` | `beleid-standard.md` |
| Agent-definitie | `std.<fase><nr>.<naam>.agent.md` | `std.a1.founding-hypothesis-owner.agent.md` |
| Prompt-definitie | `std.<fase><nr>.<naam>.prompt.md` | `std.a1.founding-hypothesis-owner.prompt.md` |
| Charter | `std.agent.charter.<fase><nr>.<naam>.md` | `std.agent.charter.a1.founding-hypothesis-owner.md` |
| ADR | `<fase><nr>.adr-<volgnr>-<naam>.md` | `b2.adr-001-service-arch.md` |
| Template | `<naam>.template.<ext>` | `feature.template.md` |

**Verplichte Karakteristieken**:
- ☑ Lowercase
- ☑ Kebab-case voor woorden
- ☑ Geen spaties
- ☑ Betekenisvol
- ☑ Consistent met bovenstaande patterns

**Bijzondere Bestanden**:
- **Beleid-bestanden** (`beleid-<workspace>.md`):
  - Verantwoordelijkheid: Moeder Standard Agent
  - Locatie: `artefacten/0-governance/`
  - Inhoud: Workspace scope, out of scope, specifieke beleidsregels
  - Input voor: Founding Hypothesis Agent (Fase A)

#### 5.1.2 Folders

**Algemene Regel**: Lowercase, meervoud waar logisch

**Voorbeelden**:
- `artefacten/` (niet `artefact/` of `Artefacten/`)
- `docs/` (niet `documentation/`)
- `scripts/` (niet `script/`)
- `templates/` (niet `template/`)

### 5.2 Fase-nummering volgens SAFe

**Verplichte Nummering**:

| Fase | Letter | Range | Gebruik |
|------|--------|-------|---------|
| Governance | 0 | 0 | Governance-specifieke agents |
| Trigger | A | 1-99 | Initiatie, business cases |
| Architectuur | B | 1-99 | ADR's, architectuurkeuzes |
| Specificatie | C | 1-99 | Requirements, features |
| Ontwerp | D | 1-99 | API design, technisch ontwerp |
| Implementatie | E | 1-99 | Code, implementatie |
| Validatie | F | 1-99 | Tests, validatie |
| Deployment | G | 1-99 | Release, deployment |
| Utility | U | 01-89 | Gewone utilities |
| Utility | U | 90-99 | Ecosysteem-bouwers |

**Nummering binnen Fase**:
- Agents binnen fase krijgen oplopende nummers (1, 2, 3, ...)
- Utility agents gebruiken leading zero (01, 02, 03, ...)
- Ecosysteem-bouwers gebruiken 90-range (90, 91, 92, ...)

### 5.3 Markdown Standaarden

**Verplichte Markdown Conventies**:

- ☑ **Frontmatter**: Gebruik YAML frontmatter voor metadata waar relevant
- ☑ **Headers**: Gebruik ATX-style headers (`#`, `##`, `###`)
- ☑ **Code blocks**: Altijd met taal-specificatie (```yaml, ```powershell, etc.)
- ☑ **Links**: Gebruik relatieve links binnen workspace
- ☑ **Lijsten**: Consistente formatting (ordered voor stappen, unordered voor items)

**Voorbeeldstructuur**:
```markdown
# Document Titel

**Versie**: 1.0.0  
**Status**: Actief  
**Datum**: YYYY-MM-DD  

## 1. Sectie

Content...

### 1.1 Subsectie

Content...
```

### 5.4 Git Conventies

**Verplichte Git Regels**:

- ☑ **`.gitignore`**: Elke workspace heeft `.gitignore`
- ☑ **README.md**: Elke workspace heeft README.md met doel en structuur
- ☑ **Commit messages**: Conventionele commits (`feat:`, `fix:`, `docs:`, etc.)
- ☑ **Geen binaries**: Geen grote binaries in git (gebruik Git LFS indien nodig)

**`.gitignore` Minimale Template**:
```gitignore
# Operating System
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp

# Temporary files
*.tmp
*.temp
*.log

# Workspace logging
logs/

# Build outputs
bin/
obj/
dist/
build/
```

---

## 6. Interoperabiliteit: Wat Downstream Agents Mogen Verwachten

### 6.1 Voorspelbare Input-locaties

**Agents kunnen verwachten**:

1. **Trigger-input**: Altijd in `input/trigger.md` (voor eerste agent in pipeline)
2. **Artefacten**: Altijd in `/artefacten/` met fase-prefix
3. **Templates**: Altijd in `/templates/` indien aanwezig
4. **Governance**: Altijd in centrale `standards` repository

### 6.2 Consistente Output-formaten

**Agents produceren output volgens**:

1. **Fase-prefix**: Altijd `<fase><nr>.<naam>.<ext>`
2. **Markdown structuur**: Consistente headers en secties
3. **Metadata**: YAML frontmatter waar relevant
4. **Traceerbaarheid**: Output verwijst naar input-artefacten

### 6.3 Expliciete Contracts

**Agents declareren in hun charter**:

1. **Inputs**: Type, locatie, verplicht/optioneel
2. **Outputs**: Type, locatie, conditie
3. **Dependencies**: Welke agents/artefacten als input

**Voorbeeld uit charter**:
```markdown
### Verwachte Inputs
- **Conceptueel Datamodel**
  - Type: Markdown
  - Locatie: `artefacten/b1.cdm.md`
  - Bron: CDM Architect (Fase B)
  - Verplicht: Ja
```

---

## 7. Governance en Compliance

### 7.1 Verplichte Naleving

**Dit document is bindend**:
- Alle nieuwe workspaces **moeten** deze structuur volgen
- Bestaande workspaces **moeten** gemigreerd worden naar deze structuur
- Afwijkingen zijn **alleen** toegestaan met expliciete governance-goedkeuring

### 7.2 Validatie

**Workspaces worden gevalideerd op**:

- ☑ Aanwezigheid van verplichte folders (`artefacten/`, `docs/`)
- ☑ Naamgevingsconventies van artefacten
- ☑ Fase-prefixes volgens SAFe
- ☑ `.gitignore` en `README.md` aanwezig
- ☑ Geen verboden content in project workspaces (geen `.github/agents/`)

### 7.3 Verantwoordelijkheid

**Workspace Moeder Agent (u01)** is verantwoordelijk voor:
- Initiële setup van nieuwe workspaces volgens deze architectuur
- Validatie van workspace-structuur
- Migratie van bestaande workspaces
- Als **Git/GitHub expert** bewaken van workspace-specifieke git-structuur, branching-strategieën en aansluiting op de standards-repository.

---

## 8. Afwijkingen en Uitzonderingen

### 8.1 Procedure voor Afwijking

Wanneer een workspace moet afwijken van deze architectuur:

1. **Documenteer rationale**: Waarom is afwijking noodzakelijk?
2. **Minimale impact**: Wijzig alleen wat strikt noodzakelijk is
3. **Governance-goedkeuring**: Escaleer naar governance-eigenaar
4. **Documenteer afwijking**: In workspace README.md

### 8.2 Grandfathering

**Bestaande workspaces**:
- Mogen tijdelijk afwijken indien volledige migratie niet haalbaar is
- Moeten migratie-plan hebben
- Nieuwe artefacten volgen altijd nieuwe structuur

---

## 9. Relatie tot Andere Governance

### 9.1 Hiërarchie

**Rangorde bij conflict**:
1. **Constitutie** — Onveranderlijke basisregels
2. **Workspace Architectuur** (dit document) — Structurele normen
3. **Beleid** — Repository-specifieke regels
4. **Charters** — Agent-specifieke richtlijnen

### 9.2 Afstemming

Dit document **implementeert** en **detailleert** de vereisten uit:
- Constitutie Artikel 2 (Workspace Structuur)
- Beleid §4 (Documentstructuur)
- Beleid §5 (Artefact-creatie)

Voor repositories die uitsluitend documentatie bevatten (document-repositories, knowledge bases) geldt aanvullend de specifieke invulling in:
- artefacten/0-governance/workspace-standaard.md

---

## 10. Wijzigingslog

| Datum | Versie | Wijziging | Auteur |
|-------|--------|-----------|--------|
| 2026-01-09 | 1.0.0 | Initiële versie: normerend document voor workspace-architectuur, structuur, conventies en interoperabiliteit | Charter Schrijver |

---

## Bijlage A: Volledige Workspace Template

```
<workspace-root>/
├── artefacten/                        # Gegenereerde artefacten
│   ├── a1.founding-hypothesis.md
│   ├── b1.cdm.md
│   └── ...
├── docs/                              # Documentatie
│   ├── architectuur/
│   │   └── solution-overview.md
│   ├── diagrammen/
│   │   └── context-diagram.png
│   └── handleidingen/
│       └── gebruikers-handleiding.md
├── scripts/                           # Automatiseringsscripts
│   ├── powershell/
│   │   └── deploy.ps1
│   └── bash/
│       └── build.sh
├── templates/                         # Project templates
│   ├── issue-templates/
│   │   └── bug-report.md
│   └── document-templates/
│       └── adr-template.md
├── .github/                           # GitHub configuratie
│   ├── workflows/
│   │   └── build.yml
│   └── ISSUE_TEMPLATE/
│       └── bug-report.md
├── .gitignore                         # Git ignore regels
└── README.md                          # Workspace documentatie
```

**Voor standards Repository (Governance & Framework)**:
```
<workspace-root>/
├── artefacten/                        # Governance artefacten
│   ├── 0-governance/                  # Workspace-overstijgende standaarden
│   │   ├── constitutie.md
│   │   ├── workspace-architectuur.md
│   │   ├── beleid-standard.md                      # Workspace-specifiek beleid
│   │   ├── agent-charter-normering.md              # Normering voor agent-charters
│   │   └── delivery-framework.md
│   ├── 1-charter-application/         # Application charters
│   └── 2-charters-fases/              # SAFe fase charters
│       ├── std.fase.charter.a.trigger.md
│       └── ...
├── docs/                              # Eco-systeem documentatie
├── templates/                         # Charter templates
│   ├── agent.charter.template.md
│   └── phase.charter.template.md
├── governance/                        # Meta-agent charters (moeder, logos)
│   └── charters-agents/
│       ├── std.agent.charter.moeder-standard.md
│       └── std.agent.charter.charter-schrijver.md
├── desc-agents/                       # Agent-beschrijvingen (overzicht)
│   ├── moeder-standard-agent.md
│   └── charter-writer-agent.md
├── .github/                           # Meta-agent definities (minimaal)
│   ├── prompts/
│   │   ├── std.moeder-standard.prompt.md
│   │   └── std.charter-schrijver.prompt.md
│   └── workflows/
│       └── validate-charter.yml
├── .gitignore
└── README.md
```

**Voor agent-capabilities Repository (Agent Implementaties)**:
```
<workspace-root>/
├── artefacten/                        # Agent-specifieke governance
│   └── 0-governance/
│       └── capabilities-beleid.md     # Agent-capabilities specifiek beleid
├── governance/                        # Capability-agent charters
│   └── charters-agents/
│       ├── std.agent.charter.a1.founding-hypothesis-owner.md
│       ├── std.agent.charter.b1.cdm-architect.md
│       └── ...
├── desc-agents/                       # Agent-beschrijvingen (overzicht)
│   ├── a1.founding-hypothesis-owner-agent.md
│   ├── b1.cdm-architect-agent.md
│   └── ...
├── .github/                           # Capability-agent definities
│   ├── agents/
│   │   ├── std.a1.founding-hypothesis-owner.agent.md
│   │   ├── std.b1.cdm-architect.agent.md
│   │   └── ...
│   ├── prompts/
│   │   ├── std.a1.founding-hypothesis-owner.prompt.md
│   │   ├── std.b1.cdm-architect.prompt.md
│   │   └── ...
│   └── workflows/
│       └── test-agents.yml
├── .gitignore
└── README.md
```

**Belangrijk Onderscheid**:
- **standards**: Bevat meta-agents (moeder, charter-schrijver) en workspace-overstijgende standaarden
- **agent-capabilities**: Bevat capability-agents (fase-specifieke agents voor daadwerkelijk werk)
- **Governance-documenten** (artefacten/0-governance/): Workspace-overstijgende standaarden en principes
- **Agent-charters** (governance/charters-agents/): Charters van specifieke agents
