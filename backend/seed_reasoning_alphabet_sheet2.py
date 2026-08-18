"""
seed_reasoning_alphabet_sheet2.py
=========================================
Seeds Alphabet Q14-Q19 from Gagan Pratap Reasoning PDFs.
Also fixes Q13 options to match actual PDF options.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet2.py

Answer key (solution images verified):
  Q13 FIX  Dead/Deal/Dean/Dear/Death    → C  (43215)    options fixed to match PDF
  Q14      JUSTICE letter distance      → C  (4)         E(5th) to J(10th) → F,G,H,I = 4 letters
  Q15      Ferocious/Fervor/Fiction...  → D  (4,5,6,1,2,3)  Faith<Feign<Ferment<Ferocious<Fervor<Fiction
  Q16      Temperament/Tenure/Tenant... → C  (1,6,5,3,4,2)  Temperament<Temperature<Temptation<Tenant<Tender<Tenure
  Q17      Dermatology/Derogation...    → C  (4,6,3,1,5,2)  Derailed<Deregulation<Derivative<Dermatology<Dermestid<Derogation
  Q18      Consistence/Conscience...    → D  (3,2,4,5,6,1)  Conflagration<Conscience<Consequence<Considerable<Consignment<Consistence
  Q19      4th word: Wheel/Wheat/Whale  → D  (When)          Whale<Wheat<Wheel<When<Whet; 4th=When
           [GD Con-20 Feb 2024 Shift 3] Solution says option(e) but DB has 4 slots; When stored as D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q14 ── JUSTICE → C,E,I,J,S,T,U; 2nd from left=E(5th), 4th from right=J(10th) ──
    # Letters between E and J: F,G,H,I = 4
    {
        "question_number": 14,
        "difficulty": "hard",
        "question_en": (
            "Each of the letters in the word JUSTICE are arranged in alphabetical order. "
            "How many letters are there in the English alphabetical series between the letter "
            "that is second from the left and the one that is fourth from the right "
            "in the new letter cluster thus formed?"
        ),
        "question_hi": (
            "शब्द JUSTICE के प्रत्येक अक्षर को वर्णमाला क्रम में व्यवस्थित किया गया है। "
            "इस प्रकार बने नए अक्षर समूह में बाईं से दूसरे अक्षर और दाईं से चौथे अक्षर के बीच "
            "अंग्रेजी वर्णमाला श्रृंखला में कितने अक्षर हैं?"
        ),
        "option_a": "7",
        "option_b": "6",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "C",
        # JUSTICE → C,E,I,J,S,T,U; 2nd from left=E(5), 4th from right=J(10); F,G,H,I between = 4
    },
    # ── Q15 ── 6 words: Ferocious,Fervor,Fiction,Faith,Feign,Ferment ────────────
    # Faith(4) < Feign(5) < Ferment(6) < Ferocious(1) < Fervor(2) < Fiction(3) → 4,5,6,1,2,3
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "1. Ferocious  2. Fervor  3. Fiction  4. Faith  5. Feign  6. Ferment"
        ),
        "question_hi": (
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के सही उस क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं। "
            "1. Ferocious  2. Fervor  3. Fiction  4. Faith  5. Feign  6. Ferment"
        ),
        "option_a": "6, 5, 2, 1, 4, 3",
        "option_b": "6, 4, 5, 3, 2, 1",
        "option_c": "4, 6, 5, 2, 1, 3",
        "option_d": "4, 5, 6, 1, 2, 3",
        "correct_answer": "D",
        # Fai(Faith4) < Fei(Feign5) < Fer-m(Ferment6) < Fer-o(Ferocious1) < Fer-v(Fervor2) < Fic(Fiction3)
    },
    # ── Q16 ── 6 words: Temperament,Tenure,Tenant,Tender,Temptation,Temperature ─
    # Temperament(1) < Temperature(6) < Temptation(5) < Tenant(3) < Tender(4) < Tenure(2) → 1,6,5,3,4,2
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "1. Temperament  2. Tenure  3. Tenant  4. Tender  5. Temptation  6. Temperature"
        ),
        "question_hi": (
            "उस विकल्प का चयन करें जो दिए गए शब्दों के सही क्रम को दर्शाता है "
            "जैसा कि वे अंग्रेजी शब्दकोश में दिखाई देंगे। "
            "1. Temperament  2. Tenure  3. Tenant  4. Tender  5. Temptation  6. Temperature"
        ),
        "option_a": "1, 6, 5, 2, 4, 3",
        "option_b": "1, 5, 6, 3, 4, 2",
        "option_c": "1, 6, 5, 3, 4, 2",
        "option_d": "1, 5, 6, 2, 4, 3",
        "correct_answer": "C",
        # Temp-e-r-a(Temperament1) < Temp-e-r-a-t(Temperature6) < Temp-t(Temptation5) < Ten-a(Tenant3) < Ten-d(Tender4) < Ten-u(Tenure2)
    },
    # ── Q17 ── 6 words: Dermatology,Derogation,Derivative,Derailed,Dermestid,Deregulation ─
    # Derailed(4) < Deregulation(6) < Derivative(3) < Dermatology(1) < Dermestid(5) < Derogation(2)
    {
        "question_number": 17,
        "difficulty": "hard",
        "question_en": (
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "1. Dermatology  2. Derogation  3. Derivative  4. Derailed  5. Dermestid  6. Deregulation"
        ),
        "question_hi": (
            "उस विकल्प का चयन करें जो दिए गए शब्दों की सही क्रम को दर्शाता है "
            "जैसा कि वे अंग्रेजी शब्दकोश में दिखाई देंगे। "
            "1. Dermatology  2. Derogation  3. Derivative  4. Derailed  5. Dermestid  6. Deregulation"
        ),
        "option_a": "4, 3, 2, 1, 5, 6",
        "option_b": "4, 6, 3, 2, 1, 5",
        "option_c": "4, 6, 3, 1, 5, 2",
        "option_d": "4, 6, 1, 5, 3, 2",
        "correct_answer": "C",
        # Dera(Derailed4) < Dere(Deregulation6) < Deri(Derivative3) < Derm-a(Dermatology1) < Derm-e(Dermestid5) < Dero(Derogation2)
    },
    # ── Q18 ── 6 words: Consistence,Conscience,Conflagration,Consequence,Considerable,Consignment ─
    # Conflagration(3) < Conscience(2) < Consequence(4) < Considerable(5) < Consignment(6) < Consistence(1)
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": (
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "1. Consistence  2. Conscience  3. Conflagration  4. Consequence  5. Considerable  6. Consignment"
        ),
        "question_hi": (
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है, "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे। "
            "1. Consistence  2. Conscience  3. Conflagration  4. Consequence  5. Considerable  6. Consignment"
        ),
        "option_a": "4, 3, 2, 5, 6, 1",
        "option_b": "4, 2, 3, 5, 1, 6",
        "option_c": "3, 4, 2, 5, 6, 1",
        "option_d": "3, 2, 4, 5, 6, 1",
        "correct_answer": "D",
        # Conf(Conflagration3) < Cons-c-i-e-n-c(Conscience2) < Cons-e-q(Consequence4) < Cons-i-d(Considerable5) < Cons-i-g(Consignment6) < Cons-i-s(Consistence1)
    },
    # ── Q19 ── 4th word in dict order: Wheel,Wheat,Whale,Whet,When ───────────────
    # Whale(3) < Wheat(2) < Wheel(1) < When(5) < Whet(4) → 4th position = When (word 5)
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": (
            "After arranging the given words according to dictionary order, "
            "which word comes at the fourth position? "
            "1. Wheel  2. Wheat  3. Whale  4. Whet  5. When"
        ),
        "question_hi": (
            "दिए गए शब्दों को शब्दकोश क्रम के अनुसार व्यवस्थित करने के बाद कौन सा शब्द "
            "चौथे स्थान पर आएगा? "
            "1. Wheel  2. Wheat  3. Whale  4. Whet  5. When"
        ),
        "option_a": "Wheat",
        "option_b": "Wheel",
        "option_c": "Whet",
        "option_d": "When",
        "correct_answer": "D",
        # Wha(Whale) < Whe-a(Wheat) < Whe-e(Wheel) < Whe-n(When)← 4th < Whe-t(Whet)
    },
]

# Fix Q13 options to match actual PDF (sequence 4,3,2,1,5 → option C in PDF = "43215")
_Q13_FIX = {
    "option_a": "1, 3, 2, 5, 4",   # 13254
    "option_b": "4, 3, 2, 5, 1",   # 43251
    "option_c": "4, 3, 2, 1, 5",   # 43215 ← correct (Dead<Deal<Dean<Dear<Death)
    "option_d": "1, 3, 2, 4, 5",   # 13245
}

# Fix map for newly inserted records with correct_answer=None
_FIXES = {
    q["question_number"]: (q["correct_answer"], {
        "option_a": q["option_a"],
        "option_b": q["option_b"],
        "option_c": q["option_c"],
        "option_d": q["option_d"],
    })
    for q in QUESTIONS
}


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_short = {
            row[0][:80]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            fp = d["question_en"][:80]
            if fp in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB (will update below)")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")

        # ── Fix Q13 options to match actual PDF options ──────────────────────
        q13 = db.query(Question).filter(
            Question.topic == TOPIC,
            Question.subject == SUBJECT,
            Question.question_number == 13,
        ).first()
        if q13:
            for field, val in _Q13_FIX.items():
                setattr(q13, field, val)
            q13.correct_answer = "C"   # 4,3,2,1,5 is option_c in PDF
            q13.source_pdf = "Gagan_Pratap_Reasoning_Alphabet_Sheet1"
            print("  FIXED Q13: options updated to match PDF; correct_answer=C")

        db.commit()

        # ── Fix any pre-existing records with correct_answer=None ─────────────
        updates = 0
        for qnum, (ans, fields) in _FIXES.items():
            q = db.query(Question).filter(
                Question.topic == TOPIC,
                Question.subject == SUBJECT,
                Question.question_number == qnum,
                Question.correct_answer == None,
            ).first()
            if q:
                q.correct_answer = ans
                for field, val in fields.items():
                    setattr(q, field, val)
                q.source_pdf = SOURCE
                updates += 1
                print(f"  UPDATE Q{qnum}: correct_answer={ans}")

        db.commit()
        if updates:
            print(f"Fixed {updates} pre-existing records.")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
