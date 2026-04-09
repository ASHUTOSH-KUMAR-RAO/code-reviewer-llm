# =============================================================================
# ui/sidebar.py — Sidebar UI Component
# =============================================================================
# This file renders the sidebar of the app.
# It handles:
#   - Dark / Light theme toggle
#   - Mode selection (Bug Finder, Reviewer, etc.)
#   - Language selection
#   - Target language (only for Code Translator)
#   - Model info display
#   - Clear chat history button
# =============================================================================

import streamlit as st
from prompts import PROMPT_MAP


# =============================================================================
# RENDER SIDEBAR
# =============================================================================

def render_sidebar() -> dict:
    """
    Renders the sidebar and returns the user's selected settings.

    Returns:
        dict: {
            "mode"            : str  — Selected analysis mode,
            "language"        : str  — Selected programming language,
            "target_language" : str  — Target language (only for Translator),
        }
    """

    with st.sidebar:
        st.markdown("## ⚙️ Settings")

        # ── Theme Toggle ──────────────────────────────────────
        _render_theme_toggle()
        st.markdown("---")

        # ── Mode Selection ────────────────────────────────────
        mode = st.selectbox(
            label="🎯 Select Mode",
            options=list(PROMPT_MAP.keys()),
            help="Choose what you want the AI to do with your code."
        )

        # ── Language Selection ────────────────────────────────
        language = st.selectbox(
            label="💻 Programming Language",
            options=[
                "Python", "JavaScript", "TypeScript",
                "Java", "C++", "C", "Go", "Rust",
                "PHP", "Ruby", "Other"
            ],
            help="Select the language your code is written in."
        )

        # ── Target Language (only for Code Translator) ────────
        target_language = None
        if mode == "🌐 Code Translator":
            target_language = st.selectbox(
                label="🔁 Translate To",
                options=[
                    "JavaScript", "Python", "TypeScript",
                    "Java", "C++", "Go", "Rust", "PHP"
                ],
                help="Select the language you want to translate your code into."
            )

        # ── Model Info ────────────────────────────────────────
        st.markdown("---")
        st.markdown("**Model:** GPT-OSS 120B via Groq ⚡")
        st.markdown("**Chain:** LangChain LCEL")

        # ── Clear Chat Button ─────────────────────────────────
        st.markdown("---")
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    return {
        "mode"            : mode,
        "language"        : language,
        "target_language" : target_language,
    }


# =============================================================================
# THEME TOGGLE (private helper)
# =============================================================================

def _render_theme_toggle():
    """
    Renders the Dark / Light mode toggle buttons in the sidebar.
    Updates st.session_state.theme on click and triggers a rerun.
    """
    col_dark, col_light = st.columns(2)

    with col_dark:
        if st.button(
            "🌙 Dark",
            use_container_width=True,
            type="primary" if st.session_state.theme == "Dark" else "secondary"
        ):
            st.session_state.theme = "Dark"
            st.rerun()

    with col_light:
        if st.button(
            "☀️ Light",
            use_container_width=True,
            type="primary" if st.session_state.theme == "Light" else "secondary"
        ):
            st.session_state.theme = "Light"
            st.rerun()
