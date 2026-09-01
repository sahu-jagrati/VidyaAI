"""
seed_reasoning_decision_making_sheet3.py
==========================================
Seeds Reasoning → Decision Making  Q6.

New direction set (Q6–10) — different conditions AND different options from Q1–5.

DIRECTIONS (Q6–10): Conditions for selecting candidates for Marketing division:
  (i)   Be at least 30 years old as on 1-3-2009.
  (ii)  Have secured at least 55 per cent marks in graduation.
  (iii) Have secured at least 60 per cent marks in Post-Graduate
        Degree/Diploma in Marketing.
  (iv)  Have post-qualification work experience of at least five years
        in the Marketing Division of an organization.
  (v)   Have secured at least 45 per cent marks in the selection process.

EXCEPTIONS:
  (a) At (iv) above, but has post-qualification work experience of at least
      two years as Deputy Marketing Manager → refer to GM-Marketing.
  (b) At (ii) above, but has secured at least 65 per cent marks in
      Post-Graduate Degree/Diploma in Marketing Management → refer to
      Vice President-Marketing.

FIXED 5 OPTIONS (A-D stored in DB; E injected by frontend based on option_d):
  A – if the candidate is not to be selected.
  B – if the candidate is to be selected.
  C – if the data are inadequate to take a decision.
  D – if the case is to be referred to Vice President-Marketing.
  E – if the case is to be referred to GM-Marketing.  ← injected by frontend

NOTE: image_url = None; upload images to Supabase bucket
      'question_image_Decision_Making' then run
      update_decision_making_image_urls_batch3.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q6 B  Navin Marathe — born 8th April 1975.
     Age on 1-3-2009 = 33 years → ≥ 30 ✓ (i)
     Graduation: 60% ≥ 55% ✓ (ii)
     PG Degree in Marketing: 60% ≥ 60% ✓ (iii)
     Work experience: 6 years in Marketing Division ≥ 5 years ✓ (iv)
     Selection process: 50% ≥ 45% ✓ (v)
     ALL 5 conditions met → candidate to be selected. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Decision Making"

# Options for this direction set (Q6–10)
# NOTE: option_d = "Vice President-Marketing" — frontend uses this to detect
#       variant 2 and injects E = "GM-Marketing" automatically.
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
# Option E ("refer to GM-Marketing") injected by frontend — not stored in DB.

DIRECTIONS_EN = (
    "Directions (Q6–10): In each question below are given details of one "
    "candidate. You have to take one of the following courses of action based "
    "on the information provided and the conditions and sub-conditions given "
    "above and mark your answer accordingly. You are not to assume anything "
    "other than the information provided in each question. All these cases "
    "are given to you as on 1-3-2009.\n\n"
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
    "पर कार्यवाही करनी है और अपने जवाब के रूप में कार्यवाही के उस संख्या को "
    "चिह्नित करना होगा। आपको प्रत्येक प्रश्न में दी गई जानकारी के अलावा कुछ भी "
    "नहीं मानना है। ये सभी मामले आपको 1-3-2009 तक दिए गए हैं।\n\n"
    "चयन की शर्तें:\n"
    "(i) 1-3-2009 को कम से कम 30 वर्ष आयु हो।\n"
    "(ii) स्नातक में कम से कम 55% अंक प्राप्त किए हों।\n"
    "(iii) मार्केटिंग में स्नातकोत्तर डिग्री/डिप्लोमा में कम से कम 60% अंक प्राप्त किए हों।\n"
    "(iv) किसी संगठन के मार्केटिंग डिवीजन में कम से कम पांच साल का कार्य अनुभव हो।\n"
    "(v) चयन प्रक्रिया में कम से कम 45% अंक प्राप्त किए हों।\n\n"
    "ऐसे उम्मीदवार के मामले में जो अन्य सभी शर्तों को पूरा करता है, सिवाय—\n"
    "(a) उपरोक्त (iv), लेकिन उप-विपणन प्रबंधक के रूप में कम से कम दो साल का "
    "कार्य अनुभव है, इस मामले को जीएम-मार्केटिंग को भेजा जाना है।\n"
    "(b) उपरोक्त (ii), लेकिन मार्केटिंग मैनेजमेंट में स्नातकोत्तर डिग्री/डिप्लोमा में "
    "कम से कम 65% अंक प्राप्त किए हैं, इस मामले को वाइस प्रेसिडेंट-विपणन को "
    "भेजा जाना है।"
)

QUESTIONS = [

    # ── Q6 ───────────────────────────────────────────────────────────────────
    # Navin Marathe: all 5 conditions met → selected. → B.
    {
        "question_number": 6,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            DIRECTIONS_EN + "\n\n"
            "Q6. Navin Marathe was born on 8th April 1975. He has secured 60 per "
            "cent marks in both graduation and Post-Graduate Degree in Marketing. "
            "He has been working for the past six years in the Marketing Division "
            "of an organization after completing his PG Degree in Marketing. He has "
            "secured 50 per cent marks in the selection process."
        ),
        "question_hi": (
            DIRECTIONS_HI + "\n\n"
            "प्र.6. नवीन मराठे का जन्म 8 अप्रैल 1975 को हुआ था। उन्होंने मार्केटिंग "
            "में स्नातक और स्नातकोत्तर उपाधि दोनों में 60% अंक प्राप्त किए हैं। "
            "वे मार्केटिंग में अपनी स्नातकोत्तर पूरी करने के बाद एक संगठन के "
            "मार्केटिंग डिवीजन में पिछले छः वर्षों से काम कर रहे हैं। उन्होंने "
            "चयन प्रक्रिया में 50% अंक हासिल किए हैं।"
        ),
        "image_url": None,
        "option_a": OPT_A,
        "option_b": OPT_B,
        "option_c": OPT_C,
        "option_d": OPT_D,
        "correct_answer": "B",
        # Age 33 ≥ 30 ✓ | Grad 60% ≥ 55% ✓ | PG Marketing 60% ≥ 60% ✓
        # Exp 6 yrs ≥ 5 yrs ✓ | Selection 50% ≥ 45% ✓ → ALL met → selected → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Decision Making Q6 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload dm_6.png to Supabase bucket "
                "'question_image_Decision_Making', then run:\n"
                "  python update_decision_making_image_urls_batch3.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
