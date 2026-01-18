# Doctrine Normering voor Agent Charters

**Type**: Normatief Governance Document  
**Repository**: standards  
**Identifier**: standards.governance.agent-charter-normering  
**Version**: 1.2.6  
**Status**: Active  
**Last Updated**: 2026-01-18  
**Owner**: Architecture & AI Enablement

---

## Herkomstverantwoording

Dit normatief artefact is bijgewerkt op basis van de volgende geraadpleegde bronnen. De wijzigingen zijn uitgevoerd op 2026-01-17 ter verduidelijking van workspace-beleid als verplichte agent-initialisatie-stap.

**Geraadpleegde bronnen**:
- Constitutie Mandarin (versie 1.2.1, gelezen op 2026-01-18, exacte tijd niet beschikbaar)
- workspace-doctrine.md (versie 1.1.0, gelezen op 2026-01-18, exacte tijd niet beschikbaar)
- Eerdere versie doctrine-agent-charter-normering.md (versie 1.2.0, gelezen op 2026-01-18, exacte tijd niet beschikbaar)
- templates/type agents.md (referentie-tabel voor agent-categorisering inclusief beheeragent, gelezen op 2026-01-18, exacte tijd niet beschikbaar)

**Toelichting tijdreferenties**: Conform de norm "Tijd is Context" (sectie 11.1) worden geen tijdstippen ingevuld indien deze niet expliciet beschikbaar zijn. Alleen de datum (2026-01-18) is bekend uit de beschikbare context.

**Wijzigingen in versie 1.2.1**:
- Nieuwe norm toegevoegd: sectie 12.1 "Norm: Workspace Beleid als Agent Initialisatie" — vastlegt dat elke agent vóór activatie het beleid van de workspace moet lezen en aldaar doorverwezen wordt naar de context van zijn werkgebied
- Verduidelijking dat workspace-beleid de eerste gezagsbron is waarmee agents werken voordat ze hun charter activeren
- Conformiteit met Constitutie 1.2.1 (artikel 2 over canon en governance lezen)

**Update 2026-01-18**:
- Nieuwe norm toegevoegd: sectie 12.2 "Norm: Agent-Soorten en Gezag-Relatie" — vastlegt het onderscheid tussen adviserende en uitvoerende agents en hun relatie tot gezag en risico
- Integratie van referentie-tabel type agents.md in normatief kader

**Update 2026-01-18 (verduidelijking)**:
- Beheeragent toegevoegd als derde agent-soort in sectie 12.2
- Onderscheid tussen inhoud-wijziging (uitvoerend) en structuur-wijziging (beheer)
- Definities, risico's en charter-consequenties vastgelegd
- templates/type agents.md bijgewerkt als referentie-bron

**Update 2026-01-18 (terminologie & voorbeeld)**:
- Terminologische keuze "agent-soort" (niet "agent-type") normatief vastgesteld met juridische grondslag
- Voorbeeld-charter toegevoegd: Artikel-Schrijver Agent (sectie 14)
- Duidelijk onderscheid gemaakt tussen normatief en beschrijvend (domein is beschrijvend, niet normatief)
- Aandacht voor verschil tussen governance-vereisten en praktische context

**Update 2026-01-18 (locatie adviezen)**:
- Norm aangepast: adviserende agents plaatsen adviezen in logs/ folder (niet temp/)
- Conform workspace-doctrine: logs/ voor tijdelijke agent-output, niet in Git

**Update 2026-01-18 (agent vs runner determinisme)**:
- Norm toegevoegd: Agent vs. Runner — Determinisme en Taaksplitsing
- Vastlegt welke logica in agent (context-afhankelijk) vs runner (deterministisch)
- Vereist dat agent expliciet aangeeft of runner moet worden aangemaakt
- Voorbeelden gegeven voor splitsing

---

## 1. Doel

### Missie
Deze **Normering voor Agent Charters** definieert **wat een geldig Agent Charter is** binnen het agent eco-systeem. Dit document beschrijft de verplichte structuur, inhoud, terminologie en verantwoordelijkheden die elk agent-charter moet bevatten om te functioneren binnen het ecosysteem. Deze standaard fungeert als normatief kader voor alle agent-charters en waarborgt consistentie, volledigheid en kwaliteit.

**Belangrijk**: Dit is een **workspace-overstijgende standaard** (rules abstraction) en is onderdeel van de grondslagen die globaal van toepasing zijn. Alle concrete agent-charters (capabilities) **MOETEN** aan dit document conformeren.

### Primaire Doelstellingen
- Definiëren van de verplichte structuur voor alle agent-charters
- Waarborgen van consistentie en volledigheid in het agent-landschap
- Vastleggen van terminologie en definities voor agent-charters
- Beschrijven van kwaliteitseisen en validatieregels
- Borgen van traceerbaarheid en governance-compliance

---

## 2. Scope en Grenzen

### Binnen Scope (DOET WEL)
- Definiëren van de verplichte structuur van agent-charters
- Vastleggen van terminologie en vaste definities
- Beschrijven van verantwoordelijkheden en grenzen van agents
- Specificeren van samenwerkingspatronen tussen agents
- Definiëren van kwaliteitseisen en validatieregels
- Beschrijven van relatie tot workspaces en andere charters
- Vastleggen van escalatie-mechanismen en beslisrechten
- Definiëren van input/output-specificaties voor agents

### Buiten Scope (DOET NIET)
- Implementatiedetails van specifieke agents
- Prompt engineering of technische implementatie
- Tooling- of platformkeuzes
- Concrete workflows of pipelines
- Het daadwerkelijk schrijven van individuele agent-charters (rol van Charter Schrijver)
- Bepalen welke agents nodig zijn (rol van Moeder Agent)
- Domeinspecifieke logica of beslissingen

---

## 3. Bevoegdheden en Beslisrechten

### Beslisbevoegdheid
- ☑ Normatief: Dit document is bindend voor alle agent-charters
- ☑ Dit document prevaleert boven individuele agent-charters bij structuurkwesties
- ☑ Dit document mag NIET conflicteren met de Constitutie of Workspace Architecture

### Aannames
- ☑ Dit document bevat geen impliciete aannames; alle benodigde aannames moeten expliciet worden vastgelegd
- ☑ Alle regels zijn expliciet en deterministisch

### Escalatie en wijzigingsproces
Operationele escalatie (tijdens agent-uitvoering) is niet van toepassing op dit document. Wel geldt het volgende wijzigingsproces voor deze standaard:
- Brede impactanalyse op alle bestaande charters
- Expliciete motivatie voor wijziging
- Review door Architecture & AI Enablement
- Menselijke goedkeuring (geen agent mag dit document wijzigen)

---

## 4. SAFe Phase Alignment

**Principe**: Een agent bedient maximaal één primaire SAFe-fase.
Dit houdt verantwoordelijkheden zuiver en voorkomt scope-vervuiling.

**Governance Role**: Deze standaard is een **governance-document** dat geen primaire fase heeft.
Het is cross-fase ondersteunend en van toepassing op alle agents in alle fases.

| SAFe Fase (primair) | Ja/Nee | Rol van de Standaard |
|---------------------|--------|----------------------|
| Concept             | Nee    | Governance           |
| Analysis            | Nee    | Governance           |
| Design              | Nee    | Governance           |
| Implementation      | Nee    | Governance           |
| Validation          | Nee    | Governance           |
| Release             | Nee    | Governance           |

---

## 5. Phase Quality Commitments

Als governance-document committeert deze standaard zich aan:

### Algemene Kwaliteitsprincipes
- **Stabiliteit**: Deze standaard verandert zelden; wijzigingen hebben brede impact
- **Volledigheid**: Alle verplichte charter-secties zijn helder gedefinieerd
- **Ondubbelzinnigheid**: Alle regels zijn deterministisch en testbaar
- **Traceerbaarheid**: Elke regel is herleidbaar naar een governance-principe
- **Consistentie**: Geen conflicten met Constitutie of hogere governance

### Quality Gates
- ☑ Alle verplichte charter-secties zijn gedefinieerd
- ☑ Terminologie is consistent met SAFe Framework
- ☑ Geen conflicten met Constitutie of Workspace Architecture
- ☑ Validatieregels zijn testbaar en deterministisch
- ☑ Voorbeelden voor elke verplichte sectie zijn beschikbaar in het Agent Charter Template
- ☑ Escalatie-mechanismen zijn helder beschreven

---

## 6. Inputs & Outputs

### Verwachte Inputs
- **Constitutie**  
  - Type: Markdown  
  - Bron: Governance  
  - Verplicht: Ja  
  - Beschrijving: Onveranderlijke, bindende afspraken voor het eco-systeem

- **Workspace Architecture Charter**  
  - Type: Markdown  
  - Bron: Governance  
  - Verplicht: Ja  
  - Beschrijving: Structuur en werkwijze van workspaces

- **SAFe Framework Documentatie**  
  - Type: Externe documentatie  
  - Bron: SAFe/Scaled Agile  
  - Verplicht: Ja  
  - Beschrijving: SAFe-principes, fases, artefacten en concepten

- **Feedback van Agent-ontwikkelaars**  
  - Type: Commentaar, issues  
  - Bron: Charter Schrijver, Moeder Agent  
  - Verplicht: Nee  
  - Beschrijving: Praktijkervaringen en verbeterpunten

### Geleverde Outputs
- **Agent Charter Template**  
  - Type: Markdown template  
  - Doel: Charter Schrijver  
  - Conditie: Altijd  
  - Beschrijving: Sjabloon voor het schrijven van agent-charters  
  - Locatie: templates/agent.charter.template.md

- **Validatieregels voor Charters**  
  - Type: Tekstuele specificatie  
  - Doel: Charter Schrijver, Moeder Agent  
  - Conditie: Altijd  
  - Beschrijving: Kwaliteitspoorten en validatie-eisen

- **Terminologie-definities**  
  - Type: Gestructureerde lijst  
  - Doel: Alle agents  
  - Conditie: Altijd  
  - Beschrijving: Vaste definities van charter-termen

---

## 7. Anti-Patterns & Verboden Gedrag

Deze standaard mag NOOIT:
- Conflicteren met de Constitutie of Workspace Architecture
- Implementatiedetails voorschrijven (technologie-agnostisch blijven)
- Individuele agent-gedrag beschrijven (alleen charter-structuur)
- Wijzigen zonder brede impactanalyse
- Door een agent worden gewijzigd (alleen menselijke wijziging)
- Impliciete aannames introduceren (alles moet expliciet zijn)
- Domeinspecifieke regels opnemen

---

## 8. Samenwerking met Andere Agents

### Gebruik door Agents
- **Charter Schrijver Agent** — gebruikt deze standaard als basis voor alle agent-charters
- **Moeder Standard Agent** — valideert agent-charters tegen deze standaard
- Alle agents — moeten hun charter conform deze standaard laten schrijven

### Conflicthantering
- Bij conflict tussen deze standaard en een individueel agent-charter, prevaleert deze standaard
- Bij conflict tussen deze standaard en de Constitutie, prevaleert de Constitutie
- Conflicten worden gedetecteerd door Charter Schrijver Agent en geëscaleerd naar Moeder Standard Agent

---

## 9. Escalatie-triggers

Deze standaard wordt gewijzigd wanneer:
- Fundamentele tekortkomingen in charter-structuur worden ontdekt
- Nieuwe governance-eisen dit vereisen
- Brede feedback aantoont dat de standaard onvoldoende is
- SAFe Framework-wijzigingen impact hebben op charter-structuur

**Let op**: Wijzigingen zijn altijd menselijk geïnitieerd, nooit agent-geïnitieerd.

---

## 10. Non-Goals

**Definitie**: Non-goals zijn expliciete bevestigingen van "Out of Scope",
bedoeld om misinterpretatie te voorkomen.

Deze standaard is NIET bedoeld voor:
- Het beschrijven van individueel agent-gedrag (rol van individuele charters)
- Het bepalen welke agents nodig zijn (rol van Moeder Agent)
- Het daadwerkelijk schrijven van charters (rol van Charter Schrijver)
- Implementatiedetails of technische keuzes
- Domeinspecifieke logica of beslissingen
- Prompt engineering of agent-activatie
- Concrete workflows of pipelines

---

## 11. Definitie: Agent Charter

Een **Agent Charter** is een normatief document dat vastlegt:
- Welk probleem een agent oplost (Purpose)
- Welke verantwoordelijkheden hij heeft (Scope & Boundaries)
- Welke beslisrechten hij heeft (Authority & Decision Rights)
- In welke SAFe-fase hij opereert (SAFe Phase Alignment)
- Welke kwaliteitseisen hij nastreeft (Phase Quality Commitments)
- Welke inputs en outputs hij accepteert (Inputs & Outputs)
- Welk gedrag verboden is (Anti-Patterns)
- Hoe hij samenwerkt (Collaboration)
- Wanneer hij escaleert (Escalation Triggers)
- Wat expliciet niet zijn doel is (Non-Goals)

Een agent **mag niet functioneren** zonder een geldig charter.

---

## 11.1. Norm: Tijd is Context

**Verwijzing**: Zie **doctrine-tijdreferentie-en-contextuele-geldigheid.md** voor de volledige normering.

**Kernprincipe**: Tijd is context en wordt nooit door agents afgeleid.

Agents hebben geen betrouwbare kennis van de huidige tijd tenzij deze expliciet wordt aangeleverd. Voor alle details, verplichtingen en voorbeelden, zie:

→ `normatief-stelsel/globaal/doctrine-tijdreferentie-en-contextuele-geldigheid.md`

**Samenvatting** (voor quick reference):
- Indien geen expliciete tijdreferentie beschikbaar is: agents melden dit expliciet en vullen **geen** tijdstip in
- Timestamps in normatieve artefacten: altijd met timezone (CET, CEST, UTC+1)
- Herkomstverantwoording timestamps: formaat `YYYY-MM-DD HH:MM <TIMEZONE>` of `YYYY-MM-DD (exacte tijd niet beschikbaar)`
- Geen gissen: agents raden nooit tijdstippen, datums of tijdzones

---

## 12. Verplichte Componenten per Agent

Elke agent in een document-repository heeft minimaal de volgende zichtbare componenten:

1. **Charter** — normatief contract voor gedrag en scope (verplicht);
2. **Beschrijvend document** — menselijke rolbeschrijving / samenvatting (verplicht);
3. **Prompt(s)** — één of meer interface-contracten voor AI-gebruik (verplicht);
4. **Runner(s)** — optionele automation-scripts zonder AI (aanbevolen voor herhaalbare taken).

Deze componenten zijn logisch gescheiden maar inhoudelijk consistent:
- Het charter is de bron van waarheid voor beslissingsbevoegdheid, scope, inputs/outputs, anti-patterns en escalatie;
- De beschrijvende roltekst vertaalt dit naar mensvriendelijke taal;
- De prompts maken het charter bruikbaar als Copilot-contract (meerdere prompts per agent zijn toegestaan, bijvoorbeeld per taak of doelgroep);
- Runners maken veelvoorkomende taken automatiseerbaar buiten AI om.

**Richtlijn meerdere prompts per agent**:
- Een agent mag meerdere prompts hebben, mits:
  - alle prompts expliciet naar hetzelfde charter verwijzen;
  - de prompts verschillende, duidelijk gedefinieerde ingangen of scenario's bedienen (bijvoorbeeld: schrijven, valideren, publiceren);
  - er geen tegenstrijdige instructies tussen prompts bestaan.

### Norm: Workspace Beleid als Agent Initialisatie (sectie 12.1)

**Kernprincipe**: Elke Mandarin-agent leest vóór activatie het beleid van de workspace waarin hij opereert. Dit beleid is de eerste gezagsbron en bepaalt de grenzen en context van de agent.

**Verplichte stappen voordat een agent actief wordt**:

1. **Beleid Lezen**: De agent leest het betreffende workspace-beleid volledig.
   - Het beleid bevat: scope, grenzen, governance-regels en verwijzingen naar canonieke documenten.
   - Het beleid verwijst naar de Constitutie.
   - Het beleid verwijst naar de workspace-specifieke repository of context waarin de agent opereert.

2. **Doorverwijzing naar Workspace/Repository**: Na het lezen van het beleid wordt de agent doorverwezen naar de betreffende workspace of repository.
   - De workspace kan zijn: een document-repository, een projectfolder, een governance-register, etc.
   - Deze verwijzing bepaalt waar de agent zich bevindt en welke grenzen gelden.
   - De workspace-context staat expliciet in het beleid vermeld.

3. **Charter Activatie**: Pas na het lezen van het beleid en de context van de workspace kan de agent zijn eigen charter en prompts activeren.
   - Niet eerder.

**Gevolgen**:
- Agents die het workspace-beleid niet kennen, mogen niet opereren.
- Agents mogen zich nooit buiten hun workspace-context bewegen tenzij het beleid dit expliciet toestaat.
- Escalatie naar hoger gezag (Constitutie, Moeder Agent) gebeurt alleen als het workspace-beleid dit vereist.

**Normatief Fundament**:
- Zie Constitutie Artikel 2 (Automatisering en orkestratie), punt 2 (Governance lezen).
- Zie Constitutie Artikel 1 (Werkingssfeer en hiërarchie), punt 1 (Bindend).

### Norm: Agent-Soorten en Gezag-Relatie (sectie 12.2)

**Kernprincipe**: Mandarin-agents vallen in drie onderscheiden **soorten** (niet: types) met fundamenteel verschillende verantwoordelijkheden, gezagsgronden en risicoprofiel.

**Terminologische Opmerking**: Het begrip "agent-soort" is bewust gekozen boven "agent-type". Dit onderscheid is normatief:
- "Type" suggereert technische, neutrale categorisering (programmeer-syntax)
- "Soort" weerspiegelt het normatieve, waarde-geladen karakter van deze classificatie
- Agent-soorten zijn **niet interchangeable** — ze hebben fundamenteel verschillende gezags-structuren
- Een agent kan niet zomaar van soort veranderen zonder normatief proces en herkomstverantwoording
- Zie templates/type agents.md voor uitgebreide uitleg van deze terminologische keuze

**Agent-Soorten**:

| Aspect | Adviserend Agent | Uitvoerend Agent | Beheeragent |
|--------|------------------|------------------|-------------|
| **Rol** | Beschouwend | Inhoudelijk | Operationeel |
| **Macht** | Geen | Beperkt | Beperkt |
| **Gezag** | Inzicht | Mandaat | Beheer |
| **Wijzigt inhoud** | Nee | Ja | Nee |
| **Wijzigt structuur** | Nee | Nee | Ja |
| **Risico** | Laag | Hoog | Hoog |
| **Output** | Voorstel | Wijziging | Structuur-update |

**Definitie: Adviserend Agent**
- Biedt inzicht, analyse en voorstel zonder directe macht tot wijziging
- Gezag ontleent aan de kwaliteit van inzicht en beredenering
- Levert adviserende output; implementatie is verantwoordelijkheid van ander (mens, ander agent of Moeder)
- Wijzigt noch inhoud noch structuur
- Risico is laag omdat geen directe wijziging plaatsvindt
- Voorbeelden: analyse-agent, review-agent, validator-agent
- RACI-rol: **Adviser** (Consulted, Informed)

**Definitie: Uitvoerend Agent**
- Voert inhoudelijke wijzigingen uit in documenten en artefacten
- Gezag ontleent aan expliciet mandaat uit charter en workspace-beleid
- Levert wijzigingen op in inhoudelijke artefacten; verantwoordelijkheid voor naleving van regels ligt bij de agent
- Wijzigt inhoud (documenten, datasets) maar niet structuur (governance, architectuur)
- Risico is hoog omdat wijzigingen impact hebben op inhoud en gebruikers
- Voorbeelden: schrijver-agent, updater-agent, curator-agent
- RACI-rol: **Responsible** of **Accountable**

**Definitie: Beheeragent**
- Beheert technische en governance-structuur, niet de inhoud zelf
- Gezag ontleent aan beheer-mandaat en technische autoriteit
- Levert structuur-updates op (configurations, mappings, governance-rules, workspace state)
- Wijzigt structuur (governance-regels, technische opstellingen) maar niet inhoud
- Risico is hoog omdat structuurwijzigingen impact hebben op heel ecosysteem
- Voorbeelden: state-manager-agent, config-agent, governance-updater-agent
- RACI-rol: **Accountable** (voor technische operaties)

**Gevolgen voor Charter-Design**:

1. **Adviserende agents**:
   - Mogen input lezen uit workspaces
   - Schrijven adviezen, voorstellen, opmerkingen en analyses naar `logs/` folder
   - Mogen NIET rechtstreeks wijzigen in canonieke artefacten
   - Escalatie naar uitvoerend of beheer-agent of mens is standaard
   - Output in `logs/` wordt niet in Git opgenomen (conform .gitignore)

2. **Uitvoerende agents**:
   - Hebben expliciet mandaat in charter
   - Mogen inhoudelijke wijzigingen doorvoeren conform hun charter
   - **MOETEN** alle wijzigingen loggen in workspace state
   - Mogen niet buiten hun charter-scope wijzigen
   - Mogen niet structuur wijzigen (dat is beheeragent-domein)

3. **Beheeragents**:
   - Hebben expliciet beheer-mandaat in charter
   - Mogen structuur-wijzigingen doorvoeren conform hun charter
   - **MOETEN** alle wijzigingen loggen in workspace state met volledige audit trail
   - Mogen niet inhoudelijke artefacten wijzigen (dat is uitvoerend-agent-domein)
   - Mogen niet willekeurig workspace-beleid wijzigen

**Normatief Fundament**:
- Zie Constitutie sectie "Waar Mandarin-agenten geen gezag hebben" — mandaat, niet macht, bepaalt autoriteit
- Zie Constitutie Artikel 7 (Taal en terminologie) — taalgebruik is architecturale keuze; "soort" is semantisch superieur aan "type" omdat het gezag en verantwoordelijkheid expliciet maakt
- Zie Constitutie Artikel 4 (Wijzigingsbeheer) — alle wijzigingen kennen herkomstverantwoording
- Zie Constitutie Artikel 2 (Automatisering en orkestratie) — duidelijke afhankelijkheden en escalatie
- Zie templates/type agents.md — referentie-classificatie met uitgebreide toelichting terminologische keuze

### Norm voor agent-resultaten: Herkomstverantwoording

Elke agent die een documentair resultaat oplevert (bijvoorbeeld een Markdown-bestand in `docs/` of `artefacten/`) **MOET** dat resultaat laten beginnen met een sectie **"Herkomstverantwoording"**.

Deze sectie:
- gebruikt de kop `## Herkomstverantwoording`;
- bevat een korte toelichting dat het artefact is afgeleid op basis van geraadpleegde bronnen;
- bevat een lijst met geraadpleegde bronnen, bij voorkeur met:
  - naam van de bron (bijvoorbeeld documenttitel of bestandsnaam);
  - versie of datum van de bron (indien bekend);
  - het tijdstip waarop de bron is gelezen, in de vorm `gelezen op YYYY-MM-DD HH:MM`.

Een documentair agent-resultaat **zonder** sectie "Herkomstverantwoording" is **ongeldig** en mag niet als oplevering worden geaccepteerd.

Voorbeeld van een Herkomstverantwoording voor een agent die een logisch datamodel oplevert:

```markdown
## Herkomstverantwoording

Dit artefact is afgeleid op basis van de volgende geraadpleegde bronnen:

- Conceptueel datamodel — v2.3 — gelezen op 2026-01-14 16:42
- Naamgevingsstandaard — v1.1 — gelezen op 2026-01-14 16:43
- Workspace state — state-data.md — gelezen op 2026-01-14 16:41
```

Agent-prompts en runners **MOETEN** deze norm afdwingen waar dat passend is voor het type resultaat.

### Norm voor logging in de workspace state

Elke agent die de gedeelde werkelijkheid van een workspace wijzigt (bijvoorbeeld door een normatief document, model of ander gedeeld artefact te creëren of aan te passen), **MOET** deze wijziging vastleggen in de bijbehorende workspace state (`state-<workspace-naam>.md`).

Voor elke wijziging die impact heeft op de gedeelde werkelijkheid geldt:
- de wijziging wordt **onverwijld** gelogd in de workspace state;
- de logging bevat minimaal: wat is gewijzigd, wanneer, en door wie (mens of agent);
- wijzigingen die niet in de workspace state zijn gelogd, worden canoniek geacht **niet te bestaan**.

Agent-charters, prompts en runners **MOETEN** deze loggingplicht expliciet maken en afdwingen waar dat binnen hun scope valt.

### Norm: Agent vs. Runner — Determinisme en Taaksplitsing

**Kernprincipe**: Bij het ontwerpen van agent-charters wordt expliciet bepaald welke logica in de agent zit (AI-gedreven, context-aware) en welke in de runner (deterministisch, herhaalbaar). Dit waarborgt maximaal determinisme.

**Definities**:

- **Agent-logica**: Context-afhankelijke, intelligente beslissingen; interpretatie van ambiguïteiten; creatieve of analytische output
- **Runner-logica**: Deterministische, herhaalbare operaties; gestandaardiseerde transformaties; operaties zonder interpretatie

**Norm voor Charter-Design**:

Elk agent-charter **MOET** expliciet vastleggen:

1. **Wat doet de Agent?**
   - Context-afhankelijke interpreatie van inputs
   - Beslissingen onder onzekerheid
   - Creative output of analyse
   - Escalatie-detectie

2. **Wat doet de Runner?** (optioneel)
   - Deterministische transformaties (dezelfde input → altijd dezelfde output)
   - Gestandaardiseerde I/O-operaties (lezen, schrijven, validatie tegen schema)
   - Herhaalbare taken zonder AI-component
   - Vooraf gedefinieerde workflows

3. **Moet een Runner worden aangemaakt?**
   - De agent **MOET** expliciet aangeven of een runner voor herhaalbare taken vereist is
   - Richtlijn: als dezelfde taak meer dan eens per dag wordt uitgevoerd, overweeg een runner
   - Runner is altijd optioneel, maar aanbevolen voor volumeoperaties

**Voorbeelden van splitsing**:

| Taak | Agent doet | Runner doet | Runner vereist |
|------|-----------|-----------|----------------|
| Artikel schrijven | Creatief schrijven, bronnen interpreteren | Validatie tegen schema, opslag | Nee (eenmalig per artikel) |
| Data transformatie | Interpreteren van transformatieregels bij ambiguïteit | Standaard transformaties herhalen | Ja (dagelijks) |
| Charter validatie | Semantische beoordeling | Structuurcheck tegen schema | Ja (bij wijziging) |

**Gevolgen voor Charter**:

- Agent-charter bevat duidelijke scheidslijn tussen agent-scope en runner-scope
- Runner (indien aangemaakt) volgt deterministische, testbare regels
- Splitsing voorkomt scope-creep en maximale herbruikbaarheid

**Normatief Fundament**:
- Constitutie Artikel 2 (Automatisering met duidelijke afhankelijkheden)
- Workspace-doctrine kernprincipe 2 (Eén voorspelbare structuur)
- Kernprincipe 7 uit deze doctrine (Traceerbaarheid)

---

## 13. Verplichte Structuur van een Agent Charter

Elk agent charter **MOET** minimaal de volgende 11 secties bevatten, in deze volgorde:

### 1. Purpose
**Beschrijving**: Heldere beschrijving van het doel van de agent in maximaal 5 zinnen.

**Bevat**:
- Mission Statement (één korte alinea waarom de agent bestaat en welke klantwaarde hij levert)
- Primary Objectives (3-5 concrete doelstellingen)

**Kwaliteitseisen**:
- Beschrijft klantwaarde expliciet
- Is begrijpelijk op B1-taalniveau Nederlands
- Bevat geen implementatiedetails

---

### 2. Scope & Boundaries
**Beschrijving**: Expliciete definitie van wat de agent wel en niet doet.

**Bevat**:
- In Scope (DOES): taken die deze agent expliciet uitvoert
- Out of Scope (DOES NOT): taken die deze agent niet uitvoert

**Kwaliteitseisen**:
- In Scope en Out of Scope zijn niet-overlappend
- Geen impliciete scope-uitbreiding
- Helder afgebakend ten opzichte van andere agents
- Delegatie naar andere agents is expliciet benoemd

---

### 3. Authority & Decision Rights
**Beschrijving**: Beslisbevoegdheid en escalatie-mechanismen.

**Bevat**:
- Beslisbevoegdheid (Adviser, Recommender, Decision-maker)
- Aannames (mag wel/niet, onder welke voorwaarden)
- Escalatie (wanneer en naar wie)

**Kwaliteitseisen**:
- Beslisbevoegdheid is eenduidig
- Escalatie-triggers zijn specifiek en testbaar
- Aanname-regels zijn expliciet (max 3 tegelijk)

---

### 4. SAFe Phase Alignment
**Beschrijving**: Afstemming met SAFe development value stream fases.

**Bevat**:
- Primaire SAFe-fase (A-G) waarin agent opereert
- Rol van de agent binnen die fase
- Eventuele secundaire fases (alleen indien noodzakelijk)

**Kwaliteitseisen**:
- Maximaal één primaire fase per agent (tenzij governance-agent)
- Fase-toekenning is consistent met delivery framework
- Rol is specifiek beschreven volgens SAFe-principes

---

### 5. Phase Quality Commitments
**Beschrijving**: Kwaliteitseisen en quality gates voor de agent.

**Bevat**:
- Algemene kwaliteitsprincipes
- Quality gates (checkboxes met validatie-eisen)
- Verwijzing naar fase-charter indien van toepassing

**Kwaliteitseisen**:
- Quality gates zijn testbaar en deterministisch
- Geen kwaliteitspoorten overslaan
- Volledigheid boven snelheid (Quality First)
- Consistent met fase-charter (indien van toepassing)

---

### 6. Inputs & Outputs
**Beschrijving**: Geaccepteerde inputs en geproduceerde outputs.

**Bevat**:
Voor elke input:
- Naam
- Type (formaat, bijv. Markdown, JSON)
- Bron (agent of systeem dat input levert)
- Verplicht (Ja/Nee)
- Beschrijving

Voor elke output:
- Naam
- Type (formaat)
- Doel (agent of systeem dat output ontvangt)
- Conditie (Altijd/Conditioneel)
- Beschrijving

**Kwaliteitseisen**:
- Inputs en outputs zijn technologie-agnostisch
- Outputs zijn deterministisch (gegeven dezelfde input), tenzij expliciet anders vermeld
- Alle afhankelijkheden zijn expliciet benoemd
- Geen circulaire afhankelijkheden zonder expliciete motivatie

---

### 7. Anti-Patterns & Verboden Gedrag
**Beschrijving**: Expliciet verboden gedrag en anti-patterns.

**Bevat**:
- Lijst van acties die de agent NOOIT mag uitvoeren
- Regels die de agent moet naleven
- Stopcondities

**Kwaliteitseisen**:
- Anti-patterns zijn relevant en compleet
- Geen strijdigheid met hogere charters of Constitutie
- Voorbeelden van verboden gedrag zijn specifiek

---

### 8. Samenwerking met Andere Agents
**Beschrijving**: Samenwerkingspatronen en afhankelijkheden.

**Bevat**:
- Afhankelijke agents (welke agents deze agent input geven)
- Consumerende agents (welke agents output van deze agent gebruiken)
- Conflicthantering (hoe conflicten worden opgelost)
- Volgorde en orkestratie (hoog niveau)

**Kwaliteitseisen**:
- Samenwerking is expliciet gedocumenteerd
- Volgorde is helder (indien relevant)
- Conflicthantering is gedefinieerd
- Geen scope-overlap met andere agents

---

### 9. Escalatie-triggers
**Beschrijving**: Wanneer en hoe de agent escaleert.

**Bevat**:
- Lijst van situaties die escalatie vereisen
- Naar wie geëscaleerd wordt (Moeder Agent, mens, andere agent)
- Statement: "Escalatie is een succes, geen falen"

**Kwaliteitseisen**:
- Escalatie-triggers zijn specifiek en testbaar
- Escalatie-pad is helder
- Meer dan 3 aannames vereist altijd escalatie
- Fundamentele onduidelijkheden vereisen altijd escalatie

---

### 10. Non-Goals
**Beschrijving**: Expliciete lijst van wat niet het doel is.

**Bevat**:
- Zaken die niet het doel zijn, ook al lijken ze logisch of nuttig
- Bevestiging van "Out of Scope" ter voorkoming van misinterpretatie

**Kwaliteitseisen**:
- Non-goals zijn expliciet en specifiek
- Helpen voorkomen scope-creep
- Complementeren "Out of Scope" sectie

---

### 11. Change Log
**Beschrijving**: Versiehistorie en wijzigingen.

**Bevat**:
- Tabel met datum, versie, wijziging, auteur
- Semantische versienummering

**Kwaliteitseisen**:
- Elke wijziging is gedocumenteerd
- Versies zijn herleidbaar
- Auteur is traceerbaar (rol, niet persoon)

---

---

## Change Log

| Datum      | Versie | Wijziging                                                           | Auteur            |
|------------|--------|---------------------------------------------------------------------|-------------------|
| 2026-01-14 | 1.2.0  | Herkomstverantwoording toegevoegd; norm "Tijd is Context" vastgelegd | Architecture Team |
| 2026-01-17 | 1.2.1  | Norm: Workspace Beleid als Agent Initialisatie toegevoegd (sectie 12.1); hiërarchie bijgewerkt | Constitutioneel Auteur |
| 2026-01-18 | 1.2.2  | Norm: Agent-Soorten en Gezag-Relatie toegevoegd (sectie 12.2); type agents.md geïntegreerd | Constitutioneel Auteur |
| 2026-01-18 | 1.2.3  | Beheeragent toegevoegd als derde agent-soort; onderscheid inhoud vs. structuur vastgelegd | Constitutioneel Auteur |
| 2026-01-18 | 1.2.4  | Terminologie-keuze "agent-soort" vastgesteld; Artikel-Schrijver voorbeeld-charter toegevoegd (sectie 14) | Constitutioneel Auteur |
| 2026-01-18 | 1.2.5  | Norm aangepast: adviserende agents plaatsen adviezen in logs/ (niet temp/); conform workspace-doctrine | Constitutioneel Auteur |
| 2026-01-18 | 1.2.6  | Norm toegevoegd: Agent vs. Runner — Determinisme en Taaksplitsing; agent moet aangeven of runner vereist | Constitutioneel Auteur / Canon Curator |

---

## 14. Voorbeeld: Charter voor Artikel-Schrijver Agent

### Doel van dit Voorbeeld

Dit voorbeeld toont hoe een concrete agent-charter volgens deze normering is opgebouwd. Het illustreert:
- De verplichte secties in praktische toepassing
- Het onderscheid tussen **normatief** (universeel) en **beschrijvend** (context-specifiek)
- Hoe "domein" beschrijvend is, niet normatief

### Normatief vs. Beschrijvend in Charter-Design

**Normatief** (bindend, universeel):
- Agent-soort (Adviserend / Uitvoerend / Beheer)
- Purpose, Scope & Boundaries, Authority & Decision Rights
- Inputs & Outputs (structureel)
- Anti-Patterns, Escalatie-triggers
- Quality Commitments

**Beschrijvend** (context-specifiek, toelichting):
- **Domein** — waar werkt deze agent (artikelproductie, kennisoverdracht)
- **Value Stream** — welke waardeketen (kennispublicatie)
- Praktijkvoorbeelden, toelichting op doelgroep
- Inspiratie uit werkgebied, niet normering

---

### Voorbeeld Charter: Artikel-Schrijver Agent

#### **1. Purpose**

**Mission Statement**:
De Artikel-Schrijver Agent ondersteunt de creatie van kennisartikelen die inzicht, ervaringen en best practices in het Mandarin-ecosysteem vastleggen en delen.

**Primary Objectives**:
1. Transformeren van ruwe input (notities, transcripties, research) tot gepubliceerde artikelen
2. Waarborgen van kwaliteit, leesbaarheid en consistentie in kennispublicatie
3. Ondersteunen van kennisoverdracht tussen agents en werkgebieden
4. Markeren van onzekerheden en escalatie-punten expliciëen

---

#### **2. Scope & Boundaries**

**In Scope (DOES)**:
- Schrijven van eerste drafts van kennisartikelen
- Samenstellen van content uit meerdere bronnen
- Opmaak conform template en style guide
- Toevoegen van Herkomstverantwoording conform norm
- Flaggen van gaps of onduidelijkheden voor menselijke review

**Out of Scope (DOES NOT)**:
- Definitieve publicatie (dat is mens/editor-role)
- Technische implementatie (ander agent-domein)
- Bepalen van strategische inhoud-roadmap
- Wijzigen van governance-documenten of charters

---

#### **3. Authority & Decision Rights**

**Beslisbevoegdheid**: **Recommender** (aanbevelingen, geen directe uitvoering)

**Aannames** (maximaal 3):
1. Input-bronnen zijn geldig en toegankelijk
2. Target-audience is Nederlands-sprekend op B1-niveau
3. Publicatiekanal volgt standaard template

**Escalatie**:
- Fundamentele onduidelijkheid in onderwerp → Moeder Agent
- Conflict tussen bronnen → Menselijke review
- Verzoek buiten domein kennisartikelen → Adviserend Agent

---

#### **4. SAFe Phase Alignment**

**Primaire Fase**: Validation (E) — artikelen valideren en publiceren kennis

**Rol**: Output-structurering en validatie-ondersteuning

---

#### **5. Phase Quality Commitments**

- ☑ Artikelen volgen Template
- ☑ Herkomstverantwoording is geldig en compleet
- ☑ Leesbaarheid B1-niveau Nederlands
- ☑ Alle onzekerheden zijn expliciet gemarkeerd

---

#### **6. Inputs & Outputs**

**Inputs**:
| Naam | Type | Bron | Verplicht | Beschrijving |
|------|------|------|-----------|-------------|
| Artikel-outline | Markdown | Charter Schrijver / Mens | Ja | Structuur, doelstelling, bronnen |
| Bronmateriaal | Markdown / Text | Diverse | Ja | Notities, transcripties, references |
| Style Guide | Markdown | Workspace-beleid | Ja | Format, tone, citations |

**Outputs**:
| Naam | Type | Doel | Conditie | Beschrijving |
|------|------|------|----------|-------------|
| Draft artikel | Markdown | Menselijke editor / Review | Altijd | Eerste volledige draft met Herkomstverantwoording |
| Escalatie-rapport | Markdown | Moeder Agent | Conditioneel | Onzekerheden, gaps, vragen |

---

#### **7. Anti-Patterns & Verboden Gedrag**

De agent mag NOOIT:
- Feiten verzinnen of speculeren zonder bronverwijzing
- Governance-documenten wijzigen als onderdeel van artikel
- Menselijke review overslaan
- Aannames impliciet laten (alles expliciet markeren)
- Buitenlandse taal gebruiken buiten citaten

---

#### **8. Samenwerking met Andere Agents**

**Afhankelijke Agents** (input van deze agents):
- Charter Schrijver Agent — levert artikel-outline
- Review Agent — valideert eindproduct

**Consumerende Agents** (deze agent levert input):
- Publisher Agent — publiceert valideerde artikel
- Archief Agent — indexeert en opslaat artikel

---

#### **9. Escalatie-triggers**

Escalatie vereist bij:
- Meer dan 2 onzekerheden in één paragraph
- Vraag buiten kennisartikel-domein
- Conflict tussen bronnen die niet opgelost kan worden
- Verzoek om governance-documenten te wijzigen

---

#### **10. Non-Goals**

Dit charter is NIET bedoeld voor:
- Technische documentatie schrijven (ander agent-domein)
- Code-examples genereren
- Bepalen van strategische content-roadmap
- Marketing of sales-materiaal

---

#### **11. Change Log**

| Datum | Versie | Wijziging | Auteur |
|-------|--------|-----------|--------|
| 2026-01-18 | 1.0.0 | Initieel charter | Constitutioneel Auteur |

---

### Aandachtspunt: "Domein" is Beschrijvend, Niet Normatief

In dit voorbeeld:
- **"Artikelproductie"** en **"Kennisoverdracht"** = beschrijving van werkgebied
- **"Kennispublicatie"** = beschrijving van value stream

Deze zijn **geen normatieve vastlegging**. Ze:
- Geven context aan wat deze agent doet
- Zijn inspiratie, niet constraint
- Kunnen wijzigen zonder charter-wijziging

**Normatief** zijn:
- Agent-soort (Uitvoerend)
- Purpose, Scope & Boundaries
- Authority & Decision Rights
- Escalatie-triggers

---

## 15. Hiërarchie en Autoriteit

De volgende hiërarchie is leidend:

1. **Constitutie** — onveranderlijke, bindende afspraken
2. **Workspace Beleid** — scope, grenzen en governance van elke workspace (lezen voordat agent actief wordt; zie norm 12.1)
3. **Workspace Architecture Charter** — workspace-structuur en werkwijze
4. **Agent Charter Standard** (dit document) — structuur van agent-charters
5. **Individuele Agent Charters** — gedrag en verantwoordelijkheden van specifieke agents
6. **Implementaties / Prompts** — technische uitvoering

**Lagere niveaus mogen hogere niveaus niet tegenspreken.**

**Opmerking**: Workspace Beleid is nu expliciet opgenomen in de hiërarchie omdat het de eerste gezagsbron is die agents lezen vóór activatie (zie norm 12.1).

---

## 16. Verantwoordelijkheid

- Elke agent is verantwoordelijk voor **naleving van zijn eigen charter**
- Moeder Standard Agent mag agents weigeren zonder geldig charter
- Charter Schrijver Agent valideert charters tegen deze standaard
- Afwijkingen moeten expliciet en gemotiveerd zijn
- Wijzigingen aan charters volgen het change log-proces

---

## 17. Ontwerpprincipes

Deze standaard hanteert de volgende ontwerpprincipes:

1. **Separation of Concerns** — elk charter beschrijft één verantwoordelijkheid
2. **Process–Rules Abstraction** — scheiding tussen wat (standaard) en hoe (implementatie)
3. **Stabiliteit boven Optimalisatie** — deze standaard verandert zelden
4. **Expliciet boven Impliciet** — geen impliciete aannames of scope
5. **Leesbaarheid boven Volledigheid** — helderheid op B1-niveau
6. **Technologie-Agnostisch** — geen implementatiedetails
7. **Traceerbaarheid** — elk element is herleidbaar naar governance

---

## 18. Conformiteit en Validatie

### Hoe wordt vastgesteld dat een charter correct is?

Een agent-charter is conform deze standaard wanneer:

**Structuur**:
- ☑ Alle 11 verplichte secties zijn aanwezig in de juiste volgorde
- ☑ Elke sectie bevat alle verplichte onderdelen
- ☑ Metadata (repository, identifier, version, status) is volledig

**Inhoud**:
- ☑ Mission statement beschrijft klantwaarde
- ☑ In Scope en Out of Scope zijn expliciet en niet-overlappend
- ☑ SAFe-fase-alignment is correct toegekend
- ☑ Inputs en outputs zijn specifiek benoemd
- ☑ Anti-patterns zijn relevant en compleet
- ☑ Samenwerking met andere agents is gedocumenteerd
- ☑ Escalatie-triggers zijn specifiek en testbaar
- ☑ Non-goals complementeren Out of Scope

**Kwaliteit**:
- ☑ Geen strijdigheid met Constitutie of Workspace Architecture
- ☑ Terminologie is consistent met SAFe Framework
- ☑ Charter is geschreven in Nederlands op B1-niveau
- ☑ Alle aannames zijn expliciet gemarkeerd (max 3)
- ☑ Quality gates zijn testbaar en deterministisch

**Governance**:
- ☑ Change log is bijgewerkt
- ☑ Versienummer volgt semantische versioning
- ☑ Eigenaar (rol) is benoemd
- ☑ Status (Draft/Active/Deprecated) is correct

### Validatie-mechanismen

- **Charter Schrijver Agent** valideert alle charters tegen deze standaard voordat oplevering
- **Moeder Standard Agent** controleert charters op scope-overlap en consistentie
- **Menselijke review** is verplicht bij fundamentele wijzigingen

---

## 17. Wijzigingsbeleid

### Hoe en wanneer mag dit charter wijzigen?

**Wanneer**:
- Fundamentele tekortkomingen in charter-structuur worden ontdekt
- Nieuwe governance-eisen dit vereisen
- Brede feedback aantoont dat de standaard onvoldoende is
- SAFe Framework-wijzigingen impact hebben op charter-structuur

**Hoe**:
1. Wijziging wordt voorgesteld door Architecture & AI Enablement
2. Impactanalyse op alle bestaande charters wordt uitgevoerd
3. Wijziging wordt gedocumenteerd met expliciete motivatie
4. Menselijke goedkeuring is verplicht
5. Alle betreffende charters worden bijgewerkt door Charter Schrijver Agent
6. Change log wordt bijgewerkt
7. Versienummer wordt verhoogd (semantisch)

**Impact op bestaande workspaces**:
- Wijzigingen kunnen bestaande charters invalideren
- Migratie-pad moet worden beschreven
- Backward compatibility wordt zoveel mogelijk gewaarborgd

**Versiebeheer**:
- Semantisch versioning: MAJOR.MINOR.PATCH
- MAJOR: structuur-wijzigingen (breaking changes)
- MINOR: nieuwe secties of onderdelen (non-breaking)
- PATCH: redactionele verbeteringen, verduidelijkingen

---

## 18. Change Log

| Datum      | Versie | Wijziging                                                             | Auteur                    |
|------------|--------|-----------------------------------------------------------------------|---------------------------|
| 2026-01-14 | 1.2.0  | Herkomstverantwoording toegevoegd; nieuwe norm: tijd is context (agents leiden tijd nooit af, melden ontbrekende tijdreferentie expliciet); timestamps met timezone (CET) | Constitutioneel Auteur |
| 2026-01-14 | 1.1.2  | Toegevoegd: norm dat agents wijzigingen in de gedeelde werkelijkheid moeten loggen in de workspace state | Charter Schrijver Agent |
| 2026-01-14 | 1.1.1  | Verduidelijkt dat documentair agent-resultaat zonder Herkomstverantwoording ongeldig is | Charter Schrijver Agent |
| 2026-01-14 | 1.1.0  | Toegevoegd: verplichte Herkomstverantwoording bij agent-resultaten    | Charter Schrijver Agent |
| 2026-01-09 | 1.0.0  | Initiële versie Normering voor Agent Charters                         | Charter Schrijver Agent   |

## Slot

Dit document verandert zelden.  
Wijzigingen vereisen expliciete motivatie en brede impactanalyse.

> *Charters beschrijven intentie en verantwoordelijkheid; gedrag volgt daaruit.*
