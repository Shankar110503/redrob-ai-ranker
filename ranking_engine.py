# ranking_engine.py

from feature_engineering import extract_features
from job_matcher import job_match_score


def final_score(candidate):

    features = extract_features(candidate)

    score = 0

    # Experience
    score += min(features["experience"] * 4, 30)

    # Skill Match
    score += features["matched_skills"] * 5

    # JD Match
    jd_score, matched = job_match_score(candidate)

    score += jd_score

    # Behaviour Signals
    score += features["github_score"] * 0.10
    score += features["response_rate"] * 10
    score += features["interview_rate"] * 10
    score += features["profile_score"] * 0.10

    # Education
    score += features["education_score"]

    # Verification
    score += features["verified_email"]
    score += features["verified_phone"]

    # Open to Work
    if features["open_to_work"]:
        score += 5

    # Relocation
    if features["relocation"]:
        score += 3

    return round(score, 2), matched
