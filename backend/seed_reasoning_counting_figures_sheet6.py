"""
seed_reasoning_counting_figures_sheet6.py
==========================================
1. UPDATES Q37 — corrects options and answer (previous entry used estimated
   options that were wrong; actual options are now visible from source image).
2. INSERTS Q38–Q44.

Answer key
──────────────────────────────────────────────────────────────────────
Q37  B (40)  — 4-pointed compass star with internal X + cross grid
Q38  B (24)  — Diamond/rhombus with internal horizontal lines + diagonals
Q39  B (11)  — Rectangle with bowtie/hourglass (X) inside
Q40  B (10)  — Right triangle / L-shape with internal grid lines
Q41  B (29)  — Wide triangular roof with multiple vertical internal lines
Q42  B (45)  — Arrow/plus (+) shape with diagonal internal lines in each arm
Q43  B (70)  — Hourglass (two triangles tip-to-tip) with internal grid
Q44  A (13)  — Diamond/kite shape with internal lines
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

# ── Q38–Q44 new inserts ──────────────────────────────────────────────
NEW_QUESTIONS = [

    # ── Q38 ─────────────────────────────────────────────────────────────────
    # Figure: Diamond / rhombus shape (wide, like a horizontal elongated
    # hexagon outline) with internal horizontal lines and diagonal lines
    # creating multiple triangular sectors.
    # Total triangles = 24.
    {
        "question_number": 38,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "22",
        "option_b": "24",
        "option_c": "28",
        "option_d": "32",
        "correct_answer": "B",   # 24 triangles
    },

    # ── Q39 ─────────────────────────────────────────────────────────────────
    # Figure: Rectangle with a bowtie / hourglass pattern inside — two
    # triangles meeting at the center point, with additional lines along the
    # rectangle boundary creating extra triangular regions.
    # Total triangles = 11.
    {
        "question_number": 39,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "10",
        "option_b": "11",
        "option_c": "9",
        "option_d": "12",
        "correct_answer": "B",   # 11 triangles
    },

    # ── Q40 ─────────────────────────────────────────────────────────────────
    # Figure: Right triangle or L-shaped figure with internal grid lines
    # (horizontal + vertical divisions inside the triangular region).
    # Total triangles = 10.
    {
        "question_number": 40,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "5",
        "option_b": "10",
        "option_c": "6",
        "option_d": "7",
        "correct_answer": "B",   # 10 triangles
    },

    # ── Q41 ─────────────────────────────────────────────────────────────────
    # Figure: Wide triangular "roof" shape with multiple vertical internal
    # lines (columns) from the apex area to the base, creating many
    # sub-triangles and compound triangles.
    # Total triangles = 29.
    {
        "question_number": 41,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "33",
        "option_b": "29",
        "option_c": "28",
        "option_d": "31",
        "correct_answer": "B",   # 29 triangles
    },

    # ── Q42 ─────────────────────────────────────────────────────────────────
    # Figure: Arrow / plus (+) / cross-shaped figure with diagonal internal
    # lines in each arm section, creating a large number of triangular regions
    # across the multi-arm shape.
    # Total triangles = 45.
    {
        "question_number": 42,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "42",
        "option_b": "45",
        "option_c": "40",
        "option_d": "50",
        "correct_answer": "B",   # 45 triangles
    },

    # ── Q43 ─────────────────────────────────────────────────────────────────
    # Figure: Hourglass shape — two triangles joined tip-to-tip (one pointing
    # up, one pointing down) with internal grid lines (fan-lines + horizontal
    # divisions) in each triangular half.
    # Total triangles = 70.
    {
        "question_number": 43,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "60",
        "option_b": "70",
        "option_c": "45",
        "option_d": "75",
        "correct_answer": "B",   # 70 triangles
    },

    # ── Q44 ─────────────────────────────────────────────────────────────────
    # Figure: Diamond / kite shape with internal diagonal and horizontal
    # lines creating triangular sub-regions inside the kite boundary.
    # Question: "How many triangles are there in the given figure?"
    # Total triangles = 13.
    {
        "question_number": 44,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": "How many triangles are there in the given figure? / दी गई आकृति में कितने त्रिभुज हैं?",
        "question_hi": "दी गई आकृति में कितने त्रिभुज हैं?",
        "image_url": None,
        "option_a": "13",
        "option_b": "12",
        "option_c": "11",
        "option_d": "14",
        "correct_answer": "A",   # 13 triangles
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = updated = 0
    try:
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        # ── 1. Correct Q37 (update options + answer) ──────────────────────
        q37 = (
            db.query(Question)
            .filter(
                Question.subject         == SUBJECT,
                Question.topic           == TOPIC,
                Question.question_number == 37,
            )
            .first()
        )
        if q37:
            q37.option_a      = "36"
            q37.option_b      = "40"
            q37.option_c      = "34"
            q37.option_d      = "30"
            q37.correct_answer = "B"   # 40 triangles
            q37.difficulty    = "hard"
            updated += 1
            print("  UPDATED  Q37 → options corrected, answer = B (40)")
        else:
            print("  WARNING  Q37 not found — inserting fresh")
            db.add(Question(
                subject=SUBJECT, topic=TOPIC,
                question_number=37,
                difficulty="hard",
                source_pdf=SOURCE,
                question_en=QUESTION_TEXT_EN,
                question_hi=QUESTION_TEXT_HI,
                image_url=None,
                option_a="36", option_b="40", option_c="34", option_d="30",
                correct_answer="B",
            ))
            inserted += 1

        # ── 2. Insert Q38–Q44 ─────────────────────────────────────────────
        for d in NEW_QUESTIONS:
            qn = d["question_number"]
            if qn in existing_qnums:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

        db.commit()
        print(
            f"\nDone — inserted: {inserted}, "
            f"updated: {updated}, skipped: {skipped}"
        )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
