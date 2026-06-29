# scoring.py

JD_SKILLS = {
    "Python",
    "Machine Learning",
    "Deep Learning",
    "LLM",
    "NLP",
    "Vector Database",
    "FAISS",
    "Pinecone",
    "Milvus",
    "Weaviate",
    "OpenSearch",
    "Qdrant",
    "Embeddings",
    "Retrieval",
    "Ranking",
    "TensorFlow",
    "PyTorch"
}


def calculate_score(candidate):

    score = 0
    reasons = []

    # Experience
    exp = candidate["profile"].get("years_of_experience", 0)

    if 5 <= exp <= 9:
        score += 30
        reasons.append(f"{exp} years experience")
    elif exp >= 3:
        score += 15

    # Skills
    candidate_skills = {
        s["name"] for s in candidate.get("skills", [])
    }

    matched = JD_SKILLS.intersection(candidate_skills)

    score += len(matched) * 4

    if matched:
        reasons.append(
            "Skills: " + ", ".join(sorted(matched))
        )

    # Behaviour Signals
    signals = candidate.get("redrob_signals", {})

    if signals.get("open_to_work_flag"):
        score += 5

    if signals.get("github_activity_score", -1) > 50:
        score += 8

    if signals.get("recruiter_response_rate", 0) > 0.70:
        score += 8

    if signals.get("interview_completion_rate", 0) > 0.80:
        score += 8

    if signals.get("verified_email"):
        score += 2

    if signals.get("verified_phone"):
        score += 2

    # Relocation
    if signals.get("willing_to_relocate"):
        score += 3

    # Notice Period
    notice = signals.get("notice_period_days", 180)

    if notice <= 30:
        score += 5
    elif notice <= 60:
        score += 3

    reasoning = "; ".join(reasons)

    if reasoning == "":
        reasoning = "Partial profile match."

    return round(score, 2), reasoning
