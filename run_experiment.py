from config import (
    NUMBER_OF_DILEMMAS,
    REPETITIONS,
)
from dataset import (
    load_dilemma,
    load_metadata,
)
from prompts import build_prompt
from model import (
    generate_response,
    parse_response,
)
from results import (
    create_result_record,
    save_result,
)

def main():
    dilemmas = load_metadata()
    selected_dilemmas = dilemmas[:NUMBER_OF_DILEMMAS]

    print(f"Total dilemmas available: {len(dilemmas)}")
    print(f"Dilemmas selected: {len(selected_dilemmas)}")
    print(f"Repetitions per dilemma: {REPETITIONS}")

    for dilemma in selected_dilemmas:
        dilemma_text = load_dilemma(dilemma["file"])
        prompt = build_prompt(dilemma_text)

        for repetition in range(1, REPETITIONS + 1):
            seed = repetition

            print(
                f"\nDilemma {dilemma['dilemma_id']} | "
                f"Repetition {repetition}/{REPETITIONS}"
            )

            raw_response = generate_response(
                prompt=prompt,
                seed=seed,
            )

            parsed_response = parse_response(
                raw_response
            )

            result_record = create_result_record(
                dilemma=dilemma,
                parsed_response=parsed_response,
                repetition=repetition,
                seed=seed,
            )

            save_result(result_record)

            print(
                f"Decision: "
                f"{parsed_response['decision']}"
            )

if __name__ == "__main__":
    main()