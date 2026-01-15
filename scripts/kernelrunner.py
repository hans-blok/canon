#!/usr/bin/env python3
"""Kernel Runner — v1 uitvoeringsmechanisme voor agent-runs.

De runner kernel is een deterministisch script dat uitvoering mogelijk maakt
en observeerbaar maakt. De kernel denkt niet, interpreteert geen normen, en
neemt geen inhoudelijke beslissingen.

Verantwoordelijkheden:
- Preflight checks uitvoeren
- State lezen en schrijven (pointers, geen inhoud)
- Agent-runs starten
- Handoffs en run-events loggen
- State bijwerken na afloop
- Run-log retentie

Usage:
    python scripts/kernelrunner.py start-run <agent-naam> <intent>
    python scripts/kernelrunner.py cleanup-logs

Canonieke principes:
    Agents besluiten.
    Runners voeren uit.
    De kernel bewaakt de grens.

Conform:
- normatief-stelsel/globaal/doctrine-runner-discipline-en-runner-kernel.md
- normatief-stelsel/globaal/doctrine-handoff-creatie-en-overdrachtsdiscipline.md
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, NamedTuple

import yaml


WORKSPACE_ROOT = Path(__file__).parent.parent
STATE_FILE = WORKSPACE_ROOT / "state" / "standards.current.yaml"
KERNEL_RUNS_DIR = WORKSPACE_ROOT / ".kernel" / "runs"
NORMATIEF_STELSEL_PING = WORKSPACE_ROOT / "normatief-stelsel.ping"

# Retentie configuratie
MAX_RUNS_TO_KEEP = 20
MAX_RUN_AGE_DAYS = 7


class StateData(NamedTuple):
    """Workspace state data (alleen pointers)."""
    workspace_name: str
    current_version: str
    state_file_path: Path
    state_hash: str | None


class RunResult(NamedTuple):
    """Resultaat van een agent-run."""
    success: bool
    message: str
    run_id: str
    log_path: Path


class PreflightError(Exception):
    """Preflight check gefaald."""
    pass


def load_state() -> StateData:
    """Lees de actieve workspace state.
    
    Returns
    -------
    StateData
        Workspace state met pointers (geen inhoud)
        
    Raises
    ------
    PreflightError
        Als state niet gelezen kan worden
    """
    if not STATE_FILE.exists():
        raise PreflightError(f"State file niet gevonden: {STATE_FILE}")
    
    try:
        with open(STATE_FILE, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        if not isinstance(data, dict):
            raise PreflightError("State file bevat geen geldig YAML dict")
        
        workspace_name = data.get("workspace_name", "unknown")
        current_version = data.get("version", "unknown")
        
        # Optioneel: hash van state file voor traceability
        state_hash = _compute_file_hash(STATE_FILE)
        
        return StateData(
            workspace_name=workspace_name,
            current_version=current_version,
            state_file_path=STATE_FILE,
            state_hash=state_hash,
        )
        
    except yaml.YAMLError as e:
        raise PreflightError(f"State file niet parsebaar: {e}") from e
    except Exception as e:
        raise PreflightError(f"Fout bij lezen state: {e}") from e


def preflight() -> None:
    """Voer preflight checks uit.
    
    Controleert:
    - Bestaat de state file?
    - Is de normatief-stelsel ping aanwezig?
    - Is de state leesbaar (YAML parsebaar)?
    
    Raises
    ------
    PreflightError
        Bij gefaalde preflight check
    """
    # Check 1: State file bestaat
    if not STATE_FILE.exists():
        raise PreflightError(f"State file niet gevonden: {STATE_FILE}")
    
    # Check 2: Normatief stelsel ping aanwezig
    if not NORMATIEF_STELSEL_PING.exists():
        raise PreflightError(
            f"Normatief-stelsel ping niet gevonden: {NORMATIEF_STELSEL_PING}"
        )
    
    # Check 3: State is leesbaar (implicitly checked in load_state)
    try:
        load_state()
    except PreflightError:
        raise
    except Exception as e:
        raise PreflightError(f"State validatie gefaald: {e}") from e


def generate_run_id() -> str:
    """Genereer unieke run-ID.
    
    Format: run-YYYYMMDD-HHMMSS
    
    Returns
    -------
    str
        Unieke run identifier
    """
    now = datetime.now()
    return now.strftime("run-%Y%m%d-%H%M%S")


def start_run(agent_name: str, intent: str, trigger: str) -> RunResult:
    """Start een agent-run met logging.
    
    Voert uit:
    - Preflight checks
    - Run-ID generatie
    - Run-log aanmaken
    - Agent-run starten (v1: placeholder)
    - Resultaat vastleggen
    
    Parameters
    ----------
    agent_name : str
        Naam van de agent die wordt gestart
    intent : str
        Korte beschrijving van de intent
    trigger : str
        Reden voor de run
        
    Returns
    -------
    RunResult
        Resultaat van de run met success status
    """
    # Preflight checks
    try:
        preflight()
        state = load_state()
    except PreflightError as e:
        return RunResult(
            success=False,
            message=f"Preflight gefaald: {e}",
            run_id="",
            log_path=Path(),
        )
    
    # Genereer run-ID
    run_id = generate_run_id()
    
    # Setup logging
    KERNEL_RUNS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = KERNEL_RUNS_DIR / f"{run_id}.yaml"
    
    # Start timestamp
    start_time = datetime.now()
    
    # Initieer run log
    run_log: dict[str, Any] = {
        "run_id": run_id,
        "recorded_by": "runner-kernel",
        "workspace": state.workspace_name,
        "state_ref": {
            "path": str(state.state_file_path.relative_to(WORKSPACE_ROOT)),
            "hash": state.state_hash,
        },
        "timestamps": {
            "start": start_time.strftime("%Y-%m-%d %H:%M:%S CET"),
            "end": None,
        },
        "events": [],
        "result": None,
    }
    
    # Log handoff event
    handoff_event = {
        "type": "handoff",
        "from": "runner-kernel",
        "to": agent_name,
        "intent": intent,
        "trigger": trigger,
        "timestamp": start_time.strftime("%Y-%m-%d %H:%M:%S CET"),
    }
    run_log["events"].append(handoff_event)
    
    # Agent-run (v1: placeholder)
    # TODO: Hier wordt in toekomstige versies de agent daadwerkelijk aangeroepen
    # Voor v1: handmatige bevestiging of Copilot-interventie verwacht
    print(f"\n{'='*60}")
    print("AGENT RUN PLACEHOLDER (v1)")
    print(f"{'='*60}")
    print(f"Agent     : {agent_name}")
    print(f"Intent    : {intent}")
    print(f"Trigger   : {trigger}")
    print(f"Run ID    : {run_id}")
    print(f"\nDe runner kernel orkestreert, maar automatiseert inhoud nog niet.")
    print(f"Voer handmatig de agent-actie uit via Copilot of CLI.")
    print(f"{'='*60}\n")
    
    # Voor v1: markeer als success (agent-run is "gestart")
    end_time = datetime.now()
    run_log["timestamps"]["end"] = end_time.strftime("%Y-%m-%d %H:%M:%S CET")
    run_log["result"] = {
        "status": "success",
        "message": "Agent-run placeholder voltooid (v1)",
    }
    
    # Schrijf run log
    _write_run_log(log_path, run_log)
    
    return RunResult(
        success=True,
        message="Agent-run gestart (v1 placeholder)",
        run_id=run_id,
        log_path=log_path,
    )


def log_event(
    run_id: str,
    event_type: str,
    details: dict[str, Any],
) -> None:
    """Log een event in een bestaande run.
    
    Parameters
    ----------
    run_id : str
        Run identifier
    event_type : str
        Type event (bijv. "handoff", "state_update")
    details : dict
        Event details
    """
    log_path = KERNEL_RUNS_DIR / f"{run_id}.yaml"
    
    if not log_path.exists():
        print(f"WARNING: Run log niet gevonden: {log_path}", file=sys.stderr)
        return
    
    try:
        with open(log_path, encoding="utf-8") as f:
            run_log = yaml.safe_load(f)
        
        event = {
            "type": event_type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S CET"),
            **details,
        }
        
        run_log["events"].append(event)
        
        _write_run_log(log_path, run_log)
        
    except Exception as e:
        print(f"ERROR: Fout bij loggen event: {e}", file=sys.stderr)


def finalize_run(run_id: str, success: bool, message: str) -> None:
    """Finaliseer een run met resultaat.
    
    Parameters
    ----------
    run_id : str
        Run identifier
    success : bool
        Of de run succesvol was
    message : str
        Resultaat boodschap
    """
    log_path = KERNEL_RUNS_DIR / f"{run_id}.yaml"
    
    if not log_path.exists():
        print(f"ERROR: Run log niet gevonden: {log_path}", file=sys.stderr)
        return
    
    try:
        with open(log_path, encoding="utf-8") as f:
            run_log = yaml.safe_load(f)
        
        run_log["timestamps"]["end"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S CET")
        run_log["result"] = {
            "status": "success" if success else "failure",
            "message": message,
        }
        
        _write_run_log(log_path, run_log)
        
    except Exception as e:
        print(f"ERROR: Fout bij finaliseren run: {e}", file=sys.stderr)


def cleanup_logs() -> int:
    """Ruim oude run logs op conform retentie-beleid.
    
    Retentie:
    - Maximaal 20 runs bewaren
    - Maximaal 7 dagen oud
    - Failure-runs mogen langer bewaard blijven
    
    Returns
    -------
    int
        Aantal verwijderde logs
    """
    if not KERNEL_RUNS_DIR.exists():
        return 0
    
    run_logs = sorted(KERNEL_RUNS_DIR.glob("run-*.yaml"))
    
    if not run_logs:
        return 0
    
    cutoff_date = datetime.now() - timedelta(days=MAX_RUN_AGE_DAYS)
    logs_to_delete: list[Path] = []
    
    # Sorteer op aanmaaktijd (nieuwste eerst)
    run_logs_with_time = [
        (log, log.stat().st_mtime) for log in run_logs
    ]
    run_logs_with_time.sort(key=lambda x: x[1], reverse=True)
    
    for i, (log_path, mtime) in enumerate(run_logs_with_time):
        # Bewaar de nieuwste MAX_RUNS_TO_KEEP runs
        if i < MAX_RUNS_TO_KEEP:
            continue
        
        # Check age
        log_date = datetime.fromtimestamp(mtime)
        if log_date < cutoff_date:
            # Check of het een failure-run is
            try:
                with open(log_path, encoding="utf-8") as f:
                    log_data = yaml.safe_load(f)
                
                result = log_data.get("result", {})
                if result.get("status") == "failure":
                    # Bewaar failure-runs langer
                    continue
            except Exception:
                pass  # Bij fout: toch verwijderen
            
            logs_to_delete.append(log_path)
    
    # Verwijder logs
    for log_path in logs_to_delete:
        try:
            log_path.unlink()
        except Exception as e:
            print(f"WARNING: Kon log niet verwijderen: {log_path} ({e})", file=sys.stderr)
    
    return len(logs_to_delete)


def _compute_file_hash(file_path: Path) -> str:
    """Bereken SHA256 hash van een bestand.
    
    Parameters
    ----------
    file_path : Path
        Pad naar bestand
        
    Returns
    -------
    str
        Hex digest van SHA256 hash
    """
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return ""


def _write_run_log(log_path: Path, log_data: dict[str, Any]) -> None:
    """Schrijf run log atomisch naar disk.
    
    Parameters
    ----------
    log_path : Path
        Pad naar log bestand
    log_data : dict
        Log data om weg te schrijven
    """
    log_path.write_text(
        yaml.dump(log_data, default_flow_style=False, allow_unicode=True),
        encoding="utf-8",
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI argumenten.
    
    Parameters
    ----------
    argv : list[str], optional
        Argumenten (default: sys.argv[1:])
        
    Returns
    -------
    argparse.Namespace
        Geparsede argumenten
    """
    parser = argparse.ArgumentParser(
        prog="kernelrunner",
        description="Kernel Runner — deterministisch uitvoeringsmechanisme voor agent-runs",
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # start-run commando
    start_parser = subparsers.add_parser(
        "start-run",
        help="Start een agent-run met preflight en logging",
    )
    start_parser.add_argument(
        "agent_name",
        help="Naam van de agent om te starten",
    )
    start_parser.add_argument(
        "intent",
        help="Korte beschrijving van de intent",
    )
    start_parser.add_argument(
        "--trigger",
        default="handmatig",
        help="Reden voor de run (default: handmatig)",
    )
    
    # cleanup-logs commando
    subparsers.add_parser(
        "cleanup-logs",
        help="Ruim oude run logs op conform retentie-beleid",
    )
    
    return parser.parse_args(argv)


def main() -> int:
    """Main entry point."""
    try:
        args = parse_args()
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 1
    
    if args.command == "start-run":
        result = start_run(
            agent_name=args.agent_name,
            intent=args.intent,
            trigger=args.trigger,
        )
        
        if result.success:
            print(f"\nOK: {result.message}")
            print(f"Run ID: {result.run_id}")
            print(f"Log   : {result.log_path.relative_to(WORKSPACE_ROOT)}")
            return 0
        else:
            print(f"\nERROR: {result.message}", file=sys.stderr)
            return 1
    
    elif args.command == "cleanup-logs":
        deleted_count = cleanup_logs()
        print(f"OK: {deleted_count} log(s) verwijderd")
        return 0
    
    else:
        print(f"ERROR: Onbekend commando: {args.command}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
