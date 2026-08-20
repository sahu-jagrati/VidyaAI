"""
seed_reasoning_cause_effect_sheet1.py
=======================================
Seeds Cause and Effect Q1-Q2 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Cause and Effect

All questions share the same 5 standard options:
  (a) Statement (A) is the cause and statement (B) is its effect.
  (b) Statement (B) is the cause and statement (A) is its effect.
  (c) Both (A) & (B) are independent causes.
  (d) Both (A) & (B) are effects of independent causes.
  (e) Both (A) & (B) are effects of a common cause.  ← stored in question body; frontend injects as option E

Answer key:
  Q1  A — A is cause (पहले/first), B is effect (बाद में/later)
           Residents reporting crime → police search & arrest criminals

  Q2  B — B is cause (पहले/first), A is effect (बाद में/later)
           Family murdered → government announces reward scheme
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cause_Effect_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Cause and Effect"

# Standard option text shared by all Cause and Effect questions
_OPT_A = (
    "If statement (A) is the cause and statement (B) is its effect. / "
    "यदि कथन (A) कारण है और कथन (B) इसका परिणाम है।"
)
_OPT_B = (
    "If statement (B) is the cause and statement (A) is its effect. / "
    "यदि कथन (B) कारण है और कथन (A) इसका परिणाम है।"
)
_OPT_C = (
    "If both the statements (A) & (B) are independent causes. / "
    "यदि दोनों कथन (A) और (B) स्वतंत्र कारण हैं।"
)
_OPT_D = (
    "If both the statements (A) & (B) are effects of independent causes. / "
    "यदि दोनों कथन (A) और (B) स्वतंत्र कारणों के परिणाम हैं।"
)
# Option (e) is injected by the frontend (CE_OPTION_E constant in TopicWise.jsx
# and DailyChallenge.jsx). Do NOT embed it in question_en / question_hi.

QUESTIONS = [
    # ── Q1 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "(A) The residents reported of increased criminal activities in the area "
            "to the local police station.\n"
            "(B) Many criminals were arrested by searching the residence of the "
            "suspected individuals.\n\n"
        ),
        "question_hi": (
            "(A) अपने इलाके में बढ़ी हुई आपराधिक गतिविधियों के बारे में निवासियों ने "
            "स्थानीय पुलिस थाने में रिपोर्ट लिखवाई।\n"
            "(B) संदिग्ध व्यक्तियों के निवास स्थान की तलाशी द्वारा बहुत-से आपराधी "
            "गिरफ्तार किए गए थे।\n\n"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Residents reporting crime (A) is the CAUSE (पहले — happened first).
        # Police searching and arresting criminals (B) is the EFFECT (बाद में — happened after).
        # A → B  ⟹  answer (a).
    },
    # ── Q2 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": (
            "(A) Government has awarded a high stake reward scheme for such persons "
            "who may provide any information about the suspect.\n"
            "(B) Four members of a family were brutally murdered by unidentified gunmen.\n\n"
        ),
        "question_hi": (
            "(A) संदिग्ध व्यक्ति के बारे में जानकारी देने वाले व्यक्ति के लिए सरकार ने "
            "बड़ी पुरस्कार योजना की घोषणा की है।\n"
            "(B) अज्ञात बंदूकधारियों ने एक परिवार के चार सदस्यों की निर्दयता से हत्या "
            "कर दी।\n\n"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # The brutal murder of four family members (B) is the CAUSE (पहले — happened first).
        # Government announcing a reward scheme (A) is the EFFECT (बाद में — happened after).
        # B → A  ⟹  answer (b).
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_number"] in existing_qnums:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}")

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
