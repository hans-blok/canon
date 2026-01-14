# Workspace Doctrine — Architectuur en Standaard voor Workspaces

**Versie**: 1.0.0  
**Status**: Actief  
**Datum**: 2026-01-14  
**Eigenaar**: Architecture & AI Enablement  
**Type**: Normerend Doctrine-document

---

## 1. Inleiding en doel

Deze workspace-doctrine bundelt twee bestaande normatieve documenten:

- de structurele **workspace-architectuur** voor alle soorten workspaces; en
- de **workspace-standaard voor document-repositories**.

Samen vormen zij één doctrine voor hoe een workspace is opgebouwd, hoe folders heten en waar documenten en artefacten horen te staan. Deze doctrine is bedoeld voor:

- de standards-workspace;
- de agent-capabilities-workspace; en
- alle document-repositories en andere workspaces die door Moeder worden beheerd.

Deze doctrine is leidend voor:

- de inrichting van nieuwe workspaces;
- validatie en ordening door Moeder;
- prompts en charters van agents die iets zeggen over structuur of locaties; en
- beleid voor concrete repositories.

De onderliggende, meer gedetailleerde architectuur- en standaarddocumenten blijven bestaan als achtergrond en detail:

- artefacten/0-governance/workspace-architectuur.md  
- artefacten/0-governance/workspace-standaard.md

Wanneer in andere documenten wordt verwezen naar de **workspace-doctrine**, bedoelen we deze bundeling van architectuur en standaard.

---

## 2. Kernprincipes van de workspace-doctrine

De volgende principes gelden voor alle workspaces:

1. **Centrale definitie, lokale uitvoering**  
   Structuur, folders en naamconventies zijn centraal vastgelegd. Elke workspace past deze lokaal toe.

2. **Eén voorspelbare structuur**  
   Agents en mensen moeten altijd weten waar zij documenten, artefacten en prompts kunnen vinden.

3. **Traceerbaarheid**  
   Artefacten zijn herleidbaar naar fase, agent en input. De doctrine dwingt dit af via mappen en naamgeving.

4. **Scheiding van governance en uitvoering**  
   Governance-documenten en agent-charters liggen in vaste plekken. Uitgevoerde artefacten liggen in artefacten- en docs-folders.

5. **Document-repositories volgen een vaste basisstructuur**  
   Document-repositories (zoals deze standards-workspace) gebruiken een vaste set root-folders voor docs, governance, templates, temp en .github.

Deze principes zijn nader uitgewerkt in de twee onderliggende onderdelen van de doctrine.

---

## 3. Onderdeel 1: Workspace-architectuur (alle workspaces)

De **workspace-architectuur** beschrijft de verplichte structuur en conventies voor alle soorten workspaces in het eco-systeem.

Belangrijke punten uit de workspace-architectuur zijn onder meer:

- onderscheid tussen standards-repository, agent-capabilities-repository en project workspaces;
- verplichte top-level structuur met onder andere artefacten/, docs/, scripts/, templates/, .github/ en README.md;
- specifieke inrichting van artefacten/ voor standards-, agent-capabilities- en project-repositories;
- conventies voor naamgeving van bestanden en folders (lowercase, kebab-case, fase-prefixen);
- afspraken over Git-structuur, .gitignore en validatie door Moeder;
- relatie met de constitutie, beleid en doctrine-it-development.

Voor de volledige, gedetailleerde architectuurnorm blijft het bestaande document leidend:

- artefacten/0-governance/workspace-architectuur.md

Wanneer in charters, prompts of beleid wordt verwezen naar de "workspace-architectuur", valt dit nu onder deze workspace-doctrine. Waar nodig kan nog direct naar het architectuurdocument worden verwezen voor detail.

---

## 4. Onderdeel 2: Workspace-standaard voor document-repositories

De **workspace-standaard voor document-repositories** specificeert de verplichte structuur en afspraken voor repositories waarin documentatie en governance centraal staan.

Belangrijke punten uit de workspace-standaard zijn onder meer:

- verplichte root-folders voor docs/, governance/, templates/, temp/ en .github/;
- afspraken over docs/resultaten/ per agent, inclusief Moeder, Publisher en Presentatie Architect;
- eisen aan governance/ (beleid.md, gedragscode, rolbeschrijvingen);
- gebruik en uitsluiting van temp/ (tijdelijke plannen en context, niet in git);
- naamgevingsconventies voor folders en bestanden in document-repositories;
- minimale eisen aan README.md, .gitignore en Markdown-kwaliteit;
- validatiechecklist voor nieuwe en bestaande workspaces.

Voor de volledige, gedetailleerde standaard blijft het bestaande document leidend:

- artefacten/0-governance/workspace-standaard.md

Wanneer in charters, prompts of beleid wordt verwezen naar de "workspace-standaard" voor document-repositories, valt dit nu onder deze workspace-doctrine. Waar nodig kan nog direct naar het standaarddocument worden verwezen voor detail.

---

## 5. Gebruik van de workspace-doctrine

### 5.1 Door Moeder

Moeder gebruikt deze doctrine als norm bij:

- het inrichten van nieuwe workspaces;
- het ordenen en opschonen van bestaande workspaces;
- het beoordelen of voorstellen voor structuur passen binnen de afspraken;
- het schrijven en valideren van governance/beleid.md.

Waar in prompts en charters eerder letterlijk `governance/workspace-standaard.md` of alleen de workspace-architectuur werd genoemd, geldt nu deze workspace-doctrine als overkoepelend document.

### 5.2 Door Agent Smeder en andere agents

Agent Smeder en andere agents die prompts, charters of runners genereren:

- baseren mappen en bestandslocaties op deze workspace-doctrine;
- controleren of voorgestelde output-locaties met de doctrine in lijn zijn;
- verwijzen in tekst en voorbeelden naar deze doctrine als bron voor structuur en conventies.

### 5.3 Door beleidsmakers en architecten

Beleid- en architectuurdocumenten die iets zeggen over workspace-structuur:

- verwijzen naar deze workspace-doctrine als norm;
- kunnen waar nodig specificeren welk onderdeel relevant is (architectuur of document-standaard);
- vermijden dubbele of conflicterende definities buiten deze doctrine.

---

## 6. Relatie met andere governance

Bij conflicten geldt de volgende rangorde:

1. Constitutie (artefacten/0-governance/constitutie.md)
2. Workspace-doctrine (dit document)
3. Repository-specifiek beleid (bijvoorbeeld artefacten/0-governance/beleid-standard.md)
4. Agent-charters en prompts

De workspace-doctrine implementeert en concretiseert de vereisten uit de constitutie rond workspace-structuur, document-repositories en governance.

---

## 7. Wijzigingslog

| Datum      | Versie | Wijziging                                                           | Auteur            |
|------------|--------|---------------------------------------------------------------------|-------------------|
| 2026-01-14 | 1.0.0  | Eerste versie, bundelt workspace-architectuur en workspace-standaard in één workspace-doctrine | Charter Schrijver |
