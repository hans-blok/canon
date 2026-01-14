# Phase Charter — Specificatie

**Doctrine IT Development**: doctrine-it-development.md  
**Phase Identifier**: standards.charter.phase.specificatie  
**Version**: 3.1.0  
**Status**: Active  
**Last Updated**: 2026-01-07  
**Owner**: Architecture & AI Enablement

---

## 1. Doel en Positionering

### Doel van de Fase
De **Specificatie-fase** (Requirements Specification in SAFe) transformeert zakelijke behoeften en architecturale kaders in ondubbelzinnige, testbare en **technologie-agnostische** specificaties. Deze fase beschrijft **WAT** het systeem moet doen, zonder te definiëren **HOE** het gebouwd wordt. Het einddoel is een volledige, consistente specificatie met uitgewerkte features, datamodellen en processen die als contractuele basis dient voor de ontwerpfase.

**Kernverschil met Ontwerp (Fase D)**:
- **Specificatie (C)**: WAT moet het systeem doen (functioneel, business-gericht, technologie-agnostisch)
- **Ontwerp (D)**: HOE gaat het systeem het doen (technisch, solution-gericht, implementatie-keuzes)

**Voorbeeld**:
- Specificatie: "Gebruiker kan producten toevoegen aan winkelwagen met maximaal 50 items"
- Ontwerp: "POST /api/cart endpoint met JSON body, Redis cache voor session, 5 min TTL"

### Plaats in het Delivery Framework
- **Voorgaande fase**: B. Architectuur — Architect & Design Decisions
- **Volgende fase**: D. Ontwerp — Functioneel & Technisch Ontwerp, Contract Design
- **Beslissend moment**: Go / No-go op basis van compleetheid, testbaarheid en technologie-agnosticisme

Deze fase is een expliciete **kwaliteits- en beslissingsstep**, geen doorgeefluik. Onvolledige of technisch-gekleurde specificaties worden niet doorgegeven.

---

## 2. Fase-doelstellingen

De fase is succesvol afgerond wanneer:
- Alle functionele en non-functionele requirements zijn ondubbelzinnig, testbaar en **technologie-agnostisch** geformuleerd
- **User Stories** voldoen aan INVEST-criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- **Acceptance Criteria** zijn gedefinieerd in Given-When-Then formaat (BDD-stijl)
- **Features** zijn volledig uitgewerkt met scope, value proposition en prioritering
- **Datamodel** beschrijft entiteiten, attributen, relaties zonder technische implementatie-details
- **Processen** zijn gedocumenteerd met business flows, beslispunten en actoren
- Alle stories voldoen aan **Definition of Ready (DoR)** voor design/build
- User stories dekken alle primaire en secundaire gebruikersstromen met scenario's
- Maximaal drie kritieke verduidelijkingsvragen zijn geïdentificeerd voor stakeholder-input
- Alle aannames en afhankelijkheden zijn expliciet gedocumenteerd
- Bounded contexts en domeinafbakening zijn helder gedefinieerd (waar relevant)
- **Geen technische termen** zoals API's, endpoints, databases, frameworks in specificaties

Doelen zijn **toetsbaar, expliciet en herhaalbaar**.

---

## 3. Scope en Grenzen

### Binnen Scope (DOET WEL)
- **Story Refinement**: Backlog items verfijnen van epics naar user stories
- **Feature Elaboration**: Features volledig uitwerken met requirements en scope
- **Acceptance Criteria definitie**: Testbare criteria per story (Given-When-Then)
- **Data Modeling**: Conceptuele datamodellen, entiteiten, attributen, relaties
- **Process Mapping**: Business processen, workflows, swimlanes, beslisbomen
- **Scenario uitwerking**: Happy flows, alternatieve flows, edge cases, error handling
- **Definition of Ready**: Zorgen dat stories klaar zijn voor design-fase
- Definiëren van functionele requirements (wat het systeem moet doen)
- Definiëren van non-functionele requirements (kwaliteitseisen, performance targets)
- Schrijven van use cases en gebruikersscenario's
- Documenteren van aannames en afhankelijkheden
- Afbakenen van feature scope (inclusief en exclusief gedrag)
- Definiëren van bounded contexts binnen het domein (DDD)
- Valideren van requirements op testbaarheid en ondubbelzinnigheid
- **Story Splitting**: Grote stories opsplitsen in kleinere, waardevolle incrementen

### Buiten Scope (DOET NIET)
- Technische implementatiekeuzes (talen, frameworks, databases)
- Contract design of technische interfaces (dat is fase D)
- API-design of service-contracten (dat is fase D)
- Functioneel of technisch ontwerp (dat is fase D)
- Architectuurbeslissingen (die komen uit fase B)
- Code-structuur of technische detaillering
- Deployment-strategieën
- Specifieke tooling-keuzes
- Het al implementeren of bouwen van features
- Geschatte effort of planning (tenzij expliciet gevraagd)

---

## 4. Entry Criteria (Input Quality Gate)

Deze fase mag **alleen starten** als aan alle onderstaande criteria is voldaan:
- ☐ Business case of initiatie is beschikbaar vanuit fase A (Trigger - Initiatie)
- ☐ Relevante ADR's en architecturale beslissingen zijn beschikbaar vanuit fase B (Architectuur)
- ☐ Technische constraints en non-functionele richtlijnen zijn gedocumenteerd
- ☐ Stakeholders en doelgroep zijn geïdentificeerd
- ☐ Openstaande architecturale issues zijn expliciet gelabeld

### Vereiste Inputs

| Artefact | Herkomst | Minimale Kwaliteitseis |
|----------|----------|------------------------|
| Business case / initiatie | Fase A (Trigger - Initiatie) | Helder geformuleerde klantwaarde en pijnpunt |
| ADR's (Architecture Decision Records) | Fase B (Architectuur) | Relevante technische kaders en constraints |
| Architectuurpatronen | Fase B (Architectuur) | Vastgestelde patterns en standaarden |
| Non-functional requirements (basis) | Fase B (Architectuur) | Performance, security, compliance kaders |
| Stakeholder-input | Fase A (Trigger - Initiatie) | Geïdentificeerde gebruikersgroepen en behoeften |

---

## 5. Activiteiten en Methoden

### Kernactiviteiten
- **Backlog Refinement**: Iteratief verfijnen van backlog items met team
- **Story Refinement**: Backlog items uitwerken en opsplitsen naar user stories
- **Feature Elaboration**: Features uitwerken met volledige requirements en scope
- **Acceptance Criteria definitie**: Testbare criteria formuleren (Given-When-Then)
- **Data Modeling**: Conceptuele datamodellen maken, entiteiten en relaties identificeren
- **Process Mapping**: Business processen en workflows in kaart brengen
- **Scenario uitwerking**: Happy flows, alternatieve flows, edge cases documenteren
- **Dependencies identificeren**: Afhankelijkheden tussen stories en features vastleggen
- **Three Amigos sessies**: Collaboration tussen Product Owner, Developer en Tester
- **Definition of Ready check**: Valideren dat stories klaar zijn voor design/build
- **Story Splitting**: Grote stories opsplitsen in kleinere, waardevolle incrementen
- **Kwaliteitsvalidatie**: Controleren op testbaarheid, ondubbelzinnigheid en technologie-agnosticisme
- **Aannames documentatie**: Expliciet vastleggen van aannames en verduidelijkingsvragen
- **User story writing**: Formuleren van user stories met acceptatiecriteria
- **Scenario definitie**: Uitwerken van primaire en alternatieve gebruikersstromen
- **Kwaliteitsvalidatie**: Controleren op testbaarheid, ondubbelzinnigheid en volledigheid
- **Aannames documentatie**: Expliciet vastleggen van aannames en verduidelijkingsvragen
- **Bounded context mapping**: Afbakenen van domeingrenzen (waar relevant)

### Methoden en Referenties
- **Kwaliteitseisen voor Specificaties** (`governance/kwaliteitseisen-specificaties.md`)
- **Yourdon-achtige data modeling**: Entity-relationship modeling
- **Domain-Driven Design (DDD)**: Bounded contexts, ubiquitous language
- **Gherkin-stijl scenario's**: Given-When-Then voor acceptatiecriteria
- **Regel- en datagedreven analyse** boven implementatie

Focus: **begrip en beslisbaarheid**, niet snelheid.

---

## 6. Rollen en Verantwoordelijkheden

| Rol | Verantwoordelijkheid | Beslisrecht |
|-----|----------------------|-------------|
| Product Owner | Valideren van requirements tegen business value | Go/No-go op feature scope |
| Business Analyst | Vertalen van business needs naar requirements | Formulering van requirements |
| Domain Expert | Valideren van domeinlogica en business rules | Correctheid van domeinregels |
| Architect | Valideren van architecturale consistentie | Technische haalbaarheid binnen kaders |
| Agents | Genereren en valideren van specificatie-artefacten | Kwaliteit en volledigheid binnen fase-scope |

Menselijke rollen blijven eindverantwoordelijk voor validatie en goedkeuring.

---

## 7. Outputs en Exit Criteria

### Geleverde Outputs
- **Requirements Specificaties**: Volledige functionele en non-functionele eisen (technologie-agnostisch)
- **User Stories**: Voldoen aan INVEST-criteria met volledige beschrijving
- **Acceptance Criteria**: Testbare criteria per story in Given-When-Then formaat (BDD)
- **Feature Descriptions**: Uitgewerkte features met scope en value proposition
- **Datamodellen**: Conceptuele entity-relationship diagrams zonder technische implementatie
- **Proces Flows**: Business process diagrams, swimlanes, activity diagrams
- **Use Cases**: Beschrijvingen van gebruikersinteracties met primaire en alternatieve flows
- **Scenario's**: Happy flows, edge cases, error handling beschrijvingen
- **Bounded Contexts**: Domain-Driven Design context mapping (waar relevant)
- **NFR's**: Non-Functional Requirements (performance targets, security eisen, compliance)
- **Aannames en Afhankelijkheden**: Expliciet gedocumenteerd
- **Verduidelijkingsvragen**: Maximaal 3 kritieke vragen voor stakeholders
- **Definition of Ready Checklist**: Per story/feature

### Exit Criteria (Phase Quality Gate)

De fase is pas afgerond wanneer:
- ☐ Alle requirements zijn ondubbelzinnig, testbaar en **strikt technologie-agnostisch**
- ☐ User stories voldoen aan **INVEST-criteria**
- ☐ Acceptance criteria zijn geformuleerd in **Given-When-Then formaat**
- ☐ Alle stories voldoen aan **Definition of Ready (DoR)**
- ☐ Processen zijn volledig gedocumenteerd met actoren en beslispunten
- ☐ Features zijn uitgewerkt met volledige scope en acceptance criteria
- ☐ Datamodel is compleet en consistent (zonder technische implementatie-keuzes)
- ☐ Geen [VERDUIDELIJKING NODIG] markeringen over (of maximaal 3 kritieke vragen)
- ☐ **Geen technische termen** zoals API, endpoint, database, framework in specificaties
- ☐ Succescriteria zijn meetbaar en gebruikersgericht (niet systeem-intern)
- ☐ Scope is helder afgebakend (inclusief en exclusief gedrag)
- ☐ Traceerbaarheid naar business case en ADR's is aantoonbaar
- ☐ Kwaliteitschecklist uit `kwaliteitseisen-specificaties.md` is volledig afgevinkt
- ☐ **Three Amigos reviews** zijn uitgevoerd voor kritieke stories

---

## 8. Kwaliteitsprincipes

Deze fase committeert zich aan de principes uit het **Application Charter** en specificeert deze als volgt:

### Fase-specifieke Principes
- **Ondubbelzinnigheid**: Elke requirement heeft één mogelijke interpretatie
- **Testbaarheid**: Alle requirements zijn verifieerbaar zonder implementatiekennis
- **INVEST Stories**: User stories zijn Independent, Negotiable, Valuable, Estimable, Small, Testable
- **Definition of Ready**: Stories zijn klaar voor design-fase voordat ze doorgegeven worden
- **Volledigheid boven snelheid**: Geen half-ingevulde requirements
- **Gebruikersgericht**: Requirements beschrijven waarde voor eindgebruikers, niet systeem-internals
- **Consistente terminologie**: Uniform taalgebruik door hele specificatie (ubiquitous language)

### Cross-fase Principes (Application Charter)
- **Fasezuiverheid**: Deze fase levert uitsluitend functionele en non-functionele requirements, datamodellen en processen. Technisch ontwerp (fase D), architecturale beslissingen (fase B), en implementatie (fase E) zijn expliciet buiten scope.
- **Technologie-agnostisch**: Deze fase maakt GEEN technische keuzes. Geen vermelding van frameworks, talen, databases, API's of tools. Implementatiedetails zijn verboden.
- **Traceerbaarheid**: Alle requirements zijn traceerbaar naar founding hypothesis (fase A) en architectuurkaders (fase B). Downstream fases (D, E) bouwen voort op deze specificaties.
- **Expliciete aannames**: Maximaal 3 kritieke verduidelijkingen tegelijk, altijd gemarkeerd (zie Constitutie Art. 4). Rest met redelijke standaarden.
- **Built-in Quality**: Kwaliteit vanaf het begin door heldere acceptance criteria en testbare requirements.
- **Quality First**: Kwaliteit gaat boven snelheid — geen half-ingevulde requirements worden doorgegeven.

"Niet zeker" is beter dan "stilzwijgend fout".  
"WAT" is gescheiden van "HOE".

---

## 9. Anti-Patterns

In deze fase is het expliciet verboden om:
- **Technische implementatie-details** te specificeren (frameworks, databases, API's, endpoints)
- **Contract designs** of API-specificaties te maken (dat is fase D)
- **Functionele of technische ontwerpen** uit te werken (dat is fase D)
- **Solution architectuur** te beschrijven (hoe iets gebouwd wordt)
- Technische oplossingen voor te schrijven in plaats van behoeften te beschrijven
- Onvolledige requirements als "work in progress" door te geven
- Meer dan 3 [VERDUIDELIJKING NODIG] markeringen te hanteren
- Vage of niet-testbare acceptatiecriteria te formuleren
- Stories door te geven die niet voldoen aan **INVEST-criteria**
- Stories door te geven zonder **Definition of Ready** check
- Aannames stil te houden zonder documentatie
- Scope te laten uitdijen zonder expliciete beslissing
- Requirements te schrijven voor ontwikkelaars in plaats van stakeholders
- Conflicten tussen requirements te verbergen of glad te strijken
- **Technische jargon** te gebruiken (REST, JSON, Redis, PostgreSQL, etc.)

---

## 10. Samenhang met Agents

**Principe**: Agents kunnen bijdragen aan deze fase,
maar mogen deze fase nooit zelfstandig afronden
of een exit-beslissing nemen.

Fase-afsluiting en exit-beslissingen blijven altijd menselijke verantwoordelijkheid.

### Ondersteunende Agents
- **Charter Schrijver Agent**: Schrijft phase charters en agent charters volgens SAFe
- **Story Refinement Agents** (indien beschikbaar): Ondersteunen bij story splitting en INVEST-validatie
- **Data Modeling Agents** (indien beschikbaar): Ondersteunen bij conceptuele datamodellen
- **Process Mapping Agents** (indien beschikbaar): Ondersteunen bij business process documentatie
- **Validation Agents** (indien beschikbaar): Controleren op technologie-agnosticisme en testbaarheid

### Afhankelijke Fases / Agents
- **Fase D (Ontwerp)**: Consumeert requirements voor functioneel & technisch ontwerp en contract design
- **Fase E (Bouw)**: Gebruikt requirements als contractuele basis voor implementatie
- **Fase F (Validatie)**: Gebruikt acceptatiecriteria als testbasis

---

## 11. Niet-Doelen

Expliciete opsomming van zaken die *niet* worden nagestreefd in deze fase:
- Het maken van contract designs of API-specificaties (dat is fase D)
- Het uitwerken van functionele of technische ontwerpen (dat is fase D)
- Het optimaliseren van technische performance (dat is fase D)
- Het nemen van architectuurbeslissingen (dat is fase B)
- Het schatten van development effort (tenzij expliciet gevraagd)
- Het prioriteren van backlog items (dat is Product Owner verantwoordelijkheid)
- Het voorschrijven van UI/UX designs (dat is fase D)
- Het maken van implementatie-keuzes
- Het volledig elimineren van alle onzekerheden (maximaal 3 kritieke vragen zijn toegestaan)

---

## 12. Wijzigingslog

| Datum | Versie | Wijziging | Auteur |
|-------|--------|-----------|--------|
| 2026-01-07 | 3.1.0 | Toegevoegd: Cross-fase principes (Fasezuiverheid, Technologie-agnostisch, Traceerbaarheid, Built-in Quality, Quality First) uit Application Charter; verwijderd duplicatie 'max 3 aannames' (verwijst naar Constitutie) | GitHub Copilot |
| 2025-12-14 | 3.0.0 | Volledig herschreven volgens SAFe Specification fase met INVEST, DoR, Three Amigos | Charter Schrijver Agent |
| 2025-12-14 | 2.0.0 | Herschreven conform nieuw delivery framework: Requirements i.p.v. Specificatie, toegevoegd proces & features | Charter Schrijver Agent |
| 2025-12-14 | 1.0.0 | Initiële versie gebaseerd op kwaliteitseisen-specificaties.md | Charter Schrijver Agent |
