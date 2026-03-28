---
name: Investigation First
type: static
tags: [workflow, investigation]
order: 8
description: Read existing code before modifying anything
---
## Investigation First

- Read the relevant code before writing or modifying anything — never guess at existing behavior
- Check the README and any guidance docs in subdirectories before starting work in that area
- For bugs: trace the data flow from input to output before touching code
- For new features: map every touch point (entry points, data models, tests, docs) before writing a single line
- Prefer one focused read pass over many scattered edits based on assumptions
