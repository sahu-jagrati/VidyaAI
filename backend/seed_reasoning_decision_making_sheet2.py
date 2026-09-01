"""
seed_reasoning_decision_making_sheet2.py
==========================================
Seeds Reasoning → Decision Making  Q2, Q3, Q4, Q5.

Same direction set as Q1 (Management Trainee selection).

DIRECTIONS (Q1–5): Conditions for selecting Management Trainee:
  (i)   Graduate with at least 60% marks.
  (ii)  Age: not less than 21 and not more than 28 years as on 1-1-2010.
  (iii) Ready to pay Rs. 50,000 as security deposit.
  (iv)  At least 40% marks in selection examination.
  (v)   At least 50% marks in personal interview.

EXCEPTIONS:
  • At (i) but ≥ 65% in PG → refer to GM-Personnel.
  • At (iii) but ready to sign bond for one year → refer to ED-Personnel.

FIXED OPTIONS (A-D in DB; E injected by frontend):
  A – Data not adequate.
  B – Candidate to be selected.
  C – Candidate not to be selected.
  D – Refer to GM-Personnel.
  E – Refer to ED-Personnel.  ← injected by frontend

NOTE: image_url = None; upload images to Supabase bucket
      'question_image_Decision_Making' then run
      update_decision_making_image_urls_batch2.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q2 C  Anuj Soren — born 25 March 1984.
     Age on 1-1-2010 = 25 years → 21 ≤ 25 ≤ 28 ✓ (ii)
     Selection exam: 50% ≥ 40% ✓ (iv)
     Personal interview: 50% ≥ 50% ✓ (v)
     Security deposit: ready ✓ (iii)
     Graduation: 58% < 60% ✗ (i FAILS)
     Post-graduation: 63% < 65% → exception does NOT apply.
     All conditions not met, exception not triggered → NOT selected. → C.

Q3 A  Seema Biswas — born 15 May 1985.
     Age on 1-1-2010 = 24 years → 21 ≤ 24 ≤ 28 ✓ (ii)
     Graduation: 65% ≥ 60% ✓ (i)
     Security deposit: ready ✓ (iii)
     Selection exam: 45% ≥ 40% ✓ (iv)
     Personal interview: NOT MENTIONED → condition (v) cannot be verified.
     Data not adequate to take a decision. → A.

Q4 E  Abhinav Ghosal — born 3 December 1984.
     Age on 1-1-2010 = 25 years → 21 ≤ 25 ≤ 28 ✓ (ii)
     Graduation: 63% ≥ 60% ✓ (i)
     Personal interview: 52% ≥ 50% ✓ (v)
     Selection exam: 40% ≥ 40% ✓ (iv)
     Security deposit: can only pay Rs. 25,000 < 50,000 ✗ (iii FAILS)
     BUT: ready to sign bond for one year → EXCEPTION to (iii)
     → refer to ED-Personnel. → E.

Q5 B  Namita Jaiswal — born 12 July 1983.
     Age on 1-1-2010 = 26 years → 21 ≤ 26 ≤ 28 ✓ (ii)
     Graduation: 62% ≥ 60% ✓ (i)
     Personal interview: 52% ≥ 50% ✓ (v)
     Security deposit: ready to pay Rs. 50,000 ✓ (iii)
     Selection exam: 46% ≥ 40% ✓ (iv)
     ALL 5 conditions met → candidate to be selected. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Decision Making"

OPT_A = (
    "If the data provided are not adequate to take a decision. / "
    "यदि दिया गया डाटा निर्णय लेने के लिए पर्याप्त नहीं है।"
)
OPT_B = (
    "If the candidate is to be selected. / "
    "यदि उम्मीदवार का चयन किया जाना है।"
)
OPT_C = (
    "If the candidate is not to be selected. / "
    "यदि उम्मीदवार का चयन नहीं किया जाना है।"
)
OPT_D = (
    "If the case is to be referred to GM-Personnel. / "
    "यदि मामला जीएम-कार्मिक को भेजा जाना है।"
)
# Option E ("refer to ED-Personnel") injected by frontend — not stored in DB.

DIRECTIONS_EN = (
    "Directions (Q1–5): Following are the conditions for selecting "
    "Management Trainee in an organization:\n"
    "(i) Be a graduate with at least 60 percent marks.\n"
    "(ii) Be not less than 21 years and not more than 28 years as on 1-1-2010.\n"
    "(iii) Be ready to pay Rs. 50,000 as security deposit.\n"
    "(iv) Have secured at least 40 percent marks in the selection examination.\n"
    "(v) Have secured at least 50 percent marks in personal interview.\n\n"
    "In the case of a candidate who has satisfied all the above conditions EXCEPT —\n"
    "(a) At (i) above, but has secured at least 65% marks in postgraduation, "
    "the case is to be referred to GM-Personnel.\n"
    "(b) At (iii) above, but is ready to sign a bond for one year, "
    "the case is to be referred to ED-Personnel.\n\n"
    "All these cases are given to you as on 1-1-2010."
)

DIRECTIONS_HI = (
    "निर्देश (प्र.1–5): एक संगठन में प्रबंधन प्रशिक्षु के चयन के लिए "
    "निम्नलिखित शर्तें हैं:\n"
    "(i) कम से कम 60 प्रतिशत अंकों के साथ स्नातक होना चाहिए।\n"
    "(ii) 1-1-2010 को कम से कम 21 वर्ष और अधिक से अधिक 28 वर्ष होना चाहिए।\n"
    "(iii) 50,000 रुपये जमानत राशि के रूप में भुगतान करने के लिए तैयार रहें।\n"
    "(iv) चयन परीक्षा में कम से कम 40 प्रतिशत अंक प्राप्त किए हों।\n"
    "(v) व्यक्तिगत साक्षात्कार में कम से कम 50 प्रतिशत अंक प्राप्त किए हों।\n\n"
    "ऐसे उम्मीदवार के मामले में जिसने उपरोक्त सभी शर्तों को पूरा किया है, सिवाय—\n"
    "(a) उपरोक्त (i) लेकिन स्नातकोत्तर में कम से कम 65% अंक हासिल किए हैं, "
    "इस मामले को जीएम-कार्मिक को भेजा जाना है।\n"
    "(b) उपरोक्त (iii), लेकिन एक वर्ष के लिए बॉन्ड पर हस्ताक्षर करने के लिए "
    "तैयार है, इस मामले को ईडी-कार्मिक को भेजा जाना है।\n\n"
    "ये सभी मामले आपको 1-1-2010 तक दिए गए हैं।"
)

QUESTIONS = [

    # ── Q2 ───────────────────────────────────────────────────────────────────
    # Anuj Soren: grad 58%<60% fails (i), PG 63%<65% exception fails → NOT selected. → C.
    {
        "question_number": 2,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q2. Anuj Soren was born on 25th March 1984. He has secured 58 per cent "
            "marks in graduation and 63 percent marks in postgraduation. He has "
            "secured 50 per cent marks in both selection examination and personal "
            "interview. He is ready to pay the security deposit of Rs. 50,000."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.2. अनुज सोरेन का जन्म 25 मार्च 1984 को हुआ था। उन्होंने स्नातक में "
            "58 प्रतिशत अंक और स्नातकोत्तर में 63% अंक प्राप्त किए हैं। उन्होंने "
            "चयन परीक्षा और व्यक्तिगत साक्षात्कार दोनों में 50 प्रतिशत अंक प्राप्त "
            "किए हैं। वह 50,000 रुपये की जमानत राशि का भुगतान करने के लिए तैयार हैं।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "C",
        # Age 25 ✓ | Sel.exam 50%≥40% ✓ | Interview 50%≥50% ✓ | Deposit ✓
        # Grad 58%<60% ✗ | PG 63%<65% (exception fails) → not selected. → C.
    },

    # ── Q3 ───────────────────────────────────────────────────────────────────
    # Seema Biswas: personal interview marks NOT given → data not adequate. → A.
    {
        "question_number": 3,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q3. Seema Biswas was born on 15th May 1985. She has secured 65 per cent "
            "marks in graduation and 70 per cent marks in postgraduation. She is ready "
            "to pay Rs. 50,000 as security deposit. She has also secured 45 per cent "
            "marks in the selection examination."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.3. सीमा बिस्वास का जन्म 15 मई 1985 को हुआ था। उन्होंने स्नातक में "
            "65 प्रतिशत अंक और स्नातकोत्तर में 70 प्रतिशत अंक प्राप्त किए हैं। "
            "वह जमानत राशि के रूप में 50,000 रुपये देने को तैयार हैं। उन्होंने "
            "चयन परीक्षा में 45 प्रतिशत अंक भी हासिल किए हैं।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "A",
        # Age 24 ✓ | Grad 65%≥60% ✓ | Deposit ✓ | Sel.exam 45%≥40% ✓
        # Personal interview marks NOT GIVEN → condition (v) unverifiable → A.
    },

    # ── Q4 ───────────────────────────────────────────────────────────────────
    # Abhinav Ghosal: deposit Rs.25k<50k fails (iii), but can sign bond → ED-Personnel. → E.
    {
        "question_number": 4,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q4. Abhinav Ghosal has secured 52 per cent marks in the personal "
            "interview and 40 per cent marks in the selection examination. He can "
            "pay Rs. 25,000 as security deposit. Alternatively, he can sign a bond "
            "of one year. He was born on 3rd December 1984. He has secured 63 per "
            "cent marks in graduation."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.4. अभिनव घोषाल ने व्यक्तिगत साक्षात्कार में 52 प्रतिशत अंक और "
            "चयन परीक्षा में 40 प्रतिशत अंक प्राप्त किए हैं। वह जमानत के रूप में "
            "25,000 रुपये का भुगतान कर सकता है। वैकल्पिक रूप से, वह एक वर्ष के "
            "बॉन्ड पर हस्ताक्षर कर सकता है। उनका जन्म 3 दिसंबर 1984 को हुआ था। "
            "उन्होंने स्नातक में 63 प्रतिशत अंक प्राप्त किए हैं।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "E",
        # Age 25 ✓ | Grad 63%≥60% ✓ | Interview 52%≥50% ✓ | Sel.exam 40%≥40% ✓
        # Deposit Rs.25k<50k ✗ (iii FAILS) BUT can sign bond → exception → ED-Personnel → E.
    },

    # ── Q5 ───────────────────────────────────────────────────────────────────
    # Namita Jaiswal: all 5 conditions met → selected. → B.
    {
        "question_number": 5,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q5. Namita Jaiswal has secured 62 per cent marks in graduation and "
            "52 per cent marks in personal interview. She was born on 12th July 1983. "
            "She is ready to pay the security deposit of Rs. 50,000. She has secured "
            "46 per cent marks in the selection examination."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.5. नमिता जायसवाल ने स्नातक में 62 प्रतिशत अंक और व्यक्तिगत "
            "साक्षात्कार में 52 प्रतिशत अंक प्राप्त किए हैं। उसका जन्म 12 जुलाई "
            "1983 को हुआ था। वह 50,000 रुपये की जमानत राशि के रूप में भुगतान करने "
            "के लिए तैयार है। उसने चयन परीक्षा में 46 प्रतिशत अंक हासिल किए हैं।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "B",
        # Age 26 ✓ | Grad 62%≥60% ✓ | Interview 52%≥50% ✓ | Deposit ✓ | Sel.exam 46%≥40% ✓
        # ALL 5 conditions met → selected. → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Decision Making Q2–Q5 into '{TOPIC}' / '{SUBJECT}'")

        for d in QUESTIONS:
            qn = d["question_number"]
            exists = (
                db.query(Question)
                .filter(
                    Question.subject == SUBJECT,
                    Question.topic == TOPIC,
                    Question.question_number == qn,
                )
                .first()
            )
            if exists:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
        if inserted:
            print(
                "\n  Upload dm_2.png, dm_3.png, dm_4.png, dm_5.png "
                "to Supabase bucket 'question_image_Decision_Making', then run:\n"
                "  python update_decision_making_image_urls_batch2.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
