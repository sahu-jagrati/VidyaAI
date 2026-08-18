"""
seed_reasoning_alphabet_sheet3.py
=========================================
Seeds Alphabet Q20-Q26 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet3.py

Answer key (solution images verified):
  Q20  Kibble/Kennel/Kettle/Kicker/Kernel   → B  (2,5,3,1,4)
       Kennel<Kernel<Kettle<Kibble<Kicker
  Q21  Infant/Indolent/Inert/Infamous...    → A  (2,6,5,3,4,1)
       Indolent<Ineffable<Inefficient<Inert<Infamous<Infant
  Q22  VIRTUAL unchanged letter count       → B  (One/एक)
       Sorted: A,I,L,R,T,U,V; only I stays at position 2
  Q23  Incest/Inception/Incense...          → D  (4,5,3,2,1)
       Incapacity<Incentive<Incense<Inception<Incest [per PDF key; CPO-28 Jun 2024 Shift 2]
  Q24  Dinnerware/Dingiest/Dinosaurs...     → D  (2,6,5,1,3,4)
       Dingiest<Dingling<Dinkier<Dinnerware<Dinosaurs<Dinucleotide
  Q25  Word formation from CKIK (C,K,I,K)  → A  (1)
       Only KICK can be formed
  Q26  TROUBLEMAKING arranged alphabetically → A  (Twelve/बारह)
       Only M(pos 8) unchanged; 13-1=12 changed
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q20 ── Dict order: Kibble,Kennel,Kettle,Kicker,Kernel ────────────────
    # Ken-n(Kennel2) < Ker(Kernel5) < Ket(Kettle3) < Kib(Kibble1) < Kic(Kicker4) → 2,5,3,1,4
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": (
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "1. Kibble  2. Kennel  3. Kettle  4. Kicker  5. Kernel"
        ),
        "question_hi": (
            "उस विकल्प का चयन करें जो दिए गए शब्दों की अंग्रेजी शब्दकोश में उनके क्रम में "
            "सही व्यवस्था को इंगित करता है। "
            "1. Kibble  2. Kennel  3. Kettle  4. Kicker  5. Kernel"
        ),
        "option_a": "5, 2, 3, 1, 4",
        "option_b": "2, 5, 3, 1, 4",
        "option_c": "5, 3, 2, 1, 4",
        "option_d": "2, 3, 5, 4, 1",
        "correct_answer": "B",
        # Ken-n(Kennel) < Ker(Kernel) < Ket(Kettle) < Kib(Kibble) < Kic(Kicker) → 2,5,3,1,4
    },
    # ── Q21 ── Dict order: Infant,Indolent,Inert,Infamous,Inefficient,Ineffable ─
    # Ind(Indolent2)<Ine-f-f-a(Ineffable6)<Ine-f-f-i(Inefficient5)<Ine-r(Inert3)<Inf-a+famous(4)<Inf-a+fant(1)
    {
        "question_number": 21,
        "difficulty": "hard",
        "question_en": (
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "1. Infant  2. Indolent  3. Inert  4. Infamous  5. Inefficient  6. Ineffable"
        ),
        "question_hi": (
            "उस विकल्प का चयन करें जो दिए गए शब्दों के सही उस क्रम को दर्शाता है "
            "जैसा कि वे अंग्रेजी शब्दकोश में दिखाई देंगे। "
            "1. Infant  2. Indolent  3. Inert  4. Infamous  5. Inefficient  6. Ineffable"
        ),
        "option_a": "2, 6, 5, 3, 4, 1",
        "option_b": "5, 4, 3, 2, 1, 6",
        "option_c": "5, 3, 4, 6, 2, 1",
        "option_d": "2, 5, 6, 1, 4, 3",
        "correct_answer": "A",
        # Ind(2) < Ine-f-f-a(6) < Ine-f-f-i(5) < Ine-r(3) < Inf-a-m(4) < Inf-a-n(1)
    },
    # ── Q22 ── VIRTUAL letters unchanged after alphabetical rearrangement ──────
    # VIRTUAL → A,I,L,R,T,U,V; original pos 2 = I; sorted pos 2 = I → only I unchanged
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "The position of how many letters will remain unchanged if each of the letters "
            "in the word VIRTUAL is arranged in English alphabetical order?"
        ),
        "question_hi": (
            "यदि शब्द VIRTUAL के प्रत्येक अक्षर को अंग्रेजी वर्णमाला क्रम में व्यवस्थित किया जाए "
            "तो कितने अक्षरों के स्थान अपरिवर्तित रहेंगे?"
        ),
        "option_a": "None/कोई नहीं",
        "option_b": "One/एक",
        "option_c": "Three/तीन",
        "option_d": "More than three/तीन से अधिक",
        "correct_answer": "B",
        # V-I-R-T-U-A-L → sorted A,I,L,R,T,U,V; only I stays at position 2 → 1 unchanged
    },
    # ── Q23 ── Dict order: Incest,Inception,Incense,Incapacity,Incentive ────────
    # Per PDF key (CPO-28 Jun 2024 Shift 2): Incapacity<Incentive<Incense<Inception<Incest → 4,5,3,2,1
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "1. Incest  2. Inception  3. Incense  4. Incapacity  5. Incentive"
        ),
        "question_hi": (
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों की सही उस क्रम में व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं। "
            "1. Incest  2. Inception  3. Incense  4. Incapacity  5. Incentive"
        ),
        "option_a": "5, 3, 2, 1, 4",
        "option_b": "4, 3, 5, 2, 1",
        "option_c": "5, 4, 3, 2, 1",
        "option_d": "4, 5, 3, 2, 1",
        "correct_answer": "D",
        # Inca(4) < Ince-n-t(5) < Ince-n-s(3) < Incep(2) < Inces(1) per official CPO key → 4,5,3,2,1
    },
    # ── Q24 ── Dict order: Dinnerware,Dingiest,Dinosaurs,Dinucleotide,Dinkier,Dingling ─
    # Ding-i(2)<Ding-l(6)<Dink(5)<Dinn(1)<Dino(3)<Dinu(4) → 2,6,5,1,3,4
    {
        "question_number": 24,
        "difficulty": "hard",
        "question_en": (
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "1. Dinnerware  2. Dingiest  3. Dinosaurs  4. Dinucleotide  5. Dinkier  6. Dingling"
        ),
        "question_hi": (
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे। "
            "1. Dinnerware  2. Dingiest  3. Dinosaurs  4. Dinucleotide  5. Dinkier  6. Dingling"
        ),
        "option_a": "5, 2, 3, 6, 1, 4",
        "option_b": "2, 6, 3, 5, 1, 4",
        "option_c": "5, 2, 6, 3, 1, 4",
        "option_d": "2, 6, 5, 1, 3, 4",
        "correct_answer": "D",
        # Ding-i(Dingiest2) < Ding-l(Dingling6) < Dink(Dinkier5) < Dinn(Dinnerware1) < Dino(Dinosaurs3) < Dinu(Dinucleotide4)
    },
    # ── Q25 ── Word formation from CKIK (C,K,I,K) ────────────────────────────
    # Only KICK can be formed using each letter once
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": (
            "How many meaningful English words can be formed with the letters CKIK, "
            "using each letter only once in each word?"
        ),
        "question_hi": (
            "प्रत्येक शब्द में प्रत्येक अक्षर का केवल एक बार प्रयोग करते हुए, "
            "CKIK अक्षरों से कितने सार्थक अंग्रेजी शब्द बनाए जा सकते हैं?"
        ),
        "option_a": "1",
        "option_b": "4",
        "option_c": "2",
        "option_d": "3",
        "correct_answer": "A",   # KICK is the only meaningful word (C,K,I,K → K-I-C-K)
    },
    # ── Q26 ── TROUBLEMAKING: how many positions change after alphabetical sort? ─
    # T-R-O-U-B-L-E-M-A-K-I-N-G (13 letters)
    # Sorted: A,B,E,G,I,K,L,M,N,O,R,T,U
    # Only M stays at position 8 → 13-1=12 positions changed
    {
        "question_number": 26,
        "difficulty": "hard",
        "question_en": (
            "The position of how many letters will change if each of the letters in the word "
            "TROUBLEMAKING is arranged from left to right in alphabetical order?"
        ),
        "question_hi": (
            "यदि शब्द TROUBLEMAKING के प्रत्येक अक्षर को वर्णमाला क्रम में बाएं से दाएं व्यवस्थित किया जाए "
            "तो कितने अक्षरों की स्थिति बदल जाएगी?"
        ),
        "option_a": "Twelve/बारह",
        "option_b": "All/सभी",
        "option_c": "Ten/दस",
        "option_d": "Eleven/ग्यारह",
        "correct_answer": "A",
        # TROUBLEMAKING→sorted: A,B,E,G,I,K,L,M,N,O,R,T,U; only M(pos8) unchanged → 12 changed
    },
]

# Fix map for pre-existing records (ans=None)
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
