# reasoning.py

def generate_reason(candidate, score):

    profile = candidate["profile"]

    exp = profile.get("years_of_experience", 0)

    title = profile.get("current_title", "Professional")

    reasons = []

    reasons.append(f"{exp} years of experience")

    reasons.append(title)

    if score >= 80:
        reasons.append("Strong overall match for the role.")

    elif score >= 60:
        reasons.append("Good technical alignment with some gaps.")

    else:
        reasons.append("Partial match with limited alignment.")

    return ". ".join(reasons)
