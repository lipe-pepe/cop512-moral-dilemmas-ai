from pathlib import Path

METADATA_FILE = Path("dilemmas_metadata.csv")
DILEMMAS_DIRECTORY = Path("dilemmas")
RESULTS_DIRECTORY = Path("results")
RESULTS_FILE = RESULTS_DIRECTORY / "trials.jsonl"
EXPERIMENT_ID = "preliminary_01"

MODEL_NAME = "llama3.2:3b"

NUMBER_OF_DILEMMAS = 2
REPETITIONS = 3
TEMPERATURE = 0.7