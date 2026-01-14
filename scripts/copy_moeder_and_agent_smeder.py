"""Hulpscript: kopieer Moeder en Agent Smeder naar c:/gitrepo/agent-services.

Dit script kopieert voor beide agents:
- charters
- prompts
- runners (Python scripts en pakketten)

Bestemmingsstructuur onder c:/gitrepo/agent-services:
- .github/prompts/
- governance/charters-agents/
- scripts/

Het script is idempotent: bestaande bestanden worden overschreven met de huidige versie.
"""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET_ROOT = Path(r"c:\gitrepo\agent-services")


def ensure_dir(path: Path) -> None:
    """Maak een directory aan als deze nog niet bestaat."""

    path.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dest: Path) -> None:
    """Kopieer één bestand, inclusief aanmaken van de doelmap."""

    ensure_dir(dest.parent)
    shutil.copy2(src, dest)


def copy_tree(src: Path, dest: Path) -> None:
    """Kopieer een complete directoryboom.

    Bestaande map wordt aangemaakt indien nodig; bestaande bestanden
    worden overschreven door shutil.copy2.
    """

    ensure_dir(dest)
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = dest / rel
        if item.is_dir():
            ensure_dir(target)
        else:
            ensure_dir(target.parent)
            shutil.copy2(item, target)


def main() -> None:
    # Bronnen in de standard workspace
    prompts_dir = ROOT / ".github" / "prompts"
    charters_dir = ROOT / "governance" / "charters-agents"
    scripts_dir = ROOT / "scripts"

    # Doelstructuur in agent-services
    target_prompts = TARGET_ROOT / ".github" / "prompts"
    target_charters = TARGET_ROOT / "governance" / "charters-agents"
    target_scripts = TARGET_ROOT / "scripts"

    # 1. Kopieer Moeder prompts
    moeder_prompts = [
        "moeder-beheer-git.prompt.md",
        "moeder-configureer-github.prompt.md",
        "moeder-orden-workspace.prompt.md",
        "moeder-schrijf-beleid.prompt.md",
        "moeder-valideer-governance.prompt.md",
        "moeder-zet-agent-boundary.prompt.md",
    ]

    for name in moeder_prompts:
        src = prompts_dir / name
        dest = target_prompts / name
        if src.exists():
            copy_file(src, dest)

    # 2. Kopieer Agent Smeder prompts
    agent_smeder_prompts = [
        "agent-smeder-1-initiele-agent.prompt.md",
        "agent-smeder-2-definieer-prompt.prompt.md",
        "agent-smeder-3-schrijf-rol.prompt.md",
        "agent-smeder-4-schrijf-runner.prompt.md",
    ]

    for name in agent_smeder_prompts:
        src = prompts_dir / name
        dest = target_prompts / name
        if src.exists():
            copy_file(src, dest)

    # 3. Kopieer charters voor Moeder en Agent Smeder
    moeder_charter = charters_dir / "charter-moeder.md"
    agent_smeder_charter = charters_dir / "charter.agent-smeder.md"

    if moeder_charter.exists():
        copy_file(moeder_charter, target_charters / moeder_charter.name)

    if agent_smeder_charter.exists():
        copy_file(agent_smeder_charter, target_charters / agent_smeder_charter.name)

    # 4. Kopieer runners (scripts en pakketten)
    # Moeder runner: scripts/moeder.py en package scripts/moeder/
    moeder_runner = scripts_dir / "moeder.py"
    if moeder_runner.exists():
        copy_file(moeder_runner, target_scripts / moeder_runner.name)

    moeder_pkg = scripts_dir / "moeder"
    if moeder_pkg.exists() and moeder_pkg.is_dir():
        copy_tree(moeder_pkg, target_scripts / "moeder")

    # Agent Smeder runner: scripts/agent-smeder.py en package scripts/agent_smeder/
    agent_smeder_runner = scripts_dir / "agent-smeder.py"
    if agent_smeder_runner.exists():
        copy_file(agent_smeder_runner, target_scripts / agent_smeder_runner.name)

    agent_smeder_pkg = scripts_dir / "agent_smeder"
    if agent_smeder_pkg.exists() and agent_smeder_pkg.is_dir():
        copy_tree(agent_smeder_pkg, target_scripts / "agent_smeder")


if __name__ == "__main__":
    main()
