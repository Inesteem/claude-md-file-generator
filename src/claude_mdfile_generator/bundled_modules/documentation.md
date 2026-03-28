---
name: Documentation
type: static
tags: [docs, documentation]
order: 25
description: Thorough documentation practices for codebases
---
## Documentation

- Update docs close to the code — keep READMEs in subdirectories alongside the code they describe
- Write meaningful docstrings for all public APIs you create or modify; skip them for obvious private helpers
- Flag undocumented public APIs you encounter but don't modify, rather than adding docstrings to untouched code
- Document non-obvious gotchas, edge cases, and lessons learned where they are most likely to be found
- Record the "why" behind non-trivial decisions, not just the "what"
- Treat outdated documentation as a bug — fix it when you encounter it, scoped to the area you are already working in
