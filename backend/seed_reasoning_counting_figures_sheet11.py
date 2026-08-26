"""
seed_reasoning_counting_figures_sheet11.py
===========================================
Seeds Reasoning → Counting Figures  Q63–Q65.

Q63 : Diagonal staircase figure — single squares question
Q64 : Larger diagonal staircase figure — single squares question
Q65 : Composite rectangle figure — 2 sub-questions (i) only-rects, (ii) total rects

Sub-question encoding: Q65(ii) → question_number = 6502

Answer key
──────────────────────────────────────────────────────────────────────
Q63     C (13)  — 10 unit (1×1) + 3 composite (2×2) = 13 squares
Q64     D (21)  — 16 unit (1×1) + 5 composite (2×2) = 21 squares
Q65(i)  A (14)  — only rectangles (total 21 − 7 squares = 14)
Q65(ii) A (21)  — total rectangles (1 outer + 12 internal + 8 composites = 21)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"
SOURCE  = "Piyush_Varshney_Counting_Figures"

Q_SQ_FIG   = "Find out the number of squares in the given figure. / दी गई आकृति में वर्गों की संख्या बताइए?"
Q_RECT_ONLY  = "Find out the number of only rectangles. / केवल आयतों की संख्या बताइए?"
Q_RECT_TOTAL = "Find out the number of total rectangles. / कुल आयतों की संख्या बताइए?"

QUESTIONS = [

    # ── Q63 ─────────────────────────────────────────────────────────────────
    # Figure: Diagonal staircase shape — squares arranged in a stepped pattern
    # (top-right to bottom-left diagonal, each step 2–3 cells wide).
    # Count:
    #   1×1 squares: top(2) + middle(3) + middle-lower(3) + bottom(2) = 10
    #   2×2 squares: top-right + middle-overlap + bottom-left           = 3
    #   Total = 10 + 3 = 13.
    {
        "question_number": 63,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_FIG,
        "question_hi": "दी गई आकृति में वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "15",
        "option_b": "12",
        "option_c": "13",
        "option_d": "14",
        "correct_answer": "C",   # 13 squares
    },

    # ── Q64 ─────────────────────────────────────────────────────────────────
    # Figure: Larger diagonal staircase shape — more rows in the stepped pattern.
    # Count:
    #   1×1 squares: row-by-row 2+3+3+3+3+2 = 16
    #   2×2 squares: 1 (top) + 4 (overlapping along central axis) = 5
    #   Total = 16 + 5 = 21.
    {
        "question_number": 64,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_FIG,
        "question_hi": "दी गई आकृति में वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "25",
        "option_b": "28",
        "option_c": "14",
        "option_d": "21",
        "correct_answer": "D",   # 21 squares
    },

    # ── Q65 (i) ─────────────────────────────────────────────────────────────
    # Figure: Composite rectangle figure — outer square divided into 4 quadrants,
    # each quadrant subdivided into smaller rectangles.
    # Only rectangles (not squares) = total rectangles − total squares
    #   Total rectangles = 21 (see Q65 ii below)
    #   Total squares    = 7  (1 outer + 4 quadrant + 2 central squares)
    #   Only rectangles  = 21 − 7 = 14.
    {
        "question_number": 65,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_ONLY,
        "question_hi": "केवल आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "14",
        "option_b": "16",
        "option_c": "20",
        "option_d": "12",
        "correct_answer": "A",   # 14 only-rectangles
    },

    # ── Q65 (ii) ────────────────────────────────────────────────────────────
    # Same figure — total rectangles (including squares).
    # Count:
    #   1 outer boundary square
    #   4 × 3 = 12 internal rectangles (each quadrant: 2 inner pieces + 1 full quadrant)
    #   8 additional composite rectangles across main dividing lines
    #   Total = 1 + 12 + 8 = 21.
    {
        "question_number": 6502,   # Q65 part 2
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_TOTAL,
        "question_hi": "कुल आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "21",
        "option_b": "20",
        "option_c": "18",
        "option_d": "24",
        "correct_answer": "A",   # 21 total rectangles
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
            label = f"Q{qn}" if qn <= 65 else f"Q{str(qn)[:2]}({str(qn)[2:]})"
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
