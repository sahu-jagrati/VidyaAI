"""
seed_reasoning_counting_figures_sheet5.py
==========================================
Seeds Reasoning → Counting Figures  Q30–Q37.
Diagram-based questions; image_url set to None — update after
uploading figures to Supabase Storage (bucket: question_image_Counting_figure).

Answer key
──────────────────────────────────────────────────────────────────────
Q30  D (16)         — Rectangle with X (2 diagonals) + center cross → 8 sectors
                      Systematic count: 8 small + 4 medium + 4 large = 16
Q31  B (18)         — 2 squares in a row, each with 2 diagonals
                      8 + 8 (individual) + 2 (spanning) = 18
Q32  C (28)         — 3 squares in a row, each with 2 diagonals
                      8×3 (individual) + 4 (spanning adjacent pairs) = 28
Q33  A (28)         — Different rectangle arrangement with diagonal cross-sections
Q34  A (35)         — L-shaped compound figure with diagonals
                      NOTE: options (b) and (c) both read "32" in source book
                      — likely a typo; correct answer is (a) 35.
Q35  C (42)         — Complex compound multi-section triangular figure
Q36  C (40 or more) — Dense square pattern; option (c) literally says "40 or more"
Q37  C (16)         — 4-pointed compass star with internal diagonals
                      NOTE: options were cut off in source image; estimated as
                      (a)8 (b)12 (c)16 (d)10 — verify from book.
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

    # ── Q30 ─────────────────────────────────────────────────────────────────
    # Figure: Rectangle / square with both corner-to-corner diagonals (X)
    # AND horizontal + vertical center lines (cross) — divides into 8 sectors.
    # Count: 8 small + 4 medium (pairs forming half-rectangle triangles) +
    #        4 large (full-edge diagonal triangles) = 16 total.
    {
        "question_number": 30,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "20",
        "option_b": "14",
        "option_c": "18",
        "option_d": "16",
        "correct_answer": "D",   # 16 triangles
    },

    # ── Q31 ─────────────────────────────────────────────────────────────────
    # Figure: Two squares placed side by side (1×2 grid), each with both
    # diagonals drawn. Individual: 8+8=16. Spanning: 2 triangles that cross
    # the shared center divider. Total = 18.
    {
        "question_number": 31,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "16",
        "option_b": "18",
        "option_c": "17",
        "option_d": "20",
        "correct_answer": "B",   # 18 triangles
    },

    # ── Q32 ─────────────────────────────────────────────────────────────────
    # Figure: Three squares placed side by side (1×3 grid), each with both
    # diagonals drawn. Individual: 8×3=24. Spanning adjacent pairs: 4
    # (2 between left-center + 2 between center-right). Total = 28.
    {
        "question_number": 32,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "20",
        "option_b": "24",
        "option_c": "28",
        "option_d": "32",
        "correct_answer": "C",   # 28 triangles
    },

    # ── Q33 ─────────────────────────────────────────────────────────────────
    # Figure: Rectangle with a different internal diagonal cross-section
    # arrangement (distinct from Q32). Total triangles = 28.
    {
        "question_number": 33,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "28",
        "option_b": "24",
        "option_c": "27",
        "option_d": "25",
        "correct_answer": "A",   # 28 triangles
    },

    # ── Q34 ─────────────────────────────────────────────────────────────────
    # Figure: L-shaped compound figure made of multiple rectangles with
    # internal diagonal lines. Complex multi-region counting.
    # NOTE: Source book options (b) and (c) both appear as "32" — likely
    # a typo. Correct answer from key is (a) 35.
    # Total triangles = 35.
    {
        "question_number": 34,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "35",
        "option_b": "32",
        "option_c": "32",   # possible typo in source; may be 30 or 33
        "option_d": "39",
        "correct_answer": "A",   # 35 triangles
    },

    # ── Q35 ─────────────────────────────────────────────────────────────────
    # Figure: Complex compound multi-section figure (larger arrangement of
    # triangles and rectangles with internal diagonals). Total = 42.
    {
        "question_number": 35,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "40",
        "option_b": "41",
        "option_c": "42",
        "option_d": "45",
        "correct_answer": "C",   # 42 triangles
    },

    # ── Q36 ─────────────────────────────────────────────────────────────────
    # Figure: Dense square pattern with many internal lines creating a large
    # number of triangles. The option "(c) 40 or more" is stated in the book,
    # indicating the count clearly exceeds 40.
    {
        "question_number": 36,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "36",
        "option_b": "38",
        "option_c": "40 or more",
        "option_d": "34",
        "correct_answer": "C",   # 40 or more triangles
    },

    # ── Q37 ─────────────────────────────────────────────────────────────────
    # Figure: 4-pointed compass star / asterisk shape with internal diagonal
    # lines — 4 outer triangular points + 4 inner sectors + compound combos.
    # NOTE: Options were cut off in source image; values below are estimated.
    # Verify from book: options likely in 8–16 range. Total = 16.
    {
        "question_number": 37,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": QUESTION_TEXT_EN,
        "question_hi": QUESTION_TEXT_HI,
        "image_url": None,
        "option_a": "8",
        "option_b": "12",
        "option_c": "16",
        "option_d": "10",
        "correct_answer": "C",   # 16 triangles [ESTIMATED — verify from book]
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
