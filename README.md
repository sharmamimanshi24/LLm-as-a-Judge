## Master Judge LLM

This project creates a debate between two LLM models. Each model is given a fixed opinion about a topic. They argue with each other for a few turns.
At the end, a **third Master LLM Iisacting as a judge and deciding the winner.**

The goal is to understand how two models stick to their role and give their opinion and show their judgment and critical analysis skills as well.


## How it works

1. A debate topic is defined in the code
2. Model A gives an opening argument
3. Model B responds with a counterargument
4. The models continue rebutting each other for fixed rounds
5. A Master Judge LLM reads the entire transcript
6. The judge declares:
   -Winner
   -Confidence score
   -Reasoning
10. The complete debate is saved automatically in the .txt file


## Models Used

- **Model A (Proponent):** Gemma  
- **Model B (Opponent):** Mistral
- **Model C (Judge):** Qwen
  All models run locally using Ollama)


## Project Structure

```text
  master_judge_llm
│
├── masterr.py
├── results/
│   └── debate_timestamp.txt
└── README.md
