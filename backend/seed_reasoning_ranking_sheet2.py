"""
seed_reasoning_ranking_sheet2.py
=========================================
Seeds Ranking Q8-Q15 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Ranking
Run     : python seed_reasoning_ranking_sheet2.py

Answer key (all verified via Python):
  Q8   Manoj 7th, Sachin 11th in class 31; ranks from bottom:
       Manoj=31-7+1=25, Sachin=31-11+1=21 → None of these           → D  25th and 21st
  Q9   Ravi 7 ahead of Sumit; Sumit 17th from last in 39;
       Sumit_start=23; Ravi=23-7=16                                   → C  16th
  Q10  Bharati 8 ahead of Divya (26th) in class 42;
       Bharati_top=18; from_bottom=42-18+1=25                         → C  25th
  Q11  A: 13th from left, 11th from right; D: 17th from right;
       total=23; D from left=23-17+1=7                                → B  7th
  Q12  Rajan 6th from left, Vinay 10th from right, 8 between;
       total=6+8+10=24                                                 → B  24
  Q13  A: 15th left, B: 4th right, 3 between; C just left of A;
       total=22; C from left=14; C from right=22-14+1=9               → A  9th
  Q14  Rohit 17th from left, Karan 17th from right, total=29;
       sum=34>29; between=34-29-2=3                                    → A  3
  Q15  P: 13th from left; Q: 9th from right; R: 4th left of Q;
       R_right=13; R_left=28; between P&R=28-13-1=14                  → C  14
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Ranking_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Ranking"

QUESTIONS = [
    # ── Q8 ── Rank from bottom = Total - Rank from top + 1 ──────────────────
    # Manoj: 31-7+1=25th; Sachin: 31-11+1=21st → None of options a/b/c → D
    # (original option d was "None of these"; storing actual values as option_d)
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": (
            "Manoj and Sachin are ranked seventh and eleventh respectively from "
            "the top in a class of 31 students. What will be their respective "
            "ranks from the bottom in the class?"
        ),
        "question_hi": (
            "मनोज और सचिन 31 छात्रों की एक कक्षा में शीर्ष से 7वें और 11वें "
            "स्थान पर हैं, तो कक्षा में अंतिम से उनके संबंधित स्थान क्या होंगे?"
        ),
        "option_a": "20th and 24th",
        "option_b": "24th and 20th",
        "option_c": "26th and 22nd",
        "option_d": "25th and 21st",
        "correct_answer": "D",   # 31-7+1=25, 31-11+1=21 (original: None of these)
    },
    # ── Q9 ── Sumit from start=39-17+1=23; Ravi=23-7=16 ─────────────────────
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": (
            "Ravi is 7 ranks ahead of Sumit in a class of 39. If Sumit's rank "
            "is seventeenth from the last, what is Ravi's rank from the start?"
        ),
        "question_hi": (
            "रवि 39 बच्चों की एक कक्षा में सुमित से 7 स्थान आगे है। यदि "
            "सुमित की कक्षा में अंतिम से 17वाँ स्थान है, तो शुरुआत से रवि का "
            "स्थान क्या है?"
        ),
        "option_a": "14th",
        "option_b": "15th",
        "option_c": "16th",
        "option_d": "17th",
        "correct_answer": "C",   # Sumit_start=39-17+1=23; Ravi=23-7=16
    },
    # ── Q10 ── Bharati_top=26-8=18; from_bottom=42-18+1=25 ──────────────────
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": (
            "Bharati is 8 ranks ahead of Divya who ranks twenty-sixth in a "
            "class of 42. What is Bharati's rank from the last?"
        ),
        "question_hi": (
            "42 बच्चों की एक कक्षा में भारती, दिव्या से 8 स्थान आगे है जो "
            "कक्षा में 26वीं है। भारती का कक्षा में अंतिम से क्या स्थान है?"
        ),
        "option_a": "9th",
        "option_b": "24th",
        "option_c": "25th",
        "option_d": "34th",
        "correct_answer": "C",   # Bharati_top=18; from_bottom=42-18+1=25
    },
    # ── Q11 ── total=13+11-1=23; D from left=23-17+1=7 ──────────────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": (
            "In a row of boys, A is thirteenth from the left and D is seventeenth "
            "from the right. If in this row A is eleventh from the right, then "
            "what is the position of D from the left?"
        ),
        "question_hi": (
            "लड़कों की एक पंक्ति में A बाएँ से 13वाँ है और D दाएँ से 17वाँ "
            "है। यदि इस पंक्ति में A दाएँ से 11वाँ है, तो D बाएँ से किस "
            "स्थान पर है?"
        ),
        "option_a": "6th",
        "option_b": "7th",
        "option_c": "10th",
        "option_d": "12th",
        "correct_answer": "B",   # total=13+11-1=23; D from left=23-17+1=7
    },
    # ── Q12 ── total = Rajan's pos + boys between + Vinay's pos = 6+8+10=24 ──
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": (
            "Rajan is sixth from the left end and Vinay is tenth from the right "
            "end in a row of boys. If there are eight boys between Rajan and "
            "Vinay, how many boys are there in the row?"
        ),
        "question_hi": (
            "लड़कों की एक पंक्ति में राजन बाएँ छोर से 6वाँ है और विनय दाएँ "
            "छोर से 10वाँ है। यदि राजन और विनय के बीच 8 लड़के हैं, तो पंक्ति "
            "में कितने लड़के हैं?"
        ),
        "option_a": "23",
        "option_b": "24",
        "option_c": "25",
        "option_d": "26",
        "correct_answer": "B",   # 6+8+10=24
    },
    # ── Q13 ── total=22; C_left=14; C from right=22-14+1=9 ──────────────────
    # A: 15th left, B: 4th right, 3 boys between → total=15+3+4=22
    # C just left of A → C_left=14; C_right=22-14+1=9
    {
        "question_number": 13,
        "difficulty": "hard",
        "question_en": (
            "In a row of boys, A is fifteenth from the left and B is fourth from "
            "the right. There are three boys between A and B. C is just left of A. "
            "What is C's position from the right?"
        ),
        "question_hi": (
            "लड़कों की एक पंक्ति में A बाएँ से 15वाँ है और B दाएँ से चौथा "
            "है। A और B के बीच में तीन लड़के हैं। C, A के ठीक बाएँ है, तो "
            "दाएँ से C का कौनसा स्थान है?"
        ),
        "option_a": "9th",
        "option_b": "10th",
        "option_c": "12th",
        "option_d": "13th",
        "correct_answer": "A",   # total=22; C from right=22-14+1=9
    },
    # ── Q14 ── sum=17+17=34>29; boys between=34-29-2=3 ──────────────────────
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "Rohit is seventeenth from the left end of a row of 29 boys and "
            "Karan is seventeenth from the right end in the same row. "
            "How many boys are there between them in the row?"
        ),
        "question_hi": (
            "29 लड़कों की एक ही पंक्ति में रोहित बाएँ छोर से 17वाँ है और "
            "करण दाएँ छोर से 17वाँ है। तो दोनों पंक्ति में उनके बीच कितने "
            "लड़के हैं?"
        ),
        "option_a": "3",
        "option_b": "5",
        "option_c": "6",
        "option_d": "Data inadequate",
        "correct_answer": "A",   # sum=34>29; between=34-29-2=3
    },
    # ── Q15 ── R_right=9+4=13; R_left=40-13+1=28; between P&R=28-13-1=14 ────
    {
        "question_number": 15,
        "difficulty": "hard",
        "question_en": (
            "In a row of forty children, P is thirteenth from the left end and "
            "Q is ninth from the right end. How many children are there between "
            "P and R if R is fourth to the left of Q?"
        ),
        "question_hi": (
            "चालीस बच्चों की एक पंक्ति में P बाएँ छोर से 13वाँ है और Q दाएँ "
            "छोर से 9वाँ है। यदि R, Q के बाएँ से चौथा है, तो P और R के बीच "
            "कितने बच्चे हैं?"
        ),
        "option_a": "12",
        "option_b": "13",
        "option_c": "14",
        "option_d": "15",
        "correct_answer": "C",   # R_right=13; R_left=28; between=28-13-1=14
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
