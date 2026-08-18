"""
seed_reasoning_inequality_sheet1.py
=========================================
Seeds Inequality Q37-Q40 from Gagan Pratap Reasoning PDFs (Practice Sheet).
Subject : Reasoning
Topic   : Inequality
Run     : python seed_reasoning_inequality_sheet1.py

NOTE: Existing Q1-Q36 already in DB from a previous session.
      These 4 questions from the Practice Sheet PDF are assigned Q37-Q40
      to continue the existing sequence.

Question type: Statement → two or four conclusions → choose which are true.
Standard answer options (mapped to A/B/C/D):
  For 2-conclusion questions:
    A = Only conclusion I is true
    B = Only conclusion II is true
    C = Both conclusions I and II are true
    D = Neither conclusion I nor II is true
  For 4-conclusion questions: options vary per question (stored verbatim).

Answer key (solutions verified):
  Q37 (PDF Q1)  Statement: I < M < F ≤ D ≤ S = J
      I) S < M → FALSE (M < S)
      II) F = S → FALSE (F ≤ S, equality not guaranteed)
      III) I > J → FALSE (I < J)
      IV) M < D → TRUE  (M < F ≤ D)
      Answer: A (Only conclusion IV is true)
      [CGL Tier 2 - 26 Oct 2023]

  Q38 (PDF Q2)  Statement: Z = E ≥ R > G < Y > Q = F
      I) R < F  → FALSE (chain breaks at G: R>G<Y, no R↔F relation)
      II) R ≥ Z → FALSE (Z = E ≥ R means R ≤ Z)
      Answer: D (Neither conclusion I nor II is true)
      [CGL Tier 2 - 7 March 2023]

  Q39 (PDF Q3)  Statement: Z > F ≥ A = B = G > S < E
      I) Z < A → FALSE (Z > F ≥ A, so Z > A)
      II) G < F → FALSE (F ≥ A = B = G, so F ≥ G; strict < not guaranteed)
      Answer: D (Neither conclusion I nor II is true)
      [CGL Tier 2 - 6 March 2023]

  Q40 (PDF Q4)  Statement: A = B ≥ C ≤ D > G < E < F
      I) B > F → FALSE (chain breaks: B ≥ C ≤ D, direction change, no B↔F)
      II) C < A → FALSE (A = B ≥ C, so A ≥ C; equality possible)
      Answer: C (Neither conclusion I nor II is true)
      [CGL Tier 2 - 3 March 2023]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Inequality_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Inequality"

QUESTIONS = [
    # ── Q37 (PDF Q1) ── 4-conclusion inequality; only IV is true ─────────────
    # I < M < F ≤ D ≤ S = J
    # IV: M < D follows from M < F ≤ D
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": (
            "A statement is followed by four conclusions. "
            "Which of the conclusions is/are true based on the given statement?\n"
            "Statement: I < M < F ≤ D ≤ S = J\n"
            "Conclusions:\n"
            "I) S < M\n"
            "II) F = S\n"
            "III) I > J\n"
            "IV) M < D\n"
            "[CGL Tier 2 - 26 Oct 2023]"
        ),
        "question_hi": (
            "एक कथन के बाद चार निष्कर्ष दिए गए हैं। दिए गए कथन के आधार पर कौन सा निष्कर्ष सत्य है/हैं?\n"
            "कथन: I < M < F ≤ D ≤ S = J\n"
            "निष्कर्ष:\n"
            "I) S < M\n"
            "II) F = S\n"
            "III) I > J\n"
            "IV) M < D"
        ),
        "option_a": "Only conclusion IV is true / केवल निष्कर्ष IV सत्य है",
        "option_b": "Conclusions I and III are true / निष्कर्ष I और III सत्य हैं",
        "option_c": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_d": "Conclusions IV and II are true / निष्कर्ष IV और II सत्य हैं",
        "correct_answer": "A",
        # I)S<M: FALSE (M<S); II)F=S: FALSE (F≤S, =not guaranteed);
        # III)I>J: FALSE (I<J); IV)M<D: TRUE (M<F≤D)
    },
    # ── Q38 (PDF Q2) ── 2-conclusion inequality; neither true ───────────────
    # Z = E ≥ R > G < Y > Q = F
    # I) R<F: chain breaks at G (R>G<Y), no R↔F relation → FALSE
    # II) R≥Z: Z=E≥R means R≤Z → FALSE
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": (
            "In the given question, the statement is followed by two conclusions. "
            "Which of the two conclusions is/are true?\n"
            "Statement: Z = E ≥ R > G < Y > Q = F\n"
            "Conclusions:\n"
            "I. R < F\n"
            "II. R ≥ Z\n"
            "[CGL Tier 2 - 7 March 2023]"
        ),
        "question_hi": (
            "दिए गए प्रश्न में, कथन के बाद दो निष्कर्ष दिए गए हैं। "
            "दोनों में से कौन सा/से निष्कर्ष सत्य है/हैं?\n"
            "कथन: Z = E ≥ R > G < Y > Q = F\n"
            "निष्कर्ष:\n"
            "I. R < F\n"
            "II. R ≥ Z"
        ),
        "option_a": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_d": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "D",
        # I)R<F: chain breaks at G — no relation; II)R≥Z: Z≥R so R≤Z, not R≥Z
    },
    # ── Q39 (PDF Q3) ── 2-conclusion inequality; neither true ───────────────
    # Z > F ≥ A = B = G > S < E
    # I) Z<A: Z>F≥A so Z>A → FALSE
    # II) G<F: F≥A=B=G so F≥G; strict G<F not guaranteed → FALSE
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": (
            "In this question, the statement is followed by two conclusions. "
            "Which of the two conclusion(s) is/are true?\n"
            "Statement: Z > F ≥ A = B = G > S < E\n"
            "Conclusions:\n"
            "I. Z < A\n"
            "II. G < F\n"
            "[CGL Tier 2 - 6 March 2023]"
        ),
        "question_hi": (
            "इस प्रश्न में, कथन के बाद दो निष्कर्ष दिए गए हैं। "
            "दोनों में से कौन सा/से निष्कर्ष सत्य है/हैं?\n"
            "कथन: Z > F ≥ A = B = G > S < E\n"
            "निष्कर्ष:\n"
            "I. Z < A\n"
            "II. G < F"
        ),
        "option_a": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "option_d": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "D",
        # I)Z<A: Z>F≥A → Z>A, FALSE; II)G<F: F≥A=B=G → F≥G, strict< not guaranteed, FALSE
    },
    # ── Q40 (PDF Q4) ── 2-conclusion inequality; neither true ───────────────
    # A = B ≥ C ≤ D > G < E < F
    # I) B>F: chain breaks at C (B≥C≤D) → no B↔F relation → FALSE
    # II) C<A: A=B≥C → A≥C; equality A=C possible → FALSE
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": (
            "In this question, the statement is followed by two conclusions. "
            "Which of the two conclusion(s) is/are true?\n"
            "Statement: A = B ≥ C ≤ D > G < E < F\n"
            "Conclusions:\n"
            "I. B > F\n"
            "II. C < A\n"
            "[CGL Tier 2 - 3 March 2023]"
        ),
        "question_hi": (
            "इस प्रश्न में, कथन के बाद दो निष्कर्ष दिए गए हैं। "
            "दोनों में से कौन सा/से निष्कर्ष सत्य है/हैं?\n"
            "कथन: A = B ≥ C ≤ D > G < E < F\n"
            "निष्कर्ष:\n"
            "I. B > F\n"
            "II. C < A"
        ),
        "option_a": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "option_d": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "correct_answer": "C",
        # I)B>F: chain breaks at C (B≥C≤D), direction reverses → no B↔F relation, FALSE
        # II)C<A: A=B≥C → A≥C; A=C is possible so strict < not guaranteed, FALSE
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
