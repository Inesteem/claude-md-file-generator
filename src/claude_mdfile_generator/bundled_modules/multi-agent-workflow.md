---
name: Multi-Agent Workflow
type: static
tags: [agents, workflow, git]
order: 35
description: Safe collaboration patterns for multi-agent tasks
---
## Multi-Agent Workflow

- Re-read the current file state before every write — never patch from stale context
- Assign tasks with clear, non-overlapping file boundaries to avoid merge conflicts
- Announce which files you intend to modify before starting work on a task
- Each agent works on its own branch; merge through pull requests, not direct pushes
- Keep task descriptions self-contained: include file paths, expected inputs/outputs, and acceptance criteria
- Prefer many small isolated tasks over one large task touching many files simultaneously
