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

## 3. Kennispublicatie

De value stream **Kennispublicatie** (Knowledge Publication) richt zich op het
expliciteren, aanscherpen en publiceren van overdraagbare kennis
(bijvoorbeeld canon-teksten, architectuurbeschrijvingen, essays en
HTML-publicaties).

Een eerste uitwerking staat in:

- `governance/temp/kennis-publicatie.md` (design-document, nog niet normatief)

De beoogde stages (fases), hier in het Nederlands, zijn:

1. **Intentie en kadering** (Intent & Framing)  
   Waarom de inhoud bestaat, voor wie zij is en in welke context zij wordt
   geplaatst.

2. **Conceptualisatie** (Conceptualization)  
   Uitwerken van het concept en de kernideeën; begrippen en structuur bepalen.

3. **Schrijven** (Authoring)  
   De inhoud in heldere, leesbare taal uitwerken.

4. **Verfijnen** (Refinement)  
   Aanscherpen, valideren en harmoniseren van de inhoud; consistentie met canon
   en terminologie.

5. **Publicatie** (Publication)  
   Beschikbaar maken en beheren van het kennisobject (formattering, kanaal,
   distributie).

Deze beschrijving vormt de basis voor een formele **Kennispublicatie-doctrine**
die later in `artefacten/0-governance/` wordt vastgelegd.
