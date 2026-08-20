"""
seed_reasoning_cause_effect_sheet4.py
=======================================
Seeds Cause and Effect Q20-Q24 from Gagan Pratap Reasoning PDFs (Sheet 4).
Subject : Reasoning
Topic   : Cause and Effect

These are SSC CGL / CHSL exam questions with a CUSTOM 4-option format:
  - Statements are labeled I and II (not (A) and (B))
  - Option texts are shuffled per-question and stored directly in DB columns
  - There is NO 5th option — option_a does NOT start with "If statement (A)",
    so the frontend will NOT inject CE_OPTION_E for these questions

Answer key:
  Q20  A — Both I (manpower layoff) and II (asset sell-off) are effects of a
            common cause: Company P's financial crisis / restructuring.
            Source: CHSL Tier-II, 07 March 2023 (Shift-1)

  Q21  A — High air pollution in the city (I = पहले/cause) →
            Respiratory & health problems increased (II = बाद में/effect).
            option (a): Event (II) is the effect and event (I) is the cause.
            Source: CHSL Tier-II, 26 June 2023 (Shift-1)

  Q22  D — Agricultural produce declining (I) and rainfall increasing (II)
            move in contradictory directions → effects of independent causes.
            Source: CHSL Tier-II, 06 March 2023 (Shift-1)

  Q23  A — Crude oil imports reduced (I) and automobile industry growth margin
            declining (II) are both effects of independent causes.
            Source: CGL Tier-II, 03 March 2023 (Shift-1)

  Q24  C — College reducing cut-off marks (I) and students union negotiating
            about canteen standards (II) are completely unrelated →
            effects of independent causes.
            Source: CGL Tier-II, 02 March 2023 (Shift-1)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cause_Effect_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Cause and Effect"

# NOTE: These questions do NOT use the standard CE option constants.
# Each question has its own shuffled option texts stored inline below.
# The frontend detects custom-format CE questions by checking whether
# option_a starts with "If statement (A)" — since these do not, CE_OPTION_E
# is NOT injected (TopicWise.jsx / DailyChallenge.jsx).

QUESTIONS = [
    # ── Q20 ───────────────────────────────────────────────────────────────────────────
    # Source: CHSL Tier-II, 07 March 2023 (Shift-1)
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": (
            "I.  Over the last two years 22% of Company P's manpower was laid off.\n"
            "II. Over the past two years Company P has sold off many of their major assets."
        ),
        "question_hi": (
            "I.  पिछले दो वर्षों में कंपनी P की 22% जनशक्ति को हटा दिया गया था।\n"
            "II. पिछले दो वर्षों में कंपनी P ने अपनी कई प्रमुख परिसंपत्तियां बेच दी हैं।"
        ),
        # option (a) is correct: both are effects of a common cause (financial crisis)
        "option_a": (
            "Both I and II are effects of a common cause. / "
            "I और II दोनों एक सामान्य कारण के प्रभाव हैं।"
        ),
        "option_b": (
            "I is the cause and II is its possible effect. / "
            "I कारण है और II इसका संभावित प्रभाव है।"
        ),
        "option_c": (
            "II is the cause and I is its possible effect. / "
            "II कारण है और I इसका संभावित प्रभाव है।"
        ),
        "option_d": (
            "Both I and II are independent cause. / "
            "I और II दोनों स्वतंत्र कारण हैं।"
        ),
        "correct_answer": "A",
        # Laying off manpower AND selling assets are both distress signals of a
        # single common cause: Company P's financial crisis / restructuring.
    },
    # ── Q21 ───────────────────────────────────────────────────────────────────────────
    # Source: CHSL Tier-II, 26 June 2023 (Shift-1)
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": (
            "I.  High level of air pollution in the city.\n"
            "II. Increase in respiratory and health-related problems in the population."
        ),
        "question_hi": (
            "I.  शहर में वायु प्रदूषण का उच्च स्तर।\n"
            "II. जनसंख्या में श्वसन संबंधी और स्वास्थ्य संबंधी समस्याओं में वृद्धि।"
        ),
        # option (a) is correct: II is the effect and I is the cause
        "option_a": (
            "Event (II) is the effect and event (I) is the cause. / "
            "घटना (II) प्रभाव है और घटना (I) इसका कारण है।"
        ),
        "option_b": (
            "Both events are effects of a common cause. / "
            "दोनों घटनाएं किसी साझा कारण के प्रभाव हैं।"
        ),
        "option_c": (
            "Both events are effects of some independent cause. / "
            "दोनों घटनाएं किन्हीं स्वतंत्र कारण के प्रभाव हैं।"
        ),
        "option_d": (
            "Event (I) is the effect and event (II) is the cause. / "
            "घटना (I) प्रभाव है और घटना (II) इसका कारण है।"
        ),
        "correct_answer": "A",
        # High air pollution (I = पहले/cause) → respiratory & health problems (II = बाद में/effect).
    },
    # ── Q22 ───────────────────────────────────────────────────────────────────────────
    # Source: CHSL Tier-II, 06 March 2023 (Shift-1)
    {
        "question_number": 22,
        "difficulty": "hard",
        "question_en": (
            "I.  Since the past three years, State M has reported a sharp and "
            "substantial decline in the state's agricultural produce.\n"
            "II. In the last five years, there has been an increase in the overall "
            "average Rainfall by 6% in State M bringing respite to the farmers."
        ),
        "question_hi": (
            "I.  पिछले तीन वर्षों से, राज्य M ने राज्य की कृषि उपज में तेज और "
            "पर्याप्त गिरावट दर्ज की है।\n"
            "II. पिछले पांच वर्षों में, राज्य M में कुल औसत वर्षा में 6% की वृद्धि "
            "हुई है, जिससे किसानों को राहत मिली है।"
        ),
        "option_a": (
            "I is the cause and II is its possible effect. / "
            "I कारण है और II इसका संभावित प्रभाव है।"
        ),
        "option_b": (
            "Both I and II are independent causes. / "
            "I और II दोनों स्वतंत्र कारण हैं।"
        ),
        "option_c": (
            "II is the cause and I is its possible effect. / "
            "II कारण है और I इसका संभावित प्रभाव है।"
        ),
        # option (d) is correct: both are effects of independent causes
        "option_d": (
            "Both I and II are the effects of independent cause. / "
            "I और II दोनों स्वतंत्र कारणों के प्रभाव हैं।"
        ),
        "correct_answer": "D",
        # Agricultural decline (I) and rainfall increase (II) move in contradictory
        # directions — decline despite more rain — driven by different independent
        # factors (pests/soil vs weather patterns).
    },
    # ── Q23 ───────────────────────────────────────────────────────────────────────────
    # Source: CGL Tier-II, 03 March 2023 (Shift-1)
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "I.  Country X reduced their crude oil import by 6% in the last 5 years.\n"
            "II. The automobile industry in Country X has witnessed a sharp decline "
            "of 13% in its growth margin this year."
        ),
        "question_hi": (
            "I.  देश X ने पिछले 5 वर्षों में अपने कच्चे तेल के आयात में 6% की कमी की है।\n"
            "II. देश X में ऑटोमोबाइल उद्योग के विकास मार्जिन में इस वर्ष 13% की भारी "
            "गिरावट देखी गई है।"
        ),
        # option (a) is correct: both are effects of independent causes
        "option_a": (
            "Both I and II are the effects of independent cause. / "
            "I और II दोनों स्वतंत्र कारणों के प्रभाव हैं।"
        ),
        "option_b": (
            "I is the cause and II is its possible effect. / "
            "I कारण है और II इसका संभावित प्रभाव है।"
        ),
        "option_c": (
            "II is the cause and I is its possible effect. / "
            "II कारण है और I इसका संभावित प्रभाव है।"
        ),
        "option_d": (
            "Both I and II are independent causes. / "
            "I और II दोनों स्वतंत्र कारण हैं।"
        ),
        "correct_answer": "A",
        # Crude oil import reduction (I) driven by govt policy / renewable push;
        # Automobile industry decline (II) driven by global competition / recession.
        # Different independent drivers → both are effects of independent causes.
    },
    # ── Q24 ───────────────────────────────────────────────────────────────────────────
    # Source: CGL Tier-II, 02 March 2023 (Shift-1)
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": (
            "I.  This year College X reduced the cut-off marks to 50 from 60 for "
            "the entrance exam.\n"
            "II. In the last two years, the Students Union in College X has been "
            "actively negotiating with the college administration regarding the "
            "Quality of food and Health and Hygiene standards at the College Canteen."
        ),
        "question_hi": (
            "I.  इस वर्ष कॉलेज X ने प्रवेश परीक्षा के लिए कट-ऑफ अंक 60 से घटाकर "
            "50 कर दिए।\n"
            "II. पिछले दो वर्षों में, कॉलेज X में छात्र संघ कॉलेज कैंटीन में भोजन "
            "की गुणवत्ता और स्वास्थ्य और स्वच्छता मानकों के संबंध में कॉलेज "
            "प्रशासन के साथ सक्रिय रूप से बातचीत कर रहा है।"
        ),
        "option_a": (
            "II is the cause and I is its possible effect. / "
            "II कारण है और I इसका संभावित प्रभाव है।"
        ),
        "option_b": (
            "I is the cause and II is its possible effect. / "
            "I कारण है और II इसका संभावित प्रभाव है।"
        ),
        # option (c) is correct: both are effects of independent causes
        "option_c": (
            "Both I and II are the effects of independent cause. / "
            "I और II दोनों स्वतंत्र कारणों के प्रभाव हैं।"
        ),
        "option_d": (
            "Both I and II are independent causes. / "
            "I और II दोनों स्वतंत्र कारण हैं।"
        ),
        "correct_answer": "C",
        # Reducing cut-off marks (I) due to: fewer qualified applicants, policy change.
        # Students negotiating about canteen standards (II) due to: food quality concerns.
        # Completely unrelated events → effects of independent causes.
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
