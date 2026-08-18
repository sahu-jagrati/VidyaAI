"""
seed_reasoning_ranking_sheet1.py
=========================================
Seeds Ranking Q1-Q7 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Ranking
Run     : python seed_reasoning_ranking_sheet1.py

Answer key (all verified via Python):
  Q1  Sam: 9th from top, 38th from bottom; 9+38-1=46                         → B  46
  Q2  Boy is 19th from both ends; 19+19-1=37                                  → B  37
  Q3  Ajay: 16th from top, 29th from bottom (passed); +6 absent +5 failed;
      passed=44, total=55                                                      → D  55
  Q4  Atul: 12th from right, 4th from left; current=15; add=28-15=13         → B  13
  Q5  Row1: Jeevan 17th from start, 11th from end → 27;
      Row2: Vikas 10th from start, 12th from end → 21; total=48
      (original option e "None of these"; 48 not in options a-c)              → D  48
  Q6  Class 60, girls=2×boys → boys=20; Kamal rank 17; 9 girls ahead;
      boys ahead=7; boys after Kamal=20-8=12                                  → C  12
  Q7  Nitin rank 18 in class 49; rank from last=49-18+1=32                   → D  32
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Ranking_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Ranking"

QUESTIONS = [
    # ── Q1 ── Total = Rank from top + Rank from bottom - 1 ──────────────────
    # 9 + 38 - 1 = 46
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "Sam ranked ninth from the top and thirty-eighth from the bottom "
            "in a class. How many students are there in the class?"
        ),
        "question_hi": (
            "सैम कक्षा में ऊपर से नौवाँ और नीचे से 38वें स्थान पर है, "
            "तो कक्षा में कुल कितने विद्यार्थी हैं?"
        ),
        "option_a": "45",
        "option_b": "46",
        "option_c": "47",
        "option_d": "48",
        "correct_answer": "B",   # 9+38-1=46
    },
    # ── Q2 ── Boy is 19th from both ends; Total = 19+19-1 = 37 ──────────────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": (
            "A class of boys stands in a single line. One boy is nineteenth "
            "in order from both the ends. How many boys are there in the class?"
        ),
        "question_hi": (
            "लड़कों का एक समूह एक ही रेखा में खड़ा होता है। एक लड़का दोनों "
            "छोर से 19वें क्रम में है, तो समूह में कितने लड़के हैं?"
        ),
        "option_a": "27",
        "option_b": "37",
        "option_c": "38",
        "option_d": "39",
        "correct_answer": "B",   # 19+19-1=37
    },
    # ── Q3 ── Passed=16+29-1=44; Total=44+6(absent)+5(failed)=55 ────────────
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": (
            "Ajay ranked sixteenth from the top and twenty-ninth from the bottom "
            "among those who passed an examination. Six boys did not participate "
            "in the competition and five failed in it. "
            "How many boys were there in the class?"
        ),
        "question_hi": (
            "पास हुए छात्रों में अजय शीर्ष से 16वें स्थान पर है और नीचे से "
            "29वें स्थान पर है। 6 लड़कों ने परीक्षा में भाग नहीं लिया और 5 "
            "इसमें असफल हुए, तो कक्षा में कुल कितने लड़के हैं?"
        ),
        "option_a": "40",
        "option_b": "50",
        "option_c": "52",
        "option_d": "55",
        "correct_answer": "D",   # passed=16+29-1=44; total=44+6+5=55
    },
    # ── Q4 ── Current line = 12+4-1=15; Boys to add = 28-15=13 ─────────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "If Atul finds that he is twelfth from the right in a line of boys "
            "and fourth from the left, how many boys should be added to the line "
            "such that there are 28 boys in the line?"
        ),
        "question_hi": (
            "यदि अतुल लड़कों को एक रेखा में अपने दाएँ से 12वाँ और बाएँ से "
            "चौथा पाता है, तो रेखा में कितने लड़कों को जोड़ा जाये कि रेखा में "
            "28 लड़के खड़े हों?"
        ),
        "option_a": "12",
        "option_b": "13",
        "option_c": "15",
        "option_d": "17",
        "correct_answer": "B",   # current=12+4-1=15; add=28-15=13
    },
    # ── Q5 ── Row1=17+11-1=27; Row2=10+12-1=21; Total=48 ────────────────────
    # NOTE: original option (e) was "None of these" (actual=48); replaced with 48 as option D
    # (original option d "Cannot be determined" dropped)
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "In a row of boys, Jeevan is seventeenth from the start and eleventh "
            "from the end. In another row of boys, Vikas is tenth from the start "
            "and twelfth from the end. How many boys are there in both the rows together?"
        ),
        "question_hi": (
            "लड़कों की एक पंक्ति में जीवन शुरुआत से 17वें और अंतिम से 11वें "
            "स्थान पर है। दूसरी पंक्ति में विकास शुरुआत से 10वें और अंतिम से "
            "12वें स्थान पर है। दोनों पंक्तियों में कुल कितने लड़के हैं?"
        ),
        "option_a": "36",
        "option_b": "37",
        "option_c": "39",
        "option_d": "48",
        "correct_answer": "D",   # row1=27, row2=21, total=48 (original: none of these)
    },
    # ── Q6 ── boys=60/3=20; boys ahead of Kamal=16-9=7; after=20-8=12 ───────
    {
        "question_number": 6,
        "difficulty": "hard",
        "question_en": (
            "In a class of 60, where girls are twice that of boys, Kamal ranked "
            "seventeenth from the top. If there are 9 girls ahead of Kamal, "
            "how many boys are after him in rank?"
        ),
        "question_hi": (
            "60 बच्चों की एक कक्षा में लड़कियाँ लड़कों से दुगुनी हैं। कमल "
            "शीर्ष से 17वें स्थान पर है। यदि कमल के आगे 9 लड़कियाँ हैं, तो "
            "श्रेणी में कितने लड़के उसके पीछे हैं?"
        ),
        "option_a": "3",
        "option_b": "7",
        "option_c": "12",
        "option_d": "23",
        "correct_answer": "C",   # boys=20; boys_ahead=7; boys_after=20-8=12
    },
    # ── Q7 ── Rank from last = Total - Rank from top + 1 = 49-18+1 = 32 ─────
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": (
            "Nitin ranks eighteenth in a class of 49 students. "
            "What is his rank from the last?"
        ),
        "question_hi": (
            "49 विद्यार्थियों की एक कक्षा में नितिन 18वें स्थान पर है, "
            "तो अंतिम से उसका स्थान क्या है?"
        ),
        "option_a": "18",
        "option_b": "19",
        "option_c": "31",
        "option_d": "32",
        "correct_answer": "D",   # 49-18+1=32
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
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
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
