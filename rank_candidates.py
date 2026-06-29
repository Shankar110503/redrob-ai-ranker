from scoring import calculate_score


def rank_candidates(candidates):

    results = []

    for candidate in candidates:

        score, reason = calculate_score(candidate)

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": score,
            "reasoning": reason
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    top100 = results[:100]

    for i, row in enumerate(top100, start=1):
        row["rank"] = i

    return top100
