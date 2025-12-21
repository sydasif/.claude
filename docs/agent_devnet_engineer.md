# Comprehensive Network Automation Guide

## Connection & Safety Standards

- **Timeouts**: SSH Connect (60s), Auth (30s), Command Execute (120s), Global (300s).
- **Retry Logic**: Implement exponential backoff for `NetmikoTimeoutException`.
- **Idempotency**: All automation scripts must be safe to run multiple times.

## Multi-Vendor Abstraction

- **Abstraction Layer**: Map generic operations to vendor-specific commands (Cisco IOS vs Juniper Junos vs Arista EOS).
- **Command Syntax**: Account for `show` (Cisco) vs `display` (HP/Aruba) vs `show configuration | display set` (Juniper).

## Safe Configuration Operations

- **Dry-Runs**: Use the `READ_ONLY_COMMANDS` list for all non-destructive discovery.
- **Config Push Pattern**:
    1. Enter configuration mode.
    2. Apply configuration.
    3. Validate with `diff`.
    4. On error: `abort` or `rollback`.
    5. On success: `commit` and verify state.

## Inventory & Templating

- **YAML Inventory**: Use hosts and groups structure for variable inheritance.
- **Jinja2**: Generate configurations using standardized templates.
- **Security**: Use environment variables for credentials; enable SSH key-based authentication where possible.
- **Recovery**: Always create a configuration checkpoint/backup before major changes.
