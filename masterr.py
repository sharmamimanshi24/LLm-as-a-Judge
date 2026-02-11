import json
import time
import urllib.request
import os
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================

OLLAMA_URL = "http://localhost:11434/api/generate"

DEBATER_A_MODEL = "gemma3:12b"            # Dalai Lama
DEBATER_B_MODEL = "mistral-nemo:latest"   # Elon Musk
JUDGE_MODEL = "qwen2.5:1.5b-instruct-fp16"

TOPIC = "Is happiness achieved through detachment or achievement?"
MAX_TURNS = 6

# =====================================================
# OLLAMA CALL
# =====================================================

def query_ollama(model, prompt, temperature=0.7):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature}
    }

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())

    return result["response"].strip()

# =====================================================
# SAVE RESULTS (MUST BE BEFORE run_debate)
# =====================================================

def save_results(topic, conversation, decision_text):
    os.makedirs("results", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/debate_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=====================================\n")
        f.write("DEBATE TRANSCRIPT\n")
        f.write("=====================================\n\n")

        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Topic: {topic}\n\n")

        f.write("---------- Debate ----------\n\n")

        for line in conversation:
            f.write(line + "\n\n")

        f.write("---------- Final Judgment ----------\n\n")
        f.write(decision_text + "\n")

    print(f"\nResults saved to {filename}\n")


# =====================================================
# PROMPT BUILDERS
# =====================================================

def build_debater_prompt(stance, conversation):
    return f"""
You are a competitive debater.

Debate topic:
{TOPIC}

Your fixed stance:
{stance}

Recent conversation:
{conversation}

Rules:
- Defend your stance strongly.
- Directly rebut the opponent.
- Max 50 words.
- Keep the language simple.
- No meta commentary.
Respond only with your argument.
"""

def build_judge_prompt(conversation):
    return f"""
You are a neutral judge.

Debate topic:
{TOPIC}

Full debate transcript:
{conversation}

Decide the winner.

Respond STRICTLY in this format:

Winner: Dalai Lama or Elon Musk or Draw
Confidence: <number between 0.0 and 1.0>
Reasoning: <short explanation>
"""

# =====================================================
# MAIN ENGINE
# =====================================================

def run_debate():
    print("\n" + TOPIC.upper() + "\n")

    conversation = []
    current_speaker = "Dalai Lama"

    for turn in range(MAX_TURNS):
        print(f"--- Turn {turn + 1} ---")

        if current_speaker == "Dalai Lama":
            model = DEBATER_A_MODEL
            stance = "Happiness is achieved through detachment."
        else:
            model = DEBATER_B_MODEL
            stance = "Happiness is achieved through achievement."

        prompt = build_debater_prompt(
            stance,
            "\n".join(conversation[-4:])
        )

        argument = query_ollama(model, prompt)

        message = f"[Debater {current_speaker}] {argument}"
        print(message + "\n")

        conversation.append(message)

        # Switch speaker
        current_speaker = (
            "Elon Musk"
            if current_speaker == "Dalai Lama"
            else "Dalai Lama"
        )

        time.sleep(0.5)

    # ============================
    # FINAL JUDGMENT
    # ============================

    print("\n⚖ FINAL JUDGMENT ⚖\n")

    judge_prompt = build_judge_prompt("\n".join(conversation))
    decision = query_ollama(JUDGE_MODEL, judge_prompt, temperature=0.2)

    print(decision)

    save_results(TOPIC, conversation, decision)

    print("\nDebate complete.\n")

# =====================================================
# ENTRY POINT
# =====================================================

if __name__ == "__main__":
    run_debate()

