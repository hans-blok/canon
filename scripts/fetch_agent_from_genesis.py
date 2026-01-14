#!/usr/bin/env python3
"""Fetch één agent uit een Genesis workspace en overschrijf lokale artefacten.

Gebruik:
    python scripts/fetch_agent_from_genesis.py \
        --genesis-root ../genesis-standard \
        --agent-naam essayist \
        [--dry-run]

Dit script gaat er vanuit dat Genesis en deze workspace **dezelfde basisstructuur** delen
voor agent-artefacten (zie artefacten/0-governance/agent-charter-normering.md):
- Rolbeschrijving:    governance/rolbeschrijvingen/<agent-naam>.md
- Prompt-contract:    .github/prompts/<agent-naam>.prompt.md of .github/prompts/std.<agent-naam>.prompt.md
- Charter (optioneel): governance/charters-agents/ (meerdere naamgevingsvarianten, zie COMPONENT_PATTERNS)
- Runner (optioneel): scripts/<agent-naam>.py

Alle gevonden bestanden in Genesis worden één-op-één gekopieerd naar deze workspace
(overschrijven is toegestaan). Bestaat een bestand hier nog niet, dan wordt het aangemaakt.

Het script verandert **nooit** iets in Genesis, alleen in de huidige workspace.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


# Mogelijke componenten en naamgevingsvarianten
COMPONENT_PATTERNS: dict[str, list[str]] = {
    "rolbeschrijving": [
        "governance/rolbeschrijvingen/{agent_naam}.md",
    ],
    "prompt": [
        ".github/prompts/{agent_naam}.prompt.md",
        ".github/prompts/std.{agent_naam}.prompt.md",
    ],
    "charter": [
        "governance/charters-agents/charter.{agent_naam}.md",
        "governance/charters-agents/charter.agent-{agent_naam}.md",
        "governance/charters-agents/std.agent.charter.{agent_naam}.md",
    ],
    "runner": [
        "scripts/{agent_naam}.py",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch één agent uit een Genesis workspace en overschrijf lokale artefacten."
        )
    )

    parser.add_argument(
        "--genesis-root",
        required=True,
        help="Pad naar de Genesis workspace (directory)",
    )

    parser.add_argument(
        "--agent-naam",
        required=True,
        help="Naam van de agent (lowercase met hyphens)",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Laat alleen zien wat er zou gebeuren, zonder bestanden te overschrijven.",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    workspace_root = Path(__file__).parent.parent.resolve()
    genesis_root = Path(args.genesis_root).resolve()
    agent_naam = args.agent_naam.strip()

    if not genesis_root.is_dir():
        print(f"ERROR: Genesis-root bestaat niet of is geen directory: {genesis_root}")
        return 1

    print(f"Workspace: {workspace_root}")
    print(f"Genesis-root: {genesis_root}")
    print(f"Agent: {agent_naam}")
    if args.dry_run:
        print("Mode: DRY RUN (geen bestanden worden overschreven)")
    print()

    copied_any = False

    for component, patterns in COMPONENT_PATTERNS.items():
        for pattern in patterns:
            rel_path_str = pattern.format(agent_naam=agent_naam)
            src = genesis_root / rel_path_str
            dst = workspace_root / rel_path_str

            if not src.is_file():
                continue

            dst.parent.mkdir(parents=True, exist_ok=True)

            if args.dry_run:
                action = "ZOU kopiëren"
            else:
                shutil.copy2(src, dst)
                action = "GEKOPIEERD"

            print(f"[{component}] {action}: {src} -> {dst}")
            copied_any = True

        # visuele scheiding per component
        print()

    if not copied_any:
        print(
            "WAARSCHUWING: Geen artefacten gevonden voor deze agent in Genesis "
            "(controleer agent-naam en structuur)."
        )
        return 1

    print("Klaar: agent is bijgewerkt op basis van Genesis.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
