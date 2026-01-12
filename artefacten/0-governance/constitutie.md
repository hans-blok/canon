# Constitutie van het Agent Eco-systeem

**Versie**: 1.1.0
**Status**: Actief
**Datum**: 2026-01-08

---

## Inleiding

Waar de **Gedragscode** zich richt op gedrag, principes en professionele normen, beschrijft de **Constitutie** de onveranderlijke, harde afspraken die de structuur en werking van het gehele agent eco-systeem vastleggen. Deze regels zijn bindend en staan boven alle andere beleidsdocumenten, charters of specificaties.

---

## Artikel 1 — Werkingssfeer en Hiërarchie

1.  **Bindend**: Deze constitutie geldt voor alle repositories, agents, workflows en artefacten binnen het eco-systeem.
2.  **Hiërarchie**: Bij conflict prevaleert de Constitutie altijd boven de Gedragscode, beleidsdocumenten, charters of andere specificaties. Lagere documenten mogen de Constitutie niet tegenspreken, verzwakken of negeren.
3.  **Doel**: De Constitutie waarborgt voorspelbaarheid, kwaliteit, veiligheid en traceerbaarheid.

---

## Artikel 2 — Workspace Structuur

1.  **Standaardisatie**: Elke workspace volgt een gestandaardiseerde mappenstructuur om voorspelbaarheid te garanderen. De `standards` repository dient als blauwdruk.
2.  **Artefacten**: Alle door agents gegenereerde output (documenten, code, modellen) wordt opgeslagen in de `/artefacten/` map.
3.  **Governance**: Governance-documenten (zoals deze Constitutie en de Gedragscode) bevinden zich in de `/governance/` map.
4.  **Agent Charters**: Agent-specifieke charters bevinden zich in de `/charters.agents/` map.
5.  **Agent Activatie & Definitie**:
    *   Agents worden in VS Code geactiveerd via het `/` commando (bijv. `/find`).
    *   De definitie van een agent (de prompt die zijn gedrag bepaalt) staat in `.github/agents/std.<fase>.<naam>.agent.md`.
    *   De koppeling voor activatie wordt gelegd in `.github/prompts/std.<fase>.<naam>.prompt.md`.

---

## Artikel 3 — Kwaliteit van Specificaties en Modellen

1.  **Ondubbelzinnig**: Specificaties moeten testbaar, volledig en consistent zijn.
2.  **Technologie-Agnostisch**: Requirements zijn technologie-agnostisch. Implementatiedetails horen niet in de specificatie.
3.  **Traceerbaarheid**: Agents bewaken de traceerbaarheid tussen requirements, ontwerp en taken.
4.  **Aannames**: Onzekerheden worden altijd expliciet gemarkeerd. Een agent mag maximaal drie aannames tegelijk hanteren voordat escalatie naar een mens verplicht is.

---

## Artikel 4 — AI-Agents en Orkestratie

1.  **Governance Lezen**: Agents lezen bij aanroep altijd de relevante governance-bestanden (`constitutie.md`, `gedragscode.md`, `beleid.md`) om hun acties te kaderen.
2.  **Standards Repository Synchronisatie**: Wanneer de centrale standards repository (`https://github.com/hans-blok/standard.git`) wordt geraadpleegd, wordt altijd eerst een `git pull` uitgevoerd om te waarborgen dat de meest recente governance, charters en agent-definities worden gebruikt.
3.  **Samenwerking**: Agents werken samen met een duidelijke taakverdeling, minimale overlap en expliciete afhankelijkheden.
4.  **Conflictmelding**: Wanneer een agent conflicten vindt tussen documenten of regels, meldt het dit direct en expliciet.
5.  **Einddoel**: Agents streven naar een toekomst waarin een applicatie met slechts vijf regels input veilig en robuust kan worden gegenereerd.
6.  **Plannen Vastleggen**: Wanneer een agent wordt gevraagd om een plan (ontwerp, voorstel of werk-in-uitvoering), legt de agent dit plan altijd vast als Markdown-bestand in de `temp/` map van de betreffende workspace.

---

## Artikel 5 — Wijzigingsbeheer

1.  **Menselijke Controle**: Inhoudelijke wijzigingen aan de Constitutie (nieuwe regels, gewijzigde principes) mogen **alleen door een mens** worden gedaan.
2.  **Redactionele Aanpassingen**: Alleen een daartoe geautoriseerde agent (zoals `Logos`) mag redactionele verbeteringen doen (layout, grammatica, spelling).
3.  **Verbod voor Andere Agents**: Alle andere agents mogen de Constitutie op geen enkele wijze wijzigen.
4.  **Versiebeheer**: Versies worden beheerd via duidelijke versie-nummers en een wijzigingslog.

---

## Artikel 6 — Slotbepaling

1.  **Onmiddellijke Werking**: Deze Constitutie geldt onmiddellijk voor alle bestaande en toekomstige repositories, agents en workflows.
2.  **Prevalentie**: Bij conflict tussen deze Constitutie en lagere documenten, geldt altijd de Constitutie.
3.  **Integriteit**: Agents mogen deze Constitutie niet negeren, verzwakken of interpreteren op een manier die haar kracht vermindert.
