"""
seed_reasoning_data_sufficiency_sheet3.py
==========================================
Seeds Data Sufficiency Q7–Q8 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Data Sufficiency

All questions use the standard fixed 5-option DS format.
Options (A)-(D) stored in DB; option (E) injected by frontend (DS_OPTION_E).

Note: The original exam pages use a non-standard 5-option format for these
questions (same custom format as Q6). The mapping from original → standard is:
  Original (A) "Data even together not sufficient"  → Standard (D) Neither
  Original (B) "Both I and II together necessary"   → Standard (E) Both together
  Original (C) "Statement II alone sufficient"      → Standard (B) Only II
  Original (D) "Either I alone or II alone"         → Standard (C) Either
  Original (E) "Statement I alone sufficient"       → Standard (A) Only I

Answer key:
  Q7  A — Among six persons A–F standing in a circle (some face centre, some
           face outside): What is A's position with respect to E?
           Stmt I : E outside; C is 2nd right of E (pos 3); C's neighbours D
                    and B (pos 2 & 4); F is 2nd left of D.
                    If D=2, B=4 → F=pos6 → A=pos5 (unique) ✓
                    If D=4, B=2 → F would be pos2 = same as B → contradiction ✗
                    Unique arrangement: E(1)D(2)C(3)B(4)A(5)F(6)
                    A is 2nd to the left of E (= 4th to the right). SUFFICIENT.
           Stmt II: B and E are 3 positions apart (2 between); both face outside;
                    E's neighbours = D & F; B's neighbours = C & A; A not adjacent D.
                    Sub-case 1 (D=2, F=6): A=5 valid → A is 4th right of E.
                    Sub-case 2 (D=6, F=2): A=3 valid → A is 2nd right of E.
                    Two different relative positions → ambiguous. NOT SUFFICIENT.
           Only Statement I is sufficient → original (E) → standard (A).

  Q8  C — How is X related to N?
           Stmt I : X is mother of J; Z is brother of J (so X is also Z's mother);
                    T is married to Z; N is daughter of T.
                    Z=N's father, X=Z's mother → X is N's paternal grandmother. ✓
           Stmt II: X married Y; Y is father of J; J is uncle of N; L has no siblings.
                    J's sibling (another child of X & Y) is N's parent.
                    X is the grandmother of N. ✓
           Each statement alone determines X is grandmother of N.
           Either I alone or II alone is sufficient → original (D) → standard (C).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Data_Sufficiency_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Data Sufficiency"

# Standard fixed options (A)-(D) — same for every Data Sufficiency question.
# Option (E) "Both Statement I and Statement II are sufficient to answer." is
# injected by the frontend (DS_OPTION_E constant).
_OPT_A = (
    "Only Statement I is sufficient to answer. / "
    "केवल कथन I उत्तर देने के लिए पर्याप्त है।"
)
_OPT_B = (
    "Only Statement II is sufficient to answer. / "
    "केवल कथन II उत्तर देने के लिए पर्याप्त है।"
)
_OPT_C = (
    "Either Statement I or Statement II is sufficient to answer. / "
    "या तो कथन I या कथन II उत्तर देने के लिए पर्याप्त है।"
)
_OPT_D = (
    "Neither Statement I nor Statement II is sufficient to answer. / "
    "न तो कथन I न ही कथन II उत्तर देने के लिए पर्याप्त है।"
)
# Option (E) injected by frontend: "Both Statement I and Statement II are sufficient."

QUESTIONS = [
    # ── Q7 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "hard",
        "question_en": (
            "Question: Among six persons A, B, C, D, E and F standing around a "
            "circle, some of them are facing the centre while others are facing "
            "outside the centre. What is the position of A with respect to E?\n\n"
            "Statement I:  C stands second to the right of E. E faces outside. "
            "C is an immediate neighbour of both D and B. F stands second to the "
            "left of D. D faces the same direction as E.\n"
            "Statement II: Only two persons stand between B and E. Both B and E "
            "face outside. E is an immediate neighbour of both D and F. B is an "
            "immediate neighbour of both C and A. A is not an immediate neighbour "
            "of D."
        ),
        "question_hi": (
            "प्रश्न: एक वृत्त के चारों ओर खड़े छह व्यक्तियों A, B, C, D, E और F "
            "में से कुछ केंद्र की ओर मुख करके और कुछ केंद्र के बाहर की ओर मुख "
            "करके खड़े हैं। E के संदर्भ में A की स्थिति क्या है?\n\n"
            "कथन I:  C, E के दाईं ओर दूसरे स्थान पर खड़ा है। E का मुख बाहर की "
            "ओर है। C, D और B दोनों का तत्काल पड़ोसी है। F, D के बाईं ओर दूसरे "
            "स्थान पर खड़ा है। D, E के समान दिशा में मुख करता है।\n"
            "कथन II: B और E के बीच केवल दो व्यक्ति खड़े हैं। B और E दोनों का "
            "मुख बाहर की ओर है। E, D और F दोनों का तत्काल पड़ोसी है। B, C और A "
            "दोनों का तत्काल पड़ोसी है। A, D का तत्काल पड़ोसी नहीं है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Stmt I alone → unique circle: E(1) D(2) C(3) B(4) A(5) F(6).
        #   A is 4th to the right (= 2nd to the left) of E. SUFFICIENT ✓
        # Stmt II alone → two valid arrangements:
        #   Case 1: E(1) D(2) C(3) B(4) A(5) F(6) → A 4th right of E
        #   Case 2: E(1) F(2) A(3) B(4) C(5) D(6) → A 2nd right of E
        #   Ambiguous → NOT SUFFICIENT ✗
        # Only Statement I is sufficient → original option (E) → standard option (A).
    },
    # ── Q8 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "Question: How is X related to N?\n\n"
            "Statement I:  X is mother of J. T is married to Z. N is daughter "
            "of T. Z is brother of J.\n"
            "Statement II: X is married to Y. Y is father of J. J is married to "
            "L. J is uncle of N. L has no siblings."
        ),
        "question_hi": (
            "प्रश्न: X, N से किस प्रकार संबंधित है?\n\n"
            "कथन I:  X, J की माँ है। T का विवाह Z से हुआ है। N, T की बेटी है। "
            "Z, J का भाई है।\n"
            "कथन II: X का विवाह Y से हुआ है। Y, J का पिता है। J का विवाह L से "
            "हुआ है। J, N का चाचा है। L का कोई भाई-बहन नहीं है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # Stmt I alone:
        #   X is mother of J; Z is brother of J → X is also mother of Z.
        #   T married Z; N is T's daughter → Z = N's father, T = N's mother.
        #   X (Z's mother) is N's paternal grandmother. ✓ SUFFICIENT.
        # Stmt II alone:
        #   X married Y; Y is J's father → X is J's mother.
        #   J is uncle of N → J's sibling (another child of X & Y) is N's parent.
        #   X is the grandmother of N. ✓ SUFFICIENT.
        # Each statement alone determines X is N's grandmother.
        # Either I alone or II alone is sufficient → original (D) → standard (C).
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
            if d["question_number"] in existing_qnums:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}")

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
