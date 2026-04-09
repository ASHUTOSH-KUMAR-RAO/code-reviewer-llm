import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

# ── Load API Key ──────────────────────────────────────────────
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🛠️",
    layout="wide"
)

# ── Session State ─────────────────────────────────────────────
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_code" not in st.session_state:
    st.session_state.last_code = ""
if "last_language" not in st.session_state:
    st.session_state.last_language = "Python"

# ── Theme CSS ─────────────────────────────────────────────────
if st.session_state.theme == "Dark":
    bg = "#0e1117"
    card = "#1e2130"
    text = "#ffffff"
    accent = "#4f8ef7"
    border = "#2e3250"
else:
    bg = "#ecfdf5"
    card = "#d1fae5"
    text = "#064e3b"
    accent = "#059669"
    border = "#6ee7b7"

st.markdown(f"""
<style>
    .stApp {{ background-color: {bg}; color: {text}; }}
    .main-title {{
        font-size: 2.2rem; font-weight: 800;
        background: linear-gradient(90deg, {accent}, #a855f7);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }}
    .subtitle {{ color: {'#9ca3af' if st.session_state.theme == 'Dark' else '#6b7280'}; font-size: 1rem; margin-bottom: 1.5rem; }}
    .feature-badge {{
        display: inline-block; padding: 4px 12px; border-radius: 20px;
        background: {accent}22; color: {accent};
        font-size: 0.8rem; font-weight: 600; margin: 2px;
        border: 1px solid {accent}44;
    }}
    .result-card {{
        background: {card}; border: 1px solid {border};
        border-radius: 12px; padding: 1.5rem; margin-top: 1rem;
    }}
    .chat-user {{
        background: {accent}22; border-radius: 12px 12px 4px 12px;
        padding: 0.8rem 1rem; margin: 0.5rem 0; color: {text};
        border-left: 3px solid {accent};
    }}
    .chat-ai {{
        background: {card}; border-radius: 12px 12px 12px 4px;
        padding: 0.8rem 1rem; margin: 0.5rem 0; color: {text};
        border: 1px solid {border};
    }}
    div[data-testid="stSidebar"] {{ background-color: {card}; }}
</style>
""", unsafe_allow_html=True)

# ── Prompt Templates ──────────────────────────────────────────
PROMPTS = {
    "🐛 Bug Finder": """
You are an expert software debugger.
Analyze the following {language} code and find ALL bugs.
For each bug, mention line number, description, and severity: Low / Medium / High.
Format your response as a clean markdown table with columns: #, Line(s), Bug Description, Severity.

Code:
{code}
""",
    "✅ Code Reviewer": """
You are a senior software engineer doing a code review.
Review the following {language} code for best practices, code quality, readability, and improvements.
Give structured, constructive feedback.

Code:
{code}
""",
    "💡 Code Explainer": """
You are a coding tutor. Explain the following {language} code in simple language.
Go block by block. Assume the reader is a beginner.

Code:
{code}
""",
    "🔧 Auto Fixer": """
You are an expert programmer. Fix ALL bugs in the following {language} code.
Return:
1. List of what was fixed
2. Complete fixed code in a code block

Code:
{code}
""",
    "⚡ Code Optimizer": """
You are a performance expert. Optimize the following {language} code for speed, readability, and best practices.
Return:
1. What was optimized and why
2. Complete optimized code in a code block

Code:
{code}
""",
    "🔒 Security Checker": """
You are a cybersecurity expert specializing in code security.
Analyze the following {language} code for security vulnerabilities including:
- SQL Injection, XSS, Buffer Overflow
- Hardcoded credentials or API keys
- Insecure dependencies or functions
- Any other security issues

For each vulnerability, provide type, line number, risk level (Low/Medium/High/Critical), and how to fix it.
Format as a clean markdown table. If no issues found, confirm the code is secure.

Code:
{code}
""",
    "🌐 Code Translator": """
You are an expert polyglot programmer.
Translate the following {language} code to {target_language}.
Make sure the translated code is idiomatic, well-commented, and follows {target_language} best practices.
Return the complete translated code in a code block.

Code:
{code}
""",
    "📝 Test Case Generator": """
You are a software testing expert.
Generate comprehensive unit tests for the following {language} code.
Include: normal cases, edge cases, error/exception cases, boundary value tests.
Use the appropriate testing framework for {language} (pytest for Python, Jest for JS, JUnit for Java).
Return complete, runnable test code in a code block.

Code:
{code}
"""
}

CHAT_SYSTEM = """You are an expert code assistant. The user has shared some code with you.
Help them understand, debug, improve, or answer any questions about their code.
Be concise, clear, and helpful. Use code blocks when showing code examples.

User's Code ({language}):
{code}
"""

# ── LLM ──────────────────────────────────────────────────────
def get_llm():
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model="openai/gpt-oss-120b",
        temperature=0.2
    )

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    # Theme Toggle
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌙 Dark", use_container_width=True,
                     type="primary" if st.session_state.theme == "Dark" else "secondary"):
            st.session_state.theme = "Dark"
            st.rerun()
    with col2:
        if st.button("☀️ Light", use_container_width=True,
                     type="primary" if st.session_state.theme == "Light" else "secondary"):
            st.session_state.theme = "Light"
            st.rerun()

    st.markdown("---")

    mode = st.selectbox("🎯 Select Mode", list(PROMPTS.keys()))

    language = st.selectbox("💻 Programming Language",
        ["Python", "JavaScript", "TypeScript", "Java", "C++", "C", "Go", "Rust", "PHP", "Ruby", "Other"])

    target_language = None
    if mode == "🌐 Code Translator":
        target_language = st.selectbox("🔁 Translate To",
            ["JavaScript", "Python", "TypeScript", "Java", "C++", "Go", "Rust", "PHP"])

    st.markdown("---")
    st.markdown("**Model:** GPT-OSS 120B via Groq ⚡")
    st.markdown("**Chain:** LangChain LCEL")

    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# ── Header ────────────────────────────────────────────────────
st.markdown('<div class="main-title">🛠️ AI Code Reviewer & Debugger</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Paste your code or upload a file — let AI do the magic! ✨</div>', unsafe_allow_html=True)

badges = ["🐛 Bug Finder", "✅ Reviewer", "🔒 Security", "🌐 Translator", "📝 Test Gen", "💬 Chat Mode"]
st.markdown(" ".join([f'<span class="feature-badge">{b}</span>' for b in badges]), unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["🔍 Analyze Code", "💬 Chat with AI"])

# ════════════════════════════════════════════
# TAB 1 — Analyze Code
# ════════════════════════════════════════════
with tab1:
    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown("### 📋 Input")

        uploaded_file = st.file_uploader(
            "📁 Upload a code file",
            type=["py", "js", "ts", "java", "cpp", "c", "go", "rs", "php", "rb", "txt"],
            help="Upload your code file directly!"
        )

        if uploaded_file:
            code_input = uploaded_file.read().decode("utf-8")
            st.success(f"✅ File uploaded: `{uploaded_file.name}`")
            st.code(code_input, language=language.lower(), line_numbers=True)
        else:
            code_input = st.text_area(
                f"Paste your {language} code here:",
                height=320,
                placeholder="# Paste your code here...",
            )

        analyze_btn = st.button("🚀 Analyze Code", use_container_width=True, type="primary")

    with col_right:
        st.markdown("### 📊 Result")

        if analyze_btn:
            if not code_input or not code_input.strip():
                st.warning("⚠️ Please paste or upload some code first!")
            elif not GROQ_API_KEY:
                st.error("❌ GROQ_API_KEY not found in .env file!")
            else:
                with st.spinner(f"Running {mode}... ⏳"):
                    try:
                        if mode == "🌐 Code Translator":
                            prompt = PromptTemplate(
                                input_variables=["code", "language", "target_language"],
                                template=PROMPTS[mode]
                            )
                            chain = prompt | get_llm() | StrOutputParser()
                            result = chain.invoke({
                                "code": code_input,
                                "language": language,
                                "target_language": target_language
                            })
                        else:
                            prompt = PromptTemplate(
                                input_variables=["code", "language"],
                                template=PROMPTS[mode]
                            )
                            chain = prompt | get_llm() | StrOutputParser()
                            result = chain.invoke({
                                "code": code_input,
                                "language": language
                            })

                        # Save for chat
                        st.session_state.last_code = code_input
                        st.session_state.last_language = language

                        st.markdown('<div class="result-card">', unsafe_allow_html=True)
                        st.markdown(f"#### {mode} Report")
                        st.markdown(result)
                        st.markdown('</div>', unsafe_allow_html=True)

                        st.download_button(
                            label="📥 Download Report",
                            data=result,
                            file_name="code_review_report.txt",
                            mime="text/plain",
                            use_container_width=True
                        )

                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
        else:
            st.info("👈 Paste your code on the left and click **Analyze Code**!")

# ════════════════════════════════════════════
# TAB 2 — Chat Mode
# ════════════════════════════════════════════
with tab2:
    st.markdown("### 💬 Chat with AI about your Code")

    if not st.session_state.last_code:
        st.info("💡 First analyze some code in the **🔍 Analyze Code** tab, then come here to chat!")
    else:
        st.success(f"✅ Code loaded! Ask anything about your {st.session_state.last_language} code.")

        # Display chat history
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-user">🧑‍💻 <b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-ai">🤖 <b>AI:</b><br><br>{msg["content"]}</div>', unsafe_allow_html=True)

        user_question = st.text_input(
            "Ask a question about your code:",
            placeholder="e.g. Why is there a memory leak? How can I fix bug #2?",
        )

        if st.button("📨 Send", use_container_width=True, type="primary"):
            if user_question.strip():
                with st.spinner("AI is thinking... 🤔"):
                    try:
                        system_msg = SystemMessage(content=CHAT_SYSTEM.format(
                            language=st.session_state.last_language,
                            code=st.session_state.last_code
                        ))

                        lc_messages = [system_msg]
                        for m in st.session_state.chat_history:
                            if m["role"] == "user":
                                lc_messages.append(HumanMessage(content=m["content"]))
                            else:
                                lc_messages.append(AIMessage(content=m["content"]))
                        lc_messages.append(HumanMessage(content=user_question))

                        response = get_llm().invoke(lc_messages)
                        ai_reply = response.content

                        st.session_state.chat_history.append({"role": "user", "content": user_question})
                        st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})

                        st.rerun()

                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<center style="color: #6b7280;">Made with ❤️ Ashutosh Kumar rao</center>',
    unsafe_allow_html=True
)
