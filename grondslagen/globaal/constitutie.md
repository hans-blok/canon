# Constitutie van het Eco-systeem

**Versie**: 1.2.0
**Status**: Actief
**Datum**: 2026-01-16

---

## Herkomstverantwoording

Dit normatief artefact is afgeleid op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- Eerdere versie constitutie.md (versie 1.1.0, gelezen op 2026-01-14)
- workspace-doctrine.md (versie 1.1.0, gelezen op 2026-01-16)
- agent-charter-normering.md (versie 1.2.0, gelezen op 2026-01-16)
- Handoff: handoff-runner-constitutioneel-auteur-20260115-0936 (context voor herstructurering)

**Wijzigingen in versie 1.2.0**:
- Artikel 2 (Workspace Structuur) ingekort tot verwijzing naar workspace-doctrine.md (detail naar doctrine verplaatst)
- Artikel 4 (Automatisering en Orkestratie) verplaatst naar Artikel 2 (prioriteitsherordening)
- Artikelen hernummerd (3-8 → 3-8)
- Herkomstverantwoording sectie toegevoegd conform agent-charter-normering.md
- Verwijzingen naar gerelateerde doctrines toegevoegd

---

## Inleiding

Waar de **Gedragscode** zich richt op gedrag, principes en professionele normen, beschrijft de **Constitutie** de onveranderlijke, harde afspraken die de structuur en werking van het gehele eco-systeem vastleggen. Deze regels zijn bindend en staan boven alle andere beleidsdocumenten, charters of specificaties.

---

## Artikel 1 — Werkingssfeer en Hiërarchie

1.  **Bindend**: Deze constitutie geldt voor alle repositories, workflows en artefacten binnen het eco-systeem.
2.  **Hiërarchie**: Bij conflict prevaleert de Constitutie altijd boven de Gedragscode, beleidsdocumenten, charters of andere specificaties. Lagere documenten mogen de Constitutie niet tegenspreken, verzwakken of negeren.
3.  **Doel**: De Constitutie waarborgt voorspelbaarheid, kwaliteit, veiligheid en traceerbaarheid.
4.  **Taalgebruik en Communicatie**: Communicatie binnen het eco-systeem is formeel, duidelijk, eenvoudig en minimaal op taalniveau B1; discriminerend, beledigend of vijandig taalgebruik is verboden.

---

## Artikel 2 — Automatisering en Orkestratie

1.  **Canon**: Voor alle agents in alle processen is de canon van toepassing. Het beleid in elke workspace verwijst naar deze consitutie om te borgen dat de canon op de juiste manier wordt gevolgd.
2.  **Canon Repository Synchronisatie**: Wanneer de centrale canon repository (`https://github.com/hans-blok/canon.git`) wordt geraadpleegd, wordt altijd eerst een `git pull` uitgevoerd om te waarborgen dat de meest recente governance, charters en definities worden gebruikt. Wanneer de canon niet kan worden gelezen wordt het proces afgebroken en wordt een nette foutmelding gegeven.
1.  **Governance Lezen**: Van toepassing voor alle geautomatiseerde processen en handmatige processen zijn de grondslagen die als onderdeel van de canon zijn vastgelegd. 
3.  **Samenwerking**: Automatisering werkt samen met een duidelijke taakverdeling, minimale overlap en expliciete afhankelijkheden.
4.  **Conflictmelding**: Wanneer een geautomatiseerd proces conflicten vindt tussen documenten of regels, meldt het dit direct en expliciet.
5.  **Einddoel**: Het eco-systeem streeft naar een toekomst waarin een feature met slechts vijf regels input veilig en robuust kan worden gegenereerd.
6.  **Plannen Vastleggen**: Wanneer een geautomatiseerd proces wordt gevraagd om een plan (ontwerp, voorstel of werk-in-uitvoering), legt dat proces dit plan als Markdown-bestand vast in de `temp/` map van de betreffende workspace. Een mens beoordeelt het plan. Na beoordeling kan het plan uit `temp/` worden verwijderd. Inhoud die blijvend nodig is, wordt vastgelegd in duurzame documenten (bijvoorbeeld `README.md`), niet in `temp`.

---

## Artikel 3 — Workspace Structuur

Zie: [grondslagen/globaal/workspace-doctrine.md](grondslagen/globaal/workspace-doctrine.md)

---

## Artikel 4 — Kwaliteit en compliance

4.  **Aannames**: Onzekerheden worden altijd expliciet gemarkeerd. Een geautomatiseerd proces mag maximaal drie aannames tegelijk hanteren voordat escalatie naar een mens verplicht is.
5.  **Professionele Normen**: Alle aanbevelingen en artefacten ondersteunen iteratief werken met focus op waarde en snelle feedback, en dragen bij aan:
    *   duurzaam ontwerp;
    *   robuuste systemen;
    *   lage onderhoudslast;
    *   heldere en testbare specificaties.
6.  **Veiligheid, Privacy en Integriteit**: Het eco-systeem verwerkt gegevens met respect voor privacy, veiligheid en wetgeving. Risico's worden geminimaliseerd door:
    *   veilige defaults;
    *   geen verwerking van gevoelige data zonder noodzaak;
    *   duidelijke waarschuwingen bij risico's.
    Integriteit van informatie heeft altijd voorrang op snelheid.

---

## Artikel 5 — Wijzigingsbeheer

1.  **Menselijke Controle**: Inhoudelijke wijzigingen aan de Constitutie (nieuwe regels, gewijzigde principes) mogen **door een mens** en door **de agent constitutioneel-auteur** worden gedaan.
3.  **Verbod voor Automatisering**: Geautomatiseerde tooling of processen mogen de Constitutie op geen enkele wijze wijzigen.
4.  **Versiebeheer**: Versies worden beheerd via duidelijke versie-nummers en een wijzigingslog.
5. Alle wijzigingen in de canon kennen een herkomstverantwoording. Dit is verder uitgewerkt in doctrine-handoff-creatie-en-overdrachtsdiscipline.md.
---

## Artikel 6 — Tegen Generalisatie

1.  **Precisie**: Wij spreken precies, of wij spreken niet.
    *   Wij zeggen niet "mensen" wanneer wij patronen bedoelen.
    *   Wij zeggen niet "agenten" wanneer wij implementaties bedoelen.
    *   Wij zeggen niet "dit gebeurt" wanneer wij "dit zien wij soms" bedoelen.

2.  **Abstractie**: Wij generaliseren niet uit gemak. Wij abstraheren alleen wanneer de onderliggende structuur aantoonbaar gedeeld is.

3.  **Kritiek Formuleren**: Wanneer wij kritiek formuleren:
    *   Benoemen wij waargenomen ontwerpkeuzes, geen groepen mensen.
    *   Spreken wij over impliciete aannames, niet over intenties.
    *   Richten wij ons op structuren, niet op schuld.

4.  **Onderscheid**: 
    *   Wij verwarren frequentie niet met universaliteit.
    *   Wij verwarren voorbeelden niet met wetten.
    *   Wij verwarren vroege experimenten niet met volwassen architectuur.

5.  **Beweringen**: Elke bewering is:
    *   **Gesitueerd**: in context geplaatst.
    *   **Begrensd**: met expliciete reikwijdte.
    *   **Herleidbaar**: naar observatie of principe.

6.  **Nuance en Scherpte**: Waar nuance nodig is, voegen wij nuance toe. Waar scherpte nodig is, maken wij grenzen expliciet — niet breder.

7.  **Fundament**: Generaliserende taal is een teken van onontworpen denken. Architectuur begint waar precisie wordt afgedwongen.

---

## Artikel 7 — Taal en terminologie

1.  **Standaardtaal**  
    De standaardtaal binnen het eco-systeem, en binnen alle canonieke en
    normatieve artefacten die rechtstreeks uit de Constitutie voortvloeien,
    is **Nederlands**.

    Dit geldt in ieder geval voor:
    - principes, doctrines en gedragscodes;
    - rolbenamingen en verantwoordelijkheden;
    - architecturale beschrijvingen en verklarende teksten.

2.  **Geleende termen uit bestaande kaders**  
    Wanneer terminologie **bewust wordt geleend** uit een bestaand
    architectuur- of denkkader, wordt de **oorspronkelijke Engelse term
    gehandhaafd**.

    Dit geldt onder meer voor:
    - formele begrippen uit modellering- en architectuurframeworks (bijv. *value stream*, *capability*);
    - expliciet benoemde concepten uit externe theorieën of publicaties.

    Doel hiervan is:
    - duidelijk maken dat het begrip **niet intern is bedacht**;
    - herleidbaarheid naar het bronkader te behouden;
    - semantische vervorming door vertaling te voorkomen.

3.  **Termen met gevestigde betekenis in IT-context**  
    Sommige begrippen hebben binnen IT-ontwikkeling een zodanig gevestigde
    betekenis dat een Nederlandse vertaling kunstmatig aanvoelt, verwarring
    oproept of afwijkt van gangbaar professioneel taalgebruik.

    In dat geval wordt de **Engelse term gebruikt als primaire term**, ook in
    Nederlandstalige tekst. Voorbeelden zijn onder meer:
    - *service*;
    - *contract*;
    - *boundary*.

    Deze keuze is pragmatisch maar niet vrijblijvend: de Engelse term wordt
    alleen gebruikt wanneer zij **duidelijker, preciezer of stabieler** is dan
    het Nederlandse alternatief.

4.  **Normatief uitgangspunt**  
    Afwijking van het Nederlands is nooit impliciet. Elke Engelse term moet:
    - óf aantoonbaar uit een extern kader zijn geleend;
    - óf aantoonbaar semantisch superieur zijn in de gegeven context.

    Taalgebruik wordt behandeld als een **architecturale keuze**, niet als puur
    stijlelement.

---

## Artikel 8 — Slotbepaling

1.  **Onmiddellijke Werking**: Deze Constitutie geldt onmiddellijk voor alle bestaande en toekomstige repositories, workflows en processen.
2.  **Prevalentie**: Bij conflict tussen deze Constitutie en lagere documenten, geldt altijd de Constitutie.
3.  **Integriteit**: Automatisering mag deze Constitutie niet negeren, verzwakken of interpreteren op een manier die haar kracht vermindert.

---

## Wijzigingslog

| Datum      | Versie | Wijziging                                                           | Auteur            |
|------------|--------|---------------------------------------------------------------------|-------------------|
| 2026-01-08 | 1.1.0  | Eerste publieke versie                                               | Constitutioneel Auteur |
| 2026-01-16 | 1.2.0  | Artikel 2 ingekort tot verwijzing naar workspace-doctrine; Artikel 4 (Automatisering) verplaatst naar Artikel 2; artikelen hernummerd | Canon Curator |

---

## Gerelateerde Doctrines en Normatieve Artefacten

Deze Constitutie is de bindende grondslag voor het gehele normatieve stelsel. De volgende documenten in `grondslagen/globaal/` concretiseren en implementeren deze Constitutie:

### Workspace Governance

- **[workspace-doctrine.md](workspace-doctrine.md)**  
  Standaardisatie van mappenstructuur, naamgeving en organisatie voor alle workspaces. Implementeert Artikel 3 (Workspace Structuur). Verplicht voor alle document-repositories.

- **[agent-charter-normering.md](agent-charter-normering.md)**  
  Structuur en vereisten voor agent-charters. Waarborgt consistentie en kwaliteit van alle agent-definities conform Artikel 1 (Hiërarchie).

### Handoff & Uitvoering

- **[doctrine-handoff-creatie-en-overdrachtsdiscipline.md](doctrine-handoff-creatie-en-overdrachtsdiscipline.md)**  
  Regels voor handoff-creatie en handoff-validatie tussen agents. Implementeert Artikel 2 (Automatisering) en het principe van duidelijke afhankelijkheden.

- **[doctrine-runner-discipline-en-runner-kernel.md](doctrine-runner-discipline-en-runner-kernel.md)**  
  Gedragsregels voor agents en runners (orchestrators). Definieert hoe automatisering zich gedraagt conform Artikel 2 (Governance Lezen, Conflictmelding).

### Tijdstempel & Geldigheid

- **[doctrine-tijdreferentie-en-contextuele-geldigheid.md](doctrine-tijdreferentie-en-contextuele-geldigheid.md)**  
  Vastlegging van hoe tijdreferenties worden beheerd en hoe normatieve artefacten hun actualiteit behouden. Ondersteunt traceerbaarheid conform Artikel 1 (Doel).

### State & Audit

- **[doctrine-workspace-state-en-legitimiteit.md](doctrine-workspace-state-en-legitimiteit.md)**  
  State-logging en audit trail voor alle wijzigingen aan canonieke artefacten. Waarborgt integriteit conform Artikel 1 (Traceerbaarheid).
