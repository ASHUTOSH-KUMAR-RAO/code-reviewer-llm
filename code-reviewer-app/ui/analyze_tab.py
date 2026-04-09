# =============================================================================
# ui/analyze_tab.py — Analyze Code Tab UI Component
# =============================================================================
# This file renders the "Analyze Code" tab of the app.
# It handles:
#   - File upload (.py, .js, .cpp etc.)
#   - Code text area (paste code manually)
#   - Analyze button
#   - Displaying the AI result in a styled card
#   - Download report button
# =============================================================================

import streamlit as st
from llm import run_chain


# =============================================================================
# RENDER ANALYZE TAB
# =============================================================================

def render_analyze_tab(mode: str, language: str, target_language: str):
    """
    Renders the full Analyze Code tab UI.

    Args:
        mode            (str): Selected mode (e.g. "Bug Finder").
        language        (str): Programming language of the code.
        target_language (str): Target language (only for Code Translator).
    """

    # Split into two columns — Input on left, Result on right
    col_input, col_result = st.columns([1, 1], gap="large")

    # ── LEFT COLUMN — Code Input ──────────────────────────────
    with col_input:
        st.markdown("### 📋 Input")

        code_input = _get_code_input(language)
        analyze_clicked = st.button(
            "🚀 Analyze Code",
            use_container_width=True,
            type="primary"
        )

    # ── RIGHT COLUMN — Result Display ─────────────────────────
    with col_result:
        st.markdown("### 📊 Result")

        if analyze_clicked:
            _run_analysis(
                code=code_input,
                mode=mode,
                language=language,
                target_language=target_language
            )
        else:
            st.info("👈 Paste your code on the left and click **Analyze Code**!")


# =============================================================================
# CODE INPUT (private helper)
# =============================================================================

def _get_code_input(language: str) -> str:
    """
    Renders file upload and text area for code input.
    File upload takes priority over the text area if a file is uploaded.

    Args:
        language (str): Used for syntax highlighting in preview.

    Returns:
        str: The code entered by the user (from file or text area).
    """

    # File uploader — supports common code file extensions
    uploaded_file = st.file_uploader(
        label="📁 Upload a code file",
        type=["py", "js", "ts", "java", "cpp", "c", "go", "rs", "php", "rb", "txt"],
        help="Upload a code file directly instead of pasting."
    )

    if uploaded_file is not None:
        # Read uploaded file content
        code = uploaded_file.read().decode("utf-8")
        st.success(f"✅ File uploaded: `{uploaded_file.name}`")
        st.code(code, language=language.lower(), line_numbers=True)
        return code

    # Fallback — manual text area
    code = st.text_area(
        label=f"Paste your {language} code here:",
        height=320,
        placeholder="# Paste your code here...",
    )
    return code


# =============================================================================
# RUN ANALYSIS (private helper)
# =============================================================================

def _run_analysis(code: str, mode: str, language: str, target_language: str):
    """
    Validates input, runs the LCEL chain, and displays the result.

    Args:
        code            (str): The code to analyze.
        mode            (str): Selected analysis mode.
        language        (str): Programming language.
        target_language (str): Target language (for Translator mode).
    """
    import os

    # ── Input Validation ──────────────────────────────────────
    if not code or not code.strip():
        st.warning("⚠️ Please paste or upload some code first!")
        return

    if not os.getenv("GROQ_API_KEY"):
        st.error("❌ GROQ_API_KEY not found! Please check your .env file.")
        return

    # ── Run Chain ─────────────────────────────────────────────
    with st.spinner(f"Running {mode}... ⏳"):
        try:
            result = run_chain(
                mode=mode,
                code=code,
                language=language,
                target_language=target_language
            )

            # Save code to session state for Chat Mode
            st.session_state.last_code     = code
            st.session_state.last_language = language

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            return

    # ── Display Result ────────────────────────────────────────
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown(f"#### {mode} Report")
    st.markdown(result)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Download Button ───────────────────────────────────────
    st.download_button(
        label="📥 Download Report",
        data=result,
        file_name="code_review_report.txt",
        mime="text/plain",
        use_container_width=True
    )
