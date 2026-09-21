import csv

from config import (
    DILEMMAS_DIRECTORY,
    METADATA_FILE,
)

def load_metadata():
    with METADATA_FILE.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        return list(csv.DictReader(csv_file))


def load_dilemma(filename):
    file_path = DILEMMAS_DIRECTORY / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dilemma file not found: {file_path}"
        )

    return file_path.read_text(
        encoding="utf-8"
    ).strip()