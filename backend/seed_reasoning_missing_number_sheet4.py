"""
seed_reasoning_missing_number_sheet4.py
=========================================
Seeds Missing Number Q30-Q40 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Missing Number
Run     : python seed_reasoning_missing_number_sheet4.py

Answer key (all verified via Python):
  Q30  four circles; TL×TR×BR=BL; 4×3×(-1)=-12                              → D  -12
  Q31  table I/II/III; C1+C2=C3, C3/6=C4; 54+?=90 → ?=36                   → A  36
  Q32  circle 6 sectors; opposite x & x³; 11³=1331                           → D  1331
  Q33  three cross figures; center=product of 4 surrounding; 10×3×3×1=90     → C  90
  Q34  3 columns; (Top×Bottom)-Bottom=Middle; (14×7)-7=91                    → B  91
  Q35  3×3 matrix; middle=first+third (row); 15+7=22                         → A  22
  Q36  3×3 matrix; (C1-C2)×2=C3; (33-19)×2=28                               → B  28
  Q37  3×3 matrix; (R1×R2)-100=R3 per col; 32×14-100=348 → ?=14             → D  14
  Q38  3×3 matrix; R1×(R2÷3)=R3 per col; ?×12=540 → ?=45                   → D  45
  Q39  3×3 matrix; (C1-C2)×2=C3; (49-5)×2=88                                → D  88
  Q40  4×4 matrix; R2+R3=R4 for col2&col3; 7+3=10                           → A  10
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Missing_Number_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Missing Number"

QUESTIONS = [
    # ── Q30 ── four circles; TL×TR×BR = BL ──────────────────────────────────
    # C1:2×2×3=12 ✓  C2:2×3×5=30 ✓  C3:5×1×(-1)=-5 ✓  C4:4×3×(-1)=-12
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "Four circles each divided into 4 quadrants (TL, TR, BL, BR): "
            "Circle1=[TL:2, TR:2, BL:12, BR:3], Circle2=[TL:2, TR:3, BL:30, BR:5], "
            "Circle3=[TL:5, TR:1, BL:-5, BR:-1], Circle4=[TL:4, TR:3, BL:?, BR:-1]. "
            "Find the missing value (pattern: TL×TR×BR = BL)."
        ),
        "question_hi": (
            "चार वृत्त, प्रत्येक चार भागों में विभाजित (ऊपर-बाएँ, ऊपर-दाएँ, नीचे-बाएँ, नीचे-दाएँ): "
            "वृत्त1=[TL:2, TR:2, BL:12, BR:3], वृत्त2=[TL:2, TR:3, BL:30, BR:5], "
            "वृत्त3=[TL:5, TR:1, BL:-5, BR:-1], वृत्त4=[TL:4, TR:3, BL:?, BR:-1]. "
            "लुप्त मान ज्ञात कीजिए (सूत्र: TL×TR×BR=BL)।"
        ),
        "option_a": "9",
        "option_b": "12",
        "option_c": "7",
        "option_d": "-12",
        "correct_answer": "D",   # 4×3×(-1)=-12
    },
    # ── Q31 ── table: C1+C2=C3, C3÷6=C4 ────────────────────────────────────
    # Row I:40+32=72, 72/6=12 ✓  Row II:30+24=54, 54/6=9 ✓  Row III:54+?=90→?=36, 90/6=15 ✓
    {
        "question_number": 31,
        "difficulty": "easy",
        "question_en": (
            "Find the missing number in the table: "
            "I: 40 32 72 12 || II: 30 24 54 9 || III: 54 ? 90 15 "
            "(pattern: C1+C2=C3, C3÷6=C4)"
        ),
        "question_hi": (
            "तालिका में लुप्त संख्या ज्ञात कीजिए: "
            "I: 40 32 72 12 || II: 30 24 54 9 || III: 54 ? 90 15 "
            "(सूत्र: C1+C2=C3, C3÷6=C4)"
        ),
        "option_a": "36",
        "option_b": "48",
        "option_c": "49",
        "option_d": "46",
        "correct_answer": "A",   # 90-54=36
    },
    # ── Q32 ── circle with 6 sectors; opposite sectors: x and x³ ─────────────
    # 4↔64(4³), 7↔343(7³), 11↔?(11³=1331)
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": (
            "A circle is divided into 6 sectors. Opposite sectors contain a number and its cube: "
            "4 and 64, 7 and 343, 11 and ?. Find the missing number."
        ),
        "question_hi": (
            "एक वृत्त 6 भागों में विभाजित है। आमने-सामने वाले भागों में एक संख्या और उसका घन होता है: "
            "4 और 64, 7 और 343, 11 और ?। लुप्त संख्या ज्ञात कीजिए।"
        ),
        "option_a": "1321",
        "option_b": "1332",
        "option_c": "1231",
        "option_d": "1331",
        "correct_answer": "D",   # 11³=1331
    },
    # ── Q33 ── three cross-shaped figures; center = product of 4 surrounding ──
    # Fig1: 3×1×4×5=60 ✓  Fig2: 7×6×1×2=84 ✓  Fig3: 10×3×3×1=90
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": (
            "Three cross-shaped figures (center = product of 4 surrounding numbers): "
            "Figure1 top=3, left=1, right=4, bottom=5, center=60. "
            "Figure2 top=7, left=6, right=1, bottom=2, center=84. "
            "Figure3 top=10, left=3, right=3, bottom=1, center=?. Find the missing center."
        ),
        "question_hi": (
            "तीन क्रॉस-आकार की आकृतियाँ (केंद्र = चारों आसपास की संख्याओं का गुणनफल): "
            "आकृति1 ऊपर=3, बाएँ=1, दाएँ=4, नीचे=5, केंद्र=60। "
            "आकृति2 ऊपर=7, बाएँ=6, दाएँ=1, नीचे=2, केंद्र=84। "
            "आकृति3 ऊपर=10, बाएँ=3, दाएँ=3, नीचे=1, केंद्र=?। लुप्त केंद्र ज्ञात कीजिए।"
        ),
        "option_a": "12",
        "option_b": "16",
        "option_c": "90",
        "option_d": "48",
        "correct_answer": "C",   # 10×3×3×1=90
    },
    # ── Q34 ── column-wise: (Top×Bottom) − Bottom = Middle ─────────────────
    # Col1:(6×8)-8=40 ✓  Col2:(21×25)-25=500 ✓  Col3:(14×7)-7=91
    {
        "question_number": 34,
        "difficulty": "easy",
        "question_en": (
            "Find the missing number. Column-wise data (top, middle, bottom): "
            "Col1: 6, 40, 8 || Col2: 21, 500, 25 || Col3: 14, ?, 7 "
            "(pattern: (Top×Bottom) - Bottom = Middle)"
        ),
        "question_hi": (
            "लुप्त संख्या ज्ञात कीजिए। स्तंभ-वार डेटा (ऊपर, मध्य, नीचे): "
            "Col1: 6, 40, 8 || Col2: 21, 500, 25 || Col3: 14, ?, 7 "
            "(सूत्र: (ऊपर×नीचे) - नीचे = मध्य)"
        ),
        "option_a": "98",
        "option_b": "91",
        "option_c": "78",
        "option_d": "84",
        "correct_answer": "B",   # (14×7)-7=98-7=91
    },
    # ── Q35 ── 3×3 matrix; middle col = first + third (row-wise) ─────────────
    # R1:7+6=13 ✓  R2:4+18=22 ✓  R3:15+7=22
    {
        "question_number": 35,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 7 13 6 || 4 22 18 || 15 ? 7",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 7 13 6 || 4 22 18 || 15 ? 7",
        "option_a": "22",
        "option_b": "24",
        "option_c": "23",
        "option_d": "21",
        "correct_answer": "A",   # 15+7=22 (middle=first+third)
    },
    # ── Q36 ── 3×3 matrix; (C1-C2)×2 = C3 per row ───────────────────────────
    # R1:(10-3)×2=14 ✓  R2:(49-15)×2=68 ✓  R3:(33-19)×2=28
    {
        "question_number": 36,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 10 3 14 || 49 15 68 || 33 19 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 10 3 14 || 49 15 68 || 33 19 ?",
        "option_a": "27",
        "option_b": "28",
        "option_c": "29",
        "option_d": "25",
        "correct_answer": "B",   # (33-19)×2=28
    },
    # ── Q37 ── 3×3 matrix; (R1×R2)-100=R3 per column ─────────────────────────
    # Col1:(21×19)-100=299 ✓  Col2:(18×22)-100=296 ✓  Col3:(32×14)-100=348
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 21 18 32 || 19 22 ? || 299 296 348",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 21 18 32 || 19 22 ? || 299 296 348",
        "option_a": "28",
        "option_b": "30",
        "option_c": "24",
        "option_d": "14",
        "correct_answer": "D",   # (32×14)-100=348 → ?=14
    },
    # ── Q38 ── 3×3 matrix; R1×(R2÷3)=R3 per column ───────────────────────────
    # Col1:42×(18/3)=252 ✓  Col2:37×(24/3)=296 ✓  Col3:?×(36/3)=540 → ?=45
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 42 37 ? || 18 24 36 || 252 296 540",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 42 37 ? || 18 24 36 || 252 296 540",
        "option_a": "50",
        "option_b": "40",
        "option_c": "55",
        "option_d": "45",
        "correct_answer": "D",   # ?×(36/3)=?×12=540 → ?=45
    },
    # ── Q39 ── 3×3 matrix; (C1-C2)×2=C3 per row ─────────────────────────────
    # R1:(15-3)×2=24 ✓  R2:(21-6)×2=30 ✓  R3:(49-5)×2=88
    {
        "question_number": 39,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 15 3 24 || 21 6 30 || 49 5 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 15 3 24 || 21 6 30 || 49 5 ?",
        "option_a": "82",
        "option_b": "92",
        "option_c": "98",
        "option_d": "88",
        "correct_answer": "D",   # (49-5)×2=88
    },
    # ── Q40 ── 4×4 matrix; R2+R3=R4 for col2 and col3 ────────────────────────
    # Col2:7+3=10 ✓  Col3:8+6=14 ✓  (missing is col2 of row4)
    # Given: Row4=[10, ?, 14, 65]; ?=R2col2+R3col2=7+3=10
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": (
            "Find the missing number in the 4×4 matrix: "
            "10 4 7 5 || 15 7 8 25 || 14 3 6 12 || 10 ? 14 65 "
            "(pattern for col2 and col3: R2+R3=R4)"
        ),
        "question_hi": (
            "4×4 आव्यूह में लुप्त संख्या ज्ञात कीजिए: "
            "10 4 7 5 || 15 7 8 25 || 14 3 6 12 || 10 ? 14 65 "
            "(col2 और col3 में सूत्र: R2+R3=R4)"
        ),
        "option_a": "10",
        "option_b": "14",
        "option_c": "18",
        "option_d": "16",
        "correct_answer": "A",   # R2+R3=R4: 7+3=10
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
