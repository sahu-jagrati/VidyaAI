"""
seed_reasoning_alphabet_sheet10.py
=========================================
Seeds Alphabet Q89-Q101 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet10.py

Mixed question types:
  - Digit ascending rearrangement + unchanged position count (Q89)
  - Meaningful word formation from specific letter positions (Q90)
  - Dictionary ordering (Q91-Q98, Q101)
  - Which word comes at 3rd position after dict ordering (Q99-Q100)

Answer key (solutions verified):
  Q89  7148356 ascending→1,3,4,5,6,7,8; only pos-3 digit 4 unchanged → B (One/एक)
       [CGL Tier II-26 Oct 2023 Shift 1]
  Q90  HOCKEY 2nd,4th,5th,6th = O,K,E,Y → YOKE only → D (One/एक)
       [CGL Tier II-26 Oct 2023 Shift 1]
  Q91  Pronoun<Proof<Propel<Proper<Prophecy → B (2,3,5,1,4)
       PRO-N < PRO-O < PROP-EL < PROP-ER < PROP-H  [CHSL-3 June 2022 Shift 2]
  Q92  Producer<Profound<Prophet<Prudent<Puberty<Quest → D (3,6,1,2,5,4)
       PRO-D < PRO-F < PRO-P < PRU < PUB < Q  [CHSL-2 June 2022 Shift 3]
  Q93  Calcium<Calculate<Calendar<Carrot<Catalyst → C (3,4,5,2,1)
       CALC-I(9) < CALC-U(21) so Calcium before Calculate  [CHSL-2 June 2022 Shift 2]
       NOTE: User said A=(4,3,5,2,1) putting Calculate before Calcium; I<U so
       Calcium(3) must come first → stored C=(3,4,5,2,1).
  Q94  Facsimile<Fanatical<Favourable<Frightful<Fructification → C (1,5,3,2,4)
       FAC < FAN < FAV < FRI < FRU  [CHSL-2 June 2022 Shift 1]
  Q95  Necessary<Needlework<Negotiate<Neigh<Networks → D (1,4,3,5,2)
       NEC < NEED < NEGO < NEI < NET  [CHSL-2 June 2022 Shift 1]
  Q96  Expedition<Expel<Expenditure<Expensive<Experience → A (2,4,5,1,3)
       EXPE-D < EXPE-L < EXPEN-D < EXPEN-S < EXPE-R  [CGL-03 Dec 2022 Shift 1]
       NOTE: User said C=(5,2,1,4,3) and also stated wrong sequence 2,5,4,1,3;
       correct 5th letters: Expedition=D, Expel=L, Expenditure=N, Expensive=N,
       Experience=R; within 5th=N: Expenditure has 6th=D < Expensive 6th=S
       → correct sequence 2,4,5,1,3 = A.
  Q97  Miscalculate<Miscall<Miscasting<Miscellaneous<Mischance → B (2,4,5,1,3)
       MISC-A-L-C < MISC-A-L-L < MISC-A-S < MISC-E < MISC-H  [CGL-06 Dec 2022 Shift 2]
       NOTE: User said (a) but provided correct sequence 2,4,5,1,3 = option B.
  Q98  Pardon<Pardoner<Parental<Parenthesis<Parenthetical → C (4,1,3,5,2)
       PARD-ON < PARD-ONE-R < PARE-N-T-A < PARE-N-T-H-E-S < PARE-N-T-H-E-T
       [CGL-03 Dec 2022 Shift 3]
  Q99  Oblate<Oblige<Oblique<Oblivion<Oblong → 3rd = Oblique → B
       OBL-A < OBL-I-G < OBL-I-Q < OBL-I-V < OBL-O  [CGL-06 Dec 2022 Shift 3]
       NOTE: User said C (Oblige) but Oblige is 2nd; 3rd position is Oblique = B.
  Q100 Chock<Chocoholic<Chocolate<Chocolatier<Chocolaty → 3rd = Chocolate → A
       CHOCK(K) < CHOCOHO(H) < CHOCOLAT-E < CHOCOLAT-I < CHOCOLAT-Y  [CGL-06 Dec 2022 Shift 4]
  Q101 Humanity<Humanoid<Humbug<Humectants<Humidity<Humility<Humoresque → A (6,3,2,7,4,1,5)
       HUMA-N-I < HUMA-N-O < HUM-B < HUM-E-C < HUM-I-D < HUM-I-L < HUM-O
       [CGL-05 Dec 2022 Shift 3]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet10"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q89 ── Digit ascending rearrangement: how many digits stay in same position ──
    # 7148356 → ascending: 1,3,4,5,6,7,8
    # Pos comparison: 7≠1, 1≠3, 4=4(✓), 8≠5, 3≠6, 5≠7, 6≠8 → only pos-3 unchanged
    {
        "question_number": 89,
        "difficulty": "medium",
        "question_en": (
            "Each of the digits in the number 7148356 is arranged in ascending order "
            "from left to right. The position of how many digits will remain unchanged "
            "as compared to that in the original number? "
            "[CGL Tier II-26 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "संख्या 7148356 में प्रत्येक अंक को बाएं से दाएं बढ़ते क्रम में व्यवस्थित किया गया है। "
            "मूल संख्या की तुलना में कितने अंकों की स्थिति अपरिवर्तित रहेगी?"
        ),
        "option_a": "None/कोई नहीं",
        "option_b": "One/एक",
        "option_c": "Two/दो",
        "option_d": "Three/तीन",
        "correct_answer": "B",
        # Ascending: 1,3,4,5,6,7,8 — only the digit 4 stays at position 3
    },
    # ── Q90 ── HOCKEY letters 2nd,4th,5th,6th = O,K,E,Y → meaningful words ───────
    # O,K,E,Y → YOKE is the only meaningful English word using all 4 letters
    {
        "question_number": 90,
        "difficulty": "easy",
        "question_en": (
            "How many meaningful English words can be formed with the second, fourth, "
            "fifth and sixth letters of the word HOCKEY "
            "(when counted from left to right), using each letter only once in each word? "
            "[CGL Tier II-26 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द HOCKEY के दूसरे, चौथे, पाँचवें और छठे अक्षरों (बाएं से दाएं गिनने पर) "
            "से प्रत्येक अक्षर का केवल एक बार प्रयोग करते हुए कितने सार्थक अंग्रेजी शब्द बनाए जा सकते हैं?"
        ),
        "option_a": "Three/तीन",
        "option_b": "Two/दो",
        "option_c": "Zero/शून्य",
        "option_d": "One/एक",
        "correct_answer": "D",
        # HOCKEY: H(1)O(2)C(3)K(4)E(5)Y(6); 2nd=O,4th=K,5th=E,6th=Y → YOKE only
    },
    # ── Q91 ── Pronoun<Proof<Propel<Proper<Prophecy → 2,3,5,1,4 ──────────────────
    {
        "question_number": 91,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Proper 2.Pronoun 3.Proof 4.Prophecy 5.Propel — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CHSL-3 June 2022 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Proper 2.Pronoun 3.Proof 4.Prophecy 5.Propel — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "2, 3, 1, 5, 4",
        "option_b": "2, 3, 5, 1, 4",
        "option_c": "2, 1, 5, 3, 4",
        "option_d": "2, 1, 3, 5, 4",
        "correct_answer": "B",
        # PRO-N(2) < PRO-O(3) < PROP-EL(5) < PROP-ER(1) < PROP-H(4)
    },
    # ── Q92 ── Producer<Profound<Prophet<Prudent<Puberty<Quest → 3,6,1,2,5,4 ──────
    {
        "question_number": 92,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Prophet 2.Prudent 3.Producer 4.Quest 5.Puberty 6.Profound — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CHSL-2 June 2022 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Prophet 2.Prudent 3.Producer 4.Quest 5.Puberty 6.Profound — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 5, 6, 1, 2, 4",
        "option_b": "3, 6, 2, 1, 5, 4",
        "option_c": "3, 1, 6, 5, 2, 4",
        "option_d": "3, 6, 1, 2, 5, 4",
        "correct_answer": "D",
        # PRO-D(3) < PRO-F(6) < PRO-P(1) < PRU(2) < PUB(5) < Q(4)
    },
    # ── Q93 ── Calcium<Calculate<Calendar<Carrot<Catalyst → 3,4,5,2,1 ──────────
    # NOTE: User said A=(4,3,5,2,1) putting Calculate before Calcium.
    # CALC-I(Calcium 5th=I=9) vs CALC-U(Calculate 5th=U=21): I<U → Calcium first → stored C.
    {
        "question_number": 93,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Catalyst 2.Carrot 3.Calcium 4.Calculate 5.Calendar — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CHSL-2 June 2022 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Catalyst 2.Carrot 3.Calcium 4.Calculate 5.Calendar — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "4, 3, 5, 2, 1",
        "option_b": "4, 5, 3, 2, 1",
        "option_c": "3, 4, 5, 2, 1",
        "option_d": "3, 2, 1, 4, 5",
        "correct_answer": "C",
        # CALC-I(3) < CALC-U(4) < CALE(5) < CAR(2) < CAT(1)
        # I(9th letter) < U(21st letter) → Calcium before Calculate
    },
    # ── Q94 ── Facsimile<Fanatical<Favourable<Frightful<Fructification → 1,5,3,2,4 ─
    {
        "question_number": 94,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Facsimile 2.Frightful 3.Favourable 4.Fructification 5.Fanatical — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CHSL-2 June 2022 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Facsimile 2.Frightful 3.Favourable 4.Fructification 5.Fanatical — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "1, 4, 2, 5, 3",
        "option_b": "1, 3, 4, 2, 5",
        "option_c": "1, 5, 3, 2, 4",
        "option_d": "1, 3, 4, 5, 2",
        "correct_answer": "C",
        # FA-C(1) < FA-N(5) < FA-V(3) < FR-I(2) < FR-U(4)
    },
    # ── Q95 ── Necessary<Needlework<Negotiate<Neigh<Networks → 1,4,3,5,2 ──────────
    {
        "question_number": 95,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Necessary 2.Networks 3.Negotiate 4.Needlework 5.Neigh — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CHSL-2 June 2022 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Necessary 2.Networks 3.Negotiate 4.Needlework 5.Neigh — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "4, 1, 3, 5, 2",
        "option_b": "1, 4, 5, 3, 2",
        "option_c": "3, 4, 1, 5, 2",
        "option_d": "1, 4, 3, 5, 2",
        "correct_answer": "D",
        # NE-C(1) < NE-E(4) < NE-G(3) < NE-I(5) < NE-T(2)
    },
    # ── Q96 ── Expedition<Expel<Expenditure<Expensive<Experience → 2,4,5,1,3 ──────
    # NOTE: User said C=(5,2,1,4,3) which is wrong.
    # 5th letter: Expedition=D, Expel=L, Expenditure=N, Expensive=N, Experience=R
    # D<L<N<R; within EXPEN: 6th=D(Expenditure) < 6th=S(Expensive) → stored A.
    {
        "question_number": 96,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Expensive 2.Expedition 3.Experience 4.Expel 5.Expenditure — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-03 Dec 2022 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Expensive 2.Expedition 3.Experience 4.Expel 5.Expenditure — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "2, 4, 5, 1, 3",
        "option_b": "2, 4, 5, 3, 1",
        "option_c": "5, 2, 1, 4, 3",
        "option_d": "4, 2, 5, 1, 3",
        "correct_answer": "A",
        # EXPE-D(2) < EXPE-L(4) < EXPEN-D(5) < EXPEN-S(1) < EXPE-R(3)
    },
    # ── Q97 ── Miscalculate<Miscall<Miscasting<Miscellaneous<Mischance → 2,4,5,1,3 ─
    # NOTE: User said (a) but sequence 2,4,5,1,3 matches option B.
    {
        "question_number": 97,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Miscellaneous 2.Miscalculate 3.Mischance 4.Miscall 5.Miscasting — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-06 Dec 2022 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Miscellaneous 2.Miscalculate 3.Mischance 4.Miscall 5.Miscasting — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "2, 4, 1, 5, 3",
        "option_b": "2, 4, 5, 1, 3",
        "option_c": "4, 2, 5, 3, 1",
        "option_d": "4, 2, 5, 1, 3",
        "correct_answer": "B",
        # MISC-A-L-C(2) < MISC-A-L-L(4) < MISC-A-S(5) < MISC-E(1) < MISC-H(3)
    },
    # ── Q98 ── Pardon<Pardoner<Parental<Parenthesis<Parenthetical → 4,1,3,5,2 ──────
    {
        "question_number": 98,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Pardoner 2.Parenthetical 3.Parental 4.Pardon 5.Parenthesis — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-03 Dec 2022 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Pardoner 2.Parenthetical 3.Parental 4.Pardon 5.Parenthesis — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "1, 4, 3, 2, 5",
        "option_b": "4, 1, 3, 2, 5",
        "option_c": "4, 1, 3, 5, 2",
        "option_d": "1, 4, 3, 5, 2",
        "correct_answer": "C",
        # PARD-ON(4) < PARD-ONE-R(1) < PARE-N-T-A(3) < PARE-N-T-H-E-S(5) < PARE-N-T-H-E-T(2)
    },
    # ── Q99 ── Oblate<Oblige<Oblique<Oblivion<Oblong → 3rd position = Oblique ──────
    # NOTE: User said C (Oblige) but Oblige is 2nd; 3rd = Oblique = B.
    # OBL-A(Oblate) < OBL-I-G(Oblige) < OBL-I-Q(Oblique) < OBL-I-V(Oblivion) < OBL-O(Oblong)
    {
        "question_number": 99,
        "difficulty": "medium",
        "question_en": (
            "After arranging the given words according to dictionary order, "
            "which word will come at the 'Third' position? "
            "1. Oblivion  2. Oblique  3. Oblige  4. Oblate  5. Oblong "
            "[CGL-06 Dec 2022 Shift 3]"
        ),
        "question_hi": (
            "दिए गए शब्दों को शब्दकोश क्रम के अनुसार व्यवस्थित करने पर, "
            "कौन-सा शब्द तीसरे स्थान पर आएगा? "
            "1. Oblivion  2. Oblique  3. Oblige  4. Oblate  5. Oblong"
        ),
        "option_a": "Oblate",
        "option_b": "Oblique",
        "option_c": "Oblige",
        "option_d": "Oblivion",
        "correct_answer": "B",
        # Order: Oblate(4)→1st, Oblige(3)→2nd, Oblique(2)→3rd, Oblivion(1)→4th, Oblong(5)→5th
    },
    # ── Q100 ── Chock<Chocoholic<Chocolate<Chocolatier<Chocolaty → 3rd = Chocolate ──
    {
        "question_number": 100,
        "difficulty": "medium",
        "question_en": (
            "After arranging the given words according to dictionary order, "
            "which word will come at the 'Third' position? "
            "1. Chocolate  2. Chocoholic  3. Chocolaty  4. Chocolatier  5. Chock "
            "[CGL-06 Dec 2022 Shift 4]"
        ),
        "question_hi": (
            "दिए गए शब्दों को शब्दकोश क्रम के अनुसार व्यवस्थित करने पर, "
            "कौन-सा शब्द तीसरे स्थान पर आएगा? "
            "1. Chocolate  2. Chocoholic  3. Chocolaty  4. Chocolatier  5. Chock"
        ),
        "option_a": "Chocolate",
        "option_b": "Chock",
        "option_c": "Chocolatier",
        "option_d": "Chocoholic",
        "correct_answer": "A",
        # Order: Chock(5)→1st, Chocoholic(2)→2nd, Chocolate(1)→3rd, Chocolatier(4)→4th, Chocolaty(3)→5th
        # CHOC-K < CHOCO-H < CHOCOLAT-E < CHOCOLAT-I < CHOCOLAT-Y
    },
    # ── Q101 ── Humanity<Humanoid<Humbug<Humectants<Humidity<Humility<Humoresque → 6,3,2,7,4,1,5 ─
    {
        "question_number": 101,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Humility 2.Humbug 3.Humanoid 4.Humidity 5.Humoresque "
            "6.Humanity 7.Humectants — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-05 Dec 2022 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Humility 2.Humbug 3.Humanoid 4.Humidity 5.Humoresque "
            "6.Humanity 7.Humectants — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "6, 3, 2, 7, 4, 1, 5",
        "option_b": "6, 3, 2, 7, 1, 4, 5",
        "option_c": "6, 3, 7, 2, 1, 4, 5",
        "option_d": "6, 3, 7, 2, 4, 1, 5",
        "correct_answer": "A",
        # HUMA-N-I(6) < HUMA-N-O(3) < HUM-B(2) < HUM-E-C(7) < HUM-I-D(4) < HUM-I-L(1) < HUM-O(5)
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
