# Security Policy

## ⚠️ Critical Security Issues Identified

This repository previously contained **exposed API keys and credentials** that have been partially remediated. If you forked or cloned this repository before the security fixes, please take action immediately.

### Exposed Credentials (Now Removed)

The following credentials were found hardcoded in the repository and have been removed:

1. **OpenAI API Key** - Found in `InvestGen (1).json`
   - Pattern: `sk-proj-*****` (starts with sk-proj-)
   - **Action Required**: This key must be revoked and regenerated at https://platform.openai.com/api-keys

2. **Financial Modeling Prep API Key** - Found in `InvestGen (1).json` and `README`
   - Pattern: Alphanumeric string
   - **Action Required**: Revoke and regenerate at https://financialmodelingprep.com/developer/docs/

3. **Database Credentials** - Found in `README`
   - Default credentials were exposed
   - **Action Required**: Change database passwords if using the default configuration

## 🔒 Security Best Practices

### For Repository Maintainers

1. **Immediately revoke exposed credentials**:
   - OpenAI API key → https://platform.openai.com/api-keys
   - FMP API key → https://financialmodelingprep.com/developer/docs/
   - Change database passwords

2. **Use the sanitization script**:
   ```bash
   python3 sanitize_secrets.py
   ```
   This script removes API keys from the workflow JSON file.

3. **Before committing**:
   ```bash
   # Check for secrets
   grep -r "sk-proj-" . --exclude-dir=.git
   grep -r "api_key.*:" . --exclude-dir=.git | grep -v "your_.*_key"

   # Run sanitization
   python3 sanitize_secrets.py
   ```

4. **Use environment variables**:
   - Never hardcode API keys in source code
   - Use `.env` file (git-ignored) for local development
   - Use secrets management for production (GitHub Secrets, AWS Secrets Manager, etc.)

### For Users

1. **Never use the exposed API keys** - They should be considered compromised

2. **Generate your own API keys**:
   - OpenAI: https://platform.openai.com/api-keys
   - Financial Modeling Prep: https://financialmodelingprep.com/developer/docs/
   - Cohere (optional): https://dashboard.cohere.ai/api-keys

3. **Configure credentials securely**:
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   # .env is automatically ignored by git
   ```

4. **In Langflow UI**:
   - Import the workflow JSON
   - Manually configure API keys in each component
   - Use environment variable references like `${OPENAI_API_KEY}` when possible

## 🛡️ Protected Files

The following files contain or may contain sensitive data and are protected by `.gitignore`:

- `.env` - Environment variables with actual credentials
- `db_config.json` - Database configuration with passwords
- `*.db`, `*.sqlite*` - Local database files
- Any file matching `*secret*`, `*apikey*`, `*api_key*`, `*credentials*`

## 📋 Security Checklist

Before committing code:

- [ ] No API keys in source code
- [ ] No passwords in configuration files
- [ ] `.env` file is not committed (only `.env.example`)
- [ ] Database credentials use environment variables
- [ ] Ran `sanitize_secrets.py` on workflow JSON
- [ ] Reviewed `git diff` for accidental secret exposure

## 🚨 Reporting Security Issues

If you discover a security vulnerability in this repository:

1. **Do NOT open a public issue**
2. Contact the repository maintainers privately
3. Include details about the vulnerability and how to reproduce it
4. Allow reasonable time for the issue to be addressed before public disclosure

## 🔍 Automated Security Scanning

Consider adding these tools to your workflow:

- **git-secrets**: Prevents committing secrets
  ```bash
  git secrets --install
  git secrets --register-aws
  git secrets --add 'sk-[a-zA-Z0-9]{48}'  # OpenAI keys
  ```

- **TruffleHog**: Scans for secrets in git history
  ```bash
  pip install trufflehog
  trufflehog git file://. --json
  ```

- **detect-secrets**: Pre-commit hook for secret detection
  ```bash
  pip install detect-secrets
  detect-secrets scan
  ```

## 📚 Additional Resources

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning)
- [Managing API Keys Securely](https://cloud.google.com/docs/authentication/api-keys)

## ✅ Remediation Status

| Issue | Status | Action Taken |
|-------|--------|--------------|
| Exposed OpenAI API key | ⚠️ Partially Fixed | Removed from code, **must be revoked by owner** |
| Exposed FMP API key | ⚠️ Partially Fixed | Removed from code, **must be revoked by owner** |
| Exposed DB credentials | ✅ Fixed | Removed, documentation updated |
| Missing .gitignore | ✅ Fixed | Added comprehensive .gitignore |
| Missing .env.example | ✅ Fixed | Added template file |
| Poor documentation | ✅ Fixed | Created comprehensive README.md |

---

**Last Updated**: 2024
**Security Contact**: [Create an issue with label 'security']
