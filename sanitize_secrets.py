#!/usr/bin/env python3
"""
Script to remove exposed API keys and secrets from the InvestGen workflow JSON file.
This should be run before committing to ensure no sensitive data is leaked.
"""

import json
import re
import sys

def sanitize_secrets(obj):
    """
    Recursively remove API keys and secrets from a JSON object.
    """
    secrets_removed = []

    if isinstance(obj, dict):
        for key, value in obj.items():
            # Check for known secret field names
            if key in ['openai_api_key', 'cohere_api_key', 'api_key', 'password', 'db_password']:
                if isinstance(value, str) and value:
                    secrets_removed.append(f"Cleared {key}: {value[:10]}...")
                    obj[key] = ''

            # Check for 'value' fields that contain secrets
            elif key == 'value' and isinstance(value, str):
                # OpenAI API keys
                if value.startswith('sk-proj-') or value.startswith('sk-'):
                    secrets_removed.append(f"Cleared OpenAI key: {value[:15]}...")
                    obj[key] = ''
                # Generic API keys (alphanumeric, 20+ chars)
                elif len(value) > 20 and re.match(r'^[a-zA-Z0-9]+$', value):
                    secrets_removed.append(f"Cleared API key: {value[:10]}...")
                    obj[key] = ''
            else:
                # Recurse into nested structures
                child_secrets = sanitize_secrets(value)
                secrets_removed.extend(child_secrets)

    elif isinstance(obj, list):
        for item in obj:
            child_secrets = sanitize_secrets(item)
            secrets_removed.extend(child_secrets)

    return secrets_removed

def main():
    json_file = '/home/runner/work/InvestGen/InvestGen/InvestGen (1).json'

    print(f"Loading {json_file}...")
    with open(json_file, 'r') as f:
        data = json.load(f)

    print("Sanitizing secrets...")
    secrets_removed = sanitize_secrets(data)

    if secrets_removed:
        print(f"\n✓ Removed {len(secrets_removed)} secrets:")
        for secret in secrets_removed[:5]:  # Show first 5
            print(f"  - {secret}")
        if len(secrets_removed) > 5:
            print(f"  ... and {len(secrets_removed) - 5} more")
    else:
        print("✓ No secrets found (file already clean)")

    print(f"\nWriting sanitized file...")
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

    print("✓ Done! File has been sanitized.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
