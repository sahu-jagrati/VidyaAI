"""
seed_reasoning_decision_making_sheet1.py
==========================================
Seeds Reasoning → Decision Making  Q1.

Question type: Decision Making
"In each question below details of one candidate are given. Based on the
 conditions and sub-conditions given, mark the number of the course of
 action as your answer."

DIRECTIONS (Q1–5): Conditions for selecting Management Trainee:
  (i)   Graduate with at least 60% marks.
  (ii)  Age: not less than 21 and not more than 28 years as on 1-1-2010.
  (iii) Ready to pay Rs. 50,000 as security deposit.
  (iv)  At least 40% marks in selection examination.
  (v)   At least 50% marks in personal interview.

EXCEPTIONS (same direction set):
  • At (i) above but secured ≥ 65% in postgraduation → refer to GM-Personnel.
  • At (iii) above but ready to sign bond for one year → refer to ED-Personnel.

FIXED 5 OPTIONS (same for all DM questions — A-D stored in DB, E injected
by frontend):
  A – If the data provided are not adequate to take a decision.
  B – If the candidate is to be selected.
  C – If the candidate is not to be selected.
  D – If the case is to be referred to GM-Personnel.
  E – If the case is to be referred to ED-Personnel.  ← injected by frontend

NOTE: image_url = None; upload images to Supabase bucket
      'question_image_Decision_Making' then run
      update_decision_making_image_urls_batch1.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q1 D  Sohan Awasthi — born 8 June 1987.
     Age on 1-1-2010 = 22 years → 21 ≤ 22 ≤ 28 ✓ (ii)
     Selection exam: 55% ≥ 40% ✓ (iv)
     Personal interview: 55% ≥ 50% ✓ (v)
     Security deposit: can pay Rs. 50,000 ✓ (iii)
     Graduation: 59% < 60% ✗ (i FAILS)
     Post-graduation: 68% ≥ 65% → EXCEPTION to (i): refer to GM-Personnel.
     → D.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Decision Making"

# Fixed options A-D stored in DB (option E is injected by the frontend)
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
# Option E ("refer to ED-Personnel") is injected by the frontend — not stored in DB.

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

    # ── Q1 ───────────────────────────────────────────────────────────────────
    # Sohan Awasthi: 59% grad (fails i) but 68% PG ≥ 65% → GM-Personnel. → D.
    {
        "question_number": 1,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q1. Sohan Awasthi was born on 8th June 1987. He has secured 55 percent "
            "marks in both selection examination and personal interview. He can pay "
            "the security deposit of Rs. 50,000. He has secured 68 per cent marks "
            "in post graduation and 59 per cent marks in graduation."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.1. सोहन अवस्थी का जन्म 8 जून 1987 को हुआ था। उन्होंने चयन परीक्षा "
            "और व्यक्तिगत साक्षात्कार दोनों में 55 प्रतिशत अंक प्राप्त किए हैं। "
            "वह 50,000 रुपये की जमानत राशि का भुगतान कर सकते हैं। उन्होंने "
            "स्नातकोत्तर में 68% और स्नातक में 59% अंक हासिल किए हैं।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "D",
        # Age 22 ✓ | Sel.exam 55%≥40% ✓ | Interview 55%≥50% ✓ | Deposit ✓
        # Graduation 59%<60% ✗ (fails i) BUT PG 68%≥65% → exception → GM-Personnel → D.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Decision Making Q1 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Create Supabase bucket 'question_image_Decision_Making', "
                "upload dm_1.png, then run:\n"
                "  python update_decision_making_image_urls_batch1.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
