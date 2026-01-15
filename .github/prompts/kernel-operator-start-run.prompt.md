# Kernel Operator Prompt — Start Run

## Rolbeschrijving

De kernel-operator start een kernel-run via kernelrunner.py met expliciete human-in-the-loop gatekeeping. Deze prompt definieert het contract voor het starten van een run met preflight checks en gebruikersbevestiging.

**VERPLICHT**: Lees governance/charters-agents/charter.kernel-operator.md voor volledige context, grenzen en werkwijze.

## Contract

### Input (Wat gaat erin)

**Verplichte parameters**:
- `state-bestand`: Pad naar state YAML bestand (relatief t.o.v. workspace root) (type: string, bijv. "state/standards.current.yaml")
- `run-trigger`: Reden voor deze kernel-run in één zin (type: string)

**Optionele parameters**:
- `check-only`: Alleen preflight checks uitvoeren, niet daadwerkelijk starten (type: boolean, default: false)
- `auto-confirm`: Automatisch bevestigen na preflight (alleen voor geautomatiseerde flows) (type: boolean, default: false)

### Output (Wat komt eruit)

Bij een geldige opdracht levert de kernel-operator altijd:
- Een samenvatting van de preflight check resultaten
- Bij succesvolle preflight: gebruikersbevestiging vraag (tenzij auto-confirm)
- Bij daadwerkelijke start: run-id van de gestarte kernel-run
- Locatie van run log voor observability

**Herkomstverantwoording**: VERPLICHT indien een rapportage-deliverable wordt geproduceerd. Voor interactieve start-operaties is HV niet vereist (operationele actie, geen documentair resultaat).

Output formaat (interactief):
```
Preflight OK:
- State bestand: <pad>
- Ping bestand: <status>
- Readability: <status>

Kernel-run starten met trigger: "<run-trigger>"?
[y/N]: _

Run gestart: <run-id>
Log: .kernel/runs/<run-id>.yaml
```

### Foutafhandeling

De kernel-operator:
- Stopt wanneer state-bestand niet bestaat of niet leesbaar is
- Stopt wanneer preflight checks falen (normatief-stelsel.ping ontbreekt, state ongeldig)
- Stopt wanneer gebruiker niet bevestigt (tenzij auto-confirm=true)
- Stopt wanneer kernelrunner.py zelf een fout teruggeeft
- Escaleert naar Moeder bij structurele workspace-problemen

## Werkwijze

Deze prompt definieert alleen de interface. Voor interne uitvoering, preflight-logica, en kernelrunner-integratie zie governance/charters-agents/charter.kernel-operator.md en scripts/kernel-operator.py.

**Governance**:
- Respecteert governance/gedragscode.md
- Volgt governance/workspace-doctrine.md
- Conform normatief-stelsel/globaal/agent-charter-normering.md
- Binnen de scope van governance/beleid-standard.md

---

Documentatie: Zie governance/charters-agents/charter.kernel-operator.md  
Runner: scripts/kernel-operator.py
