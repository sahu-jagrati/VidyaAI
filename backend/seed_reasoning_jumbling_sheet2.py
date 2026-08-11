"""
seed_reasoning_jumbling_sheet2.py
====================================
Seeds Jumbling questions Q27-Q32 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Jumbling
Run     : python seed_reasoning_jumbling_sheet2.py

Two question sub-types:
  Type A (Q27)   : Letter codes assigned; find permutation that forms a word.
  Type B (Q28-32): Arrange given words in meaningful (logical) order.

Answer key (verified via Python):
  Q27  R=1,E=2,A=3,C=4,T=5,I=6,V=7,E=8        → A (CREATIVE)
  Q28  House/Road/Room/Town/District             → C  3,1,2,4,5  (small→large)
  Q29  Doctor/Fever/Medicine/Medical Shop        → B  Fever→Doctor→Medical Shop→Medicine
  Q30  Pulp/Print/Paper/Purchase/Publish         → A  1,3,2,5,4  (production chain)
  Q31  Seed/Fruit/Plant/Food                     → C  1,3,2,4    (growth cycle)
  Q32  Wood/Book/Factory/Paper/Print             → A  1,3,4,5,2  (book-making chain)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Jumbling_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Jumbling"

QUESTIONS = [
    # ── Q27 ── CREATIVE ── (letter code type) ────────────────────────────────────
    # R=1,E=2,A=3,C=4,T=5,I=6,V=7,E=8  (E appears twice with codes 2 and 8)
    {
        "question_number": 27,
        "difficulty": "easy",
        "question_en": (
            "Letter codes: R=1, E=2, A=3, C=4, T=5, I=6, V=7, E=8. "
            "Which number permutation forms a meaningful word?"
        ),
        "question_hi": (
            "अक्षर कूट: R=1, E=2, A=3, C=4, T=5, I=6, V=7, E=8. "
            "कौन सा संख्या क्रम एक सार्थक शब्द बनाता है?"
        ),
        "option_a": "4,1,2,3,5,6,7,8",
        "option_b": "4,3,1,5,6,7,8,2",
        "option_c": "7,2,1,3,8,4,5,6",
        "option_d": "4,1,2,3,5,8,7,6",
        "correct_answer": "A",   # → C,R,E,A,T,I,V,E = CREATIVE
    },
    # ── Q28 ── Meaningful order: size/scope (small → large) ──────────────────────
    # (1)House  (2)Road  (3)Room  (4)Town  (5)District
    # Order: Room→House→Road→Town→District  →  3,1,2,4,5
    {
        "question_number": 28,
        "difficulty": "easy",
        "question_en": (
            "Arrange in meaningful order (smallest to largest): "
            "(1)House  (2)Road  (3)Room  (4)Town  (5)District"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (छोटे से बड़े): "
            "(1)House/घर  (2)Road/सड़क  (3)Room/कमरा  (4)Town/कस्बा  (5)District/जिला"
        ),
        "option_a": "3,2,1,4,5",
        "option_b": "3,1,4,2,5",
        "option_c": "3,1,2,4,5",
        "option_d": "3,1,2,5,4",
        "correct_answer": "C",   # Room → House → Road → Town → District
    },
    # ── Q29 ── Meaningful order: logical event sequence ───────────────────────────
    # Doctor, Fever, Medicine, Medical Shop
    # Order: Fever → Doctor → Medical Shop → Medicine
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": (
            "Arrange in meaningful (logical) order: "
            "Doctor, Fever, Medicine, Medical Shop"
        ),
        "question_hi": (
            "निम्नलिखित को तार्किक अर्थपूर्ण क्रम में व्यवस्थित कीजिए: "
            "डॉ., बुखार, दवाई, चिकित्सा की दुकान"
        ),
        "option_a": "Medical Shop, Medicine, Fever, Doctor",
        "option_b": "Fever, Doctor, Medical Shop, Medicine",
        "option_c": "Doctor, Medical Shop, Medicine, Fever",
        "option_d": "Medicine, Doctor, Medical Shop, Fever",
        "correct_answer": "B",   # Fever→Doctor→Medical Shop→Medicine
    },
    # ── Q30 ── Meaningful order: printing/publishing chain ────────────────────────
    # (1)Pulp  (2)Print  (3)Paper  (4)Purchase  (5)Publish
    # Order: Pulp→Paper→Print→Publish→Purchase  →  1,3,2,5,4
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "Arrange in meaningful order (production chain): "
            "(1)Pulp  (2)Print  (3)Paper  (4)Purchase  (5)Publish"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (उत्पादन श्रृंखला): "
            "(1)Pulp/लुगदी  (2)Print/छपाई  (3)Paper/कागज  (4)Purchase/खरीद  (5)Publish/प्रकाशित"
        ),
        "option_a": "1,3,2,5,4",
        "option_b": "1,4,5,2,3",
        "option_c": "1,2,3,5,4",
        "option_d": "1,5,4,2,3",
        "correct_answer": "A",   # Pulp→Paper→Print→Publish→Purchase
    },
    # ── Q31 ── Meaningful order: plant growth cycle ───────────────────────────────
    # (1)Seed  (2)Fruit  (3)Plant  (4)Food
    # Order: Seed→Plant→Fruit→Food  →  1,3,2,4
    {
        "question_number": 31,
        "difficulty": "easy",
        "question_en": (
            "Arrange in meaningful order (growth cycle): "
            "(1)Seed  (2)Fruit  (3)Plant  (4)Food"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (विकास चक्र): "
            "(1)Seed/बीज  (2)Fruit/फल  (3)Plant/पौधा  (4)Food/भोजन"
        ),
        "option_a": "2,1,4,3",
        "option_b": "1,4,2,3",
        "option_c": "1,3,2,4",
        "option_d": "3,1,2,4",
        "correct_answer": "C",   # Seed→Plant→Fruit→Food
    },
    # ── Q32 ── Meaningful order: book-making chain ────────────────────────────────
    # (1)Wood  (2)Book  (3)Factory  (4)Paper  (5)Print
    # Order: Wood→Factory→Paper→Print→Book  →  1,3,4,5,2
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": (
            "Arrange in meaningful order (book-making chain): "
            "(1)Wood  (2)Book  (3)Factory  (4)Paper  (5)Print"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (पुस्तक निर्माण श्रृंखला): "
            "(1)Wood/लकड़ी  (2)Book/किताब  (3)Factory/कारखाना  (4)Paper/कागज  (5)Print/छपाई"
        ),
        "option_a": "1,3,4,5,2",
        "option_b": "2,5,1,3,4",
        "option_c": "3,1,4,5,2",
        "option_d": "4,2,3,1,5",
        "correct_answer": "A",   # Wood→Factory→Paper→Print→Book
    },
]


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
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = SOURCE,
                **d,
            ))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
