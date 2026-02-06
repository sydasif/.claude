# Security Rules (Always-On)

Critical security constraints that must always be followed.

## Core Principles

### 1. Input Validation
- Validate and sanitize ALL user inputs
- Implement proper input length limits
- Use parameterized queries (never string interpolation)
- Escape user-generated content for XSS prevention

### 2. Secret Management
- NEVER commit secrets, API keys, or passwords to repositories
- Store secrets in environment variables or secure vaults
- Use secure random generators for tokens (not pseudo-random)
- Hash passwords with bcrypt, Argon2, or similar

### 3. Secure Coding Practices
- Never use eval/exec with user input
- Use secure XML parsing (prevent XXE)
- Implement proper error handling (don't leak sensitive info)
- Use HTTPS for all communications
- Scan dependencies for vulnerabilities regularly

### 4. File Security
- Validate file types and sizes before accepting uploads
- Store uploads outside web root
- Use proper access controls for sensitive files
- Implement secure file permissions

## Language-Specific Patterns

### Python

```python
# Path Traversal Prevention
safe_path = os.path.normpath(user_input)
if safe_path.startswith("..") or os.path.isabs(safe_path):
    raise ValueError("Path traversal attempt detected")

# Command Injection Prevention
subprocess.run(["ls", user_dir], shell=False)  # NEVER shell=True with user input

# SQL Injection Prevention
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))  # Parameterized
```

## STOP & ASK Triggers

You MUST stop and ask if:
1. You find a security vulnerability in unrelated code
2. You are tempted to bypass existing architecture for "cleaner" code
3. Requirements conflict with security best practices

## Authentication & Authorization
- Implement proper auth mechanisms
- Use industry-standard protocols (OAuth 2.0, OpenID Connect)
- Implement rate limiting
- Use secure session management

## Logging
- Log security events without exposing sensitive data
- Monitor for suspicious activities
- Implement intrusion detection
