# config.py

# File Paths
INPUT_FILE = "data/candidates.jsonl.gz"
OUTPUT_FILE = "output/team_shankar.csv"

# Job Description
JOB_TITLE = "Senior AI Engineer"

# Experience
MIN_EXPERIENCE = 5
MAX_EXPERIENCE = 9

# Preferred Locations
PREFERRED_LOCATIONS = [
    "Pune",
    "Noida",
    "Bangalore",
    "Hyderabad",
    "Chennai"
]

# Core Skills
CORE_SKILLS = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "LLM",
    "NLP",
    "PyTorch",
    "TensorFlow",
    "Embeddings",
    "Retrieval",
    "Ranking",
    "FAISS",
    "Milvus",
    "Qdrant",
    "Pinecone",
    "Weaviate",
    "OpenSearch",
    "Elasticsearch"
]

# Score Weights
WEIGHTS = {
    "experience": 30,
    "skills": 40,
    "behavior": 20,
    "location": 5,
    "education": 5
}
