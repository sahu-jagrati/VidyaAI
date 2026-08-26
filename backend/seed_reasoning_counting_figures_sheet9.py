"""
seed_reasoning_counting_figures_sheet9.py
==========================================
Seeds Reasoning → Counting Figures  Q58–Q59.

Q58 : 6×4 grid — 3 sub-questions (i) squares, (ii) rectangles, (iii) only-rects
Q59 : 5×2 rectangular grid — 2 sub-questions (i) squares, (ii) rectangles

Sub-question encoding: main QN = first part; extras = QN*100 + part_index
  e.g. Q58(ii) → question_number = 5802

Answer key
──────────────────────────────────────────────────────────────────────
Q58(i)    C (50)   — 6×4 grid squares: 24+15+8+3 = 50
Q58(ii)   A (210)  — 6×4 grid rectangles: C(7,2)×C(5,2) = 21×10 = 210
Q58(iii)  B (160)  — 6×4 only-rectangles: 210 − 50 = 160
Q59(i)    A (14)   — 5×2 grid squares: 10(1×1) + 4(2×2) = 14
Q59(ii)   A (45)   — 5×2 grid rectangles: C(6,2)×C(3,2) = 15×3 = 45
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"
SOURCE  = "Piyush_Varshney_Counting_Figures"

Q_SQ_TOTAL   = "Find out the number of total squares. / कुल वर्गों की संख्या बताइए?"
Q_RECT_TOTAL = "Find out the number of total rectangles. / आयतों की संख्या बताइए?"
Q_RECT_ONLY  = "Find out the number of only rectangles (excluding squares). / केवल आयतों की संख्या बताइए?"

QUESTIONS = [

    # ── Q58 (i) ─────────────────────────────────────────────────────────────
    # Figure: 6×4 grid of unit squares (6 columns, 4 rows).
    # Squares by size:
    #   1×1 = 6×4 = 24
    #   2×2 = 5×3 = 15
    #   3×3 = 4×2 = 8
    #   4×4 = 3×1 = 3
    #   Total = 24+15+8+3 = 50.
    {
        "question_number": 58,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_TOTAL,
        "question_hi": "कुल वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "45",
        "option_b": "40",
        "option_c": "50",
        "option_d": "60",
        "correct_answer": "C",   # 50 squares
    },

    # ── Q58 (ii) ────────────────────────────────────────────────────────────
    # 6×4 grid — total rectangles (including squares).
    # C(7,2) × C(5,2) = 21 × 10 = 210.
    {
        "question_number": 5802,   # Q58 part 2
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_TOTAL,
        "question_hi": "आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "210",
        "option_b": "200",
        "option_c": "190",
        "option_d": "220",
        "correct_answer": "A",   # 210 rectangles
    },

    # ── Q58 (iii) ───────────────────────────────────────────────────────────
    # 6×4 grid — only rectangles (not squares).
    # 210 (total rectangles) − 50 (squares) = 160.
    {
        "question_number": 5803,   # Q58 part 3
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_ONLY,
        "question_hi": "केवल आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "150",
        "option_b": "160",
        "option_c": "180",
        "option_d": "200",
        "correct_answer": "B",   # 160 only-rectangles
    },

    # ── Q59 (i) ─────────────────────────────────────────────────────────────
    # Figure: 5×2 grid of unit squares (5 columns, 2 rows) with a triangular
    # extension on the right side (arrow shape). Only the rectangular grid
    # portion is counted for squares/rectangles.
    # Squares by size:
    #   1×1 = 5×2 = 10
    #   2×2 = 4×1 = 4
    #   Total = 14.
    {
        "question_number": 59,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_TOTAL,
        "question_hi": "कुल वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "14",
        "option_b": "10",
        "option_c": "18",
        "option_d": "20",
        "correct_answer": "A",   # 14 squares
    },

    # ── Q59 (ii) ────────────────────────────────────────────────────────────
    # 5×2 grid — total rectangles (including squares).
    # C(6,2) × C(3,2) = 15 × 3 = 45.
    {
        "question_number": 5902,   # Q59 part 2
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_TOTAL,
        "question_hi": "आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "45",
        "option_b": "50",
        "option_c": "40",
        "option_d": "60",
        "correct_answer": "A",   # 45 rectangles
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
            label = f"Q{qn}" if qn <= 59 else f"Q{str(qn)[:2]}({str(qn)[2:]})"
            print(f"  INSERT {label}")
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
