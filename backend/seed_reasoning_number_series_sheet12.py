"""
seed_reasoning_number_series_sheet12.py
=========================================
Seeds Number Series Q93-Q100 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet12.py

All Q93-Q100 are "Find the wrong term" type.

Answer key (verified via Python):
  Q93  5,27,61,122,213,340,509      n³−3; 27 should be 24               → A  27
  Q94  121,143,165,186,209          11×odd; 186 should be 187            → C  186
  Q95  16,22,30,45,52,66            diffs +6,+8,+10,+12,+14; 45→40      → B  45
  Q96  8,13,21,32,47,63,83          diffs +5,+8,+11,+14,+17,+20; 47→46  → D  47
  Q97  4,10,22,46,96,190,382        ×2+2; 96 should be 94               → C  96
  Q98  125,126,124,127,123,129      alt +1,−2,+3,−4,+5; 129→128        → D  129
  Q99  105,85,60,30,0,−45,−90      first term 105 should be 100          → A  105
  Q100 325,259,202,160,127,105,94  diffs from right ×11 (11,22,…66); 202→204 → C  202
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet12"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q93 ── n³−3 for n=2..8; 3³−3=24 but series shows 27 ─────────────────────
    {
        "question_number": 93,
        "difficulty": "medium",
        "question_en": "Find the wrong term in the series: 5, 27, 61, 122, 213, 340, 509",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 5, 27, 61, 122, 213, 340, 509",
        "option_a": "27",
        "option_b": "61",
        "option_c": "122",
        "option_d": "509",
        "correct_answer": "A",   # n³−3: 3³−3=24 not 27
    },
    # ── Q94 ── 11×odd numbers; 11×17=187 but series shows 186 ───────────────────
    {
        "question_number": 94,
        "difficulty": "easy",
        "question_en": "Find the wrong term in the series: 121, 143, 165, 186, 209",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 121, 143, 165, 186, 209",
        "option_a": "143",
        "option_b": "165",
        "option_c": "186",
        "option_d": "209",
        "correct_answer": "C",   # 11×17=187 not 186
    },
    # ── Q95 ── diffs +6,+8,+10,+12,+14; 30+10=40 but series shows 45 ─────────────
    {
        "question_number": 95,
        "difficulty": "easy",
        "question_en": "Find the wrong term in the series: 16, 22, 30, 45, 52, 66",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 16, 22, 30, 45, 52, 66",
        "option_a": "30",
        "option_b": "45",
        "option_c": "52",
        "option_d": "66",
        "correct_answer": "B",   # diffs +6,+8,+10,+12,+14: 30+10=40 not 45
    },
    # ── Q96 ── diffs +5,+8,+11,+14,+17,+20 (AP d=+3); 32+14=46 shows as 47 ──────
    {
        "question_number": 96,
        "difficulty": "medium",
        "question_en": "Find the wrong term in the series: 8, 13, 21, 32, 47, 63, 83",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 8, 13, 21, 32, 47, 63, 83",
        "option_a": "13",
        "option_b": "21",
        "option_c": "32",
        "option_d": "47",
        "correct_answer": "D",   # diffs +5,+8,+11,+14…: 32+14=46 not 47
    },
    # ── Q97 ── each term = prev×2+2; 46×2+2=94 but series shows 96 ───────────────
    {
        "question_number": 97,
        "difficulty": "easy",
        "question_en": "Find the wrong term in the series: 4, 10, 22, 46, 96, 190, 382",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 4, 10, 22, 46, 96, 190, 382",
        "option_a": "4",
        "option_b": "10",
        "option_c": "96",
        "option_d": "382",
        "correct_answer": "C",   # ×2+2: 46×2+2=94 not 96
    },
    # ── Q98 ── alternating +1,−2,+3,−4,+5; 123+5=128 but series shows 129 ────────
    {
        "question_number": 98,
        "difficulty": "easy",
        "question_en": "Find the wrong term in the series: 125, 126, 124, 127, 123, 129",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 125, 126, 124, 127, 123, 129",
        "option_a": "126",
        "option_b": "124",
        "option_c": "123",
        "option_d": "129",
        "correct_answer": "D",   # alt +1,−2,+3,−4,+5: 123+5=128 not 129
    },
    # ── Q99 ── first term 105 should be 100; correct diffs: −15,−25,−30,−30,−45,−45
    {
        "question_number": 99,
        "difficulty": "medium",
        "question_en": "Find the wrong term in the series: 105, 85, 60, 30, 0, -45, -90",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 105, 85, 60, 30, 0, -45, -90",
        "option_a": "105",
        "option_b": "60",
        "option_c": "0",
        "option_d": "-45",
        "correct_answer": "A",   # 105 should be 100 (diff from 100: −15,−25,−30,−30,−45,−45)
    },
    # ── Q100 ── diffs from right +11,+22,+33,+44,+55,+66; 160+44=204 shows as 202 ─
    # Correct (R→L): 94,105,127,160,204,259,325
    {
        "question_number": 100,
        "difficulty": "medium",
        "question_en": "Find the wrong term in the series: 325, 259, 202, 160, 127, 105, 94",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 325, 259, 202, 160, 127, 105, 94",
        "option_a": "94",
        "option_b": "127",
        "option_c": "202",
        "option_d": "259",
        "correct_answer": "C",   # diffs 11,22,33,44,55,66 from right: 160+44=204 not 202
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
