"""
seed_reasoning_statement_argument_sheet1.py
============================================
Seeds Statement-Argument Q1–Q4 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Statement Argument

Fixed 4-option format (same options every question):
  (A) Only argument I is strong.
  (B) Only argument II is strong.
  (C) Both I & II are strong.
  (D) Neither I nor II is strong.

No 5th option injection by frontend — stored entirely in 4 DB columns.

Answer key:
  Q1  A — Sex determination test: ban or not?
           I:  Leads to female foeticide & social imbalance → STRONG (concrete harm) ✓
           II: People have right to know sex of unborn child → WEAK
               (right overridden by documented social harm)
           Only Argument I is strong.

  Q2  D — One-child policy for Indian parents?
           I:  "Only way" to check ever-increasing population → WEAK
               ("only way" is too absolute; education/awareness are alternatives)
           II: No other country uses this pressure tactic → WEAK
               (irrelevant comparison; policy need not follow other nations)
           Neither I nor II is strong.

  Q3  B — Allow oil companies to fix petroleum prices on market basis?
           I:  "Only way" to make oil companies commercially viable → WEAK
               (subsidies, efficiency drives are other routes)
           II: Additional burden on retail prices of essentials, hardship for
               masses → STRONG (concrete economic harm to common people) ✓
           Only Argument II is strong.

  Q4  B — Abolish capital punishment altogether in India?
           I:  EU countries have abolished it → WEAK
               (irrelevant cross-country comparison for India's policy)
           II: Instills fear in criminals, restrains heinous crimes → STRONG
               (deterrence of capital punishment is a legitimate, widely-held
               rationale; directly relevant to the statement) ✓
           Only Argument II is strong.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Argument_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Statement Argument"

# Standard fixed options — identical for every Statement-Argument question.
_OPT_A = "Only argument I is strong. / केवल तर्क I ठोस है।"
_OPT_B = "Only argument II is strong. / केवल तर्क II ठोस है।"
_OPT_C = "Both I & II are strong. / तर्क I और II दोनों ठोस हैं।"
_OPT_D = "Neither I nor II is strong. / न तो तर्क I और न ही तर्क II ठोस है।"

QUESTIONS = [
    # ── Q1 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should sex determination test during pregnancy be "
            "completely banned?\n\n"
            "Arguments:\n"
            "I.  Yes, this leads to indiscriminate female foeticide and eventually "
            "will lead to social imbalance.\n"
            "II. No, people have a right to know about the sex of their unborn child."
        ),
        "question_hi": (
            "कथन: क्या गर्भावस्था के दौरान लिंग निर्धारण परीक्षण पर पूरी तरह से "
            "प्रतिबंध लगा दिया जाना चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, इससे मादा भ्रूण की अंधाधुंध हत्या होती है और अंततः सामाजिक "
            "असंतुलन होगा।\n"
            "II. नहीं, लोगों को उनके अजन्मे बच्चों के बारे में जानने का अधिकार है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # I:  Female foeticide and gender imbalance are documented, concrete harms.
        #     A ban directly prevents these → STRONG ✓
        # II: "Right to know" sounds valid but is outweighed by severe social harm;
        #     not strong enough in this socio-legal context → WEAK ✗
    },
    # ── Q2 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should the parents in India in future be forced to opt for "
            "only one child as against two or many at present?\n\n"
            "Arguments:\n"
            "I.  Yes, this is the only way to check the ever increasing population "
            "of India.\n"
            "II. No, this type of pressure tactic is not adopted by any other country "
            "in the world."
        ),
        "question_hi": (
            "कथन: क्या भारत में भविष्य में माता-पिता को वर्तमान में दो या कई बच्चों "
            "के मुकाबले एक के लिए ही बाध्य किया जाना चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, भारत की सदैव बढ़ती रहने वाली जनसंख्या को नियंत्रित करने का "
            "यही एकमात्र तरीका है।\n"
            "II. नहीं, इस तरह की दबाव डालने की युक्ति विश्व में कोई भी देश नहीं "
            "अपनाता है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # I:  "ONLY way" is too absolute — education, awareness, and incentives
        #     are proven alternatives; overly extreme claim → WEAK ✗
        # II: Comparison with other countries is irrelevant; India's policy choices
        #     don't require foreign precedent → WEAK ✗
    },
    # ── Q3 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should the oil companies be allowed to fix the price of "
            "petroleum products depending on market conditions?\n\n"
            "Arguments:\n"
            "I.  Yes, this is the only way to make the oil companies commercially "
            "viable.\n"
            "II. No, this will put additional burden on the retail prices of essential "
            "commodities and will cause a lot of hardships to the masses."
        ),
        "question_hi": (
            "कथन: क्या तेल कंपनियों को पेट्रोलियम उत्पादों का मूल्य बाजार की "
            "स्थितियों के आधार पर तय करने की अनुमति देनी चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, यही एकमात्र तरीका है जिससे तेल कंपनियों को वाणिज्यिक रूप में "
            "सफल बनाया जा सके।\n"
            "II. नहीं, इससे आम लोगों को बहुत कठिनाई होगी क्योंकि इस अनुमति से "
            "आवश्यक वस्तुओं के खुदरा कीमतों पर अतिरिक्त बोझ आएगा।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # I:  "ONLY way" to ensure viability is too absolute; subsidies, efficiency
        #     measures, and public-sector support exist → WEAK ✗
        # II: Market-priced petroleum raises transport costs, inflating prices of
        #     all essential goods — a concrete, wide-ranging burden on the masses
        #     → STRONG ✓
    },
    # ── Q4 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should capital punishment be abolished altogether in India?\n\n"
            "Arguments:\n"
            "I.  Yes, countries belonging to European Union have abolished capital "
            "punishment.\n"
            "II. No, this is the only way to instill fear in the minds of criminals "
            "which will restrain them from committing heinous crime."
        ),
        "question_hi": (
            "कथन: क्या मृत्यु दण्ड भारत में पूरी तरह से समाप्त कर देना चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, यूरोपीय संघ के सभी देशों ने मृत्यु दण्ड समाप्त कर दिया है।\n"
            "II. नहीं, अपराधी के मन में भय बनाए रखने का एक तरीका है, जो उन्हें "
            "जघन्य अपराध करने से रोकता है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # I:  EU countries abolishing capital punishment is an irrelevant comparison;
        #     India's socio-legal context is distinct → WEAK ✗
        # II: Capital punishment as a deterrent against heinous crime is a strong,
        #     substantive argument directly relevant to the statement → STRONG ✓
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
