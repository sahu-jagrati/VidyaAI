"""
seed_reasoning_decision_making_sheet4.py
==========================================
Seeds Reasoning → Decision Making  Q7, Q8, Q9, Q10.

Same direction set as Q6 (Marketing division selection, as on 1-3-2009).

DIRECTIONS (Q6–10) — same as seed_reasoning_decision_making_sheet3.py.

FIXED 5 OPTIONS (A-D in DB; E = "GM-Marketing" injected by frontend):
  A – if the candidate is not to be selected.
  B – if the candidate is to be selected.
  C – if the data are inadequate to take a decision.
  D – if the case is to be referred to Vice President-Marketing.
  E – if the case is to be referred to GM-Marketing.  ← injected by frontend

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q7 A  Divya Kohli — born 2nd April 1979.
     Age on 1-3-2009 = 29 years → < 30 ✗ (i FAILS)
     PG Diploma in Marketing: 65% ≥ 60% ✓ (iii)
     Graduation: 55% ≥ 55% ✓ (ii)
     Selection process: 50% ≥ 45% ✓ (v)
     Work experience: 5 years in Marketing Division ≥ 5 ✓ (iv)
     Condition (i) fails; no exception covers failing (i) → NOT selected. → A.

Q8 B  Suresh Mehta — born 19th May 1975.
     Age on 1-3-2009 = 33 years ≥ 30 ✓ (i)
     Graduation: 58% ≥ 55% ✓ (ii)
     PG in Marketing: 62% ≥ 60% ✓ (iii)
     Work experience: 7 years in Marketing Division ≥ 5 ✓ (iv)
     Selection process: 50% ≥ 45% ✓ (v)
     ALL 5 conditions met → candidate to be selected. → B.

Q9 E  Varun Malhotra — born 3rd July 1976.
     Age on 1-3-2009 = 32 years ≥ 30 ✓ (i)
     PG Degree in Marketing: 65% ≥ 60% ✓ (iii)
     Graduation: 55% ≥ 55% ✓ (ii)
     Selection process: 55% ≥ 45% ✓ (v)
     Work experience: 3 years as Deputy Marketing Manager < 5 years ✗ (iv FAILS)
     BUT: 3 years as Deputy Marketing Manager ≥ 2 years → exception (a)
     → refer to GM-Marketing. → E.

Q10 D  Sudha Gopalan — born 14th October 1978.
      Age on 1-3-2009 = 30 years ≥ 30 ✓ (i)
      PG Diploma in Marketing: 70% ≥ 60% ✓ (iii)
      Work experience: 6 years in Marketing Division ≥ 5 ✓ (iv)
      Selection process: 50% ≥ 45% ✓ (v)
      Graduation: 50% < 55% ✗ (ii FAILS)
      BUT: PG Marketing 70% ≥ 65% → exception (b)
      → refer to Vice President-Marketing. → D.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Decision Making"

OPT_A = (
    "if the candidate is not to be selected. / "
    "यदि उम्मीदवार का चयन नहीं किया जाना है।"
)
OPT_B = (
    "if the candidate is to be selected. / "
    "यदि उम्मीदवार का चयन किया जाना है।"
)
OPT_C = (
    "if the data are inadequate to take a decision. / "
    "यदि डेटा निर्णय लेने के लिए अपर्याप्त हैं।"
)
OPT_D = (
    "if the case is to be referred to Vice President-Marketing. / "
    "यदि मामला वाइस प्रेसिडेंट-विपणन को भेजा जाना है।"
)
# Option E ("GM-Marketing") injected by frontend — not stored in DB.

DIRECTIONS_EN = (
    "Directions (Q6–10): In each question below are given details of one "
    "candidate. You have to take one of the following courses of action based "
    "on the information provided and the conditions and sub-conditions given "
    "above and mark your answer accordingly. All these cases are given to you "
    "as on 1-3-2009.\n\n"
    "Conditions for selecting candidates:\n"
    "(i) Be at least 30 years old as on 1-3-2009.\n"
    "(ii) Have secured at least 55 per cent marks in graduation.\n"
    "(iii) Have secured at least 60 per cent marks in Post-Graduate "
    "Degree/Diploma in Marketing.\n"
    "(iv) Have post-qualification work experience of at least five years "
    "in the Marketing Division of an organization.\n"
    "(v) Have secured at least 45 per cent marks in the selection process.\n\n"
    "In the case of a candidate who satisfies all other conditions EXCEPT —\n"
    "(a) At (iv) above, but has post-qualification work experience of at least "
    "two years as Deputy Marketing Manager, the case is to be referred to "
    "GM-Marketing.\n"
    "(b) At (ii) above, but has secured at least 65 per cent marks in "
    "Post-Graduate Degree/Diploma in Marketing Management, the case is to be "
    "referred to Vice President-Marketing."
)

DIRECTIONS_HI = (
    "निर्देश (प्र.6–10): नीचे दिए गए प्रत्येक प्रश्न में एक उम्मीदवार का विवरण "
    "दिया गया है। आपको दी गई जानकारी और ऊपर दी गई शर्तों और उप-शर्तों के आधार "
    "पर कार्यवाही करनी है। ये सभी मामले आपको 1-3-2009 तक दिए गए हैं।\n\n"
    "चयन की शर्तें:\n"
    "(i) 1-3-2009 को कम से कम 30 वर्ष आयु हो।\n"
    "(ii) स्नातक में कम से कम 55% अंक प्राप्त किए हों।\n"
    "(iii) मार्केटिंग में स्नातकोत्तर डिग्री/डिप्लोमा में कम से कम 60% अंक प्राप्त किए हों।\n"
    "(iv) किसी संगठन के मार्केटिंग डिवीजन में कम से कम पांच साल का कार्य अनुभव हो।\n"
    "(v) चयन प्रक्रिया में कम से कम 45% अंक प्राप्त किए हों।\n\n"
    "ऐसे उम्मीदवार के मामले में जो अन्य सभी शर्तों को पूरा करता है, सिवाय—\n"
    "(a) उपरोक्त (iv), लेकिन उप-विपणन प्रबंधक के रूप में कम से कम दो साल का "
    "अनुभव है → जीएम-मार्केटिंग को भेजा जाना है।\n"
    "(b) उपरोक्त (ii), लेकिन मार्केटिंग मैनेजमेंट में PG में कम से कम 65% → "
    "वाइस प्रेसिडेंट-विपणन को भेजा जाना है।"
)

QUESTIONS = [

    # ── Q7 ───────────────────────────────────────────────────────────────────
    # Divya Kohli: age 29 < 30 (i fails), no exception for (i) → not selected. → A.
    {
        "question_number": 7,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q7. Divya Kohli has been working for the past five years in the "
            "Marketing Division of an organization after completing her "
            "Post-Graduate Diploma in Marketing with 65 per cent marks. She has "
            "secured 55 per cent marks in graduation and 50 per cent marks in "
            "the selection process. She was born on 2nd April 1979."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.7. दिव्या कोहली 65% अंकों के साथ मार्केटिंग में स्नातकोत्तर "
            "डिप्लोमा पूरी करने के बाद एक संगठन के मार्केटिंग डिवीजन में पिछले "
            "पांच वर्षों से काम कर रही हैं। उसने स्नातक में 55% अंक और चयन "
            "प्रक्रिया में 50 प्रतिशत अंक प्राप्त किए हैं। उनका जन्म 2 अप्रैल "
            "1979 को हुआ था।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "A",
        # Age 29 < 30 ✗ (i FAILS) | PG 65% ✓ | Grad 55% ✓ | Sel 50% ✓ | Exp 5yr ✓
        # No exception covers condition (i) failing → not selected. → A.
    },

    # ── Q8 ───────────────────────────────────────────────────────────────────
    # Suresh Mehta: all 5 conditions met → selected. → B.
    {
        "question_number": 8,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q8. Suresh Mehta has secured 58 per cent marks in graduation. He was "
            "born on 19th May 1975. He has secured 50 per cent marks in the "
            "selection process. He has been working for the past seven years in the "
            "Marketing Division of an organization after completing his Post "
            "Graduation with 62 per cent marks."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.8. सुरेश मेहता ने स्नातक में 58% अंक प्राप्त किए हैं। उनका जन्म "
            "19 मई 1975 को हुआ था। उन्होंने चयन प्रक्रिया में 50 प्रतिशत अंक "
            "प्राप्त किए। वह 62% अंकों के साथ मार्केटिंग में स्नातकोत्तर पूरी "
            "करने के बाद एक संगठन के मार्केटिंग डिवीजन में पिछले सात वर्षों से "
            "काम कर रहा है।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "B",
        # Age 33 ✓ | Grad 58% ✓ | PG Marketing 62% ✓ | Exp 7yr ✓ | Sel 50% ✓
        # ALL 5 conditions met → selected. → B.
    },

    # ── Q9 ───────────────────────────────────────────────────────────────────
    # Varun Malhotra: 3yr as Deputy MM < 5yr (iv fails), but 3yr ≥ 2yr → GM-Marketing. → E.
    {
        "question_number": 9,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q9. Varun Malhotra was born on 3rd July 1976. He has been working as "
            "Deputy Marketing Manager in an organization for the past three years "
            "after completing his Post Graduate Degree in Marketing with 65 per cent "
            "marks. He secured 55 per cent marks in both graduation and selection "
            "process."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.9. वरुण मल्होत्रा का जन्म 3 जुलाई 1976 को हुआ था। वह 65% अंकों "
            "के साथ मार्केटिंग में स्नातकोत्तर डिग्री पूरी करने के बाद पिछले तीन "
            "वर्षों से एक संगठन में डिप्टी मार्केटिंग मैनेजर के रूप में काम कर "
            "रहे हैं। उन्होंने स्नातक और चयन प्रक्रिया दोनों में 55% अंक हासिल "
            "किए।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "E",
        # Age 32 ✓ | PG 65% ✓ | Grad 55% ✓ | Sel 55% ✓
        # Exp: 3yr as Deputy MM < 5yr ✗ (iv FAILS)
        # BUT 3yr ≥ 2yr as Deputy MM → exception (a) → GM-Marketing → E.
    },

    # ── Q10 ──────────────────────────────────────────────────────────────────
    # Sudha Gopalan: grad 50% < 55% (ii fails), PG 70% ≥ 65% → VP-Marketing. → D.
    {
        "question_number": 10,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q10. Sudha Gopalan has secured 50 per cent marks in both selection "
            "process and graduation. She has been working for the past six years in "
            "the Marketing Division of an organization after completing her "
            "Post-Graduate Diploma in Marketing with 70 per cent marks. She was "
            "born on 14th October 1978."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.10. सुधा गोपालन ने चयन प्रक्रिया और स्नातक दोनों में 50% अंक "
            "प्राप्त किए हैं। वह 70% अंकों के साथ मार्केटिंग में स्नातकोत्तर "
            "डिप्लोमा पूरी करने के बाद एक संगठन के मार्केटिंग डिवीजन में पिछले "
            "छः वर्षों से काम कर रही हैं। उनका जन्म 14 अक्टूबर 1978 को हुआ था।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "D",
        # Age 30 ✓ | PG 70% ✓ | Exp 6yr ✓ | Sel 50% ✓
        # Grad 50% < 55% ✗ (ii FAILS)
        # BUT PG Marketing 70% ≥ 65% → exception (b) → VP-Marketing → D.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Decision Making Q7–Q10 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload dm_7.png, dm_8.png, dm_9.png, dm_10.png "
                "to Supabase bucket 'question_image_Decision_Making', then run:\n"
                "  python update_decision_making_image_urls_batch4.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
