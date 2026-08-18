"""
seed_reasoning_ranking_sheet3.py
=========================================
Seeds Ranking Q16-Q21 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Ranking
Run     : python seed_reasoning_ranking_sheet3.py

Answer key (all verified via Python):
  Q16  Kunal=7th from bottom (→29th from top); Sonali=9th; Pulkit midway;
       distance=20; Pulkit dist from each=10                               → B  10
  Q17  Richard=15th from front; behind=3×14=42; total=57;
       7th from end=51st; between Richard & 7th boy=51-15-1=35            → C  35
  Q18  40 boys; Amit=11th left; Deepak=31st right (→10th left);
       Shreya=14th left; dist Shreya-Deepak=4                             → C  4th
       NOTE: Q18 may already exist with ans=None — handle via update below
  Q19  Amisha=22nd; Sajal=27th; passed=60; failed=60/4=15; total=75       → B  75
  Q20  A=18th front; C=25th front; C midway A&B; B=32nd front; total=47  → C  47
  Q21  N=5th; T=5+6=11th; S=11+6=17th; total=17+8-1=24                   → B  24
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Ranking_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Ranking"

QUESTIONS = [
    # ── Q16 ── Kunal=29th from top; Sonali=9th; Pulkit midway; dist=10 ───────
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "In a class of 35 students, Kunal is placed seventh from the bottom "
            "whereas Sonali is placed ninth from the top. Pulkit is placed exactly "
            "in between the two. What is Kunal's position from Pulkit?"
        ),
        "question_hi": (
            "35 विद्यार्थियों की एक कक्षा में कुणाल नीचे से 7वें स्थान पर है "
            "जबकि सोनाली ऊपर से 9वें स्थान पर है। पुलकित दोनों के ठीक बीच में "
            "है, तो कुणाल की पुलकित से कितने स्थान की दूरी है?"
        ),
        "option_a": "9",
        "option_b": "10",
        "option_c": "11",
        "option_d": "13",
        "correct_answer": "B",   # Kunal_top=29; dist=20; midpoint=10
    },
    # ── Q17 ── total=57; 7th from end=51st; between=51-15-1=35 ─────────────
    {
        "question_number": 17,
        "difficulty": "hard",
        "question_en": (
            "Richard is fifteenth from the front in a column of boys. There were "
            "thrice as many behind him as there were in front. How many boys are "
            "there between Richard and the seventh boy from the end of the column?"
        ),
        "question_hi": (
            "लड़कों के एक कतार में रिचर्ड सामने से 15वाँ है। सामने की तुलना में "
            "उसके पीछे तीन गुने लड़के हैं, तो रिचर्ड और कतार के अंतिम छोर से 7वें "
            "लड़के के बीच कितने लड़के हैं?"
        ),
        "option_a": "33",
        "option_b": "34",
        "option_c": "35",
        "option_d": "Data inadequate",
        "correct_answer": "C",   # front=14; behind=42; total=57; 7th_end=51st; between=35
    },
    # ── Q18 ── Deepak=10th left; Shreya=14th left; dist=4 ───────────────────
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "Forty boys are standing in a row facing the North. Amit is eleventh "
            "from the left and Deepak is thirty-first from the right end of the row. "
            "How far will Shreya, who is third to the right of Amit in the row, "
            "be from Deepak?"
        ),
        "question_hi": (
            "चालीस लड़के एक पंक्ति में उत्तर की ओर मुँह करके खड़े हैं। अमित बाएँ "
            "से 11वाँ और दीपक दाएँ छोर से 31वाँ है। पंक्ति में अमित के दाएँ से "
            "तीसरी श्रेया, दीपक से कितनी दूर होगी?"
        ),
        "option_a": "2nd",
        "option_b": "3rd",
        "option_c": "4th",
        "option_d": "5th",
        "correct_answer": "C",   # Deepak_left=10; Shreya_left=14; dist=4
    },
    # ── Q19 ── passed=60; failed=15; total=75 ────────────────────────────────
    {
        "question_number": 19,
        "difficulty": "hard",
        "question_en": (
            "In a class, among the passed students, Amisha is twenty-second from "
            "the top and Sajal, who is 5 ranks below Amisha, is thirty-fourth from "
            "the bottom. All the students from the class have appeared for the exam. "
            "If the ratio of the students who passed in the exam to those who failed "
            "is 4:1 in that class, how many students are there in the class?"
        ),
        "question_hi": (
            "उत्तीर्ण हुए विद्यार्थियों की एक कक्षा में अमीशा शीर्ष से 22वें "
            "स्थान पर है और सजल जो अमीशा से 5 स्थान नीचे है, नीचे से 34वें "
            "स्थान पर है। सभी विद्यार्थियों ने परीक्षा दी। यदि पास होने वाले "
            "का अनुपात असफल छात्रों से 4:1 है, तो कक्षा में कितने विद्यार्थी हैं?"
        ),
        "option_a": "60",
        "option_b": "75",
        "option_c": "90",
        "option_d": "Data inadequate",
        "correct_answer": "B",   # Sajal_top=27; passed=60; failed=15; total=75
    },
    # ── Q20 ── B=32nd from front; total=32+16-1=47 ───────────────────────────
    {
        "question_number": 20,
        "difficulty": "hard",
        "question_en": (
            "In a queue, A is eighteenth from the front while B is sixteenth from "
            "the back. If C is twenty-fifth from the front and is exactly in the "
            "middle of A and B, then how many persons are there in the queue?"
        ),
        "question_hi": (
            "एक पंक्ति में A सामने से 18वाँ है जबकि B पीछे से 16वाँ है। यदि C "
            "सामने से 25वाँ है और A तथा B के ठीक बीच में है, तो पंक्ति में कितने "
            "व्यक्ति हैं?"
        ),
        "option_a": "45",
        "option_b": "46",
        "option_c": "47",
        "option_d": "48",
        "correct_answer": "C",   # dist(A,C)=7; B=32nd front; total=32+16-1=47
    },
    # ── Q21 ── T=11th; S=17th from top; total=17+8-1=24 ────────────────────
    {
        "question_number": 21,
        "difficulty": "hard",
        "question_en": (
            "N ranks fifth in a class. S is eighth from the last. If T is sixth "
            "after N and just in the middle of N and S, then how many students "
            "are there in the class?"
        ),
        "question_hi": (
            "N का स्थान कक्षा में पाँचवाँ है। S अंतिम से आठवाँ है। यदि T का "
            "स्थान N के बाद छठा है और N तथा S के ठीक बीच में है, तो कक्षा में "
            "कितने विद्यार्थी हैं?"
        ),
        "option_a": "23",
        "option_b": "24",
        "option_c": "25",
        "option_d": "26",
        "correct_answer": "B",   # T=11th; S=17th; total=17+8-1=24
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
                print(f"  SKIP  Q{d['question_number']}: already in DB (needs manual update)")
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
