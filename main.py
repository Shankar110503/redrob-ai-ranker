import gzip
import json
import pandas as pd

from rank_candidates import rank_candidates


def load_candidates(file_path):
    candidates = []

    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                candidates.append(json.loads(line))

    return candidates


def main():

    INPUT_FILE = "data/candidates.jsonl.gz"
    OUTPUT_FILE = "output/team_shankar.csv"

    print("Loading candidates...")
    candidates = load_candidates(INPUT_FILE)

    print(f"Loaded {len(candidates)} candidates")

    print("Ranking candidates...")
    ranked = rank_candidates(candidates)

    df = pd.DataFrame(ranked)

    df.to_csv(
        OUTPUT_FILE,
        index=False,
        columns=[
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    )

    print("Submission generated successfully.")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()
