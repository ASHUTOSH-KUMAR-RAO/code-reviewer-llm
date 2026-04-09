
# =============================================================================
# ui/chat_tab.py — Chat Mode Tab UI Component
# =============================================================================
# This file renders the "Chat with AI" tab of the app.
# It allows users to have a multi-turn conversation with the AI
# about the code they analyzed in the Analyze Code tab.
#
# How it works:
#   1. User first analyzes code in the Analyze tab
#   2. That code is saved in st.session_state.last_code
#   3. In this tab, the user can ask follow-up questions about that code
#   4. Full conversation history is maintained in st.session_state.chat_history
#   5. Each message is sent to the LLM with the code as system context
# =============================================================================

import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from llm import get_llm


# =============================================================================
# SYSTEM PROMPT TEMPLATE
# This is injected as the system message to give the LLM context
# about the user's code before the conversation starts.
# =============================================================================

CHAT_SYSTEM_PROMPT = """
You are an expert code assistant. The user has shared some code with you.
Help them understand, debug, improve, or answer any questions about their code.

Rules:
  - Be concise and clear
  - Use code blocks when showing code examples
  - Reference specific line numbers when relevant
  - If the user asks something unrelated to code, politely redirect them

User's Code ({language}):
{code}
"""


# =============================================================================
# RENDER CHAT TAB
# =============================================================================

def render_chat_tab():
    """
    Renders the full Chat with AI tab UI.

    Requires st.session_state.last_code to be set
    (done automatically when user runs an analysis in the Analyze tab).
    """

    st.markdown("### 💬 Chat with AI about your Code")

    # ── Guard: No code analyzed yet ──────────────────────────
    if not st.session_state.get("last_code"):
        st.info(
            "💡 First analyze some code in the **🔍 Analyze Code** tab, "
            "then come here to ask questions about it!"
        )
        return

    # ── Show which code is loaded ─────────────────────────────
    language = st.session_state.get("last_language", "Code")
    st.success(f"✅ {language} code loaded! Ask anything about it.")

    # ── Render Chat History ───────────────────────────────────
    _render_chat_history()

    # ── Chat Input & Send Button ──────────────────────────────
    _render_chat_input(language)


# =============================================================================
# CHAT HISTORY RENDERER (private helper)
# =============================================================================

def _render_chat_history():
    """
    Renders all previous messages in the chat history
    as styled chat bubbles (user on right style, AI on left style).
    """
    for message in st.session_state.get("chat_history", []):
        if message["role"] == "user":
            st.markdown(
                f'<div class="chat-user">🧑‍💻 <b>You:</b> {message["content"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-ai">🤖 <b>AI:</b><br><br>{message["content"]}</div>',
                unsafe_allow_html=True
            )


# =============================================================================
# CHAT INPUT (private helper)
# =============================================================================

def _render_chat_input(language: str):
    """
    Renders the text input and send button.
    On send, builds the full message history and calls the LLM.

    Args:
        language (str): The programming language of the loaded code.
    """
    user_question = st.text_input(
        label="Ask a question about your code:",
        placeholder="e.g. Why is there a memory leak? How can I fix bug #2?",
    )

    if st.button("📨 Send", use_container_width=True, type="primary"):

        # Validate input
        if not user_question.strip():
            st.warning("⚠️ Please type a question first!")
            return

        with st.spinner("AI is thinking... 🤔"):
            try:
                ai_reply = _call_llm(user_question, language)

                # Save both messages to chat history
                st.session_state.chat_history.append(
                    {"role": "user", "content": user_question}
                )
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": ai_reply}
                )

                # Rerun to show updated chat history
                st.rerun()

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")


# =============================================================================
# LLM CALLER (private helper)
# =============================================================================

def _call_llm(user_question: str, language: str) -> str:
    """
    Builds the full message list (system + history + new question)
    and sends it to the LLM.

    Args:
        user_question (str): The user's latest question.
        language      (str): Programming language for context.

    Returns:
        str: The AI's response as a plain string.
    """
    # Step 1 — Build the system message with code context
    system_content = CHAT_SYSTEM_PROMPT.format(
        language=language,
        code=st.session_state.last_code
    )
    messages = [SystemMessage(content=system_content)]

    # Step 2 — Add full chat history for multi-turn context
    for msg in st.session_state.get("chat_history", []):
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))

    # Step 3 — Add the new user question
    messages.append(HumanMessage(content=user_question))

    # Step 4 — Call LLM and return response
    llm      = get_llm()
    response = llm.invoke(messages)
    return response.content
