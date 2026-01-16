# Canon — Agent Eco-systeem Governance

**Versie**: 1.4.0  
**Status**: Active  
**Last Updated**: 2026-01-16

Canon is the canonical source for the architectural foundations of agent-based systems.

It defines the constitutional principles, doctrines, and normative structures from which agent ecosystems are designed, governed, and reasoned about.
Not as tooling, not as best practices, but as explicit foundations that make systems explainable, durable, and transferable.

Canon exists to support thinking before implementation.
It makes implicit assumptions explicit, separates fundamentals from contingencies, and provides a stable basis that remains valid as technologies change.

What lives here is not optional.
Everything else — agents, charters, workflows, implementations — is derived from this canon, never the other way around.

---

## Doel en Scope

Deze **canon**-repository is het governancecentrum van het **Agent Eco-systeem**. Het bevat:

- **Foundational documents**: Constitutie, principes, doctrines
- **Governance**: Beleid, normen, contracten
- **Agent definitions**: Charters, prompts, grenzen en rollen
- **Templates & structures**: Standaard structuren voor artefacten, fases, workflows

**Niet in deze repo**: Gegenereerde artefacten, project-specifieke code, implementaties (die horen in project-workspaces).

---

## Workspace-Structuur

```
canon/
├── grondslagen/          — Foundational principles & doctrines
│   ├── globaal/          — Universele governance & constitutie
│   └── value-streams/    — Value stream–specifieke doctrine
│
├── beleid/               — Workspace-specifieke regels & normen
│
├── charters-agents/      — Volledige agent charters met rollen & verantwoordelijkheden
│
├── docs/                 — Governance-documentatie & resultaten
│   ├── resultaten/       — Rapportages, escalaties, analyses
│   └── governance/       — Agent boundaries, handoff-documenten
│
├── templates/            — Herbruikbare documentatie templates
│
├── scripts/              — Utility scripts (pull, publish, etc.)
│
└── artefacten/           — (Extern) Gegenereerde content (niet gecommit)
    └── 0-governance/     — Generated governance docs
```

---

## Kernprincipes

### 1. Centraal Beheer
- Alle agent-definities, governance en normen blijven hier
- Eén bron van waarheid voor eco-systeem-ordening
- Expliciete grenzen en contracts per rol

### 2. Expliciete Governance
- Niet impliciet, niet best practices, maar geschreven principes
- Traceerbaarheid: wie, waarom, wanneer, wat
- Change management via versies en audit trail

### 3. Schone Projecten
- Project-repositories hebben geen `.github/prompts/` of `.github/agents/`
- Agents roepen vanuit **centraal** op, genereren in **lokaal**
- Artefacten: in projectspecifieke `artefacten/` folders, nooit in canon

---

## Navigatie naar Belangrijke Documenten

### Governance Fundamenteel
| Document | Doel |
|----------|------|
| [Grondslagen: Workspace-doctrine](grondslagen/globaal/workspace-doctrine.md) | Foundational principles en werking van deze workspace |
| [Grondslagen: Constitutie](grondslagen/globaal/constitutie.md) | Universele wetten en principes |
| [Beleid](beleid/beleid-standard.md) | In-scope/out-of-scope, naamgeving, norms |

### Value Stream IT Development
| Document | Doel |
|----------|------|
| [Value Stream Doctrine](grondslagen/value-streams/value-streams.md) | Globale waardestroom-architectuur |
| [IT Development Doctrine](grondslagen/value-streams/it-development/doctrine-it-development.md) | SAFe-gebaseerde doctrine voor IT fases A-G |
| [Phase Charter Templates](grondslagen/value-streams/it-development/charters-fases/) | Standard charter structure per fase |

### Agents & Rollen
| Agent | Charter | Grenzen |
|-------|---------|---------|
| **Moeder** (Factory, Ordening) | [Charter](charters-agents/charter-moeder.md) | [Boundaries](docs/resultaten/moeder/agent-boundary-*.md) |
| **Kernel-Operator** | [Charter](charters-agents/charter.kernel-operator.md) | [Boundaries](docs/resultaten/moeder/agent-boundary-kernel-operator.md) |
| **Canon-Curator** | [Charter](charters-agents/charter.canon-curator.md) | [Escalaties](docs/resultaten/canon-curator/escalatie-*.md) |
| **Python-Expert** | [Charter](charters-agents/charter.python-expert.md) | [Boundaries](docs/resultaten/moeder/agent-boundary-python-expert.md) |
| **Constitutioneel Auteur** | [Charter](charters-agents/charter.constitutioneel-auteur.md) | [Boundaries](docs/resultaten/moeder/agent-boundary-constitutioneel-auteur.md) |

---

## Wijzigingen & Versiebeheer

### Governance Documents
- **Constitutie**: Wijzigingen via review & vote (fundamenteel)
- **Doctrine**: Via value stream owner, met audit trail
- **Beleid**: Wijzigingen met versienummer en change log

### Agent Charters
- Nieuwe agents: Via **Moeder** (create workflow)
- Wijzigingen: Via **Canon-Curator** (review) en **Constitutioneel Auteur** (wording)
- Alle wijzigingen: Gedocumenteerd in charter-versie en change log

---

## Externe Repositories & Relaties

| Repository | Rol | Beheer |
|------------|-----|--------|
| **agent-capabilities** | PowerShell scripts, artefact-tooling | Central tooling |
| **[hans-blok/*]** repos | External standard libraries | Pull via `scripts/pull_repo.py` |
| **project-workspaces** | Locale applicatie-repos (artefacten, code) | Project-owner |

---

## Taalgebruik & Conventies

- **Documentatie**: Nederlands (B1-begrijpelijk)
- **Code/identifiers**: Engels (internationale standaard)
- **Technische termen**: Engels waar geen gangbare NL-equivalent
- **Versioning**: `major.minor.patch` semantic versioning
- **Naamgeving**: Zie [beleid/](beleid/beleid-standard.md) voor volledige conventie

---

## Snel Starten

### Repo Clonen
```powershell
git clone https://github.com/hans-blok/canon.git C:\git\canon
cd C:\git\canon
```

### Externe Repos Pullen
```powershell
# Via utility script
python scripts/pull_repo.py agent-services

# Of rechtstreeks
git clone https://github.com/hans-blok/agent-services.git external/agent-services
```

### Editor & Terminal Instellingen
```powershell
# .vscode/settings.json bevat workspace color scheme
# Light theme + white editor/terminal
```

---

## Contact & Eigenaarschap

**Governance Owner**: Architecture & AI Enablement  
**Agent Factory**: [Moeder](charters-agents/charter-moeder.md)  
**Quality Gate**: [Canon-Curator](charters-agents/charter.canon-curator.md)  
**Last Updated**: 2026-01-16 | **Version**: 1.4.0
