from pathlib import Path
from datetime import datetime

METADATA_FILE = Path("dilemmas_metadata.csv")
DILEMMAS_DIRECTORY = Path("dilemmas")

MODEL_NAME = "llama3.2:3b"

NUMBER_OF_DILEMMAS = None
REPETITIONS = 10
TEMPERATURE = 0.7

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

RUN_TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

EXPERIMENT_ID = f"baseline_{RUN_TIMESTAMP}"
RESULTS_PATH = RESULTS_DIR / f"{EXPERIMENT_ID}.jsonl"