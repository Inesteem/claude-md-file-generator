# claude-mdfile-generator

[![CI](https://github.com/yourusername/claude-mdfile-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/claude-mdfile-generator/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Stop writing `CLAUDE.md` files from scratch. Pick from 38 reusable modules — generic best practices and agent-filled project-specific templates — preview the result, and generate a tailored `CLAUDE.md` in seconds.

**Static modules** give universal rules ("use conventional commits", "write tests first"). **Template modules** produce `<Fill ...>` placeholders that an agent analyzes your codebase to fill in ("this project uses pytest, tests in `tests/`, 90% coverage required").

## Quick start

```bash
# Install from GitHub
pip install git+https://github.com/yourusername/claude-mdfile-generator.git

# Bootstrap your modules directory with all 42 bundled modules
claude-md --init

# Or just use the bundled modules directly (read-only)
claude-md --bundled
```

## Installation

### From GitHub

```bash
pip install git+https://github.com/yourusername/claude-mdfile-generator.git
```

### From source (for development)

```bash
git clone https://github.com/yourusername/claude-mdfile-generator.git
cd claude-mdfile-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

After installation, the `claude-md` command is available in the Python environment.

### Requirements

- Python 3.11+

Runtime dependencies:

| Package | Version | Purpose |
|---|---|---|
| `pyyaml` | >=6.0 | YAML frontmatter parsing in module files |
| `questionary` | >=2.0 | Interactive terminal prompts (checkbox, select, text) |
| `rich` | >=13.0 | Pretty terminal output (tables, panels, markdown preview) |

Dev dependencies:

| Package | Version | Purpose |
|---|---|---|
| `pytest` | >=8.0 | Test framework |
| `ruff` | >=0.8 | Linter and formatter |
| `pyright` | >=1.1 | Type checker |

## Usage

### Interactive TUI

```bash
claude-md
```

The TUI lets you:
1. **Browse** all available modules in a table
2. **Select** the modules you want via checkbox
3. **Preview** the assembled `CLAUDE.md` in the terminal
4. **Write** it to a file (default: `CLAUDE.md`)
5. **Create, edit, and delete** modules through the menu

### CLI flags

| Flag | Description |
|---|---|
| `--modules-dir PATH` | Use a custom modules directory |
| `--bundled` | Use the 42 modules shipped with the package (read-only) |
| `--init` | Copy bundled modules to your modules directory (won't overwrite existing) |
| `--init-skills DIR` | Copy the bundled `fill` skill to a directory (e.g. `~/.claude/skills`) |

### Environment variable

```bash
export CLAUDE_MD_MODULES_DIR=~/my-modules
claude-md
```

### Modules directory

By default, modules are stored in `~/.config/claude-mdfile-generator/modules/`.

To get started with the bundled modules:

```bash
# Copy all 42 bundled modules to your config dir for customization
claude-md --init

# Or copy to a project-local directory
claude-md --init --modules-dir ./my-project-modules
```

## How it works

### Module concept

Modules are the building blocks of a `CLAUDE.md` file. There are two types:

- **static** — Generic best-practice advice (e.g. "use conventional commits", "write tests before implementation"). Included as-is in the generated file. Same content for every project.
- **template** — A `<Fill SectionName>` placeholder block with instructions for an agent. The agent analyzes the target project's codebase and replaces the placeholder with real, project-specific content.

Most topics ship as a **static + template pair**. The static module provides universal rules; the companion template captures what's actually true for this specific project:

| Example | Static module | Companion template |
|---|---|---|
| Git | "Use conventional commits, keep commits atomic" | "This project uses Angular-style commits, squash merges to `main`" |
| Testing | "Write tests before implementation, prefer real implementations over mocks" | "Uses pytest, tests in `tests/`, 90% coverage required, uses `tmp_path` fixtures" |
| Database | "Use snake_case, write idempotent migrations" | "PostgreSQL + SQLAlchemy + Alembic, migrations in `alembic/versions/`" |

### Module storage format

Each module is a Markdown file with YAML frontmatter:

```markdown
---
name: Module Name
type: static
tags: [relevant, tags]
order: 20
description: One-line description
---
## Module Name

- Guideline one
- Guideline two
```

Template modules use `<Fill ...>` tags instead of markdown content:

```markdown
---
name: Module Name
type: template
tags: [relevant, tags]
order: 20
description: One-line description (agent-filled)
---
<Fill Module Name>
Instructions for the agent:
- What to look for in the codebase
- What to document

Ask the user:
- Questions the agent cannot answer from code alone
</Fill Module Name>
```

### Frontmatter fields

| Field | Required | Notes |
|---|---|---|
| `name` | yes | Display name shown in the TUI |
| `type` | yes | `static` or `template` |
| `tags` | no | List of strings for filtering |
| `order` | no | Integer; lower values appear first (default 50) |
| `description` | no | One-line summary shown in the TUI table |

### Creating custom modules

- **Via TUI:** Select "Create new module" from the main menu
- **Manually:** Create a `.md` file in your modules directory following the format above

## Bundled modules

The package ships with **42 modules** (22 template, 20 static) organized by topic:

### Project overview (templates)

| Module | Order | Description |
|---|---|---|
| Project Summary | 1 | Project name, purpose, tech stack, entry points |
| Project Context | 2 | Setup commands, test/lint commands, env requirements |
| Glossary | 3 | Project-specific terms and jargon |
| Architecture | 5 | Directory structure, components, data flows, state |
| Key Conventions | 6 | Error handling, logging, naming, testing conventions |

### Workflow (static + template pairs)

| Static module | Companion template | What the template adds |
|---|---|---|
| Investigation First (8) | — | Generic; no project-specific details needed |
| Forbidden Actions (9) | Forbidden Zones (9) | Generated files, lock files, team-owned boundaries |
| Git Rules (10) | Git Configuration (10) | Actual commit format, branch naming, merge strategy |
| Pull Requests (12) | PR Configuration (12) | PR template, CODEOWNERS, labels, required checks |
| Testing (15) | Testing Configuration (15) | Framework, directory structure, coverage, fixtures |

### Code quality (static + template pairs)

| Static module | Companion template | What the template adds |
|---|---|---|
| Code Style (20) | Code Style (21) | Naming conventions, import ordering, project patterns |
| Code Quality (22) | — | Generic; tooling details in separate templates below |
| — | Linter Configuration (23) | Which linter, commands, config, notable rules |
| — | Type Checker Configuration (23) | Which type checker, commands, strictness |
| — | Formatter Configuration (24) | Which formatter, commands, settings |
| Documentation (25) | Documentation Strategy (25) | Doc inventory, update triggers, external docs |

### Security and operations (static + template pairs)

| Static module | Companion template | What the template adds |
|---|---|---|
| Security (26) | — | Generic; no project-specific details needed |
| — | CI Pipeline (27) | CI system, checks, matrix, required gates |
| — | Pre-commit Hooks (27) | Hook framework, hooks in order, install command |
| Error Handling (28) | Error Patterns (29) | Custom error types, propagation, retry policies |
| Dependency Management (30) | Dependency Configuration (30) | Package manager, lock files, banned packages |
| Changelog Conventions (33) | Changelog Configuration (33) | Changelog format, versioning, release process |
| API Interaction (34) | API Configuration (34) | Specific APIs, auth patterns, rate limits |
| Multi-Agent Workflow (35) | — | Generic; no project-specific details needed |
| Slash Commands (36) | — | Claude Code meta-advice; no project-specific template |
| TODO Conventions (37) | TODO Inventory (37) | Scans for TODOs/FIXMEs, surfaces technical debt |
| Database Conventions (38) | Database Configuration (38) | Engine, ORM, migration tool, connection setup |

### Platform and output (static only)

| Static module | Order | Description |
|---|---|---|
| Cross-Platform Compatibility | 40 | Path abstractions, encoding, line endings |
| Performance | 42 | Algorithm choices, batching, caching, profiling |
| Output Formatting | 45 | Markdown conventions, conciseness, emoji policy |

## Agent skill for template modules

Template modules produce `<Fill SectionName>...</Fill SectionName>` placeholder blocks in the generated `CLAUDE.md`. A single agent skill — `skills/fill.md` — handles all of them.

### Installing the skill

```bash
claude-md --init-skills ~/.claude/skills
```

This copies `fill.md` to your global Claude Code skills directory.

### What the skill does

The `fill` skill instructs an agent to:

1. Scan the `CLAUDE.md` for `<Fill ...>` blocks
2. For each block, analyze the target project's codebase
3. Replace the placeholder with real, verified content
4. Ask the user when information cannot be derived from code alone
5. Mark unresolvable gaps with `<!-- TODO -->` comments

### Supported tags

| Tag | Agent action | Asks user? |
|---|---|---|
| `<Fill Project Summary>` | Reads README, entry points, dep files | No |
| `<Fill Project Context>` | Extracts setup, test, lint commands | No |
| `<Fill Glossary>` | Scans for domain-specific terms | No |
| `<Fill Architecture>` | Maps directory structure, components, data flows | No |
| `<Fill Key Conventions>` | Analyzes error handling, logging, naming patterns | No |
| `<Fill Testing Configuration>` | Identifies test framework, runs suite | Yes |
| `<Fill Forbidden Zones>` | Finds generated/locked/team-owned files | Yes |
| `<Fill Error Patterns>` | Traces error types and propagation | Yes |
| `<Fill Git Configuration>` | Inspects recent commits and branches | Yes |
| `<Fill PR Configuration>` | Finds PR templates, CODEOWNERS | Yes |
| `<Fill Code Style>` | Samples source files for conventions | No |
| `<Fill Linter Configuration>` | Identifies linter, runs it | No |
| `<Fill Type Checker Configuration>` | Identifies type checker, runs it | No |
| `<Fill Formatter Configuration>` | Identifies formatter, runs check mode | No |
| `<Fill Documentation Strategy>` | Inventories docs and update triggers | Yes |
| `<Fill CI Pipeline>` | Reads CI config files | No |
| `<Fill Pre-commit Hooks>` | Reads hook config | No |
| `<Fill Dependency Configuration>` | Locates package manager, lock files | Yes |
| `<Fill Database Configuration>` | Identifies engine, ORM, migrations | Yes |
| `<Fill API Configuration>` | Finds API clients, auth patterns | Yes |
| `<Fill Changelog Configuration>` | Identifies changelog format, versioning, release process | Yes |
| `<Fill TODO Inventory>` | Greps for TODO/FIXME/HACK, categorizes and surfaces critical items | Yes |

### Final review pass

After filling all templates, the skill instructs the agent to do a coherence review of the entire file:

1. **Duplications** — finds rules repeated across static + filled sections, keeps the more specific version
2. **Contradictions** — catches where generic advice conflicts with the project's actual setup
3. **Irrelevant sections** — recommends removing static modules that don't apply (e.g. Database Conventions when there's no database)
4. **Restructuring** — suggests merging overly granular sections or reordering for better flow

### Workflow

1. **Generate** a `CLAUDE.md` with the TUI, selecting the modules you want
2. **Run the fill skill** by pointing an agent at the target project with the skill prompt
3. The agent reads the codebase, fills in templates, and asks you about anything it can't determine from code alone
4. The agent does a **final review pass** checking for duplications, contradictions, and irrelevant sections
5. **Review** the agent's suggestions and the filled-in `CLAUDE.md`, then commit it to the project

## Development

### Running tests

```bash
pytest
```

### Linting and formatting

```bash
ruff check src/ tests/       # lint
ruff format src/ tests/       # format
```

### Type checking

```bash
pyright src/
```

### Project structure

```
claude-mdfile-generator/
  src/claude_mdfile_generator/
    models.py          # Module dataclass and ModuleType enum
    storage.py         # CRUD for module files (YAML frontmatter markdown)
    generator.py       # Compose selected modules into a claude.md string
    tui.py             # Interactive TUI (questionary + rich)
    cli.py             # CLI entry point with --init, --bundled, --init-skills
    bundled.py         # Access bundled modules/skills shipped with the package
    bundled_modules/   # 38 bundled module files (embedded in pip package)
    bundled_skills/    # fill.md skill (embedded in pip package)
  tests/               # 65 tests (models, storage, generator, TUI, CLI, bundled)
  modules/             # Source of truth for bundled modules (development copy)
  skills/              # Source of truth for bundled skills (development copy)
```

## License

MIT — see [LICENSE](LICENSE) for details.
