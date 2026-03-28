---
name: Environment Setup
type: static
tags: [environment, setup]
order: 32
description: Rules for handling environment variables and paths
---
## Environment Setup

- Compute all paths relative to the project root — never hardcode absolute paths
- Access only environment variables that have been explicitly allowed or documented
- Replace real credentials with clearly fake placeholders in all examples and demos
- Document every required environment variable with its name, purpose, and an example value
