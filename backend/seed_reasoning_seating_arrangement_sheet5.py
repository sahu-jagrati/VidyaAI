"""
seed_reasoning_seating_arrangement_sheet5.py
=============================================
Seeds Reasoning → Seating Arrangement  book Q23–Q25 (Piyush Varshney source).

Stored as question_numbers 46–48.

Answer key
──────────────────────────────────────────────────────────────────────
Q46 (book Q23)  C (D,H,G)  — 8-person OUTWARD-facing circle (left=CCW, right=CW).
                              Arrangement CW: D(1)–A(2)–G(3)–F(4)–H(5)–E(6)–B(7)–C(8).
                              B=2nd-left(CCW) of D: 1-2=7=B ✓; F=3rd-left of B: 7-3=4=F ✓;
                              A=2nd-left of F: 4-2=2=A ✓; C=2nd-left of A: 2-2=0→8=C ✓;
                              G=3rd-left of E: 6-3=3=G ✓; H=5 by elimination.
                              Chains: Chain1=D–B–F–A–C (rules 1-4), Chain2=E–G (rule 5),
                              H=isolated (no given relationship).
                              (a)ACE, (b)DBG, (d)CEF each have 2 from Chain1 + 1 from Chain2.
                              (c)DHG has D(Chain1)+H(isolated)+G(Chain2) → does NOT belong.

Q47 (book Q24)  B (W)      — 5-person circle: S(1)–T(2)–U(3)–V(4)–W(5).
                              S nbr of T&W → T=2,W=5. U=immediate-right of T(2)=3.
                              V nbr of U(3)&W(5): common=pos4 ✓.
                              Immediate left of S(1) = ccw = W(5).

Q48 (book Q25)  B (E)      — 9-person row facing south (left-to-right pos 1-9).
                              E=5(middle); G=1(3 between E&G, 3 left of E);
                              B=8(6 between G&B: pos 2-7); A=4(3 between B&A: pos 5-7);
                              F=6(F=A+2); remaining {C,D,H,I} at {2,3,7,9}.
                              B(8)&C not nbr → C≠7,9 → C∈{2,3}. I not nbr of E(5)→ auto ✓.
                              4th to the right of G(1) = pos 1+4 = 5 = E.
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

    # ── Q46 (book Q23) — 8-person outward-facing circle; grouping question ────
    # Arrangement CW: D(1)–A(2)–G(3)–F(4)–H(5)–E(6)–B(7)–C(8).
    # Three of (a)–(d) share the logic: 2 members from Chain D–B–F–A–C + 1 from E–G.
    # (c) D,H,G contains H (not in any given relationship) → does NOT belong.
    {
        "question_number": 46,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Eight girls A, B, C, D, E, F, G and H are sitting around a circular "
            "table facing opposite to the centre (not necessarily in the same order). "
            "B is second to the left of D. F is third to the left of B. A is second "
            "to the left of F. C is second to the left of A. G is third to the left "
            "of E. Three out of the following four options are similar by a certain "
            "logic and form a group. Which of the following does NOT belong to that group?"
        ),
        "question_hi": (
            "आठ लड़कियाँ A, B, C, D, E, F, G और H एक वृत्ताकार मेज के चारों ओर "
            "केंद्र के विपरीत उन्मुख होकर बैठी हैं (आवश्यक नहीं इसी क्रम में हों)। "
            "B, D के बायें से दूसरे स्थान पर है। F, B के बायें से तीसरे स्थान पर "
            "है। A, F के बायें से दूसरे स्थान पर है। C, A के बायें से दूसरे स्थान "
            "पर है। G, E के बायें से तीसरे स्थान पर है। "
            "निम्नलिखित चार विकल्पों में से तीन एक निश्चित तर्क से समान हैं और एक "
            "समूह बनाते हैं। निम्नलिखित में से कौन उस समूह से संबंधित नहीं है?"
        ),
        "image_url": None,
        "option_a": "A, C, E",
        "option_b": "D, B, G",
        "option_c": "D, H, G",
        "option_d": "C, E, F",
        "correct_answer": "C",   # D,H,G — H is not part of any given relationship chain
    },

    # ── Q47 (book Q24) — 5-person circle ─────────────────────────────────────
    # Clockwise: S(1)–T(2)–U(3)–V(4)–W(5).
    # S nbr of T&W: T=2, W=5. U=immediate-right of T(2)=3.
    # V nbr of U(3)&W(5): U-nbrs={2,4}, W-nbrs={4,1}→common=4 ✓.
    # Immediate left of S(1) = ccw = W(5).
    {
        "question_number": 47,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "S, T, U, V and W are sitting around a circular table facing the centre "
            "(not necessarily in the same order). S is the immediate neighbour of T "
            "and W. U is to the immediate right of T. V is the immediate neighbour "
            "of U and W. Who is sitting to the immediate left of S?"
        ),
        "question_hi": (
            "S, T, U, V और W एक वृत्ताकार मेज के चारों ओर केंद्र के सम्मुख बैठे "
            "हैं (लेकिन आवश्यक नहीं कि इसी क्रम में हों)। S, T और W का निकटतम "
            "पड़ोसी है। U, T के निकटतम दायें है। V, U और W का निकटतम पड़ोसी है। "
            "S के निकटतम बायें कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "V",
        "option_b": "W",
        "option_c": "U",
        "option_d": "T",
        "correct_answer": "B",   # W(5) is immediately counterclockwise from S(1)
    },

    # ── Q48 (book Q25) — 9-person row facing south ────────────────────────────
    # Facing south (right = toward position of higher number, 1=leftmost).
    # Positions 1–9 (left to right from observer's view).
    # E=5(middle); G=1(3 between E&G: pos2,3,4); B=8(6 between G&B: pos2-7);
    # A=4(3 between B&A: pos5=E,6,7); F=6(2nd-right of A: 4+2=6);
    # Remaining {C,D,H,I} at {2,3,7,9}; C not nbr of B(8)→C∈{2,3};
    # I not nbr of E(5)→auto satisfied; H right of D→e.g. D=2,H=3 or D=3,H=9 etc.
    # 4th to the right of G(1) = pos 1+4 = 5 = E.
    {
        "question_number": 48,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Nine people A, B, C, D, E, F, G, H, and I are sitting in a row facing "
            "south. E sits in the middle. Three people sit between E and G. Six "
            "people sit between G and B. Three people sit between B and A. F sits "
            "second to the right of A. I and E are not immediate neighbours. "
            "B and C are not neighbours. H sits to the right of D. "
            "Who is sitting fourth to the right of G?"
        ),
        "question_hi": (
            "नौ व्यक्ति A, B, C, D, E, F, G, H और I एक पंक्ति में दक्षिण की ओर "
            "मुख करके बैठे हैं। E बीच में बैठा है। E और G के बीच तीन व्यक्ति "
            "बैठे हैं। G और B के बीच छह व्यक्ति बैठे हैं। B और A के बीच तीन "
            "व्यक्ति बैठे हैं। F, A के दायें से दूसरे स्थान पर बैठा है। I और E "
            "निकटतम पड़ोसी नहीं हैं। B और C पड़ोसी नहीं हैं। H, D के दायें "
            "बैठा है। G के दायें से चौथे स्थान पर कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "A",
        "option_b": "E",
        "option_c": "F",
        "option_d": "G",
        "correct_answer": "B",   # Position G(1)+4 = pos5 = E
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
            if row[0] is not None
        }
        print(f"Topic '{TOPIC}' — existing question_numbers: {len(existing_qnums)}")

        for d in QUESTIONS:
            qn = d["question_number"]
            if qn in existing_qnums:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            book_q = qn - 23   # 46→23, 47→24, 48→25
            print(f"  INSERT Q{qn}  (book Q{book_q})")

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
