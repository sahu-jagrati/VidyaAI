"""
seed_reasoning_counting_figures_sheet8.py
==========================================
Seeds Reasoning → Counting Figures  Q52–Q57.

Q52  : single triangle-counting question
Q53  : 2×2 grid — 3 sub-questions (i) squares, (ii) rectangles, (iii) only-rects
Q54  : 4×3 grid — 2 sub-questions (i) squares, (ii) rectangles
Q55  : 7×3 grid — 2 sub-questions (i) squares, (ii) rectangles
Q56  : 5×5 grid — single squares question
Q57  : 5×3 grid — 2 sub-questions (i) rectangles, (ii) only-rects

Sub-questions encoded as: main_QN = first part; extras = QN*100+part_index
  e.g. Q53(ii) → question_number = 5302

Answer key
──────────────────────────────────────────────────────────────────────
Q52       D (48)   — Triangle of side 5: 35 up + 13 down = 48
Q53(i)    B (5)    — 2×2 grid squares: 4(1×1) + 1(2×2) = 5
Q53(ii)   D (9)    — 2×2 grid rectangles: C(3,2)² = 9
Q53(iii)  A (4)    — 2×2 only-rectangles: 9 − 5 = 4
Q54(i)    B (20)   — 4×3 grid squares: 12+6+2 = 20
Q54(ii)   A (60)   — 4×3 grid rectangles: C(5,2)×C(4,2) = 60
Q55(i)    D (38)   — 7×3 grid squares: 21+12+5 = 38
Q55(ii)   A (168)  — 7×3 grid rectangles: C(8,2)×C(4,2) = 168
Q56       A (55)   — 5×5 grid squares: 25+16+9+4+1 = 55
Q57(i)    C (90)   — 5×3 grid rectangles: C(6,2)×C(4,2) = 90
Q57(ii)   D (64)   — 5×3 only-rectangles: 90 − 26 = 64
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"
SOURCE  = "Piyush_Varshney_Counting_Figures"

# ── Shared question texts ────────────────────────────────────────────
Q_TRIANGLE   = "Find out the number of triangles in the given figure. / दी गयी आकृति में त्रिभुजों की संख्या बताइए?"
Q_SQ_TOTAL   = "Find out the number of total squares. / कुल वर्गों की संख्या बताइए?"
Q_RECT_TOTAL = "Find out the number of total rectangles. / कुल आयतों की संख्या बताइए?"
Q_RECT_ONLY  = "Find out the number of only rectangles (excluding squares). / बनने वाले केवल आयतों की संख्या बताइए?"
Q_RECT_FIG   = "Find out the number of rectangles in the given figure. / दी गई आकृति में आयतों की संख्या बताइए?"
Q_SQ_FIG     = "Find out the number of total squares in the given figure. / निम्नलिखित आकृति में कुल वर्गों की संख्या ज्ञात कीजिए?"

QUESTIONS = [

    # ── Q52 ─────────────────────────────────────────────────────────────────
    # Figure: Equilateral triangle subdivided into a 5-row grid of small
    # equilateral triangles (side-5 triangular grid).
    # Counting by size:
    #   Upward:   size1=15, size2=10, size3=6, size4=3, size5=1 → 35
    #   Downward: size1=10, size2=3                              → 13
    #   Total = 35 + 13 = 48.
    {
        "question_number": 52,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_TRIANGLE,
        "question_hi": "दी गयी आकृति में त्रिभुजों की संख्या बताइए?",
        "image_url": None,
        "option_a": "41",
        "option_b": "50",
        "option_c": "43",
        "option_d": "48",
        "correct_answer": "D",   # 48 triangles
    },

    # ── Q53 (i) ─────────────────────────────────────────────────────────────
    # Figure: 2×2 grid of unit squares (2 columns, 2 rows).
    # Squares: 1×1=4, 2×2=1 → Total = 5.
    {
        "question_number": 53,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_TOTAL,
        "question_hi": "कुल वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "4",
        "option_b": "5",
        "option_c": "6",
        "option_d": "9",
        "correct_answer": "B",   # 5 squares
    },

    # ── Q53 (ii) ────────────────────────────────────────────────────────────
    # 2×2 grid — total rectangles (including squares).
    # C(3,2) × C(3,2) = 3 × 3 = 9.
    {
        "question_number": 5302,   # Q53 part 2
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_TOTAL,
        "question_hi": "कुल आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "6",
        "option_b": "7",
        "option_c": "8",
        "option_d": "9",
        "correct_answer": "D",   # 9 rectangles
    },

    # ── Q53 (iii) ───────────────────────────────────────────────────────────
    # 2×2 grid — only rectangles (not squares).
    # 9 (total) − 5 (squares) = 4.
    {
        "question_number": 5303,   # Q53 part 3
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_ONLY,
        "question_hi": "बनने वाले केवल आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "4",
        "option_b": "5",
        "option_c": "6",
        "option_d": "7",
        "correct_answer": "A",   # 4 only-rectangles
    },

    # ── Q54 (i) ─────────────────────────────────────────────────────────────
    # Figure: 4×3 grid of unit squares (4 columns, 3 rows).
    # Squares: 1×1=12, 2×2=6, 3×3=2 → Total = 20.
    {
        "question_number": 54,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_TOTAL,
        "question_hi": "कुल वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "16",
        "option_b": "20",
        "option_c": "18",
        "option_d": "24",
        "correct_answer": "B",   # 20 squares
    },

    # ── Q54 (ii) ────────────────────────────────────────────────────────────
    # 4×3 grid — total rectangles.
    # C(5,2) × C(4,2) = 10 × 6 = 60.
    {
        "question_number": 5402,   # Q54 part 2
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_TOTAL,
        "question_hi": "कुल आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "60",
        "option_b": "50",
        "option_c": "40",
        "option_d": "80",
        "correct_answer": "A",   # 60 rectangles
    },

    # ── Q55 (i) ─────────────────────────────────────────────────────────────
    # Figure: 7×3 grid of unit squares (7 columns, 3 rows).
    # Squares: 1×1=21, 2×2=12, 3×3=5 → Total = 38.
    {
        "question_number": 55,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_TOTAL,
        "question_hi": "कुल वर्गों की संख्या बताइए?",
        "image_url": None,
        "option_a": "50",
        "option_b": "40",
        "option_c": "34",
        "option_d": "38",
        "correct_answer": "D",   # 38 squares
    },

    # ── Q55 (ii) ────────────────────────────────────────────────────────────
    # 7×3 grid — total rectangles.
    # C(8,2) × C(4,2) = 28 × 6 = 168.
    {
        "question_number": 5502,   # Q55 part 2
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_TOTAL,
        "question_hi": "कुल आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "168",
        "option_b": "174",
        "option_c": "160",
        "option_d": "150",
        "correct_answer": "A",   # 168 rectangles
    },

    # ── Q56 ─────────────────────────────────────────────────────────────────
    # Figure: 5×5 grid of unit squares (5 columns, 5 rows).
    # Squares: 1×1=25, 2×2=16, 3×3=9, 4×4=4, 5×5=1 → Total = 55.
    {
        "question_number": 56,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_SQ_FIG,
        "question_hi": "निम्नलिखित आकृति में कुल वर्गों की संख्या ज्ञात कीजिए?",
        "image_url": None,
        "option_a": "55",
        "option_b": "60",
        "option_c": "50",
        "option_d": "70",
        "correct_answer": "A",   # 55 squares
    },

    # ── Q57 (i) ─────────────────────────────────────────────────────────────
    # Figure: 5×3 grid of unit squares (5 columns, 3 rows).
    # Total rectangles (including squares):
    # C(6,2) × C(4,2) = 15 × 6 = 90.
    {
        "question_number": 57,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": Q_RECT_FIG,
        "question_hi": "दी गई आकृति में आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "70",
        "option_b": "80",
        "option_c": "90",
        "option_d": "100",
        "correct_answer": "C",   # 90 rectangles
    },

    # ── Q57 (ii) ────────────────────────────────────────────────────────────
    # 5×3 grid — only rectangles (not squares).
    # Squares in 5×3: 1×1=15, 2×2=8, 3×3=3 → 26.
    # Only-rectangles = 90 − 26 = 64.
    {
        "question_number": 5702,   # Q57 part 2
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": "Find out the number of only rectangles (excluding squares). / केवल आयतों की संख्या बताइए?",
        "question_hi": "केवल आयतों की संख्या बताइए?",
        "image_url": None,
        "option_a": "68",
        "option_b": "80",
        "option_c": "60",
        "option_d": "64",
        "correct_answer": "D",   # 64 only-rectangles
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
            label = (
                f"Q{qn}" if qn <= 57
                else f"Q{str(qn)[:2]}({str(qn)[2:]})"
            )
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
