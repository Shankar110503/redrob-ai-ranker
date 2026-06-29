# feature_engineering.py

from config import CORE_SKILLS, EDUCATION_SCORE


def extract_features(candidate):

    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    skills = {s["name"].lower() for s in candidate.get("skills", [])}

    matched_skills = 0

    for skill in CORE_SKILLS:
        if skill.lower() in skills:
            matched_skills += 1

    education_score = 0

    if candidate.get("education"):
        tier = candidate["education"][0].get("tier", "unknown")
        education_score = EDUCATION_SCORE.get(tier, 0)

    features = {
        "experience": profile.get("years_of_experience", 0),

        "matched_skills": matched_skills,

        "github_score": signals.get("github_activity_score", -1),

        "response_rate": signals.get("recruiter_response_rate", 0),

        "interview_rate": signals.get("interview_completion_rate", 0),

        "profile_score": signals.get("profile_completeness_score", 0),

        "notice_period": signals.get("notice_period_days", 180),

        "education_score": education_score,

        "open_to_work": int(signals.get("open_to_work_flag", False)),

        "verified_email": int(signals.get("verified_email", False)),

        "verified_phone": int(signals.get("verified_phone", False)),

        "relocation": int(signals.get("willing_to_relocate", False))
    }

    return features
