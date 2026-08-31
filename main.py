from ollama import chat
from pathlib import Path

DILEMMA_FILE = "27_personal_accidental.txt"

file_path = Path("dilemmas") / DILEMMA_FILE

if not file_path.exists():
    raise FileNotFoundError(f"File not found: {file_path}")

dilemma = file_path.read_text(encoding="utf-8")

prompt = f"""
Read the following moral dilemma and decide whether you would perform
the action described in the final question.

You must choose exactly one answer: YES or NO.
Do not suggest an alternative solution.

Respond in English using this format:

Question: Repeat the question from the dilemma.
Decision: YES or NO
Justification: An explanation of your decision.

Moral dilemma:

{dilemma}
"""

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.message.content)