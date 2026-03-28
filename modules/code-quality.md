---
name: Code Quality
type: static
tags: [quality, linting, type-checking]
order: 22
description: Linting and type checking practices
---
## Code Quality

- Run the linter before committing; do not leave lint errors in changed files
- Use a type checker (pyright or mypy) and fix type errors in any code you touch
- Prefer strict type checking settings over lenient ones
- Do not suppress type errors with broad ignores — fix the underlying issue or use a narrow, commented suppression
- Keep cyclomatic complexity low; extract helpers rather than nesting conditionals
