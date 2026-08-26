"""
seed_reasoning_counting_figures_sheet14.py
===========================================
Seeds Reasoning → Counting Figures  Q77–Q80.

Q77 : Count circles in a stacked-circle figure
Q78 : Count cubes in a small cube arrangement
Q79 : Count cubes in a medium pyramid arrangement
Q80 : 4-level pyramid — 3 sub-questions (total, visible, hidden cubes)

Sub-question encoding: Q80(ii) → 8002,  Q80(iii) → 8003

Answer key
──────────────────────────────────────────────────────────────────────
Q77      C (18)  — 6 large circles × 3 circles each (outer+2 inner) = 18
Q78      C (4)   — small arrangement: 1 top + 3 bottom = 4 cubes
Q79      A (10)  — 3-level pyramid: 1+3+6 = 10 cubes
Q80(i)   C (20)  — 4-level pyramid: 1+3+6+10 = 20 total cubes
Q80(ii)  B (10)  — visible cubes: 1+2+3+4 = 10
Q80(iii) A (10)  — hidden cubes: 20 − 10 = 10
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"
SOURCE  = "Piyush_Varshney_Counting_Figures"

Q_CIRC        = "Find out the number of circles in the given figure. / दी गयी आकृति में वृत्तों की संख्या बताइए?"
Q_CUBES       = "Find out the number of cubes in the given figure. / दी गयी आकृति में घनों की संख्या बताइए?"
Q_TOTAL_CUBES = "What is the number of total cubes? / कुल घनों की संख्या बताइए?"
Q_VISIBLE     = "How many cubes are there which can be seen? / ऐसे कितने घन हैं जो दिखाई दे रहे हैं?"
Q_HIDDEN      = "How many cubes are there which are hidden? / ऐसे कितने घन हैं जो छिपे हुए हैं?"

QUESTIONS = [

    # ── Q77 ─────────────────────────────────────────────────────────────────
    # Figure: Triangle stack of 6 large circles (3+2+1 arrangement), each
    # containing 2 inner concentric circles → 3 circles per group.
    # Total = 6 × 3 = 18.
    {
        "question_number": 77,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": Q_CIRC,
        "question_hi": "दी गयी आकृति में वृत्तों की संख्या बताइए?",
        "image_url": None,
        "option_a": "16",
        "option_b": "20",
        "option_c": "18",
        "option_d": "21",
        "correct_answer": "C",   # 18 circles
    },

    # ── Q78 ─────────────────────────────────────────────────────────────────
    # Figure: Small cube arrangement — 1 cube on top supported by 3 cubes
    # at the bottom (2 visible front + 1 behind/support). Total = 1 + 3 = 4.
    {
        "question_number": 78,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": Q_CUBES,
        "question_hi": "दी गयी आकृति में घनों की संख्या बताइए?",
        "image_url": None,
        "option_a": "1",
        "option_b": "3",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "C",   # 4 cubes
    },

    # ── Q79 ─────────────────────────────────────────────────────────────────
    # Figure: 3-level pyramid of cubes.
    #   Level 1 (top)    : 1 cube
    #   Level 2 (middle) : 3 cubes (1 hidden support + 2 visible)
    #   Level 3 (bottom) : 6 cubes (3 hidden supports + 3 visible)
    #   Total = 1 + 3 + 6 = 10.
    {
        "question_number": 79,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_CUBES,
        "question_hi": "दी गयी आकृति में घनों की संख्या बताइए?",
        "image_url": None,
        "option_a": "10",
        "option_b": "12",
        "option_c": "8",
        "option_d": "9",
        "correct_answer": "A",   # 10 cubes
    },

    # ── Q80 (i) ─────────────────────────────────────────────────────────────
    # Figure: 4-level triangular pyramid of cubes.
    #   Level 1 (top)    : 1  cube
    #   Level 2          : 3  cubes
    #   Level 3          : 6  cubes
    #   Level 4 (bottom) : 10 cubes
    #   Total = 1 + 3 + 6 + 10 = 20.
    {
        "question_number": 80,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_TOTAL_CUBES,
        "question_hi": "कुल घनों की संख्या बताइए?",
        "image_url": None,
        "option_a": "14",
        "option_b": "18",
        "option_c": "20",
        "option_d": "10",
        "correct_answer": "C",   # 20 total cubes
    },

    # ── Q80 (ii) ────────────────────────────────────────────────────────────
    # Same figure — visible cubes (front-facing, not hidden behind others).
    #   Layer 1: 1, Layer 2: 2, Layer 3: 3, Layer 4: 4
    #   Visible = 1 + 2 + 3 + 4 = 10.
    {
        "question_number": 8002,   # Q80 part 2
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_VISIBLE,
        "question_hi": "ऐसे कितने घन हैं जो दिखाई दे रहे हैं?",
        "image_url": None,
        "option_a": "14",
        "option_b": "10",
        "option_c": "12",
        "option_d": "8",
        "correct_answer": "B",   # 10 visible cubes
    },

    # ── Q80 (iii) ───────────────────────────────────────────────────────────
    # Same figure — hidden cubes (not visible from the front).
    #   Hidden = Total − Visible = 20 − 10 = 10.
    {
        "question_number": 8003,   # Q80 part 3
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": Q_HIDDEN,
        "question_hi": "ऐसे कितने घन हैं जो छिपे हुए हैं?",
        "image_url": None,
        "option_a": "10",
        "option_b": "12",
        "option_c": "8",
        "option_d": "14",
        "correct_answer": "A",   # 10 hidden cubes
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
            label = f"Q{qn}" if qn <= 80 else f"Q{str(qn)[:2]}({str(qn)[2:]})"
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
