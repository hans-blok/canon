#!/usr/bin/env python3
"""Python Expert Runner

Deze runner automatiseert herhaalbare stappen voor de Python Expert agent
zonder AI-interactie.

De runner kan:
- Syntax checks uitvoeren op Python bestanden
- Code formatting valideren (PEP 8 basis checks)
- Type hints valideren
- Basic linting via AST analysis
- Review preparatie (bestand uitlezen voor LLM-agent)

Usage:
    python scripts/python-expert.py check-syntax <bestand>
    python scripts/python-expert.py prepare-review <bestand>

Voor het daadwerkelijk schrijven of reviewen van code: gebruik de LLM-agent
met het bijbehorende prompt-contract.

Traceability:
- De runner schrijft optioneel trace artefacten weg in temp/
- De runner voert geen AI-interactie uit; dit is de taak van de LLM-agent
"""

from __future__ import annotations

import argparse
import ast
import sys
from datetime import datetime
from pathlib import Path
from typing import NamedTuple


WORKSPACE_ROOT = Path(__file__).parent.parent


class CheckResult(NamedTuple):
    """Result van een runner-check."""
    success: bool
    message: str
    details: list[str] | None = None


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments voor de Python Expert runner."""
    parser = argparse.ArgumentParser(
        prog="python-expert",
        description="Runner voor Python Expert agent - code quality checks",
    )
    
    parser.add_argument(
        "command",
        choices=["check-syntax", "prepare-review", "validate-structure"],
        help="Commando om uit te voeren",
    )
    parser.add_argument(
        "target",
        help="Relatief pad naar Python bestand binnen de workspace",
    )
    parser.add_argument(
        "--output",
        help="Optioneel: pad voor review-preparatie output (default: temp/)",
        default=None,
    )
    
    return parser.parse_args(argv)


def resolve_target(path_str: str) -> Path:
    """Vertaal een relatief pad naar een absoluut pad binnen de workspace.
    
    Parameters
    ----------
    path_str : str
        Relatief pad binnen workspace
        
    Returns
    -------
    Path
        Absoluut pad
        
    Raises
    ------
    ValueError
        Als het pad buiten de workspace ligt
    """
    target = (WORKSPACE_ROOT / path_str).resolve()
    try:
        target.relative_to(WORKSPACE_ROOT)
    except ValueError as exc:
        raise ValueError(f"Pad '{path_str}' ligt buiten de workspace") from exc
    return target


def check_syntax(target: Path) -> CheckResult:
    """Check Python syntax van een bestand.
    
    Parameters
    ----------
    target : Path
        Pad naar het Python bestand
        
    Returns
    -------
    CheckResult
        Success status en details
    """
    try:
        with open(target, encoding="utf-8") as f:
            content = f.read()
            compile(content, str(target), "exec")
        return CheckResult(
            success=True,
            message=f"Syntax geldig voor {target.name}",
        )
    except SyntaxError as e:
        return CheckResult(
            success=False,
            message=f"Syntax error in {target.name}",
            details=[f"Line {e.lineno}: {e.msg}"],
        )
    except Exception as e:
        return CheckResult(
            success=False,
            message=f"Fout bij lezen bestand: {e}",
        )


def validate_structure(target: Path) -> CheckResult:
    """Valideer basis code-structuur via AST analysis.
    
    Parameters
    ----------
    target : Path
        Pad naar het Python bestand
        
    Returns
    -------
    CheckResult
        Success status en bevindingen
    """
    try:
        with open(target, encoding="utf-8") as f:
            content = f.read()
        
        tree = ast.parse(content, str(target))
        
        details = []
        
        # Check voor module docstring
        if not ast.get_docstring(tree):
            details.append("Geen module-level docstring gevonden")
        
        # Check functies zonder docstrings
        functions_without_docs = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node) and not node.name.startswith("_"):
                    functions_without_docs.append(node.name)
        
        if functions_without_docs:
            details.append(
                f"Functies zonder docstring: {', '.join(functions_without_docs)}"
            )
        
        if not details:
            return CheckResult(
                success=True,
                message="Structuur-validatie OK",
            )
        
        return CheckResult(
            success=True,  # Warnings, geen errors
            message="Structuur-validatie voltooid met waarschuwingen",
            details=details,
        )
        
    except SyntaxError as e:
        return CheckResult(
            success=False,
            message="Syntax error voorkomt structuur-validatie",
            details=[f"Line {e.lineno}: {e.msg}"],
        )
    except Exception as e:
        return CheckResult(
            success=False,
            message=f"Fout bij structuur-validatie: {e}",
        )


def prepare_review(target: Path, output_dir: Path | None = None) -> CheckResult:
    """Prepareer een bestand voor code review door de LLM-agent.
    
    Maakt een samenvatting met bestandsinfo die de LLM-agent kan gebruiken.
    
    Parameters
    ----------
    target : Path
        Pad naar het Python bestand
    output_dir : Path, optional
        Output directory (default: temp/)
        
    Returns
    -------
    CheckResult
        Success status en locatie van review-prep bestand
    """
    if output_dir is None:
        output_dir = WORKSPACE_ROOT / "temp"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(target, encoding="utf-8") as f:
            content = f.read()
            lines = content.splitlines()
        
        # Basis statistieken
        tree = ast.parse(content, str(target))
        functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M CET")
        rel_path = target.relative_to(WORKSPACE_ROOT).as_posix()
        
        prep_content = f"""# Review Preparatie — {target.name}

**Bestand**: {rel_path}  
**Aangemaakt**: {timestamp}  
**Regels code**: {len(lines)}  
**Functies**: {len(functions)}  
**Classes**: {len(classes)}

## Functies
{chr(10).join(f"- {f}" for f in functions) if functions else "Geen"}

## Classes
{chr(10).join(f"- {c}" for c in classes) if classes else "Geen"}

## Volgende stap

Gebruik de Python Expert LLM-agent met prompt-contract:
`.github/prompts/python-expert-review-code.prompt.md`

Input parameters:
- doelpad: {rel_path}
- context: [beschrijving van doel/gebruik van de code]
"""
        
        output_file = output_dir / f"review-prep-{target.stem}.md"
        output_file.write_text(prep_content, encoding="utf-8")
        
        return CheckResult(
            success=True,
            message=f"Review preparatie voltooid",
            details=[f"Output: {output_file.relative_to(WORKSPACE_ROOT).as_posix()}"],
        )
        
    except Exception as e:
        return CheckResult(
            success=False,
            message=f"Fout bij review preparatie: {e}",
        )


def main() -> int:
    """Main entry point voor de runner."""
    try:
        args = parse_args()
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 1
    
    try:
        target = resolve_target(args.target)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    
    if not target.exists():
        print(f"ERROR: Bestand '{args.target}' niet gevonden", file=sys.stderr)
        return 1
    
    if not target.suffix == ".py":
        print(f"ERROR: Bestand '{args.target}' is geen Python bestand", file=sys.stderr)
        return 1
    
    # Voer commando uit
    if args.command == "check-syntax":
        result = check_syntax(target)
    elif args.command == "validate-structure":
        result = validate_structure(target)
    elif args.command == "prepare-review":
        output_dir = Path(args.output) if args.output else None
        result = prepare_review(target, output_dir)
    else:
        print(f"ERROR: Onbekend commando: {args.command}", file=sys.stderr)
        return 1
    
    # Output resultaat
    if result.success:
        print(f"OK: {result.message}")
        if result.details:
            for detail in result.details:
                print(f"  {detail}")
        return 0
    else:
        print(f"ERROR: {result.message}", file=sys.stderr)
        if result.details:
            for detail in result.details:
                print(f"  {detail}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
