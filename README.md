# CodePilot

CodePilot is a safety-aware, multi-agent engineering assistant that turns a product brief into a structured plan, architecture tasks, and a generated project workspace.

## Why this is a senior-level project

- **Planner → architect → coder pipeline** implemented with LangGraph.
- **Typed contracts** between agents using Pydantic models.
- **CLI and Streamlit dashboard** for automation and interactive use.
- **Configurable model/runtime** through environment variables.
- **Workspace sandboxing** that prevents path traversal and limits command execution time.
- **Regression tests** for security boundaries and command timeouts.

## Architecture

```text
User brief ──> Planner (Plan) ──> Architect (TaskPlan) ──> Coder ──> generated_project/
                                                        └── tools: read/write/list/run
```

## Quick start

```bash
git clone https://github.com/utsab345/CodePilot.git
cd CodePilot
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
# Edit .env and set GROQ_API_KEY
```

Run from the terminal:

```bash
python main.py --prompt "Build a FastAPI task manager with a React frontend"
```

Run the dashboard:

```bash
streamlit run app.py
```

Run tests:

```bash
pytest
```

## Configuration

| Variable | Purpose | Default |
|---|---|---|
| `GROQ_API_KEY` | Groq API credential | required |
| `CODEPILOT_MODEL` | Chat model identifier | `openai/gpt-oss-120b` |
| `CODEPILOT_RECURSION_LIMIT` | Maximum graph iterations (10–1000) | `100` |
| `CODEPILOT_DEBUG` | Enable LangChain debug logging | `false` |

Generated files are written under `generated_project/`. Commands run by the agent are bounded to 120 seconds and destructive patterns are rejected.

## CV-ready summary

> Built CodePilot, a typed LangGraph multi-agent system that converts natural-language product briefs into architecture plans and generated code. Added a Streamlit dashboard, configurable model runtime, workspace path isolation, bounded command execution, and automated security regression tests.

## License

MIT
