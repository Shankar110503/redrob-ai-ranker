# build_submission.py

import pandas as pd


def build_submission(ranked_candidates, output_file):

    rows = []

    for rank, candidate in enumerate(ranked_candidates[:100], start=1):

        rows.append({
            "candidate_id": candidate["candidate_id"],
            "rank": rank,
            "score": round(candidate["score"], 4),
            "reasoning": candidate["reasoning"]
        })

    df = pd.DataFrame(
        rows,
        columns=[
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    )

    df.to_csv(output_file, index=False, encoding="utf-8")

    print(f"Submission saved to: {output_file}")
