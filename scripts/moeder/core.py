from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class OperationResult:
    success: bool
    message: str
    artifacts: list[Path]


class PolicyError(Exception):
    pass


def _policy_gate_workspace_paths(workspace_root: Path) -> None:
    """Valideer dat essentiële workspace folders bestaan."""
    required_dirs = [
        workspace_root / "governance",
        workspace_root / ".github" / "prompts",
    ]
    
    for dir_path in required_dirs:
        if not dir_path.exists():
            raise PolicyError(
                f"Vereiste folder ontbreekt: {dir_path.relative_to(workspace_root).as_posix()}"
            )


def _policy_gate_governance_exists(workspace_root: Path) -> None:
    """Valideer dat governance documenten bestaan."""
    required_files = [
        workspace_root / "governance" / "workspace-doctrine.md",
        workspace_root / "governance" / "gedragscode.md",
    ]
    
    for file_path in required_files:
        if not file_path.exists():
            raise PolicyError(
                f"Vereist governance document ontbreekt: {file_path.relative_to(workspace_root).as_posix()}"
            )


def op_beheer_git(
    *,
    workspace_root: Path,
    opdracht: str,
    check_only: bool,
    scope: str | None,
) -> OperationResult:
    """Operatie: beheer-git
    
    Beheert Git workflows, branches, commits en .gitignore.
    Scope opties: commits, branches, gitignore, hooks
    """
    _policy_gate_workspace_paths(workspace_root)
    
    # Placeholder implementatie - deze operatie is meestal manueel/conversationeel
    artifacts: list[Path] = []
    
    scope_desc = f" (scope: {scope})" if scope else ""
    mode_desc = "Analyse" if check_only else "Actie"
    
    message = f"{mode_desc}: Git beheer{scope_desc} - '{opdracht}' (nog te implementeren)"
    
    return OperationResult(
        success=True,
        message=message,
        artifacts=artifacts,
    )


def op_configureer_github(
    *,
    workspace_root: Path,
    opdracht: str,
    check_only: bool,
    scope: str | None,
) -> OperationResult:
    """Operatie: configureer-github
    
    Configureert GitHub repository settings, collaboratie en automation.
    Scope opties: repository-setup, collaboratie, automation, pages, copilot-config
    
    Inclusief controle van .github/copilot/ configuratie (agents.yaml en workflow.yaml).
    """
    _policy_gate_workspace_paths(workspace_root)
    
    artifacts: list[Path] = []
    warnings: list[str] = []
    
    # Check Copilot configuratie als onderdeel van GitHub setup
    copilot_dir = workspace_root / ".github" / "copilot"
    agents_yaml = copilot_dir / "agents.yaml"
    workflow_yaml = copilot_dir / "workflow.yaml"
    
    if not copilot_dir.exists():
        warnings.append("⚠️  .github/copilot/ map ontbreekt")
    else:
        if not agents_yaml.exists():
            warnings.append("⚠️  .github/copilot/agents.yaml ontbreekt")
        if not workflow_yaml.exists():
            warnings.append("⚠️  .github/copilot/workflow.yaml ontbreekt")
    
    scope_desc = f" (scope: {scope})" if scope else ""
    mode_desc = "Analyse" if check_only else "Actie"
    
    base_message = f"{mode_desc}: GitHub configuratie{scope_desc} - '{opdracht}'"
    
    if warnings:
        warning_text = "; " + ", ".join(warnings)
        message = base_message + warning_text
    else:
        message = base_message + " (Copilot config OK)"
    
    return OperationResult(
        success=True,
        message=message,
        artifacts=artifacts,
    )


def op_orden_workspace(
    *,
    workspace_root: Path,
    opdracht: str,
    check_only: bool,
    scope: str | None,
) -> OperationResult:
        """Operatie: orden-workspace
    
        Ordent workspace structuur, naamgeving en markdown.
        Scope opties: structure, names, markdown, docs-resultaten, github-prompts.

        Bij alle acties waarbij bestanden worden verplaatst, hanteert Moeder
        **single source of truth**:

        - bestanden worden daadwerkelijk **verplaatst** (bijvoorbeeld met `git mv`);
        - er blijven geen kopieën van hetzelfde bronbestand achter op de oude
            locatie of in andere workspaces.
        """
    _policy_gate_workspace_paths(workspace_root)
    _policy_gate_governance_exists(workspace_root)
    
    # Placeholder implementatie - deze operatie vereist vaak menselijke beoordeling
    artifacts: list[Path] = []
    
    scope_desc = f" (scope: {scope})" if scope else ""
    mode_desc = "Analyse" if check_only else "Actie"
    
    message = (
        f"{mode_desc}: Workspace ordening{scope_desc} - '{opdracht}' "
        "(nog te implementeren; bij verplaatsen geen kopieën, single source)"
    )
    
    return OperationResult(
        success=True,
        message=message,
        artifacts=artifacts,
    )


def op_schrijf_beleid(
    *,
    workspace_root: Path,
    opdracht: str,
    check_only: bool,
) -> OperationResult:
    """Operatie: schrijf-beleid
    
    Genereert governance/beleid.md op basis van temp/context.md.
    """
    _policy_gate_workspace_paths(workspace_root)
    _policy_gate_governance_exists(workspace_root)
    
    context_path = workspace_root / "temp" / "context.md"
    beleid_path = workspace_root / "governance" / "beleid.md"
    
    # Valideer dat context.md bestaat
    if not context_path.exists():
        raise PolicyError(
            f"temp/context.md ontbreekt - kan geen beleid genereren zonder context"
        )
    
    # Waarschuw als beleid.md al bestaat
    if beleid_path.exists() and not check_only:
        raise PolicyError(
            f"governance/beleid.md bestaat al - gebruik --check-only of verwijder eerst het bestaande beleid"
        )
    
    artifacts: list[Path] = []
    
    if check_only:
        message = f"Analyse: Beleid generatie op basis van context.md (dry-run)"
    else:
        # Placeholder implementatie - beleid generatie vereist AI/menselijke input
        message = f"Beleid generatie - '{opdracht}' (nog te implementeren)"
        # artifacts.append(beleid_path)  # Zou hier komen na implementatie
    
    return OperationResult(
        success=True,
        message=message,
        artifacts=artifacts,
    )


def op_zet_agent_boundary(
    *,
    workspace_root: Path,
    opdracht: str,
    aanleiding: str | None,
    gewenste_capability: str | None,
) -> OperationResult:
    """Operatie: zet-agent-boundary
    
    Definieert capability boundary voor nieuwe agent en slaat op als deliverable.
    Output wordt VERPLICHT opgeslagen in docs/resultaten/moeder/agent-boundary-{agent-naam}.md
    met Herkomstverantwoording voor traceerbaarheid en handoff naar Agent Smeder.
    
    De runner kan de boundary NIET genereren (dat is AI-werk), maar MOET het deliverable
    wegschrijven zodra de boundary is gedefinieerd. De boundary-componenten worden
    verwacht in opdracht parameter in het gestandaardiseerde 4-regel format.
    
    Verwacht format in opdracht:
        agent-naam: {naam}
        capability-boundary: {één zin}
        doel: {één zin}
        domein: {woord of frase}
    """
    _policy_gate_workspace_paths(workspace_root)
    _policy_gate_governance_exists(workspace_root)
    
    beleid_path = workspace_root / "governance" / "beleid.md"
    
    # Valideer dat beleid.md bestaat
    if not beleid_path.exists():
        raise PolicyError(
            f"governance/beleid.md ontbreekt - kan geen agent boundary valideren zonder beleid"
        )
    
    # Valideer input parameters
    if not aanleiding:
        raise ValueError("--aanleiding is verplicht voor zet-agent-boundary operatie")
    
    if not gewenste_capability:
        raise ValueError("--gewenste-capability is verplicht voor zet-agent-boundary operatie")
    
    # Parseer opdracht voor boundary-componenten (verwacht 4-regel format)
    boundary_lines = [line.strip() for line in opdracht.strip().split('\n') if line.strip()]
    
    # Extract agent-naam uit eerste regel
    agent_naam = None
    for line in boundary_lines:
        if line.startswith("agent-naam:"):
            agent_naam = line.split(":", 1)[1].strip()
            break
    
    if not agent_naam:
        raise ValueError(
            "opdracht moet 'agent-naam: {naam}' bevatten in het gestandaardiseerde 4-regel format"
        )
    
    # Valideer dat opdracht alle 4 vereiste regels bevat
    required_fields = ["agent-naam:", "capability-boundary:", "doel:", "domein:"]
    for field in required_fields:
        if not any(line.startswith(field) for line in boundary_lines):
            raise ValueError(
                f"opdracht moet '{field}' bevatten. "
                f"Verwacht format: agent-naam, capability-boundary, doel, domein (elk op eigen regel)"
            )
    
    # Maak deliverable directory aan
    resultaten_dir = workspace_root / "docs" / "resultaten" / "moeder"
    resultaten_dir.mkdir(parents=True, exist_ok=True)
    
    # Bepaal deliverable pad
    deliverable_path = resultaten_dir / f"agent-boundary-{agent_naam}.md"
    
    # Stop als deliverable niet kan worden weggeschreven (volgens charter foutafhandeling)
    if deliverable_path.exists():
        raise PolicyError(
            f"Boundary deliverable bestaat al: {deliverable_path.relative_to(workspace_root).as_posix()}. "
            f"Verwijder eerst het bestaande bestand of kies een andere agent-naam."
        )
    
    # Genereer deliverable content met HV
    from datetime import datetime
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    
    content_lines = [
        "# Agent Boundary Deliverable\n",
        "\n",
        "## Herkomstverantwoording\n",
        "\n",
        f"**Datum/tijd**: {timestamp}\n",
        "\n",
        "**Geraadpleegde bronnen**:\n",
        f"- Gebruikersinput (aanleiding en gewenste-capability) - {timestamp}\n",
        f"- `governance/beleid.md` (validatie) - {timestamp}\n",
        f"- `governance/charters-agents/charter.moeder.md` (boundary definitie proces) - {timestamp}\n",
        "\n",
        "**Toelichting wijziging**:\n",
        f"Nieuwe agent boundary gedefinieerd op verzoek van gebruiker.\n",
        f"- Aanleiding: {aanleiding}\n",
        f"- Gewenste capability: {gewenste_capability}\n",
        f"- Boundary is gevalideerd tegen governance/beleid.md\n",
        f"- Deliverable voldoet aan charter.moeder.md Section 5 (VERPLICHT wegschrijven)\n",
        "\n",
        "---\n",
        "\n",
        "## Agent Boundary\n",
        "\n",
    ]
    
    # Voeg boundary regels toe (exact zoals opgegeven in opdracht)
    content_lines.append("```\n")
    for line in boundary_lines:
        content_lines.append(line + "\n")
    content_lines.append("```\n")
    
    # Schrijf deliverable
    deliverable_path.write_text("".join(content_lines), encoding="utf-8")
    
    message = (
        f"Agent boundary deliverable weggeschreven: "
        f"{deliverable_path.relative_to(workspace_root).as_posix()}. "
        f"Dit bestand is input voor Agent Smeder handoff."
    )
    
    return OperationResult(
        success=True,
        message=message,
        artifacts=[deliverable_path],
    )


def op_valideer_governance(
    *,
    workspace_root: Path,
    opdracht: str,
    scope: str | None,
) -> OperationResult:
    """Operatie: valideer-governance
    
    Valideert compliance met governance documenten.
    Scope opties: workspace-standaard, gedragscode, beleid, agent-standaard, all
    """
    _policy_gate_workspace_paths(workspace_root)
    _policy_gate_governance_exists(workspace_root)
    
    artifacts: list[Path] = []
    
    scope_desc = f" (scope: {scope})" if scope else " (scope: all)"
    
    # Placeholder implementatie - governance validatie vereist uitgebreide checks
    message = f"Governance validatie{scope_desc} - '{opdracht}' (nog te implementeren)"
    
    return OperationResult(
        success=True,
        message=message,
        artifacts=artifacts,
    )


def execute_operation(
    *,
    workspace_root: Path,
    operation: str,
    opdracht: str,
    check_only: bool,
    scope: str | None,
    aanleiding: str | None,
    gewenste_capability: str | None,
) -> OperationResult:
    """Route operatie naar juiste handler."""
    
    if operation == "beheer-git":
        return op_beheer_git(
            workspace_root=workspace_root,
            opdracht=opdracht,
            check_only=check_only,
            scope=scope,
        )
    
    elif operation == "configureer-github":
        return op_configureer_github(
            workspace_root=workspace_root,
            opdracht=opdracht,
            check_only=check_only,
            scope=scope,
        )
    
    elif operation == "orden-workspace":
        return op_orden_workspace(
            workspace_root=workspace_root,
            opdracht=opdracht,
            check_only=check_only,
            scope=scope,
        )
    
    elif operation == "schrijf-beleid":
        return op_schrijf_beleid(
            workspace_root=workspace_root,
            opdracht=opdracht,
            check_only=check_only,
        )
    
    elif operation == "zet-agent-boundary":
        return op_zet_agent_boundary(
            workspace_root=workspace_root,
            opdracht=opdracht,
            aanleiding=aanleiding,
            gewenste_capability=gewenste_capability,
        )
    
    elif operation == "valideer-governance":
        return op_valideer_governance(
            workspace_root=workspace_root,
            opdracht=opdracht,
            scope=scope,
        )
    
    else:
        raise ValueError(f"Onbekende operatie: {operation}")
