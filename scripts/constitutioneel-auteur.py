#!/usr/bin/env python3
"""Runner voor de constitutioneel-auteur agent.

Deze runner automatiseert herhaalbare, deterministische stappen zonder
AI-interactie. Hij helpt bij het starten van de Constitutioneel Auteur
voor het schrijven of bijwerken van normatieve artefacten op basis van
de constitutie.

Usage:
    python scripts/constitutioneel-auteur.py --help

De runner zelf schrijft **geen** normatieve teksten, maar:
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

    print("Constitutioneel Auteur — runner")
    print("--------------------------------")
    print(f"Opdracht : {args.opdracht}")
    print(f"Doelpad : {rel}")
    if target_path.exists():
        print("Status  : bestaand Markdown-bestand; gereed voor bijwerken door de LLM-agent.")
    else:
        print("Status  : bestand bestaat nog niet; gereed om nieuw normatief artefact te schrijven.")

    print()
    print(
        "Let op: deze runner schrijft zelf geen inhoud en voert geen AI-interactie uit. "
        "Gebruik de LLM-agent met het prompt-contract om het normatieve artefact te genereren of bij te werken."
    )

    return 0


if __name__ == "__main__":  # pragma: no cover - direct CLI gebruik
    raise SystemExit(main())
