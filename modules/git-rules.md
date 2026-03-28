---
name: Git Rules
type: static
tags: [git, workflow]
order: 10
description: Git workflow conventions and commit practices
---
## Git Rules

- Use conventional commits (feat:, fix:, refactor:, docs:, test:, chore:)
- Write concise commit messages that explain the "why", not the "what"
- Never force push to main/master
- Prefer creating new commits over amending existing ones
- Always review staged changes before committing
- Stage specific files by name — avoid `git add -A` or `git add .`
- Keep commits atomic — one logical change per commit
