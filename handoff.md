# Handoff — Constitutioneel Auteur

## Handoff ID

handoff-runner-constitutioneel-auteur-20260115-0936

## Timestamp + Status

- **Created**: 2026-01-15 09:36 CET
- **Status**: open

## Routing

- **From**: Runner (constitutioneel-auteur.py)
- **To**: Agent (constitutioneel-auteur, via LLM prompt)
- **Type**: Normatieve wijziging

## Context

**Opdracht**: leg herkomstverantwoording vast

**Doelpad**: normatief-stelsel/globaal/doctrine-runner-discipline-en-runner-kernel.md

**Workspace**: standard

## Payload

### Normatief artefact

**Doelbestand**: normatief-stelsel/globaal/doctrine-runner-discipline-en-runner-kernel.md

**Status**: Bestaand bestand (bijwerken)

## Required Reads

De agent moet voorafgaand lezen:

1. **Workspace state**: state-standard.md (inclusief normatief-stelsel-ping)
2. **Constitutie**: normatief-stelsel/globaal/constitutie.md (of huidige versie)
3. **Doctrine tijdreferentie**: normatief-stelsel/globaal/doctrine-tijdreferentie-en-contextuele-geldigheid.md
4. **Handoff doctrine**: normatief-stelsel/globaal/doctrine-handoff-creatie-en-overdrachtsdiscipline.md
5. **Target artefact** (indien bestaand): normatief-stelsel/globaal/doctrine-runner-discipline-en-runner-kernel.md

## Acceptance Criteria

De agent levert:

1. Bijgewerkt of nieuw normatief artefact op doelpad
2. Herkomstverantwoording in artefact met verwijzing naar handoff-id: handoff-runner-constitutioneel-auteur-20260115-0936
3. Correcte tijdreferentie (uit deze handoff: 2026-01-15 09:36 CET)
4. Voldoet aan agent-charter-normering (indien van toepassing)

## Constraints

- Tijdreferentie: gebruik 2026-01-15 09:36 CET (niet afleiden)
- Workspace: standard
- Handoff status wordt door agent bijgewerkt naar 'accepted' bij start, 'completed' bij afronding

---

**Let op**: Deze handoff is aangemaakt door de runner conform doctrine-handoff-creatie-en-overdrachtsdiscipline.md.
De agent is verplicht deze handoff volledig te lezen en alle Required Reads te raadplegen.
