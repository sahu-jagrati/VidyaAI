"""
seed_reasoning_seating_arrangement_sheet3.py
=============================================
Seeds Reasoning → Seating Arrangement  book Q11–Q15 (Piyush Varshney source).

Stored as question_numbers 34–38 because "Class Question" rows already occupy
Q1–Q26 in this topic; these PV numbers must be offset past the existing max.

Answer key  (clockwise positions given in comments)
──────────────────────────────────────────────────────────────────────
Q34 (book Q11)  B (B)       — 6-person: A(1)–Z(2)–B(3)–Y(4)–C(5)–X(6).
                              X immediately left of A → X=6; only 1 between X&Z
                              → Z=2; C=B+2 → B=3,C=5; Y not nbr of A → Y=4.
                              Immediate right of Z(2) = clockwise = B(3).

Q35 (book Q12)  C (Rashmi)  — 6-person: Rashmi(1)–Raju(2)–Ravi(3)–Rohini(4)–
                              Ramesh(5)–Rahul(6). Ravi 2nd-right of Rashmi=3;
                              Rohini 3rd-left of Rashmi=4; Ravi between Rohini&Raju
                              → Raju=2; Rahul between Rashmi&Ramesh → pos6&5.
                              Immediate left of Raju(2) = Rashmi(1).

Q36 (book Q13)  C (A)       — 6-person: A(1)–O(2)–S(3)–R(4)–T(5)–E(6).
                              T 2nd-left of A → T=5; only 1 between A&S → S=3;
                              only 2 between S&E → E=6; R 2nd-left of E → R=4;
                              O=2. Immediate left of O(2) = A(1).

Q37 (book Q14)  C (Rajan)   — 6-person: Aaron(1)–Suhail(2)–Elroy(3)–Nelson(4)–
                              Carlton(5)–Rajan(6). Nelson immediately right of
                              Elroy; Suhail nbr of Elroy&Aaron; Rajan 2nd-left of
                              Suhail(2) = pos6; Carlton nbr of Nelson(4) = pos5.
                              Aaron(1) nbrs: Rajan,Suhail. Carlton(5) nbrs: Nelson,
                              Rajan. Common = Rajan(6).

Q38 (book Q15)  B (Sunil)   — 7-person OUTWARD-facing (left=clockwise, right=ccw):
                              Amit(1)–Deepak(2)–Bablu(3)–Imran(4)–Ramesh(5)–
                              Sanju(6)–Sunil(7). Ramesh 4th-left(clockwise) of
                              Amit=5; Sanju 2nd-left(cw) of Imran → Imran=4,Sanju=6;
                              Amit not adj Imran/Sanju ✓; Bablu not adj Amit → 3;
                              Deepak adj Bablu → 2. Immediate right(ccw) of Amit
                              = pos7 = Sunil.
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

    # ── Q34 (book Q11) ────────────────────────────────────────────────────────
    # Clockwise: A(1)–Z(2)–B(3)–Y(4)–C(5)–X(6).
    # X immediately left of A → X=6 (ccw of A=1). X&Z one person apart → Z=2.
    # C second right of B: B=3,C=5. Y not neighbour of A(1); A-nbrs={6,2}: Y=4 ✓.
    # Immediate right of Z(2) = clockwise = B(3).
    {
        "question_number": 34,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "A, B, C, X, Y and Z are sitting around a circular table facing the "
            "centre (but not necessarily in the same order). X sits to the "
            "immediate left of A. Only one person sits between X and Z. C sits "
            "second to the right of B. Y is not an immediate neighbour of A. "
            "Who is sitting to the immediate right of Z?"
        ),
        "question_hi": (
            "A, B, C, X, Y और Z एक गोलाकार मेज के चारों ओर केंद्र की ओर मुंह "
            "करके बैठे हैं (लेकिन जरूरी नहीं इसी क्रम में)। X, A के ठीक बाएं "
            "बैठा है। X और Z के बीच केवल एक व्यक्ति बैठा है। C, B के दायें से "
            "दूसरे स्थान पर बैठा है। Y, A का निकटतम पड़ोसी नहीं है। "
            "Z के ठीक दाएं कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "C",
        "option_b": "B",
        "option_c": "A",
        "option_d": "Y",
        "correct_answer": "B",   # B(3) is immediately clockwise from Z(2)
    },

    # ── Q35 (book Q12) ────────────────────────────────────────────────────────
    # Clockwise: Rashmi(1)–Raju(2)–Ravi(3)–Rohini(4)–Ramesh(5)–Rahul(6).
    # Ravi 2nd-right of Rashmi(1): 1→2→3 = Ravi ✓.
    # Rohini 3rd-left of Rashmi(1): ccw 3 = pos4 ✓.
    # Ravi(3) between Rohini(4) & Raju(2): Raju(2)–Ravi(3)–Rohini(4) ✓.
    # Rahul between Rashmi(1) & Ramesh(5): Rashmi(1)–Rahul(6)–Ramesh(5) (ccw) ✓.
    # Immediate left of Raju(2) = ccw = Rashmi(1).
    {
        "question_number": 35,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Six friends are playing a bottle-spinning game around a circular "
            "table, facing the centre. Rohini is sitting third to the left of "
            "Rashmi. Rahul is sitting in between Rashmi and Ramesh. Ravi is "
            "sitting in between Rohini and Raju. Ravi is sitting second to the "
            "right of Rashmi. Who among the following is sitting to the immediate "
            "left of Raju?"
        ),
        "question_hi": (
            "छह दोस्त एक गोलाकार मेज के चारों ओर केंद्र की ओर मुंह करके बोतल "
            "घुमाने का खेल खेल रहे हैं। रोहिणी, रश्मि के तीसरे स्थान पर बाईं "
            "ओर बैठी है। राहुल, रश्मि और रमेश के बीच में बैठा है। रवि, रोहिणी "
            "और राजू के बीच में बैठा है। रवि, रश्मि के दायें से दूसरे स्थान "
            "पर बैठा है। निम्नलिखित में से कौन राजू के ठीक बाईं ओर बैठा है?"
        ),
        "image_url": None,
        "option_a": "Rohini/ रोहिणी",
        "option_b": "Rahul/ राहुल",
        "option_c": "Rashmi/ रश्मि",
        "option_d": "Ramesh/ रमेश",
        "correct_answer": "C",   # Rashmi(1) is immediately counterclockwise from Raju(2)
    },

    # ── Q36 (book Q13) ────────────────────────────────────────────────────────
    # Clockwise: A(1)–O(2)–S(3)–R(4)–T(5)–E(6).
    # T 2nd-left of A(1): ccw 2 = pos5 ✓. Only 1 between A(1) & S: S=3 ✓.
    # Only 2 between S(3) & E: both directions give E=6 (3 apart) ✓.
    # R 2nd-left of E(6): ccw 2 = pos4 ✓. Remaining O=2.
    # Immediate left of O(2) = ccw = A(1).
    {
        "question_number": 36,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "A, E, O, R, S and T are sitting around a circular table facing the "
            "centre (but not necessarily in the same order). Only one person sits "
            "between A and S. Only two people sit between S and E. R sits second "
            "to the left of E. T sits second to the left of A. "
            "Who is sitting to the immediate left of O?"
        ),
        "question_hi": (
            "A, E, O, R, S और T एक गोल मेज के परितः उसके केंद्र की ओर अभिमुख "
            "होकर बैठे हैं (लेकिन इसी क्रम में जरूरी नहीं)। A और S के बीच "
            "केवल एक व्यक्ति बैठा है। S और E के बीच केवल दो व्यक्ति बैठे हैं। "
            "R, E के बायें से दूसरे स्थान पर बैठा है। T, A के बायें से दूसरे "
            "स्थान पर बैठा है। O के ठीक बाईं कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "T",
        "option_b": "R",
        "option_c": "A",
        "option_d": "S",
        "correct_answer": "C",   # A(1) is immediately counterclockwise from O(2)
    },

    # ── Q37 (book Q14) ────────────────────────────────────────────────────────
    # Clockwise: Aaron(1)–Suhail(2)–Elroy(3)–Nelson(4)–Carlton(5)–Rajan(6).
    # Nelson immediately right of Elroy(3): Nelson=4 ✓.
    # Suhail nbr of Elroy(3) & Aaron(1): common pos = 2 ✓.
    # Rajan 2nd-left of Suhail(2): ccw 2 = pos6 ✓.
    # Carlton nbr of Nelson(4): Carlton at 3=Elroy or 5 → Carlton=5 ✓.
    # Aaron(1) nbrs: Rajan(6), Suhail(2). Carlton(5) nbrs: Nelson(4), Rajan(6).
    # Common neighbour = Rajan(6).
    {
        "question_number": 37,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Six scientists are sitting around a circular table facing the centre. "
            "Suhail is an immediate neighbour of Elroy and Aaron. Nelson is sitting "
            "to the immediate right of Elroy. Rajan is sitting second to the left "
            "of Suhail. Carlton is an immediate neighbour of Nelson. "
            "Who is the immediate neighbour of both Aaron and Carlton?"
        ),
        "question_hi": (
            "छह वैज्ञानिक एक गोल मेज के परितः उसके केंद्र की ओर अभिमुख होकर "
            "बैठे हैं। सुहैल, एलरॉय और आरोन का निकटतम पड़ोसी है। नेल्सन, एलरॉय "
            "के ठीक दाएं बैठा है। राजन, सुहैल के बायें से दूसरे स्थान पर बैठा "
            "है। कार्लटन, नेल्सन का निकटतम पड़ोसी है। "
            "आरोन और कार्लटन के बीच में कौन बैठा है?"
        ),
        "image_url": None,
        "option_a": "Suhail/ सुहैल",
        "option_b": "Elroy/ एलरॉय",
        "option_c": "Rajan/ राजन",
        "option_d": "Nelson/ नेल्सन",
        "correct_answer": "C",   # Rajan(6) is common nbr of Aaron(1) and Carlton(5)
    },

    # ── Q38 (book Q15) ────────────────────────────────────────────────────────
    # OUTWARD-FACING circle (facing opposite the centre):
    #   left = clockwise, right = counterclockwise.
    # Clockwise: Amit(1)–Deepak(2)–Bablu(3)–Imran(4)–Ramesh(5)–Sanju(6)–Sunil(7).
    # Ramesh 4th-left (=clockwise) of Amit(1): 1→2→3→4→5 = Ramesh ✓.
    # Sanju 2nd-left (=clockwise) of Imran: try Imran=4 → 4→5→6=Sanju ✓.
    # Amit(1) not adj Imran(4) or Sanju(6): Amit nbrs={2,7} → neither 4 nor 6 ✓.
    # Bablu not adj Amit(1): Bablu ≠ 2,7 → Bablu=3 ✓.
    # Deepak & Bablu(3) adj: Deepak=2 or 4=Imran → Deepak=2 ✓. Sunil=7.
    # Immediate RIGHT (=ccw) of Amit(1) = pos7 = Sunil.
    {
        "question_number": 38,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Amit, Bablu, Ramesh, Deepak, Imran, Sunil, and Sanju are sitting "
            "around a circular table facing opposite the centre. Amit does not sit "
            "adjacent to Imran and Sanju. Bablu does not sit adjacent to Amit. "
            "Sanju sits second to the left of Imran. Ramesh sits fourth to the "
            "left of Amit. Deepak and Bablu sit adjacent to each other. "
            "Who sits to the immediate right of Amit?"
        ),
        "question_hi": (
            "अमित, बब्लू, रमेश, दीपक, इमरान, सुनील और संजू एक वृत्ताकार मेज "
            "के चारों ओर केंद्र की ओर उन्मुख होकर बैठे हैं। अमित, इमरान और "
            "संजू के आसन्न नहीं बैठा है। बब्लू अमित के आसन्न नहीं बैठा है। "
            "संजू, इमरान के बायें से दूसरे स्थान पर बैठा है। रमेश, अमित के "
            "बायें से चौथे स्थान पर बैठा है। दीपक और बब्लू एक दूसरे के आसन्न "
            "बैठे हैं। अमित के ठीक दायें कौन बैठे हैं?"
        ),
        "image_url": None,
        "option_a": "Bablu/ बब्लू",
        "option_b": "Sunil/ सुनील",
        "option_c": "Ramesh/ रमेश",
        "option_d": "Sanju/ संजू",
        "correct_answer": "B",   # Sunil(7) is immediately counterclockwise from Amit(1)
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
            book_q = qn - 23   # 34→11, 35→12, 36→13, 37→14, 38→15
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
