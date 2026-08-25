"""
seed_reasoning_counting_figures_sheet1.py
==========================================
Seeds Reasoning → Counting Figures  Q1–Q7.
These are diagram-based questions.
image_url is left NULL here — upload actual figure images to Supabase Storage
and update image_url for each row afterwards.

Answer key  (options stored in standard A/B/C/D order per question)
──────────────────────────────────────────────────────────────────────
Q1   C  (3)   — 1 internal line from apex → 2 sectors → 3 total triangles
Q2   D  (8)   — 2 cevians (from base vertices crossing inside) → 8 triangles
Q3   B  (21)  — 5 fan-lines from apex, 6 sectors → C(7,2) = 21 triangles
Q4   B  (22)  — fan+horizontal grid → 22 triangles
Q5   B  (70)  — large multi-row fan figure → 70 triangles
Q6   C  (100) — larger multi-row fan figure → 100 triangles
Q7   B  (20)  — medium fan+grid figure → 20 triangles

Counting formula reminder
──────────────────────────
Fan-only (n internal lines from apex, n+1 sectors):
    Total = C(n+2, 2) = (n+1)(n+2)/2
    n=1 → 3, n=2 → 6, n=3 → 10, n=4 → 15, n=5 → 21
Grid (combined fan + horizontal): counted case-by-case per figure.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"
SOURCE  = "Piyush_Varshney_Counting_Figures"

QUESTION_TEXT_EN = "Find out the number of triangles in the given figure."
QUESTION_TEXT_HI = "दी गयी आकृति में त्रिभुजों की संख्या बताइए?"

QUESTIONS = [

    # ── Q1 ──────────────────────────────────────────────────────────────────
    # Figure: Triangle with 1 internal line from apex to base (2 sectors).
    # Triangles: 2 small (left, right) + 1 large (whole) = 3.
    {
        "question_number": 1,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure image and fill this URL
        "option_a": "2",
        "option_b": "4",
        "option_c": "3",
        "option_d": "5",
        "correct_answer": "C",   # 3 triangles
    },

    # ── Q2 ──────────────────────────────────────────────────────────────────
    # Figure: Triangle with 2 cevians from the two base vertices (crossing
    # inside the triangle at one interior point), creating 3 triangular
    # sub-regions + 1 quadrilateral.
    # All valid triangles (sub + combinations + whole) = 8.
    {
        "question_number": 2,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "5",
        "option_b": "7",
        "option_c": "6",
        "option_d": "8",
        "correct_answer": "D",   # 8 triangles
    },

    # ── Q3 ──────────────────────────────────────────────────────────────────
    # Figure: Triangle with 5 internal fan-lines from apex to base (6 sectors).
    # Formula: C(7,2) = 21 triangles.
    {
        "question_number": 3,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "23",
        "option_b": "21",
        "option_c": "18",
        "option_d": "25",
        "correct_answer": "B",   # 21 triangles
    },

    # ── Q4 ──────────────────────────────────────────────────────────────────
    # Figure: Triangle with fan-lines and horizontal divisions (larger grid
    # than Q3); total countable triangles = 22.
    {
        "question_number": 4,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "18",
        "option_b": "22",
        "option_c": "20",
        "option_d": "25",
        "correct_answer": "B",   # 22 triangles
    },

    # ── Q5 ──────────────────────────────────────────────────────────────────
    # Figure: Large pyramid-like triangle with multiple horizontal rows and
    # fan-lines from apex; total countable triangles = 70.
    {
        "question_number": 5,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "60",
        "option_b": "70",
        "option_c": "50",
        "option_d": "75",
        "correct_answer": "B",   # 70 triangles
    },

    # ── Q6 ──────────────────────────────────────────────────────────────────
    # Figure: Larger pyramid than Q5 (more rows / more fan-lines);
    # total countable triangles = 100.
    {
        "question_number": 6,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "120",
        "option_b": "110",
        "option_c": "100",
        "option_d": "105",
        "correct_answer": "C",   # 100 triangles
    },

    # ── Q7 ──────────────────────────────────────────────────────────────────
    # Figure: Medium-complexity pyramid triangle (fewer rows than Q5/Q6);
    # total countable triangles = 20.
    {
        "question_number": 7,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "19",
        "option_b": "20",
        "option_c": "18",
        "option_d": "21",
        "correct_answer": "B",   # 20 triangles
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
