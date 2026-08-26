"""
seed_reasoning_counting_figures_sheet2.py
==========================================
Seeds Reasoning → Counting Figures  Q8–Q14.
Diagram-based questions; image_url set to None here — update after
uploading figures to Supabase Storage (bucket: question_image_Counting_figure).

Answer key
──────────────────────────────────────────────────────────────────────
Q8   B (40)  — large triangle, 4 fan-lines + 4 horizontal rows
Q9   B (8)   — triangle with 2 cevians from different vertices (crossing inside)
Q10  D (27)  — medium fan + horizontal grid
Q11  D (70)  — taller figure, more fan + horizontal layers
Q12  B (125) — very large multi-row fan triangle
Q13  D (20)  — simpler triangle, fewer internal lines
Q14  C (70)  — dense horizontal + vertical grid inside triangle
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

    # ── Q8 ──────────────────────────────────────────────────────────────────
    # Figure: Large triangle with 4 fan-lines from apex (5 sectors) and
    # 4 horizontal lines (5 rows). Multi-row fan pyramid.
    # Total triangles = 40.
    {
        "question_number": 8,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload and fill
        "option_a": "37",
        "option_b": "40",
        "option_c": "35",
        "option_d": "42",
        "correct_answer": "B",   # 40 triangles
    },

    # ── Q9 ──────────────────────────────────────────────────────────────────
    # Figure: Triangle with 2 cevians drawn from different vertices,
    # crossing at an interior point — creating 4 sub-regions plus
    # compounded triangles. Total triangles = 8.
    {
        "question_number": 9,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "7",
        "option_b": "8",
        "option_c": "9",
        "option_d": "6",
        "correct_answer": "B",   # 8 triangles
    },

    # ── Q10 ─────────────────────────────────────────────────────────────────
    # Figure: Triangle with fan-lines from apex combined with horizontal
    # divisions — medium-complexity grid. Total triangles = 27.
    {
        "question_number": 10,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "25",
        "option_b": "30",
        "option_c": "18",
        "option_d": "27",
        "correct_answer": "D",   # 27 triangles
    },

    # ── Q11 ─────────────────────────────────────────────────────────────────
    # Figure: Taller pyramid triangle with more fan-lines and horizontal
    # rows than Q8 — results in 70 triangles.
    {
        "question_number": 11,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "64",
        "option_b": "60",
        "option_c": "72",
        "option_d": "70",
        "correct_answer": "D",   # 70 triangles
    },

    # ── Q12 ─────────────────────────────────────────────────────────────────
    # Figure: Very large multi-row fan pyramid with many fan-lines and
    # horizontal divisions (shaded regions visible in original). Total = 125.
    {
        "question_number": 12,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "120",
        "option_b": "125",
        "option_c": "115",
        "option_d": "130",
        "correct_answer": "B",   # 125 triangles
    },

    # ── Q13 ─────────────────────────────────────────────────────────────────
    # Figure: Simpler triangle with fewer internal fan/horizontal lines.
    # Total triangles = 20.
    {
        "question_number": 13,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "24",
        "option_b": "28",
        "option_c": "30",
        "option_d": "20",
        "correct_answer": "D",   # 20 triangles
    },

    # ── Q14 ─────────────────────────────────────────────────────────────────
    # Figure: Triangle with a dense internal grid of horizontal and vertical
    # (or fan) lines — grid-type pyramid. Total triangles = 70.
    {
        "question_number": 14,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "50",
        "option_b": "60",
        "option_c": "70",
        "option_d": "80",
        "correct_answer": "C",   # 70 triangles
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
