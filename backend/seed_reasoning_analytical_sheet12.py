"""
seed_reasoning_analytical_sheet12.py
=========================================
Seeds Analytical Reasoning Q56-Q60 from Gagan Pratap Reasoning PDFs (Sheet 12).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet12.py

All Q56-Q60 are "Cause and Effect" relationship type questions.

Standard options (same across all questions):
  (a) 'A' is the effect and 'B' is its immediate and principal cause
  (b) 'A' is the immediate and principal cause and 'B' is its effect
  (c) 'A' is an effect but 'B' is not its immediate and principal cause
  (d) 'B' is an effect but 'A' is not its immediate and principal cause

Answer key (solutions verified):
  Q56  Event A: India won the world cup cricket in 1983 despite being underdogs.
       Event B: Kapil Dev and Roger Binny played very well in the 1983 world cup.
       Individual brilliance (B) contributed critically to the win (A), but cricket
       is a team sport; B is a major contributor, NOT the sole immediate/principal cause.
       Answer: C  ('A' is an effect but 'B' is not its immediate and principal cause)

  Q57  Event A: Monica Lewinsky is said to have illicit relations with the US President.
       Event B: A lot of journalists are reporting interviews of Monica Lewinsky and
       giving her media attention.
       The high-profile affair allegation (A) directly caused the media frenzy (B).
       Answer: B  ('A' is the immediate and principal cause and 'B' is its effect)

  Q58  Event A: Orissa has a lot of corruption.
       Event B: Orissa is one of the poorest states of our country.
       Corruption (A) is a major contributor to poverty (B) but poverty is also driven
       by other systemic factors (geography, infrastructure); A is not the sole
       immediate/principal cause.
       Answer: D  ('B' is an effect but 'A' is not its immediate and principal cause)

  Q59  Event A: The PM has announced that the Government will take measures to remove
       subsidies on diesel in a phased manner.
       Event B: Subsidies on diesel result in a lot of loss of revenue to the Government.
       Revenue loss from subsidies (B) is the primary driver behind the decision to
       phase them out (A). B → A.
       Answer: A  ('A' is the effect and 'B' is its immediate and principal cause)

  Q60  Event A: Uttarkashi is very prone to earthquakes.
       Event B: According to seismologists, there is a lot of tectonic activity going
       on in the belt below Uttarkashi.
       Tectonic activity (B) directly explains and causes the region's earthquake
       vulnerability (A). B → A.
       Answer: A  ('A' is the effect and 'B' is its immediate and principal cause)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet12"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

_OPT_A = ("If 'A' is the effect and 'B' is its immediate and principal cause / "
           "यदि 'A' एक प्रभाव है और 'B' इसका तात्कालिक और मुख्य कारण है")
_OPT_B = ("If 'A' is the immediate and principal cause and 'B' is its effect / "
           "यदि 'A' तात्कालिक और मुख्य कारण है और 'B' इसका प्रभाव है")
_OPT_C = ("If 'A' is an effect but 'B' is not its immediate and principal cause / "
           "यदि 'A' एक प्रभाव है लेकिन 'B' इसका तात्कालिक और मुख्य कारण नहीं है")
_OPT_D = ("If 'B' is an effect but 'A' is not its immediate and principal cause / "
           "यदि 'B' एक प्रभाव है लेकिन 'A' इसका तात्कालिक और मुख्य कारण नहीं है")

_INSTRUCTION = (
    "Given below are pairs of events 'A' and 'B'. You have to read both the events "
    "'A' and 'B' and decide their nature of relationship. You have to assume that "
    "the information given in 'A' and 'B' is true and you will not assume anything "
    "beyond the given information in deciding the answer."
)
_INSTRUCTION_HI = (
    "नीचे घटनाओं 'A' और 'B' के जोड़े दिए गए हैं। आपको दोनों घटनाओं 'A' और 'B' को "
    "पढ़ना होगा और उनके रिश्ते की प्रकृति का फैसला करना होगा। आपको यह मानना होगा "
    "कि 'A' और 'B' में दी गई जानकारी सत्य है और उत्तर तय करने में आप दी गई "
    "जानकारी से परे कुछ भी नहीं मानेंगे।"
)

QUESTIONS = [
    # ── Q56 ── C: A is an effect but B is not its immediate/principal cause ────
    {
        "question_number": 56,
        "difficulty": "medium",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: India won the world cup cricket in 1983 despite being the "
            "underdogs.\n"
            "Event B: Kapil Dev and Roger Binny played very well in the 1983 "
            "world cup."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: भारत ने 1983 में अंडरडॉग होने के बावजूद विश्व कप क्रिकेट जीता।\n"
            "घटना B: 1983 विश्व कप में कपिल देव और रोजर बिन्नी ने बहुत अच्छा खेला।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # India winning (A) is an effect of the team's combined effort, but Kapil Dev
        # and Binny's individual performances (B) alone are NOT the immediate and
        # principal cause — cricket is a team sport requiring collective performance ✓
    },
    # ── Q57 ── B: A is cause; B is effect (Monica Lewinsky media attention) ───
    {
        "question_number": 57,
        "difficulty": "easy",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: Monica Lewinsky is said to have had illicit relations with the "
            "US President.\n"
            "Event B: A lot of journalists are reporting interviews of Monica Lewinsky "
            "and giving her media attention."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: मोनिका लेविंस्की के अमेरिकी राष्ट्रपति के साथ अनैतिक संबंध "
            "होने की बात कही जाती है।\n"
            "घटना B: बहुत सारे पत्रकार मोनिका लेविंस्की के साक्षात्कार की रिपोर्ट "
            "कर रहे हैं और उन्हें मीडिया का ध्यान दे रहे हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # The high-profile affair allegation (A) directly triggered the media frenzy (B)
        # → A is the immediate and principal cause; B is its effect ✓
    },
    # ── Q58 ── D: B is an effect; A is not its immediate/principal cause ───────
    {
        "question_number": 58,
        "difficulty": "hard",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: Orissa has a lot of corruption.\n"
            "Event B: Orissa is one of the poorest states of our country."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: उड़ीसा में भ्रष्टाचार का बोलबाला है।\n"
            "घटना B: उड़ीसा हमारे देश के सबसे गरीब राज्यों में से एक है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # Poverty (B) is an effect; corruption (A) is a major contributing factor
        # but NOT the sole immediate/principal cause — poverty also stems from
        # geography, infrastructure gaps, and other systemic factors ✓
    },
    # ── Q59 ── A: B is cause; A is effect (diesel subsidy removal) ────────────
    {
        "question_number": 59,
        "difficulty": "easy",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: The PM has announced that the Government will take measures to "
            "remove subsidies on diesel in a phased manner.\n"
            "Event B: Subsidies on diesel result in a lot of loss of revenue to the "
            "Government."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: प्रधानमंत्री ने घोषणा की है कि सरकार चरणबद्ध तरीके से डीजल "
            "पर सब्सिडी हटाने के उपाय करेगी।\n"
            "घटना B: डीजल पर सब्सिडी से सरकार के राजस्व का काफी नुकसान होता है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Revenue loss from diesel subsidies (B) is the primary driver behind the
        # PM's decision to remove them (A) → B is the cause; A is the effect ✓
    },
    # ── Q60 ── A: B is cause; A is effect (Uttarkashi earthquakes) ────────────
    {
        "question_number": 60,
        "difficulty": "easy",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: Uttarkashi is very prone to earthquakes.\n"
            "Event B: According to seismologists, there is a lot of tectonic activity "
            "going on in the belt below Uttarkashi."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: उत्तरकाशी भूकंप के लिहाज से बेहद संवेदनशील है।\n"
            "घटना B: भूकंप विशेषज्ञों का कहना है कि उत्तरकाशी के नीचे बेल्ट में "
            "काफी टेक्टोनिक हलचल हो रही है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Tectonic activity below Uttarkashi (B) directly explains and causes the
        # region's high earthquake vulnerability (A) → B is the cause; A is the effect ✓
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
