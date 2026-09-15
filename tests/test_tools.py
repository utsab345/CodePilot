from agent.tools import run_cmd, safe_path_for_project


def test_safe_path_rejects_workspace_escape():
    try:
        safe_path_for_project("../../secrets.txt")
    except ValueError:
        pass
    else:
        raise AssertionError("workspace escape was not rejected")


def test_run_cmd_rejects_destructive_commands():
    code, _, error = run_cmd.invoke({"cmd": "rm -rf generated_project"})
    assert code == 126
    assert "safety policy" in error


def test_run_cmd_times_out_cleanly():
    code, _, error = run_cmd.invoke({"cmd": "python3 -c 'import time; time.sleep(1)'", "timeout": 1})
    assert code == 124
    assert "timed out" in error
