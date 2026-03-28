# Compose a CLAUDE.md for a Project

You are an agent tasked with analyzing a project and composing a tailored CLAUDE.md file using `claude-md`. You will select the relevant modules, generate the file, then fill in the template sections.

## Prerequisites

Ensure `claude-md` is installed:
```bash
claude-md --version
```
If not installed, run: `pip install git+https://github.com/Inesteem/claude-md-file-generator.git`

## Step 1 — Analyze the project

Before selecting modules, understand the project:

1. Read the README, main config file (pyproject.toml, package.json, Cargo.toml, etc.)
2. Identify:
   - **Language and framework** (determines which modules apply)
   - **Has database?** (if no → skip Database modules)
   - **Has external APIs?** (if no → skip API modules)
   - **Has CI?** (if no → skip CI Pipeline module)
   - **Has pre-commit hooks?** (if no → skip Pre-commit Hooks module)
   - **Multi-agent project?** (if no → skip Multi-Agent Workflow)
   - **Cross-platform?** (if single OS → skip Cross-Platform)

## Step 2 — List available modules

```bash
claude-md list --bundled --json
```

This outputs all 42 bundled modules with name, type, tags, order, and description.

## Step 3 — Select modules

Based on your analysis, decide which modules to include. Rules of thumb:

**Almost always include:**
- Project Summary, Project Context, Architecture, Key Conventions (templates)
- Investigation First, Forbidden Actions, Git Rules, Code Style, Code Quality (static)
- Security, Error Handling (static)

**Include if the project uses them:**
- Testing + Testing Configuration (if tests exist)
- Linter/Formatter/Type Checker Configuration (if those tools are configured)
- Database Conventions + Database Configuration (if a database exists)
- API Interaction + API Configuration (if external APIs are consumed)
- CI Pipeline (if CI is configured)
- Pre-commit Hooks (if hooks are configured)
- Pull Requests + PR Configuration (if the project uses PRs)
- Git Configuration (to document actual conventions)

**Include the companion template** whenever you include a static module that has one — the template adds project-specific details that make the static advice actionable.

**Skip if not applicable:**
- Multi-Agent Workflow (solo projects)
- Cross-Platform Compatibility (single-platform projects)
- Slash Commands (if not using Claude Code commands)
- Database modules (no database)
- API modules (no external APIs)

## Step 4 — Generate

Use `--modules` for explicit selection or `--exclude` to remove from the full set:

```bash
# Explicit selection (recommended for precision)
claude-md generate --bundled \
  --modules "Project Summary,Project Context,Architecture,Key Conventions,Investigation First,Git Rules,Git Configuration,Testing,Testing Configuration,Code Style,Code Quality,Linter Configuration,Security,Error Handling" \
  -o CLAUDE.md

# Or start with everything and exclude what doesn't apply
claude-md generate --bundled \
  --exclude "Database Conventions,Database Configuration,API Interaction,API Configuration,Multi-Agent Workflow,Cross-Platform Compatibility,Slash Commands" \
  -o CLAUDE.md
```

You can also filter by tags:
```bash
# Only static modules (no templates)
claude-md generate --bundled --type static -o CLAUDE.md

# Only testing-related modules
claude-md generate --bundled --tags testing -o CLAUDE.md
```

## Step 5 — Fill templates

The generated CLAUDE.md contains `<Fill ...>` placeholder blocks. Fill them by following the fill skill instructions:

1. For each `<Fill SectionName>` block, analyze the project's codebase
2. Replace the placeholder with real, verified content
3. For blocks with "Ask the user" instructions, present what you found and ask the user to confirm or add details
4. Mark unresolvable gaps with `<!-- TODO: ask project owner about ... -->`

## Step 6 — Final review

After filling all templates, review the complete CLAUDE.md for:

1. **Duplications** — same advice in both a static section and a filled template
2. **Contradictions** — static advice that conflicts with the project's actual setup
3. **Irrelevant sections** — modules that turned out not to apply
4. **Completeness** — any important project aspects not covered

Present a summary of findings and the complete CLAUDE.md to the user for review.

## Augmenting an existing CLAUDE.md

If the project already has a CLAUDE.md and the user wants to add specific modules to it:

1. **Read the existing CLAUDE.md** and identify which sections are already present
2. **List available modules** and determine which ones are missing
3. **Generate only the missing modules** and append them:

```bash
# Append specific modules to an existing file
claude-md generate --bundled \
  --modules "Testing Configuration,Linter Configuration,Security" \
  --append -o CLAUDE.md
```

4. **Fill any new `<Fill ...>` blocks** that were added
5. **Review for duplications** — the new modules may overlap with content already in the file. Check and deduplicate.

**Important:** When appending, the agent should:
- Read the existing file first to understand what's already there
- Only add modules whose content is not already covered
- After appending, review the full file for coherence — the ordering of appended sections may need adjustment
- Remove any `<Fill ...>` blocks for templates whose content is already manually written in the existing file

## Example: New CLAUDE.md for a Python project

```bash
# 1. See what's available
claude-md list --bundled --type template --json

# 2. Generate with relevant modules
claude-md generate --bundled \
  --exclude "Database Conventions,Database Configuration,API Interaction,API Configuration,Multi-Agent Workflow,Slash Commands,Cross-Platform Compatibility" \
  -o CLAUDE.md

# 3. Fill templates (done by the agent, not a CLI command)
# Read CLAUDE.md, fill each <Fill ...> block from code analysis

# 4. Review and present to user
```

## Example: Add modules to an existing CLAUDE.md

```bash
# 1. Check what's already in the file
cat CLAUDE.md

# 2. See what modules are available
claude-md list --bundled --json

# 3. Append only the missing modules
claude-md generate --bundled \
  --modules "Testing Configuration,Linter Configuration,Formatter Configuration" \
  --append -o CLAUDE.md

# 4. Fill the new <Fill ...> blocks
# 5. Review the full file for duplications and coherence
```

## CLI Reference

```
claude-md list [--json] [--tags TAGS] [--type static|template] [--bundled] [--modules-dir PATH]
claude-md generate [--modules NAMES] [--tags TAGS] [--type static|template] [--exclude NAMES] [-o FILE] [--append] [--bundled] [--modules-dir PATH]
claude-md init [--modules-dir PATH]
claude-md init-skills DEST
claude-md                              # launch interactive TUI (default)
```
