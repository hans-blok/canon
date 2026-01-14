#!/usr/bin/env python3
"""Runner voor de constitutioneel-auteur agent.

Deze runner automatiseert herhaalbare, deterministische stappen zonder
AI-interactie. Hij helpt bij het starten van de Constitutioneel Auteur
voor het schrijven of bijwerken van normatieve artefacten op basis van
de constitutie.

Conform doctrine-handoff-creatie-en-overdrachtsdiscipline.md creëert deze
runner een handoff voorafgaand aan elke normatieve wijziging.

Usage:
    python scripts/constitutioneel-auteur.py --help

De runner zelf schrijft **geen** normatieve teksten, maar:
- creëert een handoff met unieke ID, tijdreferentie, en required reads;
- leest CLI-parameters (opdracht, doelpad);
- valideert paden tegen de workspace-structuur;
- geeft een samenvatting van de gevraagde taak weer;
- kan optioneel een leeg of bestaand `.md`-bestand als doel tonen.

De feitelijke inhoud wordt door de LLM-agent geleverd conform het
prompt-contract.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).parent.parent


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parseer CLI-argumenten voor de constitutioneel-auteur.

    Parameters
    ----------
    argv:
        Optionele lijst met argumenten; standaard wordt sys.argv[1:] gebruikt.
    """

    parser = argparse.ArgumentParser(
        prog="constitutioneel-auteur",
        description=(
            "Start de constitutioneel-auteur voor het schrijven of bijwerken "
            "van een normatief artefact op basis van de constitutie."
        ),
    )

    parser.add_argument(
        "opdracht",
        help=(
            "Korte beschrijving van het normatieve artefact dat moet worden "
            "geschreven of bijgewerkt (bijv. 'werk doctrine-it-development bij')."
        ),
    )
    parser.add_argument(
        "doelpad",
        help=(
            "Relatief pad naar het doelbestand (Markdown) binnen de workspace, "
            "bijv. 'artefacten/0-governance/doctrine-it-development.md'."
        ),
    )

    return parser.parse_args(argv)


def resolve_target(path_str: str) -> Path:
    """Vertaal een relatief pad naar een absoluut pad binnen de workspace.

    Het pad moet binnen WORKSPACE_ROOT liggen. De runner maakt geen
    directories aan en schrijft zelf geen inhoud; hij bewaakt alleen
    dat het doel binnen de workspace valt en verwijst ernaar.
    """

    target = (WORKSPACE_ROOT / path_str).resolve()
    try:
        target.relative_to(WORKSPACE_ROOT)
    except ValueError as exc:  # path buiten workspace
        raise ValueError("doelpad ligt buiten de workspace") from exc
    return target


def generate_handoff_id(opdracht: str) -> str:
    """Genereer unieke handoff-id conform doctrine.
    
    Format: handoff-{bron}-{doel}-{datum}-{volgnummer}
    """
    now = datetime.now()
    date_str = now.strftime("%Y%m%d")
    # Simplified: gebruik timestamp als volgnummer
    seq = now.strftime("%H%M")
    return f"handoff-runner-constitutioneel-auteur-{date_str}-{seq}"


def create_handoff(opdracht: str, doelpad: str, target_path: Path) -> Path:
    """Creëer handoff voor normatieve wijziging.
    
    Conform doctrine-handoff-creatie-en-overdrachtsdiscipline.md:
    - Unieke handoff-id
    - Tijdreferentie met timezone (CET)
    - Workspace-identiteit
    - Routing (From/To/Type)
    - Required reads
    - Status: open
    """
    handoff_id = generate_handoff_id(opdracht)
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M CET")
    
    # Bepaal workspace naam
    workspace_name = "standard"  # Placeholder - zou uit state gelezen moeten worden
    
    handoff_content = f"""# Handoff — Constitutioneel Auteur

## Handoff ID

{handoff_id}

## Timestamp + Status

- **Created**: {timestamp}
- **Status**: open

## Routing

- **From**: Runner (constitutioneel-auteur.py)
- **To**: Agent (constitutioneel-auteur, via LLM prompt)
- **Type**: Normatieve wijziging

## Context

**Opdracht**: {opdracht}

**Doelpad**: {doelpad}

**Workspace**: {workspace_name}

## Payload

### Normatief artefact

**Doelbestand**: {target_path.relative_to(WORKSPACE_ROOT).as_posix()}

**Status**: {'Bestaand bestand (bijwerken)' if target_path.exists() else 'Nieuw bestand (aanmaken)'}

## Required Reads

De agent moet voorafgaand lezen:

1. **Workspace state**: state-{workspace_name}.md (inclusief normatief-stelsel-ping)
2. **Constitutie**: normatief-stelsel/globaal/constitutie.md (of huidige versie)
3. **Doctrine tijdreferentie**: normatief-stelsel/globaal/doctrine-tijdreferentie-en-contextuele-geldigheid.md
4. **Handoff doctrine**: normatief-stelsel/globaal/doctrine-handoff-creatie-en-overdrachtsdiscipline.md
5. **Target artefact** (indien bestaand): {target_path.relative_to(WORKSPACE_ROOT).as_posix()}

## Acceptance Criteria

De agent levert:

1. Bijgewerkt of nieuw normatief artefact op doelpad
2. Herkomstverantwoording in artefact met verwijzing naar handoff-id: {handoff_id}
3. Correcte tijdreferentie (uit deze handoff: {timestamp})
4. Voldoet aan agent-charter-normering (indien van toepassing)

## Constraints

- Tijdreferentie: gebruik {timestamp} (niet afleiden)
- Workspace: {workspace_name}
- Handoff status wordt door agent bijgewerkt naar 'accepted' bij start, 'completed' bij afronding

---

**Let op**: Deze handoff is aangemaakt door de runner conform doctrine-handoff-creatie-en-overdrachtsdiscipline.md.
De agent is verplicht deze handoff volledig te lezen en alle Required Reads te raadplegen.
"""
    
    handoff_path = WORKSPACE_ROOT / "handoff.md"
    handoff_path.write_text(handoff_content, encoding="utf-8")
    return handoff_path


def main(argv: list[str] | None = None) -> int:
    """Entrypoint voor de constitutioneel-auteur runner.

    Deze functie:
    - leest opdracht + doelpad;
    - valideert dat het doelpad binnen de workspace ligt;
    - rapporteert de taak en het doelbestand in Markdown;
    - schrijft zelf geen inhoud en voert geen AI-calls uit.
    """

    try:
        args = parse_args(argv)
        target_path = resolve_target(args.doelpad)
    except Exception as exc:  # pragma: no cover - eenvoudige CLI-foutmelding
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    rel = target_path.relative_to(WORKSPACE_ROOT).as_posix()
    
    # Stap 1: Creëer handoff (conform doctrine)
    try:
        handoff_path = create_handoff(args.opdracht, args.doelpad, target_path)
        handoff_rel = handoff_path.relative_to(WORKSPACE_ROOT).as_posix()
    except Exception as exc:
        print(f"ERROR: Handoff creatie gefaald: {exc}", file=sys.stderr)
        return 1

    print("Constitutioneel Auteur — runner")
    print("--------------------------------")
    print(f"Opdracht : {args.opdracht}")
    print(f"Doelpad  : {rel}")
    print(f"Handoff  : {handoff_rel}")
    if target_path.exists():
        print("Status   : bestaand Markdown-bestand; gereed voor bijwerken door de LLM-agent.")
    else:
        print("Status   : bestand bestaat nog niet; gereed om nieuw normatief artefact te schrijven.")

    print()
    print(
        "BELANGRIJK: Handoff aangemaakt conform doctrine-handoff-creatie-en-overdrachtsdiscipline.md."
    )
    print(
        "De LLM-agent MOET deze handoff lezen en alle Required Reads raadplegen voordat wijzigingen worden doorgevoerd."
    )
    print()
    print(
        "Let op: deze runner schrijft zelf geen inhoud en voert geen AI-interactie uit. "
        "Gebruik de LLM-agent met het prompt-contract om het normatieve artefact te genereren of bij te werken."
    )

    return 0


if __name__ == "__main__":  # pragma: no cover - direct CLI gebruik
    raise SystemExit(main())
