# Contributing to CodePilot

1. Create a virtual environment and install development dependencies with `pip install -e '.[dev]'`.
2. Make focused changes with tests where behavior changes.
3. Run `ruff check .` and `pytest -q` before opening a pull request.
4. Describe the user-facing behavior and include configuration changes in the PR description.

Keep secrets in environment variables or Streamlit secrets. Never commit `.env`, generated workspaces, or API keys.
