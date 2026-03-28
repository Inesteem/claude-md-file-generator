# Fill Project Summary

You are an agent tasked with filling in the `<Project Summary>` template section of a CLAUDE.md file.

## Instructions

1. Read the project's top-level files to understand its purpose:
   - `README.md`, `pyproject.toml`, `package.json`, `Cargo.toml`, or equivalent
   - The main entry point(s)
2. Identify the tech stack by examining dependency files and source code
3. Find the primary entry points (CLI commands, API routes, main modules)

## Output

Replace the `<Project Summary>...</Project Summary>` block in CLAUDE.md with filled-in content. Use this format:

```markdown
## Project Summary

**<project-name>** — <one-sentence purpose>.

- **Problem:** <what it solves and for whom>
- **Tech stack:** <language, framework, runtime, key libraries>
- **Entry points:** <CLI commands, API endpoints, or main modules>
```

## Rules

- Be concise — this section should be 3-6 lines, not a wall of text
- State facts derived from the code, not assumptions
- If something is unclear from the code alone, say so rather than guessing
