
# 🤝 Contributing to AI Code Reviewer & Debugger

First off, thank you for considering contributing to this project! 🎉
Every contribution — bug reports, feature suggestions, documentation, or code — is genuinely appreciated.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Branch Naming Convention](#branch-naming-convention)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Development Setup](#development-setup)
- [Style Guide](#style-guide)

---

## 📜 Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Be kind, constructive, and collaborative at all times.

---

## 💡 How Can I Contribute?

### 🐛 Reporting Bugs
- First, check if the bug has already been reported in [GitHub Issues](https://github.com/ASHUTOSH-KUMAR-RAO/code-reviewer-llm/issues).
- If not, open a new issue using the **Bug Report** template.
- Clearly describe: what happened, what you expected, and steps to reproduce.

### ✨ Suggesting Features
- Use the **Feature Request** template in GitHub Issues.
- Explain why the feature would be useful and how it should work.

### 📝 Improving Documentation
- Spotted something unclear in the README, docstrings, or comments? Send a PR!

### 🔧 Fixing Bugs / Adding Features
- Pick an existing issue or create one first, then follow the workflow below.

---

## 🚀 Getting Started

```bash
# 1. Fork the repo (click "Fork" on GitHub)

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/code-reviewer-llm.git
cd code-reviewer-llm

# 3. Set up Conda environment
conda create -n code-reviewer python=3.9
conda activate code-reviewer

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up environment variables
cp .env.example .env
# Add your GROQ_API_KEY to .env

# 6. Run the app to verify everything works
streamlit run app.py
```

---

## 🌿 Branch Naming Convention

| Type | Format | Example |
|------|--------|---------|
| New Feature | `feature/short-description` | `feature/add-rust-support` |
| Bug Fix | `fix/short-description` | `fix/chat-mode-crash` |
| Documentation | `docs/short-description` | `docs/update-readme` |
| Refactor | `refactor/short-description` | `refactor/llm-chain-cleanup` |

```bash
# Create a new branch
git checkout -b feature/your-amazing-feature
```

---

## ✍️ Commit Message Guidelines

We follow **Conventional Commits**:

```
<type>: <short description>
```

| Type | When to Use |
|------|-------------|
| `feat` | Adding a new feature |
| `fix` | Fixing a bug |
| `docs` | Documentation changes |
| `style` | Formatting only, no logic change |
| `refactor` | Code restructure, no feature/fix |
| `test` | Adding or updating tests |
| `chore` | Build process or dependency updates |

**Examples:**
```bash
git commit -m "feat: add Go language support in translator"
git commit -m "fix: resolve file upload crash for .cpp files"
git commit -m "docs: update installation steps in README"
```

---

## 🔄 Pull Request Process

1. Fork the repo and create your branch (see steps above).
2. Make your changes with meaningful commits.
3. Ensure the app runs correctly:
   ```bash
   streamlit run app.py
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-amazing-feature
   ```
5. Open a **Pull Request** into the `main` branch on GitHub.
6. Fill out the PR template — describe what changed, why, and add screenshots for UI changes.
7. Wait for a review — we'll respond quickly! 😊

---

## 🛠️ Development Setup

### Project Structure (Quick Reference)
```
code-reviewer-app/
├── ui/              ← Streamlit UI components
├── app.py           ← Main entry point
├── prompts.py       ← Prompt templates (add new modes here)
├── llm.py           ← LangChain LCEL chain setup
└── themes.py        ← Dark/Light CSS themes
```

### Want to Add a New Mode?
1. Add a new `PromptTemplate` in `prompts.py`.
2. Add the mode option in `ui/analyze_tab.py`.
3. Test that all existing modes still work correctly.

---

## 🎨 Style Guide

- **Python**: Follow [PEP 8](https://pep8.org/).
- Use **snake_case** for functions and variables.
- Write docstrings for all important functions.
- Do not leave unnecessary commented-out code.
- **Never commit your `.env` file** — keep API keys private!

---

## ❓ Questions?

Feel free to ask anything in [GitHub Issues](https://github.com/ASHUTOSH-KUMAR-RAO/code-reviewer-llm/issues).

---

<center>Made with ❤️ by <a href="https://github.com/ASHUTOSH-KUMAR-RAO">Ashutosh Kumar Rao</a></center>
