
# 📋 Changelog

All notable changes to **AI Code Reviewer & Debugger** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]
> Upcoming features and fixes will be listed here.

- [ ] GitHub Copilot-style inline suggestions
- [ ] Support for more file types (`.ts`, `.rb`, `.swift`)
- [ ] Multi-file upload support

---

## [1.0.0] - 2025-01-01

### 🎉 Initial Release

#### ✨ Added
- **Bug Finder** mode — detects all bugs with severity levels in a clean table
- **Code Reviewer** mode — best practices and code quality analysis
- **Code Explainer** mode — line-by-line explanation in simple language
- **Auto Fixer** mode — buggy code in → fixed code out
- **Code Optimizer** mode — transforms slow/messy code into faster, cleaner version
- **Security Checker** mode — detects SQL Injection, XSS, hardcoded keys, and more
- **Code Translator** mode — converts code between any two programming languages
- **Test Case Generator** mode — auto-generates unit tests for pytest, Jest, and JUnit
- **File Upload** support — `.py`, `.js`, `.cpp`, `.java`, and more
- **Chat Mode** — converse with AI about your code
- **Dark / Light Theme** toggle
- **Download Report** feature — save results as `.txt`
- **Multi-language support** — Python, JS, Java, C++, Go, Rust, PHP & more
- LangChain **LCEL Chain** integration (`prompt | llm | output_parser`)
- **Groq (GPT-OSS-120B)** as the AI backbone
- **Streamlit** based clean and responsive UI
- `.env.example` for easy environment setup
- GitHub Issue Templates — Bug Report & Feature Request
- Pull Request template

#### 🏗️ Architecture
- Modular UI structure under `ui/` directory
- Separate `prompts.py` for all prompt templates
- Centralized `llm.py` for LangChain chain setup
- `themes.py` for Dark/Light CSS theming

---

## Versioning Legend

| Symbol | Meaning |
|--------|---------|
| ✨ Added | New features |
| 🔧 Fixed | Bug fixes |
| ♻️ Changed | Changes to existing features |
| 🗑️ Removed | Removed features |
| 🔒 Security | Security improvements |
| ⚠️ Deprecated | Soon-to-be removed features |

---

<center>Made with ❤️ by <a href="https://github.com/ASHUTOSH-KUMAR-RAO">Ashutosh Kumar Rao</a></center>
