"""
seed_reasoning_counting_figures_sheet7.py
==========================================
Seeds Reasoning → Counting Figures  Q45–Q51.
Diagram-based questions; image_url set to None — update after
uploading figures to Supabase Storage (bucket: question_image_Counting_figure).

Answer key
──────────────────────────────────────────────────────────────────────
Q45  A (18)  — Square with multiple crossing diagonals (complex X pattern)
Q46  D (20)  — Wide rectangle with diagonal sections throughout
Q47  C (10)  — 5-pointed star (pentagram): 5 outer tips + 5 inner = 10
Q48  B (8)   — Basic Star of David (hexagram): 6 outer tips + 2 large = 8
Q49  B (20)  — Complex Star of David with inner hexagon divisions = 20
Q50  B (13)  — Triangle of side 3 (3-row equilateral grid):
               9 small (size-1) + 3 medium (size-2) + 1 large (size-3) = 13
Q51  A (27)  — Triangle of side 4 (4-row equilateral grid):
               16 (size-1) + 7 (size-2) + 3 (size-3) + 1 (size-4) = 27
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

    # ── Q45 ─────────────────────────────────────────────────────────────────
    # Figure: Square with many internal crossing diagonal lines (multiple X
    # patterns / dense diagonal grid). More complex than a simple X+cross.
    # Question: "How many triangles are there in the given figure?"
    # Total triangles = 18.
    {
        "question_number": 45,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": "How many triangles are there in the given figure? / दी गई आकृति में कितने त्रिभुज हैं?",
        "question_hi": "दी गई आकृति में कितने त्रिभुज हैं?",
        "image_url": None,
        "option_a": "18",
        "option_b": "12",
        "option_c": "14",
        "option_d": "16",
        "correct_answer": "A",   # 18 triangles
    },

    # ── Q46 ─────────────────────────────────────────────────────────────────
    # Figure: Wide rectangle with multiple diagonal sections — a longer
    # rectangle subdivided with internal diagonal lines throughout.
    # Question: "How many triangles are there in the given figure?"
    # Total triangles = 20.
    {
        "question_number": 46,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": "How many triangles are there in the given figure? / दी गई आकृति में कितने त्रिभुज हैं?",
        "question_hi": "दी गई आकृति में कितने त्रिभुज हैं?",
        "image_url": None,
        "option_a": "10",
        "option_b": "12",
        "option_c": "18",
        "option_d": "20",
        "correct_answer": "D",   # 20 triangles
    },

    # ── Q47 ─────────────────────────────────────────────────────────────────
    # Figure: 5-pointed star (pentagram) — five lines forming a 5-pointed
    # star with the inner pentagon region.
    # Counting: 5 outer tip triangles + 5 inner composite triangles = 10.
    {
        "question_number": 47,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "8",
        "option_b": "7",
        "option_c": "10",
        "option_d": "12",
        "correct_answer": "C",   # 10 triangles
    },

    # ── Q48 ─────────────────────────────────────────────────────────────────
    # Figure: Basic Star of David (simple hexagram) — two overlapping
    # equilateral triangles forming a 6-pointed star, no extra internal lines.
    # Counting: 6 outer tiny tip triangles + 2 large outer triangles = 8.
    {
        "question_number": 48,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "10",
        "option_b": "8",
        "option_c": "6",
        "option_d": "7",
        "correct_answer": "B",   # 8 triangles
    },

    # ── Q49 ─────────────────────────────────────────────────────────────────
    # Figure: More complex Star of David / hexagram — inner hexagon regions
    # are visibly divided, creating additional triangular sectors.
    # Counting: 6 outer tips + 2 large + 6 inner hexagon sectors +
    #           6 medium (tip + 2 adjacent inner sectors) = 20.
    {
        "question_number": 49,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "14",
        "option_b": "20",
        "option_c": "16",
        "option_d": "18",
        "correct_answer": "B",   # 20 triangles
    },

    # ── Q50 ─────────────────────────────────────────────────────────────────
    # Figure: Equilateral triangle subdivided into a 3-row grid of small
    # equilateral triangles (side-3 triangular grid).
    # Counting by size:
    #   Size 1 (small): 6 upward + 3 downward = 9
    #   Size 2 (medium): 3 upward + 0 downward = 3
    #   Size 3 (whole): 1 + 0 = 1
    #   Total = 9 + 3 + 1 = 13.
    {
        "question_number": 50,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "12",
        "option_b": "13",
        "option_c": "18",
        "option_d": "20",
        "correct_answer": "B",   # 13 triangles
    },

    # ── Q51 ─────────────────────────────────────────────────────────────────
    # Figure: Equilateral triangle subdivided into a 4-row grid of small
    # equilateral triangles (side-4 triangular grid).
    # Counting by size:
    #   Size 1: 10 upward + 6 downward = 16
    #   Size 2: 6 upward + 1 downward  = 7
    #   Size 3: 3 upward + 0 downward  = 3
    #   Size 4: 1 upward + 0 downward  = 1
    #   Total = 16 + 7 + 3 + 1 = 27.
    {
        "question_number": 51,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "27",
        "option_b": "26",
        "option_c": "25",
        "option_d": "30",
        "correct_answer": "A",   # 27 triangles
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
