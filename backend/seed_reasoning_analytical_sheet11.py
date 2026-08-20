"""
seed_reasoning_analytical_sheet11.py
=========================================
Seeds Analytical Reasoning Q51-Q55 from Gagan Pratap Reasoning PDFs (Sheet 11).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet11.py

Q51-Q55 are "Cause and Effect" relationship type questions.
You read two events A and B and decide their causal relationship.

Standard options for this question type:
  (a) 'A' is the effect and 'B' is its immediate and principal cause
  (b) 'A' is the immediate and principal cause and 'B' is its effect
  (c) 'A' is not an immediate and principal cause of 'B', but both are
      independent effects of some common cause
  (d) 'B' is an effect but 'A' is not its immediate and principal cause

Answer key (solutions verified):
  Q51  Event A: The US crushed Iraq in the gulf war.
       Event B: The US had almost total international support in the gulf war.
       B → A: International support (B) directly enabled the military victory (A).
       Answer: A  ('A' is the effect and 'B' is its immediate and principal cause)

  Q52  Event A: India's proposal to delink social issues (labour) from trade
       issues was turned down at the WTO meet.
       Event B: Indian proposal would have hurt the interests of the developed nations.
       B → A: Threat to developed nations' interests (B) caused the proposal
       to be rejected (A).
       Answer: A  ('A' is the effect and 'B' is its immediate and principal cause)

  Q53  Event A: XYZ co. has benefited immensely by the Finance ministry's
       decision to free naphtha from import duty.
       Event B: The turnover of XYZ co. has almost doubled in the last financial year.
       A → B: Benefit from duty-free naphtha (A) contributed directly to the
       company's doubled turnover (B).
       Answer: B  ('A' is the immediate and principal cause and 'B' is its effect)

  Q54  Event A: Modiguard brand of cosmetics does not sell much.
       Event B: Modiguard brand of cosmetics is poorly advertised.
       B → A: Poor advertising (B) directly causes low visibility and low sales (A).
       Answer: A  ('A' is the effect and 'B' is its immediate and principal cause)

  Q55  Event A: The Indian Vikas party promised to bring in a corruption-free government.
       Event B: The Indian Vikas party won the elections with a thumping margin.
       A contributed to B, but election victories depend on multiple political dynamics;
       A is not the sole immediate and principal cause.
       Answer: D  ('B' is an effect but 'A' is not its immediate and principal cause)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet11"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

# Standard cause-effect options (same across all 5 questions)
_OPT_A = ("If 'A' is the effect and 'B' is its immediate and principal cause / "
           "यदि 'A' एक प्रभाव है और 'B' इसका तात्कालिक और मुख्य कारण है")
_OPT_B = ("If 'A' is the immediate and principal cause and 'B' is its effect / "
           "यदि 'A' तात्कालिक और मुख्य कारण है और 'B' इसका प्रभाव है")
_OPT_C = ("If 'A' is not an immediate and principal cause of 'B' but they are "
           "independent effects of some common cause / "
           "यदि 'A' 'B' का तात्कालिक और मुख्य कारण नहीं है, लेकिन दोनों किसी "
           "साझा कारण के स्वतंत्र प्रभाव हैं")
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
    # ── Q51 ── A is effect; B is cause (US Gulf War) ──────────────────────────
    {
        "question_number": 51,
        "difficulty": "medium",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: The US crushed Iraq in the gulf war.\n"
            "Event B: The US had almost total international support in the gulf war."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: अमेरिका ने खाड़ी युद्ध में इराक को कुचल दिया।\n"
            "घटना B: खाड़ी युद्ध में अमेरिका को लगभग पूरा अंतर्राष्ट्रीय समर्थन मिला था।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # B (international support) directly enabled the US military victory (A)
        # → B is the immediate and principal cause; A is the effect ✓
    },
    # ── Q52 ── A is effect; B is cause (India WTO proposal) ──────────────────
    {
        "question_number": 52,
        "difficulty": "medium",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: India's proposal to delink social issues such as labour from "
            "trade issues was turned down at the WTO meet.\n"
            "Event B: Indian proposal would have hurt the interests of the developed "
            "nations."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: श्रम जैसे सामाजिक मुद्दों को व्यापार मुद्दों से अलग करने के "
            "भारत के प्रस्ताव को WTO बैठक में खारिज कर दिया गया।\n"
            "घटना B: भारतीय प्रस्ताव विकसित देशों के हितों को नुकसान पहुँचाता।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # B (threat to developed nations' interests) → proposal was rejected (A)
        # → B is the immediate and principal cause; A is the effect ✓
    },
    # ── Q53 ── A is cause; B is effect (XYZ co. naphtha duty) ────────────────
    {
        "question_number": 53,
        "difficulty": "medium",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: XYZ co. has benefited immensely by the Finance ministry's "
            "decision to free naphtha from import duty.\n"
            "Event B: The turnover of XYZ co. has almost doubled in the last "
            "financial year."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: वित्त मंत्रालय के नेफ्था को आयात शुल्क से मुक्त करने के "
            "निर्णय से XYZ कंपनी को बहुत लाभ हुआ है।\n"
            "घटना B: पिछले वित्तीय वर्ष में XYZ कंपनी का टर्नओवर लगभग दोगुना हो "
            "गया है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # A (duty-free naphtha benefit) → directly caused doubling of turnover (B)
        # → A is the immediate and principal cause; B is the effect ✓
    },
    # ── Q54 ── A is effect; B is cause (Modiguard cosmetics) ─────────────────
    {
        "question_number": 54,
        "difficulty": "easy",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: Modiguard brand of cosmetics does not sell much.\n"
            "Event B: Modiguard brand of cosmetics is poorly advertised."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: मोदीगार्ड ब्रांड के सौंदर्य प्रसाधन ज्यादा नहीं बिकते।\n"
            "घटना B: मोदीगार्ड ब्रांड के सौंदर्य प्रसाधनों का बहुत कम विज्ञापन "
            "किया जाता है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # B (poor advertising) → directly causes low visibility and low sales (A)
        # → B is the immediate and principal cause; A is the effect ✓
    },
    # ── Q55 ── B is effect; A is not the immediate cause (Indian Vikas party) ─
    {
        "question_number": 55,
        "difficulty": "hard",
        "question_en": (
            f"{_INSTRUCTION}\n\n"
            "Event A: The Indian Vikas party promised to bring in a corruption-free "
            "government.\n"
            "Event B: The Indian Vikas party won the elections with a thumping margin."
        ),
        "question_hi": (
            f"{_INSTRUCTION_HI}\n\n"
            "घटना A: भारतीय विकास पार्टी ने भ्रष्टाचार मुक्त सरकार लाने का वादा किया।\n"
            "घटना B: भारतीय विकास पार्टी ने भारी अंतर से चुनाव जीता।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # A (anti-corruption promise) contributed to B (election win), but election
        # victories depend on multiple political dynamics — A is not the sole
        # immediate and principal cause; B is an effect but with multiple causes ✓
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
