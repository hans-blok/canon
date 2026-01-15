#!/usr/bin/env python3
"""Kernel Operator Runner

Runner voor kernel-operator agent. Beheert kernelrunner-uitvoering met
human-in-the-loop gatekeeping en observability.

Usage:
    python scripts/kernel-operator.py --help

Operaties:
    start-run    - Start een kernel-run met preflight en gebruikersbevestiging
    observe-run  - Observeer status en logs van een kernel-run
    cleanup      - Voer cleanup uit volgens retentiebeleid

Traceability:
- Runner schrijft traces weg in temp/ voor debugging
- Verwijst naar kernelrunner.py voor daadwerkelijke kernel-run uitvoering

TODO: Implementatie in stap 4 (schrijf runner).
"""

import sys
from pathlib import Path


def main() -> int:
    """Main entry point."""
    print("ERROR: kernel-operator runner nog niet geïmplementeerd", file=sys.stderr)
    print("TODO: Implementeer in Agent Smeder stap 4", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
