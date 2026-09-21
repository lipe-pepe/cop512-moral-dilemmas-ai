import json
import sys
from pathlib import Path


def load_results(results_path):
    results = []

    with results_path.open("r", encoding="utf-8") as results_file:
        for line in results_file:
            line = line.strip()

            if line:
                results.append(json.loads(line))

    return results


def calculate_group_statistics(results, personal_force):
    group_results = [
        result
        for result in results
        if result["personal_force"] == personal_force
    ]

    total = len(group_results)

    utilitarian_count = sum(
        result["utilitarian"]
        for result in group_results
    )

    utilitarian_rate = (
        utilitarian_count / total
        if total > 0
        else 0
    )

    return {
        "total": total,
        "utilitarian_count": utilitarian_count,
        "utilitarian_rate": utilitarian_rate,
    }


def print_group(name, statistics):
    print(f"\nGroup: {name}")
    print(f'Total responses: {statistics["total"]}')
    print(
        "Utilitarian responses: "
        f'{statistics["utilitarian_count"]}'
    )
    print(
        "Utilitarian rate: "
        f'{statistics["utilitarian_rate"]:.2%}'
    )


def main():
    if len(sys.argv) != 2:
        print(
            "Usage: python analyze_results.py "
            "<results_file>"
        )
        sys.exit(1)

    results_path = Path(sys.argv[1])

    if not results_path.exists():
        print(f"Results file not found: {results_path}")
        sys.exit(1)

    results = load_results(results_path)

    personal = calculate_group_statistics(
        results,
        "personal",
    )

    impersonal = calculate_group_statistics(
        results,
        "impersonal",
    )

    difference = (
        impersonal["utilitarian_rate"]
        - personal["utilitarian_rate"]
    )

    print(f"Results file: {results_path}")
    print(f"Total results loaded: {len(results)}")

    print_group("personal", personal)
    print_group("impersonal", impersonal)

    print("\nHypothesis comparison")
    print(
        "H0: personal and impersonal dilemmas produce "
        "the same utilitarian response rate."
    )
    print(
        "H1: personal dilemmas produce a lower "
        "utilitarian response rate."
    )

    print(
        "\nObserved difference "
        "(impersonal - personal): "
        f"{difference:.2%}"
    )

    if personal["utilitarian_rate"] < impersonal["utilitarian_rate"]:
        print(
            "Preliminary result: the observed difference "
            "is in the direction predicted by H1."
        )
    elif personal["utilitarian_rate"] == impersonal["utilitarian_rate"]:
        print(
            "Preliminary result: no difference was observed "
            "between the groups."
        )
    else:
        print(
            "Preliminary result: the observed difference "
            "is opposite to the direction predicted by H1."
        )

    print(
        "This is a descriptive result; statistical "
        "significance was not tested."
    )


if __name__ == "__main__":
    main()