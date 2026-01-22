# Overzicht van erkende value streams

Dit document geeft een **workspace-overstijgend** overzicht van de value streams
die in het agent eco-systeem worden erkend. Voor elke value stream staat hier:

- waar de bijbehorende doctrine(s) te vinden zijn;
- welke stages (fases) daarin worden onderscheiden, met Nederlandstalige namen.

Het is een aanvulling op de constitutie en de doctrine-documenten in
`artefacten/0-governance/`.

Voor **alle** value streams geldt: zodra er agents worden ingezet om taken
uit te voeren, is de agent-ecosysteem constitutie van toepassing zoals
vastgelegd in de constitutie in `artefacten/0-governance/constitutie.md`.

---

## 1. Agent enablement

De value stream **Agent enablement** richt zich op het ontwerpen, bouwen en
beheren van agents binnen het eco-systeem.

Doel:

- zorgen dat er voor elke behoefte een passende agent-capability is;
- agents duurzaam beheren (introduceren, verbeteren, uitfaseren).

Typische stages (fases):

1. **Behoefte bepalen voor agents**  
   Vaststellen welke capabilities, rollen en automatiseerbare taken nodig zijn.

2. **Ontwerpen van agents**  
   Uitwerken van boundaries, charters, rollen en contracts.

3. **Realiseren van agents**  
   Maken van prompts, runners en benodigde integraties.

4. **Inbedden en beheren van agents**  
   Agents inzetten in workspaces, monitoren, verbeteren en waar nodig uitfaseren.

Een uitgewerkte doctrine voor Agent enablement volgt nog. Tot die tijd worden
deze stages gebruikt als werkbaar referentiekader.

---

## 2. IT-development

De value stream **IT-development** is uitgewerkt in de **Doctrine IT
Development**:

- `artefacten/0-governance/doctrine-it-development.md`

Deze doctrine is gebaseerd op SAFe en beschrijft de volledige ontwikkelstroom
van idee tot deployment. De belangrijkste fases (stages) zijn:

1. **Trigger** (A)  
   Initiatie en business cases: kansen identificeren, business value en prioriteit
   bepalen.

2. **Architectuur** (B)  
   Architectuur- en ontwerpbeslissingen: ADR's, patronen, technische richtlijnen.

3. **Specificatie** (C)  
   Requirements, features, datamodellen en processen specificeren, technologie-
   agnostisch.

4. **Ontwerp** (D)  
   Functioneel en technisch ontwerp, API- en contractdesign, data- en
   componentinteracties.

5. **Bouw** (E)  
   Implementatie en integratie: code, scripts, configuratie en CI.

6. **Validatie** (F)  
   Testen en kwaliteitscontrole: geautomatiseerde tests, performance, security.

7. **Deployment** (G)  
   Release en uitrol naar productie: deployment, monitoring en runbooks.

Agents met primary value stream **IT-development** volgen deze doctrine.

---

value
Deze beschrijving vormt de basis voor een formele **Kennispublicatie-doctrine**
die later in `artefacten/0-governance/` wordt vastgelegd.

---

## 4. Solution-architecting

## Herkomstverantwoording

Dit normatief artefact is geschreven op basis van de hieronder geraadpleegde
bronnen. De value stream Solution-architecting is afgeleid uit bestaande
governance-documenten en aangevuld met kennis over de specifieke context van
gemeentelijke enterprise architectuur (GEMMA, Common Ground).

**Geraadpleegde bronnen**:
- Constitutie Mandarin (versie 1.2.1, gelezen op 2026-01-18 09:15)
- value-streams.md (bestaande versie met IT-development, Agent enablement en
  Kennispublicatie, gelezen op 2026-01-18 09:15)
- doctrine-it-development.md (gelezen op 2026-01-18 09:15)
- Opdracht van gebruiker (received 2026-01-18 09:15): beschrijf value stream
  solution-architecting die documenten reviewt van enterprise architect in
  omgeving van gemeente, GEMMA, Common Ground

**Toelichting op structuur**:
Deze value stream beschrijft het proces van het beoordelen, verfijnen en
valideren van enterprise architectuurdocumentatie in de context van Nederlandse
gemeenten. De stages volgen de logische volgorde van review-activiteiten, van
initiële intake tot borging en publicatie van goedgekeurde architectuur.

---

De value stream **Solution-architecting** richt zich op het reviewen,
beoordelen en verfijnen van architectuurdocumentatie die door enterprise
architects wordt aangeleverd in de context van gemeentelijke IT-landschappen,
met specifieke aandacht voor GEMMA (Gemeentelijke Model Architectuur) en
Common Ground.

Doel:

- waarborgen dat oplossingsarchitectuur aansluit bij enterprise-kaders en
  gemeentelijke standaarden;
- borgen van architectuurkwaliteit, compliance en consistentie;
- faciliteren van inhoudelijke dialoog tussen enterprise- en solution-niveau.

Context:

Deze value stream is specifiek relevant voor organisaties die werken met:
- **GEMMA**: het referentiemodel voor gemeentelijke informatievoorziening;
- **Common Ground**: de visie op een moderne gemeentelijke gegevensuitwisseling
  met API's, bronregistraties en scheiding van gegevens en applicaties;
- enterprise-architectuurprincipes zoals vastgelegd in gemeentelijke
  architectuurbeleid.

Typische stages (fases):

1. **Intake en kadering** (Intake & Framing)  
   Ontvangen en registreren van architectuurdocumenten; bepalen van scope,
   context en toetsingskader (welke GEMMA-lagen, welke Common Ground-principes,
   welke beleidskaders zijn van toepassing).

2. **Beoordeling en analyse** (Assessment & Analysis)  
   Toetsen van de aangeleverde architectuur aan enterprise-principes,
   GEMMA-referenties, Common Ground-uitgangspunten en gemeentelijke
   architectuurbeleid. Identificeren van afwijkingen, risico's en
   verbeterpunten.

3. **Dialoog en verfijning** (Dialogue & Refinement)  
   In gesprek met de enterprise architect en stakeholders om onduidelijkheden
   op te helderen, alternatieven te verkennen en consensus te bereiken over
   aanpassingen.

4. **Vaststelling en advisering** (Decision & Advice)  
   Formaliseren van het reviewoordeel: akkoord, akkoord onder voorwaarden of
   afgekeurd. Vastleggen van adviezen, aanbevelingen en eventuele voorwaarden.

5. **Borging en publicatie** (Assurance & Publication)  
   Verankeren van goedgekeurde architectuur in de gemeentelijke
   architectuurrepository; beschikbaar maken voor realisatieteams en
   governance-processen.

Een formele **Doctrine Solution-architecting** die deze value stream uitwerkt,
inclusief rollen, artefacten en kwaliteitscriteria, volgt in een later stadium
en wordt opgenomen in `artefacten/0-governance/`.

---

## 5. Architectuur-en-oplossingsontwerp

## Herkomstverantwoording

Dit normatief artefact is geschreven op basis van de hieronder geraadpleegde
bronnen. De value stream Architectuur-en-oplossingsontwerp is afgeleid uit
bestaande governance-documenten en aangevuld met kennis over generieke
architectuur- en ontwerppraktijken.

**Geraadpleegde bronnen**:
- Constitutie Mandarin (versie 1.2.1, gelezen op 2026-01-22 10:30)
- value-streams.md (bestaande versie met Agent enablement, IT-development,
  Kennispublicatie en Solution-architecting, gelezen op 2026-01-22 10:30)
- doctrine-it-development.md (gelezen op 2026-01-22 10:30)
- Opdracht van gebruiker (ontvangen op 2026-01-22): voeg toe een nieuwe value
  stream architectuur-en-oplossingsontwerp

**Toelichting op structuur**:
Deze value stream beschrijft het proces van het ontwerpen van architectuur en
oplossingen voor complexe vraagstukken. De stages volgen de natuurlijke
progressie van architectuurwerk, van probleemverkenning via conceptueel ontwerp
naar gedetailleerd uitwerking en validatie. De value stream is generiek en kan
toegepast worden in verschillende contexten (IT, bedrijfsprocessen, organisatie).

---

De value stream **Architectuur-en-oplossingsontwerp** richt zich op het
systematisch ontwerpen van architecturen en oplossingen die beantwoorden aan
complexe vraagstukken, waarbij rekening wordt gehouden met technische,
functionele en organisatorische aspecten.

Doel:

- vertalen van behoeften en eisen naar coherente architectuur- en
  oplossingsconcepten;
- waarborgen van technische haalbaarheid, schaalbaarheid en onderhoudbaarheid;
- creëren van gedeeld begrip tussen stakeholders door heldere architectuur-
  documentatie;
- faciliteren van gefundeerde ontwerpbeslissingen op basis van afwegingen en
  trade-offs.

Typische stages (fases):

1. **Probleemverkenning en context** (Problem Exploration & Context)  
   Begrijpen van het vraagstuk, stakeholders, randvoorwaarden en bestaande
   situatie. Identificeren van drivers, constraints en kwaliteitsattributen.

2. **Conceptueel ontwerp** (Conceptual Design)  
   Uitwerken van architectuurvisie en hoofdlijnen. Definiëren van
   architectuurprincipes, patronen en high-level componenten. Maken van
   initiële architectuurschetsen en conceptuele modellen.

3. **Oplossingsuitwerking** (Solution Elaboration)  
   Detailleren van de gekozen oplossingsrichting. Specificeren van componenten,
   interfaces, data-flows en integraties. Opstellen van Architecture Decision
   Records (ADR's) voor belangrijke ontwerpkeuzes.

4. **Validatie en verfijning** (Validation & Refinement)  
   Toetsen van het ontwerp aan requirements en kwaliteitsattributen. Uitvoeren
   van architecture reviews, proof-of-concepts en haalbaarheidsanalyses.
   Bijstellen op basis van feedback en bevindingen.

5. **Formalisering en overdracht** (Formalization & Handover)  
   Vastleggen van definitieve architectuur in standaard documentatieformaten.
   Voorbereiden van overdracht naar realisatieteams. Opstellen van
   implementatierichtlijnen en architectuurbewakingsafspraken.

Een formele **Doctrine Architectuur-en-oplossingsontwerp** die deze value
stream uitwerkt, inclusief rollen, deliverables en kwaliteitscriteria, volgt
in een later stadium en wordt opgenomen in `artefacten/0-governance/`.
