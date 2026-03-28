---
name: TODO Conventions
type: static
tags: [workflow, todos]
order: 37
description: Conventions for tracking TODOs, FIXMEs, and technical debt in code
---
## TODO Conventions

- Use `TODO:` for planned improvements and `FIXME:` for known broken behavior that needs urgent attention
- Always include context: who, why, and ideally a ticket reference (e.g. `TODO(user): refactor once #123 lands`)
- Never leave a bare `TODO` without an explanation — future readers need to understand the intent
- Treat `FIXME` items as bugs — they should be resolved before merging or tracked in the issue tracker
- Periodically review and clean up stale TODOs that are no longer relevant
- Do not use TODOs as a substitute for proper issue tracking on non-trivial work
