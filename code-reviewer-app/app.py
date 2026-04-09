# =============================================================================
# app.py — Main Entry Point
# =============================================================================
# This is the main file that runs the Streamlit app.
# It is intentionally kept short and clean — all logic is in separate modules:
#
#   themes.py          → Theme CSS injection
#   ui/sidebar.py      → Sidebar settings & theme toggle
#   ui/analyze_tab.py  → Analyze Code tab
#   ui/chat_tab.py     → Chat with AI tab
#   prompts.py         → All prompt templates
#   llm.py             → LLM setup and chain runner
#
# Run with:
#   streamlit run app.py
# =============================================================================

import streamlit as st
from themes import apply_theme
from ui.sidebar     import render_sidebar
from ui.analyze_tab import render_analyze_tab
from ui.chat_tab    import render_chat_tab


# =============================================================================
# PAGE CONFIG
# Must be the first Streamlit call in the script.
# =============================================================================

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🛠️",
    layout="wide"
)


# =============================================================================
# SESSION STATE INITIALIZATION
# =============================================================================

def init_session_state():
    """Initialize all required session state variables."""
    defaults = {
        "theme"         : "Dark",
        "chat_history"  : [],
        "last_code"     : "",
        "last_language" : "Python",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# =============================================================================
# HEADER
# =============================================================================

def render_header():
    """Renders the app title, subtitle, and feature badge pills."""
    st.markdown('<div class="main-title">🛠️ AI Code Reviewer & Debugger</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Paste your code or upload a file — let AI do the magic! ✨</div>',
        unsafe_allow_html=True
    )
    badges = [
        "🐛 Bug Finder", "✅ Reviewer", "💡 Explainer",
        "🔧 Auto Fixer", "⚡ Optimizer", "🔒 Security",
        "🌐 Translator", "📝 Test Gen", "💬 Chat Mode"
    ]
    badge_html = " ".join([f'<span class="feature-badge">{b}</span>' for b in badges])
    st.markdown(badge_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Main function — orchestrates the entire app."""
    init_session_state()
    apply_theme()
    settings = render_sidebar()
    render_header()

    tab_analyze, tab_chat = st.tabs(["🔍 Analyze Code", "💬 Chat with AI"])

    with tab_analyze:
        render_analyze_tab(
            mode=settings["mode"],
            language=settings["language"],
            target_language=settings["target_language"]
        )

    with tab_chat:
        render_chat_tab()

    st.markdown("---")
    st.markdown(
        '<center style="color: #6b7280;">Made with ❤️ Ashutosh Kumar Rao</center>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
