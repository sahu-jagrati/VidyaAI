"""
seed_reasoning_cause_effect_sheet3.py
=======================================
Seeds Cause and Effect Q11-Q15 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Cause and Effect

Standard 5-option format — options (a)-(d) in DB; option (e) injected by frontend
via CE_OPTION_E when option_a starts with "If statement (A)".

Answer key:
  Q11  D — Vegetable prices fell (A) and quality improved (B) are driven by
            different independent market forces → effects of independent causes.

  Q12  A — Pest damage destroyed sugarcane crop causing huge farmer loss (A=cause/कारण)
            → farmers switched to grapes cultivation (B=effect/परिणाम).

  Q13  B — Police unable to nab culprits (B=cause/पहले) → crimes against women
            increased (A=effect/बाद में).

  Q14  B — Parents' agitation against high fees last year (B=cause/पहले) → govt
            recently fixed/capped fees at lower level (A=effect/बाद में).

  Q15  B — Farmers suffering from drought, unable to feed family (B=cause/पहले)
            → PM visited drought areas and promised assistance (A=effect/बाद में).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cause_Effect_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Cause and Effect"

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
# Option E is injected by the frontend — do NOT embed in question body.

QUESTIONS = [
    # ── Q11 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": (
            "(A) The prices of vegetables have fallen considerably during the last "
            "few days.\n"
            "(B) There has been considerable improvement in the quality of vegetable "
            "products."
        ),
        "question_hi": (
            "(A) पिछले कुछ दिनों में सब्जियों के दामों में भारी कमी हुई है।\n"
            "(B) सब्जी की गुणवत्ता में काफी हद तक सुधार हुआ है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # Vegetable prices falling (A) and quality improving (B) are driven by
        # different independent market forces → effects of independent causes.
    },
    # ── Q12 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": (
            "(A) Major part of the sugarcane crop were affected by pests resulting "
            "into huge loss incurred by the farmers in the state.\n"
            "(B) The farmers in the state who were cultivating sugarcane earlier have "
            "now switched over to grapes cultivation this year."
        ),
        "question_hi": (
            "(A) गन्ने की ज्यादातर फसल कीड़ों के असर में आ गई। परिणामस्वरूप राज्य के "
            "किसानों को बहुत नुकसान हुआ।\n"
            "(B) राज्य के किसान जो पिछले साल गन्ने की खेती करते थे, इस साल उसके बदले "
            "अंगूरों की खेती करने लगे हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Pest destruction of sugarcane causing huge loss (A = कारण/cause) →
        # Farmers switch to grapes to avoid further loss (B = परिणाम/effect).
    },
    # ── Q13 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 13,
        "difficulty": "easy",
        "question_en": (
            "(A) There has been a high increase in the incidents of securities against "
            "women in the city during the past few months.\n"
            "(B) The police authority has been unable to nab the culprits who are "
            "committing crime against women."
        ),
        "question_hi": (
            "(A) पिछले कुछ महीनों के दौरान शहर में महिलाओं पर अत्याचार की घटनाएं "
            "काफी बढ़ गई हैं।\n"
            "(B) पुलिस प्राधिकरण उन दोषियों को पकड़ने में असफल रही है जो महिलाओं के "
            "खिलाफ अपराध कर रहे हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # Police failure to nab culprits (B = पहले/cause) →
        # Crimes against women emboldened and increased (A = बाद में/effect).
    },
    # ── Q14 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "(A) The Govt. has recently fixed the fees for professional courses offered "
            "by the unaided institutions which are much lower than the fees charged "
            "last year.\n"
            "(B) The parents of the aspiring students launched a severe agitation last "
            "year protesting against the high fees charged by the unaided institutions."
        ),
        "question_hi": (
            "(A) सरकार ने हाल ही में गैर-सहायता प्राप्त संस्थाओं द्वारा चलाए जाने "
            "वाले प्रोफेशनल कोर्सों की फीस तय कर दी है जो पिछले साल की फीस से काफी "
            "कम है।\n"
            "(B) आकांक्षी छात्रों के माता-पिता ने पिछले साल गैर-सहायता प्राप्त "
            "संस्थाओं द्वारा ली जाने वाली ऊंची फीस के विरोध में गंभीर आंदोलन छेड़ा था।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # Parents' agitation against high fees last year (B = पहले/cause) →
        # Govt intervened and fixed fees much lower (A = बाद में/effect).
    },
    # ── Q15 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": (
            "(A) The Prime Minister has visited the drought affected areas and promised "
            "Govt. assistance to help the farmers.\n"
            "(B) A large number of farmers in the drought affected areas have been "
            "suffering due to drought situation and are unable to feed their family."
        ),
        "question_hi": (
            "(A) प्रधानमंत्री ने सूखाग्रस्त क्षेत्रों का दौरा किया है और किसानों को "
            "सरकारी सहायता का वादा किया है।\n"
            "(B) सूखाग्रस्त क्षेत्रों के अधिकांश किसान सूखे से पीड़ित थे और अपने "
            "परिवार का पेट नहीं भर पा रहे हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # Farmers suffering from drought, unable to feed family (B = पहले/cause) →
        # PM visits drought areas and promises govt assistance (A = बाद में/effect).
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
