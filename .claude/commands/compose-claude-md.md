---
description: Compose a tailored CLAUDE.md for a project by selecting relevant modules, generating, and filling templates
argument-hint: [project path (default: current directory)]
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Agent
---

Compose a CLAUDE.md for the project at: $ARGUMENTS (default: current working directory).

Follow the skill instructions in ~/.claude/skills/compose-claude-md.md exactly.

Summary of the workflow:
1. Analyze the project (README, config, source code) to understand its stack and needs
2. List available modules: `claude-md list --bundled --json`
3. Select relevant modules — skip ones that don't apply (no DB → skip Database, no API → skip API, etc.)
4. Generate: `claude-md generate --bundled --modules "..." -o CLAUDE.md`
5. Fill all `<Fill ...>` template blocks by analyzing the codebase (follow ~/.claude/skills/fill.md)
6. Do a final review pass for duplications, contradictions, and irrelevant sections
7. Present the completed CLAUDE.md to the user for review

If the project already has a CLAUDE.md, read it first and use `--append` to add only missing modules.
