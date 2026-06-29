# 🚀 Redrob AI Candidate Ranking System

AI-powered Candidate Discovery & Ranking System built for the **Redrob Hackathon**.

---

## 📌 Problem Statement

Recruiters receive thousands of resumes for a single AI Engineering role.

The objective of this project is to automatically identify the **Top 100 candidates** using:

- Job Description Matching
- Skills Analysis
- Experience Analysis
- Behavioral Signals
- Candidate Ranking
- Human-readable Reasoning

---

# 🏗 Project Architecture

```
Job Description
        │
        ▼
Candidate Dataset
        │
        ▼
Feature Engineering
        │
        ▼
JD Matching
        │
        ▼
Behavior Score
        │
        ▼
Final Ranking
        │
        ▼
Top 100 CSV
```

---

# 📂 Folder Structure

```
redrob-ai-candidate-ranking/

data/
docs/
output/

main.py
rank_candidates.py
scoring.py
feature_engineering.py
job_matcher.py
reasoning.py
utils.py
config.py

README.md
requirements.txt
```

---

# ⚙ Installation

```bash
git clone https://github.com/USERNAME/redrob-ai-candidate-ranking.git

cd redrob-ai-candidate-ranking

pip install -r requirements.txt
```

---

# ▶ Run

```bash
python main.py
```

---

# 📊 Output

The program generates:

```
output/team_shankar.csv
```

Columns

- candidate_id
- rank
- score
- reasoning

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn

---

# 📈 Ranking Factors

- Experience
- AI Skills
- Python
- LLM
- Vector Database
- Embeddings
- Behavioral Signals
- Education
- GitHub Activity
- Recruiter Response Rate

---

# 📜 License

MIT License
