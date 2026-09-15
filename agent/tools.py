import pathlib
import subprocess
from typing import Tuple

from langchain_core.tools import tool

PROJECT_ROOT = pathlib.Path.cwd() / "generated_project"
MAX_COMMAND_TIMEOUT = 120
BLOCKED_COMMANDS = ("rm -rf", "sudo ", " mkfs", "shutdown", "reboot")


def safe_path_for_project(path: str) -> pathlib.Path:
    p = (PROJECT_ROOT / path).resolve()
    if PROJECT_ROOT.resolve() not in p.parents and PROJECT_ROOT.resolve() != p.parent and PROJECT_ROOT.resolve() != p:
        raise ValueError("Attempt to write outside project root")
    return p


@tool
def write_file(path: str, content: str) -> str:
    """Writes content to a file at the specified path within the project root."""
    p = safe_path_for_project(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return f"WROTE:{p}"


@tool
def read_file(path: str) -> str:
    """Reads content from a file at the specified path within the project root."""
    p = safe_path_for_project(path)
    if not p.exists():
        return ""
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


@tool
def get_current_directory() -> str:
    """Returns the current working directory."""
    return str(PROJECT_ROOT)


@tool
def list_files(directory: str = ".") -> str:
    """Lists all files in the specified directory within the project root."""
    p = safe_path_for_project(directory)
    if not p.is_dir():
        return f"ERROR: {p} is not a directory"
    files = [str(f.relative_to(PROJECT_ROOT)) for f in p.glob("**/*") if f.is_file()]
    return "\n".join(files) if files else "No files found."

@tool
def run_cmd(cmd: str, cwd: str = None, timeout: int = 30) -> Tuple[int, str, str]:
    """Run a bounded shell command inside the generated project workspace."""
    if not cmd.strip():
        return 2, "", "command cannot be empty"
    if any(blocked in cmd.lower() for blocked in BLOCKED_COMMANDS):
        return 126, "", "command rejected by workspace safety policy"
    timeout = max(1, min(timeout, MAX_COMMAND_TIMEOUT))
    cwd_dir = safe_path_for_project(cwd) if cwd else PROJECT_ROOT
    try:
        res = subprocess.run(cmd, shell=True, cwd=str(cwd_dir), capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        return 124, exc.stdout or "", f"command timed out after {timeout}s"
    return res.returncode, res.stdout, res.stderr


@tool
def workspace_summary() -> str:
    """Return a compact inventory of generated files for agent context."""
    files = sorted(f.relative_to(PROJECT_ROOT).as_posix() for f in PROJECT_ROOT.glob("**/*") if f.is_file())
    return "\n".join(files) if files else "No files found."


def init_project_root():
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
    return str(PROJECT_ROOT)
