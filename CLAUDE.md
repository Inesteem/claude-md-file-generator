## Project Summary

**claude-mdfile-generator** — A lightweight TUI for composing CLAUDE.md files from reusable, modular building blocks.

- **Problem:** Manually writing CLAUDE.md files is repetitive and error-prone. This tool lets developers select from a library of static best-practice modules and agent-filled templates to generate a tailored CLAUDE.md for any project.
- **Tech stack:** Python 3.11+, hatchling (build), pyyaml, questionary, rich
- **Entry points:** `claude-md` CLI command (`src/claude_mdfile_generator/cli.py:main`)

## Project Context

### Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Run
```bash
claude-md --bundled                          # use bundled modules (read-only)
claude-md --modules-dir ./modules            # use project's dev modules
claude-md --init                             # copy bundled modules to ~/.config/claude-mdfile-generator/modules/
claude-md --init-skills ~/.claude/skills     # copy fill skill
```

### Test
```bash
pytest                   # 44 tests, ~0.3s
pytest -q                # quiet output
pytest tests/test_storage.py  # single file
```

### Lint
```bash
ruff check src/ tests/         # lint
ruff format src/ tests/        # format
ruff check --fix src/ tests/   # auto-fix
```

### Type check
```bash
pyright src/
```

### Requirements
- Python 3.11+ (uses `StrEnum`, `X | None` syntax)

### Key Dependencies
- **pyyaml** — parses YAML frontmatter in module .md files
- **questionary** — interactive terminal prompts (checkbox, select, text, path)
- **rich** — terminal output formatting (tables, panels, markdown preview)

## Glossary

**Module**
: A markdown file with YAML frontmatter that represents one semantic section of a CLAUDE.md file. Can be `static` (fixed content) or `template` (agent-filled placeholder).

**Static module**
: A module containing generic best-practice advice included as-is. Same content for every project.

**Template module**
: A module containing a `<Fill SectionName>` placeholder block. An agent analyzes the target project and replaces the placeholder with project-specific content.

**Companion template**
: A template module that pairs with a static module at the same order number, adding project-specific details to the generic advice.

**Fill skill**
: The agent prompt (`skills/fill.md`) that instructs an agent how to process all `<Fill ...>` blocks in a generated CLAUDE.md.

**Bundled modules**
: The 38 modules shipped inside the pip package under `bundled_modules/`, accessible via `--bundled` or `--init`.

## Architecture

### Directory Structure
- `src/claude_mdfile_generator/` — Python package (models, storage, generator, TUI, CLI, bundled data)
- `tests/` — pytest test suite (44 tests covering models, storage, generator, TUI)
- `modules/` — development copy of bundled modules (source of truth, 38 .md files)
- `skills/` — development copy of bundled skills (source of truth, fill.md)

### Components
- **models.py** — `Module` dataclass and `ModuleType` enum (`StrEnum`: static/template)
- **storage.py** — CRUD for module files: `load_module`, `save_module`, `delete_module`, `list_modules`. Parses YAML frontmatter + markdown body.
- **generator.py** — Pure function `generate(modules) -> str`. Sorts by (order, name), joins with newlines.
- **tui.py** — Interactive TUI using questionary + rich. Main loop: browse, select, create, edit, delete modules.
- **cli.py** — argparse entry point. Handles `--init`, `--bundled`, `--init-skills`, `--modules-dir`.
- **bundled.py** — `importlib.resources`-based access to embedded modules/skills. `copy_bundled_modules()` and `copy_bundled_skills()`.

### Data Flow
1. User runs `claude-md` → CLI parses args → resolves modules directory
2. `list_modules()` reads all `.md` files from the directory, parses frontmatter, returns sorted `Module` list
3. TUI displays modules table → user selects via checkbox
4. `generate()` sorts selected modules by (order, name), concatenates content with newline separators
5. User previews output, confirms path, file is written

### External Integrations
- None. Pure local filesystem operations. No network, no database.

### State
- **Modules directory** (filesystem) — user's module files, default `~/.config/claude-mdfile-generator/modules/`
- **Bundled data** (package) — read-only modules/skills embedded in the installed package
- No persistent state, config files, or databases

### Design Decisions
- **Markdown with YAML frontmatter** for module storage — modules are human-readable and editable outside the tool. No JSON/YAML serialization pain for multiline markdown content.
- **`src/` layout** — prevents accidental local imports during testing.
- **Generator is a pure function** — no I/O, trivially testable. All file operations happen in storage and CLI layers.
- **Bundled modules are copied into the package** — means `pip install` gives users the full module library without cloning the repo. Trade-off: development copy (`modules/`) and bundled copy (`bundled_modules/`) must be kept in sync manually.

## Key Conventions

### Error Handling
- `StorageError` exception for malformed module files (missing frontmatter, missing required fields)
- `list_modules()` catches `StorageError` and `ValueError` per-file and logs a warning, returning only valid modules — never crashes the whole list on one corrupt file
- `FileNotFoundError` raised directly for missing files in `load_module` and `delete_module`

### Logging
- `logging` stdlib module, used only in `storage.py` for warning about skipped corrupt files
- No structured logging; plain text warnings

### Language Constraints
- Python 3.11+ required — uses `StrEnum` (3.11+), `X | None` union syntax (3.10+)
- No `from __future__ import annotations`

### Naming
- Standard Python: `snake_case` functions/variables, `PascalCase` classes, `UPPER_CASE` constants
- Module filenames use kebab-case (e.g. `git-rules.md`, `testing-config-template.md`)
- Template modules end with `-template.md`

### Imports
- Enforced by ruff `I` rule: stdlib first, third-party second, local third, alphabetical within groups
- Relative imports within the package (e.g. `from .models import Module`)

### Testing
- pytest with `tmp_path` fixtures for filesystem tests
- Test classes grouped by feature (`TestSaveAndLoad`, `TestDelete`, `TestListModules`)
- Shared fixtures in `conftest.py` (`sample_static_module`, `sample_template_module`, `populated_modules_dir`)
- TUI tested via `unittest.mock.patch` on questionary
- No mocking of storage layer — all tests use real filesystem via `tmp_path`

### Configuration
- `pyproject.toml` — build config, dependencies, ruff config, pyright config, pytest config (all in one file)
- `requirements.txt` / `requirements-dev.txt` — pinned versions for reproducibility

### Intentional Oddities
- `bundled_modules/` and `modules/` contain duplicate content — this is intentional. `modules/` is the development source of truth; `bundled_modules/` is the copy embedded in the pip package. After changing `modules/`, you must re-copy to `bundled_modules/` (or reinstall with `pip install -e .`).

## Investigation First

- Read the relevant code before writing or modifying anything — never guess at existing behavior
- Check the README and any guidance docs in subdirectories before starting work in that area
- For bugs: trace the data flow from input to output before touching code
- For new features: map every touch point (entry points, data models, tests, docs) before writing a single line
- Prefer one focused read pass over many scattered edits based on assumptions

## Git Configuration

- **Commit format:** Conventional commits — `feat:`, `fix:`, `refactor:`, `chore:`, `docs:` prefixes, followed by a short summary. Body explains the "why". All commits include `Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>` trailer.
- **Branch naming:** Single `master` branch (no feature branches yet — solo development)
- **Protected branches:** None configured
- **Merge strategy:** Not applicable yet (no PRs, single branch)
- **Default base branch:** `master`
- **Ticket references:** None — no issue tracker configured

## Testing Configuration

- **Framework:** pytest 9.0.2
- **Run all:** `pytest` (or `pytest -q` for quiet)
- **Run single file:** `pytest tests/test_storage.py`
- **Run single test:** `pytest tests/test_storage.py::TestSaveAndLoad::test_round_trip`
- **Test directory:** `tests/` — naming convention: `test_*.py`, classes `Test*`, methods `test_*`
- **Coverage:** Not configured
- **Test DB/fixtures:** No database. Filesystem tests use pytest `tmp_path`. Shared fixtures in `conftest.py`.
- **Mocking:** `unittest.mock.patch` for TUI tests only. Storage and generator tests use real implementations.
- **CI command:** No CI configured
- **Known skips:** None

## Code Style

- **Language(s):** Python 3.11+, no framework
- **Naming:** functions: `snake_case`, classes: `PascalCase`, constants: `UPPER_CASE`, files: `snake_case.py`, module files: `kebab-case.md`
- **Line length:** 120 (enforced by ruff)
- **Imports:** stdlib / third-party / local, alphabetical within groups (enforced by ruff `I` rule, relative imports within package)
- **Project-specific patterns:** Module dataclass uses `@property` for `slug` and `filename` (derived, not stored). Generator is a pure function — no side effects.
- **Style guide:** None beyond ruff enforcement

## Code Quality

- Run the linter before committing; do not leave lint errors in changed files
- Use the project's type checker and fix type errors in any code you touch
- Prefer strict type checking settings over lenient ones
- Do not suppress type errors with broad ignores — fix the underlying issue or use a narrow, commented suppression
- Keep cyclomatic complexity low; extract helpers rather than nesting conditionals

## Linter Configuration

- **Linter:** ruff >=0.8 (pinned: 0.15.8)
- **Command:** `ruff check src/ tests/`
- **Config:** `pyproject.toml` under `[tool.ruff]` and `[tool.ruff.lint]`
- **Auto-fix:** `ruff check --fix src/ tests/` (use `--unsafe-fixes` for migrations like `str, Enum` → `StrEnum`)
- **Notable rules:** `E, F, W` (pycodestyle + pyflakes), `I` (isort), `UP` (pyupgrade), `B` (bugbear), `SIM` (simplify), `RUF` (ruff-specific)

## Type Checker Configuration

- **Type checker:** pyright >=1.1 (pinned: 1.1.408)
- **Command:** `pyright src/`
- **Config:** `pyproject.toml` under `[tool.pyright]`
- **Strictness:** `basic` mode, targeting Python 3.11, Linux platform
- **Known suppressions:** None — 0 errors, 0 warnings, 0 informations

## Formatter Configuration

- **Formatter:** ruff format (same tool as linter)
- **Command:** `ruff format src/ tests/`
- **Check mode:** `ruff format --check src/ tests/`
- **Config:** `pyproject.toml` under `[tool.ruff]` — line-length: 120, target-version: py311
- **Settings:** Line length 120, double quotes (ruff default), no trailing comma enforcement
- **Enforcement:** Manual (no CI or pre-commit hooks configured)

## Documentation Strategy

### Documentation Inventory
| Artifact | Location | Covers | Update when |
|---|---|---|---|
| README.md | `/README.md` | Installation, usage, all CLI flags, full module catalog, skill docs, dev guide | New modules, CLI changes, workflow changes |
| requirements.txt | `/requirements.txt` | Pinned runtime deps | Dependency version changes |
| requirements-dev.txt | `/requirements-dev.txt` | Pinned dev deps | Dev dependency changes |
| fill.md skill | `/skills/fill.md` | Agent instructions for all 20 Fill tags | New template modules added |

### Generated Docs
- None

### External Docs
- None

### Process
- README must be updated when adding new modules, CLI flags, or changing the workflow
- Fill skill must be updated when adding new `<Fill ...>` template types
- Bundled copies (`bundled_modules/`, `bundled_skills/`) must be re-synced after changing `modules/` or `skills/`

## Dependency Configuration

- **Package manager:** pip
- **Dependency file:** `pyproject.toml` under `[project.dependencies]` and `[project.optional-dependencies.dev]`
- **Lock file:** `requirements.txt` (runtime) and `requirements-dev.txt` (dev) — update manually with `pip freeze`
- **Banned packages:** None
- **Vendored deps:** None
- **Monorepo:** N/A (single package)
- **Vetting policy:** None formal — preference for minimal dependencies (currently 3 runtime deps)

## Multi-Agent Workflow

- Re-read the current file state before every write — never patch from stale context
- Assign tasks with clear, non-overlapping file boundaries to avoid merge conflicts
- Announce which files you intend to modify before starting work on a task
- Each agent works on its own branch; merge through pull requests, not direct pushes
- Keep task descriptions self-contained: include file paths, expected inputs/outputs, and acceptance criteria
- Prefer many small isolated tasks over one large task touching many files simultaneously
