"""
seed_reasoning_inequality_sheet2.py
=========================================
Seeds Inequality Q5-Q12 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Inequality
Run     : python seed_reasoning_inequality_sheet2.py

Answer key (solutions verified):
  Q5   Statement: M < K > I < J > H = G ≤ F
       I)  H = F  → FALSE  (H ≤ F from H=G≤F; equality not guaranteed)
       II) J > G  → TRUE   (J > H = G)
       Answer: C  (Only conclusion II is true)
       [CGL Tier 2 - 2 March 2023]

  Q6   Statement: P ≤ L ≥ M ≥ N = U < V < G
       I)  P > V  → FALSE  (chain breaks at L: P≤L≥M, no P↔V relation)
       II) G ≤ L  → FALSE  (chain breaks at U: L≥M≥N=U<V<G, no G↔L relation)
       Answer: D  (Neither conclusion I nor II is true)
       [CHSL Tier 2 - 10 Jan 2024]

  Q7   Statement: T ≥ M < W = P ≥ Q > R ≤ S
       I)  P ≤ M  → FALSE  (M < W = P, so P > M)
       II) Q > T  → FALSE  (chain breaks at M: T≥M<W, no Q↔T relation)
       Answer: A  (Neither conclusion I nor II is true)
       [CHSL Tier 2 - 10 Jan 2024]

  Q8   Statement: Z < Y = J ≥ G ≥ P ≥ C ≥ R
       I)  Z ≥ R  → FALSE  (chain breaks at Y: Z<Y=J≥...≥R, no Z↔R)
       II) J = C  → FALSE  (J ≥ G ≥ P ≥ C, equality not guaranteed)
       Answer: C  (Neither conclusion I nor II is true)
       [CHSL Tier 2 - 2 Nov 2023]

  Q9   Statement: G < H > K ≤ S ≥ L = M < Q
       I)  G > L  → FALSE  (chain breaks at H: G<H>K, no G↔L relation)
       II) H = Q  → FALSE  (chain breaks at K then S: H>K≤S≥L=M<Q)
       Answer: C  (Neither conclusion I nor II is true)
       [CHSL Tier 2 - 2 Nov 2023]

  Q10  Statement: F > B < E ≤ C = D ≥ A > G
       I)  G < F  → FALSE  (chain breaks at B: F>B<E, no G↔F relation)
       II) C > G  → TRUE   (C = D ≥ A > G → C > G)
       Answer: A  (Only Conclusion II is true)
       [CHSL Tier 2 - 26 June 2023]

  Q11  Statement: M < K ≤ N > P = J > O ≥ L
       I)  N > L  → TRUE   (N > P = J > O ≥ L, strict chain → N > L)
       II) O = M  → FALSE  (chain breaks at N: M<K≤N>P, no O↔M relation)
       Answer: C  (Only Conclusion I is true)
       [CHSL Tier 2 - 26 June 2023]

  Q12  Statements: 11>10=9 ; 11<12≤13 ; 12>14=15
       Combined chain: 9=10<11<12>14=15 (and 12≤13)
       I)  14 > 10 → NEITHER  (chain 10<11<12>14 breaks at 12)
       II) 15 ≤ 10 → NEITHER  (since 14=15; same path, breaks at 12)
       Either/Or: I (14>10) and II (14≤10) are complementary, covering ALL
       possibilities → exactly one must be true.
       Answer: C  (Either Conclusion I or II follows)
       [CHSL Tier 2 - 2 Nov 2023]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Inequality_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Inequality"

QUESTIONS = [
    # ── Q5 ── Only conclusion II (J > G) is true ──────────────────────────────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "In the following question, the statement is followed by two conclusions. "
            "Which of the two conclusions is/are true?\n"
            "Statement: M < K > I < J > H = G ≤ F\n"
            "Conclusions:\n"
            "I. H = F\n"
            "II. J > G\n"
            "[CGL Tier 2 - 2 March 2023]"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में, कथन के बाद दो निष्कर्ष दिए गए हैं। "
            "दोनों में से कौन सा/से निष्कर्ष सत्य है/हैं?\n"
            "कथन: M < K > I < J > H = G ≤ F\n"
            "निष्कर्ष:\n"
            "I. H = F\n"
            "II. J > G"
        ),
        "option_a": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_b": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "option_c": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_d": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "C",
        # I)H=F: H=G≤F so H≤F, equality not guaranteed → FALSE
        # II)J>G: J>H=G → J>G → TRUE
    },
    # ── Q6 ── Neither conclusion is true ─────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            "A statement is followed by two conclusions, numbered I and II. "
            "Find out which of the following conclusion(s) is/are true based on the given statements.\n"
            "Statement: P ≤ L ≥ M ≥ N = U < V < G\n"
            "Conclusions:\n"
            "I. P > V\n"
            "II. G ≤ L\n"
            "[CHSL Tier 2 - 10 Jan 2024]"
        ),
        "question_hi": (
            "एक कथन के बाद दो निष्कर्ष दिए गए हैं। दिए गए कथनों के आधार पर "
            "ज्ञात कीजिए कि निम्नलिखित में से कौन सा/से निष्कर्ष सत्य है/हैं।\n"
            "कथन: P ≤ L ≥ M ≥ N = U < V < G\n"
            "निष्कर्ष:\n"
            "I. P > V\n"
            "II. G ≤ L"
        ),
        "option_a": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_d": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "D",
        # I)P>V: breaks at L (P≤L≥M) → no P↔V → FALSE
        # II)G≤L: breaks at U (L≥M≥N=U<V<G) → no G↔L → FALSE
    },
    # ── Q7 ── Neither conclusion is true ─────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": (
            "A statement is followed by two conclusions, numbered I and II. "
            "Find out which of the following conclusion(s) is/are true based on the given statements.\n"
            "Statement: T ≥ M < W = P ≥ Q > R ≤ S\n"
            "Conclusions:\n"
            "I. P ≤ M\n"
            "II. Q > T\n"
            "[CHSL Tier 2 - 10 Jan 2024]"
        ),
        "question_hi": (
            "एक कथन के बाद दो निष्कर्ष दिए गए हैं। दिए गए कथनों के आधार पर "
            "ज्ञात कीजिए कि निम्नलिखित में से कौन सा/से निष्कर्ष सत्य है/हैं।\n"
            "कथन: T ≥ M < W = P ≥ Q > R ≤ S\n"
            "निष्कर्ष:\n"
            "I. P ≤ M\n"
            "II. Q > T"
        ),
        "option_a": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "option_b": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_c": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_d": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "correct_answer": "A",
        # I)P≤M: M<W=P so P>M → P≤M is FALSE
        # II)Q>T: breaks at M (T≥M<W) → no Q↔T → FALSE
    },
    # ── Q8 ── Neither conclusion is true ─────────────────────────────────────
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "A statement is followed by two conclusions, numbered I and II. "
            "Find out which of the following conclusion(s) is/are true based on the given statements.\n"
            "Statement: Z < Y = J ≥ G ≥ P ≥ C ≥ R\n"
            "Conclusions:\n"
            "I. Z ≥ R\n"
            "II. J = C\n"
            "[CHSL Tier 2 - 2 Nov 2023]"
        ),
        "question_hi": (
            "एक कथन के बाद दो निष्कर्ष दिए गए हैं। दिए गए कथनों के आधार पर "
            "ज्ञात कीजिए कि निम्नलिखित में से कौन सा/से निष्कर्ष सत्य है/हैं।\n"
            "कथन: Z < Y = J ≥ G ≥ P ≥ C ≥ R\n"
            "निष्कर्ष:\n"
            "I. Z ≥ R\n"
            "II. J = C"
        ),
        "option_a": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_b": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_c": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "option_d": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "correct_answer": "C",
        # I)Z≥R: Z<Y=J≥...≥R; chain breaks at Y (Z<Y but Y≥R) → no Z↔R → FALSE
        # II)J=C: J≥G≥P≥C so J≥C; equality not guaranteed → FALSE
    },
    # ── Q9 ── Neither conclusion is true ─────────────────────────────────────
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": (
            "A statement is followed by two conclusions, numbered I and II. "
            "Find out which of the following conclusion(s) is/are true based on the given statements.\n"
            "Statement: G < H > K ≤ S ≥ L = M < Q\n"
            "Conclusions:\n"
            "I. G > L\n"
            "II. H = Q\n"
            "[CHSL Tier 2 - 2 Nov 2023]"
        ),
        "question_hi": (
            "एक कथन के बाद दो निष्कर्ष दिए गए हैं। दिए गए कथनों के आधार पर "
            "ज्ञात कीजिए कि निम्नलिखित में से कौन सा/से निष्कर्ष सत्य है/हैं।\n"
            "कथन: G < H > K ≤ S ≥ L = M < Q\n"
            "निष्कर्ष:\n"
            "I. G > L\n"
            "II. H = Q"
        ),
        "option_a": "Both conclusions I and II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "option_b": "Only conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_c": "Neither conclusion I nor II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "option_d": "Only conclusion II is true / केवल निष्कर्ष II सत्य है",
        "correct_answer": "C",
        # I)G>L: breaks at H (G<H>K) → no G↔L → FALSE
        # II)H=Q: multiple breaks (H>K≤S≥L=M<Q) → no H↔Q → FALSE
    },
    # ── Q10 ── Only Conclusion II (C > G) is true ────────────────────────────
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": (
            "Read the given statement and conclusions carefully. Decide which of the given "
            "conclusions is/are definitely true from the statement.\n"
            "Statement: F > B < E ≤ C = D ≥ A > G\n"
            "Conclusion I: G < F\n"
            "Conclusion II: C > G\n"
            "[CHSL Tier 2 - 26 June 2023]"
        ),
        "question_hi": (
            "दिए गए कथन और निष्कर्ष को ध्यानपूर्वक पढ़िए। निर्णय लीजिए कि कथन से "
            "कौन सा/से निष्कर्ष निश्चित रूप से सत्य है/हैं।\n"
            "कथन: F > B < E ≤ C = D ≥ A > G\n"
            "निष्कर्ष I: G < F\n"
            "निष्कर्ष II: C > G"
        ),
        "option_a": "Only Conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_b": "Both Conclusion I and Conclusion II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "option_c": "Only Conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_d": "Neither Conclusion I nor Conclusion II is true / न तो निष्कर्ष I और न ही II सत्य है",
        "correct_answer": "A",
        # I)G<F: breaks at B (F>B<E) → no G↔F → FALSE
        # II)C>G: C=D≥A>G → C>G → TRUE
    },
    # ── Q11 ── Only Conclusion I (N > L) is true ─────────────────────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": (
            "Read the given statement and conclusions carefully. Decide which of the given "
            "conclusions is/are definitely true from the statement.\n"
            "Statement: M < K ≤ N > P = J > O ≥ L\n"
            "Conclusion I: N > L\n"
            "Conclusion II: O = M\n"
            "[CHSL Tier 2 - 26 June 2023]"
        ),
        "question_hi": (
            "दिए गए कथन और निष्कर्ष को ध्यानपूर्वक पढ़िए। निर्णय लीजिए कि कथन से "
            "कौन सा/से निष्कर्ष निश्चित रूप से सत्य है/हैं।\n"
            "कथन: M < K ≤ N > P = J > O ≥ L\n"
            "निष्कर्ष I: N > L\n"
            "निष्कर्ष II: O = M"
        ),
        "option_a": "Only Conclusion II is true / केवल निष्कर्ष II सत्य है",
        "option_b": "Neither Conclusion I nor Conclusion II is true / न तो निष्कर्ष I और न ही निष्कर्ष II सत्य है",
        "option_c": "Only Conclusion I is true / केवल निष्कर्ष I सत्य है",
        "option_d": "Both Conclusion I and Conclusion II are true / निष्कर्ष I और II दोनों सत्य हैं",
        "correct_answer": "C",
        # I)N>L: N>P=J>O≥L → N>O≥L → N>L → TRUE
        # II)O=M: breaks at N (M<K≤N>P) → no O↔M → FALSE
    },
    # ── Q12 ── Either Conclusion I or II follows (complementary pair) ─────────
    {
        "question_number": 12,
        "difficulty": "hard",
        "question_en": (
            "Direction: In the given statement, the relationship between different elements "
            "is shown and two conclusions follow it. Choose the correct answer based on the "
            "information given below.\n"
            "Statements: 11 > 10 = 9 ; 11 < 12 ≤ 13 ; 12 > 14 = 15\n"
            "Conclusions:\n"
            "I. 14 > 10\n"
            "II. 15 ≤ 10\n"
            "[CHSL Tier 2 - 2 Nov 2023]"
        ),
        "question_hi": (
            "निर्देश: दिए गए कथन में विभिन्न तत्वों के बीच संबंध दर्शाया गया है "
            "और इसके बाद दो निष्कर्ष दिए गए हैं। नीचे दी गई जानकारी के आधार पर "
            "सही उत्तर चुनें।\n"
            "कथन: 11 > 10 = 9 ; 11 < 12 ≤ 13 ; 12 > 14 = 15\n"
            "निष्कर्ष:\n"
            "I. 14 > 10\n"
            "II. 15 ≤ 10"
        ),
        "option_a": "Only Conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Only Conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Either Conclusion I or II follows / या तो निष्कर्ष I या II अनुसरण करता है",
        "option_d": "Neither Conclusion I nor II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # Chain: 9=10<11<12>14=15; path 10↔14 breaks at 12 → no definite relation
        # I (14>10) and II (15≤10 ≡ 14≤10) form complementary pair covering all cases
        # → Either I or II must be true
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
