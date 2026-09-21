import json
from datetime import datetime, timezone
from config import (
    EXPERIMENT_ID,
    MODEL_NAME,
    RESULTS_DIRECTORY,
    RESULTS_FILE,
    TEMPERATURE,
)


def create_result_record(
    dilemma,
    parsed_response,
    repetition,
    seed,
):
    decision = parsed_response["decision"]

    return {
        "experiment_id": EXPERIMENT_ID,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": MODEL_NAME,
        "dilemma_id": int(dilemma["dilemma_id"]),
        "file": dilemma["file"],
        "personal_force": dilemma["personal_force"],
        "intentionality": dilemma["intentionality"],
        "repetition": repetition,
        "seed": seed,
        "temperature": TEMPERATURE,
        "decision": decision,
        "utilitarian": 1 if decision == "YES" else 0,
        "justification": parsed_response["justification"],
        "raw_response": parsed_response["raw_response"],
    }


def save_result(record):
    RESULTS_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    with RESULTS_FILE.open(
        "a",
        encoding="utf-8",
    ) as results_file:
        results_file.write(
            json.dumps(
                record,
                ensure_ascii=False,
            )
            + "\n"
        )