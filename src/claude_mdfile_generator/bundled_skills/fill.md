# Fill Template Sections

You are an agent tasked with filling in all `<Fill ...>` template sections in a CLAUDE.md file. Scan the file for any `<Fill SectionName>...</Fill SectionName>` blocks and replace each one with real content derived from analyzing the target project's codebase.

## General Rules

- Derive everything from the actual code — do not guess or assume
- Be concise — each section should be the minimum needed to orient a new contributor
- Omit sub-sections that don't apply to the project
- Keep the markdown heading level consistent (use `##` for section titles)

## Asking the User

Some templates include an "Ask the user" block. When you encounter one:

1. First fill in everything you can derive from the codebase
2. Then ask the user the listed questions — present what you found so far and ask them to confirm, correct, or add details
3. Incorporate their answers into the final output
4. If the user is unavailable or says "skip", fill in what you can and mark gaps with `<!-- TODO: ask project owner about ... -->`

Never invent answers to user questions. If you can't derive it and can't ask, leave the TODO marker.

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

---

## `<Fill Documentation Strategy>`

**What to read:** All README files, docs/ directory, any .rst/.md docs, Sphinx/typedoc/rustdoc config, requirements docs, changelogs, CONTRIBUTING.md.

**Ask the user:**
- Are there docs outside the repo (wiki, Confluence, Notion, Google Docs)? Where?
- Which docs are user-facing vs. developer-facing?
- Is there a documentation review process (e.g. docs required in PRs)?

**Output format:**
```markdown
## Documentation Strategy

### Documentation Inventory
| Artifact | Location | Covers | Update when |
|---|---|---|---|
| <name> | `<path>` | <what it covers> | <trigger for update> |

### Generated Docs
- **Tool:** <Sphinx, typedoc, etc. — or "None">
- **Build command:** `<command>`
- **Output:** `<where generated docs go>`

### External Docs
- <wiki/Confluence/Notion links and what they cover — or "None">

### Process
- <when and how docs are updated: in PRs, after release, on a schedule>
- <who is responsible: author, reviewer, dedicated docs role>
```

Omit subsections that don't apply. If the project has no documentation beyond a root README, say so simply.

---

## `<Fill Testing Configuration>`

**What to read:** Test config files (pytest.ini, pyproject.toml, jest.config, vitest.config, Cargo.toml), test directories, CI config for test commands, coverage config.

**Verification:** Run the test suite and confirm it passes. Note failing or skipped tests.

**Ask the user:**
- Is there a minimum coverage requirement?
- Are there tests that are known-flaky or intentionally skipped?

**Output format:**
```markdown
## Testing Configuration

- **Framework:** <name (e.g. pytest, vitest, go test)>
- **Run all:** `<command>`
- **Run single file:** `<command>`
- **Run single test:** `<command>`
- **Test directory:** `<path>` — naming convention: `<pattern>`
- **Coverage:** `<tool and threshold, or "not configured">`
- **Test DB/fixtures:** <setup approach, or "N/A">
- **Mocking:** <libraries used, what gets mocked>
- **CI command:** `<if different from local>`
- **Known skips:** <intentionally skipped tests and why>
```

---

## `<Fill Forbidden Zones>`

**What to read:** .gitattributes (linguist-generated), codegen config, auto-generated file headers, vendored directories, CODEOWNERS.

**Verification:** Check for auto-generated markers in file headers, .gitattributes entries, and codegen config files.

**Ask the user:**
- Are there files or directories owned by another team?
- Are there config files that require a special process to change?
- Are there generated files that should never be hand-edited?

**Output format:**
```markdown
## Forbidden Zones

### Generated Files (do not hand-edit)
| File/Directory | Generated by | Regenerate with |
|---|---|---|
| `<path>` | `<tool>` | `<command>` |

### Lock Files
| File | Update with |
|---|---|
| `<path>` | `<command>` |

### Team-Owned Boundaries
- `<path>` — owned by <team>, requires <process> to change

### Special-Process Config
- `<path>` — change via <process>
```

Omit subsections that don't apply.

---

## `<Fill Error Patterns>`

**What to read:** Custom exception/error classes, error handling in request handlers or CLI entry points, logging around errors, retry logic.

**Verification:** Search for custom error/exception classes and trace how they propagate through the codebase.

**Ask the user:**
- Is there a retry/fallback policy for external service failures?
- Are there error types that should never be caught silently?

**Output format:**
```markdown
## Error Patterns

- **Propagation:** <exceptions, Result types, error codes, HTTP statuses>
- **Custom types:** <list of error classes/types and when to use each>
- **Logging:** <errors logged at origin vs. boundary, which logger>
- **API error shape:** <response format for errors, if applicable>
- **Third-party errors:** <wrap, re-raise, or convert to domain errors>
- **Retry/fallback:** <policy, or "none">
```

---

## `<Fill Git Configuration>`

**What to read:** Last 20 git commits (patterns), branch names, CODEOWNERS, CI config for branch protection, .github/ config.

**Verification:** Inspect recent commits for actual message format. Check for branch protection markers in CI config.

**Ask the user:**
- What commit message convention does this project follow?
- What is the preferred merge strategy for PRs (squash, rebase, merge)?

**Output format:**
```markdown
## Git Configuration

- **Commit format:** <convention detected or stated by user>
- **Branch naming:** `<pattern>` (e.g. `feature/<slug>`, `fix/<ticket>-<slug>`)
- **Protected branches:** <list>
- **Merge strategy:** <squash, rebase, or merge commit>
- **Default base branch:** `<branch name>`
- **Ticket references:** <whether commit messages reference issue numbers>
```

---

## `<Fill PR Configuration>`

**What to read:** .github/PULL_REQUEST_TEMPLATE.md, CODEOWNERS, CI config for required checks, label definitions.

**Verification:** Check for PR template files, CODEOWNERS, and CI required-check config.

**Ask the user:**
- Are there required reviewers or CODEOWNERS for specific paths?
- Do you use labels on PRs? If so, what conventions?

**Output format:**
```markdown
## PR Configuration

- **PR template:** `<path, or "none">`
- **Required reviewers:** <CODEOWNERS rules or team conventions>
- **Required checks:** <list of CI checks that must pass>
- **Labels:** <conventions, or "none">
- **Auto-merge:** <rules, or "not configured">
- **Base branch:** `<default target branch>`
```

---

## `<Fill Code Style>`

**What to read:** 5-10 representative source files, import blocks, naming patterns, any STYLE.md or CONTRIBUTING.md.

**Verification:** Sample source files and confirm conventions are consistent. Note inconsistencies.

Do NOT duplicate what Formatter Configuration captures (which tool, how to run it). Focus on intent the formatter cannot enforce.

**Output format:**
```markdown
## Code Style

- **Language(s):** <primary language and framework>
- **Naming:** functions: `<convention>`, classes: `<convention>`, constants: `<convention>`, files: `<convention>`
- **Line length:** <max, or "formatter default">
- **Imports:** <ordering convention>
- **Project-specific patterns:** <things a newcomer would get wrong>
- **Style guide:** `<path, or "none">`
```

---

## `<Fill Dependency Configuration>`

**What to read:** Package manager config, lock files, dependency specification files, any CONTRIBUTING.md notes on deps.

**Verification:** Locate lock files and confirm they are committed. Check for vendored directories.

**Ask the user:**
- Are there any packages or categories that should not be added?
- Is there a policy for vetting new dependencies (license, popularity)?

**Output format:**
```markdown
## Dependency Configuration

- **Package manager:** <name>
- **Dependency file:** `<path>`
- **Lock file:** `<path>` — update with `<command>`
- **Banned packages:** <list, or "none">
- **Vendored deps:** `<path>`, or "none"
- **Monorepo:** <workspace setup, or "N/A">
- **Vetting policy:** <requirements for new deps, or "none">
```

---

## `<Fill Database Configuration>`

**What to read:** ORM/database config, migration directory, model files, connection setup, schema files.

**Verification:** Check for migration files, ORM config, and database connection setup. If no database is found, state that explicitly and recommend removing the Database Conventions static module.

**Ask the user:**
- What database engine and ORM/migration tool does this project use?

**Output format:**
```markdown
## Database Configuration

- **Engine:** <PostgreSQL, MySQL, SQLite, MongoDB, etc.>
- **ORM/query builder:** <SQLAlchemy, Prisma, ActiveRecord, etc.>
- **Migration tool:** <Alembic, Flyway, Prisma Migrate, etc.>
- **Migration directory:** `<path>`
- **Run migrations:** `<command>`
- **Naming conventions:** <detected from existing schema/models>
- **Connection:** <env var name, pooling setup>
```

If no database is used, write "No database configured. Consider removing the Database Conventions module."

---

## `<Fill API Configuration>`

**What to read:** HTTP client imports/usage, API base URLs, auth configuration, retry logic, SDK references.

**Verification:** Search for HTTP client usage, base URLs, and auth patterns. If no external API usage is found, state that explicitly and recommend removing the API Interaction static module.

**Ask the user:**
- Does this project interact with external APIs? If so, which ones?
- Are there rate limits or quotas the agent should be aware of?

**Output format:**
```markdown
## API Configuration

### APIs Consumed
| Service | Base URL / SDK | Auth pattern |
|---|---|---|
| <name> | `<url or package>` | <OAuth, API key, bearer, etc.> |

- **HTTP client:** <library used>
- **Retry policy:** <backoff strategy, or "none">
- **Rate limits:** <known limits, or "unknown">
```

If the project does not use external APIs, write "No external API integrations. Consider removing the API Interaction module."
