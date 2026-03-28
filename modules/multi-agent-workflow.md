---
name: Multi-Agent Workflow
type: static
tags: [agents, workflow, git]
order: 35
description: Safe collaboration patterns for multi-agent tasks
---
## Multi-Agent Workflow

- Assign tasks with clear, non-overlapping file boundaries to avoid merge conflicts
- Always stage specific files by name — never use `git add -A` or `git add .` in automated contexts
- Each agent works on its own branch; merge through pull requests, not direct pushes
- Resolve conflicts by re-reading the current file state before writing — never patch from stale context
- Keep task descriptions self-contained: include file paths, expected inputs/outputs, and acceptance criteria
- Prefer many small isolated tasks over one large task touching many files simultaneously
