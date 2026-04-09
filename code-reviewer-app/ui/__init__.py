
# =============================================================================
# ui/__init__.py
# =============================================================================
# This file makes the `ui` directory a Python package.
# It exposes the main render functions for clean imports in app.py.
#
# Usage in app.py:
#   from ui.sidebar      import render_sidebar
#   from ui.analyze_tab  import render_analyze_tab
#   from ui.chat_tab     import render_chat_tab
# =============================================================================

from ui.sidebar      import render_sidebar
from ui.analyze_tab  import render_analyze_tab
from ui.chat_tab     import render_chat_tab

__all__ = [
    "render_sidebar",
    "render_analyze_tab",
    "render_chat_tab",
]
