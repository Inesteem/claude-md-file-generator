---
name: Cross-Platform Compatibility
type: static
tags: [compatibility, platform]
order: 40
description: Writing code that works across operating systems
---
## Cross-Platform Compatibility

- Use the language's standard path abstraction (e.g. `pathlib.Path` in Python, `path.join` in Node.js, `filepath.Join` in Go) — never concatenate paths with string operations
- Avoid OS-specific assumptions about path separators, temp directory locations, or executable names
- Specify text encoding explicitly (prefer UTF-8) rather than relying on the system default
- Handle line ending differences explicitly when reading or writing text files across platforms
- Validate cross-platform behavior in CI or on the target OS — passing on one platform does not guarantee correctness on another
