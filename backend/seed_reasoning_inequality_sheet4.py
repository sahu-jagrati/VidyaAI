"""
seed_reasoning_inequality_sheet4.py
=========================================
Seeds Inequality Q21-Q28 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Inequality
Run     : python seed_reasoning_inequality_sheet4.py

Answer key (solutions verified):
  Q21  Statements: H > S ≥ F = B ≤ U ≤ T ; E ≤ B ≤ K
       I)  U ≥ E → TRUE   (E ≤ B ≤ U → U ≥ E)
       II) S > T → FALSE  (S ≥ F = B ≤ U ≤ T; breaks at B → no S↔T)
       Answer: D  (Only conclusion I is true)

  Q22  Statement: B ≥ C > D ≤ E ≤ F < G = L < M ≥ T > Q
       I)  B ≥ F → FALSE  (breaks at D: B≥C>D≤E; no B↔F)
       II) D < G → TRUE   (D ≤ E ≤ F < G → D < G)
       Answer: C  (Only conclusion II is true)

  Q23  Statement: Y < O ≤ G ≤ K = U > L > P
       O ≤ G ≤ K = U → O ≤ U
       I)  O = U → not guaranteed (NEITHER alone)
       II) U > O → not guaranteed (NEITHER alone)
       Either/Or: I (O=U) and II (U>O) are complementary covering O≤U
       Answer: C  (Either conclusion I or conclusion II follows)

  Q24  Statements: P ≥ Q ≤ R = S ; Q ≥ T > N ; P = L ≤ M
       Combined: M ≥ L = P ≥ Q ≥ T
       I)  M = T → not guaranteed (NEITHER alone)
       II) M > T → not guaranteed (NEITHER alone)
       Either/Or: I (M=T) and II (M>T) are complementary covering M≥T
       Answer: C  (If either conclusion I or II follows)

  Q25  Statements: A > O = H ≥ U > I ; I ≤ Y
       I)  A > U → TRUE   (A > O = H ≥ U → A > U)
       II) U > Y → FALSE  (U > I ≤ Y; breaks at I → no U↔Y)
       Answer: A  (If only conclusion I follows)

  Q26  Statements: E = G ≥ H = N ; C > F ≥ M = N
       Combined: E = G ≥ H = N = M ≤ F < C
       I)  E ≥ M → TRUE   (E = G ≥ H = N = M → E ≥ M)
       II) C > H → TRUE   (C > F ≥ M = N = H → C > H)
       Answer: C  (If both conclusions I and II are true)

  Q27  Statements: M ≤ N < L ≥ Q ; R > T ≥ Q
       I)  L > M → TRUE   (M ≤ N < L → M < L → L > M)
       II) R ≥ M → FALSE  (R > T ≥ Q ≤ L > N ≥ M; breaks at Q → no R↔M)
       Answer: B  (If only conclusion I is true)

  Q28  Statements: M ≥ P < H ; V > T = M
       Combined: V > T = M ≥ P < H
       I)  V > P → TRUE   (V > T = M ≥ P → V > P)
       II) T ≥ H → FALSE  (T = M ≥ P < H; breaks at P → no T↔H)
       Answer: A  (If only conclusion I is true)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Inequality_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Inequality"

QUESTIONS = [
    # ── Q21 ── Only conclusion I (U ≥ E) is true ─────────────────────────────
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and it is followed by two conclusions. Choose the correct answer based "
            "on the information given below.\n"
            "Statements: H > S ≥ F = B ≤ U ≤ T ; E ≤ B ≤ K\n"
            "Conclusions:\n"
            "I. U ≥ E\n"
            "II. S > T"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: H > S ≥ F = B ≤ U ≤ T ; E ≤ B ≤ K\n"
            "निष्कर्ष:\n"
            "I. U ≥ E\n"
            "II. S > T"
        ),
        "option_a": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_b": "Either conclusion I or II is true / या तो निष्कर्ष I या II सत्य है",
        "option_c": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "option_d": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "correct_answer": "D",
        # I)U≥E: E≤B≤U → TRUE; II)S>T: S≥F=B≤U≤T → breaks at B → FALSE
    },
    # ── Q22 ── Only conclusion II (D < G) is true ─────────────────────────────
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statement: B ≥ C > D ≤ E ≤ F < G = L < M ≥ T > Q\n"
            "Conclusions:\n"
            "I. B ≥ F\n"
            "II. D < G"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: B ≥ C > D ≤ E ≤ F < G = L < M ≥ T > Q\n"
            "निष्कर्ष:\n"
            "I. B ≥ F\n"
            "II. D < G"
        ),
        "option_a": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_b": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "option_c": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_d": "Either conclusion I or II is true / या तो निष्कर्ष I या II सत्य है",
        "correct_answer": "C",
        # I)B≥F: breaks at D (B≥C>D≤E) → FALSE; II)D<G: D≤E≤F<G → TRUE
    },
    # ── Q23 ── Either/Or (O≤U; O=U and U>O complementary) ───────────────────
    {
        "question_number": 23,
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
        "option_c": "Either conclusion I or conclusion II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "correct_answer": "C",
        # O≤G≤K=U → O≤U; I(O=U) & II(U>O) complementary → one must hold
    },
    # ── Q24 ── Either/Or (M≥T; M=T and M>T complementary) ───────────────────
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: P ≥ Q ≤ R = S ; Q ≥ T > N ; P = L ≤ M\n"
            "Conclusions:\n"
            "I. M = T\n"
            "II. M > T"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: P ≥ Q ≤ R = S ; Q ≥ T > N ; P = L ≤ M\n"
            "निष्कर्ष:\n"
            "I. M = T\n"
            "II. M > T"
        ),
        "option_a": "If only conclusion I follows / यदि केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "If only conclusion II follows / यदि केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "If either conclusion I or II follows / यदि या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "If neither conclusion I nor II follows / यदि न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # M≥L=P≥Q≥T → M≥T; I(M=T) & II(M>T) complementary → one must hold
    },
    # ── Q25 ── Only conclusion I (A > U) is true ──────────────────────────────
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": (
            "Directions: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: A > O = H ≥ U > I ; I ≤ Y\n"
            "Conclusions:\n"
            "I. A > U\n"
            "II. U > Y"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: A > O = H ≥ U > I ; I ≤ Y\n"
            "निष्कर्ष:\n"
            "I. A > U\n"
            "II. U > Y"
        ),
        "option_a": "If only conclusion I follows / यदि केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "If only conclusion II follows / यदि केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "If either conclusion I or II follows / यदि या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "If neither conclusion I nor II follows / यदि न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "A",
        # I)A>U: A>O=H≥U → TRUE; II)U>Y: U>I≤Y → breaks at I → FALSE
    },
    # ── Q26 ── Both conclusions true ──────────────────────────────────────────
    # E=G≥H=N=M; C>F≥M=N=H
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "Directions: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: E = G ≥ H = N ; C > F ≥ M = N\n"
            "Conclusions:\n"
            "I. E ≥ M\n"
            "II. C > H"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: E = G ≥ H = N ; C > F ≥ M = N\n"
            "निष्कर्ष:\n"
            "I. E ≥ M\n"
            "II. C > H"
        ),
        "option_a": "If neither conclusion I nor II is true / यदि न तो निष्कर्ष I और न ही II सत्य है",
        "option_b": "If only conclusion I is true / यदि केवल निष्कर्ष I सत्य है",
        "option_c": "If both conclusions I and II are true / यदि निष्कर्ष I और II दोनों सत्य हैं",
        "option_d": "If either conclusion I or II is true / यदि या तो निष्कर्ष I या II सत्य है",
        "correct_answer": "C",
        # I)E≥M: E=G≥H=N=M → TRUE; II)C>H: C>F≥M=N=H → TRUE
    },
    # ── Q27 ── Only conclusion I (L > M) is true ──────────────────────────────
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: M ≤ N < L ≥ Q ; R > T ≥ Q\n"
            "Conclusions:\n"
            "I. L > M\n"
            "II. R ≥ M"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: M ≤ N < L ≥ Q ; R > T ≥ Q\n"
            "निष्कर्ष:\n"
            "I. L > M\n"
            "II. R ≥ M"
        ),
        "option_a": "If either conclusion I or II is true / यदि या तो निष्कर्ष I या II सत्य है",
        "option_b": "If only conclusion I is true / यदि केवल निष्कर्ष I सत्य है",
        "option_c": "If both conclusions I and II are true / यदि निष्कर्ष I और II दोनों सत्य हैं",
        "option_d": "If neither conclusion I nor II is true / यदि न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "B",
        # I)L>M: M≤N<L → L>M TRUE; II)R≥M: R>T≥Q≤L>N≥M → breaks at Q → FALSE
    },
    # ── Q28 ── Only conclusion I (V > P) is true ──────────────────────────────
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: M ≥ P < H ; V > T = M\n"
            "Conclusions:\n"
            "I. V > P\n"
            "II. T ≥ H"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: M ≥ P < H ; V > T = M\n"
            "निष्कर्ष:\n"
            "I. V > P\n"
            "II. T ≥ H"
        ),
        "option_a": "If only conclusion I is true / यदि केवल निष्कर्ष I सत्य है",
        "option_b": "If only conclusion II is true / यदि केवल निष्कर्ष II सत्य है",
        "option_c": "If either conclusion I or II is true / यदि या तो निष्कर्ष I या II सत्य है",
        "option_d": "If neither conclusion I nor II is true / यदि न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "A",
        # I)V>P: V>T=M≥P → TRUE; II)T≥H: T=M≥P<H → breaks at P → FALSE
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
