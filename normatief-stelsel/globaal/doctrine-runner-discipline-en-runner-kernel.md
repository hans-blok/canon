## Herkomstverantwoording

Dit normatief artefact is vastgelegd door de Constitutioneel Auteur op basis van directe input van Hans Blok en de bestaande doctrine-inhoud.

**Geraadpleegde bronnen**:
- Constitutie van het Eco-systeem (versie 1.1.0, datum 2026-01-08), gelezen op 2026-01-15 09:30
- Doctrine — Workspace State & Legitimiteit, gelezen op 2026-01-15 09:30
- Doctrine — Handoff Creation en Overdrachtsdiscipline, gelezen op 2026-01-15 09:30
- Doctrine — Tijdreferentie en Contextuele Geldigheid, gelezen op 2026-01-15 09:30
- temp/handoff-loggin-contract.yaml (handoff logging schema specificatie), gelezen op 2026-01-15 (exacte tijd niet beschikbaar)
- Input Hans Blok, ontvangen op 2026-01-15 09:30

**Toelichting wijzigingen**:
- Initiële Herkomstverantwoording toegevoegd conform prompt contract (2026-01-15 09:30)
- Sectie 9 "Handoff Logging Contract" toegevoegd op basis van temp/handoff-loggin-contract.yaml (2026-01-15)
- Deze toevoeging specificeert het normatieve logging-contract voor handoffs conform de Runner Kernel discipline

---

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
---

### 9. Handoff Logging Contract

De Runner Kernel legt handoffs vast als **uitvoeringsspoor** (observability).

**Belangrijk**: Logs zijn **niet-normatief**. 
Ze mogen niet dienen als bron van waarheid, 
maar uitsluitend als trace voor debugging en audit.

#### 9.1. Storage

Handoff logs worden opgeslagen als:
- **Formaat**: YAML
- **Locatie**: `.kernel/runs/`
- **Mode**: run_log (alle events van één run in één bestand)

#### 9.2. Retentie

Logs worden behouden volgens:
- Bewaar maximaal **20 runs**, of
- Bewaar maximaal **7 dagen**, of
- Bij failure: bewaar maximaal **30 dagen**

Oudere logs mogen worden verwijderd conform retentie-beleid.

#### 9.3. Redactie-beleid

Logs bevatten **alleen pointers**, geen inhoud:

**Verboden** in logs:
- volledige prompts
- volledige policy-teksten
- secrets of credentials
- file content dumps

**Toegestaan** in logs:
- bestandspaden
- commit hashes
- timestamps
- status indicatoren
- korte berichten (max 500 karakters)

#### 9.4. Verplichte velden

Elke run log **moet** bevatten:
- `schema`: identificatie van contract versie
- `run_id`: unieke run identifier
- `created_at_utc`: UTC timestamp van aanmaak
- `recorded_by`: component identificatie (`{component, name, version}`)
- `workspace`: workspace metadata (`{name, root, active_branch, base_commit}`)
- `state_ref`: referentie naar state (`{path, hash}`)
- `events`: lijst van events (minimaal één handoff)
- `result`: eindresultaat (`{status, message}`)

#### 9.5. Handoff event structuur

Elk handoff event **moet** bevatten:
- `type`: "handoff"
- `id`: unieke event identifier
- `at_utc`: UTC timestamp van handoff
- `from_agent`: agent/runner die overdraagt
- `to_agent`: agent/runner die ontvangt
- `intent`: korte beschrijving van doel
- `trigger`: gestructureerd (`{reason, summary}`)
- `result`: event resultaat (`{status, message}`)

**Optioneel**:
- `pointers`: referenties naar specs/governance (geen inhoud)
- `effects`: gewijzigde bestanden (`{files_changed, state_updates}`)

#### 9.6. Trigger classificatie

De `trigger.reason` moet één van deze waarden hebben:
- `normative_change`: wijziging aan normatief stelsel
- `policy_gate`: policy validatie vereist actie
- `user_request`: handmatige gebruikersopdracht
- `recovery`: herstelactie na failure
- `other`: overige redenen (met toelichting)

#### 9.7. Event regels

De volgende regels zijn **verplicht**:
1. Elke daadwerkelijke overgang van agent A naar agent B **moet** een handoff-event produceren
2. Een handoff-event **moet** een `state_ref` bevatten (direct of via envelope)
3. `effects` **moet** paden loggen voor wijzigingen, maar **mag niet** inhoud loggen
4. Bij failure **moet** een korte message aanwezig zijn (≤ 500 karakters)

#### 9.8. Schema versie

Het logging contract is geversioneerd.
Huidige versie: `runner_handoff_logging_contract/v1`

Runners **moeten** de schema-versie vermelden in elk log-bestand
voor toekomstige compatibiliteit en validatie.