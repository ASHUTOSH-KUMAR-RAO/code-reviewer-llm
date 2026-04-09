# 🛠️ AI Code Reviewer & Debugger

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.56-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-GPT--OSS--120B-F55036?style=for-the-badge&logo=groq&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)

> **Paste your code or upload a file → Get bugs found, fixed, explained, secured & optimized — instantly!**
> Powered by **LangChain (LCEL)** + **Groq (GPT-OSS-120B)** + **Streamlit**

---

## ✨ Features

### 🔍 Core Modes
| Mode | Description |
|---|---|
| 🐛 **Bug Finder** | Finds all bugs with severity levels in a clean table |
| ✅ **Code Reviewer** | Best practices & code quality check |
| 💡 **Code Explainer** | Line-by-line explanation in simple language |
| 🔧 **Auto Fixer** | Buggy code in → Fixed code out |
| ⚡ **Code Optimizer** | Slow/messy code → Faster, cleaner version |
| 🔒 **Security Checker** | SQL Injection, XSS, hardcoded keys & more |
| 🌐 **Code Translator** | Convert code between any two languages |
| 📝 **Test Case Generator** | Auto unit tests — pytest, Jest, JUnit |

### 🌟 UI Features
- 📁 **File Upload** — `.py`, `.js`, `.cpp`, `.java` and more
- 💬 **Chat Mode** — Converse with AI about your code
- 🌙 **Dark / 🟢 Light Theme** — Toggle anytime
- 📥 **Download Report** — Save results as `.txt`
- 💻 **Multi-Language** — Python, JS, Java, C++, Go, Rust, PHP & more

---

## 🏗️ Architecture

```
PromptTemplate  |  ChatGroq (GPT-OSS-120B)  |  StrOutputParser
      ↓                      ↓                       ↓
  Code + Mode           AI Analysis             Clean Output
```

**LCEL Chain:**
```python
chain = prompt | llm | output_parser
result = chain.invoke({"code": user_code, "language": language})
```

---

## 🧱 Project Structure

```
code-reviewer-app/
│
├── .github/                        # GitHub specific files
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md           # Bug report template
│   │   └── feature_request.md      # Feature request template
│   └── pull_request_template.md    # PR template
│
├── ui/                             # Streamlit UI components
│   ├── __init__.py
│   ├── sidebar.py                  # Sidebar settings & theme toggle
│   ├── analyze_tab.py              # Analyze Code tab
│   └── chat_tab.py                 # Chat Mode tab
│
├── app.py                          # Main entry point
├── prompts.py                      # All prompt templates
├── llm.py                          # LLM & LCEL chain setup
├── themes.py                       # Dark/Light theme CSS
├── requirements.txt                # Project dependencies
├── .env                            # API keys (NOT pushed to GitHub)
├── .env.example                    # API key template
├── .gitignore                      # Git ignore rules
├── LICENSE                         # MIT License
├── CONTRIBUTING.md                 # Contribution guide
├── CHANGELOG.md                    # Version history
└── README.md                       # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Groq API Key (free at [console.groq.com](https://console.groq.com))

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/ASHUTOSH-KUMAR-RAO/code-reviewer-llm.git
cd code-reviewer-llm

# 2. Create & activate conda environment
conda create -n code-reviewer python=3.9
conda activate code-reviewer

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment variables
cp .env.example .env
# Add your GROQ_API_KEY in .env
```

### Environment Variables

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your free API key at [console.groq.com](https://console.groq.com)

---

## 💻 Usage

```bash
streamlit run app.py
```

App will open at `http://localhost:8501` 🌐

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repo
2. Create your branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Ashutosh Kumar Rao**

[![GitHub](https://img.shields.io/badge/GitHub-ASHUTOSH--KUMAR--RAO-181717?style=for-the-badge&logo=github)](https://github.com/ASHUTOSH-KUMAR-RAO)

---

<center>Made with ❤️ Ashutosh Kumar Rao</center>
