"""
seed_reasoning_ranking_sheet7.py
=========================================
Seeds Ranking Q43-Q50 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Ranking
Run     : python seed_reasoning_ranking_sheet7.py

Answer key (all verified via Python):
  Q43  C>A>D>B; B scored least runs                                    → B  B
  Q44  Heavier=more valuable; order Yogesh>Naresh>Ram>Ramesh>Mohan;
       most valuable = Yogesh                                           → C  Yogesh
  Q45  Raju=10th top, Ravi=21st bottom, 3 between;
       non-overlap=10+21+3=34; overlap=26; only 34 in options          → A  34
  Q46  T>R>Q>P (1st→last); 2nd = R                                     → C  R
  Q47  D>C>B>E>A (oldest→youngest); oldest = D                         → C  D
  Q48  Walk order front→back: Mother>Son>Daughter>Father; back=Father  → B  Father
  Q49  Arun=17th in class of 31; from end=31-17+1=15                  → B  15
  Q50  Flying order front→back: SmallPigeon>Crow>Pigeon>BigCrow>Eagle;
       back = Eagle (option_c says 'Earth' in PDF — typo for Eagle)    → C  Eagle
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Ranking_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Ranking"

QUESTIONS = [
    # ── Q43 ── C>A>D>B; B scored least ───────────────────────────────────────
    {
        "question_number": 43,
        "difficulty": "easy",
        "question_en": (
            "A scored more runs than B but less than C. D scored more runs "
            "than B but less than A. Who scored the least runs?"
        ),
        "question_hi": (
            "A ने B से अधिक रन बनाए लेकिन C से कम। D ने B से अधिक रन बनाए "
            "लेकिन A से कम। सबसे कम रन किसने बनाए?"
        ),
        "option_a": "A",
        "option_b": "B",
        "option_c": "C",
        "option_d": "D",
        "correct_answer": "B",   # C>A>D>B; B=least
    },
    # ── Q44 ── Yogesh>Naresh>Ram>Ramesh>Mohan; most valuable=Yogesh ──────────
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": (
            "Heavier coins are worth more. Ram's coin is heavier than Mohan's "
            "coin and more valuable than Ramesh's coin. Naresh's coin is more "
            "valuable than Ram's coin but lighter than Yogesh's. Ramesh's coin "
            "is more expensive than Mohan's coin. So who has the most valuable coin?"
        ),
        "question_hi": (
            "अधिक भारी सिक्के अधिक मूल्य के होते हैं। राम का सिक्का, मोहन के "
            "सिक्के से भारी और रमेश के सिक्के से अधिक मूल्यवान है। नरेश का "
            "सिक्का राम के सिक्के से अधिक मूल्यवान लेकिन योगेश के सिक्के से "
            "हल्का है। रमेश का सिक्का, मोहन के सिक्के से महँगा है तो सबसे "
            "मूल्यवान सिक्का किसके पास है?"
        ),
        "option_a": "Ram/राम",
        "option_b": "Ramesh/रमेश",
        "option_c": "Yogesh/योगेश",
        "option_d": "Naresh/नरेश",
        "correct_answer": "C",   # Yogesh>Naresh>Ram>Ramesh>Mohan; most valuable=Yogesh
    },
    # ── Q45 ── non-overlap total=10+21+3=34 (only option in list) ────────────
    {
        "question_number": 45,
        "difficulty": "hard",
        "question_en": (
            "Raju is 10th from the top and Ravi is 21st from the bottom. "
            "There are 3 students between them. How many students are there "
            "in the class?"
        ),
        "question_hi": (
            "राजू ऊपर से 10वें स्थान पर है और रवि नीचे से 21वें स्थान पर है। "
            "उनके बीच में 3 छात्र हैं। कक्षा में कुल कितने छात्र हैं?"
        ),
        "option_a": "34",
        "option_b": "33",
        "option_c": "31",
        "option_d": "32",
        "correct_answer": "A",   # non-overlap=10+21+3=34; overlap=26 (not in options)
    },
    # ── Q46 ── T>R>Q>P (1st→last); 2nd=R ────────────────────────────────────
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": (
            "P, Q, R and T appeared in an examination. In the results, 'P' was "
            "immediately behind 'Q', but there was no one after 'P'. 'R' was "
            "ahead of 'Q', but could not score as many marks as 'T'. Who will "
            "be second?"
        ),
        "question_hi": (
            "P, Q, R और T एक परीक्षा में बैठे। परिणामों में 'Q' के तत्काल पीछे 'P' "
            "था, किन्तु 'P' के बाद कोई नहीं था। 'R', 'Q' से आगे था, किन्तु उतने "
            "अंक प्राप्त नहीं कर पाया जितने 'T' ने किए। दूसरे नम्बर पर कौन होगा?"
        ),
        "option_a": "P",
        "option_b": "Q",
        "option_c": "R",
        "option_d": "T",
        "correct_answer": "C",   # T>R>Q>P (1st→last); 2nd=R
    },
    # ── Q47 ── D>C>B>E>A (oldest→youngest); oldest=D ─────────────────────────
    {
        "question_number": 47,
        "difficulty": "medium",
        "question_en": (
            "B is older than A but younger than C. E is younger than B but "
            "older than A. If C is younger than D, then who is the oldest?"
        ),
        "question_hi": (
            "B, A से बड़ा है परंतु C से छोटा है। E, D से छोटा है परंतु A से बड़ा "
            "है। यदि C, D से छोटा है तो आयु में सबसे बड़ा कौन है?"
        ),
        "option_a": "A",
        "option_b": "B",
        "option_c": "D",
        "option_d": "E",
        "correct_answer": "C",   # D>C>B>E>A; oldest=D (stored as option_c)
    },
    # ── Q48 ── Walk order front→back: Mother>Son>Daughter>Father ─────────────
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": (
            "A family went out for a walk. The daughter walked ahead of her "
            "father. The son was walking behind his mother and ahead of his "
            "father. Who was at the back?"
        ),
        "question_hi": (
            "एक परिवार घूमने निकला। पुत्री अपने पिता से आगे चली। पुत्र अपनी "
            "माता से पीछे चल रहा था और पिता से आगे सबसे पीछे कौन था?"
        ),
        "option_a": "Son/पुत्र",
        "option_b": "Father/पिता",
        "option_c": "Mother/माता",
        "option_d": "Daughter/पुत्री",
        "correct_answer": "B",   # Mother>Son>Daughter>Father (front→back); back=Father
    },
    # ── Q49 ── pos_from_end = 31-17+1 = 15 ──────────────────────────────────
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": (
            "Arun ranks 17th in a class of 31 students. What is his position "
            "from the end?"
        ),
        "question_hi": (
            "31 विद्यार्थियों की एक कक्षा में अरुण का स्थान 17वाँ है। अंत से "
            "उसका स्थान कौन-सा है?"
        ),
        "option_a": "14",
        "option_b": "15",
        "option_c": "16",
        "option_d": "17",
        "correct_answer": "B",   # 31-17+1=15
    },
    # ── Q50 ── Flying order front→back: SmallPigeon>Crow>Pigeon>BigCrow>Eagle ─
    # NOTE: PDF option_c has typo "Earth" instead of "Eagle/गरुड़"; stored correctly
    {
        "question_number": 50,
        "difficulty": "hard",
        "question_en": (
            "Five birds, a crow, a pigeon, a small pigeon, a big crow and an "
            "eagle fly one after the other from a tree branch. The big crow "
            "flies after the crow but is ahead of the eagle. The pigeon is "
            "between the crow and the big crow. The small pigeon is ahead of "
            "the crow. Which bird is at the back?"
        ),
        "question_hi": (
            "पाँच पक्षी कौआ, कबूतर, छोटा कबूतर, बड़ा कौआ और गरुड़ एक पेड़ "
            "की डाली से एक के बाद एक उड़ते हैं। बड़ा कौआ, कौए के बाद उड़ता है "
            "मगर गरुड़ से आगे है। कबूतर कौए और बड़े कौए के बीच में है। छोटा "
            "कबूतर कौए के आगे है। सबसे पीछे कौन-सा पक्षी है?"
        ),
        "option_a": "Pigeon/कबूतर",
        "option_b": "Big crow/बड़ा कौआ",
        "option_c": "Eagle/गरुड़",      # PDF has typo "Earth"; corrected to Eagle
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "C",   # SmallPigeon>Crow>Pigeon>BigCrow>Eagle; back=Eagle
    },
]

# Fix map for any pre-existing records (ans=None) skipped by deduplication
_FIXES = {
    43: ("B", {"option_a": "A", "option_b": "B", "option_c": "C", "option_d": "D"}),
    44: ("C", {
        "option_a": "Ram/राम",
        "option_b": "Ramesh/रमेश",
        "option_c": "Yogesh/योगेश",
        "option_d": "Naresh/नरेश",
    }),
    45: ("A", {"option_a": "34", "option_b": "33", "option_c": "31", "option_d": "32"}),
    46: ("C", {"option_a": "P", "option_b": "Q", "option_c": "R", "option_d": "T"}),
    47: ("C", {"option_a": "A", "option_b": "B", "option_c": "D", "option_d": "E"}),
    48: ("B", {
        "option_a": "Son/पुत्र",
        "option_b": "Father/पिता",
        "option_c": "Mother/माता",
        "option_d": "Daughter/पुत्री",
    }),
    49: ("B", {"option_a": "14", "option_b": "15", "option_c": "16", "option_d": "17"}),
    50: ("C", {
        "option_a": "Pigeon/कबूतर",
        "option_b": "Big crow/बड़ा कौआ",
        "option_c": "Eagle/गरुड़",
        "option_d": "None of these/इनमें से कोई नहीं",
    }),
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

        # ── Fix any pre-existing records that were skipped ────────────────────
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
                print(f"  UPDATE Q{qnum}: correct_answer={ans}, options cleaned")

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
