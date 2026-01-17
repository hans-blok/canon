## Doctrine — Handoff Creation en Overdrachtsdiscipline

**Versie**: 1.1.0  
**Status**: Actief  
**Datum**: 2026-01-16  
**Eigenaar**: Architecture & AI Enablement  
**Type**: Normerend Doctrine-document

---

## Herkomstverantwoording

Dit normatief artefact is afgeleid op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- Doctrine — Workspace State & Legitimiteit (gelezen op 2026-01-16)
- Doctrine — Tijdreferentie en Contextuele Geldigheid (gelezen op 2026-01-16)
- Eerdere versie doctrine-handoff-creatie-en-overdrachtsdiscipline.md (versie 1.0.0, gelezen op 2026-01-16)
- Vereisten voor artefact-herkomst structuur (ontvangen op 2026-01-16)

**Wijzigingen in versie 1.1.0**:
- Metagegevens header toegevoegd (Versie, Status, Datum, Eigenaar, Type)
- Herkomstverantwoording sectie toegevoegd conform agent-charter-normering.md
- Nieuwe sectie 7 toegevoegd: Herkomst-structuur voor afgeleide artefacten (Status, Input-tracking, Menselijke validatie)
- Originele secties hernummerd (7 → 8, 8 → 9)

---

Een **handoff** is een formeel overdrachtsmechanisme
tussen rollen of agents binnen het ecosysteem.

Een handoff maakt expliciet:
- intentie van overdracht
- geldige context
- verplichte leesbronnen
- tijdreferentie
- verantwoordelijkheden vóór en na uitvoering

Zonder handoff is overdracht **impliciet**
en daarmee **niet legitiem**.

---

### 2. Verplichting tot handoff-creatie

Voor elke agent-run waarbij:

- normatieve inhoud wordt gewijzigd
- een afgeleid artefact wordt geproduceerd
- een andere agent of rol wordt geactiveerd
- expliciete input wordt aangeleverd (mens of systeem)

**moet voorafgaand een handoff worden aangemaakt.**

Handelen zonder voorafgaande handoff
is niet toegestaan binnen het normatieve stelsel.

---

### 3. Verantwoordelijkheid voor handoff-creatie

De **runner** is verantwoordelijk voor het aanmaken van de handoff.

Dit omvat minimaal:
- genereren van een unieke handoff-id
- vastleggen van tijdreferentie (met timezone)
- vastleggen van workspace-identiteit
- vastleggen van routing (From / To / Type)
- vastleggen van aangeleverde input (payload references)
- vastleggen van verplichte leesbronnen

Agents creëren **geen** handoffs.

Agents handelen uitsluitend **op basis van bestaande handoffs**.

---

### 4. Handoff als contractueel input-artefact

De handoff fungeert als een **contractueel input-artefact**.

De ontvangende agent is verplicht om:
- de handoff volledig te lezen
- de vermelde workspace state te lezen
- alle verplichte leesbronnen te raadplegen
- uitsluitend te handelen binnen de grenzen van de handoff

Niet-naleving maakt de output ongeldig.

---

### 5. Relatie tot tijdreferentie

Elke handoff bevat exact één geldige tijdreferentie.

Deze tijdreferentie:
- wordt aangeleverd door de runner
- is leidend voor alle afleidingen
- wordt ongewijzigd overgenomen door agents

Agents mogen **geen eigen tijd afleiden**
en geen tijdstip aanvullen dat niet expliciet is aangeleverd.

---

### 6. Relatie tot herkomstverantwoording

Elke output die voortkomt uit een handoff
moet een herkomstverantwoording bevatten
die expliciet verwijst naar:

- de handoff-id
- de gelezen workspace state (inclusief ping)
- alle geraadpleegde payload references
- de gebruikte tijdreferentie

Herkomstverantwoording zonder handoff-verwijzing
is nu nog geldig. Maar dit is tijdelijk.

---

### 7. Herkomst-structuur voor afgeleide artefacten

Elk artefact dat wordt gegenereerd of geproduceerd door een agent
**moet** een gestructureerde **Herkomst**-sectie bevatten.

Deze sectie vastlegt de volledige provenance en status van het artefact:

```
## Herkomst

- Gegenereerd door: <agent-id of rol>
- Agent charter: <verwijzing naar agent charter>
- Fase: <SAFe fase, bijv. Design, Implementation>
- Input-artefacten:
  - <Naam en verwijzing van input-artefact A>
  - <Naam en verwijzing van input-artefact B>
  - (voeg toe als van toepassing)
- Datum: <YYYY-MM-DD>
- Handoff-referentie: <handoff-id indien van toepassing>
- Status:
  - ☐ Advies (aanbeveling, niet bindend)
  - ☐ Concept (werk in uitvoering, onder review)
  - ☐ Vastgesteld (definitief goedgekeurd)
- Menselijke validatie:
  - ☐ Nog niet gevalideerd
  - ☐ Gevalideerd door <naam/rol en datum>
```

**Toelichting**:
- **Gegenereerd door**: Identificeert de bron (agent, rol of systeem)
- **Agent charter**: Verwijzing naar het charter dat de agent definieert
- **Fase**: Situeert het artefact in de SAFe lifecycle
- **Input-artefacten**: Maakt de afhankelijkheden expliciet (traceerbaarheid)
- **Datum**: Creatie- of publicatiedatum (conform doctrine-tijdreferentie)
- **Handoff-referentie**: Linkt het artefact aan de legitimatiebron (handoff)
- **Status**: Markeert het rijpniveau van het artefact
- **Menselijke validatie**: Vastlegging van goedkeuring door verantwoordelijke persoon

Deze structuur waarborgt dat elk artefact volledig traceerbaar is
naar zijn bron, input, fase en goedkeuringsstatus.

---

### 8. Afhandeling en status

De handoff doorloopt expliciet de volgende statussen:

- `open` — aangemaakt door de runner
- `accepted` — gelezen en geaccepteerd door de ontvangende agent
- `completed` — uitvoering afgerond en output geleverd
- `cancelled` — handoff ingetrokken vóór uitvoering

Statusovergangen worden vastgelegd
en zijn navolgbaar.

---

### 9. Slotbepaling

Handoffs zijn geen administratief hulpmiddel,
maar een **legitimatiemechanisme**.

Zij maken overdracht expliciet,
context overdraagbaar
en verantwoordelijkheid toetsbaar.

Handelen zonder handoff
is handelen zonder legitimiteit.

---

## Wijzigingslog

| Datum      | Versie | Wijziging                                                           | Auteur            |
|------------|--------|---------------------------------------------------------------------|-------------------|
| 2026-01-14 | 1.0.0  | Eerste versie: handoff-discipline en overdrachtsvereisten          | Constitutioneel Auteur |
| 2026-01-16 | 1.1.0  | Herkomst-structuur voor artefacten toegevoegd (sectie 7); metadata header en herkomstverantwoording toegevoegd; secties hernummerd | Canon Curator |
