# CodePilot

CodePilot is a safety-aware, multi-agent engineering assistant that turns a product brief into a structured plan, architecture tasks, and a generated project workspace.

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

### Deploy publicly

The repository is ready for [Streamlit Community Cloud](https://share.streamlit.io/): select `app.py` as the entrypoint and add `GROQ_API_KEY` plus any `CODEPILOT_*` variables under **Advanced settings → Secrets**. Credentials stay out of the repository.

For self-hosting:

```bash
docker build -t codepilot .
docker run --rm -p 8501:8501 --env-file .env codepilot
```

The same image runs on Render, Railway, Fly.io, or any container platform.

Run tests:

```bash
pytest
```

## Configuration

| Variable | Purpose | Default |
|---|---|---|
| `GROQ_API_KEY` | Groq API credential | required |
| `CODEPILOT_MODEL` | Chat model identifier | `openai/gpt-oss-120b` |
| `CODEPILOT_PROVIDER` | `groq`, `openai-compatible`, or `opencode` | `groq` |
| `CODEPILOT_API_BASE` | OpenAI-compatible API base URL | unset |
| `CODEPILOT_RECURSION_LIMIT` | Maximum graph iterations (10–1000) | `100` |
| `CODEPILOT_DEBUG` | Enable LangChain debug logging | `false` |

Generated files are written under `generated_project/`. Commands run by the agent are bounded to 120 seconds and destructive patterns are rejected.

## Workflows

The dashboard exposes four workflows over the same graph: build a project end to end, create a plan without writing files, review an existing workspace, or explain the architecture. The model provider is selected at startup, so local OpenCode/Ollama-compatible endpoints can be used without changing agent code.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development checks and [SECURITY.md](SECURITY.md) for vulnerability reporting.

## License

MIT
