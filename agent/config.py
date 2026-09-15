"""Runtime configuration for CodePilot."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Configuration loaded from environment variables."""

    model: str = "openai/gpt-oss-120b"
    recursion_limit: int = 100
    debug: bool = False

    @classmethod
    def from_env(cls) -> "Settings":
        """Build settings from environment variables with safe defaults."""
        raw_limit = os.getenv("CODEPILOT_RECURSION_LIMIT", "100")
        try:
            recursion_limit = max(10, min(int(raw_limit), 1000))
        except ValueError:
            recursion_limit = 100
        return cls(
            model=os.getenv("CODEPILOT_MODEL", cls.model),
            recursion_limit=recursion_limit,
            debug=os.getenv("CODEPILOT_DEBUG", "false").lower() in {"1", "true", "yes"},
        )


settings = Settings.from_env()
