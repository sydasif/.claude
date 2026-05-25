# Async Patterns

- Use `async`/`await`
- `asyncio.gather()` for concurrent independent tasks
- `asyncio.create_task()` for spawning tasks
- `asyncio.timeout()` (3.11+) for timeouts
- `async with` for async context managers
- Never `asyncio.run()` in libraries (use `asyncio.get_running_loop()` instead)

## Anti‑patterns

- No sync blocking calls (`time.sleep`, `open()`) inside async functions
- Await all coroutines – unawaited coroutines silently do nothing
- Replace `asyncio.sleep(0)` busy‑loops with proper event‑driven patterns
