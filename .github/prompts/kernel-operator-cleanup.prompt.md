# Kernel Operator Prompt — Cleanup

## Rolbeschrijving

De kernel-operator voert cleanup uit van oude kernel-run logs volgens het retentiebeleid uit de runner doctrine. Deze prompt definieert het contract voor log cleanup met optionele dry-run modus.

**VERPLICHT**: Lees governance/charters-agents/charter.kernel-operator.md voor volledige context, grenzen en werkwijze.

## Contract

### Input (Wat gaat erin)

**Verplichte parameters**:
- (geen - default retentiebeleid uit doctrine wordt gebruikt)

**Optionele parameters**:
- `dry-run`: Alleen rapporteren wat verwijderd zou worden, niet daadwerkelijk verwijderen (type: boolean, default: false)
- `retention-runs`: Maximaal aantal runs te behouden (type: integer, default: 20 uit doctrine)
- `retention-days`: Maximaal aantal dagen succesvollen te behouden (type: integer, default: 7 uit doctrine)
- `retention-days-failed`: Maximaal aantal dagen failures te behouden (type: integer, default: 30 uit doctrine)

### Output (Wat komt eruit)

Bij een geldige opdracht levert de kernel-operator altijd:
- Aantal runs gevonden in .kernel/runs/
- Aantal runs die voldoen aan retentiecriteria (te verwijderen)
- Lijst van run-ids die verwijderd worden/zouden worden
- Bevestiging van verwijdering (tenzij dry-run)
- Aantal behouden runs na cleanup

**Herkomstverantwoording**: VERPLICHT indien een cleanup-rapport als deliverable wordt weggeschreven. Voor interactieve cleanup-operaties is HV niet vereist (operationele actie).

Output formaat:
```
Cleanup analyse:
- Totaal runs: <count>
- Te verwijderen (>20 runs): <count>
- Te verwijderen (>7 dagen, success): <count>
- Te verwijderen (>30 dagen, failed): <count>

Verwijderen:
- <run-id-1> (<created>, <result>)
- <run-id-2> (<created>, <result>)
...

[Dry-run: geen bestanden verwijderd]
of
[Verwijderd: <count> runs]
[Behouden: <count> runs]
```

### Foutafhandeling

De kernel-operator:
- Stopt wanneer .kernel/runs/ directory niet bestaat
- Stopt wanneer run logs niet leesbaar zijn (YAML parse errors)
- Waarschuwt wanneer geen runs voldoen aan retentiecriteria (alles is recent)
- Stopt bij bestandssysteem errors tijdens verwijdering (tenzij dry-run)

## Werkwijze

Deze prompt definieert alleen de interface. Voor retentielogica, YAML parsing, en bestandsverwijdering zie governance/charters-agents/charter.kernel-operator.md en scripts/kernel-operator.py.

**Governance**:
- Respecteert governance/gedragscode.md
- Volgt governance/workspace-doctrine.md
- Conform normatief-stelsel/globaal/agent-charter-normering.md
- Binnen de scope van governance/beleid-standard.md

---

Documentatie: Zie governance/charters-agents/charter.kernel-operator.md  
Runner: scripts/kernel-operator.py
