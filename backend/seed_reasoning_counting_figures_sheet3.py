"""
seed_reasoning_counting_figures_sheet3.py
==========================================
Seeds Reasoning → Counting Figures  Q15–Q21.
Diagram-based questions; image_url set to None — update after
uploading figures to Supabase Storage (bucket: question_image_Counting_figure).

Answer key
──────────────────────────────────────────────────────────────────────
Q15  B (18)  — triangle with cevians from all three vertices
Q16  D (24)  — triangle with 1 vertical cevian + 2 horizontal lines (3 rows)
Q17  D (24)  — bowtie/double triangle joined at shared apex with fan-lines
Q18  B (8)   — simple triangle with 2 cevians crossing at interior point
Q19  C (20)  — diamond/rhombus (two triangles joined at base) with fan-lines
Q20  A (20)  — triangle with internal shaded grid lines
Q21  C (16)  — triangle with horizontal + fan lines forming partial grid
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

    # ── Q15 ─────────────────────────────────────────────────────────────────
    # Figure: Triangle with cevians drawn from all three vertices, creating
    # multiple interior intersection points and sub-triangles.
    # Total triangles = 18.
    {
        "question_number": 15,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_15.png
        "option_a": "16",
        "option_b": "18",
        "option_c": "20",
        "option_d": "14",
        "correct_answer": "B",   # 18 triangles
    },

    # ── Q16 ─────────────────────────────────────────────────────────────────
    # Figure: Triangle with 1 vertical center cevian from apex to base
    # + 2 horizontal lines parallel to base (creating 3 rows).
    # Total triangles = 24.
    {
        "question_number": 16,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_16.png
        "option_a": "15",
        "option_b": "14",
        "option_c": "13",
        "option_d": "24",
        "correct_answer": "D",   # 24 triangles
    },

    # ── Q17 ─────────────────────────────────────────────────────────────────
    # Figure: Bowtie / double-triangle figure — two triangles joined at a
    # shared central apex with horizontal lines running through both halves
    # and fan-lines from the shared apex.
    # Total triangles = 24.
    {
        "question_number": 17,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_17.png
        "option_a": "18",
        "option_b": "22",
        "option_c": "20",
        "option_d": "24",
        "correct_answer": "D",   # 24 triangles
    },

    # ── Q18 ─────────────────────────────────────────────────────────────────
    # Figure: Simple triangle with 2 cevians from different base vertices
    # crossing at one interior point, creating 4 sub-regions.
    # Total triangles = 8.
    {
        "question_number": 18,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_18.png
        "option_a": "6",
        "option_b": "8",
        "option_c": "7",
        "option_d": "9",
        "correct_answer": "B",   # 8 triangles
    },

    # ── Q19 ─────────────────────────────────────────────────────────────────
    # Figure: Diamond / rhombus shape (two triangles joined at their base —
    # one pointing up, one pointing down) with internal fan-lines from the
    # left and right apex points.
    # Total triangles = 20.
    {
        "question_number": 19,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_19.png
        "option_a": "18",
        "option_b": "19",
        "option_c": "20",
        "option_d": "21",
        "correct_answer": "C",   # 20 triangles
    },

    # ── Q20 ─────────────────────────────────────────────────────────────────
    # Figure: Triangle with internal shaded grid lines (fan-lines from apex
    # + horizontal lines), creating a multi-row grid inside the triangle.
    # Total triangles = 20.
    {
        "question_number": 20,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_20.png
        "option_a": "20",
        "option_b": "18",
        "option_c": "22",
        "option_d": "19",
        "correct_answer": "A",   # 20 triangles
    },

    # ── Q21 ─────────────────────────────────────────────────────────────────
    # Figure: Triangle with horizontal lines + fan-lines from apex forming
    # a partial grid; moderately complex structure.
    # Total triangles = 16.
    {
        "question_number": 21,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_21.png
        "option_a": "20",
        "option_b": "15",
        "option_c": "16",
        "option_d": "18",
        "correct_answer": "C",   # 16 triangles
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
