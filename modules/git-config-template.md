---
name: Git Configuration
type: template
tags: [git, workflow]
order: 10
description: Project-specific git conventions, branching, and merge strategy (agent-filled)
---
<Fill Git Configuration>
Analyze the project's git conventions and document:
- Commit message format actually used (check recent git log)
- Branch naming pattern (e.g. feature/, fix/, <user>/<ticket>-<slug>)
- Protected branches and merge strategy (squash, rebase, merge commit)
- Default base branch for PRs
- Whether commit messages reference issue/ticket numbers

Verify: inspect the last 20 commits for actual patterns. Check for
branch protection rules in CI config or CODEOWNERS file.

Ask the user:
- What commit message convention does this project follow?
- What is the preferred merge strategy for PRs (squash, rebase, merge)?
</Fill Git Configuration>
