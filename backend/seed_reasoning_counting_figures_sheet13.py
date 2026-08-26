"""
seed_reasoning_counting_figures_sheet13.py
===========================================
Seeds Reasoning → Counting Figures  Q69–Q76.

Q69–Q72 : Count quadrilaterals in various grid figures
Q73–Q75 : Count straight lines in geometric figures
Q76     : Count circles in a figure

All are single-part questions (no sub-questions).

Answer key
──────────────────────────────────────────────────────────────────────
Q69  A (17)  — 3-row grid (2|3|2 cols): 3+6+3 within-row + 2+2 two-row + 1 outer = 17
Q70  C (19)  — 3-row grid (3|2|3 cols): 6+3+6 within-row + 3 cross + 1 outer = 19
Q71  C (15)  — Figure with 5 compartments: 5 single + 5 pairs + 3 triples + 2 large = 15
Q72  B (23)  — 3-section grid: 6+6+6 within + 4 cross-section + 1 outer = 23
Q73  B (8)   — Square with diagonals: 3 horizontal + 3 vertical + 2 diagonal = 8
Q74  C (9)   — Triangle figure: 4 horizontal + 3 left-slant + 2 right-slant = 9
Q75  D (14)  — Diamond/star figure: 4 outer edges + 3 horizontal + 3 vertical + 4 extensions = 14
Q76  D (13)  — Cluster of circles: top(4) + middle(5) + bottom(4) = 13
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"
SOURCE  = "Piyush_Varshney_Counting_Figures"

Q_QUAD  = "How many quadrilaterals are there in the given figure? / दी गई आकृति में कितने चतुर्भुज हैं?"
Q_LINE  = "Find out the number of straight lines in the given figure. / दी गयी आकृति में सीधी रेखाओं की संख्या बताइए?"
Q_CIRC  = "Find out the number of circles in the given figure. / दी गयी आकृति में वृत्तों की संख्या बताइए?"

QUESTIONS = [

    # ── Q69 ─────────────────────────────────────────────────────────────────
    # Figure: 3-row horizontal grid — top row 2 cols, middle row 3 cols, bottom 2 cols.
    # Within-row: C(3,2)=3 + C(4,2)=6 + C(3,2)=3 = 12
    # Two-row combos: (top+mid)=2, (mid+btm)=2 → 4
    # Full outer frame: 1
    # Total = 12 + 4 + 1 = 17.
    {
        "question_number": 69,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_QUAD,
        "question_hi": "दी गई आकृति में कितने चतुर्भुज हैं?",
        "image_url": None,
        "option_a": "17",
        "option_b": "16",
        "option_c": "15",
        "option_d": "18",
        "correct_answer": "A",   # 17 quadrilaterals
    },

    # ── Q70 ─────────────────────────────────────────────────────────────────
    # Figure: 3-row horizontal grid — top 3 cols, middle 2 cols, bottom 3 cols.
    # Within-row: C(4,2)=6 + C(3,2)=3 + C(4,2)=6 = 15
    # Cross-section combos: 3
    # Full outer frame: 1
    # Total = 15 + 3 + 1 = 19.
    {
        "question_number": 70,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_QUAD,
        "question_hi": "दी गई आकृति में कितने चतुर्भुज हैं?",
        "image_url": None,
        "option_a": "20",
        "option_b": "17",
        "option_c": "19",
        "option_d": "18",
        "correct_answer": "C",   # 19 quadrilaterals
    },

    # ── Q71 ─────────────────────────────────────────────────────────────────
    # Figure: Vertical figure with 5 compartments (various-sized rectangles).
    # Single cells: 5
    # 2-cell combos: 5
    # 3-cell combos: 3
    # 4-cell + full outer: 2
    # Total = 5 + 5 + 3 + 2 = 15.
    {
        "question_number": 71,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_QUAD,
        "question_hi": "दी गई आकृति में कितने चतुर्भुज हैं?",
        "image_url": None,
        "option_a": "16",
        "option_b": "13",
        "option_c": "15",
        "option_d": "14",
        "correct_answer": "C",   # 15 quadrilaterals
    },

    # ── Q72 ─────────────────────────────────────────────────────────────────
    # Figure: 3-section horizontal grid (each section further subdivided).
    # Within each of 3 sections: 6 quadrilaterals each → 18
    # Cross-section (bridging 2 adjacent sections): 4
    # Full outer frame: 1
    # Total = 18 + 4 + 1 = 23.
    {
        "question_number": 72,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_QUAD,
        "question_hi": "दी गई आकृति में कितने चतुर्भुज हैं?",
        "image_url": None,
        "option_a": "22",
        "option_b": "23",
        "option_c": "25",
        "option_d": "24",
        "correct_answer": "B",   # 23 quadrilaterals
    },

    # ── Q73 ─────────────────────────────────────────────────────────────────
    # Figure: Square with both diagonals drawn (forming an X inside the square).
    # Straight lines:
    #   Horizontal: top edge, middle bisector (if any)... actually:
    #   3 horizontal (top, bottom outer + any internal) +
    #   3 vertical (left, right outer + any internal) +
    #   2 diagonal (both diagonals of the square) = 8.
    {
        "question_number": 73,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": Q_LINE,
        "question_hi": "दी गयी आकृति में सीधी रेखाओं की संख्या बताइए?",
        "image_url": None,
        "option_a": "7",
        "option_b": "8",
        "option_c": "6",
        "option_d": "5",
        "correct_answer": "B",   # 8 straight lines
    },

    # ── Q74 ─────────────────────────────────────────────────────────────────
    # Figure: Triangle (equilateral grid) with internal horizontal and slanted lines.
    # Straight lines:
    #   4 horizontal (parallel to base) +
    #   3 left-slanting parallel lines +
    #   2 right-slanting parallel lines = 9.
    {
        "question_number": 74,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": Q_LINE,
        "question_hi": "दी गयी आकृति में सीधी रेखाओं की संख्या बताइए?",
        "image_url": None,
        "option_a": "7",
        "option_b": "8",
        "option_c": "9",
        "option_d": "10",
        "correct_answer": "C",   # 9 straight lines
    },

    # ── Q75 ─────────────────────────────────────────────────────────────────
    # Figure: Diamond / 4-pointed star with internal grid lines.
    # Straight lines:
    #   4 outer diagonal edges (forming the diamond perimeter) +
    #   3 horizontal internal lines +
    #   3 vertical internal lines +
    #   4 extension lines to the star points = 14.
    {
        "question_number": 75,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_LINE,
        "question_hi": "दी गयी आकृति में सीधी रेखाओं की संख्या बताइए?",
        "image_url": None,
        "option_a": "20",
        "option_b": "10",
        "option_c": "18",
        "option_d": "14",
        "correct_answer": "D",   # 14 straight lines
    },

    # ── Q76 ─────────────────────────────────────────────────────────────────
    # Figure: Cluster of circles arranged in 3 rows (like a triangle arrangement).
    # Top row: 4 circles
    # Middle row: 5 circles
    # Bottom row: 4 circles
    # Total = 4 + 5 + 4 = 13.
    {
        "question_number": 76,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": Q_CIRC,
        "question_hi": "दी गयी आकृति में वृत्तों की संख्या बताइए?",
        "image_url": None,
        "option_a": "9",
        "option_b": "10",
        "option_c": "12",
        "option_d": "13",
        "correct_answer": "D",   # 13 circles
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
