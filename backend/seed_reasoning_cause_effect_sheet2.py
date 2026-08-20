"""
seed_reasoning_cause_effect_sheet2.py
=======================================
Seeds Cause and Effect Q3-Q10 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Cause and Effect

All questions share the same 5 standard options (a)-(e).
Options (a)-(d) are stored in DB columns; option (e) is injected by the
frontend via CE_OPTION_E constant in TopicWise.jsx / DailyChallenge.jsx.

Answer key:
  Q3  A — Stone pelting (A) caused wounded people hospitalised (B).
           A=पहले (cause), B=बाद में (effect).

  Q4  D — People leaving city AND tourists gathering are effects of
           independent causes (different drivers during summer).

  Q5  E — Schools declared holiday AND colleges declared holiday are both
           effects of a common cause: the major festival.

  Q6  A — Student enrollment (A) → school authority cancelled tour (B).
           Overwhelming enrollment prompted the cancellation.

  Q7  D — Fruit prices dropped AND foodgrain prices rose are independent
           market-driven phenomena with different causes.

  Q8  E — Road traffic AND rail traffic disrupted between the same two towns
           since the same week → both are effects of a single common cause
           (e.g., floods, landslide, political unrest).

  Q9  A — Heavy rain forecast (A=पहले) → cricket tournament cancelled (B=बाद में).
           A=cause, B=effect.

  Q10 B — Bumper Kharif crops for two seasons (B=cause) →
           Government decides to distribute surplus foodgrain via PDS (A=effect).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cause_Effect_Sheet2"
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
    # ── Q3 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": (
            "(A) There have been sporadic events of stone pelting throughout the day "
            "in the affected areas of the city.\n"
            "(B) Many wounded people were brought to the nearby hospitals from the "
            "affected areas of the city."
        ),
        "question_hi": (
            "(A) दिनभर शहर के प्रभावित क्षेत्रों में पथराव की छुटपुट घटनाएँ हुई हैं।\n"
            "(B) शहर के प्रभावित क्षेत्रों से बहुत-से घायल लोगों को पास के अस्पतालों "
            "में लाया गया था।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Stone pelting (A) = पहले / cause → wounded people hospitalised (B) = बाद में / effect.
    },
    # ── Q4 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "(A) Many people left from the city for their native places during the "
            "summer months.\n"
            "(B) Many tourists gathered in the city during summer months."
        ),
        "question_hi": (
            "(A) गर्मी के महीनों में बहुत-से लोग अपने मूल निवास स्थान जाने के लिए "
            "शहर से गए।\n"
            "(B) गर्मी के महीनों में बहुत-से पर्यटक शहर में एकत्रित हुए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # A (residents leaving) and B (tourists arriving) are contradictory, driven by
        # different independent reasons during summer → effects of independent causes.
    },
    # ── Q5 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": (
            "(A) All the schools declared holiday on the next day of the major festival.\n"
            "(B) All the colleges declared holiday on the next day of the major festival."
        ),
        "question_hi": (
            "(A) प्रमुख त्यौहार के अगले दिन सभी स्कूलों ने छुट्टी की घोषणा की।\n"
            "(B) प्रमुख त्यौहार के अगले दिन सभी कॉलेजों ने छुट्टी की घोषणा की।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "E",
        # Both A and B are effects of the same common cause: the major festival.
        # Option E = "Both are effects of a common cause" is injected by the frontend.
    },
    # ── Q6 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            "(A) Most of the students enrolled themselves for educational tour "
            "scheduled for next month.\n"
            "(B) The school authority cancelled the educational tour scheduled for "
            "next month."
        ),
        "question_hi": (
            "(A) अधिकांश छात्रों ने अगले महीने जाने वाले शैक्षणिक दौरे में शामिल होने "
            "के लिए अपने नाम लिखवाएं।\n"
            "(B) स्कूल अधिकारियों ने अगले महीने जाने वाले शैक्षणिक दौरे को रद्द कर "
            "दिया।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Students enrolling in large numbers (A) → school authority decides to cancel
        # due to logistics/safety/capacity concerns (B). A is cause, B is effect.
    },
    # ── Q7 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": (
            "(A) The prices of fruits have dropped substantially during the last "
            "few days.\n"
            "(B) The prices of foodgrains have increased substantially during the "
            "last few days."
        ),
        "question_hi": (
            "(A) पिछले कुछ दिनों के दौरान फलों की कीमतों में काफी ज्यादा कमी हुई है।\n"
            "(B) पिछले कुछ दिनों के दौरान खाद्यान्न की कीमतों में काफी ज्यादा वृद्धि "
            "हुई है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # Fruit prices ↓ and foodgrain prices ↑ move in opposite directions due to
        # completely different market forces → effects of independent causes.
    },
    # ── Q8 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": (
            "(A) The road traffic between the two towns in the state has been "
            "disrupted since last week.\n"
            "(B) The rail traffic between the two towns in the state has been "
            "disrupted since last week."
        ),
        "question_hi": (
            "(A) राज्य के दो नगरों के बीच सड़क यातायात पिछले सप्ताह से बाधित रहा है।\n"
            "(B) राज्य के दो नगरों के बीच रेल यातायात पिछले सप्ताह से बाधित रहा है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "E",
        # Both road AND rail traffic disrupted between the same two towns since the
        # same time last week → a single common cause (flood, landslide, unrest, etc.)
        # disrupted all transport simultaneously. Option E injected by frontend.
    },
    # ── Q9 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": (
            "(A) Heavy rain has been expected in urban areas during the next 48 hours.\n"
            "(B) The weekly inter-club cricket tournament has been cancelled."
        ),
        "question_hi": (
            "(A) अगले 48 घंटों के दौरान शहरी इलाकों में भारी बारिश की आशंका जताई "
            "गई है।\n"
            "(B) सप्ताह में होने वाला इंटर-क्लब क्रिकेट टूर्नामेंट रद्द कर दिया गया है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Heavy rain forecast (A) = पहले / cause →
        # Cricket tournament cancelled (B) = बाद में / effect.
    },
    # ── Q10 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": (
            "(A) Government has decided to distribute part of the foodgrain stock "
            "through Public Distribution System to people below poverty line.\n"
            "(B) There has been bumper Kharif crops for the last two seasons."
        ),
        "question_hi": (
            "(A) सरकार ने गरीबी रेखा से नीचे के लोगों को खाद्यान्न के कुछ भंडार का "
            "वितरण सार्वजनिक वितरण प्रणाली के जरिए करने का निर्णय लिया है।\n"
            "(B) पिछले दो मौसमों में खरीफ की बंपर फसल हुई है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # Bumper Kharif crops for two seasons (B) → surplus foodgrain stock →
        # Government decides to distribute surplus through PDS (A).
        # B is cause (पहले), A is effect (बाद में).
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
