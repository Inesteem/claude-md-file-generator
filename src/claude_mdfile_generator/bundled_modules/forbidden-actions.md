---
name: Forbidden Actions
type: static
tags: [safety, anti-patterns]
order: 9
description: Actions the agent must never take
---
## Forbidden Actions

- Do not modify files outside the defined project scope
- No speculative refactoring without first showing a diff plan for review
- Do not add features beyond what was explicitly asked for
- Do not create config, utility, or helper files when the logic fits naturally in an existing file
- Never silently delete or overwrite user code — confirm before destructive edits
