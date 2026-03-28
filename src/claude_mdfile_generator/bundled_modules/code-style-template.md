---
name: Code Style
type: template
tags: [style, conventions]
order: 21
description: Project-specific naming, import, and style conventions (agent-filled)
---
<Fill Code Style>
Analyze the project's code style conventions and document:
- Language(s) and primary framework
- Naming convention for each symbol type (functions, classes, constants, files, test files)
- Max line length (if enforced beyond formatter default)
- Import ordering convention (stdlib / third-party / local, alphabetical, grouped)
- Project-specific patterns a newcomer would get wrong
- Whether a written style guide exists (and where it lives)

Verify: sample 5-10 source files and confirm the detected conventions
are consistent. Note any inconsistencies.

Do not duplicate what Formatter Configuration captures (which tool, how to run it).
Focus on the intent that the formatter cannot enforce.
</Fill Code Style>
