# Contributing to InvestGen

Thank you for your interest in contributing to InvestGen! This document provides guidelines and best practices for contributing.

## 🔒 Security First

**CRITICAL**: Before making any commits, read [SECURITY.md](SECURITY.md) to understand our security policies.

### Pre-Commit Checklist

- [ ] No API keys or secrets in code
- [ ] No hardcoded passwords or credentials
- [ ] Environment variables used for sensitive data
- [ ] `.env` file not committed (use `.env.example` as template)
- [ ] Ran `sanitize_secrets.py` if modifying workflow JSON
- [ ] Reviewed `git diff` for accidental exposures

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/InvestGen.git
   cd InvestGen
   ```

3. **Set up your environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt

   # Configure credentials
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to custom components
- Keep functions focused and single-purpose

### Langflow Components

When creating new components:

```python
from langflow.custom import Component
from langflow.io import MessageTextInput, SecretStrInput, Output
from langflow.schema import Data

class YourComponent(Component):
    display_name = "Your Component Name"
    description = "Clear description of what it does"
    icon = "📊"  # Choose an appropriate emoji

    inputs = [
        MessageTextInput(
            name="input_field",
            display_name="Input Field",
            info="Help text for users"
        ),
        SecretStrInput(
            name="api_key",
            display_name="API Key",
            info="Never hardcode - use environment variables!"
        ),
    ]

    outputs = [
        Output(
            display_name="Output Name",
            name="output_field",
            method="process_data"
        ),
    ]

    def process_data(self) -> Data:
        # Your logic here
        result = {"key": "value"}
        return Data(data=result)
```

### Security Requirements

1. **Never hardcode secrets**:
   ```python
   # ❌ BAD
   api_key = "sk-proj-abc123..."

   # ✅ GOOD
   import os
   api_key = os.getenv("OPENAI_API_KEY")
   ```

2. **Use environment variables**:
   ```python
   from dotenv import load_dotenv
   load_dotenv()  # Load .env file
   ```

3. **Validate inputs**:
   ```python
   if not api_key:
       raise ValueError("API key not configured")
   ```

### Database Operations

- Use SQLAlchemy for database operations
- Use parameterized queries to prevent SQL injection
- Handle connection errors gracefully
- Close connections properly (use context managers)

Example:
```python
from sqlalchemy import create_engine
import os

def get_engine():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL not configured")
    return create_engine(db_url)

with get_engine().connect() as conn:
    # Your database operations
    pass
```

## 🧪 Testing

### Manual Testing

1. Import your modified workflow into Langflow
2. Test each component individually
3. Test the complete workflow end-to-end
4. Verify error handling with invalid inputs

### Test Cases to Cover

- [ ] Valid inputs produce expected outputs
- [ ] Invalid inputs raise appropriate errors
- [ ] API rate limits are handled gracefully
- [ ] Database operations succeed and fail gracefully
- [ ] Environment variables are properly loaded

## 📤 Submitting Changes

### Commit Messages

Use clear, descriptive commit messages:

```
Add semantic routing for investment queries

- Implemented route matching for stock analysis
- Added fallback for unrecognized queries
- Updated documentation

Fixes #123
```

### Pull Request Process

1. **Update documentation** if you've changed functionality
2. **Test your changes** thoroughly
3. **Run security check**:
   ```bash
   python3 sanitize_secrets.py
   git diff  # Review changes carefully
   ```

4. **Create pull request** with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots/examples if applicable
   - Security checklist completed

5. **Respond to feedback** from maintainers

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Security fix

## Testing
Describe how you tested your changes

## Security Checklist
- [ ] No API keys or secrets committed
- [ ] Used environment variables for sensitive data
- [ ] Ran sanitize_secrets.py
- [ ] Reviewed git diff for sensitive data

## Related Issues
Closes #(issue number)
```

## 🐛 Reporting Bugs

When reporting bugs, include:

1. **Description**: What happened vs. what you expected
2. **Steps to reproduce**: Detailed steps
3. **Environment**: OS, Python version, Langflow version
4. **Logs**: Relevant error messages (redact any sensitive info!)
5. **Screenshots**: If applicable

## 💡 Feature Requests

For feature requests:

1. Check if it's already been requested
2. Clearly describe the use case
3. Explain why it would be useful
4. Provide examples if possible

## 📚 Documentation

Documentation improvements are always welcome!

- Fix typos or unclear instructions
- Add examples and use cases
- Improve setup guides
- Add troubleshooting tips

## ❓ Questions?

- Check existing issues and discussions
- Review the README.md and documentation
- Open a new issue with the "question" label

## 🙏 Thank You!

Your contributions make InvestGen better for everyone. We appreciate your time and effort!

---

**Remember**: Security is everyone's responsibility. When in doubt, ask!
