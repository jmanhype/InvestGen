# ⚠️ CRITICAL: Workflow JSON Contains Exposed Credentials

## Immediate Action Required

The file `InvestGen (1).json` contains **hardcoded API keys** that must be removed before this repository can be considered secure.

### Exposed Credentials Detected

1. **OpenAI API Key**: Pattern `sk-proj-*` found in JSON
2. **Financial Modeling Prep API Key**: Alphanumeric key found in JSON

### Required Actions

#### For Repository Owner (URGENT)

1. **Revoke the exposed API keys immediately**:
   - OpenAI: https://platform.openai.com/api-keys
   - Financial Modeling Prep: https://financialmodelingprep.com/developer/docs/

2. **Generate new API keys** with restricted permissions

3. **Sanitize the workflow JSON**:
   ```bash
   # Option 1: Use the provided script
   python3 sanitize_secrets.py

   # Option 2: Manual edit
   # Open InvestGen (1).json in an editor
   # Search for "sk-proj-" and replace with empty string ""
   # Search for long alphanumeric strings in api_key fields
   # Replace all with empty strings ""
   ```

4. **Verify secrets are removed**:
   ```bash
   # Should return 0 results
   grep -i "sk-proj-" "InvestGen (1).json"
   grep -o "[a-zA-Z0-9]{32}" "InvestGen (1).json" | head
   ```

5. **Commit the sanitized file**:
   ```bash
   git add "InvestGen (1).json"
   git commit -m "security: Remove exposed API keys from workflow JSON"
   ```

#### For Users/Contributors

**DO NOT use any API keys found in this repository!** They are compromised.

1. Generate your own API keys from the respective providers
2. Configure them using environment variables (see `.env.example`)
3. Never commit API keys to version control

### Why This Matters

Exposed API keys can lead to:

- **Unauthorized usage** of your API quotas
- **Unexpected charges** on your accounts
- **Data breaches** if keys have excessive permissions
- **Service abuse** by malicious actors

### Prevention

Going forward:

1. ✅ Use `.env` files for local development (git-ignored)
2. ✅ Use environment variables in Langflow components
3. ✅ Run `sanitize_secrets.py` before committing workflow changes
4. ✅ Review `git diff` carefully before pushing
5. ✅ Enable GitHub secret scanning
6. ✅ Use pre-commit hooks to catch secrets

### Automated Remediation Script

The `sanitize_secrets.py` script will:

- Scan `InvestGen (1).json` for known secret patterns
- Replace API keys with empty strings
- Preserve the workflow structure
- Report what was found and removed

**Run it like this**:
```bash
python3 sanitize_secrets.py
```

### Manual Remediation

If you prefer to manually edit the JSON:

1. Open `InvestGen (1).json` in a text editor
2. Search for these patterns:
   - `"value": "sk-proj-` (OpenAI keys)
   - `"value": "356f` (FMP key example)
   - Any field named `api_key`, `openai_api_key`, `password` with non-empty values
3. Replace the value strings with empty strings: `""`
4. Save the file
5. Verify: `git diff "InvestGen (1).json"`

### Verification Checklist

Before considering this issue resolved:

- [ ] Old API keys have been revoked at the provider
- [ ] New API keys have been generated
- [ ] `InvestGen (1).json` contains no hardcoded secrets
- [ ] `.env.example` shows proper configuration template
- [ ] `.gitignore` prevents `.env` from being committed
- [ ] Documentation explains secure credential management

### Questions?

See [SECURITY.md](SECURITY.md) for more information on security policies and best practices.

---

**This is a critical security issue. Please address it immediately.**
