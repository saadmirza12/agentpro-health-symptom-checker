# AgentPro Health Symptom Checker 🩺🤖

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![AgentPro](https://img.shields.io/badge/AgentPro-v0.1-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Try%20on-Hugging%20Face-blue?logo=huggingface&logoColor=yellow)](https://huggingface.co/spaces/saadmirza12/agentpro-health-symptom-checker)

---

A multi-agent AI assistant that **analyzes your health symptoms** and provides likely causes and safe advice using [AgentPro](https://github.com/traversaal-ai/AgentPro) and OpenAI GPT models.

---

## 🚀 Features

- **Multi-agent reasoning**: Each AI agent specializes in a sub-task (symptom checking, advice, etc.)
- **Transparent logic**: Step-by-step reasoning and "Final Answer" explanations.
- **Powered by OpenAI GPT**: State-of-the-art language models for accurate, relevant responses.
- **Secure**: No API keys stored in code or git history.
- **Easy setup**: Run on any modern PC with Python.

---

## 🚀 Live Demo

- [Try the app live on Hugging Face Spaces!](https://huggingface.co/spaces/saadmirza12/agentpro-health-symptom-checker)

## 🛠️ Setup

**Clone the repository:**
```bash
git clone https://github.com/saadmirza12/agentpro-health-symptom-checker.git
cd agentpro-health-symptom-checker

Install dependencies:
pip install -r requirements.txt

🚦 Usage
Run the assistant:
python main.py

Enter your OpenAI API key when prompted (never hardcode it!).

Type your symptoms when asked.

Receive a stepwise diagnosis and practical advice.

🔒 Security
No API keys or secrets are stored or pushed to GitHub.

Always enter your OpenAI API key when prompted, or set it as an environment variable.

Use .gitignore to keep secrets, cache, and IDE files out of your repo.

🩺 Troubleshooting
Error: “Push declined due to repository rule violations”

You may have committed an API key by mistake.
See GitHub's secret scanning guide and remove the secret from history before pushing again.

Module not found:

Run pip install -r requirements.txt

Python not found:

Make sure Python 3.8+ is installed and on your PATH.

Other issues:

Open an Issue or contact the author.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change or add.

🙏 Credits
AgentPro for multi-agent orchestration.

OpenAI GPT for LLM-powered reasoning.

VS Code for a great development experience.

