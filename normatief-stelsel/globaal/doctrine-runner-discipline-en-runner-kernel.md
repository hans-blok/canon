## Doctrine — Runner Discipline & Runner Kernel

### Status
- Type: Doctrine
- Geldigheid: Canoniek
- Scope: Alle runners, agents en workspaces
- Afgeleid van:
  - Doctrine — Workspace State & Legitimiteit
  - Doctrine — Handoff Creation en Overdrachtsdiscipline
  - Doctrine — Tijdreferentie en Contextuele Geldigheid

---

### 1. Doel en positie van de runner

Een **runner** is het uitvoeringsmechanisme waarmee een agent
binnen een workspace tot actie komt.

De runner is verantwoordelijk voor:
- het voorbereiden van geldige context
- het afdwingen van lees- en overdrachtsdiscipline
- het uitvoeren van een agent binnen expliciete grenzen

De runner bevat **geen betekenis**, **geen interpretatie**
en **geen normatieve besluitvorming**.

---

### 2. Verplichte runner-discipline

Elke runner **moet** vóór uitvoering van een agent
een vaste **preflight** uitvoeren.

Deze preflight omvat minimaal:

1. het aanmaken of ontvangen van een geldige handoff;
2. het vaststellen en injecteren van een expliciete tijdreferentie;
3. het beschikbaar stellen van de geldende workspace state;
4. het afdwingen dat state en handoff worden gelezen vóór handelen.

Een runner die deze preflight niet uitvoert,
mag geen agent-acties starten.

---

### 3. Runner Kernel als canoniek uitvoeringsmechanisme

Alle runners maken gebruik van één **canonieke Runner Kernel**.

De Runner Kernel is een gedeelde uitvoeringscomponent die:

- handoff-creatie en -injectie verzorgt;
- tijdreferentie vastlegt en overdraagt;
- verplichte leesbronnen beschikbaar stelt;
- uniforme preflight- en postflight-stappen afdwingt.

Specifieke runners **componeren** de Runner Kernel
en voegen uitsluitend taak-specifieke uitvoering toe.

Afwijking van de Runner Kernel is niet toegestaan,
tenzij expliciet geautoriseerd via het normatieve stelsel.

---

### 4. Scheiding tussen agent en runner

De scheiding tussen agent en runner is principieel:

- **De agent**:
  - definieert betekenis en verantwoordelijkheid;
  - handelt binnen aangeleverde context;
  - levert output met herkomstverantwoording.

- **De runner**:
  - creëert en beheert context;
  - dwingt overdrachts- en leesregels af;
  - verzorgt uitvoering en omgevingsinteractie.

Agents leiden geen context af.
Runners interpreteren geen betekenis.

---

### 5. Relatie tot handoffs

Handoffs worden **altijd** aangemaakt of geïnjecteerd door de runner.

De runner:
- genereert een unieke handoff-id;
- legt routing en payload vast;
- levert de handoff als contractueel input-artefact.

Agents:
- creëren geen handoffs;
- handelen uitsluitend op basis van een bestaande handoff;
- verwijzen naar de handoff-id in hun herkomstverantwoording.

---

### 6. Relatie tot tijdreferentie

De runner is de enige bron van tijdreferentie tijdens uitvoering.

Elke runner:
- levert exact één expliciete tijdreferentie;
- draagt deze ongewijzigd over aan de agent;
- voorkomt dat agents tijd afleiden of invullen.

Uitvoering zonder expliciete tijdreferentie
is canoniek ongeldig.

---

### 7. Validiteit en afdwinging

Een agent-output is ongeldig indien:

- geen handoff aanwezig is;
- de workspace state niet is gelezen;
- geen geldige tijdreferentie is gebruikt;
- de runner niet conformeert aan deze doctrine.

Runners die niet voldoen aan deze discipline
mogen niet worden ingezet binnen het ecosysteem.

---

### 8. Slotbepaling

Runner discipline is geen implementatiedetail,
maar een **legitimatiemechanisme**.

De Runner Kernel borgt dat:
- context expliciet is;
- overdracht navolgbaar is;
- uitvoering reproduceerbaar blijft.

Zonder runner discipline
is geen sprake van legitieme agent-actie.
