"""
seed_reasoning_inequality_sheet5.py
=========================================
Seeds Inequality Q29-Q40 from Gagan Pratap Reasoning PDFs (Sheet 5).
Subject : Reasoning
Topic   : Inequality
Run     : python seed_reasoning_inequality_sheet5.py

Answer key (solutions verified):
  Q29  Statements: Q > R < S; K = Q > L > M; A = N > M
       I) M < K  → TRUE   (K = Q > L > M → K > M)
       II) S > K → FALSE  (S > R < Q = K; breaks at R → no S↔K)
       Answer: A  (Only I is true)

  Q30  Statements: E > F > G; K > L < M = G; P > Q < R = E
       I)  Q > F → FALSE  (Q < R = E > F; breaks at E → no Q↔F)
       II) G > K → FALSE  (G = M > L < K; breaks at L → no G↔K)
       Answer: D  (Neither I nor II is true)

  Q31  Statements: B > Q < Z; Z = K; K < A < T
       I)  Z < B → FALSE  (B > Q < Z; breaks at Q → no Z↔B)
       II) T > Q → TRUE   (Q < Z = K < A < T → Q < T)
       III) K < T → TRUE  (K < A < T)
       Answer: D  (Only conclusions II and III are true)

  Q32  Statements: P > Q < R; R = S; S < T < U
       I)  Q < U → TRUE   (Q < R = S < T < U → Q < U)
       II) U > S → TRUE   (S < T < U → U > S)
       Answer: D  (Both conclusions I and II are true)

  Q33  Statements: J < T ≥ P = B; D ≤ F ≤ P = G
       I)  D ≤ T → TRUE   (D ≤ F ≤ P and T ≥ P → D ≤ P ≤ T)
       II) G = B → TRUE   (G = P = B)
       Answer: A  (Both conclusions I and II are true)

  Q34  Statements: Q > M ≤ N; Q = S > A < O
       I)  N > A → FALSE  (N ≥ M < Q = S > A; direction changes → no N↔A)
       II) M < S → TRUE   (M < Q = S → M < S)
       Answer: B  (Only conclusion II is true)

  Q35  Statements: P ≤ Q > M ≤ N; Q = S > A < O
       I)  S > P → FALSE  (P ≤ Q = S → P ≤ S; equality possible, strict > not guaranteed)
       II) N < S → FALSE  (N ≥ M < Q = S; breaks at M → no N↔S)
       Answer: D  (Neither conclusion I nor II is true)

  Q36  Statements: A > B > C < D; C = E > G > P = R
       I)  D > G → TRUE   (D > C = E > G → D > G)
       II) B > E → TRUE   (B > C = E → B > E)
       Answer: D  (Both conclusions I and II are true)

  Q37  Statements: P = Q ≤ R > W; S = T ≥ R; A > L > G = R
       I)  P > S → FALSE  (P = Q ≤ R ≤ T = S → P ≤ S → P > S is false)
       II) A > P → TRUE   (A > L > G = R ≥ Q = P → A > P)
       Answer: B  (If only conclusion II follows)

  Q38  Statements: L > M ≤ N > O; O = Q > R
       I)  L > R → FALSE  (L > M ≤ N; breaks at M → no L↔R via this chain)
       II) M = O → FALSE  (M ≤ N > O; breaks at N → no M↔O)
       Answer: D  (If neither conclusion I nor II follows)

  Q39  Statements: P > Q; X ≤ R < S; S > P
       I)  P ≤ R → FALSE  (P < S and R < S but no P↔R direct relation)
       II) X > S → FALSE  (X ≤ R < S → X < S → X > S is false)
       Answer: D  (Neither conclusion I nor II follows)

  Q40  Statements: A < B ≤ E > F; F = G ≥ H > I
       I)  A < F → FALSE  (A < B ≤ E > F; breaks at E → no A↔F)
       II) E > I → TRUE   (E > F = G ≥ H > I → E > I)
       Answer: B  (If only conclusion II follows)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Inequality_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Inequality"

QUESTIONS = [
    # ── Q29 ── Only conclusion I (M < K) is true ──────────────────────────────
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: Q > R < S ; K = Q > L > M ; A = N > M\n"
            "Conclusions:\n"
            "I. M < K\n"
            "II. S > K"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: Q > R < S ; K = Q > L > M ; A = N > M\n"
            "निष्कर्ष:\n"
            "I. M < K\n"
            "II. S > K"
        ),
        "option_a": "Only I is true / केवल I सत्य है",
        "option_b": "Only II is true / केवल II सत्य है",
        "option_c": "Both I and II are true / I और II दोनों सत्य हैं",
        "option_d": "Either I or II is true / या तो I या II सत्य है",
        "correct_answer": "A",
        # I)M<K: K=Q>L>M → K>M → TRUE; II)S>K: S>R<Q=K breaks at R → FALSE
    },
    # ── Q30 ── Neither conclusion is true ─────────────────────────────────────
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: E > F > G ; K > L < M = G ; P > Q < R = E\n"
            "Conclusions:\n"
            "I. Q > F\n"
            "II. G > K"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: E > F > G ; K > L < M = G ; P > Q < R = E\n"
            "निष्कर्ष:\n"
            "I. Q > F\n"
            "II. G > K"
        ),
        "option_a": "Only I is true / केवल I सत्य है",
        "option_b": "Only II is true / केवल II सत्य है",
        "option_c": "Both I and II are true / I और II दोनों सत्य हैं",
        "option_d": "Neither I nor II is true / न तो I और न ही II सत्य है",
        "correct_answer": "D",
        # I)Q>F: Q<R=E>F breaks at E → FALSE; II)G>K: G=M>L<K breaks at L → FALSE
    },
    # ── Q31 ── Only conclusions II and III are true ────────────────────────────
    # 3-conclusion question
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and three conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: B > Q < Z ; Z = K ; K < A < T\n"
            "Conclusions:\n"
            "I. Z < B\n"
            "II. T > Q\n"
            "III. K < T"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद तीन निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: B > Q < Z ; Z = K ; K < A < T\n"
            "निष्कर्ष:\n"
            "I. Z < B\n"
            "II. T > Q\n"
            "III. K < T"
        ),
        "option_a": "All conclusions are true / सभी निष्कर्ष सत्य हैं",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_d": "Only conclusions II and III are true / केवल निष्कर्ष II और III सत्य हैं",
        "correct_answer": "D",
        # I)Z<B: B>Q<Z breaks at Q → FALSE; II)T>Q: Q<Z=K<A<T → TRUE; III)K<T: K<A<T → TRUE
    },
    # ── Q32 ── Both conclusions true ──────────────────────────────────────────
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the following question assuming the given statements to be true, "
            "find which of the conclusion(s) among given conclusions is/are definitely true "
            "and give your answers accordingly.\n"
            "Statements: P > Q < R ; R = S ; S < T < U\n"
            "Conclusions:\n"
            "I. Q < U\n"
            "II. U > S"
        ),
        "question_hi": (
            "निर्देश: निम्नलिखित प्रश्न में दिए गए कथनों को सत्य मानते हुए, यह ज्ञात करें "
            "कि दिए गए निष्कर्षों में से कौन सा/कौन से निष्कर्ष निश्चित रूप से सत्य है/हैं "
            "और फिर उसके अनुसार अपने उत्तर दें।\n"
            "कथन: P > Q < R ; R = S ; S < T < U\n"
            "निष्कर्ष:\n"
            "I. Q < U\n"
            "II. U > S"
        ),
        "option_a": "Either I or II follow / या तो I या II सत्य है",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_d": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "correct_answer": "D",
        # I)Q<U: Q<R=S<T<U → TRUE; II)U>S: S<T<U → TRUE
    },
    # ── Q33 ── Both conclusions true ──────────────────────────────────────────
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and it is followed by two conclusions. Choose the correct answer based "
            "on the information given below.\n"
            "Statements: J < T ≥ P = B ; D ≤ F ≤ P = G\n"
            "Conclusions:\n"
            "I. D ≤ T\n"
            "II. G = B"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: J < T ≥ P = B ; D ≤ F ≤ P = G\n"
            "निष्कर्ष:\n"
            "I. D ≤ T\n"
            "II. G = B"
        ),
        "option_a": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "option_b": "Either conclusion I or II is true / या तो निष्कर्ष I या II सत्य है",
        "option_c": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_d": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "correct_answer": "A",
        # I)D≤T: D≤F≤P and T≥P → D≤P≤T → TRUE; II)G=B: G=P=B → TRUE
    },
    # ── Q34 ── Only conclusion II (M < S) is true ─────────────────────────────
    {
        "question_number": 34,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: Q > M ≤ N ; Q = S > A < O\n"
            "Conclusions:\n"
            "I. N > A\n"
            "II. M < S"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: Q > M ≤ N ; Q = S > A < O\n"
            "निष्कर्ष:\n"
            "I. N > A\n"
            "II. M < S"
        ),
        "option_a": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Either conclusion I or II is true / या तो निष्कर्ष I या II सत्य है",
        "option_d": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "B",
        # I)N>A: N≥M<Q=S>A direction changes → no N↔A → FALSE; II)M<S: M<Q=S → TRUE
    },
    # ── Q35 ── Neither conclusion is true ─────────────────────────────────────
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": (
            "Directions: In these questions, a relationship between different elements is "
            "shown in the statements. The statements are followed by two conclusions. "
            "Read the given statement very carefully and decide which conclusion definitely "
            "follows the given statement.\n"
            "Statements: P ≤ Q > M ≤ N ; Q = S > A < O\n"
            "Conclusions:\n"
            "I. S > P\n"
            "II. N < S"
        ),
        "question_hi": (
            "निर्देश: इन प्रश्नों में, कथनों में विभिन्न तत्वों के बीच संबंध दिखाया गया है। "
            "कथनों के बाद दो निष्कर्ष दिए गए हैं। दिए गए कथन को बहुत ध्यान से पढ़िए "
            "और तय कीजिए कि कौन सा निष्कर्ष निश्चित रूप से दिए गए कथन का अनुसरण करता है।\n"
            "कथन: P ≤ Q > M ≤ N ; Q = S > A < O\n"
            "निष्कर्ष:\n"
            "I. S > P\n"
            "II. N < S"
        ),
        "option_a": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Either conclusion I or II is true / या तो निष्कर्ष I या II सत्य है",
        "option_d": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "D",
        # I)S>P: P≤Q=S → P≤S; equality possible → strict > not guaranteed → FALSE
        # II)N<S: N≥M<Q=S breaks at M → no N↔S → FALSE
    },
    # ── Q36 ── Both conclusions true ──────────────────────────────────────────
    {
        "question_number": 36,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: A > B > C < D ; C = E > G > P = R\n"
            "Conclusions:\n"
            "I. D > G\n"
            "II. B > E"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: A > B > C < D ; C = E > G > P = R\n"
            "निष्कर्ष:\n"
            "I. D > G\n"
            "II. B > E"
        ),
        "option_a": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Either conclusion I or II is true / या तो निष्कर्ष I या II सत्य है",
        "option_d": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "correct_answer": "D",
        # I)D>G: D>C=E>G → TRUE; II)B>E: B>C=E → TRUE
    },
    # ── Q37 ── Only conclusion II (A > P) follows ─────────────────────────────
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: P = Q ≤ R > W ; S = T ≥ R ; A > L > G = R\n"
            "Conclusions:\n"
            "I. P > S\n"
            "II. A > P"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: P = Q ≤ R > W ; S = T ≥ R ; A > L > G = R\n"
            "निष्कर्ष:\n"
            "I. P > S\n"
            "II. A > P"
        ),
        "option_a": "If only conclusion I follows / यदि केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "If only conclusion II follows / यदि केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "If either conclusion I or II follows / यदि या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "If neither conclusion I nor II follows / यदि न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I)P>S: P=Q≤R≤T=S → P≤S → P>S is FALSE
        # II)A>P: A>L>G=R≥Q=P → A>P → TRUE
    },
    # ── Q38 ── Neither conclusion follows ─────────────────────────────────────
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": (
            "Directions: In these questions, a relationship between different elements is "
            "shown in the statements. The statements are followed by two conclusions. "
            "Read the given statement very carefully and decide which conclusion definitely "
            "follows the given statement.\n"
            "Statements: L > M ≤ N > O ; O = Q > R\n"
            "Conclusions:\n"
            "I. L > R\n"
            "II. M = O"
        ),
        "question_hi": (
            "निर्देश: इन प्रश्नों में, कथनों में विभिन्न तत्वों के बीच संबंध दिखाया गया है। "
            "कथनों के बाद दो निष्कर्ष दिए गए हैं। दिए गए कथन को बहुत ध्यान से पढ़िए "
            "और तय कीजिए कि कौन सा निष्कर्ष निश्चित रूप से दिए गए कथन का अनुसरण करता है।\n"
            "कथन: L > M ≤ N > O ; O = Q > R\n"
            "निष्कर्ष:\n"
            "I. L > R\n"
            "II. M = O"
        ),
        "option_a": "If only conclusion I follows / यदि केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "If only conclusion II follows / यदि केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "If either conclusion I or II follows / यदि या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "If neither conclusion I nor II follows / यदि न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I)L>R: L>M≤N>O=Q>R breaks at M (>≤) → no L↔R → FALSE
        # II)M=O: M≤N>O breaks at N (≤>) → no M↔O → FALSE
    },
    # ── Q39 ── Neither conclusion follows ─────────────────────────────────────
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: P > Q ; X ≤ R < S ; S > P\n"
            "Conclusions:\n"
            "I. P ≤ R\n"
            "II. X > S"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: P > Q ; X ≤ R < S ; S > P\n"
            "निष्कर्ष:\n"
            "I. P ≤ R\n"
            "II. X > S"
        ),
        "option_a": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Either conclusion I or II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "Neither conclusion I nor II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I)P≤R: P<S and R<S but P↔R undetermined (both < S) → FALSE
        # II)X>S: X≤R<S → X<S → X>S is FALSE
    },
    # ── Q40 ── Only conclusion II (E > I) follows ─────────────────────────────
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on "
            "the information given below.\n"
            "Statements: A < B ≤ E > F ; F = G ≥ H > I\n"
            "Conclusions:\n"
            "I. A < F\n"
            "II. E > I"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में, विभिन्न तत्वों के बीच संबंध दिखाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: A < B ≤ E > F ; F = G ≥ H > I\n"
            "निष्कर्ष:\n"
            "I. A < F\n"
            "II. E > I"
        ),
        "option_a": "If only conclusion I follows / यदि केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "If only conclusion II follows / यदि केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "If either conclusion I or II follows / यदि या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "If neither conclusion I nor II follows / यदि न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I)A<F: A<B≤E>F breaks at E (≤>) → no A↔F → FALSE
        # II)E>I: E>F=G≥H>I → E>I → TRUE
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
