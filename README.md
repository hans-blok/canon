# Standards — Agent Eco-systeem Governance

**Versie**: 1.3.0  
**Status**: Active  
**Last Updated**: 2025-12-30

---

## Overzicht

De **standards** repository is het governancecentrum van het **Agent Eco-systeem**. Het bevat alle charters, templates, beleid en kwaliteitseisen die de basis vormen voor consistente en gestructureerde AI-agent-ontwikkeling.

---

## Agent Eco-systeem Architectuur

Het ecosysteem wordt beschreven met **C4 (Context, Containers, Components, Code)** en gevisualiseerd met Structurizr.

### Structurizr Docker Container

Start de Structurizr Lite viewer met het volgende commando:

```bash
docker run --rm -it -p 8080:8080 -v C:\gitrepo\standard\artefacten:/usr/local/structurizr structurizr/lite
```

Open vervolgens een browser op [http://localhost:8080](http://localhost:8080) om de architectuur te bekijken.

### Architectuurdiagram

```
┌─────────────────────────────────────────────────────────────┐
│  Agent Eco-systeem (Centraal)                               │
│  ├── standards/          — Governance, charters, templates  │
│  ├── agent-capabilities/ — PowerShell scripts, tooling      │
│  └── [andere centrale repos]                                │
└─────────────────────────────────────────────────────────────┘
                          ↓ aanroepen
┌─────────────────────────────────────────────────────────────┐
│  Project-Workspaces (Lokaal, "schoon")                      │
│  └── /artefacten/        — Alle gegenereerde artefacten     │
│      ├── a.trigger/                                          │
│      ├── b.architectuur/                                     │
│      ├── c.specificatie/                                     │
│      └── ...                                                 │
│  GEEN .github/agents/, GEEN .github/prompts/                │
└─────────────────────────────────────────────────────────────┘
```

### Kernprincipes

1. **Centraal Beheer**
   - Alle agents, charters en governance blijven in centrale repositories
   - Eén bron van waarheid voor agent-definities

2. **Schone Project-Workspaces**
   - Project-repositories bevatten GEEN `.github/agents/` of `.github/prompts/`
   - Alleen gegenereerde artefacten en applicatiecode

3. **Scheiding van Verantwoordelijkheden**
   - Agent-definitie: centraal (standards)
   - Artefact-generatie: lokaal (project-workspaces)

---

## Repository Structuur

```
standards/
├── governance/           — Constitutie, beleid, frameworks
│   ├── constitutie.md
│   ├── beleid-standard.md
│   ├── delivery-framework.md
│   └── wetten-it-ontwikkeling.md
│
├── charters.agents/      — Volledige agent-charters
│   ├── governance/       — Meta-agents (Moeder, Logos, Charter-schrijver)
│   ├── b.architectuur/   — Fase B agents
│   ├── c.specificatie/   — Fase C agents
│   ├── d.ontwerp/        — Fase D agents
│   └── u.utility/        — Utility agents
│
├── charters.fases/       — Fase-specifieke charters (SAFe)
│   └── std.fase.charter.c.specificatie.md
│
├── templates/            — Herbruikbare templates
│   ├── agent.charter.template.md
│   └── phase.charter.template.md
│
├── desc-agents/          — Beknopte agent-beschrijvingen
│   ├── moeder-agent.md
│   └── charter-writer-agent.md
│
├── agent-eco-systeem/    — Eco-systeem documentatie
│   ├── architectuur-agent-eco-systeem.md
│   └── stappenplan-opbouw-ecosysteem.md
│
└── designs/              — Ontwerpen (datamodellen, etc.)
    └── datamodellen/
```

---

## Belangrijke Documenten

### Governance
- **[Constitutie](governance/constitutie.md)** — Fundamentele principes en wetten
- **[Beleid](artefacten/0-governance/beleid-standard.md)** — Workspace-specifieke regels (scope & out of scope)
- **[Delivery Framework](governance/delivery-framework.md)** — SAFe development value stream
- **[Wetten IT Ontwikkeling](governance/wetten-it-ontwikkeling.md)** — Universele ontwikkelprincipes

### Agent Charters
- **[Moeder Agent](charters.agents/governance/std.agent.charter.moeder.md)** — Agent factory en landschap-beheer
- **[Logos Agent](charters.agents/governance/std.agent.charter.logos.md)** — Kwaliteitsbewaker
- **[Charter Schrijver](charters.agents/governance/std.agent.charter.charter-schrijver.md)** — Charter-documentatie specialist

### Templates
- **[Agent Charter Template](templates/agent.charter.template.md)** — Standaard agent charter structuur
- **[Phase Charter Template](templates/phase.charter.template.md)** — Standaard fase charter structuur

---

## Hoe Agents Werken

### 1. Agent-Aanroep vanuit Project-Workspace

```powershell
# Vanuit een project-workspace (bijv. C:\projects\myapp)
# Agents worden aangeroepen vanuit centrale repository

# Agent genereert artefacten in project-workspace
# Folder-structuur wordt automatisch aangemaakt indien nodig
```

### 2. Artefact-Generatie

Agents genereren artefacten in de **artefacten** folder conform het Delivery Framework:

```
Project-Workspace/
└── artefacten/
    ├── a.trigger/          — Business cases, initiaties
    ├── b.architectuur/     — ADR's, architectuurpatronen
    ├── c.specificatie/     — Requirements, features, datamodellen
    ├── d.ontwerp/          — API designs, technisch ontwerp
    ├── e.bouw/             — Code, scripts, implementatie
    ├── f.validatie/        — Test rapporten, validatie
    ├── g.deployment/       — Release notes, deployment scripts
    └── u.utility/          — Ondersteunende tools en utilities
```

### 3. PowerShell Scripts

Alle PowerShell scripts voor artefact-creatie bevinden zich in de **agent-capabilities** repository.

---

## Development Value Stream (SAFe)

Alle agents (behalve Logos) opereren binnen het SAFe framework:

```
A. Trigger → B. Architectuur → C. Specificatie → D. Ontwerp → 
E. Bouw → F. Validatie → G. Deployment
                  ↕
              U. Utility
```

Zie [Delivery Framework](governance/delivery-framework.md) voor details.

---

## Agent-Ontwikkeling

### Nieuwe Agent Creëren

Nieuwe agents worden gecreëerd door de **Moeder Agent**:

1. Moeder Agent analyseert de behoefte
2. Bepaalt fase-positie (A-G of U)
3. Creëert 4 verplichte bestanden:
   - Agent-file: `.github/agents/std.<fase>.<naam>.agent.md`
   - Prompt-file: `.github/prompts/std.<fase>.<naam>.prompt.md`
   - Charter: `charters.agents/<fase>/std.agent.charter.<naam>.md`
   - Beschrijving: `desc-agents/<naam>-agent.md`

### Charter Kwaliteitseisen

Elk agent-charter moet voldoen aan:
- Volledigheid (alle 10 secties ingevuld)
- Consistentie (uniforme terminologie)
- Traceerbaarheid (beslissingen herleidbaar)
- Helderheid (begrijpelijk op B1-niveau)
- Evolutie (versiebeheer en change logs)

---

## Taalgebruik

**Alle documentatie gebeurt in het Nederlands** (conform [beleid-standard.md](artefacten/0-governance/beleid-standard.md)):
- Documentatie: Nederlands
- Technische termen: Engels waar geen gangbare Nederlandse vertaling bestaat
- Code en identifiers: Engels (internationale conventies)
- Agent-communicatie: Nederlands op B1-niveau

---

## Wijzigingsproces

### Governance-documenten
- **Constitutie**: Alleen inhoudelijke wijzigingen door mens
- **Beleid**: Wijzigingen via expliciet updateproces en versiebeheer
- **Frameworks**: Wijzigingen na review door architect

### Agent-charters
- Nieuwe charters via Moeder Agent en Charter Writer Agent
- Wijzigingen via gecontroleerd proces
- Alle wijzigingen gedocumenteerd in Change Log

---

## Relatie tot Andere Repositories

### agent-capabilities
Bevat PowerShell scripts en tooling voor:
- Artefact-generatie
- Format-conversie
- Data-transformatie
- Proces-automatisering

### Project-Workspaces
Lokale repositories waar:
- Agents artefacten genereren
- Applicatiecode wordt ontwikkeld
- GEEN agents of prompts worden opgeslagen

---

## Contact en Eigenaarschap

**Eigenaar**: Architecture & AI Enablement  
**Governance**: Conform `governance/constitutie.md`  
**Agent Factory**: Moeder Agent (`charters.agents/governance/std.agent.charter.moeder.md`)

---

## Versiegeschiedenis

| Datum | Versie | Wijziging |
|------|--------|-----------|
| 2025-12-30 | 1.2.0 | Initiële README — Agent Eco-systeem architectuur, schone project-workspaces, centrale agent-beheer || 2025-12-30 | 1.3.0 | Gewijzigd: Folder-structuur naar artefacten/* met naamgevingsconventie `<fase letter lowercase>.<fase naam>` |
---

**Voor gedetailleerde governance-regels, zie [beleid-standard.md](artefacten/0-governance/beleid-standard.md)**
