---
name: Cross-Platform Compatibility
type: static
tags: [compatibility, platform]
order: 40
description: Writing code that works across operating systems
---
## Cross-Platform Compatibility

- Use `pathlib.Path` for all filesystem paths — never concatenate paths with string operations
- Avoid OS-specific assumptions about path separators, temp directory locations, or executable names
- Open text files with an explicit encoding (`encoding="utf-8"`) rather than relying on the system default
- Handle line ending differences explicitly when reading or writing text files across platforms
- Test on the target platform before declaring something works — behavior on Linux does not guarantee behavior on Windows or macOS
