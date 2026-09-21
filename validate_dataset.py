import csv
from pathlib import Path

METADATA_FILE = Path("dilemmas_metadata.csv")
DILEMMAS_DIRECTORY = Path("dilemmas")

VALID_PERSONAL_FORCE = {
    "personal",
    "impersonal",
}

VALID_INTENTIONALITY = {
    "instrumental",
    "accidental",
}


def read_metadata():
    with METADATA_FILE.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        return list(csv.DictReader(csv_file))


def validate_metadata(rows):
    errors = []
    dilemma_ids = set()
    metadata_files = set()

    for line_number, row in enumerate(rows, start=2):
        dilemma_id = row["dilemma_id"]
        filename = row["file"]
        personal_force = row["personal_force"]
        intentionality = row["intentionality"]

        if dilemma_id in dilemma_ids:
            errors.append(
                f"Line {line_number}: duplicate dilemma ID "
                f"{dilemma_id}."
            )

        dilemma_ids.add(dilemma_id)
        metadata_files.add(filename)

        file_path = DILEMMAS_DIRECTORY / filename

        if not file_path.exists():
            errors.append(
                f"Line {line_number}: file not found: "
                f"{file_path}"
            )

        if personal_force not in VALID_PERSONAL_FORCE:
            errors.append(
                f"Line {line_number}: invalid personal_force: "
                f"{personal_force}"
            )

        if intentionality not in VALID_INTENTIONALITY:
            errors.append(
                f"Line {line_number}: invalid intentionality: "
                f"{intentionality}"
            )

    directory_files = {
        file_path.name
        for file_path in DILEMMAS_DIRECTORY.glob("*.txt")
    }

    missing_from_metadata = directory_files - metadata_files

    for filename in sorted(missing_from_metadata):
        errors.append(
            f"File exists in the directory but not in the CSV: "
            f"{filename}"
        )

    return errors


def main():
    rows = read_metadata()
    errors = validate_metadata(rows)

    print(f"Dilemmas in metadata: {len(rows)}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s):\n")

        for error in errors:
            print(f"- {error}")

        raise SystemExit(1)

    print("Dataset validation completed successfully.")


if __name__ == "__main__":
    main()