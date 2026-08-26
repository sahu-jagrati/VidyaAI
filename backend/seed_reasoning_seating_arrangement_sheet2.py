"""
seed_reasoning_seating_arrangement_sheet2.py
=============================================
Seeds Reasoning → Seating Arrangement  book Q6–Q10 (Piyush Varshney source).

Q6  → question_number 6   (WILL BE SKIPPED — already in DB as id=5858)
Q7  → question_number 30  (Q7–Q10 at 7-10 are occupied by "Class Question" rows)
Q8  → question_number 31
Q9  → question_number 32
Q10 → question_number 33

Answer key  (clockwise positions in comments)
──────────────────────────────────────────────────────────────────────
Q6   D (B)      — 6-person: A(1)–E(2)–B(3)–F(4)–C(5)–D(6).
                  Only 2 between A&F → A,F are 3 apart.
                  Only 1 between F&E → E at pos 2. C-left-of-D → C=5,D=6.
                  Immediate left of F(4) = counterclockwise = B(3). [SKIP]

Q7   C (Max)    — 6-person: Van(1)–Ruth(2)–Luke(3)–Max(4)–Jude(5)–Tess(6).
                  Van 2nd-left of Luke(3); Jude 2nd-left of Van(1)=pos5;
                  Ruth common neighbour of Luke&Van = pos2.
                  Jude(5) neighbours: Max,Tess. Luke(3) neighbours: Ruth,Max.
                  Common = Max.

Q8   A (E)      — 6-person: A(1)–E(2)–D(3)–B(4)–C(5)–F(6).
                  A neighbours E&F; B=E+2=pos4; D=F-3=pos3; C common of B&F=pos5.
                  A(1) neighbours: F,E. D(3) neighbours: E,B. Common = E.

Q9   C (S)      — 7-person: S(1)–Q(2)–T(3)–R(4)–U(5)–P(6)–V(7).
                  R=3rd right of S=pos4; R between U&T → T=3,U=5;
                  Q-T neighbours → Q=pos2; S not neighbour of P → P=6.
                  Immediate left of Q(2) = S(1).

Q10  A (Ankur)  — 6-person: Arnab(1)–Ankur(2)–Fathima(3)–Maya(4)–Vinayak(5)–Ritu(6).
                  Arnab 2nd-left of Fathima(3); Fathima 2nd-left of Vinayak(5);
                  Vinayak neighbours Ritu&Maya → Maya=4,Ritu=6;
                  Ritu common of Vinayak&Arnab → Ritu=6.
                  Fathima(3) neighbours: Ankur,Maya. Arnab(1) neighbours: Ritu,Ankur.
                  Common = Ankur.
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

    # ── Q6 (book Q6) ──────────────────────────────────────────────────────────
    # Already in DB as id=5858, question_number=6. This entry will be SKIPPED
    # by the dedup check. Included here for documentation only.
    {
        "question_number": 6,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "A, B, C, D, E and F are sitting around a circular table facing the "
            "centre. Only two people sit between A and F. Only one person sits "
            "between F and E. C sits to the immediate left of D. C is not an "
            "immediate neighbour of A. Who is sitting to the immediate left of F?"
        ),
        "question_hi": (
            "A, B, C, D, E और F एक गोलाकार मेज के चारों ओर केंद्र की ओर मुख "
            "करके बैठे हैं। A और F के बीच केवल दो लोग बैठे हैं। F और E के बीच "
            "केवल एक व्यक्ति बैठा है। C, D के तुरंत बाएं बैठा है। C, A का "
            "निकटतम पड़ोसी नहीं है। F के तुरंत बाएं कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "E",
        "option_b": "A",
        "option_c": "D",
        "option_d": "B",
        "correct_answer": "D",   # B(3) is immediately counterclockwise from F(4)
    },

    # ── Q7 (book Q7) — stored as Q30 ─────────────────────────────────────────
    # Clockwise: Van(1)–Ruth(2)–Luke(3)–Max(4)–Jude(5)–Tess(6).
    # Van 2nd-left of Luke(3) → van=pos1 ✓
    # Jude 2nd-left of Van(1) → jude=pos5 ✓
    # Ruth common neighbour of Luke(3) & Van(1) → Ruth=pos2 ✓
    # Luke(3) neighbours: Ruth(2) & Max(4) ✓
    # Jude(5) neighbours: Max(4) & Tess(6). Luke(3) neighbours: Ruth(2) & Max(4).
    # Common = Max(4).
    {
        "question_number": 30,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Six students are sitting around a circular table facing the centre. "
            "Van is sitting second to the left of Luke. Luke is an immediate "
            "neighbour of both Ruth and Max. Jude is sitting second to the left "
            "of Van. Ruth is an immediate neighbour of both Luke and Van. "
            "Who is the immediate neighbour of Jude and Luke?"
        ),
        "question_hi": (
            "छह छात्र एक गोलाकार मेज के चारों ओर केंद्र की ओर उन्मुख बैठे हैं। "
            "वैन, ल्यूक के बायीं ओर से दूसरे स्थान पर बैठी है। ल्यूक, रूथ और "
            "मैक्स दोनों का निकटतम पड़ोसी है। जूड, वैन के बायीं ओर से दूसरे "
            "स्थान पर बैठा है। रूथ, ल्यूक और वैन दोनों का निकटतम पड़ोसी है। "
            "जूड और ल्यूक का निकटतम पड़ोसी कौन है?"
        ),
        "image_url": None,
        "option_a": "Ruth/ रूथ",
        "option_b": "Tess/ टेस",
        "option_c": "Max/ मैक्स",
        "option_d": "Van/ वैन",
        "correct_answer": "C",   # Max(4) is common neighbour of Jude(5) and Luke(3)
    },

    # ── Q8 (book Q8) — stored as Q31 ─────────────────────────────────────────
    # Clockwise: A(1)–E(2)–D(3)–B(4)–C(5)–F(6).
    # A neighbours E & F: E=2, F=6 ✓
    # B is 2nd right of E(2): 2→3→4 = pos4 ✓
    # D is 3rd left of F(6): 6→5→4→3 = pos3 ✓
    # C is common neighbour of B(4) & F(6): 4-nbrs={3,5}, 6-nbrs={5,1} → C=5 ✓
    # A(1) neighbours: F(6),E(2). D(3) neighbours: E(2),B(4). Common = E(2).
    {
        "question_number": 31,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Six students — A, B, C, D, E and F — are sitting around a circular "
            "table, facing the centre. A is the immediate neighbour of both E and F. "
            "B is sitting second to the right of E. D is sitting third to the left "
            "of F. C is the immediate neighbour of both B and F. "
            "Who among the following is the immediate neighbour of both A and D?"
        ),
        "question_hi": (
            "छह विद्यार्थी A, B, C, D, E और F एक गोलाकार मेज के चारों ओर केंद्र "
            "की ओर मुख करके बैठे हैं। A, E और F दोनों का निकटतम पड़ोसी है। "
            "B, E के दायें से दूसरे स्थान पर बैठा है। D, F के बायीं ओर तीसरे "
            "स्थान पर बैठा है। C, B और F दोनों का निकटतम पड़ोसी है। "
            "निम्नलिखित में से कौन A और D दोनों का निकटतम पड़ोसी है?"
        ),
        "image_url": None,
        "option_a": "E",
        "option_b": "B",
        "option_c": "C",
        "option_d": "F",
        "correct_answer": "A",   # E(2) is common neighbour of A(1) and D(3)
    },

    # ── Q9 (book Q9) — stored as Q32 ─────────────────────────────────────────
    # Clockwise: S(1)–Q(2)–T(3)–R(4)–U(5)–P(6)–V(7).
    # R 3rd right of S(1): 1→2→3→4=R ✓
    # R between U & T: T=3, U=5 ✓
    # Q & T neighbours: Q at 4-1=3-adj or T-adj → Q=2 (T=3, Q must be at 2 or 4;
    #   4=R, so Q=2) ✓
    # S(1) not neighbour of P: S-nbrs={7,2}; P at remaining pos 6 ✓
    # Immediate left of Q(2) = counterclockwise = S(1).
    {
        "question_number": 32,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Seven friends P, Q, R, S, T, U, and V are sitting in a circle facing "
            "the centre. R is sitting third to the right of S and is in between U "
            "and T. S is not a neighbour to P. Q and T are neighbours. "
            "Who is sitting to the immediate left of Q?"
        ),
        "question_hi": (
            "सात मित्र P, Q, R, S, T, U और V केंद्र की ओर मुख करके एक वृत्त "
            "में बैठे हैं। R, S के दायीं ओर तीसरे स्थान पर बैठा है और U और T "
            "के बीच में है। S, P का पड़ोसी नहीं है। Q और T पड़ोसी हैं। "
            "Q के ठीक बाएं कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "U",
        "option_b": "P",
        "option_c": "S",
        "option_d": "R",
        "correct_answer": "C",   # S(1) is immediately counterclockwise from Q(2)
    },

    # ── Q10 (book Q10) — stored as Q33 ───────────────────────────────────────
    # Clockwise: Arnab(1)–Ankur(2)–Fathima(3)–Maya(4)–Vinayak(5)–Ritu(6).
    # Arnab 2nd-left of Fathima: Fathima = Arnab+2 = 3 ✓
    # Fathima(3) 2nd-left of Vinayak: Vinayak = Fathima+2 = 5 ✓
    # Vinayak(5) neighbours Ritu & Maya: Maya=4, Ritu=6 ✓
    # Ritu common neighbour of Vinayak(5) & Arnab(1): V-nbrs={4,6}, A-nbrs={6,2}
    #   → Ritu=6 ✓  Maya=4, Ankur=2.
    # Fathima(3) neighbours: Ankur(2), Maya(4).
    # Arnab(1) neighbours: Ritu(6), Ankur(2). Common = Ankur(2).
    {
        "question_number": 33,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Six students (Ritu, Vinayak, Arnab, Maya, Fathima and Ankur) are "
            "sitting around a circular table facing the centre (but not necessarily "
            "in the same order). Ritu is an immediate neighbour of both Vinayak and "
            "Arnab. Arnab is sitting second to Fathima's left. Fathima is sitting "
            "second to the left of Vinayak. Vinayak is an immediate neighbour of "
            "both Ritu and Maya. Who is the immediate neighbour of both Fathima "
            "and Arnab?"
        ),
        "question_hi": (
            "छः विद्यार्थी (रितु, विनायक, अर्नब, माया, फातिमा और अंकुर) एक गोल "
            "मेज के चारों ओर केंद्र की ओर मुख करके बैठे हैं (लेकिन जरूरी इसी "
            "क्रम में नहीं)। रितु, विनायक और अर्नब दोनों का निकटतम पड़ोसी है। "
            "अर्नब, फातिमा के बाएं से दूसरे स्थान पर बैठा है। फातिमा, विनायक "
            "के बाएं से दूसरे स्थान पर बैठी है। विनायक, रितु और माया दोनों का "
            "निकटतम पड़ोसी है। फातिमा और अर्नब के ठीक बीच में कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "Ankur/ अंकुर",
        "option_b": "Vinayak/ विनायक",
        "option_c": "Maya/ माया",
        "option_d": "Ritu/ रितु",
        "correct_answer": "A",   # Ankur(2) is common neighbour of Fathima(3) & Arnab(1)
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
            book_q = qn if qn <= 6 else qn - 23   # 30→7, 31→8, 32→9, 33→10
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
