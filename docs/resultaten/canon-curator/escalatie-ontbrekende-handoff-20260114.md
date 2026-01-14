# Escalatie — Ontbrekende Handoff voor Normatieve Wijziging

**Type**: Handoff-schending  
**Timestamp**: 2026-01-14 (exacte tijd niet beschikbaar)  
**Betreft**: doctrine-runner-discipline-en-runner-kernel.md

---

## Situatie

Canon-curator heeft opdracht ontvangen om normatieve wijziging te publiceren:
- **Doctrine**: normatief-stelsel/globaal/doctrine-runner-discipline-en-runner-kernel.md
- **Actie**: "bump de wijziging" en "wijzig state"

## Handoff-schending

Conform charter.canon-curator.md v1.2, Clausule Handoff-validatie punt 1:

> "De Canon Curator accepteert uitsluitend wijzigingen aan het normatieve stelsel die zijn aangeleverd via een geldige handoff. Wijzigingen zonder voorafgaande handoff worden niet gepubliceerd en worden geacht niet te hebben plaatsgevonden."

**Bevinding**: Geen handoff aanwezig in workspace root (handoff.md bevat template).

## Doctrine-context

Conform doctrine-handoff-creatie-en-overdrachtsdiscipline.md sectie 2:

> "Voor elke agent-run waarbij normatieve inhoud wordt gewijzigd moet voorafgaand een handoff worden aangemaakt."

## Analyse

Deze situatie is waarschijnlijk ontstaan omdat:
1. De doctrine-runner-discipline-en-runner-kernel.md werd aangemaakt vóór implementatie van handoff-mechanisme
2. De doctrine beschrijft zelf het handoff-mechanisme (bootstrapping probleem)
3. Er is geen runner-flow gevolgd die een handoff zou aanmaken

## Aanbeveling

**Optie A - Retroactieve handoff**:
Creëer alsnog een handoff voor deze doctrine met:
- Handoff-id: handoff-constitutioneel-auteur-canon-curator-20260114-retro
- Tijdreferentie: expliciet aanleveren (niet afleiden)
- Required reads: constitutie, handoff-doctrine, workspace state
- Status: direct naar 'accepted' (retroactief)

**Optie B - Bootstrap-uitzondering**:
Registreer deze doctrine als bootstrap-uitzondering in state-standard.md:
- Markeer als "initiële doctrine zonder handoff (bootstrap)"
- Documenteer waarom handoff ontbreekt
- Alle toekomstige wijzigingen vereisen wel handoff

**Optie C - Niet publiceren**:
Conform governance niet publiceren totdat geldige handoff is aangeleverd door constitutioneel-auteur runner.

## Besluit

Canon-curator escaleert dit naar governance/mens voor besluit.

Publicatie wordt **opgeschort** tot:
- Geldige handoff is aangeleverd, OF
- Expliciete instructie voor bootstrap-uitzondering is gegeven

---

**Clausule 6 (Escalatie)**: "Structureel ontbreken of onjuist gebruik van handoffs wordt door de Canon Curator geëscaleerd als schending van het normatieve stelsel."
