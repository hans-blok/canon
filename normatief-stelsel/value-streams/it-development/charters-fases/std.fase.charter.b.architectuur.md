# Phase Charter — Architectuur

**Doctrine IT Development**: doctrine-it-development.md  
**Phase Identifier**: standards.charter.phase.b.architectuur  
**Version**: 1.1.0  
**Status**: Active  
**Last Updated**: 2026-01-07  
**Owner**: Architecture & AI Enablement

---

## 1. Doel en Positionering

### Doel van de Fase
De **Architectuur-fase** (Architectural Runway & Enablers in SAFe) transformeert de founding hypothesis en business case uit Fase A in strategische technische beslissingen, architectuurpatronen en technische fundamenten. Deze fase beschrijft **HOE** het systeem technisch gefundeerd wordt zonder al het detail van het ontwerp (dat is Fase D). Het einddoel is een **5-regels prompt** waarmee agents de volledige applicatie kunnen bouwen, ondersteund door een architecturale runway die toekomstige features ondersteunt en technische risico's mitigeert.

**Kernverschil met Ontwerp (Fase D)**:
- **Architectuur (B)**: Strategische technische beslissingen, patterns, frameworks, infrastructuur
- **Ontwerp (D)**: Gedetailleerd technisch ontwerp van specifieke features, API-contracten, componenten

**Voorbeeld**:
- Architectuur: "We hanteren een hybride REST architectuur met Resource APIs (CRUD) en Function APIs (acties)"
- Ontwerp: "POST /api/orders/{id}/confirm endpoint met JSON schema X en validatieregels Y"

### Plaats in het Delivery Framework
- **Voorgaande fase**: A. Trigger — Initiatie
- **Volgende fase**: C. Specificatie — Requirements Specification
- **Beslissend moment**: Go / No-go op basis van architecturale haalbaarheid, technische risico's en NFR-compliance

Deze fase is een expliciete **kwaliteits- en beslissingsstep**, geen doorgeefluik. Architecturaal onhaalbare of niet-onderbouwde initiatieven worden niet doorgegeven.

---

## 2. Fase-doelstellingen

De fase is succesvol afgerond wanneer:
- **Architecture Decision Records (ADR's)** documenteren alle strategische technische beslissingen
- **Architectuurpatronen** zijn gedefinieerd (service architectuur, API-stijl, data patterns)
- **Conceptueel Datamodel (CDM)** beschrijft de kernconcepten en hun relaties
- **Bounded Contexts** zijn geïdentificeerd volgens Domain-Driven Design
- **Non-Functional Requirements (NFR's)** zijn gedocumenteerd (performance, security, compliance)
- **Technology Stack** is bepaald (frameworks, platforms, tooling)
- **Infrastructuur keuzes** zijn vastgelegd (cloud, containerization, etc.)
- **Architectural Runway** is gecreëerd voor toekomstige features
- **Enablers** zijn geïdentificeerd (technisch werk voor architectuur, infrastructuur, compliance)
- **Technische risico's** zijn geïdentificeerd en gemitigeerd
- Alle beslissingen zijn **onderbouwd** en **traceerbaar** naar founding hypothesis en NFR's
- **Architectuur compliance** is geborgd (binnen organisatorische standaarden)
- **5-regels prompt** is geformuleerd waarmee agents de applicatie kunnen bouwen

Doelen zijn **toetsbaar, expliciet en herhaalbaar**.

---

## 3. Scope en Grenzen

### Binnen Scope (DOET WEL)
- **ADR's schrijven**: Architecture Decision Records voor strategische technische beslissingen
- **Architectuurpatronen definiëren**: Service architectuur, API-stijl, messaging patterns, data patterns
- **Conceptueel Datamodel maken**: Kernconcepten, entiteiten, relaties (high-level, niet gedetailleerd)
- **Bounded Contexts identificeren**: DDD-contexts en context mapping
- **NFR's documenteren**: Performance, security, scalability, reliability, compliance kaders
- **Technology Stack bepalen**: Frameworks, platforms, programmeertalen, databases
- **Infrastructuur keuzes**: Cloud providers, containerization, orchestration
- **Architecturale standaarden**: Coding standards, security practices, observability patterns
- **Enablers identificeren**: Technisch werk dat features mogelijk maakt
- **Technische risico's**: Identificeren en mitigation strategieën
- **Architectural Runway**: Fundament voor toekomstige features
- **Intentional Architecture**: Bewuste architecturale keuzes aligned met business strategie
- **Service Types definiëren**: Entity, Task, Orchestration, Rule, Utility services

### Buiten Scope (DOET NIET)
- **Gedetailleerd API-ontwerp**: Geen specifieke endpoints, JSON schemas, validaties (dat is fase D)
- **Feature-specificatie**: Geen requirements of user stories (dat is fase C)
- **Logisch Datamodel (LDM)**: Geen gedetailleerde tabellen, kolommen, indices (dat is fase D)
- **Implementatie**: Geen code of configuratie (dat is fase E)
- **Release planning**: Geen deployment strategieën (dat is fase G)
- Gedetailleerde component design (dat is fase D)
- Test strategieën (dat is fase F met input van deze fase)
- Operationele procedures (dat is fase G)

---

## 4. Entry Criteria (Input Quality Gate)

Deze fase mag **alleen starten** als aan alle onderstaande criteria is voldaan:
- ☐ **Founding Hypothesis** is gevalideerd en goedgekeurd (uit Fase A)
- ☐ **Business Case** is goedgekeurd door stakeholders (uit Fase A)
- ☐ **Target Audience** en **Value Proposition** zijn helder (uit Fase A)
- ☐ **5-regels Prompt** is beschikbaar (uit Fase A)
- ☐ **Initial Backlog** met high-level epics is beschikbaar (uit Fase A)
- ☐ **Go-beslissing** is genomen om door te gaan naar architectuur
- ☐ **Stakeholder commitment** is aanwezig voor architectuur-investeringen

### Vereiste Inputs

| Artefact | Herkomst | Minimale Kwaliteitseis |
|----------|----------|------------------------|
| Founding Hypothesis | Fase A | Volledige hypothesis volgens Knapp-methodologie |
| Business Case | Fase A | Goedgekeurde business case met ROI en risico's |
| Initial Backlog | Fase A | Minimaal 3-5 high-level epics |
| Value Proposition | Fase A | Unieke waarde en competitief voordeel |
| Target Audience | Fase A | Beschrijving van primaire gebruikersgroepen |

---

## 5. Activiteiten en Methoden

### Kernactiviteiten
1. **Architectuurverkenning**: Analyseren van founding hypothesis en business case voor architecturale implicaties
2. **ADR's schrijven**: Documenteren van architecturale beslissingen met context, opties en rationale
3. **Patronen selecteren**: Kiezen van architectuurpatronen (service architectuur, messaging, data)
4. **Conceptueel Datamodel**: Identificeren van kernconcepten en hun relaties
5. **Bounded Context Mapping**: DDD-analyse en context afbakening
6. **NFR's definiëren**: Performance targets, security requirements, compliance eisen
7. **Technology Stack bepalen**: Frameworks, platforms, tooling selecteren
8. **Infrastructuur ontwerp**: Cloud, containerization, orchestration beslissingen
9. **Enablers identificeren**: Technisch werk voor architectuur en infrastructuur
10. **Risico-analyse**: Technische risico's identificeren en mitigation bepalen
11. **Architectuur validatie**: Haalbaarheidscheck en proof-of-concepts waar nodig
12. **5-regels Prompt formuleren**: Korte, krachtige prompt (max 5 regels) waarmee agents de applicatie kunnen bouwen
13. **Documentatie**: Alle beslissingen traceerbaar documenteren

### Methoden en Referenties
- **Architecture Decision Records (ADR)**: Structured format voor architecturale beslissingen
- **Domain-Driven Design (DDD)**: Bounded contexts, ubiquitous language, context mapping
- **SOA Methodologie (Thomas Erl)**: Service types (Entity, Task, Utility)
- **Arcitura SOA Patterns**: [https://patterns.arcitura.com/soa-patterns](https://patterns.arcitura.com/soa-patterns)
- **Hybride REST Architectuur**: Resource APIs (CRUD) vs Function APIs (acties)
- **C4 Model**: Context, Container, Component, Code diagrams
- **Architectural Runway (SAFe)**: Intentional architecture voor toekomstige features
- **Quality Attribute Scenarios**: Voor NFR-definitie en validatie
- **TLX Service Architectuur**: Entity (E), Task (T), Orchestration (O), Rule (R), Utility (U)

Focus: **strategische beslissingen en architecturale runway**, niet detail.

---

## 6. Rollen en Verantwoordelijkheden

| Rol | Verantwoordelijkheid | Beslisrecht |
|-----|----------------------|-------------|
| Enterprise Architect | Bewaken van consistentie met organisatie-architectuur | Architecturale standaarden en compliance |
| Solution Architect | Definiëren van solution architectuur | Architectuurpatronen en technology stack |
| Domain Architect | Bounded contexts en domeinmodellering | Conceptueel datamodel en DDD-keuzes |
| Security Architect | Security requirements en patterns | Security NFR's en compliance |
| CDM Architect Agent | Genereren van conceptueel datamodel | Structuur van CDM binnen architecturale kaders |
| Agents (algemeen) | Ondersteunen bij ADR's en documentatie | Kwaliteit van artefacten binnen fase-scope |

**Menselijke architecten blijven eindverantwoordelijk** — agents ondersteunen, maar architecten beslissen.

---

## 7. Outputs en Exit Criteria

### Geleverde Outputs
1. **Architecture Decision Records (ADR's)**:
   - Context en probleem
   - Overwogen opties
   - Gekozen oplossing en rationale
   - Consequenties en trade-offs

2. **Architectuurpatronen Documentatie**:
   - Service architectuur (Entity, Task, Orchestration, Rule, Utility)
   - API-stijl (Resource APIs vs Function APIs)
   - Messaging patterns
   - Data patterns
   - Security patterns

3. **Conceptueel Datamodel (CDM)**:
   - Kernconcepten en entiteiten
   - Relaties tussen concepten
   - Bounded contexts
   - Ubiquitous language per context

4. **Non-Functional Requirements (NFR's)**:
   - Performance targets (latency, throughput)
   - Security requirements (authentication, authorization, encryption)
   - Scalability requirements
   - Reliability en availability targets
   - Compliance eisen (GDPR, ISO, etc.)

5. **Technology Stack Documentatie**:
   - Frameworks en libraries
   - Platforms en runtime environments
   - Databases en data stores
   - Monitoring en observability tools

6. **Infrastructuur Architectuur**:
   - Cloud provider keuzes
   - Containerization strategie
   - Orchestration platform
   - Netwerk topologie
   - Security zones

7. **Enablers Backlog**:
   - Technisch werk voor architectuur
   - Infrastructuur setup
   - Compliance implementaties

8. **Risico-analyse en Mitigation**:
   - Geïdentificeerde technische risico's
   - Mitigation strategieën
   - Contingency plans

9. **Architectuur Compliance Report**:
   - Afstemming met organisatie-standaarden
   - Afwijkingen en rationale

10. **5-Regels Prompt**:
   - Korte, krachtige prompt (max 5 regels)
   - Integreert founding hypothesis, architectuurpatronen en technische keuzes
   - Waarmee agents autonom de volledige applicatie kunnen bouwen
   - Bevat essentiële architecturale context en richting

### Exit Criteria (Phase Quality Gate)

De fase is pas afgerond wanneer:
- ☑ Minimaal 5 strategische ADR's zijn gedocumenteerd
- ☑ Service architectuur is gedefinieerd (E/T/O/R/U types)
- ☑ API-stijl is vastgelegd (Resource vs Function APIs)
- ☑ Conceptueel Datamodel is volledig en consistent
- ☑ Bounded Contexts zijn geïdentificeerd en gedocumenteerd
- ☑ NFR's zijn SMART geformuleerd (Specific, Measurable, Achievable, Relevant, Time-bound)
- ☑ Technology Stack is gekozen en onderbouwd
- ☑ Infrastructuur keuzes zijn gedocumenteerd
- ☑ Enablers zijn geïdentificeerd en geprioriteerd
- ☑ Technische risico's zijn benoemd met mitigation
- ☑ Architectuur is compliant met organisatie-standaarden
- ☑ Alle beslissingen zijn traceerbaar naar founding hypothesis
- ☑ 5-regels prompt is geformuleerd en integreert architecturale keuzes
- ☑ Prompt stelt agents in staat om autonom de applicatie te bouwen
- ☑ Go/no-go beslissing is genomen (GA DOOR naar fase C, of STOP)

---

## 8. Kwaliteitsprincipes

Deze fase committeert zich aan de principes uit het **Application Charter** en specificeert deze als volgt:

### Fase-specifieke Principes
- **Onderbouwing**: Elke architecturale beslissing is onderbouwd met rationale
- **Intentional Architecture**: Bewuste keuzes die business strategie ondersteunen
- **Minimale overhead**: Niet over-architecturen, focus op essentiële beslissingen
- **Bounded Context Respect**: Entity en Rule services blijven binnen context
- **Technology-agnostic waar mogelijk**: High-level patterns boven specifieke tooling
- **NFR-driven**: Non-functional requirements sturen architecturale keuzes
- **Evolutie-vriendelijk**: Architectuur moet kunnen evolueren met nieuwe inzichten
- **Prompt-gericht**: Alle beslissingen moeten vertaalbaar zijn naar een 5-regels prompt voor agents

### Cross-fase Principes (Application Charter)
- **Fasezuiverheid**: Deze fase levert uitsluitend strategische architecturale beslissingen, patronen en NFR's. Gedetailleerd API-ontwerp (fase D), feature-specificatie (fase C), en implementatie (fase E) zijn expliciet buiten scope.
- **Technologie-agnostisch**: Waar mogelijk blijven we op patroon-niveau, specifieke tooling alleen met onderbouwing.
- **Traceerbaarheid**: Alle beslissingen zijn traceerbaar naar founding hypothesis (fase A) en business case. Downstream fases (C, D, E) bouwen voort op deze architectuur.
- **Expliciete aannames**: Maximaal 3 aannames tegelijk, altijd gemarkeerd (zie Constitutie Art. 4).
- **Built-in Quality**: Kwaliteit vanaf het begin — geen ongedocumenteerde of niet-onderbouwde architecturale beslissingen.
- **Quality First**: Kwaliteit gaat boven snelheid — architectuur moet gevalideerd zijn voordat fase afsluit.

"Geen beslissing zonder onderbouwing" en "Geen architectuur zonder business value".

---

## 9. Anti-Patterns

In deze fase is het expliciet verboden om:
- **Over-architecturen**: Geen "we bouwen alles voor elke mogelijke toekomst"
- **Ongedocumenteerde beslissingen**: Elke keuze moet gedocumenteerd zijn (ADR)
- **Niet-traceerbare keuzes**: Alle beslissingen moeten terug te leiden zijn naar founding hypothesis
- **Detailontwerp vooruitlopen**: Geen gedetailleerde API-contracten of database schemas
- **Technology hype volgen**: Geen tooling kiezen zonder solide rationale
- **NFR's negeren**: Architectuur moet NFR's expliciet adresseren
- **Bounded Context schenden**: Entity/Rule services mogen niet cross-context zijn
- **SQL in Task Services**: Task services orchestreren, geen directe database access
- Architectuur maken zonder validatie met stakeholders
- Onrealistische NFR's stellen zonder haalbaarheidscheck
- Architectuur kopiëren zonder aanpassing aan context

---

## 10. Samenhang met Agents

**Principe**: Agents kunnen bijdragen aan deze fase,
maar mogen deze fase nooit zelfstandig afronden
of een exit-beslissing nemen.

Fase-afsluiting en exit-beslissingen blijven altijd menselijke verantwoordelijkheid.

### Ondersteunende Agents
- **CDM Architect** (Fase B): Primaire agent voor conceptueel datamodel
- **Moeder Agent**: Orkestratie en kwaliteitscontrole over alle fase-outputs
- **Logos**: Documentatie-verbetering en consistentie

### Afhankelijke Fases / Agents
- **Fase C (Specificatie)**: Gebruikt CDM, bounded contexts en NFR's als input voor feature-specificatie
- **Fase D (Ontwerp)**: Gebruikt architectuurpatronen, technology stack en NFR's voor gedetailleerd ontwerp
- **Feature-Analist** (Fase C): Gebruikt CDM om feature-specificaties technologie-agnostisch te houden
- **LDM Agent** (Fase D): Gebruikt CDM als basis voor logisch datamodel
- **Service Architect** (Fase D): Gebruikt service types (E/T/O/R/U) en API-stijl voor service design

**Let op**: Architecturale beslissingen zijn **fundament** voor alle downstream fases. Als architectuur wijzigt, moeten alle afhankelijke artefacten herzien worden.

---

## 11. Non-Goals

Expliciete lijst van zaken die **niet** worden nagestreefd in deze fase:

- **Geen gedetailleerd API-ontwerp**: Dat gebeurt in fase D
- **Geen feature-specificatie**: Dat gebeurt in fase C
- **Geen logisch datamodel**: Dat gebeurt in fase D
- **Geen implementatie**: Dat gebeurt in fase E
- **Geen operationele procedures**: Dat gebeurt in fase G
- **Geen test strategieën**: Dat gebeurt in fase F (met input van deze fase)
- **Geen release planning**: Dat gebeurt rond fase G
- **Geen effort estimatie**: Dat gebeurt na fase C
- **Geen proof-of-concept bouwen**: Tenzij strikt noodzakelijk voor haalbaarheid
- **Geen volledige infrastructuur opzetten**: Alleen keuzes, niet implementatie

---

## 12. TLX Service Architectuur Referentie

Deze fase definieert de **TLX Service Types** die in alle downstream fases gebruikt worden:

### Service Type Matrix

| Type | Code | Resource API | Function API | Logica Type | Bounded Context | SQL Toegestaan |
|------|------|--------------|--------------|-------------|-----------------|----------------|
| **Entity** | E | +++ | + | Data | ✅ Ja | ✅ Ja (binnen context) |
| **Task** | T | ++ | ++ | Composition | ❌ Nee | ❌ Nee (orchestreert Entity services) |
| **Orchestration** | O | + | +++ | Proces Composition | ❌ Nee | ❌ Nee |
| **Rule** | R | +++ | - | Rules | ✅ Ja | ✅ Ja (binnen context) |
| **Utility** | U | + | +++ | Divers | ❌ Nee | Contextafhankelijk |

**Legend**: +++ = primair gebruik, ++ = regelmatig, + = beperkt, - = niet van toepassing

### API-stijl Principes

#### Resource APIs (CRUD-oriented)
- **Naamgeving**: Noun-based (entiteiten)
- **HTTP Methods**: GET, POST, PATCH, PUT, DELETE
- **Idempotentie**: Altijd
- **Connectie**: Synchroon
- **Focus**: Objecten en hun state

#### Function APIs (Action-oriented)
- **Naamgeving**: Verb-based (acties)
- **HTTP Methods**: POST
- **Idempotentie**: Waar mogelijk (met compensatie/rollback mechanisme)
- **Connectie**: Synchroon én Asynchroon
- **Focus**: Commands, side-effects, processen

### Belangrijke Principes

1. **Combineren in Eén Service**: Resource APIs en Function APIs worden samengevoegd in dezelfde services (tenzij NFR's splitsen vereisen)

2. **Waarom Onderscheid Resource vs Function?**
   - Duidelijker mental model voor clients
   - Beter gebruik van HTTP-semantiek
   - Eenvoudiger versionering en evolutie
   - Gerichte observability en governance (metrics, autorisatie, rate-limits)

3. **Bounded Context Respect**:
   - Entity (E) en Rule (R) blijven binnen context
   - Task (T) en Orchestration (O) mogen cross-context zijn
   - Utility (U) is context-agnostisch

4. **Geen SQL in Task Services**: Task orchestreert Entity services (geen directe database access)

5. **Views & Rapportages**:
   - Entity Services: Joins mogelijk binnen bounded context
   - Task Services: Geen SQL, views niet relevant
   - Cross-domain rapportages: Views/Materialized Views (in overleg met DBA)

### SOA Methodologie Basis (Thomas Erl)

|  | **Business** | **Non-business** |
|---|--------------|------------------|
| **Proces non-agnostisch** | [Task Services](https://patterns.arcitura.com/soa-patterns/basics/soamethodology/task_services) | - |
| **Proces agnostisch** | [Entity Services](https://patterns.arcitura.com/soa-patterns/basics/soamethodology/entity_services) | [Utility Services](https://patterns.arcitura.com/soa-patterns/basics/soamethodology/utility_services) |

**Referenties**:
- [Arcitura SOA Patterns](https://patterns.arcitura.com/soa-patterns)
- [Amazon SOA White Paper](https://softwarearchitecture.s3.amazonaws.com/ServiceDesignPrinciples.pdf)

### Visuele Representatie

```
                         API-stijl
         +----------------------------------+
         | Resource API    | Function API   |
+--------+----------------------------------+
| Entity | 1:1 CRUD op     | Acties op      |
| (E)    | entiteit        | entiteit,      |
|        |                 | side-effects & |
|        |                 | commands       |
+--------+-----------------+----------------+
| Task   | Zelden;         | Orkestraties,  |
| (T)    | soms read-model | processen en   |
|        |                 | business-taken |
+--------+-----------------+----------------+
```

---

## 13. Change Log

| Datum | Versie | Wijziging | Auteur |
|------|--------|-----------|--------|
| 2026-01-07 | 1.1.0 | Toegevoegd: Cross-fase principes (Fasezuiverheid, Technologie-agnostisch, Traceerbaarheid, Built-in Quality, Quality First) uit Application Charter; verwijderd duplicatie 'max 3 aannames' (verwijst naar Constitutie) | GitHub Copilot |
| 2025-12-30 | 1.0.0 | Initiële versie — fase-charter voor Architectuur met TLX service types, hybride REST architectuur en SAFe architectural runway principes | Agent Charter Schrijver |
