## Doctrine — Handoff Creation en Overdrachtsdiscipline

### Status
- Type: Doctrine
- Geldigheid: Canoniek
- Scope: Alle agents, runners en workspaces
- Afgeleid van:
  - Doctrine — Workspace State & Legitimiteit
  - Doctrine — Tijdreferentie en Contextuele Geldigheid

---

### 1. Doel en functie van handoffs

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

### 7. Afhandeling en status

De handoff doorloopt expliciet de volgende statussen:

- `open` — aangemaakt door de runner
- `accepted` — gelezen en geaccepteerd door de ontvangende agent
- `completed` — uitvoering afgerond en output geleverd
- `cancelled` — handoff ingetrokken vóór uitvoering

Statusovergangen worden vastgelegd
en zijn navolgbaar.

---

### 8. Slotbepaling

Handoffs zijn geen administratief hulpmiddel,
maar een **legitimatiemechanisme**.

Zij maken overdracht expliciet,
context overdraagbaar
en verantwoordelijkheid toetsbaar.

Handelen zonder handoff
is handelen zonder legitimiteit.
