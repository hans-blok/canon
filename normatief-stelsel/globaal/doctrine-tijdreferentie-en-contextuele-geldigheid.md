# Doctrine — Tijdreferentie en Contextuele Geldigheid

**Type**: Normatieve Doctrine  
**Repository**: standards  
**Identifier**: standards.doctrine.tijdreferentie-en-contextuele-geldigheid  
**Versie**: 1.0.0  
**Status**: Actief  
**Datum**: 2026-01-14  
**Eigenaar**: Architecture & AI Enablement  
**Geldigheid**: Canoniek (alle agents en workspaces)

---

## Herkomstverantwoording

Dit normatief artefact is afgeleid op basis van de volgende bronnen:

**Geraadpleegde bronnen**:
- normatief-stelsel/globaal/constitutie.md (gelezen op 2026-01-14, exacte tijd niet beschikbaar)
- normatief-stelsel/globaal/doctrine-workspace-state-en-legitimiteit.md (gelezen op 2026-01-14, exacte tijd niet beschikbaar)
- temp/doctrine-tijdreferentie encontextuele geldigheid.md (concept-versie, gelezen op 2026-01-14, exacte tijd niet beschikbaar)
- Gebruikersinstructies voor doctrine-formalisering (ontvangen op 2026-01-14, exacte tijd niet beschikbaar)

**Toelichting tijdreferenties**: Conform deze doctrine worden geen tijdstippen ingevuld indien niet expliciet beschikbaar. Alleen de datum (2026-01-14) is bekend.

**Afleiding en structuur**:
Deze doctrine formaliseert het principe dat tijd een contextueel gegeven is en geen afleidbaar feit. De doctrine is afgeleid van de legitimiteitsvoorwaarden in de workspace state doctrine en concretiseert deze voor het specifieke domein van tijdsreferenties in agent-output.

---

## 1. Doel en Scope

### 1.1 Missie

Deze doctrine definieert **hoe agents omgaan met tijd en tijdreferenties**. Tijd is een cruciaal contextueel gegeven voor traceerbaarheid, legitimiteit en reproduceerbaarheid van agent-handelen. Deze doctrine waarborgt dat tijdreferenties altijd expliciet en herleidbaar zijn.

### 1.2 Scope

**Binnen scope (DOET WEL)**:
- Definiëren wat een geldige tijdreferentie is
- Vastleggen welke bronnen voor tijdreferenties zijn toegestaan
- Beschrijven hoe tijd gerelateerd is aan legitimiteit
- Specificeren hoe tijdreferenties in herkomstverantwoording worden opgenomen
- Verbieden van tijdsschatting, -afleiding of -benadering door agents

**Buiten scope (DOET NIET)**:
- Bepalen van tijdzones of formaten (dit is conventie-kwestie)
- Technische implementatie van tijdregistratie in runners
- Workspace-specifieke logging van tijd
- Domeinlogica over wanneer acties moeten gebeuren

---

## 2. Kernprincipe: Tijd als Context, Niet als Afleiding

**Principe**: Tijd is een **contextueel gegeven** en geen afleidbaar feit.

Agents beschikken niet over een intrinsiek besef van het huidige tijdstip en mogen tijd daarom **niet zelf bepalen, afleiden of benaderen**.

Elke tijdsaanduiding die door een agent wordt gebruikt, moet expliciet van buiten de agent zijn aangeleverd.

**Rationale**:
- Agents hebben geen betrouwbare kennis van actuele tijd
- Onjuiste tijdreferenties ondermijnen traceerbaarheid
- Tijd is bepalend voor legitimiteit van handelen
- Reproduceerbaarheid vereist expliciete tijdscontext

---

## 3. Verbod op Tijdsschatting

Het is agents expliciet **niet toegestaan** om:

- Een tijdstip te gokken of te raden
- Een tijdstip te benaderen of te schatten
- Een aannemelijk tijdstip in te vullen
- Impliciete aanduidingen zoals "nu", "vandaag" of "recent" te concretiseren zonder expliciete bron
- Tijdstippen af te leiden uit andere gegevens

**Consequentie**: Wanneer geen expliciete tijdreferentie beschikbaar is, moet de agent dit **expliciet vermelden**.

**Voorbeeld correcte melding**:
> "Tijdreferentie niet beschikbaar. Exacte tijd niet ingevuld."  
> "Alleen datum bekend: 2026-01-14 (exacte tijd niet beschikbaar)"

**Ongeldig**: Een ingevuld maar niet-aangeleverd tijdstip wordt beschouwd als **ongeldige output**.

---

## 4. Geldige Bronnen voor Tijdreferentie

Een agent mag uitsluitend een tijdreferentie gebruiken wanneer deze expliciet is aangeleverd via één van de volgende bronnen:

1. **Workspace state** (`state-<workspace>.md`) — gelogde wijzigingstijden
2. **Handoff-document** — expliciete timestamps in handoff
3. **Runner of workflow-context** — technische timestamp van uitvoering
4. **Gebruikersinstructie** — expliciete vermelding in opdracht
5. **Normatief artefact** — timestamp uit geraadpleegd document

**Verplichtingen**:
- De agent neemt de tijdreferentie **ongewijzigd over**
- Interpretatie, afronding of herformulering is niet toegestaan
- De bron moet expliciet worden vermeld in herkomstverantwoording

**Ongeldige bronnen**:
- "Huidige tijd" zonder technische timestamp
- "Geschatte tijd op basis van context"
- "Afgeleid uit bestandsdatum"

---

## 5. Tijd in Herkomstverantwoording

Wanneer een agent een tijdreferentie gebruikt, moet deze worden opgenomen in de herkomstverantwoording met expliciete vermelding van de bron.

### 5.1 Verplichte Elementen

Bij **elke tijdreferentie** in herkomstverantwoording:

1. **Bron**: Waar komt de tijdreferentie vandaan?
2. **Precisie**: Datum + tijd, of alleen datum?
3. **Timezone**: Indien tijd beschikbaar, met timezone (bijv. CET, UTC+1)

### 5.2 Voorbeelden

**Correcte voorbeelden**:
```markdown
- document.md (gelezen op 2026-01-14 15:30 CET)
  Bron: runner-context timestamp

- document.md (gelezen op 2026-01-14, exacte tijd niet beschikbaar)
  Bron: gebruikersinstructie (alleen datum)

**Toelichting tijdreferenties**: Timestamps overgenomen uit handoff-20260114-001
```

**Onjuiste voorbeelden** (niet toegestaan):
```markdown
- document.md (gelezen vandaag om ongeveer 15:00)
- document.md (recent geraadpleegd)
- document.md (gelezen op 2026-01-14 14:30) [zonder bronvermelding]
```

### 5.3 Ontbrekende Tijd

Indien **geen expliciete tijdreferentie** beschikbaar is:

```markdown
**Toelichting tijdreferenties**: Geen expliciete tijdreferentie aangeleverd. 
Alleen datum bekend: 2026-01-14 (exacte tijd niet beschikbaar).
```

Herkomstverantwoording zonder duidelijke status van de tijdreferentie is **ongeldig**.

---

## 6. Relatie tot Legitimiteit

Tijd is bepalend voor:

- **Geldigheid van normen**: Welke versie van een doctrine gold op het moment van handelen?
- **Interpretatie van wijzigingen**: Welke artefacten waren actueel?
- **Herleidbaarheid van besluiten**: Kunnen beslissingen worden gereconstrueerd?
- **Workspace state logging**: Wanneer vonden wijzigingen plaats?

### 6.1 Legitimiteitsvoorwaarde

> Output met een onjuiste of niet-herleidbare tijdreferentie  
> is **niet legitiem**, ongeacht de inhoudelijke kwaliteit.

**Consequenties**:
- Agent-output zonder geldige tijdreferentie is ongeldig
- Herkomstverantwoording zonder tijdsbronvermelding is ongeldig
- Geschatte of verzonnen tijden maken output illegitiem

### 6.2 Relatie tot Workspace State Doctrine

Deze doctrine concretiseert de legitimiteitsvoorwaarden uit de workspace state doctrine:

- Agents moeten workspace state lezen vóór handelen
- Workspace state bevat timestamps van wijzigingen
- Deze timestamps zijn **gezaghebbend** en mogen niet door agents worden aangepast
- Nieuwe wijzigingen moeten worden gelogd met **expliciete tijdreferentie** (uit runner of gebruiker)

---

## 7. Slotbepalingen

### 7.1 Kernboodschap

> Tijd behoort tot de expliciete context van handelen.

Agents die handelen zonder geldige tijdreferentie handelen buiten hun legitimiteit.

Agents die tijd invullen zonder bron handelen in strijd met het normatieve stelsel.

### 7.2 Verplichtingen voor Agents

Elke agent **moet**:
- Expliciete tijdreferenties overnemen uit geldige bronnen
- Tijdsbron vermelden in herkomstverantwoording
- Ontbrekende tijd expliciet melden (niet invullen)
- Timezone vermelden bij tijdsreferenties

Elke agent **mag niet**:
- Tijd raden, schatten of afleiden
- Tijdreferenties herformuleren zonder bronvermelding
- Output produceren met ongeldige tijdreferenties

### 7.3 Validatie

Agent-output is **ongeldig** wanneer:
- Tijdreferentie ontbreekt waar vereist (herkomstverantwoording)
- Tijdreferentie niet herleidbaar is tot geldige bron
- Tijdsbron niet is vermeld
- Tijd is geschat of afgeleid

---

## 8. Relatie met Andere Governance

Bij conflicten geldt de volgende rangorde:

1. Constitutie
2. Workspace State Doctrine
3. Deze Tijdreferentie Doctrine
4. Agent Charter Normering
5. Individuele agent-charters

Deze doctrine implementeert en concretiseert legitimiteitsvoorwaarden uit de constitutie en workspace state doctrine.

---

## 9. Wijzigingslog

| Datum      | Versie | Wijziging                                                             | Auteur                    |
|------------|--------|-----------------------------------------------------------------------|---------------------------|
| 2026-01-14 | 1.0.0  | Eerste versie, formaliseert principe "Tijd is Context" als canonieke doctrine | Constitutioneel Auteur |

---

## Slot

Tijd is context, geen afleiding.

Legitimiteit vereist herleidbaarheid.

Herleidbaarheid vereist expliciete tijdsreferenties.

> *Agents die tijd invullen zonder bron, handelen buiten het normatieve stelsel.*
