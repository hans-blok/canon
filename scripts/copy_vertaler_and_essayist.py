"""Kopieer Vertaler- en Essayist-agent artefacten naar c:/gitrepo/agent-services.

Dit script kopieert voor de agents **Vertaler** en **Essayist** de belangrijkste
artefacten vanuit de `standard` workspace naar de `agent-services` workspace:

- GitHub prompts (.github/prompts)
- Rolbeschrijvingen (governance/rolbeschrijvingen)
- Python runners (scripts/*.py)

Het script voert **alleen lokale kopieer-acties** uit en doet geen Git- of
GitHub-operaties. Het past dus binnen de grenzen van Moeder-beheer-git:
- geen push
- geen remote operaties
- alleen lokale bestandsmutaties.
"""

from __future__ import annotations

from pathlib import Path
import shutil


def ensure_dir(path: Path) -> None:
    """Zorg dat de doelmap bestaat."""

    path.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dest: Path) -> None:
    """Kopieer één bestand naar dest, maak de doelmap indien nodig."""

    ensure_dir(dest.parent)
    shutil.copy2(src, dest)


def main() -> None:
    workspace_root = Path(__file__).resolve().parents[1]
    target_root = Path(r"c:\gitrepo\agent-services")

    # Definieer alle relevante paden voor Vertaler en Essayist
    items: list[tuple[Path, Path]] = []

    # Vertaler: prompt, rolbeschrijving, runner
    items.append(
        (
            workspace_root / ".github" / "prompts" / "vertaler-vertaal.prompt.md",
            target_root / ".github" / "prompts" / "vertaler-vertaal.prompt.md",
        )
    )
    items.append(
        (
            workspace_root
            / "governance"
            / "rolbeschrijvingen"
            / "vertaler.md",
            target_root
            / "governance"
            / "rolbeschrijvingen"
            / "vertaler.md",
        )
    )
    items.append(
        (
            workspace_root / "scripts" / "vertaler.py",
            target_root / "scripts" / "vertaler.py",
        )
    )

    # Essayist: prompt, rolbeschrijving, runner
    items.append(
        (
            workspace_root
            / ".github"
            / "prompts"
            / "essayist-schrijf-essay.prompt.md",
            target_root
            / ".github"
            / "prompts"
            / "essayist-schrijf-essay.prompt.md",
        )
    )
    items.append(
        (
            workspace_root
            / "governance"
            / "rolbeschrijvingen"
            / "essayist.md",
            target_root
            / "governance"
            / "rolbeschrijvingen"
            / "essayist.md",
        )
    )
    items.append(
        (
            workspace_root / "scripts" / "essayist.py",
            target_root / "scripts" / "essayist.py",
        )
    )

    for src, dest in items:
        if not src.exists():
            print(f"[WAARSCHUWING] Bron ontbreekt, sla over: {src}")
            continue
        copy_file(src, dest)
        print(f"[OK] Gekopieerd: {src} -> {dest}")


if __name__ == "__main__":  # pragma: no cover
    main()
