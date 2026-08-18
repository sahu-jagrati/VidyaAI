"""
seed_reasoning_missing_number_sheet3.py
=========================================
Seeds Missing Number Q20-Q29 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Missing Number
Run     : python seed_reasoning_missing_number_sheet3.py

Answer key (all verified via Python):
  Q20  two crossed-oval figures; outer sum=center; 54-36=18               → D  18
  Q21  circle center=8; clockwise ×8+1; 137×8+1=1097                     → B  1097
  Q22  7 5 3 || 8 4 9 || 2 8 ? || 112 160 162; product top3=bottom; ?=6  → B  6
  Q23  three 2×2 boxes; TL×TR×BL=BR; 6×5×0=0                             → D  0
  Q24  2 4 2 || ... || 8 64 ?; col3=√col2; √64=8                         → B  8
  Q25  three circles, counter-clockwise digit reading → center; Fig3=5634 → A  5634
  Q26  I:25 15 40 8 || II:65 25 90 ? || III:45 15 60 12; (C1+C2)/5=C4   → D  18
  Q27  two triangles; center=sum of √sides; √121+√81+√100=30              → B  30
  Q28  18 21 24 || 3 9 3 || 6 4 8 || 21 26 ?; R4=R1+|R2-R3|; 24+5=29   → B  29
  Q29  three circles; (sum outer)×7=center; (1+5+7+3+4+2)×7=154          → A  154
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Missing_Number_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Missing Number"

QUESTIONS = [
    # ── Q20 ── center = sum of 4 outer numbers (two crossed-oval figures) ────
    # Fig1: 14+12+7+3=36 ✓  Fig2: 9+11+16+?=54 → ?=18
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": (
            "Two figures: Figure 1 has outer numbers 14, 12, 7, 3 and center=36. "
            "Figure 2 has outer numbers 9, 11, 16, ? and center=54. Find the missing number."
        ),
        "question_hi": (
            "दो आकृतियाँ: आकृति 1 में बाहरी संख्याएँ 14, 12, 7, 3 हैं और केंद्र=36। "
            "आकृति 2 में बाहरी संख्याएँ 9, 11, 16, ? हैं और केंद्र=54। लुप्त संख्या ज्ञात कीजिए।"
        ),
        "option_a": "16",
        "option_b": "12",
        "option_c": "17",
        "option_d": "18",
        "correct_answer": "D",   # 54-(9+11+16)=18
    },
    # ── Q21 ── circular; clockwise starting from 2: ×center(8)+1 ─────────────
    # 2→17→137→1097 (each term = prev×8+1)
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            "In a circular diagram, center=8. Outer numbers clockwise: 2, 17, 137, ?. "
            "Find the missing number."
        ),
        "question_hi": (
            "वृत्ताकार आरेख में केंद्र=8। बाहरी संख्याएँ दक्षिणावर्त: 2, 17, 137, ?। "
            "लुप्त संख्या ज्ञात कीजिए।"
        ),
        "option_a": "907",
        "option_b": "1097",
        "option_c": "97",
        "option_d": "9107",
        "correct_answer": "B",   # 137×8+1=1097
    },
    # ── Q22 ── product of top 3 numbers in each column = bottom number ────────
    # C1:7×8×2=112 ✓  C2:5×4×8=160 ✓  C3:3×9×?=162 → ?=6
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 7 5 3 || 8 4 9 || 2 8 ? || 112 160 162",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 7 5 3 || 8 4 9 || 2 8 ? || 112 160 162",
        "option_a": "8",
        "option_b": "6",
        "option_c": "12",
        "option_d": "4",
        "correct_answer": "B",   # 162/(3×9)=6
    },
    # ── Q23 ── three 2×2 boxes; TL×TR×BL = BR ────────────────────────────────
    # Box1: 3×2×4=24 ✓  Box2: 2×(−1)×(−2)=4 ✓  Box3: 6×5×0=0
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "Three 2x2 boxes: Box1=[3,2; 4,24], Box2=[2,-1; -2,4], Box3=[6,5; 0,?]. "
            "Find the missing number (pattern: top-left × top-right × bottom-left = bottom-right)."
        ),
        "question_hi": (
            "तीन 2×2 बक्से: Box1=[3,2; 4,24], Box2=[2,-1; -2,4], Box3=[6,5; 0,?]। "
            "लुप्त संख्या ज्ञात कीजिए।"
        ),
        "option_a": "11",
        "option_b": "30",
        "option_c": "1",
        "option_d": "0",
        "correct_answer": "D",   # 6×5×0=0
    },
    # ── Q24 ── Col2=Col1²; Col3=√Col2=Col1 ──────────────────────────────────
    # Row4: Col1=8, Col2=64, Col3=√64=8
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 2 4 2 || 3 9 3 || 4 16 4 || 8 64 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 2 4 2 || 3 9 3 || 4 16 4 || 8 64 ?",
        "option_a": "24",
        "option_b": "8",
        "option_c": "16",
        "option_d": "9",
        "correct_answer": "B",   # col3=√col2: √64=8
    },
    # ── Q25 ── three circles; reading outer digits counter-clockwise → center ─
    # {3,4,5,6} permutation; Fig3: 5(TR)→6(TL)→3(B)→4(R)=5634
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": (
            "Three circular figures: Figure1 center=6543, Figure2 center=3456. "
            "Reading outer digits {3,4,5,6} counter-clockwise gives the center number. "
            "Find the center of Figure3."
        ),
        "question_hi": (
            "तीन वृत्ताकार आकृतियाँ: आकृति1 केंद्र=6543, आकृति2 केंद्र=3456। "
            "बाहरी अंकों {3,4,5,6} को वामावर्त पढ़ने से केंद्र संख्या मिलती है। "
            "आकृति3 का केंद्र ज्ञात कीजिए।"
        ),
        "option_a": "5634",
        "option_b": "5364",
        "option_c": "6543",
        "option_d": "3564",
        "correct_answer": "A",   # counter-clockwise: 5,6,3,4 → 5634
    },
    # ── Q26 ── (Col1 + Col2) / 5 = Col4 ─────────────────────────────────────
    # Row I:(25+15)/5=8 ✓  Row III:(45+15)/5=12 ✓  Row II:(65+25)/5=18
    {
        "question_number": 26,
        "difficulty": "easy",
        "question_en": (
            "Find the missing number in the table: "
            "I: 25 15 40 8 || II: 65 25 90 ? || III: 45 15 60 12"
        ),
        "question_hi": (
            "तालिका में लुप्त संख्या ज्ञात कीजिए: "
            "I: 25 15 40 8 || II: 65 25 90 ? || III: 45 15 60 12"
        ),
        "option_a": "24",
        "option_b": "12",
        "option_c": "6",
        "option_d": "18",
        "correct_answer": "D",   # (65+25)/5=18
    },
    # ── Q27 ── two triangles; center = sum of √(three outer values) ───────────
    # T1:√64+√36+√49=8+6+7=21 ✓  T2:√121+√81+√100=11+9+10=30
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "Two triangles: Triangle1 has outer values 64, 36, 49 and center=21. "
            "Triangle2 has outer values 121, 81, 100 and center=?. Find the missing center."
        ),
        "question_hi": (
            "दो त्रिभुज: त्रिभुज1 में बाहरी मान 64, 36, 49 हैं और केंद्र=21। "
            "त्रिभुज2 में बाहरी मान 121, 81, 100 हैं और केंद्र=?। लुप्त केंद्र मान ज्ञात कीजिए।"
        ),
        "option_a": "10",
        "option_b": "30",
        "option_c": "41",
        "option_d": "20",
        "correct_answer": "B",   # √121+√81+√100=11+9+10=30
    },
    # ── Q28 ── Row4 = Row1 + |Row2 − Row3| per column ────────────────────────
    # C1:18+|3-6|=21 ✓  C2:21+|9-4|=26 ✓  C3:24+|3-8|=29
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 18 21 24 || 3 9 3 || 6 4 8 || 21 26 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 18 21 24 || 3 9 3 || 6 4 8 || 21 26 ?",
        "option_a": "24",
        "option_b": "29",
        "option_c": "27",
        "option_d": "22",
        "correct_answer": "B",   # R4=R1+|R2-R3|: 24+|3-8|=24+5=29
    },
    # ── Q29 ── three circles; (sum of outer numbers) × 7 = center ────────────
    # Fig1:(6+4+3+1+0+5)×7=133 ✓  Fig2:(2+5+3+4+6+8)×7=196 ✓
    # Fig3:(1+5+7+3+4+2)×7=22×7=154
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": (
            "Three circular figures: Figure1 outer=[6,4,3,1,0,5] center=133, "
            "Figure2 outer=[2,5,3,4,6,8] center=196, "
            "Figure3 outer=[1,5,7,3,4,2] center=?. Find the missing center."
        ),
        "question_hi": (
            "तीन वृत्ताकार आकृतियाँ: आकृति1 बाहर=[6,4,3,1,0,5] केंद्र=133, "
            "आकृति2 बाहर=[2,5,3,4,6,8] केंद्र=196, "
            "आकृति3 बाहर=[1,5,7,3,4,2] केंद्र=?। लुप्त केंद्र मान ज्ञात कीजिए।"
        ),
        "option_a": "154",
        "option_b": "535",
        "option_c": "451",
        "option_d": "702",
        "correct_answer": "A",   # (1+5+7+3+4+2)×7=22×7=154
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
