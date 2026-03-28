# Fill Project Context

You are an agent tasked with filling in the `<Project Context>` template section of a CLAUDE.md file.

## Instructions

1. Determine setup commands by reading:
   - `pyproject.toml`, `package.json`, `Makefile`, `Dockerfile`, or equivalent
   - Any existing setup/install scripts
2. Figure out how to run the project locally (look for `[project.scripts]`, `main` entries, `Makefile` targets)
3. Identify test and lint commands by examining:
   - Test config (`pytest.ini`, `pyproject.toml [tool.pytest]`, `jest.config`, etc.)
   - Lint/format config (`.ruff.toml`, `.eslintrc`, `pyproject.toml [tool.ruff]`, etc.)
4. Check for `.env.example`, `.env.template`, or env var references in code
5. Note any non-obvious requirements (specific Python/Node version, system libraries, OS constraints)

## Output

Replace the `<Project Context>...</Project Context>` block in CLAUDE.md with filled-in content. Use this format:

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
- `ENV_VAR_NAME` — <purpose> (example: `value`)

### Requirements
- <runtime version, system libs, or other non-obvious constraints>

### Key Dependencies
- **<package>** — <why it exists, only if non-obvious>
```

## Rules

- Use the exact commands that work — verify by reading config, don't guess
- Only list dependencies whose purpose is non-obvious from their name
- Omit sections that don't apply (e.g. no Environment section if there are no env vars)
