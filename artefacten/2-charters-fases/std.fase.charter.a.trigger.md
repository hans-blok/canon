# Phase Charter — Trigger (Initiatie)

**Doctrine IT Development**: doctrine-it-development.md  
**Phase Identifier**: standards.charter.phase.a.trigger  
**Version**: 1.1.0  
**Status**: Active  
**Last Updated**: 2026-01-07  
**Owner**: Architecture & AI Enablement

---

## 1. Doel en Positionering

### Doel van de Fase
De **Trigger-fase** (Initiatie, Discovery en Opportunity Canvas in SAFe) legt het fundament voor alle verdere ontwikkeling door zakelijke behoeften, klantpijnpunten en kansen te identificeren en te formuleren in een heldere, gedeelde visie. Het einddoel van deze fase is een **solide founding hypothesis, business case en initiële backlog** die de basis vormen voor architecturale beslissingen in Fase B. Deze fase wordt **nauw afgestemd met stakeholders** en vormt het contractuele startpunt voor alle downstream fases.

**Kernprincipe**: *"Als we niet kunnen uitleggen waarom klanten voor ons kiezen in plaats van alternatieven, dan weten we niet wat we moeten bouwen."*

### Plaats in het Delivery Framework
- **Voorgaande fase**: (geen — dit is de eerste fase)
- **Volgende fase**: B. Architectuur — Architect & Design Decisions
- **Beslissend moment**: Go / No-go op basis van:
  - Helderheid van de founding hypothesis
  - Validiteit van de business case
  - Testbaarheid van de success criteria
  - Volledigheid van stakeholder-afstemming

Deze fase is een expliciete **kwaliteits- en beslissingsstep**, geen doorgeefluik. Vage of onderbouwde initiatieven worden niet doorgegeven naar architectuur en specificatie.

---

## 2. Fase-doelstellingen

De fase is succesvol afgerond wanneer:
- **Founding Hypothesis** is geformuleerd volgens Knapp-methodologie (Jake Knapp, "Sprint"/"Click")
- **Business Case** beschrijft klantwaarde, ROI en strategische rationale
- **Target Audience** (doelgroep) is expliciet geïdentificeerd en beschreven
- **Klantpijnpunten** zijn helder gearticuleerd en gevalideerd met stakeholders
- **Competitief voordeel** is expliciet beschreven (waarom kiezen klanten voor ons boven alternatieven)
- **Success criteria** zijn testbaar en meetbaar gedefinieerd
- **Problem Statement** beschrijft het op te lossen probleem ondubbelzinnig
- **Value Proposition** legt uit welke waarde de oplossing levert
- **Initial Backlog Items** bevat high-level epics of capabilities
- **Stakeholder-afstemming** is gedocumenteerd (wie, wanneer, akkoord)
- Maximaal **3 aannames** zijn expliciet gedocumenteerd en gevalideerd
- **Scope boundaries** zijn helder (wat wel en niet binnen scope valt)
- Alle artefacten zijn afgestemd en gevalideerd met stakeholders

Doelen zijn **toetsbaar, expliciet en herhaalbaar**.

---

## 3. Scope en Grenzen

### Binnen Scope (DOET WEL)
- **Founding Hypothesis schrijven**: Volgens Knapp-methodologie ("Als [doelgroep] [situatie], dan kiezen zij voor [onze oplossing] boven [concurrent], omdat [unieke waarde]")
- **Business Case opstellen**: Klantwaarde, ROI, strategische rationale, risico's
- **Problem Statement formuleren**: Helder beschrijven welk probleem opgelost wordt
- **Value Proposition definiëren**: Welke waarde levert de oplossing aan klanten
- **Target Audience identificeren**: Wie zijn de primaire gebruikers en klanten
- **Klantpijnpunten articuleren**: Welke problemen ervaren klanten nu
- **Competitief voordeel beschrijven**: Waarom kiezen klanten voor ons boven alternatieven
- **Success criteria definiëren**: Meetbare criteria voor succes
- **Initial Backlog creëren**: High-level epics, capabilities, features (nog niet uitgewerkt)
- **Stakeholder-afstemming**: Validatie en akkoord van alle key stakeholders
- **Scope boundaries bepalen**: Wat wel en niet binnen scope valt (high-level)
- **Aannames documenteren**: Expliciet markeren van aannames (maximaal 3)
- **Economic Framework**: Bepalen van prioriteringsprincipes (WSJF, ROI, etc.)

### Buiten Scope (DOET NIET)
- **Architecturale beslissingen**: Geen technische keuzes (dat is fase B)
- **Gedetailleerde requirements**: Geen uitgewerkte user stories of acceptance criteria (dat is fase C)
- **Feature specificatie**: Geen gedetailleerde feature-beschrijvingen (dat is fase C)
- **Technisch ontwerp**: Geen API's, databases, interfaces (dat is fase D)
- **Implementatie**: Geen code of configuratie (dat is fase E)
- Gedetailleerde datamodellen (dat is fase C met input van fase B)
- Procesbeschrijvingen op operationeel niveau (dat is fase C)
- Release planning of roadmap (komt uit backlog prioritering na deze fase)
- Effort estimatie of sprint planning
- Technische haalbaarheidsanalyse (komt in fase B)

---

## 4. Entry Criteria (Input Quality Gate)

Deze fase mag **altijd starten** — het is de eerste fase. Wel zijn er **minimale voorwaarden** voor kwalitatieve output:

- ☐ Er is een **sponsor of initiator** geïdentificeerd (wie drijft dit initiatief)
- ☐ Er is een **initiële probleemomschrijving** beschikbaar (al is deze nog vaag)
- ☐ Er is **toegang tot stakeholders** voor validatie en afstemming
- ☐ Er is **commitment** om de fase grondig te doorlopen (geen "snel iets beginnen")

### Vereiste Inputs

| Artefact | Herkomst | Minimale Kwaliteitseis |
|----------|----------|------------------------|
| Initiële probleemomschrijving | Sponsor/Initiator | Beschrijving van pijnpunt of kans, al is deze nog vaag |
| Stakeholder-toegang | Organisatie | Mogelijkheid om met key stakeholders te spreken |
| Strategische context | Product Owner / Management | Hoe past dit in bredere strategie (indien beschikbaar) |

**Let op**: Deze fase **creëert helderheid**, dus vage inputs zijn acceptabel. Het is de verantwoordelijkheid van deze fase om vaagheid om te zetten in helderheid.

---

## 5. Activiteiten en Methoden

### Kernactiviteiten
1. **Discovery Sessions**: Gesprekken met stakeholders om behoeften en pijnpunten te identificeren
2. **Problem Statement formuleren**: Helder beschrijven welk probleem opgelost wordt
3. **Target Audience Workshop**: Identificeren en beschrijven van primaire gebruikersgroepen
4. **Competitieve Analyse**: Begrijpen van alternatieven en concurrenten
5. **Value Proposition Design**: Formuleren van unieke waarde-aanbod
6. **Founding Hypothesis schrijven**: Volgens Knapp-methodologie
7. **Business Case opstellen**: ROI, klantwaarde, risico's, strategische fit
8. **Success Criteria definiëren**: Meetbare criteria voor succes
9. **Initial Backlog creëren**: High-level epics en capabilities
10. **Stakeholder Validatie**: Alle artefacten afstemmen en valideren met stakeholders
11. **Aannames identificeren en documenteren**: Expliciet markeren van aannames (max 3)

### Methoden en Referenties
- **Jake Knapp Methodologie**: Founding Hypothesis volgens "Sprint" en "Click"
- **Lean Business Case**: Lichtgewicht business case voor snelle go/no-go beslissingen
- **Opportunity Canvas**: Visualiseren van probleem, oplossing, waarde
- **Hypothesis-Driven Development**: Start met testbare hypothese
- **Jobs-to-be-Done Framework**: Begrijpen van klantbehoeften
- **Value Proposition Canvas**: Visualiseren van waarde-aanbod
- **Economic Framework (SAFe)**: Prioriteringsprincipes (WSJF, Cost of Delay)
- **Design Thinking**: Gebruiker-centrische benadering

Focus: **helderheid en afstemming met stakeholders**, niet snelheid.

---

## 6. Rollen en Verantwoordelijkheden

| Rol | Verantwoordelijkheid | Beslisrecht |
|-----|----------------------|-------------|
| Product Owner | Definiëren van productvisie en waarde | Go/No-go op initiatief |
| Sponsor/Initiator | Aandragen van initiatief en strategische context | Strategische fit en commitment |
| Stakeholders | Valideren van hypotheses en business case | Feedback en akkoord op artefacten |
| Business Analyst | Faciliteren van discovery en formuleren van artefacten | Kwaliteit van business case en problem statement |
| Founding Hypothesis Owner Agent | Genereren van founding hypothesis volgens Knapp | Formulering van hypothesis |
| Agents (algemeen) | Ondersteunen bij creatie van artefacten | Kwaliteit en structuur binnen fase-scope |

**Menselijke rollen blijven eindverantwoordelijk** — agents ondersteunen, maar stakeholders beslissen.

---

## 7. Outputs en Exit Criteria

### Geleverde Outputs
1. **Founding Hypothesis**: Volledige hypothesis volgens Knapp-methodologie
   - Doelgroep
   - Situatie/context
   - Onze oplossing (kort)
   - Concurrent/alternatief
   - Unieke waarde (waarom beter)
   - Success criteria
   - Aannames (max 3, expliciet gemarkeerd)
   - Business value

2. **Business Case**: 
   - Klantwaarde en ROI
   - Strategische rationale
   - Risico's en mitigation
   - Go/no-go aanbeveling

3. **Problem Statement**: 
   - Helder beschreven probleem
   - Impact van het probleem
   - Huidige situatie (as-is)

4. **Value Proposition**:
   - Welke waarde levert de oplossing
   - Voor wie (target audience)
   - Competitief voordeel

5. **Target Audience Beschrijving**:
   - Primaire gebruikersgroepen
   - Behoeften en pijnpunten
   - Context en gebruik

6. **Initial Backlog**:
   - High-level epics
   - Capabilities
   - Features (nog niet uitgewerkt)

7. **Stakeholder Validatie Log**:
   - Wie gevalideerd heeft
   - Wanneer
   - Akkoord of feedback

8. **Aannames Log**:
   - Expliciet gemarkeerde aannames (max 3)
   - Validatiestatus

### Exit Criteria (Phase Quality Gate)

De fase is pas afgerond wanneer:
- ☑ Founding Hypothesis is volledig en volgt Knapp-structuur
- ☑ Business Case is goedgekeurd door sponsor/stakeholders
- ☑ Target Audience is expliciet beschreven
- ☑ Competitief voordeel is helder gearticuleerd
- ☑ Success criteria zijn testbaar en meetbaar
- ☑ Alle key stakeholders hebben gevalideerd en akkoord gegeven
- ☑ Aannames zijn expliciet gedocumenteerd (max 3)
- ☑ Initial backlog bevat minimaal 3-5 high-level epics
- ☑ Scope boundaries zijn helder (wat wel/niet binnen scope)
- ☑ Geen conflicten of onduidelijkheden in artefacten
- ☑ Alle outputs zijn begrijpelijk op B1-taalniveau Nederlands
- ☑ Go/no-go beslissing is genomen (GA DOOR naar fase B, of STOP)

**Zonder akkoord van stakeholders gaat NIETS door naar fase B.**

---

## 8. Kwaliteitsprincipes

Deze fase committeert zich aan de principes uit het **Application Charter** en specificeert deze als volgt:

### Fase-specifieke Principes
- **Helderheid boven volledigheid**: Beter een heldere, beperkte scope dan een vage, brede scope
- **Stakeholder-afstemming boven snelheid**: Alle artefacten zijn gevalideerd met stakeholders
- **Testbaarheid**: Alle hypotheses en success criteria zijn meetbaar
- **Klantgerichtheid**: Klantwaarde staat centraal, niet technologie
- **Competitief bewustzijn**: Waarom kiezen klanten voor ons boven alternatieven
- **Eenvoud**: 5-regels prompt moet voldoende zijn voor agent-driven development
- **Geen impliciete scope-uitbreiding**: Alleen wat expliciet in hypothesis en business case staat

### Cross-fase Principes (Application Charter)
- **Fasezuiverheid**: Deze fase levert uitsluitend initiatie-artefacten (business case, hypothese, problem statement). Architecturale beslissingen (fase B), gedetailleerde requirements (fase C), en technisch ontwerp (fase D) zijn expliciet buiten scope.
- **Technologie-agnostisch**: Deze fase maakt GEEN technische keuzes. Implementatiedetails zijn verboden.
- **Traceerbaarheid**: Elk artefact in deze fase wordt de basis voor downstream beslissingen (architectuur, specificatie, ontwerp).
- **Expliciete aannames**: Maximaal 3 aannames tegelijk, altijd gemarkeerd (zie Constitutie Art. 4).
- **Built-in Quality**: Kwaliteit vanaf het begin — geen vage hypotheses of onvolledige business cases worden doorgegeven.
- **Quality First**: Kwaliteit gaat boven snelheid — stakeholder-validatie is verplicht voordat fase afsluit.

"Niet zeker" is beter dan "stilzwijgend fout".

---

## 9. Anti-Patterns

In deze fase is het expliciet verboden om:
- **Vage hypotheses**: Geen "we bouwen iets nuttigs" — specificeer WAT, VOOR WIE, WAAROM BETER
- **Ontbrekend competitief voordeel**: Altijd beschrijven waarom klanten voor ons kiezen boven alternatieven
- **Geen stakeholder-validatie**: Niets doorgeven zonder akkoord van key stakeholders
- **Technische beslissingen**: Geen architectuur of technische keuzes (dat is fase B)
- **Feature-specificatie**: Geen gedetailleerde requirements (dat is fase C)
- **Onmeetbare success criteria**: Alle criteria moeten testbaar en meetbaar zijn
- **Meer dan 3 aannames**: Bij meer aannames → escalatie en aanvullende discovery
- **Doorgaan zonder go-beslissing**: Bij twijfel → no-go of refinement
- Founding hypothesis overslaan ("we weten al wat we moeten bouwen")
- 5-regels prompt weglaten of uitbreiden tot pagina's tekst
- Conflicten of onduidelijkheden verbergen

---

## 10. Samenhang met Agents

**Principe**: Agents kunnen bijdragen aan deze fase,
maar mogen deze fase nooit zelfstandig afronden
of een exit-beslissing nemen.

Fase-afsluiting en exit-beslissingen blijven altijd menselijke verantwoordelijkheid.

### Ondersteunende Agents
- **Founding Hypothesis Owner** (Fase A): Primaire agent voor het schrijven van founding hypotheses
- **Moeder Agent**: Orkestratie en kwaliteitscontrole over alle fase-outputs
- **Logos**: Documentatie-verbetering en consistentie

### Afhankelijke Fases / Agents
- **Fase B (Architectuur)**: Gebruikt founding hypothesis en business case als input voor architecturale beslissingen
- **Fase C (Specificatie)**: Gebruikt founding hypothesis, value proposition en initial backlog als input voor feature-specificatie
- **CDM Architect** (Fase B): Gebruikt target audience en business case om conceptueel datamodel te bepalen
- **Feature-Analist** (Fase C): Gebruikt founding hypothesis om features uit te werken met benefit hypotheses

**Let op**: Founding Hypothesis is **fundament** voor alle downstream beslissingen. Als deze wijzigt, moeten alle afhankelijke artefacten herzien worden.

---

## 11. Non-Goals

Expliciete lijst van zaken die **niet** worden nagestreefd in deze fase:

- **Geen volledige productspecificatie**: Dat gebeurt in fase C
- **Geen technische architectuur**: Dat gebeurt in fase B
- **Geen gedetailleerde roadmap**: Initial backlog is high-level, geen sprintplanning
- **Geen marktonderzoek uitvoeren**: We gebruiken bestaand onderzoek, voeren zelf geen nieuw onderzoek uit
- **Geen pricing of business model**: We beschrijven waarde, maar bepalen geen prijzen
- **Geen marketing strategie**: We beschrijven value proposition, maar geen go-to-market
- **Geen effort estimatie**: Dat gebeurt na fase C wanneer requirements bekend zijn
- **Geen technische haalbaarheid**: Dat wordt in fase B gevalideerd
- **Geen juridische of compliance analyse**: Dat is input voor fase B (architectuur)

---

## 12. Change Log

| Datum | Versie | Wijziging | Auteur |
|------|--------|-----------|--------|
| 2026-01-07 | 1.1.0 | Toegevoegd: Cross-fase principes (Fasezuiverheid, Technologie-agnostisch, Traceerbaarheid, Built-in Quality, Quality First) uit Application Charter; verwijderd duplicatie 'max 3 aannames' (verwijst naar Constitutie) | GitHub Copilot |
| 2025-12-30 | 1.0.0 | Initiële versie — fase-charter voor Trigger (Initiatie) met focus op founding hypothesis, business case, 5-regels prompt en stakeholder-afstemming | Agent Charter Schrijver |
