# claude-mdfile-generator

A lightweight TUI for composing `CLAUDE.md` files from a library of reusable modules. Pick the modules that apply to your project, preview the result, and write it out in one step.

## Installation

```
pip install -e ".[dev]"
```

Requires Python 3.11+.

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
| `tdd-practices.md` | 15 | static | Test-driven development guidelines |
| `testing-patterns.md` | 16 | static | Advanced testing patterns |
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
