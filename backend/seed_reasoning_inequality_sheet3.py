"""
seed_reasoning_inequality_sheet3.py
=========================================
Seeds Inequality Q13-Q20 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Inequality
Run     : python seed_reasoning_inequality_sheet3.py

Answer key (solutions verified):
  Q13  Statements: A=B>C ; E≤D<C ; E≥F>G=H
       Combined chain: A=B > C > D ≥ E ≥ F > G = H
       I)  A > E → TRUE  (A > C > D ≥ E)
       II) D ≥ F → TRUE  (D ≥ E ≥ F)
       Answer: D  (Both Conclusions I and II follow)

  Q14  Statements: J > I = H ; J < K ≤ L ; L = M ≥ N > O
       Combined chain: H = I < J < K ≤ L = M ≥ N > O
       I)  K > H → TRUE  (H = I < J < K)
       II) L > O → TRUE  (L = M ≥ N > O)
       Answer: D  (Both I and II follow)

  Q15  Statements: D=E>F ; H≤G<F ; H≥I>J=K
       Combined chain: D = E > F > G ≥ H ≥ I > J = K
       I)   D > H → TRUE   (D > F > G ≥ H)
       II)  G ≥ I → TRUE   (G ≥ H ≥ I)
       III) F < K → FALSE  (F > G ≥ H ≥ I > J = K → F > K)
       Answer: D  (Both Conclusions I and II follow)

  Q16  Statements: A > B ; B = C ; D = M > E < C
       From A > B = C > E:
       I)  A > E → TRUE  (A > B = C > E)
       II) E < B → TRUE  (B = C > E → E < B)
       Answer: D  (Both I and II follow)

  Q17  Statements: L > M ; M ≤ O = N ; L = Q < K
       I)  K > M → TRUE   (K > Q = L > M)
       II) O ≤ K → FALSE  (chain breaks at M: O ≥ M < L = Q < K, no O↔K)
       Answer: B  (Only conclusion I follows)

  Q18  Statements: M ≥ S ; K < A ; S = T ; A > Y ; K > M ; Y ≤ O ; T ≥ E
       Key chain: A > K > M ≥ S = T ≥ E
       I)  A > M → TRUE   (A > K > M)
       II) T = K → FALSE  (K > M ≥ S = T → K > T)
       Answer: A  (Only conclusion I follows)

  Q19  Statement: Y < O ≤ G ≤ K = U > L > P
       From O ≤ G ≤ K = U we get O ≤ U
       I)  O = U → not guaranteed (O < U possible) → NEITHER individually true
       II) U > O → not guaranteed (O = U possible) → NEITHER individually true
       Either/Or: I (O=U) and II (U>O ≡ O<U) are complementary covering O≤U
       → exactly one must be true
       Answer: D  (Either conclusion I or conclusion II follows)

  Q20  Statement: B > A ≥ T = F = Y ≤ S < D
       I)  F < D → TRUE   (F = Y ≤ S < D → F < D)
       II) A > S → FALSE  (A ≥ T = F = Y ≤ S; breaks at Y)
       Answer: C  (Only conclusion I follows)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Inequality_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Inequality"

QUESTIONS = [
    # ── Q13 ── Both conclusions true ──────────────────────────────────────────
    # A=B>C>D≥E≥F>G=H; I)A>E TRUE; II)D≥F TRUE
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: A = B > C, E ≤ D < C, E ≥ F > G = H\n"
            "Conclusions:\n"
            "I. A > E\n"
            "II. D ≥ F"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और उसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: A = B > C, E ≤ D < C, E ≥ F > G = H\n"
            "निष्कर्ष:\n"
            "I. A > E\n"
            "II. D ≥ F"
        ),
        "option_a": "Only Conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Only Conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Either Conclusion I or II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "Both Conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "correct_answer": "D",
        # I)A>E: A=B>C>D≥E → TRUE; II)D≥F: D≥E≥F → TRUE
    },
    # ── Q14 ── Both conclusions true ──────────────────────────────────────────
    # H=I<J<K≤L=M≥N>O; I)K>H TRUE; II)L>O TRUE
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: J > I = H ; J < K ≤ L ; L = M ≥ N > O\n"
            "Conclusions:\n"
            "I. K > H\n"
            "II. L > O"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और उसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: J > I = H ; J < K ≤ L ; L = M ≥ N > O\n"
            "निष्कर्ष:\n"
            "I. K > H\n"
            "II. L > O"
        ),
        "option_a": "Only Conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Only Conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Either I or II follows / या तो I या II अनुसरण करता है",
        "option_d": "Both I and II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "D",
        # I)K>H: H=I<J<K → TRUE; II)L>O: L=M≥N>O → TRUE
    },
    # ── Q15 ── Three conclusions; only I and II true ───────────────────────────
    # D=E>F>G≥H≥I>J=K; I)D>H TRUE; II)G≥I TRUE; III)F<K FALSE (F>K)
    {
        "question_number": 15,
        "difficulty": "hard",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and three conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: D = E > F, H ≤ G < F, H ≥ I > J = K\n"
            "Conclusions:\n"
            "I. D > H\n"
            "II. G ≥ I\n"
            "III. F < K"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और उसके बाद तीन निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: D = E > F, H ≤ G < F, H ≥ I > J = K\n"
            "निष्कर्ष:\n"
            "I. D > H\n"
            "II. G ≥ I\n"
            "III. F < K"
        ),
        "option_a": "Only Conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "All Conclusions follow / सभी निष्कर्ष अनुसरण करते हैं",
        "option_c": "Either Conclusion I or II and Conclusion III follow / या तो निष्कर्ष I या II और निष्कर्ष III अनुसरण करते हैं",
        "option_d": "Both Conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "correct_answer": "D",
        # Chain: D=E>F>G≥H≥I>J=K
        # I)D>H: D>F>G≥H TRUE; II)G≥I: G≥H≥I TRUE; III)F<K: F>K FALSE
    },
    # ── Q16 ── Both conclusions true ──────────────────────────────────────────
    # A>B=C>E; I)A>E TRUE; II)E<B TRUE
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and it is followed by two conclusions. Choose the correct answer based "
            "on the information given below.\n"
            "Statements: A > B ; B = C ; D = M > E < C\n"
            "Conclusions:\n"
            "I. A > E\n"
            "II. E < B"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: A > B ; B = C ; D = M > E < C\n"
            "निष्कर्ष:\n"
            "I. A > E\n"
            "II. E < B"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_d": "Both I and II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "D",
        # A>B=C>E: I)A>E TRUE; II)E<B: B=C>E → E<B TRUE
    },
    # ── Q17 ── Only conclusion I (K > M) is true ──────────────────────────────
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and it is followed by two conclusions. Choose the correct answer based "
            "on the information given below.\n"
            "Statements: L > M ; M ≤ O = N ; L = Q < K\n"
            "Conclusions:\n"
            "I. K > M\n"
            "II. O ≤ K"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: L > M ; M ≤ O = N ; L = Q < K\n"
            "निष्कर्ष:\n"
            "I. K > M\n"
            "II. O ≤ K"
        ),
        "option_a": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_b": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_c": "Both conclusions I and II follow / दोनों निष्कर्ष I और II अनुसरण करते हैं",
        "option_d": "Either conclusion I or II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "correct_answer": "B",
        # I)K>M: K>Q=L>M TRUE; II)O≤K: O≥M<L=Q<K → breaks at M, no O↔K → FALSE
    },
    # ── Q18 ── Only conclusion I (A > M) is true ──────────────────────────────
    # Key chain: A > K > M ≥ S = T
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: M ≥ S, K < A, S = T, A > Y, K > M, Y ≤ O, T ≥ E\n"
            "Conclusions:\n"
            "I. A > M\n"
            "II. T = K"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और उसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: M ≥ S, K < A, S = T, A > Y, K > M, Y ≤ O, T ≥ E\n"
            "निष्कर्ष:\n"
            "I. A > M\n"
            "II. T = K"
        ),
        "option_a": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Both conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "option_c": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_d": "Either conclusion I or II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "correct_answer": "A",
        # Chain: A>K>M≥S=T≥E
        # I)A>M: A>K>M TRUE; II)T=K: K>M≥S=T → K>T → FALSE
    },
    # ── Q19 ── Either/Or complementary pair ───────────────────────────────────
    # Y<O≤G≤K=U>L>P; O≤U; I)O=U and II)U>O cover all cases of O≤U
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statement: Y < O ≤ G ≤ K = U > L > P\n"
            "Conclusions:\n"
            "I. O = U\n"
            "II. U > O"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: Y < O ≤ G ≤ K = U > L > P\n"
            "निष्कर्ष:\n"
            "I. O = U\n"
            "II. U > O"
        ),
        "option_a": "Neither conclusion I nor conclusion II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "option_b": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_d": "Either conclusion I or conclusion II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "correct_answer": "D",
        # O≤G≤K=U → O≤U; I(O=U) & II(O<U) are complementary → one must hold
    },
    # ── Q20 ── Only conclusion I (F < D) is true ──────────────────────────────
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statement: B > A ≥ T = F = Y ≤ S < D\n"
            "Conclusions:\n"
            "I. F < D\n"
            "II. A > S"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: B > A ≥ T = F = Y ≤ S < D\n"
            "निष्कर्ष:\n"
            "I. F < D\n"
            "II. A > S"
        ),
        "option_a": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_b": "Neither conclusion I nor conclusion II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "option_c": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_d": "Either conclusion I or conclusion II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "correct_answer": "C",
        # I)F<D: F=Y≤S<D → F<D TRUE; II)A>S: A≥T=F=Y≤S → breaks at Y → FALSE
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
