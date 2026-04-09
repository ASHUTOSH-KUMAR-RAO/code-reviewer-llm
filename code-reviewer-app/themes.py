# =============================================================================
# themes.py — Dark and Light Theme Configuration
# =============================================================================
# This file handles all the visual theming of the app.
# It defines color palettes for Dark and Light modes,
# and returns the CSS string that Streamlit injects into the page.
# =============================================================================

import streamlit as st


# =============================================================================
# COLOR PALETTES
# Each theme is a dictionary of color variables used across the app.
# =============================================================================

DARK_THEME = {
    "bg"      : "#080c14",   # Deeper almost-black with blue hint
    "card"    : "#0f1729",   # Blue-navy card — clear separation
    "text"    : "#e6edf3",   # Crisp soft white
    "subtext" : "#8b949e",   # Warmer muted gray
    "accent"  : "#6366f1",   # Indigo/violet — modern & unique
    "border"  : "#1e3a5f",   # Blue-tinted border — premium glow feel
}

LIGHT_THEME = {
    "bg"      : "#f0fdf9",   # Soft sea-green white — cleaner feel
    "card"    : "#ccfbf1",   # Teal tinted card — well defined
    "text"    : "#0f4c3a",   # Deep green — high contrast & readable
    "subtext" : "#5f7b72",   # Muted teal-gray
    "accent"  : "#0d9488",   # Vibrant teal accent
    "border"  : "#99f6e4",   # Clean teal border
}


# =============================================================================
# THEME GETTER
# =============================================================================

def get_theme_colors() -> dict:
    """
    Returns the color palette for the currently active theme.

    Reads from st.session_state.theme which is set by the sidebar toggle.

    Returns:
        dict: Color palette with keys: bg, card, text, subtext, accent, border
    """
    if st.session_state.get("theme", "Dark") == "Dark":
        return DARK_THEME
    return LIGHT_THEME


# =============================================================================
# CSS INJECTOR
# =============================================================================

def apply_theme():
    """
    Injects the theme CSS into the Streamlit app using st.markdown.

    This function should be called once at the top of app.py,
    after session state is initialized.

    It styles:
      - App background
      - Sidebar background
      - Page title gradient
      - Subtitle text
      - Feature badge pills
      - Result card container
      - Chat bubbles (user and AI)
    """
    c = get_theme_colors()  # Get current theme colors

    css = f"""
    <style>

    /* ── Global App Background ── */
    .stApp {{
        background-color: {c['bg']};
        color: {c['text']};
    }}

    /* ── Sidebar Background ── */
    div[data-testid="stSidebar"] {{
        background-color: {c['card']};
    }}

    /* ── Gradient Title ── */
    .main-title {{
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, {c['accent']}, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }}

    /* ── Subtitle Text ── */
    .subtitle {{
        color: {c['subtext']};
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }}

    /* ── Feature Badge Pills ── */
    .feature-badge {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        background: {c['accent']}22;
        color: {c['accent']};
        font-size: 0.8rem;
        font-weight: 600;
        margin: 2px;
        border: 1px solid {c['accent']}44;
    }}

    /* ── Result Card Container ── */
    .result-card {{
        background: {c['card']};
        border: 1px solid {c['border']};
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }}

    /* ── Chat Bubble — User ── */
    .chat-user {{
        background: {c['accent']}22;
        border-radius: 12px 12px 4px 12px;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        color: {c['text']};
        border-left: 3px solid {c['accent']};
    }}

    /* ── Chat Bubble — AI ── */
    .chat-ai {{
        background: {c['card']};
        border-radius: 12px 12px 12px 4px;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        color: {c['text']};
        border: 1px solid {c['border']};
    }}

    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
