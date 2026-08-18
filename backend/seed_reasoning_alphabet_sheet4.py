"""
seed_reasoning_alphabet_sheet4.py
=========================================
Seeds Alphabet Q27-Q34 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet4.py

NOTE: Ordering questions use "Words: [list] — ..." format so first-80-char
fingerprints are unique (avoids collision with earlier questions sharing the
same long preamble text).

Answer key (solution text verified):
  Q27  Straight/Strict/Stamp/Sticker/Streaming → C  (3,4,1,5,2)
       STA-M(Stamp3)<STI-C(Sticker4)<STR-A(Straight1)<STR-E(Streaming5)<STR-I(Strict2)
  Q28  STRANGE letter distance                 → B  (Four)
       sorted A,E,G,N,R,S,T; 4th=N(14), 2nd-right=S(19); O,P,Q,R = 4 between
  Q29  Mountain/Mould/Monster/Mouth/Moving     → B  (3,2,1,4,5)
       Monster<Mould<Mountain<Mouth<Moving
  Q30  Lambast/Lighten/Legacy/Languish...      → A  (1,4,5,3,2,6)
       Lambast<Languish<Laughter<Legacy<Lighten<Lightly
  Q31  Highway/History/Hired/Hierarchy/Hibiscus→ C  (5,4,1,3,2)
       Hibiscus<Hierarchy<Highway<Hired<History
  Q32  ETHICAL vowels+1 consonants-1 → FSGJBBK  → B  (Three)
       3rd=G(7), 1st-right=K(11); H,I,J = 3 between
  Q33  Greed/Green/Grown/Grip/Granite          → C  (5,1,2,4,3)
       Granite<Greed<Green<Grip<Grown
  Q34  Significant/Sinful/Signed/Singing/Simplify → A  (3,1,5,2,4)
       Signed<Significant<Simplify<Sinful<Singing
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q27 ── Stamp<Sticker<Straight<Streaming<Strict → 3,4,1,5,2 ──────────
    {
        "question_number": 27,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Straight 2.Strict 3.Stamp 4.Sticker 5.Streaming — "
            "Which option represents the correct order of the given words "
            "as they would appear in the English dictionary? "
            "[GD Con-24 Jan 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Straight 2.Strict 3.Stamp 4.Sticker 5.Streaming — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "3, 5, 4, 1, 2",
        "option_b": "4, 5, 2, 3, 1",
        "option_c": "3, 4, 1, 5, 2",
        "option_d": "4, 3, 1, 5, 2",
        "correct_answer": "C",
        # STA-M(3) < STI-C(4) < STR-A(1) < STR-E(5) < STR-I(2) → 3,4,1,5,2
    },
    # ── Q28 ── STRANGE: sorted A,E,G,N,R,S,T; 4th=N(14), 2nd-right=S(19) ────
    # Between N and S: O,P,Q,R = 4 letters
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            "Each of the letters in the word STRANGE are arranged in alphabetical order. "
            "How many letters are there in the English alphabetical series between the "
            "letter which is fourth from the left and the one which is second from the right "
            "in the new letter cluster thus formed?"
        ),
        "question_hi": (
            "शब्द STRANGE के प्रत्येक अक्षर को वर्णमाला क्रम में व्यवस्थित किया गया है। "
            "इस प्रकार बने नए अक्षर-समूह में बाएं से चौथे अक्षर और दाएं से दूसरे अक्षर के बीच "
            "अंग्रेजी वर्णमाला श्रृंखला में कितने अक्षर हैं?"
        ),
        "option_a": "Five/पाँच",
        "option_b": "Four/चार",
        "option_c": "Three/तीन",
        "option_d": "Two/दो",
        "correct_answer": "B",
        # A,E,G,N,R,S,T; 4th=N(14th), 2nd from right=S(19th); O,P,Q,R = 4 letters between
    },
    # ── Q29 ── Monster<Mould<Mountain<Mouth<Moving → 3,2,1,4,5 ──────────────
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Mountain 2.Mould 3.Monster 4.Mouth 5.Moving — "
            "Which option represents the correct order of the given words "
            "as they would appear in the English dictionary? "
            "[GD Con-16 Jan 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Mountain 2.Mould 3.Monster 4.Mouth 5.Moving — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "2, 3, 1, 4, 5",
        "option_b": "3, 2, 1, 4, 5",
        "option_c": "1, 2, 3, 4, 5",
        "option_d": "4, 3, 2, 1, 5",
        "correct_answer": "B",
        # Mon(Monster3) < Mou-l(Mould2) < Mou-n(Mountain1) < Mou-t(Mouth4) < Mov(Moving5)
    },
    # ── Q30 ── Lambast<Languish<Laughter<Legacy<Lighten<Lightly → 1,4,5,3,2,6 ─
    {
        "question_number": 30,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Lambast 2.Lighten 3.Legacy 4.Languish 5.Laughter 6.Lightly — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-17 July 2023 Shift 4]"
        ),
        "question_hi": (
            "शब्द: 1.Lambast 2.Lighten 3.Legacy 4.Languish 5.Laughter 6.Lightly — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "1, 4, 5, 3, 2, 6",
        "option_b": "1, 4, 5, 2, 3, 6",
        "option_c": "1, 5, 4, 2, 3, 6",
        "option_d": "1, 5, 4, 3, 6, 2",
        "correct_answer": "A",
        # Lam(1) < Lan(4) < Lau(5) < Leg(3) < Ligh-t-e(2) < Ligh-t-l(6) → 1,4,5,3,2,6
    },
    # ── Q31 ── Hibiscus<Hierarchy<Highway<Hired<History → 5,4,1,3,2 ──────────
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Highway 2.History 3.Hired 4.Hierarchy 5.Hibiscus — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[CGL-17 July 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Highway 2.History 3.Hired 4.Hierarchy 5.Hibiscus — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "5, 4, 3, 1, 2",
        "option_b": "5, 4, 3, 2, 1",
        "option_c": "5, 4, 1, 3, 2",
        "option_d": "5, 4, 2, 1, 3",
        "correct_answer": "C",
        # Hib(5) < Hie(4) < Hig(1) < Hir(3) < His(2) → 5,4,1,3,2
    },
    # ── Q32 ── ETHICAL: vowels→next, consonants→prev; new word FSGJBBK ─────────
    # 3rd from left = G(7th), 1st from right = K(11th); H,I,J = 3 letters between
    {
        "question_number": 32,
        "difficulty": "hard",
        "question_en": (
            "Each vowel in the word ETHICAL is changed to the following letter in the "
            "English alphabetical series and each consonant is changed to the previous "
            "letter in the English alphabetical series. In the newly formed word, how many "
            "alphabets are there in the English alphabetical series between the alphabet "
            "which is 3rd from the left and 1st from the right?"
        ),
        "question_hi": (
            "शब्द ETHICAL में प्रत्येक स्वर को अंग्रेजी वर्णमाला श्रृंखला में अगले अक्षर से बदल दिया जाता है "
            "और प्रत्येक व्यंजन को अंग्रेजी वर्णमाला श्रृंखला में पिछले अक्षर से बदल दिया गया है। "
            "नवगठित शब्द में, बाएं से तीसरे और दाएं से पहले अक्षर के बीच अंग्रेजी वर्णमाला श्रृंखला में कितने अक्षर हैं?"
        ),
        "option_a": "Four/चार",
        "option_b": "Three/तीन",
        "option_c": "Two/दो",
        "option_d": "Five/पाँच",
        "correct_answer": "B",
        # E→F, T→S, H→G, I→J, C→B, A→B, L→K → FSGJBBK; 3rd=G(7), last=K(11); H,I,J = 3 between
    },
    # ── Q33 ── Granite<Greed<Green<Grip<Grown → 5,1,2,4,3 ───────────────────
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Greed 2.Green 3.Grown 4.Grip 5.Granite — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[CGL-17 July 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Greed 2.Green 3.Grown 4.Grip 5.Granite — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "5, 2, 1, 4, 3",
        "option_b": "5, 4, 1, 2, 3",
        "option_c": "5, 1, 2, 4, 3",
        "option_d": "5, 1, 4, 3, 2",
        "correct_answer": "C",
        # Gra(5) < Gree-d(1) < Gree-n(2) < Gri(4) < Gro(3) → 5,1,2,4,3
    },
    # ── Q34 ── Signed<Significant<Simplify<Sinful<Singing → 3,1,5,2,4 ────────
    {
        "question_number": 34,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Significant 2.Sinful 3.Signed 4.Singing 5.Simplify — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-18 July 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Significant 2.Sinful 3.Signed 4.Singing 5.Simplify — "
            "उस विकल्प का चयन करें जो दिए गए शब्दों को उसी प्रकार दर्शाता है "
            "जिस प्रकार वे अंग्रेजी शब्दकोश में दिखाई देंगे।"
        ),
        "option_a": "3, 1, 5, 2, 4",
        "option_b": "3, 5, 1, 2, 4",
        "option_c": "3, 2, 1, 5, 4",
        "option_d": "3, 1, 2, 5, 4",
        "correct_answer": "A",
        # Sig-n-e(Signed3) < Sig-n-i(Significant1) < Sim(Simplify5) < Sin-f(Sinful2) < Sin-g(Singing4) → 3,1,5,2,4
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        # Use question_number-based dedup to avoid fingerprint collision issues
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
