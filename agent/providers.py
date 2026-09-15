"""Provider factory for Groq and OpenAI-compatible model endpoints."""

from langchain_core.language_models import BaseChatModel
from langchain_groq import ChatGroq

from agent.config import settings


def create_chat_model() -> BaseChatModel:
    """Create the configured chat model without coupling the graph to one vendor."""
    if settings.provider == "groq":
        return ChatGroq(model=settings.model)
    if settings.provider in {"openai", "openai-compatible", "opencode"}:
        from langchain_openai import ChatOpenAI

        kwargs = {"model": settings.model}
        if settings.api_base:
            kwargs["base_url"] = settings.api_base
        return ChatOpenAI(**kwargs)
    raise ValueError(f"Unsupported CODEPILOT_PROVIDER: {settings.provider}")
