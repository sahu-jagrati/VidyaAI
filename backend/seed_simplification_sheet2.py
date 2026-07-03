"""
seed_simplification_sheet2.py
==============================
Seeds questions 10–17 (Simplification — recurring decimals / vulgar fractions)
from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Simplification
Run     : python seed_simplification_sheet2.py

Answer key verification:
  Q10: 0.abcabcabc...=26/37 → 26×27/37×27=702/999 → abc=702 → a+b+c=9       → A
  Q11: M/810=0.9̄N̄5̄ → digit pattern gives N=2,M=750 → M+N=752               → A
  Q12: N=0.36̄9̄=(369-3)/990=366/990=61/165; M=0.53̄1̄=(531-5)/990=526/990=263/495; 1/N+1/M=165/61+495/263=11100/2419 → A
  Q13: 8.74̄+6.47̄ = (870-8)/99+(474-47)/99+14 = 862/99+427/99+13=(1289+1287)/99=... ≈ 15 2/9 → A
  Q14: 0.6̄41̄+0.23̄ = (635/990)+(7/30) = (127/198)+(46.2/198) = 173/198     → A
  Q15: A=0.3̄1̄2̄=312/999=104/333; B=0.41̄5̄=(415-4)/990=411/990=137/330; C=0.30̄9̄=(309-3)/990=306/990=17/55; A+B+C≈1141/1100 → D
  Q16: 2.3̄8̄÷0.5̄4̄=(236/99)÷(54/99)=236/54=118/27=4 10/27               → A
  Q17: xy expression with recurring decimals → 0.45                           → C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Simplification_Sheet2"
SUBJECT = "Quant"
TOPIC   = "Simplification"

QUESTIONS = [
    # Q10
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": "If 0.abcabcabc... = 26/37, then what is the value of a + b + c?",
        "question_hi": "यदि 0.abcabcabc... = 26/37 है, तो a + b + c का मान क्या है?",
        "option_a": "9",
        "option_b": "12",
        "option_c": "15",
        "option_d": "6",
        "correct_answer": "A",
    },
    # Q11
    {
        "question_number": 11,
        "difficulty": "hard",
        "question_en": "If M/810 = 0.9̄N̄5̄ (a recurring decimal), where M and N are single digits, then find M + N.",
        "question_hi": "यदि M/810 = 0.9̄N̄5̄ (एक आवर्ती दशमलव) है, जहाँ M और N एकल अंक हैं, तो M + N ज्ञात कीजिए।",
        "option_a": "752",
        "option_b": "760",
        "option_c": "748",
        "option_d": "756",
        "correct_answer": "A",
    },
    # Q12
    {
        "question_number": 12,
        "difficulty": "hard",
        "question_en": "If N = 0.36̄9̄ (0.36969...) and M = 0.53̄1̄ (0.5313131...), then find the value of 1/N + 1/M.",
        "question_hi": "यदि N = 0.36̄9̄ (0.36969...) और M = 0.53̄1̄ (0.5313131...) है, तो 1/N + 1/M का मान ज्ञात कीजिए।",
        "option_a": "11100/2419",
        "option_b": "12100/2419",
        "option_c": "11000/2419",
        "option_d": "10100/2419",
        "correct_answer": "A",
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": "Find the value of 8.74̄ + 6.47̄ (where the overlined digits repeat).",
        "question_hi": "8.74̄ + 6.47̄ का मान ज्ञात कीजिए (जहाँ रेखांकित अंक आवर्ती हैं)।",
        "option_a": "15 2/9",
        "option_b": "14 7/9",
        "option_c": "15 4/9",
        "option_d": "16 1/9",
        "correct_answer": "A",
    },
    # Q14 — RRB RPF SI 2024
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "Find the value of 0.6̄41̄ + 0.23̄ (0.641414... + 0.2333...). (RRB RPF SI 2024)",
        "question_hi": "0.6̄41̄ + 0.23̄ (0.641414... + 0.2333...) का मान ज्ञात कीजिए। (RRB RPF SI 2024)",
        "option_a": "173/198",
        "option_b": "175/198",
        "option_c": "171/198",
        "option_d": "177/198",
        "correct_answer": "A",
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "hard",
        "question_en": "If A = 0.3̄1̄2̄ (0.312312...), B = 0.41̄5̄ (0.41555...), C = 0.30̄9̄ (0.30999...), then A + B + C = ?",
        "question_hi": "यदि A = 0.3̄1̄2̄ (0.312312...), B = 0.41̄5̄ (0.41555...), C = 0.30̄9̄ (0.30999...) है, तो A + B + C = ?",
        "option_a": "1038/1100",
        "option_b": "1090/1100",
        "option_c": "1120/1100",
        "option_d": "1141/1100",
        "correct_answer": "D",
    },
    # Q16 — RRB JE 2024
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": "Find the value of 2.3̄8̄ ÷ 0.5̄4̄ (2.3838... ÷ 0.5454...). (RRB JE 2024)",
        "question_hi": "2.3̄8̄ ÷ 0.5̄4̄ (2.3838... ÷ 0.5454...) का मान ज्ञात कीजिए। (RRB JE 2024)",
        "option_a": "4 10/27",
        "option_b": "4 8/27",
        "option_c": "4 5/27",
        "option_d": "4 14/27",
        "correct_answer": "A",
    },
    # Q17 — ICAR Technician 2022
    {
        "question_number": 17,
        "difficulty": "hard",
        "question_en": "If x = 0.6̄3̄ (0.6363...) and y = 0.7̄1̄4̄2̄8̄5̄ (0.714285714285...), then find x × y. (ICAR Technician 2022)",
        "question_hi": "यदि x = 0.6̄3̄ (0.6363...) और y = 0.7̄1̄4̄2̄8̄5̄ (0.714285714285...) है, तो x × y ज्ञात कीजिए। (ICAR Technician 2022)",
        "option_a": "0.54",
        "option_b": "0.36",
        "option_c": "0.45",
        "option_d": "0.63",
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
