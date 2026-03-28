# claude-mdfile-generator

A lightweight TUI for composing `CLAUDE.md` files from a library of reusable modules. Pick the modules that apply to your project, preview the result, and write it out in one step.

## Requirements

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

Pinned versions are available in `requirements.txt` and `requirements-dev.txt`.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Or without editable install:

```bash
pip install -r requirements-dev.txt
```

## Usage

```
claude-md
```

or

```
python -m claude_mdfile_generator.cli
```

The TUI lets you browse your module library, select the modules you want, preview the generated output, and write it to a file (default: `CLAUDE.md`).

## Module concept

Modules are the building blocks of a `CLAUDE.md` file. There are two types:

- **static** — contains finished content written by you. It is included as-is.
- **template** — contains a placeholder instruction wrapped in an XML-style tag. The agent (Claude) is expected to fill it in when it reads the file.

## Module storage format

Each module is a Markdown file with YAML frontmatter stored in a directory:

```
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

Fields:

| Field | Required | Notes |
|---|---|---|
| `name` | yes | Display name shown in the TUI |
| `type` | yes | `static` or `template` |
| `tags` | no | List of strings for filtering |
| `order` | no | Integer; lower values appear first (default 50) |
| `description` | no | One-line summary shown in the TUI table |

## Modules directory

By default modules are stored in `~/.config/claude-mdfile-generator/modules/`.

Override with the `--modules-dir` flag:

```
claude-md --modules-dir ./my-modules
```

Or set the environment variable:

```
CLAUDE_MD_MODULES_DIR=./my-modules claude-md
```

## Creating custom modules

Use the TUI ("Create new module") or create a `.md` file directly in the modules directory following the format above.

## Bundled example modules

The `modules/` directory in this repository contains ready-to-use examples:

| File | Order | Type | Description |
|---|---|---|---|
| `project-summary-template.md` | 1 | template | Project purpose and tech stack |
| `project-context-template.md` | 2 | template | Setup commands and environment |
| `glossary-template.md` | 3 | template | Project-specific terminology |
| `architecture-template.md` | 5 | template | High-level architecture overview |
| `key-conventions-template.md` | 6 | template | Project-specific patterns and constraints |
| `investigation-first.md` | 8 | static | Read existing code before modifying |
| `forbidden-actions.md` | 9 | static | Explicit anti-patterns and forbidden behaviors |
| `git-rules.md` | 10 | static | Git workflow and commit practices |
| `pr-workflow.md` | 12 | static | Pull request conventions |
| `tdd-practices.md` | 15 | static | TDD guidelines and testing patterns |
| `code-style.md` | 20 | static | Code style and formatting |
| `code-quality.md` | 22 | static | Linting and type checking |
| `documentation.md` | 25 | static | Documentation practices |
| `security.md` | 26 | static | Security and secrets handling |
| `error-handling.md` | 28 | static | Error handling and resilience |
| `dependency-management.md` | 30 | static | Keeping dependencies minimal |
| `environment-setup.md` | 32 | static | Environment variables and setup |
| `api-interaction.md` | 34 | static | API interaction conventions |
| `multi-agent-workflow.md` | 35 | static | Safe multi-agent collaboration |
| `slash-commands.md` | 36 | static | Custom slash commands for Claude Code |
| `database-conventions.md` | 38 | static | Database naming and migration practices |
| `cross-platform.md` | 40 | static | Cross-platform compatibility |
| `performance.md` | 42 | static | Performance and optimization guidelines |
| `output-formatting.md` | 45 | static | Output formatting preferences |

Copy any of these into your modules directory to get started.

## Agent skills for template modules

Template modules produce placeholder sections (e.g. `<Architecture>...</Architecture>`) in the generated `CLAUDE.md`. These are meant to be filled in by an agent that analyzes the target project.

The `skills/` directory contains ready-made agent prompts for each template module:

| Skill | Fills template | What the agent does |
|---|---|---|
| `fill-project-summary.md` | `<Project Summary>` | Reads README and entry points to summarize the project |
| `fill-project-context.md` | `<Project Context>` | Extracts setup, test, lint commands and env requirements |
| `fill-glossary.md` | `<Glossary>` | Scans for domain-specific terms and jargon |
| `fill-architecture.md` | `<Architecture>` | Maps directory structure, components, data flows |
| `fill-key-conventions.md` | `<Key Conventions>` | Analyzes error handling, logging, naming, testing patterns |

### Usage

1. Generate a `CLAUDE.md` with the TUI, including the template modules you want
2. Point an agent at the target project with the corresponding skill prompt
3. The agent reads the codebase and replaces the `<Template>` blocks with real content

Each skill file contains detailed instructions, expected output format, and rules the agent must follow.
