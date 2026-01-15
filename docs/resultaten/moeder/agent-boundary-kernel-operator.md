## Herkomstverantwoording

Dit agent boundary deliverable is vastgelegd door Moeder op basis van user input voor een nieuwe kernel-operator agent.

**Geraadpleegde bronnen**:
- User input "kernel-operator boundary" (ontvangen op 2026-01-15, exacte tijd niet beschikbaar)
- governance/charters-agents/ (bestaande agents gecontroleerd op overlap)
- governance/beleid-standard.md (scope validatie)

**Toelichting**:
De kernel-operator agent is een orchestrator/operator die de kernelrunner beheert met human-in-the-loop gatekeeping. Dit vult een gap tussen directe kernelrunner-aanroep en veilige, gecontroleerde uitvoering met observability. Geen overlap met bestaande agents gevonden.

---

agent-naam: kernel-operator
capability-boundary: Beheert en observeert kernelrunner-uitvoering met human-in-the-loop gatekeeping en observability
doel: Veilig kernel-runs starten, monitoren en rapporteren met expliciete gebruikersbevestiging
domein: Runner operations
