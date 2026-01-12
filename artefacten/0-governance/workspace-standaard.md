# Workspace Standaard voor Document-Repositories

**Type**: Normerend Structuurdocument  
**Versie**: 1.0.0  
**Status**: Actief  
**Datum**: 2026-01-12  
**Eigenaar**: Architecture & AI Enablement

---

## 1. Doel en Scope

Deze standaard normeert de **folderstructuur en organisatie van document-repositories**. Doel is om consistentie, vindbaarheid en professionaliteit te borgen in alle repositories die primair uit documentatie bestaan.

Deze standaard is van toepassing op repositories die:
- hoofdzakelijk Markdown-documentatie, policies of procedures bevatten;
- geen applicatiecode of SAFe-fase-artefacten beheren;
- functioneren als knowledge base, governance- of policy-repository.

Voor repositories die onderdeel zijn van het centrale Agent Eco-systeem en SAFe-fase-artefacten beheren, geldt primair:
- artefacten/0-governance/workspace-architectuur.md  
Deze **Workspace Standaard** specialiseert die architectuur voor "document-only" repositories. Bij conflict prevaleert workspace-architectuur.md.

---

## 2. Verplichte Root-structuur voor Document-Repositories

Elke document-repository **moet** minimaal de volgende structuur hanteren:

```text
/docs                    # Alle inhoudelijke documentatie
/governance              # Gedragscode, policies, procedures, rolbeschrijvingen
/templates               # Document-templates en voorbeelden
/temp                    # Tijdelijke context en voorstellen (niet in git)
/.github                 # GitHub-configuratie (workflows, prompts)
README.md                # Repository-overzicht en getting started
.gitignore               # Git ignore patterns
```

### 2.1 `/docs` — Inhoudelijke Documentatie

**Doel**: Alle inhoudelijke documentatie die het primaire doel van de repository vormt.

Aanbevolen structuur:

```text
/docs
  /resultaten/             # (Optioneel) Agent-output per agent
    /{agent-naam}/
  /procedures/             # Algemene procedures
  /policies/               # Policies
  /guidelines/             # Richtlijnen en best practices
  /references/             # Naslagwerk en definities
```

**Richtlijnen**:
- Documenteer agent-output (indien aanwezig) onder `/docs/resultaten/{agent-naam}/`.
- Gebruik beschrijvende bestandsnamen in het Nederlands.
- Beperk de mapdiepte tot maximaal drie niveaus.

### 2.2 `/governance` — Repo-specifieke Governance

**Doel**: Regels, normen en structuur van de specifieke repository.

Verplichte inhoud:

```text
/governance
  gedragscode.md        # Of verwijzing naar centrale gedragscode
  beleid.md             # Repo-specifiek beleid met scope en niet-in-scope
```

Aanbevolen aanvullingen:
- `/rolbeschrijvingen/` – rolbeschrijvingen voor belangrijke rollen of agents;
- `CONTRIBUTING.md` – bijdragen-richtlijnen;
- `CODEOWNERS` – verantwoordelijken per domein.

`beleid.md` beschrijft minimaal: context, scope, niet-in-scope en relatie tot centrale governance (constitutie, gedragscode).

### 2.3 `/templates` — Templates

**Doel**: Herbruikbare sjablonen voor nieuwe documenten.

Voorbeelden:

```text
/templates
  document-template.md
  procedure-template.md
  policy-template.md
  meeting-notes-template.md
```

Richtlijnen:
- Gebruik placeholders tussen `< >` voor invulvelden.
- Voeg bovenaan elk template een korte instructiesectie toe.

### 2.4 `/.github` — GitHub-configuratie

**Doel**: GitHub-specifieke configuratie en (optioneel) agent-prompts.

Aanbevolen structuur:

```text
/.github
  /prompts/             # Prompt-bestanden (*.prompt.md)
  /workflows/           # GitHub Actions (optioneel)
  ISSUE_TEMPLATE/       # Issue-templates (optioneel)
  PULL_REQUEST_TEMPLATE.md  # PR-template (optioneel)
```

Richtlijnen:
- Houd `.github` vrij van inhoudelijke documenten; het is puur technisch.
- Prompt-bestanden eindigen op `.prompt.md` en volgen het contract-formaat (rol, input, output, foutafhandeling).

### 2.5 `/temp` — Tijdelijke Context (Niet in Git)

**Doel**: Lokale context, voorstellen, plannen en werk-in-uitvoering.

Typische inhoud:

```text
/temp
  context.md             # Workspace-context en scope-beschrijving
  {onderwerp}-plan.md    # Plannen (ontwerp, migratie, opschoning)
  notities.md            # Werknotities en ideeën
```

Richtlijnen:
- De map `/temp/` wordt expliciet genegeerd in `.gitignore`.
- Plannen worden in Markdown vastgelegd met bestandsnaam `{onderwerp}-plan.md`.
- Agents die om een plan worden gevraagd, schrijven dit plan als Markdown-bestand in `/temp/` (zie ook constitutie.md, Artikel 4).

### 2.6 Verplichte Root-bestanden

**README.md**
- Beschrijft doel, structuur en gebruik van de repository.
- Bevat ten minste: titel + korte beschrijving, structuur-overzicht, gebruik, bijdragen (indien relevant) en licentie (indien van toepassing).

**.gitignore**
- Neemt minimaal op:
  - `temp/`  (tijdelijke context)
  - editor-folders (`.vscode/`, `.idea/`)
  - OS-bestanden (`.DS_Store`, `Thumbs.db`)

---

## 3. Naamgevings- en Markdown-conventies

Voor document-repositories gelden dezelfde basisconventies als gedefinieerd in:
- artefacten/0-governance/workspace-architectuur.md, secties **5.1 Naamgevingsconventies** en **5.3 Markdown Standaarden**.

Samengevat:
- Folders en bestandsnamen in lowercase met `-` tussen woorden;
- Beschrijvende namen die de inhoud duidelijk maken;
- Documenten in Markdown met één H1-titel en logische heading-hiërarchie.

Dubbele uitwerking wordt hier bewust vermeden; wijzigingen in generieke conventies gebeuren in workspace-architectuur.md.

---

## 4. Validatie voor Document-Repositories

Gebruik deze checklist bij het opzetten of reviewen van een document-repository:

- [ ] Verplichte root-structuur aanwezig (`/docs`, `/governance`, `/templates`, `/.github`, `README.md`, `.gitignore`).
- [ ] `/temp/` bestaat lokaal en staat in `.gitignore`.
- [ ] `governance/beleid.md` beschrijft scope en niet-in-scope en verwijst naar centrale governance.
- [ ] Structuur onder `/docs/` is niet dieper dan drie niveaus.
- [ ] Bestands- en foldernamen volgen de naamgevingsconventies uit workspace-architectuur.md.
- [ ] Markdown-documenten volgen de Markdown-standaarden uit workspace-architectuur.md.

---

## 5. Relatie tot Andere Documenten

Deze Workspace Standaard voor Document-Repositories staat in relatie tot:

- **Constitutie** — artefacten/0-governance/constitutie.md  
  Bepaalt hiërarchie en basisregels.

- **Workspace Architectuur** — artefacten/0-governance/workspace-architectuur.md  
  Definieert de generieke workspace-structuur voor het Agent Eco-systeem.

- **Gedragscode** — artefacten/0-governance/gedragscode.md  
  Bepaalt professioneel gedrag, taalgebruik en samenwerking.

Bij tegenstrijdigheden prevaleert de Constitutie, vervolgens workspace-architectuur.md. Deze standaard mag geen conflicten introduceren, maar specialiseert de toepassing voor document-only repositories.

---

## 6. Wijzigingslog

| Datum       | Versie | Wijziging                                 | Auteur                |
|------------|--------|-------------------------------------------|-----------------------|
| 2026-01-12 | 1.0.0  | Initiële versie op basis van temp-variant | Charter Schrijver Agent |
