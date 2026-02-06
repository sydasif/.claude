# Security Best Practices

This document contains centralized security best practices to be referenced by various skills and agents.

## General Security Principles

### 1. Input Validation and Sanitization

- Validate and sanitize all user inputs
- Implement proper input length limits to prevent buffer overflow attacks
- Use parameterized queries or ORM to prevent SQL injection (see Database Guidelines)
- Escape user-generated content to prevent XSS

### 2. Secret Management

- Never commit secrets, API keys, or passwords to code repositories
- Store secrets in environment variables or secure vaults
- Use secure random generators for tokens (not pseudo-random)
- Hash passwords with bcrypt, Argon2, or similar

For language-specific implementations, see [Python Guidelines](~/.claude/shared/python.md).

### 3. Dependency Security

- Regularly update dependencies and scan for vulnerabilities
- Verify the authenticity of third-party packages before installation
- Limit the scope of dependencies to only what's needed

### 4. Authentication and Authorization

- Implement proper authentication and authorization mechanisms
- Use industry-standard protocols like OAuth 2.0 or OpenID Connect
- Implement rate limiting to prevent abuse
- Use secure session management

### 5. Secure Coding Practices

- Avoid dynamic code execution with user input (eval, exec)
- Use secure XML parsing libraries to prevent XXE attacks
- Implement proper error handling that doesn't leak sensitive information
- Use HTTPS for all communications

For language-specific secure coding practices, see [Python Guidelines](~/.claude/shared/python.md).

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

For Python-specific security guidelines and examples, see [Python Guidelines](~/.claude/shared/python.md).

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
