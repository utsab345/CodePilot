from agent.config import Settings


def test_settings_use_safe_defaults(monkeypatch):
    monkeypatch.delenv("CODEPILOT_MODEL", raising=False)
    monkeypatch.delenv("CODEPILOT_PROVIDER", raising=False)
    monkeypatch.delenv("CODEPILOT_RECURSION_LIMIT", raising=False)
    settings = Settings.from_env()
    assert settings.provider == "groq"
    assert settings.recursion_limit == 100


def test_settings_bound_invalid_recursion_limit(monkeypatch):
    monkeypatch.setenv("CODEPILOT_RECURSION_LIMIT", "999999")
    assert Settings.from_env().recursion_limit == 1000
    monkeypatch.setenv("CODEPILOT_RECURSION_LIMIT", "invalid")
    assert Settings.from_env().recursion_limit == 100
