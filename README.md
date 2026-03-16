# 🏛️ Master Judge LLM

> Two AIs debate. A third one judges. Nobody gets to argue with the verdict.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLMs-black?style=flat)
![Gemma](https://img.shields.io/badge/Gemma-Proponent-green?style=flat)
![Mistral](https://img.shields.io/badge/Mistral-Opponent-red?style=flat)
![Qwen](https://img.shields.io/badge/Qwen-Judge-gold?style=flat)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat)

---

## 📋 Table of Contents
- [About](#about)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 About

This project extends the idea of two LLMs debating by introducing a **third model as an impartial judge**.

Gemma defends a topic. Mistral attacks it. After several rounds of structured argumentation, Qwen reads the entire transcript and delivers a verdict — complete with a winner, a confidence score, and detailed reasoning.

The goal was to explore how LLMs handle role-locked reasoning, adversarial argumentation, and critical evaluation — and whether a third model can reliably judge the quality of arguments made by two others.

---

## ⚙️ How It Works

```
Define a debate topic
        ↓
Gemma (Proponent) — opening argument
        ↓
Mistral (Opponent) — counterargument
        ↓
  [N rounds of rebuttals]
        ↓
Qwen (Judge) reads the full transcript
        ↓
Verdict:
  - Winner
  - Confidence score
  - Reasoning
        ↓
Full debate + verdict saved to results/debate_timestamp.txt
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.11+
- [Ollama](https://ollama.ai) installed locally
- Gemma, Mistral, and Qwen models pulled

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/sharmamimanshi24/LLM-as-a-Judge.git
cd LLM-as-a-Judge
```

**2. Install dependencies**
```bash
pip install ollama
```

**3. Pull all three models**
```bash
ollama pull gemma
ollama pull mistral
ollama pull qwen
```

**4. Make sure Ollama is running**
```bash
ollama serve
```

---

## 🚀 Usage

**1. Set your debate topic and rounds in `masterr.py`:**
```python
topic = "Remote work is better than working from office"
rounds = 3
```

**2. Run the debate:**
```bash
python masterr.py
```

**3. Check the results folder for the full transcript:**
```
results/debate_2025-01-15_14-30-22.txt
```

---

## 📄 Sample Output

```
TOPIC: Remote work is better than working from office

[ROUND 1]
Proponent (Gemma): Remote work eliminates commute time, giving employees
back hours of their lives every week...

Opponent (Mistral): That ignores the collaboration deficit. Spontaneous
hallway conversations drive innovation in ways Slack never will...

[ROUND 2]
...

════════════════════════════════
JUDGE VERDICT (Qwen)
════════════════════════════════
Winner: Proponent (Gemma)
Confidence: 72%
Reasoning: While both models presented structured arguments,
the Proponent consistently backed claims with specific examples
and addressed counterpoints directly. The Opponent relied
heavily on generalizations without sufficient evidence...
```

---

## 📁 Project Structure

```
master_judge_llm/
│
├── masterr.py          # Main script — debate loop + judge evaluation
├── results/
│   └── debate_timestamp.txt   # Auto-saved debate transcripts
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

---

## 📄 License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.

---

## 🆘 Support

- **Issues:** [GitHub Issues](https://github.com/sharmamimanshi24/LLM-as-a-Judge/issues)
- **Email:** sharma.mimanshi24@gmail.com

---

## 👩‍💻 Authors & Acknowledgments

**Mimanshi Sharma**

[![GitHub](https://img.shields.io/badge/GitHub-sharmamimanshi24-181717?style=flat&logo=github)](https://github.com/sharmamimanshi24)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-mimanshi--sharma-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/mimanshi-sharma/)

**Acknowledgments:**
- [Ollama](https://ollama.ai) — for local LLM inference
- [Gemma](https://ai.google.dev/gemma) — Google's open model
- [Mistral AI](https://mistral.ai) — for the Mistral model
- [Qwen](https://huggingface.co/Qwen) — Alibaba's open model used as judge

---

*Built with Ollama · Gemma · Mistral · Qwen · 2025*
