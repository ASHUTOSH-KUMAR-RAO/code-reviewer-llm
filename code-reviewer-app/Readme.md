
# 🛠️ AI Code Reviewer & Debugger

> **Paste your code → Get bugs found, fixed, explained & optimized — instantly!**
> Powered by **LangChain (LCEL)** + **ChatGroq (Llama3 70B)**

---

## ✨ Features

### 🔍 Core Features

| Feature | Description |
|---|---|
| 🐛 **Bug Finder** | Code paste karo, saare bugs automatically detect ho jaate hain |
| ✅ **Code Reviewer** | Best practices & code quality check with actionable suggestions |
| 💡 **Code Explainer** | Line-by-line explanation in simple, human-friendly language |
| 🔧 **Auto Fixer** | Buggy code in → Clean fixed code out |
| ⚡ **Code Optimizer** | Slow or messy code → Faster, cleaner version |

### 🌟 Cool Add-ons

- 🌐 **Multi-Language Support** — Python, JavaScript, Java, C++, and more
- 📊 **Severity Levels** — Every bug tagged as `Low` / `Medium` / `High`
- 📋 **Review Report** — A clean, organized report with all findings

---

## 🏗️ Architecture

```
PromptTemplate  |  ChatGroq (Llama3-70B)  |  StrOutputParser
      ↓                    ↓                       ↓
  Code + Mode         AI Analysis             Clean Output
```

This project uses **LangChain Expression Language (LCEL)** to chain components in a simple, readable pipeline:

```python
chain = prompt | llm | output_parser
result = chain.invoke({"code": user_code, "mode": selected_mode})
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python >= 3.9
```

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/ASHUTOSH-KUMAR-RAO/code-reviewer-llm
cd code-reviewer-app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Add your GROQ_API_KEY in .env
```

### Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your free Groq API key at [console.groq.com](https://console.groq.com)

---

## 💻 Usage

```bash
# Run the app
python app.py
```

Then paste your code and choose a mode:

```
Select Mode:
  1. 🐛 Bug Finder
  2. ✅ Code Reviewer
  3. 💡 Code Explainer
  4. 🔧 Auto Fixer
  5. ⚡ Code Optimizer
```

---

## 🧱 Project Structure

```
code-reviewer-app/
│
├── app.py                  # Main entry point — LCEL chain + all logic
├── requirements.txt        # Project dependencies
├── .env                    # API keys (NOT pushed to GitHub)
├── .gitignore              # Ignores .env and other sensitive files
└── README.md               # Project documentation
```

---

## 📦 Tech Stack

| Tool | Purpose |
|---|---|
| [LangChain](https://langchain.com) | LCEL Chain orchestration |
| [ChatGroq](https://console.groq.com) | LLM API (Llama3 70B) |
| [Python](https://python.org) | Core language |
| `StrOutputParser` | Clean text output from LLM |

---

## 📋 Sample Output

```
============================================================
📋 CODE REVIEW REPORT
============================================================
Language  : Python
Mode      : Bug Finder
------------------------------------------------------------

🔴 [HIGH]   Line 12 — Undefined variable 'reslt' (possible typo: 'result')
🟡 [MEDIUM] Line 27 — Division by zero risk if 'n' is 0
🟢 [LOW]    Line 5  — Unused import 'os'

------------------------------------------------------------
✅ 3 issue(s) found | 0 critical errors
============================================================
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Made with ❤️ by **[Ashutosh Kumar Rao](https://github.com/ASHUTOSH-KUMAR-RAO)**

> *"Good code is its own best documentation."* — Steve McConnell
