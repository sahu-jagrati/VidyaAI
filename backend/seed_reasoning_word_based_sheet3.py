"""
seed_reasoning_word_based_sheet3.py
=========================================
Seeds Word-Based Q71-Q82 from Gagan Pratap Reasoning PDFs (Exercise-4).
Subject : Reasoning
Topic   : Word-Based
Run     : python seed_reasoning_word_based_sheet3.py

Directions Q71-Q80: A series is given with a missing word.
Choose the correct option that completes the series.

Answer key (from Exercise-4 published key):
  Q71  master, ember, bombay, animal, abdomen, ?   → C  crime
  Q72  Good, Odour, Urban, Anthem, ?               → B  Empathy
  Q73  Money, Amity, Camera, Animal, Telomere, ?   → A  Talisman
  Q74  bat, thin, reply, length, ?                 → B  display
  Q75  hello, lower, error, organ, anarch, ?       → D  chain
  Q76  nephew, anther, tenses, prunes, preens, ?   → D  return
  Q77  Oxygen, Toil, Arouse, Arson, Tenuous, ?     → B  Lustrous
  Q78  employ, oyster, errors, isolate, tennis, ?  → D  isomer
  Q79  Smar, Aspire, Castle, Abysmal, Accost, ?    → D  Duties
  Q80  nature, ensure, tense, spent, spurn, ?      → C  upturn
  Q81  Same-category member: Lucknow, Patna,
       Bhopal, Jaipur → State capitals of India   → D  Shimla
  Q82  Flower series: Lily, Daisy, Datura, ?
       (all white flowers)                         → C  Jasmine
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Word_Based_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Word-Based"

QUESTIONS = [
    # ── Q71 ── Series: master, ember, bombay, animal, abdomen, ? ─────────────
    {
        "question_number": 71,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "master, ember, bombay, animal, abdomen, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "master, ember, bombay, animal, abdomen, ?"
        ),
        "option_a": "money",
        "option_b": "ambush",
        "option_c": "crime",
        "option_d": "deform",
        "correct_answer": "C",
    },
    # ── Q72 ── Series: Good, Odour, Urban, Anthem, ? ─────────────────────────
    {
        "question_number": 72,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "Good, Odour, Urban, Anthem, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "Good, Odour, Urban, Anthem, ?"
        ),
        "option_a": "Anthill",
        "option_b": "Empathy",
        "option_c": "Europe",
        "option_d": "Goose",
        "correct_answer": "B",
    },
    # ── Q73 ── Series: Money, Amity, Camera, Animal, Telomere, ? ─────────────
    {
        "question_number": 73,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "Money, Amity, Camera, Animal, Telomere, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "Money, Amity, Camera, Animal, Telomere, ?"
        ),
        "option_a": "Talisman",
        "option_b": "Litmus",
        "option_c": "Matter",
        "option_d": "Shame",
        "correct_answer": "A",
    },
    # ── Q74 ── Series: bat, thin, reply, length, ? ───────────────────────────
    {
        "question_number": 74,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "bat, thin, reply, length, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "bat, thin, reply, length, ?"
        ),
        "option_a": "terror",
        "option_b": "display",
        "option_c": "dome",
        "option_d": "scolding",
        "correct_answer": "B",
    },
    # ── Q75 ── Series: hello, lower, error, organ, anarch, ? ─────────────────
    {
        "question_number": 75,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "hello, lower, error, organ, anarch, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "hello, lower, error, organ, anarch, ?"
        ),
        "option_a": "night",
        "option_b": "rapture",
        "option_c": "senile",
        "option_d": "chain",
        "correct_answer": "D",
    },
    # ── Q76 ── Series: nephew, anther, tenses, prunes, preens, ? ─────────────
    {
        "question_number": 76,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "nephew, anther, tenses, prunes, preens, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "nephew, anther, tenses, prunes, preens, ?"
        ),
        "option_a": "teen",
        "option_b": "pester",
        "option_c": "repent",
        "option_d": "return",
        "correct_answer": "D",
    },
    # ── Q77 ── Series: Oxygen, Toil, Arouse, Arson, Tenuous, ? ───────────────
    {
        "question_number": 77,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "Oxygen, Toil, Arouse, Arson, Tenuous, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "Oxygen, Toil, Arouse, Arson, Tenuous, ?"
        ),
        "option_a": "Onion",
        "option_b": "Lustrous",
        "option_c": "Lion",
        "option_d": "Onto",
        "correct_answer": "B",
    },
    # ── Q78 ── Series: employ, oyster, errors, isolate, tennis, ? ────────────
    {
        "question_number": 78,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "employ, oyster, errors, isolate, tennis, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "employ, oyster, errors, isolate, tennis, ?"
        ),
        "option_a": "neptune",
        "option_b": "nature",
        "option_c": "terminate",
        "option_d": "isomer",
        "correct_answer": "D",
    },
    # ── Q79 ── Series: Smar, Aspire, Castle, Abysmal, Accost, ? ─────────────
    {
        "question_number": 79,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "Smar, Aspire, Castle, Abysmal, Accost, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "Smar, Aspire, Castle, Abysmal, Accost, ?"
        ),
        "option_a": "Shop",
        "option_b": "Class",
        "option_c": "Showman",
        "option_d": "Duties",
        "correct_answer": "D",
    },
    # ── Q80 ── Series: nature, ensure, tense, spent, spurn, ? ────────────────
    {
        "question_number": 80,
        "difficulty": "hard",
        "question_en": (
            "Directions: A series is given, in which a word is missing. "
            "Choose the correct option that completes the series. "
            "nature, ensure, tense, spent, spurn, ?"
        ),
        "question_hi": (
            "निर्देश: एक श्रृंखला दी गई है जिसमें एक शब्द लुप्त है। "
            "सही विकल्प चुनें जो श्रृंखला को पूरा करे। "
            "nature, ensure, tense, spent, spurn, ?"
        ),
        "option_a": "pushup",
        "option_b": "thrash",
        "option_c": "upturn",
        "option_d": "asset",
        "correct_answer": "C",
    },
    # ── Q81 ── Same-category: Lucknow, Patna, Bhopal, Jaipur (state capitals) ─
    {
        "question_number": 81,
        "difficulty": "medium",
        "question_en": (
            "Which one of the given alternatives will be the other member "
            "of the group of the same category? "
            "Lucknow, Patna, Bhopal, Jaipur, ?"
        ),
        "question_hi": (
            "दिए गए विकल्पों में से कौन-सा एक ही वर्ग का दूसरा सदस्य होगा? "
            "लखनऊ, पटना, भोपाल, जयपुर, ?"
        ),
        "option_a": "Pune/पुणे",
        "option_b": "Indore/इंदौर",
        "option_c": "Masore/मैसूर",
        "option_d": "Shimla/शिमला",
        "correct_answer": "D",   # all are state capitals; Shimla = capital of HP ✓
    },
    # ── Q82 ── Flower series: Lily, Daisy, Datura (all white flowers) ─────────
    {
        "question_number": 82,
        "difficulty": "easy",
        "question_en": "Lily, Daisy, Datura, ?",
        "question_hi": "लिली, डेजी, धतूरा, ?",
        "option_a": "Sunflower/सूरजमुखी",
        "option_b": "Gudhal/गुड़हल",
        "option_c": "Jasmine/चमेली",
        "option_d": "Marigold/गेंदा",
        "correct_answer": "C",   # all white flowers; Jasmine is white ✓
    },
]

# Fix map for pre-existing records
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
