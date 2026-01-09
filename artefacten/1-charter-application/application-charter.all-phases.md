# Application Charter — Bouwen van een Applicatie (Alle Fases)

**Versie**: 0.2.0  
**Status**: Active  
**Geldigheid**: Alle software-gerichte workspaces  
**Onderliggend aan**: Constitutie & Wet  
**Bovenliggend aan**: Fase-charters, Agent-charters, Workspace-beleid  

---

## 1. Doel van dit Charter

Dit **Application Charter** definieert de niet-onderhandelbare spelregels, kwaliteitsverwachtingen en verantwoordelijkheden voor het **end-to-end bouwen van een applicatie**, over **alle fases van de lifecycle** heen.

Het doel is:
- consistente kwaliteit over alle workspaces,
- veilige en controleerbare agent-samenwerking,
- voorspelbare waardecreatie,
- en een fundament voor het genereren van complete applicaties met minimale input.

---

## 2. Positionering in de Governance-hiërarchie

De governance-lagen zijn strikt geordend:

1. **Constitutie** — universeel, altijd van kracht  
2. **Wet** — geldt voor *alle* software-ontwikkeling  
3. **Application Charter (dit document)** — geldt voor *elke applicatie*  
4. **Fase Charters** — SAFe-fase-specifiek  
5. **Agent Charters** — rol- en scope-specifiek  
6. **Workspace Beleid** — context- en domeinspecifiek  

Conflicten worden altijd opgelost volgens deze volgorde.

---

## 3. Scope

### Geldt WEL voor:
- Alle softwareproducten (ECMR, facturatie, EFTI, etc.)
- Alle SAFe-fases (A t/m G + Utility)
- Menselijke en AI-gedreven activiteiten
- Alle agents die bijdragen aan de applicatie

### Geldt NIET voor:
- Niet-software workspaces (alleen constitutie)
- Operationeel beheer na overdracht (tenzij expliciet onderdeel van scope)

---

## 4. Kernprincipes (Niet Onderhandelbaar)

1. **Charter-first werken**  
   Geen fase, agent of activiteit zonder expliciet charter.

2. **Traceerbaarheid end-to-end**  
   Elk artefact is herleidbaar naar:
   - businessdoel (fase A),
   - requirement (fase C),
   - ontwerpbesluit (fase D),
   - implementatie (fase E),
   - validatie (fase F).
   
   Fase-charters definiëren hoe traceerbaarheid binnen hun fase wordt gewaarborgd.

3. **Built-in Quality**  
   Kwaliteit wordt ingebouwd vanaf het begin, niet achteraf toegevoegd.
   Elke fase committeert zich aan:
   - Quality First: kwaliteit gaat altijd boven snelheid
   - Objectieve validatie: tests, checks, reviews
   - Geen impliciete scope-uitbreiding

4. **Agent-gedreven ontwikkeling**  
   Alle activiteiten worden ondersteund door agents die:
   - binnen hun charter handelen,
   - samenwerken volgens expliciete patronen,
   - conflicten escaleren in plaats van gladstrijken.

**Let op**: Principes zoals "Fasezuiverheid", "Technologie-agnostisch tot specificatie" en "Expliciete aannames" zijn gedefinieerd in respectievelijk de Fase-charters en Constitutie, om duplicatie te voorkomen.

---

## 5. Verplichte Lifecycle (SAFe-aligned)

Elke applicatie doorloopt expliciet de volgende fases:

| Fase | Naam | Minimale Output |
|-----|------|----------------|
| A | Trigger | Business case, waarde-hypothese |
| B | Architectuur | ADR’s, NFR’s, architectuurkaders |
| C | Specificatie | Features, requirements, datamodel |
| D | Ontwerp | API’s, contracten, solution design |
| E | Bouw | Werkende code + CI |
| F | Validatie | Bewijs van voldoen aan criteria |
| G | Deployment | Release, runbooks |
| U | Utility | Ondersteunende services |

Geen fase mag worden overgeslagen.

---

## 6. Kwaliteitsverplichtingen

Voor de **gehele applicatie** gelden:

### Cross-fase Kwaliteitsprincipes
- **Built-in Quality**: Kwaliteit is ingebouwd vanaf het begin, niet achteraf toegevoegd
- **Quality First**: Kwaliteit gaat altijd boven snelheid — geen artefact wordt opgeleverd totdat het voldoet aan alle kwaliteitspoorten
- **Objectieve validatie**: Alle beslissingen en artefacten zijn testbaar via tests, checks, reviews
- **Volledigheid**: Alle verplichte secties en artefacten zijn compleet
- **Consistentie**: Terminologie en structuur zijn uniform over alle fases
- **Helderheid**: Alle documentatie is begrijpelijk op B1-taalniveau Nederlands

### Fase-specifieke Verplichtingen
- **Definition of Ready (DoR)**: Elke fase definieert entry criteria
- **Definition of Done (DoD)**: Elke fase definieert exit criteria
- **Fase-zuiverheid**: Elke fase levert uitsluitend haar eigen type beslissingen (zie fase-charters)
- **Traceerbaarheid**: Elk artefact is herleidbaar naar upstream beslissingen

### Governance-compliance
- Geen impliciete scope-uitbreiding
- Alle aannames expliciet gedocumenteerd (max 3, zie Constitutie Art. 4)
- Conflicten worden geëscaleerd, niet verborgen
- Agents handelen binnen hun charter

---

## 7. Agent-orkestratie

- Elke agent:
  - heeft exact één primaire verantwoordelijkheid,
  - opereert binnen één of meerdere expliciet benoemde fases,
  - handelt uitsluitend binnen zijn charter.
- Samenwerking is expliciet beschreven.
- Conflicten worden geëscaleerd, niet gladgestreken.

---

## 8. Veiligheid & Compliance

- Privacy en security zijn **cross-cutting concerns**
- NFR’s worden vastgesteld in fase B
- Validatie in fase F is verplicht
- Geen deployment zonder expliciete vrijgave

---

## 9. Anti-Patterns (Verboden)

Dit Application Charter verbiedt expliciet:
- “We doen het later wel”
- Impliciete aannames
- Design tijdens specificatie
- Code zonder traceerbare requirements
- Validatie zonder acceptatiecriteria
- Agents die buiten hun charter handelen

---

## 10. Relatie tot Fase- en Agent-Charters

- Fase-charters **concretiseren** dit Application Charter
- Agent-charters **implementeren** het binnen hun scope
- Dit charter is leidend bij interpretatiegeschillen

---

## 11. Wijzigingen

- Alleen de gebruiker mag dit charter inhoudelijk wijzigen
- Wijzigingen vereisen:
  - versie-up,
  - motivatie,
  - impactanalyse

---

## 12. Einddoel

Dit charter ondersteunt het strategische einddoel:

> *Met een minimale, eenduidige prompt een volledige, veilige en robuuste applicatie genereren.*

---

## Change Log

| Datum | Versie | Wijziging | Auteur |
|------|--------|-----------|--------|
| 2026-01-07 | 0.2.0 | Herstructurering: verplaatst fase-specifieke principes (Fasezuiverheid, Technologie-agnostisch) naar fase-charters; gecentraliseerd algemene kwaliteitsprincipes (Built-in Quality, Quality First); verwijderd duplicatie met Constitutie (max 3 aannames) | GitHub Copilot |
| 2026-01-07 | 0.1.0 | Initiële versie | Agent-bouwer |
