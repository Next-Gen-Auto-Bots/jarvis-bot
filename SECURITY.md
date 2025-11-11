# Security Policy

## Supported Versions

The following versions of Jarvis Bot are currently being supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

We recommend always using the latest stable version for the best security posture.

## Reporting a Vulnerability

### How to Report

If you discover a security vulnerability in Jarvis Bot, please help us by reporting it responsibly:

1. **DO NOT** create a public GitHub issue for security vulnerabilities
2. Email us at: **security@nextgenautobots.com** (or create a private security advisory on GitHub)
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)
   - Your contact information for follow-up

### What to Expect

- **Acknowledgment:** We'll acknowledge receipt within 48 hours
- **Assessment:** We'll assess the vulnerability and determine severity within 5 business days
- **Updates:** We'll provide progress updates at least weekly
- **Resolution:** 
  - **Critical vulnerabilities:** Patch within 7 days
  - **High severity:** Patch within 14 days
  - **Medium/Low severity:** Patch in next scheduled release
- **Credit:** We'll credit you in the security advisory (unless you prefer to remain anonymous)

### Our Commitment

- We'll keep you informed throughout the process
- We'll work with you to understand and reproduce the issue
- We'll notify you when the fix is released
- We'll publicly acknowledge your responsible disclosure (with your permission)

## 🔒 Security Best Practices for Users

### 1. API Key Security

**Critical:** Never expose your API keys!

- ✅ Use `.env` file for local development (never commit it)
- ✅ Use environment variables in production
- ✅ Use secret managers (HashiCorp Vault, AWS Secrets Manager, etc.) for enterprise deployments
- ✅ Rotate keys periodically (monthly recommended)
- ✅ Use different keys for dev/staging/production
- ❌ Never hardcode keys in source code
- ❌ Never commit `.env` to Git (it's in `.gitignore`)
- ❌ Never share keys via chat, email, or screenshots

### 2. Access Control

**Principle:** Least privilege access

- Implement role-based access controls (RBAC) for sensitive commands
- Restrict who can execute `/sms` and `/call` commands
- Monitor logs for unauthorized access attempts
- Use Telegram's chat restrictions and user permissions
- Consider implementing command rate limiting

### 3. Provider Security

**Secure your third-party service accounts:**

#### Twilio Security
- Enable two-factor authentication (2FA)
- Set up IP access control lists
- Configure spending limits
- Monitor usage dashboards regularly
- Enable webhook signature validation

#### OpenAI/DeepSeek Security
- Enable API key restrictions (IP allowlists)
- Set usage limits
- Monitor API usage dashboards
- Rotate keys monthly
- Use separate keys for different environments

#### GitHub Security
- Enable 2FA on your GitHub account
- Use branch protection rules
- Require code review for merges
- Use GitHub Actions secrets (never hardcode)
- Regularly audit repository access

### 4. Billing & Cost Security

**Prevent unexpected charges and billing fraud:**

#### Understand All Costs
- Read [BILLING.md](BILLING.md) to understand what may cost money
- Jarvis Bot itself is free - costs come from third-party services YOU configure
- No hidden charges - you must explicitly set up and use paid services

#### Set Spending Limits
- **Twilio:** Configure account spending limits in console
- **OpenAI:** Set monthly usage limits in account settings
- **GitHub:** Monitor Actions minutes and storage usage

#### Monitor Usage
- Review `logs/requests.json` daily in production
- Set up billing alerts in all service provider accounts
- Use `/stats` command to monitor bot activity
- Check provider dashboards weekly

#### Prevent Unauthorized Usage
- Secure your `.env` file (permissions: 600)
- Implement command-level authentication
- Log all SMS/call attempts with user IDs
- Review logs for suspicious patterns
- Implement rate limiting per user

#### GitHub Billing Specifically
- **Important:** GitHub billing is separate from Jarvis Bot
- Monitor: https://github.com/settings/billing
- GitHub may charge for:
  - GitHub Actions usage (CI/CD)
  - Private repository storage
  - GitHub LFS bandwidth
  - GitHub Packages storage
- Set up billing alerts in GitHub settings
- Review usage reports monthly

### 5. Data Protection

**Protect user data and privacy:**

- **Logs:** Store securely, implement log rotation, redact PII
- **Message Content:** Don't log sensitive information (passwords, credit cards, etc.)
- **User Data:** Minimize collection, encrypt at rest, comply with GDPR/CCPA
- **Transmission:** Use HTTPS for all API calls, verify SSL certificates
- **Retention:** Implement data retention policies, delete old logs

### 6. Secure Deployment

**Production deployment security:**

#### Local/VPS Deployment
- Use systemd for process management
- Run bot as non-root user
- Use firewall rules (ufw, iptables)
- Keep system and dependencies updated
- Implement automatic security updates

#### Container Deployment (Docker/Kubernetes)
- Use official base images
- Scan images for vulnerabilities (Trivy, Snyk)
- Don't run as root in containers
- Use secrets management (Kubernetes Secrets, Docker Secrets)
- Implement network policies
- Regularly update base images

#### Cloud Deployment
- Use managed secrets (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager)
- Implement least privilege IAM roles
- Enable audit logging
- Use VPC/private networking where possible
- Enable encryption at rest and in transit

### 7. Code Security

**Secure coding practices:**

- **Dependencies:** Regularly update dependencies (`pip install -U`)
- **Vulnerability Scanning:** Use tools like `pip-audit`, `safety`, `bandit`
- **Input Validation:** Sanitize all user inputs
- **Error Handling:** Don't expose sensitive info in error messages
- **Logging:** Redact credentials, tokens, and PII from logs
- **Code Review:** Review all changes, especially security-related

### 8. Monitoring & Incident Response

**Be prepared for security incidents:**

#### Monitoring
- Set up alerts for unusual activity
- Monitor API error rates
- Track failed authentication attempts
- Watch for unusual spending patterns
- Use SIEM tools for enterprise deployments

#### Incident Response Plan
1. **Detect:** Identify the security incident
2. **Contain:** Immediately revoke compromised API keys
3. **Investigate:** Review logs to understand scope
4. **Remediate:** Fix the vulnerability, rotate all keys
5. **Notify:** Inform affected users if necessary
6. **Document:** Create post-mortem report
7. **Improve:** Update security practices based on lessons learned

#### Emergency Actions
If you suspect a security breach:
1. **Immediately:** Revoke all API keys (Twilio, OpenAI, DeepSeek)
2. **Stop:** Shut down the bot (`Ctrl+C` or stop systemd service)
3. **Investigate:** Review `logs/requests.json` for suspicious activity
4. **Rotate:** Generate new API keys from all providers
5. **Update:** Change all passwords and enable 2FA
6. **Report:** If user data was compromised, report according to local regulations

## 🛡️ Security Features Built Into Jarvis Bot

### Current Security Features
- ✅ No hardcoded secrets
- ✅ Environment variable configuration
- ✅ `.gitignore` prevents accidental secret commits
- ✅ Structured logging with correlation IDs
- ✅ Request/response logging for audit trails
- ✅ Provider-scoped configuration
- ✅ Input validation for commands
- ✅ Error handling that doesn't leak sensitive info
- ✅ Timeout protections for API calls
- ✅ Modular architecture for security audits

### Planned Security Enhancements
- 🔄 Role-based access control (RBAC)
- 🔄 Command-level authorization
- 🔄 Rate limiting per user
- 🔄 Webhook signature validation
- 🔄 Encrypted log storage
- 🔄 Automated dependency updates (Dependabot)
- 🔄 Regular security scanning in CI/CD

## 📚 Security Resources

### Documentation
- [BILLING.md](BILLING.md) - Cost transparency and billing security
- [FAQ.md](FAQ.md) - Security-related FAQs
- [README.md](README.md) - General security guidelines

### External Resources
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Telegram Bot Security](https://core.telegram.org/bots/faq#security)
- [Twilio Security Best Practices](https://www.twilio.com/docs/usage/security)
- [OpenAI API Security](https://platform.openai.com/docs/guides/safety-best-practices)

### Security Tools
- `pip-audit` - Scan Python dependencies for vulnerabilities
- `bandit` - Python security linter
- `safety` - Check dependencies against security advisories
- `trivy` - Container vulnerability scanner
- `snyk` - Dependency and container scanning

## 📞 Security Contact

- **Email:** security@nextgenautobots.com
- **GitHub Security Advisories:** https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/security/advisories
- **Emergency:** For critical vulnerabilities requiring immediate attention, please use email with "[URGENT]" in the subject line

---

**Remember:** Security is a shared responsibility. We're committed to maintaining a secure bot, and we ask users to follow best practices when deploying and using Jarvis Bot.
