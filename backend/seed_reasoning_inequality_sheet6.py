"""
seed_reasoning_inequality_sheet6.py
=========================================
Seeds Inequality Q41-Q50 from Gagan Pratap Reasoning PDFs (Sheet 6).
Subject : Reasoning
Topic   : Inequality
Run     : python seed_reasoning_inequality_sheet6.py

Answer key (solutions verified):
  Q41  Statements: K ≥ J = L < M ≤ N ; N > O = P
       I)  M < P → FALSE  (M ≤ N > O = P; breaks at N → no M↔P)
       II) J > O → FALSE  (J = L < M ≤ N > O; breaks at N → no J↔O)
       Answer: D  (If neither conclusion I nor II follows)

  Q42  Statements: A ≥ B < D ≤ E ; A ≥ G > H = F ; G = I
       I)  I > F → TRUE   (I = G > H = F → I > F)
       II) E ≥ I → FALSE  (E ≥ D > B < A ≥ G = I; breaks at B → no E↔I)
       Answer: A  (Only conclusion I follows)

  Q43  Statements: A < B ; C = D ; E < F ; B > D ; G ≥ C ; A > F ; H = E
       I)  G > B → FALSE  (G ≥ C = D < B; breaks at D → no G↔B)
       II) C = H → FALSE  (C = D < B > A > F > E = H; breaks at B → no C↔H)
       Answer: D  (Neither conclusion I nor II follows)

  Q44  Statement: M < T < G ≤ J = U > Y > R
       I)  G < U → FALSE  (G ≤ J = U → G ≤ U; equality possible → strict < not guaranteed)
       II) J > R → TRUE   (J = U > Y > R → J > R)
       Answer: B  (Only conclusion II follows)

  Q45  Statements: X > Y ; M = X < Z ; T < S ; G ≥ T
       I)  Z > M → TRUE   (M = X < Z → M < Z → Z > M)
       II) Y < Z → TRUE   (Y < X < Z → Y < Z)
       Answer: A  (Both conclusions I and II are true)

  Q46  Statements: W < K ; Z < M ≤ W ; B > Z ; R ≤ K
       I)  W < B → FALSE  (W ≥ M > Z < B; breaks at Z → no W↔B)
       II) R > W → FALSE  (R ≤ K > W; breaks at K → no R↔W)
       Answer: D  (Neither conclusion I nor II follows)

  Q47  Statements: F < G < D ; D < H > C ; F < A
       I)  G < C → FALSE  (G < D < H > C; breaks at H → no G↔C)
       II) H = A → FALSE  (A > F < G < D < H; breaks at F → no H↔A)
       Answer: C  (Neither conclusion I nor II follows)

  Q48  Statements: B ≥ P = M ; X > B < T ; Y = H ≤ X ; R > Y > N
       I)  P > H → FALSE  (P ≤ B < X ≥ H; breaks at X → no P↔H)
       II) R > X → FALSE  (R > Y = H ≤ X; breaks at H → no R↔X)
       Answer: D  (Neither conclusion I nor II follows)

  Q49  Statements: R > I = N > P ; Y ≥ R > K ; N ≤ E < Z
       I)  K > I → FALSE  (K < R > I; breaks at R → no K↔I)
       II) I < Z → TRUE   (I = N ≤ E < Z → I < Z)
       Answer: B  (Only conclusion II follows)

  Q50  Statements: S ≤ D > Q > V ; M ≤ N < Q = W
       I)  D ≥ M → [per source: FALSE — chain gives D > M (strict), not D ≥ M]
       II) N < D → TRUE   (N < Q < D → N < D)
       Answer: A  (Only conclusion II follows)
       [NOTE: Mathematically D > M implies D ≥ M, so I is also logically true.
        The source marks I as False by exam convention — only the strictly
        derived sign is accepted as the conclusion.]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Inequality_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Inequality"

QUESTIONS = [
    # ── Q41 ── Neither conclusion follows ─────────────────────────────────────
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: K ≥ J = L < M ≤ N ; N > O = P\n"
            "Conclusions:\n"
            "I. M < P\n"
            "II. J > O"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: K ≥ J = L < M ≤ N ; N > O = P\n"
            "निष्कर्ष:\n"
            "I. M < P\n"
            "II. J > O"
        ),
        "option_a": "If only conclusion I follows / यदि केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "If only conclusion II follows / यदि केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "If either conclusion I or II follows / यदि या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "If neither conclusion I nor II follows / यदि न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I)M<P: M≤N>O=P; breaks at N → FALSE; II)J>O: J=L<M≤N>O; breaks at N → FALSE
    },
    # ── Q42 ── Only conclusion I (I > F) follows ──────────────────────────────
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: A ≥ B < D ≤ E ; A ≥ G > H = F ; G = I\n"
            "Conclusions:\n"
            "I. I > F\n"
            "II. E ≥ I"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: A ≥ B < D ≤ E ; A ≥ G > H = F ; G = I\n"
            "निष्कर्ष:\n"
            "I. I > F\n"
            "II. E ≥ I"
        ),
        "option_a": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Either conclusion I or II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "Neither conclusion I nor II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "A",
        # I)I>F: I=G>H=F → TRUE; II)E≥I: E≥D>B<A≥G=I breaks at B → FALSE
    },
    # ── Q43 ── Neither conclusion follows (multi-statement) ───────────────────
    {
        "question_number": 43,
        "difficulty": "hard",
        "question_en": (
            "Direction: In the following question assuming the given statements to be true, "
            "find which of the conclusions among given conclusions is/are definitely true, "
            "and then give your answers accordingly.\n"
            "Statements: A < B ; C = D ; E < F ; B > D ; G ≥ C ; A > F ; H = E\n"
            "Conclusions:\n"
            "I. G > B\n"
            "II. C = H"
        ),
        "question_hi": (
            "निर्देश: निम्नलिखित प्रश्न में दिए गए कथनों को सत्य मानते हुए, यह ज्ञात करें "
            "कि दिए गए निष्कर्षों में से कौन सा/कौन से निष्कर्ष निश्चित रूप से सत्य है/हैं "
            "और फिर उसके अनुसार अपने उत्तर दें।\n"
            "कथन: A < B ; C = D ; E < F ; B > D ; G ≥ C ; A > F ; H = E\n"
            "निष्कर्ष:\n"
            "I. G > B\n"
            "II. C = H"
        ),
        "option_a": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_b": "Both conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "option_c": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_d": "Neither conclusion I nor II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I)G>B: G≥C=D<B; breaks at D → no G↔B → FALSE
        # II)C=H: C=D<B>A>F>E=H; breaks at B → no C↔H → FALSE
    },
    # ── Q44 ── Only conclusion II (J > R) follows ─────────────────────────────
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statement: M < T < G ≤ J = U > Y > R\n"
            "Conclusions:\n"
            "I. G < U\n"
            "II. J > R"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: M < T < G ≤ J = U > Y > R\n"
            "निष्कर्ष:\n"
            "I. G < U\n"
            "II. J > R"
        ),
        "option_a": "Either conclusion I or conclusion II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "option_b": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_d": "Both conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "correct_answer": "B",
        # I)G<U: G≤J=U → G≤U; strict < not guaranteed (G=J=U possible) → FALSE
        # II)J>R: J=U>Y>R → J>R → TRUE
    },
    # ── Q45 ── Both conclusions true ──────────────────────────────────────────
    {
        "question_number": 45,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: X > Y ; M = X < Z ; T < S ; G ≥ T\n"
            "Conclusions:\n"
            "I. Z > M\n"
            "II. Y < Z"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: X > Y ; M = X < Z ; T < S ; G ≥ T\n"
            "निष्कर्ष:\n"
            "I. Z > M\n"
            "II. Y < Z"
        ),
        "option_a": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "option_b": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_c": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_d": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "A",
        # I)Z>M: M=X<Z → M<Z → TRUE; II)Y<Z: Y<X<Z (X>Y, X<Z) → TRUE
    },
    # ── Q46 ── Neither conclusion follows ─────────────────────────────────────
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: W < K ; Z < M ≤ W ; B > Z ; R ≤ K\n"
            "Conclusion:\n"
            "I. W < B\n"
            "II. R > W"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: W < K ; Z < M ≤ W ; B > Z ; R ≤ K\n"
            "निष्कर्ष:\n"
            "I. W < B\n"
            "II. R > W"
        ),
        "option_a": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Both conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither conclusion I nor II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I)W<B: W≥M>Z<B breaks at Z → no W↔B → FALSE
        # II)R>W: R≤K>W breaks at K → no R↔W → FALSE
    },
    # ── Q47 ── Neither conclusion follows ─────────────────────────────────────
    {
        "question_number": 47,
        "difficulty": "medium",
        "question_en": (
            "Directions: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: F < G < D ; D < H > C ; F < A\n"
            "Conclusions:\n"
            "I. G < C\n"
            "II. H = A"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: F < G < D ; D < H > C ; F < A\n"
            "निष्कर्ष:\n"
            "I. G < C\n"
            "II. H = A"
        ),
        "option_a": "Both conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "option_b": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_c": "Neither conclusion I nor II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "option_d": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "correct_answer": "C",
        # I)G<C: G<D<H>C; breaks at H → no G↔C → FALSE
        # II)H=A: A>F<G<D<H; breaks at F → no H↔A → FALSE
    },
    # ── Q48 ── Neither conclusion follows ─────────────────────────────────────
    {
        "question_number": 48,
        "difficulty": "hard",
        "question_en": (
            "Directions: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: B ≥ P = M ; X > B < T ; Y = H ≤ X ; R > Y > N\n"
            "Conclusions:\n"
            "I. P > H\n"
            "II. R > X"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: B ≥ P = M ; X > B < T ; Y = H ≤ X ; R > Y > N\n"
            "निष्कर्ष:\n"
            "I. P > H\n"
            "II. R > X"
        ),
        "option_a": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_b": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_c": "Either conclusion I or II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "Neither conclusion I nor II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I)P>H: P≤B<X≥H; breaks at X → no P↔H → FALSE
        # II)R>X: R>Y=H≤X; breaks at H → no R↔X → FALSE
    },
    # ── Q49 ── Only conclusion II (I < Z) follows ─────────────────────────────
    {
        "question_number": 49,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and it is followed by two conclusions. Choose the correct answer based "
            "on the information given below.\n"
            "Statements: R > I = N > P ; Y ≥ R > K ; N ≤ E < Z\n"
            "Conclusions:\n"
            "I. K > I\n"
            "II. I < Z"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: R > I = N > P ; Y ≥ R > K ; N ≤ E < Z\n"
            "निष्कर्ष:\n"
            "I. K > I\n"
            "II. I < Z"
        ),
        "option_a": "Both conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "option_b": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_d": "Neither conclusion I nor conclusion II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I)K>I: K<R>I; breaks at R → no K↔I → FALSE
        # II)I<Z: I=N≤E<Z → I<Z → TRUE
    },
    # ── Q50 ── Only conclusion II (N < D) follows ─────────────────────────────
    # NOTE: D>Q>N≥M proves D>M which logically implies D≥M (conclusion I).
    # However, per source exam convention, when the derived sign is strictly ">",
    # the conclusion "≥" is NOT credited — only "N < D" (conclusion II) is accepted.
    {
        "question_number": 50,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and it is followed by two conclusions. Choose the correct answer based "
            "on the information given below.\n"
            "Statements: S ≤ D > Q > V ; M ≤ N < Q = W\n"
            "Conclusions:\n"
            "I. D ≥ M\n"
            "II. N < D"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: S ≤ D > Q > V ; M ≤ N < Q = W\n"
            "निष्कर्ष:\n"
            "I. D ≥ M\n"
            "II. N < D"
        ),
        "option_a": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_b": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_c": "Either conclusion I or conclusion II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "Both conclusions I and II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "correct_answer": "A",
        # I)D≥M: D>Q>N≥M → D>M; per source convention strict > → ≥ conclusion not credited → FALSE
        # II)N<D: N<Q<D → N<D → TRUE
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
