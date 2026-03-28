---
name: Formatter Configuration
type: template
tags: [formatting, tooling]
order: 24
description: Project-specific formatter setup and commands (agent-filled and verified)
---
<Fill Formatter Configuration>
Identify the code formatter(s) used in this project and document:
- Which formatter(s) are configured (e.g. black, prettier, rustfmt, gofmt, ruff format)
- The exact command to run them
- Where the configuration lives (e.g. pyproject.toml, .prettierrc)
- Any notable settings (line length, quote style, trailing commas, etc.)
- Whether formatting is enforced in CI or pre-commit hooks

Verify: run the format command in check/dry-run mode and confirm it works.
If no formatter is configured, state that explicitly.
</Fill Formatter Configuration>
