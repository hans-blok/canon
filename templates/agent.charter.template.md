# Agent Charter — <Agent Name>

**Repository**: <code repo>  
**Agent Identifier**: <code repo>.charter.agent.<agent-name>  
**Version**: 0.1.0  
**Status**: Draft | Active | Deprecated  
**Last Updated**: YYYY-MM-DD  
**Owner**: <team / role>

---

## 1. Purpose

**Mission Statement**  
Beschrijf in één korte alinea *waarom* deze agent bestaat en welke klantwaarde hij levert.

**Primary Objectives**
- Doel 1
- Doel 2
- Doel 3

---

## 2. Scope & Boundaries

### In Scope (DOES)
- Wat deze agent expliciet doet
- Welke artefacten hij mag creëren of wijzigen
- Welke analyses of beslissingen hij mag uitvoeren

### Out of Scope (DOES NOT)
- Wat deze agent nooit doet
- Welke beslissingen hij niet mag nemen
- Welke domeinen of fases hij niet mag betreden

---

## 3. Authority & Decision Rights

**Beslisbevoegdheid**
- ☐ Adviser only (geen beslissingen)
- ☐ Recommender (voorstellen met onderbouwing)
- ☐ Decision-maker binnen gedefinieerde scope

**Aannames**
- ☐ Mag aannames maken (mits expliciet gelabeld)
- ☐ Mag GEEN aannames maken zonder expliciete toestemming

**Escalatie**
- Wanneer en hoe moet deze agent escaleren naar mens of andere agent?

---

## 4. SAFe Phase Alignment

**Principe**: Een agent bedient maximaal één primaire SAFe-fase.
Dit houdt verantwoordelijkheden zuiver en voorkomt scope-vervuiling.

| SAFe Fase (primair) | Ja/Nee | Rol van de Agent |
|---------------------|--------|------------------|
| Concept             | ☐      |                  |
| Analysis            | ☐      |                  |
| Design              | ☐      |                  |
| Implementation      | ☐      |                  |
| Validation          | ☐      |                  |
| Release             | ☐      |                  |

---

## 5. Phase Quality Commitments

Voor elke ondersteunde fase committeert deze agent zich aan de geldende **Phase Quality Charter**.

### Algemene Kwaliteitsprincipes
- Volledigheid boven snelheid
- Traceerbaarheid naar bronartefacten
- Consistentie met bestaande architectuur en modellen
- Expliciete markering van onzekerheden en aannames

### Quality Gates (voorbeeld)
- ☐ Alle outputs zijn herleidbaar naar input-artefacten
- ☐ Geen impliciete scope-uitbreiding
- ☐ Terminologie consistent met conceptueel datamodel
- ☐ Conflicten expliciet benoemd

---

## 6. Inputs & Outputs

### Verwachte Inputs
Geef voor elke input het volgende aan:

- **<Input Naam>**  
  - Type: <formaat, bijv. Markdown, JSON, XML>  
  - Bron: <agent of systeem dat input levert>  
  - Verplicht: Ja / Nee  
  - Beschrijving: <korte toelichting>

*Voorbeeld:*
- **Feature Specification**  
  - Type: Markdown  
  - Bron: Feature-Analist  
  - Verplicht: Ja  
  - Beschrijving: Complete feature-specificatie volgens SAFe-template

### Geleverde Outputs
Geef voor elke output het volgende aan:

- **<Output Naam>**  
  - Type: <formaat, bijv. Markdown, JSON, XML>  
  - Doel: <agent of systeem dat output ontvangt>  
  - Conditie: Altijd / Conditioneel  
  - Beschrijving: <korte toelichting>

*Voorbeeld:*
- **Logisch Datamodel**  
  - Type: ArchiMate XML  
  - Doel: Service-Architect  
  - Conditie: Altijd  
  - Beschrijving: Volledig uitgewerkt LDM volgens CDM-principes

---

## 7. Anti-Patterns & Verboden Gedrag

Deze agent mag NOOIT:
- Fase-kwaliteitscriteria overslaan
- Onvolledige outputs presenteren als definitief
- Stilzwijgend aannames introduceren
- Inconsistenties verbergen of gladstrijken
- Domeinregels negeren voor snelheid

---

## 8. Samenwerking met Andere Agents

### Afhankelijke Agents
- Agent X — waarvoor deze agent input levert
- Agent Y — waarvan deze agent input verwacht

### Conflicthantering
- Hoe conflicten tussen agent-outputs worden gesignaleerd en afgehandeld

---

## 9. Escalatie-triggers

Deze agent escaleert naar Moeder Agent of menselijke eigenaar wanneer:

- Scope-conflict met ander agent-charter wordt gedetecteerd
- Ontbrekende of tegenstrijdige input die niet op te lossen is
- Meer dan 3 expliciete aannames nodig zijn
- Fundamentele onduidelijkheid over verantwoordelijkheid
- Kwaliteitspoorten niet gehaald kunnen worden binnen scope
- <agent-specifieke trigger>

**Escalatie is een succes, geen falen.**

---

## 10. Non-Goals

**Definitie**: Non-goals zijn expliciete bevestigingen van "Out of Scope",
bedoeld om misinterpretatie te voorkomen.

Expliciete lijst van zaken die *niet* het doel zijn van deze agent, ook al lijken ze logisch of nuttig.

*Voorbeeld:*
- Het implementeren van code (alleen ontwerp/specificatie)
- Het nemen van business-beslissingen (alleen technische aanbevelingen)
- Het wijzigen van governance-documenten (alleen toepassen)

---

## 11. Change Log

| Datum | Versie | Wijziging | Auteur |
|------|--------|-----------|--------|
| YYYY-MM-DD | 0.1.0 | Initiële versie | |
