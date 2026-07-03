"""
seed_ratio_proportion_sheet6.py
================================
Seeds questions 37–44 (Ratio & Proportion) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Ratio & Proportion
Run     : python seed_ratio_proportion_sheet6.py

Answer key verification:
  Q37: p/q=r/s=t/u=k=5/2; ratio=k³=(5/2)³=125/8=15.625                      → D
  Q38: x/y=216/125=(6/5)³; cube-root ratio=6/5=1.2                            → C
  Q39: k²=9→k=3; k+k²+k³=3+9+27=39                                           → B
  Q40: a/b=c/d→(a+b)/(c+d)=a/c (Componendo property)                         → D
  Q41: p/q=r/s=k; ((p+r)/(q+s))²=k²=pr/qs                                    → B
  Q42: k²-k-6=0→k=3; x=3z/2,y=7z/12; (x+y+z)/z=37/12                       → B
  Q43: sum property: 1/5=2a→a=1/10                                             → B
  Q44: sum of denoms=(a+b+c)(x+y+z); each ratio=1/(a+b+c)                     → C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Ratio_Proportion_Sheet6"
SUBJECT = "Quant"
TOPIC   = "Ratio & Proportion"

QUESTIONS = [
    # Q37
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": "If p/q = r/s = t/u = 5/2, then find the value of (ap³ − br³ + ct³) / (aq³ − bs³ + cu³) = ?",
        "question_hi": "यदि p/q = r/s = t/u = 5/2 है, तो (ap³ − br³ + ct³) / (aq³ − bs³ + cu³) का मान ज्ञात कीजिए।",
        "option_a": "25",
        "option_b": "5/2",
        "option_c": "25/4",
        "option_d": "15.625",
        "correct_answer": "D",
    },
    # Q38
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": "If x/y = p/q = r/s = 216/125, then find (∛x − 2∛p + 5∛r) / (∛y − 2∛q + 5∛s) = ?",
        "question_hi": "यदि x/y = p/q = r/s = 216/125 है, तो (∛x − 2∛p + 5∛r) / (∛y − 2∛q + 5∛s) ज्ञात कीजिए।",
        "option_a": "36/25",
        "option_b": "36/125",
        "option_c": "1.2",
        "option_d": "1.3",
        "correct_answer": "C",
    },
    # Q39
    {
        "question_number": 39,
        "difficulty": "hard",
        "question_en": "If a₁/b₁ = a₂/b₂ = a₃/b₃ and (5a₁²+6a₂²+7a₃²)/(5b₁²+6b₂²+7b₃²) = 9, then a₁/b₁ + a₁a₂/(b₁b₂) + a₁a₂a₃/(b₁b₂b₃) = ?",
        "question_hi": "यदि a₁/b₁ = a₂/b₂ = a₃/b₃ और (5a₁²+6a₂²+7a₃²)/(5b₁²+6b₂²+7b₃²) = 9 है, तो a₁/b₁ + a₁a₂/(b₁b₂) + a₁a₂a₃/(b₁b₂b₃) ज्ञात कीजिए।",
        "option_a": "40",
        "option_b": "39",
        "option_c": "30",
        "option_d": "36",
        "correct_answer": "B",
    },
    # Q40
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": "If a:b = c:d, then which of the following ratios is equal to a:c?",
        "question_hi": "यदि a:b = c:d है, तो निम्नलिखित में से कौन सा अनुपात a:c के बराबर है?",
        "option_a": "a:d",
        "option_b": "b:c",
        "option_c": "a+d:b+c",
        "option_d": "a+b:c+d",
        "correct_answer": "D",
    },
    # Q41
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": "If p/q = r/s, then ((p+r)/(q+s))² = ?",
        "question_hi": "यदि p/q = r/s है, तो ((p+r)/(q+s))² ज्ञात कीजिए?",
        "option_a": "pq/rs",
        "option_b": "pr/qs",
        "option_c": "((p-r)/(r+s))²",
        "option_d": "1",
        "correct_answer": "B",
    },
    # Q42
    {
        "question_number": 42,
        "difficulty": "hard",
        "question_en": "If z/(x−2y) = (2z+x)/(2y) = 2x/z, then find the value of (x+y+z)/z = ?",
        "question_hi": "यदि z/(x−2y) = (2z+x)/(2y) = 2x/z है, तो (x+y+z)/z का मान ज्ञात कीजिए।",
        "option_a": "35/16",
        "option_b": "37/12",
        "option_c": "44/12",
        "option_d": "41/12",
        "correct_answer": "B",
    },
    # Q43
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": "Find a, if (x+y+z) ≠ 0 and x/(3x+y+z) = y/(x+3y+z) = z/(x+y+3z) = 2a?",
        "question_hi": "a ज्ञात कीजिये, यदि (x+y+z) ≠ 0 और x/(3x+y+z) = y/(x+3y+z) = z/(x+y+3z) = 2a है?",
        "option_a": "1/15",
        "option_b": "1/10",
        "option_c": "1/5",
        "option_d": "1/2",
        "correct_answer": "B",
    },
    # Q44
    {
        "question_number": 44,
        "difficulty": "hard",
        "question_en": "If x/(xa+yb+zc) = y/(ya+zb+xc) = z/(za+xb+yc) and x+y+z ≠ 0, then each ratio equals to?",
        "question_hi": "यदि x/(xa+yb+zc) = y/(ya+zb+xc) = z/(za+xb+yc) और x+y+z ≠ 0 है, तो प्रत्येक अनुपात किसके बराबर है?",
        "option_a": "-1/(a-b+c)",
        "option_b": "1/(a-b+c)",
        "option_c": "1/(a+b+c)",
        "option_d": "1/(a-b-c)",
        "correct_answer": "C",
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
            if d["question_en"][:80] in existing_short:
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
        print(f"\nDone — inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
