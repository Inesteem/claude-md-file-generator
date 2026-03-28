---
name: API Configuration
type: template
tags: [api, http, tooling]
order: 34
description: Project-specific API integrations, clients, and auth patterns (agent-filled)
---
<Fill API Configuration>
Identify whether and how this project interacts with external APIs:
- Does the project consume external APIs at all?
- Specific APIs/services consumed (with base URLs or SDK references)
- Auth pattern per API (OAuth, API key header, service account, bearer token)
- Preferred HTTP client library
- Retry/backoff policy (if one exists)
- Rate limit specifics the agent should respect

Verify: search for HTTP client usage, API base URLs, and auth configuration.
If the project does not interact with external APIs, state that explicitly
and recommend removing the API Interaction static module from this CLAUDE.md.

Ask the user:
- Does this project interact with external APIs? If so, which ones?
- Are there rate limits or quotas the agent should be aware of?
</Fill API Configuration>
