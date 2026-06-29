from rank_candidates import rank_candidates
from build_submission import build_submission
from config import CANDIDATES_FILE, OUTPUT_FILE

# load_candidates(...) पहले जैसा रहेगा

def main():

    candidates = load_candidates(CANDIDATES_FILE)

    ranked = rank_candidates(candidates)

    build_submission(
        ranked_candidates=ranked,
        output_file=OUTPUT_FILE
    )

if __name__ == "__main__":
    main()
