# Security Best Practices

This document contains centralized security best practices to be referenced by various skills and agents.

## General Security Principles

### 1. Input Validation and Sanitization
- Validate and sanitize all user inputs using libraries like `validators` or custom validation
- Implement proper input length limits to prevent buffer overflow attacks
- Use parameterized queries or ORM to prevent SQL injection
- Use `html.escape()` when displaying user-generated content to prevent XSS

### 2. Secret Management
- Never commit secrets, API keys, or passwords to code repositories
- Store secrets in environment variables, secure vaults, or use libraries like `python-dotenv` with proper `.gitignore`
- Use secure random generators for tokens: `secrets` module instead of `random`
- Hash passwords with bcrypt, Argon2, or similar: `bcrypt.hashpw(password.encode(), bcrypt.gensalt())`

### 3. Dependency Security
- Regularly update dependencies and scan for vulnerabilities with tools like `safety` or `pip-audit`
- Verify the authenticity of third-party packages before installation
- Limit the scope of dependencies to only what's needed

### 4. Authentication and Authorization
- Implement proper authentication and authorization mechanisms
- Use industry-standard protocols like OAuth 2.0 or OpenID Connect
- Implement rate limiting to prevent abuse
- Use secure session management

### 5. Secure Coding Practices
- Avoid using `eval()`, `exec()`, or `compile()` with user input
- Use `defusedxml` instead of standard XML libraries to prevent XXE attacks
- Implement proper error handling that doesn't leak sensitive information
- Use HTTPS for all communications

### 6. File and Resource Security
- Validate file types and sizes before accepting uploads
- Store uploaded files outside the web root
- Implement proper access controls for sensitive files
- Use secure file permissions

### 7. Logging and Monitoring
- Log security-relevant events without exposing sensitive data
- Monitor for suspicious activities
- Implement intrusion detection mechanisms
- Regular security audits

## Language-Specific Security Guidelines

### Python Security
- Insecure deserialization (pickle) with untrusted data
- Using `input()` or similar functions without validation in production
- Importing modules from untrusted sources
- Direct use of `eval()`, `exec()`, or `compile()` with user input
- Unsanitized input in SQL queries

### Web Application Security
- Cross-site scripting (XSS)
- Cross-site request forgery (CSRF)
- Session hijacking
- Clickjacking
- Insecure direct object references

## Security Testing
- Perform regular penetration testing
- Conduct code reviews with security focus
- Use automated security scanning tools
- Implement security-focused unit tests
- Regular vulnerability assessments

## Incident Response
- Have a documented incident response plan
- Implement proper backup and recovery procedures
- Establish communication channels for security incidents
- Regular security training for team members