"""
fix_seating_arrangement_pv_sheet1.py
======================================
1. Updates correct_answer for 3 existing Practice-Set PV rows (ids 5856-5858)
   that were inserted in a previous session with ans=None.
2. Inserts the 3 missing PV questions (book Q2, Q3, Q4) as question_numbers
   27, 28, 29 (first slots free after the existing max of 26).

Answer key
──────────────────────────────────────────────────────────────────────
id=5856  Q1   B (S)   — 7-person circle; immediate left of N = S.
id=5857  Q5   A (L)   — 6-person circle; immediate right of K = L.
id=5858  Q6   D (B)   — 6-person circle: A=1,E=2,B=3,F=4,C=5,D=6;
                        immediate left of F(4) = B(3).
NEW Q27  (book Q2)  D (Penny)  — 5-person circle; immediate right of Quin = Penny.
NEW Q28  (book Q3)  C (Oliver) — 6-person circle; exactly between Quinn & Nora = Oliver.
NEW Q29  (book Q4)  B          — 6-person circle: A=1,D=2,B=3,F=4,E=5,C=6;
                                  position of E = immediate left of C.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Seating Arrangement"
SOURCE  = "Piyush_Varshney_Seating_Arrangement"

# ── Rows to fix (update correct_answer) ────────────────────────────────────
FIXES = {
    5856: "B",   # Q1: immediate left of N = S → option B
    5857: "A",   # Q5: immediate right of K = L → option A
    5858: "D",   # Q6: immediate left of F = B → option D
}

# ── New questions to insert ─────────────────────────────────────────────────
NEW_QUESTIONS = [

    # ── Q27 (book Q2) ─────────────────────────────────────────────────────
    # Clockwise: Penny(1)-Oliver(2)-Sophie(3)-Ryan(4)-Quin(5).
    # Immediate right of Quin(5) → clockwise = Penny(1).
    {
        "question_number": 27,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Five friends Oliver, Penny, Quin, Ryan, and Sophie are sitting on a "
            "circular table facing the centre. Oliver is sitting to the immediate "
            "right of Penny. Ryan is sitting exactly between Quin and Sophie. "
            "Sophie is not a neighbour of Penny. "
            "Who is sitting to the immediate right of Quin?"
        ),
        "question_hi": (
            "पांच मित्र- ऑलिवर, पेनी, क्विन, रयान और सोफी एक वृत्ताकार मेज "
            "के केंद्र के सम्मुख बैठे हैं। ऑलिवर, पेनी के निकटतम दाएं बैठा "
            "है। रयान, क्विन और सोफी के ठीक बीच में बैठा है। सोफी पेनी की "
            "पड़ोसी नहीं है। क्विन के निकटतम दाएं कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "Sophie/ सोफी",
        "option_b": "Ryan/ रयान",
        "option_c": "Oliver/ ऑलिवर",
        "option_d": "Penny/ पेनी",
        "correct_answer": "D",
    },

    # ── Q28 (book Q3) ─────────────────────────────────────────────────────
    # Clockwise: Max(1)-Quinn(2)-Oliver(3)-Nora(4)-Lila(5)-Penny(6).
    # Exactly between Quinn(2) and Nora(4) → Oliver(3).
    {
        "question_number": 28,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Six family members Lila, Max, Nora, Oliver, Penny, and Quinn are "
            "seated at a circular table facing each other. Max is to the immediate "
            "left of Quinn and Lila is second to the left of Max. Nora is second "
            "to the left of Penny. "
            "Who sits exactly between Quinn and Nora?"
        ),
        "question_hi": (
            "परिवार के छह सदस्य- लीला, मैक्स, नोरा, ऑलिवर, पेन और क्विन एक "
            "वृत्ताकार मेज के सामने एक दूसरे के सम्मुख बैठे हैं। मैक्स क्विन "
            "के निकटतम बाएं है और लीला मैक्स के बाएं से दूसरे स्थान पर है। "
            "नोरा पेनी के बाएं से दूसरे स्थान पर है। "
            "क्विन और नोरा के ठीक बीच में कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "Max/ मैक्स",
        "option_b": "Penny/ पेनी",
        "option_c": "Oliver/ ऑलिवर",
        "option_d": "Lila/ लीला",
        "correct_answer": "C",
    },

    # ── Q29 (book Q4) ─────────────────────────────────────────────────────
    # Clockwise: A(1)-D(2)-B(3)-F(4)-E(5)-C(6).
    # Position of E(5) = immediate left of C(6).
    {
        "question_number": 29,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Six friends A, B, C, D, E and F are sitting around a circular table, "
            "facing towards the centre of the table. D and C are immediate "
            "neighbours of A. B is second to the right of A. F is an immediate "
            "neighbour of E, and fourth to the left of D. "
            "What is the position of E?"
        ),
        "question_hi": (
            "छह मित्र- A, B, C, D, E और F- एक गोलाकार मेज के चारों ओर केंद्र "
            "की ओर उन्मुख बैठे हैं। D और C, A के निकटतम पड़ोसी हैं। B, A के "
            "दायीं ओर से दूसरे स्थान पर है। F, E का निकटतम पड़ोसी है और D के "
            "बायीं ओर से चौथे स्थान पर है। E का स्थान क्या है?"
        ),
        "image_url": None,
        "option_a": "Third to the left of A",
        "option_b": "Immediate left of C",
        "option_c": "Second to the right of A",
        "option_d": "Immediate neighbour of D and F",
        "correct_answer": "B",
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    fixed = inserted = skipped = 0
    try:
        # ── Step 1: Fix correct_answers ──────────────────────────────────
        print("Step 1: Fixing correct_answers for existing PV rows...")
        for row_id, answer in FIXES.items():
            row = db.query(Question).filter(Question.id == row_id).first()
            if row is None:
                print(f"  NOT FOUND  id={row_id}")
                continue
            if row.correct_answer == answer:
                print(f"  ALREADY OK  id={row_id} Q{row.question_number} ans={answer!r}")
                continue
            row.correct_answer = answer
            print(f"  FIXED  id={row_id} Q{row.question_number} → ans={answer!r}")
            fixed += 1

        # ── Step 2: Insert missing PV Q2, Q3, Q4 ────────────────────────
        print("\nStep 2: Inserting missing PV Q2, Q3, Q4...")
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
            if row[0] is not None
        }
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
        print(f"\nDone — fixed: {fixed}, inserted: {inserted}, skipped: {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
