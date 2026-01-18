# Referentie: Agent-Soorten en Karakterisering

**Type**: Referentie-tabel voor agent-classificatie  
**Versie**: 1.0.0  
**Status**: Actief  
**Datum**: 2026-01-18  

---

## Herkomstverantwoording

Dit referentie-document is afgeleid op basis van de volgende geraadpleegde bronnen. De inhoud vormt de basis voor normatief kader in doctrine-agent-charter-normering.md (versie 1.2.2).

**Geraadpleegde bronnen**:
- Constitutie Mandarin (versie 1.2.1, gelezen op 2026-01-18, exacte tijd niet beschikbaar)
- doctrine-agent-charter-normering.md (versie 1.2.2, gelezen op 2026-01-18, exacte tijd niet beschikbaar)
- Axioma van gezag (verwijzing naar fundamenteel onderscheid tussen macht, inzicht en mandaat)

**Toelichting**:
Dit document bevat een classificatie van drie agent-soorten die binnen het Mandarin-ecosysteem bestaan. De tabel vormt een referentiepunt voor charter-writers en agents. Het onderscheid is gebaseerd op:
- Welke aspecten van de werkelijkheid een agent mag wijzigen
- De gezagsbron waarop de agent opereert
- Het risicoprofiel van de agent

---

## Tabel: Agent-Soorten

| Aspect            | Adviserend agent | Uitvoerend agent | Beheeragent  |
| ----------------- | ---------------- | ---------------- | ------------ |
| Rol               | Beschouwend      | Inhoudelijk      | Operationeel |
| Wijzigt inhoud    | Nee              | Ja               | Nee          |
| Wijzigt structuur | Nee              | Nee              | Ja           |
| Gezag             | Inzicht          | Mandaat          | Beheer       |
| Risico            | Laag             | Hoog             | Hoog         |

---

## Definities

### Adviserend Agent
- **Rol**: Beschouwend — analyseert en adviseert zonder directe wijziging
- **Wijzigt inhoud**: Nee — levert voorstel, niet wijziging
- **Wijzigt structuur**: Nee — raakt geen architectonische keuzes
- **Gezag**: Inzicht — autoriteit ontleend aan kwaliteit van analyse
- **Risico**: Laag — geen directe impact op gedeelde werkelijkheid

### Uitvoerend Agent
- **Rol**: Inhoudelijk — voert wijzigingen uit in documenten en artefacten
- **Wijzigt inhoud**: Ja — wijzigt tekst, data, inhoudelijke artefacten
- **Wijzigt structuur**: Nee — raakt niet de architectuur of governance-structuur
- **Gezag**: Mandaat — autoriteit ontleend aan expliciet charter en workspace-beleid
- **Risico**: Hoog — wijzigingen impact hebben op inhoud en gebruikers

### Beheeragent
- **Rol**: Operationeel — beheert technische en governance-structuur
- **Wijzigt inhoud**: Nee — raakt niet inhoudelijke artefacten direct
- **Wijzigt structuur**: Ja — wijzigt governance-regels, mappings, konfiguratie, state
- **Gezag**: Beheer — autoriteit ontleend aan beheer-mandaat en technisch gezag
- **Risico**: Hoog — structuurwijzigingen impact hebben op heel ecosysteem

---

## Terminologische Keuze: "Soort" vs. "Type"

### Waarom "Agent-Soort" en niet "Agent-Type"?

Deze keuze is bewust en normatief vastgesteld. Het onderscheid is fundamenteel:

**"Agent-Type"** suggereert:
- Technische of implementatie-categorisering (zoals in programmeren: `Type = Integer`, `Type = String`)
- Neutrale, syntactische classificatie
- Uitwisselbare implementatie-varianten
- Nadruk op **hoe** iets technisch is opgebouwd

**"Agent-Soort"** suggereert:
- Conceptuele of normatieve categorisering (naar aard, karakter, essence)
- Waarde-geladen onderscheid met betekenis
- Fundamentele verschillen in bevoegdheden en verantwoordelijkheden
- Nadruk op **wat** een agent mag doen en waarom

### Normatieve Grondslag

Conform Constitutie Artikel 7 (Taal en terminologie):
- Taalgebruik wordt behandeld als **architecturale keuze**, niet als puur stijlelement
- Het begrip "soort" is semantisch superieur in deze context omdat het:
  1. Precisie vergt (geen willekeurige types, maar betekenisvolle kategorieën)
  2. Gezag en verantwoordelijkheid expliciet maakt
  3. Het onderscheid tussen **macht**, **inzicht** en **mandaat** weerspiegelt

### De Drie Agent-Soorten Zijn Geen Interchangeable Types

Ze zijn fundamenteel verschillend:

| Aspekt | Type (technisch) | Soort (normatief) |
|--------|------------------|-------------------|
| **Uitwisselbaar** | Ja — je kunt het type veranderen | **Nee** — je kunt niet zomaar adviserend ↔ uitvoerend wisselen |
| **Gezag** | Geen gezag-implicatie | **Volle gezag-implicatie** — bepaalt mandaat en verantwoordelijkheid |
| **Wijziging van soort** | Simpele code-change | **Normatief proces** met herkomstverantwoording nodig |
| **Charter-gevolgen** | Implementatie-detail | **Structureel** — bepaalt gehele charter-opbouw |

### Herleidbaarheid tot Constitutie

De term "soort" weerspiegelt Constitutie-principes:
- **Artikel 1 "Werkingssfeer en hiërarchie"**: Soorten hebben verschillende gezags-hierachie
- **Artikel 2 "Automatisering en orkestratie"**: Soorten hebben verschillende governance-vereisten
- **Artikel 4 "Wijzigingsbeheer"**: Soorten hebben verschillende wijzigings-verantwoordelijkheid
- **Sectie "Waar Mandarin-agenten geen gezag hebben"**: Soort bepaalt wat gezag is en waar het ontbreekt

---

## Normatief Fundament

Deze classificatie is vastgesteld in **doctrine-agent-charter-normering.md** (versie 1.2.2, sectie 12.2).

Voor het volledige normatieve kader zie:
- → [doctrine-agent-charter-normering.md](../grondslagen/globaal/doctrine-agent-charter-normering.md#norm-agent-soorten-en-gezag-relatie-sectie-122)

Conform Constitutie:
- Artikel 2 (Automatisering en orkestratie) — duidelijke afhankelijkheden
- Artikel 4 (Wijzigingsbeheer) — alle wijzigingen kennen herkomstverantwoording
- "Waar Mandarin-agenten geen gezag hebben" — mandaat bepaalt autoriteit
