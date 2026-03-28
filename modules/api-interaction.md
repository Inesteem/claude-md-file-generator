---
name: API Interaction
type: static
tags: [api, http]
order: 34
description: Safe and correct patterns for working with HTTP APIs
---
## API Interaction

- Never expose authentication tokens in examples — use `Bearer ****` or `<TOKEN>` as placeholders
- Respect API rate limits; add backoff or retry logic where appropriate
- Handle pagination and continuation tokens — never assume a single response contains all results
- Always include explicit headers in `curl` and HTTP client examples (e.g. `Content-Type`, `Authorization`)
