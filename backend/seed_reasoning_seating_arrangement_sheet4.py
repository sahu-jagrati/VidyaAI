"""
seed_reasoning_seating_arrangement_sheet4.py
=============================================
Seeds Reasoning → Seating Arrangement  book Q16–Q22 (Piyush Varshney source).

Stored as question_numbers 39–45 (Class Question rows occupy Q1–Q26; PV
questions continue from the last inserted batch which ended at Q38).

Answer key
──────────────────────────────────────────────────────────────────────
Q39 (book Q16)  B (P)       — Linear queue, 5 people: M,N,O,P,Q.
                              Only P between M&Q → M-P-Q or Q-P-M;
                              O ahead of only N → O=4th, N=5th.
                              Both orderings give P at position 2.

Q40 (book Q17)  D (G3)      — 7-person circle: G1(1)–G3(2)–G5(3)–G7(4)–
                              G4(5)–G6(6)–G2(7).
                              G6=2nd-left of G1=pos6; G7=2nd-left of G6=pos4;
                              G5=3rd-right of G2(7)=pos3; G4=3rd-right of G3(2)=pos5.
                              2nd-left of G7(4) = ccw2 = pos2 = G3.

Q41 (book Q18)  C (Kaushal) — 6-person: Aryan(1)–Arshit(2)–Harsh(3)–Puneet(4)–
                              Kaushal(5)–Shreya(6). Puneet=Aryan+3=4;
                              Shreya=Puneet+2=6; Harsh=2nd-left of Kaushal(5)=3;
                              Arshit=2. Shreya nbrs: Kaushal,Aryan. Puneet nbrs:
                              Harsh,Kaushal. Common = Kaushal.

Q42 (book Q19)  C (C)       — Linear line (8 people facing north):
                              F(1)–C(2)–B(3)–G(4)–D(5)–H(6)–E(7)–A(8).
                              F at extreme-end=1; B=F+2=3; E=B+4=7;
                              C=D-3 → C=2,D=5,A=8; G not nbr of E(7) → G=4,H=6.
                              Immediate left of B(3) = C(2).

Q43 (book Q20)  A (B)       — 5-person circle: E(1)–C(2)–B(3)–A(4)–D(5).
                              B=E+2=3; A=E-2=4; C not nbr of D or A → C=2,D=5.
                              Immediate right of C(2) = B(3).

Q44 (book Q21)  C (R)       — 6-person circle: U(1)–R(2)–T(3)–S(4)–Q(5)–P(6).
                              Q=2nd-left of U=5; P between Q&U=6; T=3rd-right of P(6)=3;
                              S not nbr of U → S=4, R=2.
                              U(1) nbrs: P,R. T(3) nbrs: R,S. Common = R.

Q45 (book Q22)  D (G)       — 5-person circle: C(1)–H(2)–P(3)–B(4)–G(5).
                              H=immediate-right of C=2; B=3rd-left of H=4;
                              P not nbr of C → P=3, G=5.
                              Immediate left of C(1) = ccw = G(5).
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

    # ── Q39 (book Q16) — Linear queue ─────────────────────────────────────────
    # 5 people in a queue. P is between M & Q → M-P-Q or Q-P-M at positions 1-3.
    # O is ahead of only N → O is 4th, N is 5th.
    # Either way, position 2 is P.
    {
        "question_number": 39,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            "M, N, O, P, and Q are standing in a queue to place their order in a "
            "restaurant. Only P is standing between M and Q. O is ahead of only N. "
            "Who is standing second in the line if there is no other person in the queue?"
        ),
        "question_hi": (
            "M, N, O, P और Q एक रेस्टोरेंट में अपना ऑर्डर देने के लिए पंक्ति "
            "में खड़े हैं। केवल P, M और Q के बीच में खड़ा है। O केवल N से आगे "
            "है। यदि पंक्ति में कोई अन्य व्यक्ति नहीं है तो पंक्ति में दूसरे "
            "स्थान पर कौन खड़ा है?"
        ),
        "image_url": None,
        "option_a": "O",
        "option_b": "P",
        "option_c": "Q",
        "option_d": "M",
        "correct_answer": "B",   # P is always at position 2 in both valid orderings
    },

    # ── Q40 (book Q17) — 7-person circle ─────────────────────────────────────
    # Clockwise: G1(1)–G3(2)–G5(3)–G7(4)–G4(5)–G6(6)–G2(7).
    # G6=2nd-left of G1(1): ccw2=pos6 ✓. G7=2nd-left of G6(6): ccw2=pos4 ✓.
    # G5=3rd-right of G2(7): cw3=pos3 ✓. G5(3) not nbr of G6(6): G6 nbrs={5,7}✓.
    # G4=3rd-right of G3(2): cw3=pos5 ✓. G4(5),G3(2) not nbr: |5-2|=3 ✓.
    # 2nd-left of G7(4) = ccw2 = pos2 = G3.
    {
        "question_number": 40,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Seven girls G1, G2, G3, G4, G5, G6, and G7 are sitting around a "
            "circular table facing the centre (not necessarily in the same order). "
            "G6 is second to the left of G1. G7 is second to the left of G6. "
            "G5 is third to the right of G2. G5 is not the immediate neighbour of G6. "
            "G4 is third to the right of G3. G4 and G3 are not immediate neighbours. "
            "Who is second to the left of G7?"
        ),
        "question_hi": (
            "सात लड़कियाँ G1, G2, G3, G4, G5, G6 और G7 एक वृत्ताकार मेज के "
            "चारों ओर केंद्र की ओर उन्मुख होकर बैठी हैं (जरूरी नहीं इसी क्रम में)। "
            "G6, G1 के बायें से दूसरे स्थान पर है। G7, G6 के बायें से दूसरे "
            "स्थान पर है। G5, G2 के दायें से तीसरे स्थान पर है। G5, G6 का "
            "निकटतम पड़ोसी नहीं है। G4, G3 के दायें से तीसरे स्थान पर है। "
            "G4, G3 के निकटतम पड़ोसी नहीं हैं। G7 के बायें से दूसरा कौन है?"
        ),
        "image_url": None,
        "option_a": "G2",
        "option_b": "G1",
        "option_c": "G4",
        "option_d": "G3",
        "correct_answer": "D",   # G3(2) is 2nd counterclockwise from G7(4)
    },

    # ── Q41 (book Q18) — 6-person circle ─────────────────────────────────────
    # Clockwise: Aryan(1)–Arshit(2)–Harsh(3)–Puneet(4)–Kaushal(5)–Shreya(6).
    # Puneet=3rd-right of Aryan(1): cw3=4 ✓.
    # Shreya=2nd-right of Puneet(4): cw2=6 ✓.
    # Harsh=2nd-left of Kaushal(5): ccw2=3 ✓. Arshit=2.
    # Arshit&Harsh not nbr of Shreya(6): Shreya nbrs={5,1}; Arshit=2,Harsh=3 ✓.
    # Shreya(6) nbrs: Kaushal(5),Aryan(1). Puneet(4) nbrs: Harsh(3),Kaushal(5).
    # Common = Kaushal(5).
    {
        "question_number": 41,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Six students, Aryan, Shreya, Arshit, Puneet, Kaushal and Harsh, are "
            "sitting around a circular table facing the centre (but not necessarily "
            "in the same order). Shreya is sitting second to the right of Puneet. "
            "Arshit and Harsh are not the immediate neighbours of Shreya. Puneet is "
            "third to the right of Aryan. Harsh is sitting second to the left of "
            "Kaushal. Who is the immediate neighbour of Shreya and Puneet?"
        ),
        "question_hi": (
            "छह छात्र- आर्यन, श्रेया, अर्शित, पुनीत, कौशल और हर्ष, एक वृत्ताकार "
            "मेज के चारों ओर केंद्र की ओर मुख करके बैठे हैं (लेकिन आवश्यक नहीं "
            "कि इसी क्रम में हों)। श्रेया, पुनीत के दायें से दूसरे स्थान पर "
            "बैठी है। अर्शित और हर्ष, श्रेया के निकटतम पड़ोसी नहीं हैं। पुनीत, "
            "आर्यन के दायें से तीसरे स्थान पर बैठा है। हर्ष, कौशल के बायें से "
            "दूसरे स्थान पर बैठा है। श्रेया और पुनीत का निकटतम पड़ोसी कौन है?"
        ),
        "image_url": None,
        "option_a": "Aryan/ आर्यन",
        "option_b": "Harsh/ हर्ष",
        "option_c": "Kaushal/ कौशल",
        "option_d": "Arshit/ अर्शित",
        "correct_answer": "C",   # Kaushal(5) is common nbr of Shreya(6) & Puneet(4)
    },

    # ── Q42 (book Q19) — 8-person straight line ───────────────────────────────
    # All facing north (left = west, right = east in the line).
    # Left-to-right: F(1)–C(2)–B(3)–G(4)–D(5)–H(6)–E(7)–A(8).
    # F at extreme end=1; B=2nd-right of F=3; only 3 between B(3)&E: E=7;
    # C=3rd-left of D → C=2,D=5; only 2 between D(5)&A: A=8;
    # G not nbr of E(7) → G=4 (not 6), H=6.
    # Immediate left of B(3) = pos2 = C.
    {
        "question_number": 42,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Eight friends A, B, C, D, E, F, G and H are seated in a straight line "
            "and all of them are facing north, but not necessarily in the same order. "
            "B sits second to right of F. F sits at one of the extreme ends of the "
            "line. Only three people sit between B and E. C sits third to the left "
            "of D. Only two people sit between D and A. G is not an immediate "
            "neighbour of E. Who is sitting on the immediate left of B?"
        ),
        "question_hi": (
            "आठ मित्र- A, B, C, D, E, F, G और H एक सीधी पंक्ति में बैठे हैं और "
            "वे सभी उत्तर की ओर सम्मुख हैं, लेकिन आवश्यक नहीं कि वे समान क्रम "
            "में हों। B, F के दायें से दूसरे स्थान पर बैठा है। F पंक्ति के एक "
            "छोर पर बैठा है। B और E के बीच केवल तीन व्यक्ति बैठे हैं। C, D के "
            "बायें से तीसरे स्थान पर बैठा है। D और A के बीच में केवल दो लोग "
            "बैठे हैं। G, E का निकटतम पड़ोसी नहीं है। B के निकटतम बाईं ओर "
            "कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "F",
        "option_b": "A",
        "option_c": "C",
        "option_d": "G",
        "correct_answer": "C",   # C(2) is immediately to the left of B(3)
    },

    # ── Q43 (book Q20) — 5-person circle ─────────────────────────────────────
    # Clockwise: E(1)–C(2)–B(3)–A(4)–D(5).
    # B=2nd-right of E(1): cw2=3 ✓. A=2nd-left of E(1): ccw2=pos4 ✓.
    # C not nbr of D&A: nbrs of C(2)={1=E,3=B}; D=5,A=4 → neither 5 nor 4 ✓.
    # Immediate right of C(2) = cw = B(3).
    {
        "question_number": 43,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Five persons A, B, C, D and E are sitting around a circular table "
            "facing towards the centre (not necessarily in the same order). "
            "C is not an immediate neighbour of D and A. B is sitting second to "
            "the right of E. A is sitting second to the left of E. "
            "Who is sitting on the immediate right of C?"
        ),
        "question_hi": (
            "पाँच व्यक्ति A, B, C, D और E एक वृत्ताकार मेज के चारों ओर केंद्र "
            "के सम्मुख बैठे हैं (आवश्यक नहीं कि इसी क्रम में)। C, D और A का "
            "निकटतम पड़ोसी नहीं है। B, E के दायें से दूसरे स्थान पर बैठा है। "
            "A, E के बायें से दूसरे स्थान पर बैठा है। C के निकटतम दायें कौन "
            "बैठा है?"
        ),
        "image_url": None,
        "option_a": "B",
        "option_b": "E",
        "option_c": "A",
        "option_d": "D",
        "correct_answer": "A",   # B(3) is immediately clockwise from C(2)
    },

    # ── Q44 (book Q21) — 6-person circle ─────────────────────────────────────
    # Clockwise: U(1)–R(2)–T(3)–S(4)–Q(5)–P(6).
    # Q=2nd-left of U(1): ccw2=pos5 ✓. P nbr of both Q(5)&U(1): P at pos6 ✓.
    # T=3rd-right of P(6): cw3=pos9→3 ✓. S not nbr of U(1): nbrs={6,2}→S≠6,2;
    # remaining {2,4} for R,S → S=4,R=2 ✓.
    # U(1) nbrs: P(6),R(2). T(3) nbrs: R(2),S(4). Common = R(2).
    {
        "question_number": 44,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Six students — P, Q, R, S, T and U — are sitting around a circular "
            "table, facing the centre. Q is sitting second to the left of U. "
            "T is sitting third to the right of P. P is the immediate neighbour "
            "of Q and U. S is not the neighbour of U. "
            "Who among the following is the neighbour of both U and T?"
        ),
        "question_hi": (
            "छः छात्र - P, Q, R, S, T और एक गोलाकार मेज के चारों ओर केंद्र "
            "की ओर उन्मुख बैठे हैं। Q, U के बायें से दूसरे स्थान पर बैठा है। "
            "T, P के दायें से तीसरे स्थान पर बैठा है। P, Q और U का निकटतम "
            "पड़ोसी है। S, U का पड़ोसी नहीं है। "
            "निम्नलिखित में से कौन U और T दोनों का पड़ोसी है?"
        ),
        "image_url": None,
        "option_a": "P",
        "option_b": "S",
        "option_c": "R",
        "option_d": "Q",
        "correct_answer": "C",   # R(2) is common nbr of U(1) and T(3)
    },

    # ── Q45 (book Q22) — 5-person circle ─────────────────────────────────────
    # Clockwise: C(1)–H(2)–P(3)–B(4)–G(5).
    # H=immediate-right of C(1): cw1=2 ✓. B=3rd-left of H(2): ccw3=pos5→pos4 ✓.
    # Wait: ccw 3 from H(2): 2→1→5→4 = pos4, so B=4 ✓.
    # P not nbr of C(1): C nbrs={2=H,5=G}; remaining {3,5} → P≠5, so P=3,G=5 ✓.
    # Immediate left of C(1) = ccw = pos5 = G.
    {
        "question_number": 45,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            "Five friends P, B, C, G, and H are sitting around a circular table "
            "facing towards the centre. H is sitting to the immediate right of C. "
            "B is sitting third to the left of H. P is not an immediate neighbour "
            "of C. Who is sitting on the immediate left of C?"
        ),
        "question_hi": (
            "पाँच मित्र P, B, C, G और H एक गोलाकार मेज के चारों ओर केंद्र की "
            "ओर मुँह करके बैठे हैं। H, C के ठीक दाईं ओर बैठा है। B, H के "
            "बायीं ओर से तीसरे स्थान पर बैठा है। P, C का निकटतम पड़ोसी नहीं है। "
            "C के ठीक बाईं ओर कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "H",
        "option_b": "B",
        "option_c": "P",
        "option_d": "G",
        "correct_answer": "D",   # G(5) is immediately counterclockwise from C(1)
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
            book_q = qn - 23   # 39→16, 40→17, ..., 45→22
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
