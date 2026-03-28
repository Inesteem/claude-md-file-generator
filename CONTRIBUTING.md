# Contributing

## Setup

```bash
git clone https://github.com/yourusername/claude-mdfile-generator.git
cd claude-mdfile-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Running checks

```bash
pytest                              # run tests
ruff check src/ tests/              # lint
ruff format src/ tests/             # format
pyright src/                        # type check
```

All four must pass before opening a PR.

## Adding a bundled module

1. Create the module file in `modules/` (static or template, with YAML frontmatter).
2. Copy it to `src/claude_mdfile_generator/bundled_modules/` to embed it in the package.
3. Reinstall locally: `pip install -e .`
4. Update `README.md` to list the new module.
5. If the module is a template, update `skills/fill.md` and `src/claude_mdfile_generator/bundled_skills/fill.md` with instructions for its `<Fill ...>` tag.

## PR expectations

- Tests pass, lint clean, type clean (see CI).
- Include a brief description of the change and reference any related issues.
- Keep PRs focused — one logical change per PR.
