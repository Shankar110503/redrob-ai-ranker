# job_matcher.py

from utils import clean_text

IMPORTANT_KEYWORDS = [
    "python",
    "machine learning",
    "deep learning",
    "llm",
    "embeddings",
    "retrieval",
    "ranking",
    "vector database",
    "pinecone",
    "milvus",
    "weaviate",
    "faiss",
    "qdrant",
    "opensearch",
    "rag",
    "nlp",
    "tensorflow",
    "pytorch",
    "evaluation",
    "production",
]


def job_match_score(candidate):

    profile = candidate.get("profile", {})

    summary = clean_text(profile.get("summary", ""))

    headline = clean_text(profile.get("headline", ""))

    text = headline + " " + summary

    score = 0
    matched = []

    for keyword in IMPORTANT_KEYWORDS:
        if keyword in text:
            score += 5
            matched.append(keyword)

    return score, matched
