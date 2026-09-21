from ollama import chat
import json
from config import (
    MODEL_NAME,
    TEMPERATURE,
)


def generate_response(prompt, seed):
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        format="json",
        options={
            "temperature": TEMPERATURE,
            "seed": seed,
        },
    )

    return response.message.content

def parse_response(raw_response):
    data = json.loads(raw_response)

    decision = data.get("decision", "").strip().upper()
    justification = data.get("justification", "").strip()

    if decision not in {"YES", "NO"}:
        raise ValueError(
            f"Invalid decision returned by model: {decision}"
        )

    if not justification:
        raise ValueError(
            "The model returned an empty justification."
        )

    return {
        "decision": decision,
        "justification": justification,
        "raw_response": raw_response,
    }