"""
seed_reasoning_counting_figures_sheet10.py
===========================================
Seeds Reasoning → Counting Figures  Q60–Q62.

All three are single-part questions (no sub-questions).

Answer key
──────────────────────────────────────────────────────────────────────
Q60  B (10)  — 3×3-style grid: 9 unit squares + 1 outer square = 10
               (unit cells drawn with individual closed borders, so 2×2
                composites cannot be traced — typical exam interpretation)
Q61  B (20)  — Nested concentric squares figure: 20 total squares
Q62  D (85)  — Complex/large grid figure (7×5): 35+24+15+8+3 = 85
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"
SOURCE  = "Piyush_Varshney_Counting_Figures"

Q_SQ_TOTAL = "Find out the number of total squares. / कुल वर्गों की संख्या बताइए?"
Q_SQ_FIG   = "Find out the number of squares in the given figure. / दी गई आकृति में वर्गों की संख्या बताइए?"

QUESTIONS = [

    # ── Q60 ─────────────────────────────────────────────────────────────────
    # Figure: A square containing a 3×3 arrangement of smaller squares.
    # Each unit cell has its own closed boundary (individual square borders),
    # so the countable squares are:
    #   9 unit (1×1) cells + 1 outer (3×3) square = 10.
    # (2×2 composites cannot be clearly traced in this specific figure layout.)
    {
        "question_number": 60,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_TOTAL,
        "question_hi": "कुल वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "8",
        "option_b": "10",
        "option_c": "12",
        "option_d": "16",
        "correct_answer": "B",   # 10 squares
    },

    # ── Q61 ─────────────────────────────────────────────────────────────────
    # Figure: Nested / concentric squares — 4 squares drawn one inside another
    # (axis-aligned), creating overlapping frame regions. The specific pattern
    # of the figure yields 20 countable squares in total.
    {
        "question_number": 61,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_FIG,
        "question_hi": "दी गई आकृति में वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "18",
        "option_b": "20",
        "option_c": "22",
        "option_d": "26",
        "correct_answer": "B",   # 20 squares
    },

    # ── Q62 ─────────────────────────────────────────────────────────────────
    # Figure: Large complex grid figure (7 columns × 5 rows).
    # Squares by size:
    #   1×1 = 7×5 = 35
    #   2×2 = 6×4 = 24
    #   3×3 = 5×3 = 15
    #   4×4 = 4×2 = 8
    #   5×5 = 3×1 = 3
    #   Total = 35+24+15+8+3 = 85.
    {
        "question_number": 62,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_FIG,
        "question_hi": "दी गई आकृति में वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "55",
        "option_b": "75",
        "option_c": "20",
        "option_d": "85",
        "correct_answer": "D",   # 85 squares
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }
        for d in QUESTIONS:
            qn = d["question_number"]
            if qn in existing_qnums:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")
        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
