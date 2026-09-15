# Security policy

## Reporting a vulnerability

Please report security issues privately through GitHub’s **Report a vulnerability** feature. Do not publish API keys, generated project secrets, or exploit details in a public issue.

CodePilot writes generated files below `generated_project/`, rejects path traversal, and bounds agent shell commands. These controls reduce accidental damage but are not a replacement for operating the service in an isolated environment.
