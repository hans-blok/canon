# Delivery framework — Development Value Stream

## Overzicht

Alle agents (behalve Logos) werken volgens het **SAFe (Scaled Agile Framework)** voor de development value stream. Dit framework beschrijft de complete flow van idee tot deployment en helpt agents hun positie in de workflow te begrijpen.

De development value stream is de reeks stappen die een organisatie gebruikt om waarde te leveren aan de klant, van het initiële concept tot de operationele software in productie.

## Development Value Stream Visualisatie

```
┌──────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────┐    ┌──────┐    ┌───────────┐    ┌────────────┐
│    A.    │───▶│      B.      │───▶│      C.      │───▶│    D.    │───▶│  E.  │───▶│     F.    │───▶│     G.     │
│ Trigger  │    │ Architectuur │    │ Specificatie │    │ Ontwerp  │    │ Bouw │    │ Validatie │    │ Deployment │
└──────────┘    └──────────────┘    └──────────────┘    └──────────┘    └──────┘    └───────────┘    └────────────┘
     ↓                  ↓                    ↓                  ↓             ↓              ↓                ↓
 Initiatie           ADR's           Requirements       Solution        Code          Tests          Release
 Business          Patterns           Features          Design       Generation     Validatie      Management
  Cases           Decisions          Datamodel         Contracts                                           
```

## Fases in Detail

### A. Trigger — Initiatie
**SAFe Fase**: Discovery, Opportunity Canvas
**Korte Beschrijving**: Initiatie, Business Cases

**Doel**: Identificeren van zakelijke behoeften en kansen, formuleren van business cases voor nieuwe initiatieven

**Kernactiviteiten**:
- Verzamelen van stakeholder input en feedback
- Identificeren van pijnpunten en verbeterkansen
- Formuleren van business cases
- Bepalen van de business value en ROI
- Prioriteren van initiatieven

**Artefacten**:
- Business cases en opportunity descriptions
- Stakeholder input en feedback
- Probleemomschrijvingen (problem statements)
- Waardevragen (value propositions)
- Initial backlog items

**SAFe Concepten**:
- **Hypothesis-Driven Development**: Start met een hypothese over waarde
- **Lean Business Case**: Lichtgewicht business case voor snelle go/no-go beslissingen
- **Economic Framework**: Gebruik economische principes voor prioritering

**Agents in deze fase**: Agents die business input verwerken, initiële analyse doen, requirements gathering

---

### B. Architectuur — Architect & Design Decisions
**SAFe Fase**: Architectural Runway, Enablers

**Doel**: Architecturale beslissingen vastleggen en technische fundamenten creëren

**Kernactiviteiten**:
- Definiëren van architectuurpatronen
- Nemen van strategische technische beslissingen
- Identificeren van architectuur enablers
- Vastleggen van technische constraints
- Bepalen van infrastructuur en platform keuzes

**Artefacten**:
- ADR's (Architecture Decision Records)
- Architectuurpatronen en -stijlen
- Technische richtlijnen en standaarden
- Infrastructuur en platform keuzes
- Non-functional requirements (NFR's)
- Technology stack definities

**SAFe Concepten**:
- **Architectural Runway**: Bestaande code, componenten en technische infrastructuur die toekomstige features ondersteunt
- **Enablers**: Architectuur, infrastructuur en compliance werk dat business features mogelijk maakt
- **Intentional Architecture**: Bewuste architecturale beslissingen die de business strategie ondersteunen

**Agents in deze fase**: Agents die architecturale beslissingen voorbereiden, ADR's opstellen, technische patterns documenteren

---

### C. Specificatie — Requirements Specification
**SAFe Fase**: Story Refinement, Specification, Backlog Refinement
**Korte Beschrijving**: Requirements, Features, Datamodel, Processen

**Doel**: Specificeren van requirements in detail, uitwerken van features, modelleren van data en processen zonder technische implementatiekeuzes

**Wat is Specificatie in SAFe?**

In SAFe is de Specification fase het moment waarop:
- **Requirements worden gedetailleerd** van hoog-niveau epics naar concrete, testbare user stories
- **Acceptance criteria worden gedefinieerd** zodat teams weten wanneer werk "done" is
- **Features worden uitgewerkt** met volledige functionaliteit beschreven op business-niveau
- **Datamodellen worden gecreëerd** die entiteiten, attributen en relaties beschrijven
- **Processen worden gedocumenteerd** die business flows en workflows vastleggen

**Belangrijk**: Deze fase blijft **technologie-agnostisch**. Er worden geen keuzes gemaakt over hoe iets gebouwd wordt, alleen over wat gebouwd moet worden.

**Kernactiviteiten**:
- **Story Refinement**: Backlog items verfijnen en uitwerken
- **Feature Elaboration**: Features uitwerken met volledige requirements
- **Acceptance Criteria definitie**: Testbare criteria voor elke story
- **Data Modeling**: Entiteiten, attributen, relaties identificeren
- **Process Mapping**: Business processen en workflows in kaart brengen
- **Scenario´s uitwerken**: Happy flows, alternatieve flows, edge cases
- **Dependencies identificeren**: Afhankelijkheden tussen stories/features
- **Definition of Ready**: Zorgen dat stories klaar zijn voor design/build

**Artefacten**:
- **Requirements Specificaties**: Volledige functionele en non-functionele eisen
- **User Stories**: Met INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- **Acceptance Criteria**: Testbare criteria per story (Given-When-Then format)
- **Feature Descriptions**: Uitgewerkte features met volledige scope
- **Datamodellen**: Entity-Relationship Diagrams, conceptuele datamodellen
- **Proces Flows**: Business process diagrams, swimlanes, activity diagrams
- **Use Cases**: Beschrijvingen van gebruikersinteracties met het systeem
- **Bounded Contexts**: Domain-Driven Design context mapping
- **NFR's**: Non-Functional Requirements (performance, security, etc.)

**SAFe Concepten**:
- **Backlog Refinement**: Iteratief proces om backlog items te verfijnen
- **Three Amigos**: Collaboration tussen Product Owner, Developer, en Tester bij story refinement
- **INVEST Criteria**: Stories moeten Independent, Negotiable, Valuable, Estimable, Small, Testable zijn
- **Definition of Ready (DoR)**: Criteria waaraan een story moet voldoen voordat deze opgepakt wordt
- **Built-In Quality**: Kwaliteit vanaf het begin inbouwen door heldere acceptance criteria
- **Behavior-Driven Development (BDD)**: Given-When-Then scenario's voor acceptance criteria
- **Story Splitting**: Grote stories opsplitsen in kleinere, waardevolle incrementen

**Verschil met Ontwerp (Fase D)**:
- **Specificatie (C)**: WAT moet het systeem doen (functioneel, business-gericht)
- **Ontwerp (D)**: HOE gaat het systeem het doen (technisch, solution-gericht)

Voorbeeld:
- Specificatie: "Gebruiker kan producten toevoegen aan winkelwagen"
- Ontwerp: "POST /api/cart endpoint met JSON body, Redis cache voor session"

**Agents in deze fase**: Agents die requirements specificeren, features uitwerken, datamodellen maken, processen documenteren, user stories schrijven

---

### D. Ontwerp — Functioneel & Technisch Ontwerp, Contract Design
**SAFe Fase**: Solution Design, Technical Design
**Korte Beschrijving**: Functioneel Ontwerp, Technisch Ontwerp, Contract Design

**Doel**: Functioneel ontwerp uitwerken, technische architectuur definiëren en API/interface contracten specificeren

**Kernactiviteiten**:
- Ontwerpen van API's en interfaces
- Definiëren van component interacties
- Uitwerken van technische designs
- Specificeren van data flows
- Maken van UX/UI designs

**Artefacten**:
- API designs en interface specificaties
- Component diagrammen en architectuur views
- Interaction designs en sequence diagrams
- Data flow diagrams
- UX wireframes en mockups
- Technical design documents

**SAFe Concepten**:
- **Set-Based Design**: Evalueer meerdere alternatieven parallel, converge naar beste oplossing
- **Design Thinking**: Gebruiker-centrische benadering van ontwerp
- **Emergent Design**: Design evolueert iteratief op basis van feedback

**Agents in deze fase**: Agents die technische ontwerpen maken, API's definiëren, componenten specificeren

---

### E. Bouw — Build & Implement
**SAFe Fase**: Implementation, Continuous Integration

**Doel**: Code generatie, implementatie en integratie

**Kernactiviteiten**:
- Genereren en schrijven van code
- Implementeren van features
- Creëren van database migraties
- Configureren van systemen
- Continuous integration

**Artefacten**:
- Gegenereerde en handgeschreven code
- Scripts en automation
- Database migraties en schema's
- Configuratiebestanden
- Build en deployment artifacts
- Integration tests

**SAFe Concepten**:
- **Continuous Integration (CI)**: Frequente integratie van code met automated builds en tests
- **Test-First Development**: Tests schrijven voor implementatie (TDD/BDD)
- **Collective Ownership**: Hele team is verantwoordelijk voor code kwaliteit
- **Small Batches**: Werk in kleine, frequente incrementen

**Agents in deze fase**: Agents die code genereren, scripts maken, implementatie automatiseren, CI/CD configureren

---

### F. Validatie — Verify & Validate
**SAFe Fase**: Testing, Verification, Validation

**Doel**: Testen, kwaliteitscontrole en validatie dat solution voldoet aan requirements

**Kernactiviteiten**:
- Uitvoeren van geautomatiseerde tests
- Valideren tegen acceptatiecriteria
- Performance en security testing
- Code reviews en quality checks
- Compliance verificatie

**Artefacten**:
- Test rapporten en resultaten
- Validatie resultaten en metrics
- Code review feedback
- Performance en security scan resultaten
- Compliance checklists
- Bug reports en defect logs

**SAFe Concepten**:
- **Built-In Quality**: Kwaliteit is onderdeel van iedere stap, niet een aparte fase
- **Test Automation**: Maximize automated testing voor snelle feedback
- **Definition of Done**: Valideer dat alle DoD criteria zijn behaald
- **Continuous Testing**: Testing door hele development cycle

**Agents in deze fase**: Agents die testen uitvoeren, kwaliteit valideren, security checks doen, compliance verificatie

---

### G. Deployment — Release & Deploy
**SAFe Fase**: Release on Demand, Deployment

**Doel**: Release management en deployment naar productie

**Kernactiviteiten**:
- Voorbereiden van releases
- Deployment naar verschillende omgevingen
- Release coordination en planning
- Monitoring en observability setup
- Rollback procedures

**Artefacten**:
- Release notes en documentation
- Deployment scripts en pipelines
- Rollback procedures
- Monitoring dashboards
- Runbooks en operational guides
- Post-deployment verification results

**SAFe Concepten**:
- **Release on Demand**: Ontkoppel deployment van release
- **Continuous Deployment (CD)**: Automated deployment naar productie
- **DevOps**: Samenwerking tussen development en operations
- **Blue-Green / Canary Deployments**: Veilige deployment strategieën
- **Feature Toggles**: Releases onafhankelijk van deployment
- Release notes
- Deployment scripts
- Rollback procedures
- Monitoring setup

**Agents in deze fase**: Agents die deployment voorbereiden, releases beheren, monitoring setup, operational support

---

### U. Utility — Supporting Services
**SAFe Concept**: Shared Services, Enablers

**Doel**: Generieke ondersteunende taken die niet direct in de lineaire workflow passen maar wel essentieel zijn voor de development value stream

**Kernactiviteiten**:
- Data transformatie en conversie
- Document generatie en formatting
- Code en template processing
- Cross-cutting utilities
- Herbruikbare helper functies

**Artefacten**:
- Format conversie tools (Markdown → XML, JSON → CSV, etc.)
- Gegenereerde documentatie
- Geformatteerde code
- Getransformeerde data
- Processing scripts

**Voorbeelden**:
- Markdown naar XML conversie voor Archi modellen
- JSON naar CSV transformatie voor rapportage
- Code formatting en linting
- Template instantiation
- Data cleaning en normalisatie

**SAFe Concepten**:
- **Shared Services**: Herbruikbare diensten die meerdere teams ondersteunen
- **Enablers**: Technische infrastructuur die features mogelijk maakt
- **Automation**: Automatiseer repetitieve taken voor efficiëntie

**Agents in deze fase**: Agents die format conversie, document generatie, data transformatie en andere ondersteunende taken uitvoeren

---

## SAFe Principes in de Development Value Stream

### 1. Take an Economic View
- Prioriteer werk op basis van economic value
- Gebruik Weighted Shortest Job First (WSJF) voor prioritering
- Minimaliseer cost of delay

### 2. Apply Systems Thinking
- Optimaliseer het gehele systeem, niet lokale optimalisaties
- Begrijp dependencies en interconnections
- Zie de value stream als één systeem

### 3. Assume Variability; Preserve Options
- Set-based design: evalueer meerdere opties
- Laatste verantwoordelijke moment voor beslissingen
- Empirische data boven aannames

### 4. Build Incrementally with Fast Feedback
- Kleine batches voor snelle feedback
- Frequent integreren en testen
- Iteratief leren en aanpassen

### 5. Base Milestones on Objective Evaluation
- Demo werkende oplossingen
- Data-driven besluitvorming
- Objectieve kwaliteitsmetrics

### 6. Visualize and Limit WIP
- Maak werk zichtbaar (Kanban boards)
- Limiteer Work in Progress
- Identificeer en verwijder bottlenecks

### 7. Apply Cadence, Synchronize with Cross-Domain Planning
- Voorspelbare planning cycles
- Synchronisatie tussen teams
- Program Increment (PI) Planning

### 8. Unlock Intrinsic Motivation
- Autonomie, Meesterschap, Purpose
- Self-organizing teams
- Continuous learning culture

### 9. Decentralize Decision-Making
- Push beslissingen naar lagere niveaus
- Snelle, lokale beslissingen waar mogelijk
- Strategische beslissingen centraal

### 10. Organize Around Value
- Value streams als organisatie-eenheid
- End-to-end verantwoordelijkheid
- Focus op customer outcomes

---

## Agent Positionering

### Moeder-Agent Verantwoordelijkheid

De **moeder-agent** plaatst elke nieuwe agent in een fase van de workflow:

1. **Agent creatie**: Moeder-agent vraagt om:
   - Naam van de agent
   - Domein van de agent
   - Context (wat doet de agent)

2. **Fase bepaling**: Op basis van de agent-context bepaalt de moeder-agent in welke fase de agent hoort

3. **Folder structuur**: Artefacten worden geplaatst in artefacten-folders:
   ```
   /artefacten/
       /a.trigger/
       /b.architectuur/
       /c.specificatie/
       /d.ontwerp/
       /e.bouw/
       /f.validatie/
       /g.deployment/
       /u.utility/
   ```

   **Agent bestanden blijven in de standards repository**:
   ```
   standards/
   ├── .github/agents/
   │   └── std.<fase>.<naam>.agent.md
   ├── .github/prompts/
   │   └── std.<fase>.<naam>.prompt.md
   └── charters.agents/<fase>/
       └── std.agent.charter.<fase>.<naam>.md
   ```

4. **Autonome plaatsing**: De moeder-agent neemt deze beslissing zelfstandig op basis van de agent-context

### Agent Naamgeving

**Formaat**: `std.<fase>.<agent-naam>`

**Voorbeelden**:
- `std.c.specificeer` — Specificatie agent
- `std.e.genereer` — Code generatie agent
- `std.u.convert` — Utility conversie agent
- `std.b.adr` — Architectuur beslissing agent

**Fase-letters (lowercase)**:
- `a` = Trigger
- `b` = Architectuur
- `c` = Specificatie
- `d` = Ontwerp
- `e` = Bouw
- `f` = Validatie
- `g` = Deployment
- `u` = Utility

### Agent Bestanden

Voor een agent genaamd `std.c.specificeer`:

**In standards repository**:
```
/.github/agents/std.c.specificeer.agent.md
/.github/prompts/std.c.specificeer.prompt.md
/charters.agents/c.specificatie/std.agent.charter.c.specificeer.md
/desc-agents/specificeer-agent.md
```

**In project-workspace** (artefacten):
```
/artefacten/c.specificatie/requirements.md
/artefacten/c.specificatie/user-stories.md
```

---



## Framework Evolutie

- Dit framework mag worden aangepast via expliciet updateproces
- Alleen de gebruiker mag het framework wijzigen
- Agents volgen het framework, maar mogen geen wijzigingen aanbrengen
- Bij onduidelijkheden meldt de agent dit aan de gebruiker

---

**Versie**: 1.0.0  
**Laatst Bijgewerkt**: 2025-12-13
