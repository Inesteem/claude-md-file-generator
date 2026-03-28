---
name: Slash Commands
type: static
tags: [commands, workflow, claude-code]
order: 36
description: Conventions for defining and using reusable /commands
---
## Slash Commands

- Define reusable `/commands` for common, repetitive workflows to keep prompts consistent
- Store command definitions as markdown files under `.claude/commands/*.md`
- Use kebab-case for command filenames (e.g. `run-tests.md`, `deploy-staging.md`)
- Include a brief description comment at the top of each command file explaining its purpose and any required arguments
- Reference available commands in `CLAUDE.md` so agents and contributors can discover them
- Distinguish between project-level commands (`.claude/commands/`) and user-level commands (`~/.claude/commands/`) and document which scope each belongs to
