"""
seed_reasoning_data_sufficiency_sheet2.py
==========================================
Seeds Data Sufficiency Q3-Q6 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Data Sufficiency

All questions use the standard fixed 5-option DS format.
Options (A)-(D) stored in DB; option (E) injected by frontend (DS_OPTION_E).

Answer key:
  Q3  E — Who is oldest among A, B, C, D, E, F?
           Stmt I : B ≥ A > C ≥ D (no info on E or F) → ✗
           Stmt II: D > E and D > F (no info on A, B, C) → ✗
           Both  : B > A > C > D > {E, F} → B is oldest ✓
           Both Statement I and II are sufficient.

  Q4  E — P, Q, R, S, T: How many persons are taller than T?
           Stmt I : {T, P} > Q > {R, S} but T vs P unknown → ✗
           Stmt II: T > P > R but Q, S positions unknown → ✗
           Both  : T > P > Q > {R, S} → 0 persons taller than T ✓
           Both Statement I and II are sufficient.

  Q5  B — A, B, C, D, E in a 5-floor building: On which floor does C live?
           Stmt I : D on floor 5; A below D — no info on C → ✗
           Stmt II: E lives 2 floors above C; C ≠ 2nd or 3rd floor.
                    C=4→E=6 ✗; C=5→E=7 ✗ → only C=1, E=3 works ✓
           Only Statement II is sufficient.

  Q6  A — 19-person line: How many persons stand between L and K?
           Stmt I : Y=pos1, K=pos7, R=pos14, L=pos19 → L−K−1=11 persons ✓
           Stmt II: J at middle(pos10); K=J−3=pos7; "L to left of K" and
                    "2 between J and L" → L=7 or 13, but both contradict L<7
                    → self-contradictory / insufficient ✗
           Only Statement I is sufficient.
           Note: The original exam question uses a non-standard 5-option format
           for Q6 where "only I sufficient" maps to option (E). We store it using
           the standard DS options so correct_answer = "A" here.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Data_Sufficiency_Sheet2"
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
    # ── Q3 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": (
            "Question: Who among the following was oldest among A, B, C, D, E, F?\n\n"
            "Statement I:  A is older than C but not older than B. "
            "D is not older than C.\n"
            "Statement II: D was older than both E and F."
        ),
        "question_hi": (
            "प्रश्न: निम्नलिखित में से कौन A, B, C, D, E, F में सबसे बड़ा था?\n\n"
            "कथन I:  A, C से बड़ा है लेकिन B से बड़ा नहीं है। D, C से बड़ा नहीं है।\n"
            "कथन II: D, E और F दोनों से बड़ा था।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "E",
        # Stmt I alone : B ≥ A > C ≥ D; E and F positions unknown → ✗
        # Stmt II alone: D > E, D > F; A, B, C positions unknown → ✗
        # Both together: B ≥ A > C ≥ D > {E, F} → B is the oldest ✓
        # Both Statement I and Statement II are sufficient → (E).
    },
    # ── Q4 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "Question: P, Q, R, S and T are the five persons in the group. "
            "How many persons are taller than T?\n\n"
            "Statement I:  P is taller than Q, who was only shorter than P and T.\n"
            "Statement II: R is shorter than P, who was shorter than T."
        ),
        "question_hi": (
            "प्रश्न: P, Q, R, S और T समूह में पांच व्यक्ति हैं। "
            "कितने व्यक्ति T से लम्बे हैं?\n\n"
            "कथन I:  P, Q से लंबा है, जो केवल P और T से छोटा था।\n"
            "कथन II: R, P से छोटा है, जो T से छोटा था।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "E",
        # Stmt I alone : T > Q, P > Q, Q > R and Q > S; T vs P unknown → ✗
        # Stmt II alone: T > P > R; Q and S positions unknown → ✗
        # Both together: T > P (from II) > Q (from I) > {R, S} (from I)
        #               → 0 persons taller than T ✓
        # Both Statement I and Statement II are sufficient → (E).
    },
    # ── Q5 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "Question: If A, B, C, D, E are living in a building with floors "
            "numbered 1 (lowest) to 5 (topmost). On which floor does C live?\n\n"
            "Statement I:  A lives on one of the floors below D, "
            "who lives in the topmost floor.\n"
            "Statement II: E lives two floors above C, who neither lives in the "
            "third nor second floor."
        ),
        "question_hi": (
            "प्रश्न: यदि A, B, C, D, E एक इमारत में रह रहे हैं। इमारत की सबसे "
            "निचली मंजिल की संख्या 1 है और सबसे ऊपरी मंजिल की संख्या 5 है। "
            "C किस मंजिल पर रहता है?\n\n"
            "कथन I:  A, D के नीचे किसी एक मंजिल पर रहता है, "
            "जो सबसे ऊपरी मंजिल पर रहता है।\n"
            "कथन II: E, C से दो मंजिल ऊपर रहता है, जो न तो तीसरी "
            "और न ही दूसरी मंजिल पर रहता है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # Stmt I alone : D on floor 5; A on floors 1–4. No info about C → ✗
        # Stmt II alone: C ≠ floor 2 or 3; E = C + 2 floors.
        #   C=1 → E=3 ✓  |  C=4 → E=6 ✗  |  C=5 → E=7 ✗
        #   ∴ C must be on floor 1, E on floor 3 ✓
        # Only Statement II is sufficient → (B).
    },
    # ── Q6 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "hard",
        "question_en": (
            "Question: How many persons are standing between L and K "
            "in a straight line of 19 persons? "
            "(Note: All are standing in a straight line, facing north.)\n\n"
            "Statement I:  Y stands on the extreme left end of the line. "
            "Only five persons stand between Y and K. "
            "Only six persons stand between K and R. "
            "Only four persons stand between R and L.\n"
            "Statement II: J stands exactly in the middle of the line. "
            "Only two persons stand between J and L. "
            "Only five persons stand between L and K. "
            "L stands to the left of K. "
            "K stands third to the left of J."
        ),
        "question_hi": (
            "प्रश्न: 19 व्यक्तियों की एक सीधी रेखा में L और K के बीच "
            "कितने व्यक्ति खड़े हैं? "
            "(नोट: सभी उत्तर दिशा की ओर मुंह करके एक सीधी रेखा में खड़े हैं।)\n\n"
            "कथन I:  Y पंक्ति के सबसे बाएं छोर पर खड़ा है। "
            "Y और K के बीच केवल पांच व्यक्ति खड़े हैं। "
            "K और R के बीच केवल छह व्यक्ति खड़े हैं। "
            "R और L के बीच केवल चार व्यक्ति खड़े हैं।\n"
            "कथन II: J पंक्ति के ठीक मध्य में खड़ा है। "
            "J और L के बीच केवल दो व्यक्ति खड़े हैं। "
            "L और K के बीच केवल पांच व्यक्ति खड़े हैं। "
            "L, K के बाईं ओर खड़ा है। "
            "K, J के बाईं ओर तीसरे स्थान पर है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Stmt I alone :
        #   Y=pos1 → K=pos7 (5 between) → R=pos14 (6 between) → L=pos19 (4 between)
        #   Persons between L and K = 19 − 7 − 1 = 11 ✓  SUFFICIENT.
        # Stmt II alone:
        #   J=pos10 (middle); K=J−3=pos7; "L to left of K" → L<7;
        #   "2 between J and L" → L=7 or 13; neither < 7 → self-contradictory → ✗
        # Only Statement I is sufficient → (A).
        # [The original exam uses a non-standard 5-option format for this question
        #  where "only I sufficient" appears as option (E). Stored here as standard
        #  DS option (A) so correct_answer = "A".]
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
