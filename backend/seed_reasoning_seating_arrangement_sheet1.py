"""
seed_reasoning_seating_arrangement_sheet1.py
=============================================
Seeds Reasoning → Seating Arrangement  book Q1–Q5 (Piyush Varshney source).
Stored as question_numbers 1–5.

NOTE: Q6 image was cut off; will be added in the next sheet.

Answer key  (clockwise positions given in comments)
──────────────────────────────────────────────────────────────────────
Q1   B (S)       — 7-person circle: M=1,P=2,S=3,N=4,Q=5,O=6,R=7.
                   Immediate left of N(4) → counterclockwise = S(3).
Q2   D (Penny)   — 5-person circle: Penny=1,Oliver=2,Sophie=3,Ryan=4,Quin=5.
                   Immediate right of Quin(5) → clockwise = Penny(1).
Q3   C (Oliver)  — 6-person circle: Max=1,Quinn=2,Oliver=3,Nora=4,Lila=5,Penny=6.
                   Exactly between Quinn(2) and Nora(4) → Oliver(3).
Q4   B           — 6-person circle: A=1,D=2,B=3,F=4,E=5,C=6.
                   E(5) = immediate left of C(6).
Q5   A (L)       — 6-person circle: J=1,M=2,O=3,P=4,K=5,L=6.
                   Immediate right of K(5) → L(6).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Seating Arrangement"
SOURCE  = "Piyush_Varshney_Seating_Arrangement"

QUESTIONS = [

    # ── Q1 ─────────────────────────────────────────────────────────────────
    # Clockwise: R-M-P-S-N-Q-O (positions 7-1-2-3-4-5-6).
    # Immediate left of N (pos 4) = counterclockwise = S (pos 3).
    {
        "question_number": 1,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Seven friends M, N, O, P, Q, R, and S are sitting around a circular "
            "table facing towards the centre. S and O are not sitting next to each "
            "other. R sits to the immediate left of M. M sits second to the left of "
            "S. Q is sitting between N and O. N is a neighbour of S. "
            "Who is sitting to the immediate left of N?"
        ),
        "question_hi": (
            "सात मित्र M, N, O, P, Q, R और S एक वृत्ताकार मेज के चारों ओर "
            "केंद्र के सम्मुख बैठे हैं। S और O एक दूसरे के निकटस्थ नहीं बैठे "
            "हैं। R, M के निकटतम बाएं बैठा है। M, S के बाईं ओर से दूसरे "
            "स्थान पर बैठा है। Q, N और O के बीच में बैठा है। N, S का पड़ोसी है। "
            "N के निकटतम बाएं कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "M",
        "option_b": "S",
        "option_c": "Q",
        "option_d": "O",
        "correct_answer": "B",   # S is immediately counterclockwise from N
    },

    # ── Q2 ─────────────────────────────────────────────────────────────────
    # Clockwise: Penny(1)-Oliver(2)-Sophie(3)-Ryan(4)-Quin(5).
    # Immediate right of Quin(5) → clockwise = Penny(1).
    {
        "question_number": 2,
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
        "correct_answer": "D",   # Penny is immediately clockwise from Quin
    },

    # ── Q3 ─────────────────────────────────────────────────────────────────
    # Clockwise: Max(1)-Quinn(2)-Oliver(3)-Nora(4)-Lila(5)-Penny(6).
    # Between Quinn(2) and Nora(4) = Oliver(3).
    {
        "question_number": 3,
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
        "correct_answer": "C",   # Oliver sits between Quinn(2) and Nora(4)
    },

    # ── Q4 ─────────────────────────────────────────────────────────────────
    # Clockwise: A(1)-D(2)-B(3)-F(4)-E(5)-C(6).
    # E(5) = immediate left of C(6).
    {
        "question_number": 4,
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
        "correct_answer": "B",   # E(5) is immediately counterclockwise from C(6)
    },

    # ── Q5 ─────────────────────────────────────────────────────────────────
    # Clockwise: J(1)-M(2)-O(3)-P(4)-K(5)-L(6).
    # Immediate right of K(5) → clockwise = L(6).
    {
        "question_number": 5,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "J, K, L, M, O and P are sitting around a circular table facing the "
            "centre. Both L and M are immediate neighbours of J. Only one person "
            "sits between M and P. O sits second to the right of J. O is not an "
            "immediate neighbour of L. "
            "Who is sitting to the immediate right of K?"
        ),
        "question_hi": (
            "J, K, L, M, O और P एक वृत्ताकार मेज के चारों ओर केंद्र की ओर "
            "उन्मुख बैठे हैं। L और M दोनों J के निकटतम पड़ोसी हैं। M और P के "
            "बीच में केवल एक व्यक्ति बैठा है। O, J के दाएं से दूसरे स्थान पर "
            "बैठा है। O, L का निकटतम पड़ोसी नहीं है। "
            "K के निकटतम दाएं कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "L",
        "option_b": "J",
        "option_c": "P",
        "option_d": "Q",
        "correct_answer": "A",   # L(6) is immediately clockwise from K(5)
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
        print(f"Topic '{TOPIC}' existing questions: {len(existing_qnums)}")
        if not existing_qnums:
            print("  → New topic! Creating first questions...")

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
