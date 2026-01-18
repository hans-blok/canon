# Workspace Doctrine — Architectuur en Standaard voor Workspaces

**Versie**: 1.2.0  
**Status**: Actief  
**Datum**: 2026-01-18  
**Eigenaar**: Architecture & AI Enablement  
**Type**: Normerend Doctrine-document

---

## Herkomstverantwoording

Dit normatief artefact is afgeleid op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- artefacten/0-governance/workspace-architectuur.md (versie 1.0.0, gelezen op 2026-01-14 14:30 CET)
- artefacten/0-governance/workspace-standaard.md (gelezen op 2026-01-14 14:30 CET)
- artefacten/0-governance/constitutie.md (versie 1.2.1, gelezen op 2026-01-18 14:20 CET)
- Gebruikersinstructies voor root-structuur aanpassing (ontvangen op 2026-01-14 14:35 CET)
- Gebruikersinstructies voor locatie agent-resultaten (ontvangen op 2026-01-18 14:20 CET)

**Wijzigingen in versie 1.1.0**:
- Root-structuur specificatie aangescherpt: verplichte folders (.github, beleid, docs, scripts) en logs (in gitignore)
- Root-bestanden gespecificeerd: .gitignore, README.md, <workspace>.ping, state-<naam-workspace>
- Herkomstverantwoording sectie toegevoegd conform agent-charter-normering.md

**Wijzigingen in versie 1.2.0**:
- Norm toegevoegd voor locatie van agent-resultaten (sectie 5.1): resultaten van value stream Kennispublicatie → docs/, templates → altijd in templates/
- Herkomstverantwoording bijgewerkt met constitutie v1.2.1 en gebruikersinstructies

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

## 3. Root-structuur voor workspaces

Elke workspace **moet** de volgende root-structuur hebben:

**UITZONDERING**: Deze structuur is niet van toepassing op de workspaces **agent-services** en **canon**. Deze workspaces volgen een eigen, specifieke architectuur buiten deze doctrine.

### 3.1 Verplichte folders in root

```
<workspace-root>/
├── .github/          # GitHub-specifieke configuratie (prompts, workflows, copilot)
├── beleid/           # Workspace-specifiek beleid (NIEUW: vervangt governance/ in sommige gevallen)
├── docs/             # Documentatie, diagrammen en agent-resultaten
├── scripts/          # Automatiseringsscripts en runners
└── logs/             # Logbestanden van agent-uitvoer (in .gitignore, niet in Git)
```

**Toelichting**:
- **.github/**: Bevat prompts (.github/prompts/), workflows (.github/workflows/) en copilot configuratie (.github/copilot/)
- **beleid/**: Workspace-specifieke beleidsregels, gedragscode en charters
- **docs/**: Alle documentatie inclusief docs/resultaten/{agent-naam}/ voor agent-output
- **scripts/**: Python runners en hulpscripts voor agents
- **logs/**: Tijdelijke logbestanden, **altijd in .gitignore**

### 3.2 Verplichte bestanden in root

```
<workspace-root>/
├── .gitignore                    # Git ignore regels (verplicht)
├── README.md                     # Workspace documentatie (verplicht)
├── <workspace>.ping              # Ping-bestand voor normatief stelsel synchronisatie
└── state-<naam-workspace>.md     # Workspace state logging (conform workspace-state doctrine)
```

**Toelichting**:
- **.gitignore**: Moet minimaal logs/ en temp/ uitsluiten
- **README.md**: Beschrijft workspace doel, structuur en beschikbare agents
- **<workspace>.ping**: Bijvoorbeeld `standard.ping`, `agent-capabilities.ping` - gebruikt voor normatief stelsel actualiteit
- **state-<naam-workspace>.md**: Bijvoorbeeld `state-standard.md` - logt wijzigingen aan canonieke/normatieve artefacten conform doctrine-workspace-state-en-legitimiteit.md

**Let op**: De folders artefacten/ en templates/ zijn optioneel en afhankelijk van workspace-type (zie onderdeel 1: workspace-architectuur voor details).

---

## 4. Onderdeel 1: Workspace-architectuur (alle workspaces)

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

## 5. Onderdeel 2: Workspace-standaard voor document-repositories

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

## 5.1 Norm: Locatie van Agent-Resultaten

**Kernprincipe**: Agent-resultaten worden opgeslagen op voorspelbare locaties conform hun value stream en artefact-type. Dit waarborgt traceerbaarheid en consistente structuur (kernprincipe 3 van deze doctrine).

**Norm**:

1. **Value Stream Kennispublicatie** → **docs/**  
   Alle agent-resultaten die vallen binnen de value stream Kennispublicatie (artikelen, documentatie, analyses, kennisoverdracht) worden opgeslagen in de `docs/` folder en subfolders daarvan, conform de structuur `docs/resultaten/{agent-naam}/`.

2. **Templates** → **altijd templates/**  
   **Uitzondering**: Templates vormen altijd een uitzondering op de bovenstaande regel. Alle templates (ongeacht value stream of agent-soort) worden opgeslagen in de `templates/` folder. Dit geldt voor:
   - Charter-templates
   - Document-templates  
   - Prompt-templates
   - Fase-charter-templates
   - Alle andere herbruikbare structuren

**Motivatie**:
- **Voorspelbaarheid**: Agents en mensen weten waar resultaten te vinden zijn
- **Traceerbaarheid**: Resultaten zijn herleidbaar naar agent en value stream (kernprincipe 3)
- **Scheiding van concerns**: Templates zijn herbruikbare structuren en horen daarom in een aparte folder, onafhankelijk van de value stream waarbinnen ze ontstaan
- **Consistentie met Constitutie**: Volgt Artikel 2 (Canon, Governance lezen, Samenwerking met duidelijke taakverdeling)

**Voorbeelden**:

| Agent-resultaat | Value Stream | Locatie |
|-----------------|--------------|---------|
| Kennisartikel | Kennispublicatie | `docs/resultaten/artikel-schrijver/` |
| Analyse-rapport | Kennispublicatie | `docs/resultaten/moeder/` |
| Charter-template | N.v.t. | `templates/agent.charter.template.md` |
| Fase-charter-template | N.v.t. | `templates/phase.charter.template.md` |
| Prompt-template | N.v.t. | `templates/agent-prompt.template.md` |

**Gevolgen voor Agent-Charters en Prompts**:
- Alle agents die output leveren **MOETEN** deze norm respecteren
- Agent-prompts specificeren de correcte output-locatie conform deze norm
- Afwijkingen van deze norm zijn **alleen** toegestaan indien expliciet gemotiveerd in het agent-charter en goedgekeurd door Architecture & AI Enablement

---

## 6. Gebruik van de workspace-doctrine

### 6.1 Door Moeder

Moeder gebruikt deze doctrine als norm bij:

- het inrichten van nieuwe workspaces;
- het ordenen en opschonen van bestaande workspaces;
- het beoordelen of voorstellen voor structuur passen binnen de afspraken;
- het schrijven en valideren van governance/beleid.md.

| 2026-01-18 | 1.2.0  | Norm toegevoegd voor locatie van agent-resultaten (sectie 5.1): value stream Kennispublicatie → docs/, templates → altijd templates/ | Constitutioneel Auteur |
Waar in prompts en charters eerder letterlijk `governance/workspace-standaard.md` of alleen de workspace-architectuur werd genoemd, geldt nu deze workspace-doctrine als overkoepelend document.

### 6.2 Door Agent Smeder en andere agents

Agent Smeder en andere agents die prompts, charters of runners genereren:

- baseren mappen en bestandslocaties op deze workspace-doctrine;
- controleren of voorgestelde output-locaties met de doctrine in lijn zijn;
- verwijzen in tekst en voorbeelden naar deze doctrine als bron voor structuur en conventies.

### 6.3 Door beleidsmakers en architecten

Beleid- en architectuurdocumenten die iets zeggen over workspace-structuur:

- verwijzen naar deze workspace-doctrine als norm;
- kunnen waar nodig specificeren welk onderdeel relevant is (architectuur of document-standaard);
- vermijden dubbele of conflicterende definities buiten deze doctrine.

---

## 7. Relatie met andere governance

Bij conflicten geldt de volgende rangorde:

1. Constitutie (artefacten/0-governance/constitutie.md)
2. Workspace-doctrine (dit document)
3. Repository-specifiek beleid (bijvoorbeeld artefacten/0-governance/beleid-standard.md)
4. Agent-charters en prompts

De workspace-doctrine implementeert en concretiseert de vereisten uit de constitutie rond workspace-structuur, document-repositories en governance.

---

## 8. Wijzigingslog

| Datum      | Versie | Wijziging                                                           | Auteur            |
|------------|--------|---------------------------------------------------------------------|-------------------|
| 2026-01-14 | 1.0.0  | Eerste versie, bundelt workspace-architectuur en workspace-standaard in één workspace-doctrine | Charter Schrijver |
| 2026-01-14 | 1.1.0  | Root-structuur aangescherpt: verplichte folders (.github, beleid, docs, scripts, logs), verplichte root-bestanden (.gitignore, README.md, <workspace>.ping, state-<naam-workspace>.md), Herkomstverantwoording sectie toegevoegd | Constitutioneel Auteur |
| 2026-01-16 | 1.1.1  | UITZONDERING toegevoegd: workspace-doctrine structuur niet van toepassing op workspaces agent-services en canon | Canon Curator |
