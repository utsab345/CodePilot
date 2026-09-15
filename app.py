"""Streamlit dashboard for interactive CodePilot runs."""

import streamlit as st

from agent.config import settings
from agent.graph import agent


st.set_page_config(page_title="CodePilot", page_icon="🚀", layout="wide")
st.title("🚀 CodePilot")
st.caption("Turn a product idea into an implementation plan and generated project.")

with st.sidebar:
    st.subheader("Runtime")
    st.code(settings.model, language="text")
    st.caption("Set GROQ_API_KEY in your environment before running.")

prompt = st.text_area(
    "What should CodePilot build?",
    placeholder="Build a production-ready habit tracker with a FastAPI backend and React frontend.",
    height=140,
)

if st.button("Generate project", type="primary", disabled=not prompt.strip()):
    with st.status("Planning and implementing…", expanded=True) as status:
        try:
            result = agent.invoke({"user_prompt": prompt.strip()}, {"recursion_limit": settings.recursion_limit})
            status.update(label="Project generated", state="complete")
            if result.get("plan"):
                st.subheader("Plan")
                st.json(result["plan"].model_dump())
            if result.get("task_plan"):
                st.subheader("Implementation tasks")
                st.json(result["task_plan"].model_dump())
            st.success("Files were written to `generated_project/`.")
        except Exception as exc:  # pragma: no cover - UI error boundary
            status.update(label="Generation failed", state="error")
            st.exception(exc)
