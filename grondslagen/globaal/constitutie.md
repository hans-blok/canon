# Constitutie van het Eco-systeem

**Versie**: 1.1.0
**Status**: Actief
**Datum**: 2026-01-08

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

## Artikel 2 — Workspace Structuur

1.  **Standaardisatie**: Elke workspace volgt een gestandaardiseerde mappenstructuur om voorspelbaarheid te garanderen. De `standards` repository dient als blauwdruk.
2.  **Artefacten**: Alle gegenereerde output (documenten, code, modellen) wordt opgeslagen in de `/artefacten/` map.
3.  **Governance**: Governance-documenten (zoals deze Constitutie en de Gedragscode) bevinden zich in de `/governance/` map.
4.  **Charters voor Geautomatiseerde Rollen**: Charters voor geautomatiseerde rollen bevinden zich in de `/charters.agents/` map.
5.  **Tijdelijke Bestanden**: Bestanden in een `temp` map zijn tijdelijk en niet duurzaam. Normatieve documenten (zoals constitutie, gedragscode, beleid, charters en doctrines) verwijzen nooit naar concrete bestanden in `temp`.
6.  **Activatie & Definitie van Geautomatiseerde Rollen**:
    *   Geautomatiseerde rollen worden in VS Code geactiveerd via het `/` commando (bijv. `/find`).
    *   De definitie van een geautomatiseerde rol (de prompt die het gedrag bepaalt) staat in `.github/agents/std.<fase>.<naam>.agent.md`.
    *   De koppeling voor activatie wordt gelegd in `.github/prompts/std.<fase>.<naam>.prompt.md`.

---

## Artikel 3 — Kwaliteit van Specificaties en Modellen

1.  **Ondubbelzinnig**: Specificaties moeten testbaar, volledig en consistent zijn.
2.  **Technologie-Agnostisch**: Requirements zijn technologie-agnostisch. Implementatiedetails horen niet in de specificatie.
3.  **Traceerbaarheid**: Werkstromen en tooling bewaken de traceerbaarheid tussen requirements, ontwerp en taken.
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

## Artikel 4 — Automatisering en Orkestratie

1.  **Governance Lezen**: Geautomatiseerde processen lezen bij aanroep altijd de relevante governance-bestanden (`constitutie.md`, `gedragscode.md`, `beleid.md`) om hun acties te kaderen.
2.  **Standards Repository Synchronisatie**: Wanneer de centrale standards repository (`https://github.com/hans-blok/standard.git`) wordt geraadpleegd, wordt altijd eerst een `git pull` uitgevoerd om te waarborgen dat de meest recente governance, charters en definities worden gebruikt.
3.  **Samenwerking**: Automatisering werkt samen met een duidelijke taakverdeling, minimale overlap en expliciete afhankelijkheden.
4.  **Conflictmelding**: Wanneer een geautomatiseerd proces conflicten vindt tussen documenten of regels, meldt het dit direct en expliciet.
5.  **Einddoel**: Het eco-systeem streeft naar een toekomst waarin een applicatie met slechts vijf regels input veilig en robuust kan worden gegenereerd.
6.  **Plannen Vastleggen**: Wanneer een geautomatiseerd proces wordt gevraagd om een plan (ontwerp, voorstel of werk-in-uitvoering), legt dat proces dit plan als Markdown-bestand vast in de `temp/` map van de betreffende workspace. Een mens beoordeelt het plan. Na beoordeling kan het plan uit `temp/` worden verwijderd. Inhoud die blijvend nodig is, wordt vastgelegd in duurzame documenten (bijvoorbeeld `README.md`), niet in `temp`.

---

## Artikel 5 — Wijzigingsbeheer

1.  **Menselijke Controle**: Inhoudelijke wijzigingen aan de Constitutie (nieuwe regels, gewijzigde principes) mogen **door een mens** en door **de agent constitutioneel-auteur** worden gedaan.
2.  **Redactionele Aanpassingen**: Alleen een daartoe geautoriseerde rol (de Moeder in de `standard` workspace) mag redactionele verbeteringen doen (layout, grammatica, spelling).
3.  **Verbod voor Automatisering**: Geautomatiseerde tooling of processen mogen de Constitutie op geen enkele wijze wijzigen.
4.  **Versiebeheer**: Versies worden beheerd via duidelijke versie-nummers en een wijzigingslog.

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
