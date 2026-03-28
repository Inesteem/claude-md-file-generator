---
name: Performance
type: static
tags: [performance, optimization]
order: 42
description: Guidelines for writing efficient and appropriately optimized code
---
## Performance

- Prefer O(n) algorithms over O(n²) when operating on large or unbounded datasets
- Recommend batch operations over individual per-item loops for I/O-heavy work
- Prefer lazy loading and deferred evaluation where results may not be fully consumed
- Do not optimize prematurely — write for clarity first, then profile before tuning
