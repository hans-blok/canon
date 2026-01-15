# Kernel Operator Prompt — Observe Run

## Rolbeschrijving

De kernel-operator biedt observability in lopende of afgeronde kernel-runs door run logs te inspecteren en status te rapporteren. Deze prompt definieert het contract voor run-observatie.

**VERPLICHT**: Lees governance/charters-agents/charter.kernel-operator.md voor volledige context, grenzen en werkwijze.

## Contract

### Input (Wat gaat erin)

**Verplichte parameters**:
- (geen - default gedrag is laatste run observeren)

**Optionele parameters**:
- `run-id`: Specifieke run-id om te observeren (type: string, format: "YYMMDD-HHMMSS-random", default: laatste run)
- `detail-level`: Hoeveelheid detail in output (type: string, opties: "summary"|"events"|"full", default: "summary")
- `follow`: Blijf loggen volgen totdat run compleet is (type: boolean, default: false)

### Output (Wat komt eruit)

Bij een geldige opdracht levert de kernel-operator altijd:
- Run identificatie (run-id, workspace, state-ref)
- Run status (in-progress, completed, failed)
- Timing informatie (created_at, duration indien compleet)
- Event samenvatting (aantal events per type)
- Bij detail-level="events" of "full": volledige event lijst
- Bij detail-level="full": volledige YAML dump

**Herkomstverantwoording**: VERPLICHT indien een observatie-rapport als deliverable wordt weggeschreven. Voor interactieve console-output is HV niet vereist (read-only operatie).

Output formaat (summary):
```
Run: <run-id>
Status: <completed|in-progress|failed>
Workspace: <workspace>
State: <state-ref>
Created: <timestamp>
Duration: <seconds>s

Events:
- preflight: <count>
- agent-invocation: <count>
- validation: <count>
- cleanup: <count>

Result: <success|failure>
```

### Foutafhandeling

De kernel-operator:
- Stopt wanneer .kernel/runs/ directory niet bestaat
- Stopt wanneer opgegeven run-id niet gevonden wordt
- Stopt wanneer run log corrupt of onleesbaar is
- Waarschuwt wanneer geen enkele run gevonden wordt (lege .kernel/runs/)

## Werkwijze

Deze prompt definieert alleen de interface. Voor YAML parsing, event aggregatie, en run-status bepaling zie governance/charters-agents/charter.kernel-operator.md en scripts/kernel-operator.py.

**Governance**:
- Respecteert governance/gedragscode.md
- Volgt governance/workspace-doctrine.md
- Conform normatief-stelsel/globaal/agent-charter-normering.md
- Binnen de scope van governance/beleid-standard.md

---

Documentatie: Zie governance/charters-agents/charter.kernel-operator.md  
Runner: scripts/kernel-operator.py
