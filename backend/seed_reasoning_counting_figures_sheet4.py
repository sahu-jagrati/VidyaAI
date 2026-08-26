"""
seed_reasoning_counting_figures_sheet4.py
==========================================
Seeds Reasoning → Counting Figures  Q22–Q29.
Diagram-based questions; image_url set to None — update after
uploading figures to Supabase Storage (bucket: question_image_Counting_figure).

Answer key
──────────────────────────────────────────────────────────────────────
Q22  B (25)  — Star of David / hexagram (upward + downward triangle overlapping)
Q23  B (36)  — Hexagon with all internal diagonals drawn
Q24  C (10)  — Small triangle with internal subdivisions
Q25  B (20)  — Kite / downward-pointing triangle with fan-lines from apex
Q26  D (20)  — Square with two diagonals + extra internal lines
Q27  A (22)  — Square with multiple crossing diagonal lines (denser X pattern)
Q28  B (10)  — Rectangle with simple triangular internal divisions
Q29  C (12)  — Square with both diagonals + center cross (8 sectors)
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

    # ── Q22 ─────────────────────────────────────────────────────────────────
    # Figure: Star of David / hexagram — upward-pointing equilateral triangle
    # overlapping with a downward-pointing equilateral triangle, creating a
    # 6-pointed star with internal hexagonal region and extra structure.
    # Total triangles = 25.
    {
        "question_number": 22,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_22.png
        "option_a": "27",
        "option_b": "25",
        "option_c": "30",
        "option_d": "32",
        "correct_answer": "B",   # 25 triangles
    },

    # ── Q23 ─────────────────────────────────────────────────────────────────
    # Figure: Regular hexagon with all internal diagonals drawn —
    # 6 sides + 9 diagonals creating a dense internal triangle pattern.
    # Total triangles = 36.
    {
        "question_number": 23,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_23.png
        "option_a": "32",
        "option_b": "36",
        "option_c": "34",
        "option_d": "28",
        "correct_answer": "B",   # 36 triangles
    },

    # ── Q24 ─────────────────────────────────────────────────────────────────
    # Figure: Small triangular arrangement with internal horizontal and
    # diagonal subdivisions creating multiple sub-triangles.
    # Question: "Find the total number of triangles in the given figure."
    # Total triangles = 10.
    {
        "question_number": 24,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": "Find the total number of triangles in the given figure. / दी गई आकृति में त्रिभुजों की कुल संख्या ज्ञात कीजिए।",
        "question_hi": "दी गई आकृति में त्रिभुजों की कुल संख्या ज्ञात कीजिए।",
        "image_url": None,   # TODO: upload figure_24.png
        "option_a": "11",
        "option_b": "9",
        "option_c": "10",
        "option_d": "8",
        "correct_answer": "C",   # 10 triangles
    },

    # ── Q25 ─────────────────────────────────────────────────────────────────
    # Figure: Kite / downward-pointing diamond shape with fan-lines from the
    # bottom apex spreading outward — multiple internal triangular sectors.
    # Question: "How many triangles are there in the given figure?"
    # Total triangles = 20.
    {
        "question_number": 25,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": "How many triangles are there in the given figure? / दी गई आकृति में कितने त्रिभुज हैं?",
        "question_hi": "दी गई आकृति में कितने त्रिभुज हैं?",
        "image_url": None,   # TODO: upload figure_25.png
        "option_a": "19",
        "option_b": "20",
        "option_c": "22",
        "option_d": "21",
        "correct_answer": "B",   # 20 triangles
    },

    # ── Q26 ─────────────────────────────────────────────────────────────────
    # Figure: Square / rectangle with two diagonals drawn plus additional
    # internal vertical/horizontal lines creating triangular regions.
    # Question: "How many triangles are there in the figure given below?"
    # Total triangles = 20.
    {
        "question_number": 26,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": "How many triangles are there in the figure given below? / नीचे दी गई आकृति में कितने त्रिभुज हैं?",
        "question_hi": "नीचे दी गई आकृति में कितने त्रिभुज हैं?",
        "image_url": None,   # TODO: upload figure_26.png
        "option_a": "22",
        "option_b": "19",
        "option_c": "21",
        "option_d": "20",
        "correct_answer": "D",   # 20 triangles
    },

    # ── Q27 ─────────────────────────────────────────────────────────────────
    # Figure: Square with multiple crossing diagonal lines forming a denser
    # X pattern — more diagonals than Q26, creating additional triangles.
    # Question: "How many triangles are there in the figure?"
    # Total triangles = 22.
    {
        "question_number": 27,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": "How many triangles are there in the figure? / दी गई आकृति में कितने त्रिभुज हैं?",
        "question_hi": "दी गई आकृति में कितने त्रिभुज हैं?",
        "image_url": None,   # TODO: upload figure_27.png
        "option_a": "22",
        "option_b": "20",
        "option_c": "23",
        "option_d": "21",
        "correct_answer": "A",   # 22 triangles
    },

    # ── Q28 ─────────────────────────────────────────────────────────────────
    # Figure: Rectangle with simple internal triangular divisions — fewer
    # crossing lines, moderate complexity.
    # Total triangles = 10.
    {
        "question_number": 28,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_28.png
        "option_a": "8",
        "option_b": "10",
        "option_c": "7",
        "option_d": "6",
        "correct_answer": "B",   # 10 triangles
    },

    # ── Q29 ─────────────────────────────────────────────────────────────────
    # Figure: Square with both diagonals + center horizontal and vertical
    # lines (cross), dividing the square into 8 triangular sectors.
    # Total triangles = 12.
    {
        "question_number": 29,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,   # TODO: upload figure_29.png
        "option_a": "11",
        "option_b": "10",
        "option_c": "12",
        "option_d": "14",
        "correct_answer": "C",   # 12 triangles
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
