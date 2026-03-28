# Fill Template Sections

You are an agent tasked with filling in all `<Fill ...>` template sections in a CLAUDE.md file. Scan the file for any `<Fill SectionName>...</Fill SectionName>` blocks and replace each one with real content derived from analyzing the target project's codebase.

## General Rules

- Derive everything from the actual code — do not guess or assume
- Be concise — each section should be the minimum needed to orient a new contributor
- Omit sub-sections that don't apply to the project
- If something is unclear from the code alone, say so rather than inventing
- Keep the markdown heading level consistent (use `##` for section titles)

---

## `<Fill Project Summary>`

**What to read:** README, pyproject.toml / package.json / Cargo.toml, main entry points.

**Output format:**
```markdown
## Project Summary

**<project-name>** — <one-sentence purpose>.

- **Problem:** <what it solves and for whom>
- **Tech stack:** <language, framework, runtime, key libraries>
- **Entry points:** <CLI commands, API endpoints, or main modules>
```

Keep to 3-6 lines.

---

## `<Fill Project Context>`

**What to read:** Dependency/build config, Makefile, Dockerfile, test config, lint config, .env.example, CI files.

**Output format:**
```markdown
## Project Context

### Setup
\`\`\`bash
<exact setup commands>
\`\`\`

### Run
\`\`\`bash
<how to run locally>
\`\`\`

### Test
\`\`\`bash
<test command>
\`\`\`

### Lint
\`\`\`bash
<lint/format command>
\`\`\`

### Environment
- `ENV_VAR` — <purpose> (example: `value`)

### Requirements
- <runtime version, system libs, or other non-obvious constraints>

### Key Dependencies
- **<package>** — <why it exists, only if non-obvious>
```

Use exact commands from config. Omit sections that don't apply.

---

## `<Fill Glossary>`

**What to read:** Source code for domain-specific class/module/constant names, docstrings, README.

**Output format:**
```markdown
## Glossary

**<Term>**
: <Definition and relevant context.>
```

Only include terms that would confuse a newcomer. Sort alphabetically. If no meaningful jargon exists, write "No project-specific terminology beyond standard usage."

---

## `<Fill Architecture>`

**What to read:** Directory tree, source files (models, core logic, UI/CLI/API layer, storage), data flow through the primary use case.

**Output format:**
```markdown
## Architecture

### Directory Structure
- `src/` — <purpose>
- `tests/` — <purpose>

### Components
- **<Component>** (`path/`) — <responsibility>

### Data Flow
<primary flow in 2-4 sentences or a numbered list>

### External Integrations
- <databases, APIs, filesystems — or "None">

### State
- <where persistent and transient state lives>

### Design Decisions
- <key trade-off or pattern choice and why>
```

Focus on what helps navigate the codebase. Omit subsections that don't apply.

---

## `<Fill Key Conventions>`

**What to read:** Error handling patterns, logging setup, import style, test conventions, config files, comments marked HACK/WORKAROUND/noqa/nolint.

**Output format:**
```markdown
## Key Conventions

### Error Handling
- <approach and any custom types>

### Logging
- <library, levels, format>

### Language Constraints
- <version, avoided features>

### Naming
- <project-specific conventions>

### Imports
- <ordering rules>

### Testing
- <naming, fixtures, mocking approach>

### Configuration
- <key config files and what they control>

### Intentional Oddities
- <patterns that look wrong but are deliberate — explain why>
```

Only document conventions actually present in the code. Omit subsections where the project follows language defaults. For intentional oddities, always explain *why*.

---

## `<Fill Linter Configuration>`

**What to read:** pyproject.toml, .ruff.toml, .eslintrc, .pylintrc, Makefile, CI config.

**Verification:** Run the lint command and confirm it executes successfully. If it fails, document the failure.

**Output format:**
```markdown
## Linter Configuration

- **Linter:** <name and version if pinned>
- **Command:** `<exact command>`
- **Config:** `<config file path>`
- **Auto-fix:** `<auto-fix command, if available>`
- **Notable rules:** <any customized, disabled, or especially strict rules>
```

If no linter is configured, write "No linter configured." and move on.

---

## `<Fill Formatter Configuration>`

**What to read:** pyproject.toml, .prettierrc, Makefile, CI config, pre-commit config.

**Verification:** Run the format command in check/dry-run mode (e.g. `black --check .`, `prettier --check .`) and confirm it works.

**Output format:**
```markdown
## Formatter Configuration

- **Formatter:** <name and version if pinned>
- **Command:** `<exact command>`
- **Check mode:** `<dry-run command>`
- **Config:** `<config file path>`
- **Settings:** <line length, quote style, trailing commas, etc.>
- **Enforcement:** <CI check, pre-commit hook, or manual>
```

If no formatter is configured, write "No formatter configured." and move on.

---

## `<Fill Type Checker Configuration>`

**What to read:** pyrightconfig.json, mypy.ini, pyproject.toml [tool.mypy], tsconfig.json, CI config.

**Verification:** Run the type checker and note whether it passes cleanly. Document any existing errors and whether they are known/accepted.

**Output format:**
```markdown
## Type Checker Configuration

- **Type checker:** <name and version if pinned>
- **Command:** `<exact command>`
- **Config:** `<config file path>`
- **Strictness:** <strict, basic, or custom — note key overrides>
- **Known suppressions:** <any intentional ignores and why>
```

If no type checker is configured, write "No type checker configured." and move on.

---

## `<Fill CI Pipeline>`

**What to read:** .github/workflows/, .gitlab-ci.yml, Jenkinsfile, .circleci/, CI config files.

**Verification:** Read the CI config files and confirm the documented steps match what is actually configured. Cross-check that commands referenced in CI match the project's actual test/lint/build commands.

**Output format:**
```markdown
## CI Pipeline

- **System:** <GitHub Actions, GitLab CI, etc.>
- **Config:** `<config file path(s)>`

### PR checks
- <list each check: tests, lint, type check, build, etc.>

### Merge to main
- <deploy, publish, release — or "same as PR checks">

### Matrix
- <OS and runtime versions tested, if any>

### Required checks
- <checks that must pass before merging>
```

If no CI is configured, write "No CI pipeline configured." and move on.

---

## `<Fill Pre-commit Hooks>`

**What to read:** .pre-commit-config.yaml, .husky/, package.json (lint-staged), lefthook.yml.

**Verification:** Read the hook config and confirm hooks are correctly wired. Check that referenced tools are actually installed as project dependencies.

**Output format:**
```markdown
## Pre-commit Hooks

- **Framework:** <pre-commit, husky, lefthook, etc.>
- **Config:** `<config file path>`
- **Install:** `<command to activate hooks locally>`

### Hooks (in order)
1. <hook name> — <what it does>
2. <hook name> — <what it does>

### Bypass
- `<command to skip hooks>` — only acceptable for <specific scenarios>
```

If no pre-commit hooks are configured, write "No pre-commit hooks configured." and move on.
