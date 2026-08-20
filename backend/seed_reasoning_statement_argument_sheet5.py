"""
seed_reasoning_statement_argument_sheet5.py
============================================
Seeds Statement-Argument Q23–Q28 from Gagan Pratap Reasoning PDFs (Sheet 5).
Subject : Reasoning
Topic   : Statement Argument

All questions are stored using the STANDARD 4-option format:
  (A) Only argument I is strong.
  (B) Only argument II is strong.
  (C) Both I & II are strong.
  (D) Neither I nor II is strong.

The original exam option sets vary (some have "Either I or II" instead of "Neither"
or "Both"; some are shuffled). They are normalised here to the standard order for
consistent display. No frontend injection needed.

Sources: UPSI (Nov 2021) and UP Constable (Jan 2019) papers.

Answer key:
  Q23  B — Should India ban Chinese products? (UPSI, 20 Nov 2021, Shift-2)
            I:  No, the Chinese market will be MORE affected than the Indian market
                → WEAK ✗ (India's policy should focus on domestic benefit, not concern
                for China's market; the argument provides no reason to protect China)
            II: Yes, low prices of Chinese goods attract buyers which has indirectly
                affected the revenues of the Indian economy → STRONG ✓
                (concrete economic harm to India: price competitiveness of Chinese
                imports hurts domestic production and government revenue)
            Only Argument II is strong.

  Q24  A — Should the police wear body cameras? (UPSI, 29 Nov 2021, Shift-2)
            I:  Improves civility of police-citizen encounters and enhances citizen
                perceptions of police transparency and legitimacy → STRONG ✓
                (two concrete institutional benefits directly relevant to policing)
            II: Doesn't look good on their uniform → WEAK ✗
                (aesthetic concern is entirely irrelevant to a policy decision about
                police accountability and public safety)
            Only Argument I is strong.

  Q25  A — Should girls learn martial arts like karate? (UPSI, 13 Nov 2021, Shift-3)
            I:  Will help them defend themselves from rogues → STRONG ✓
                (self-defence is a direct, practical and safety-enhancing benefit)
            II: They will lose their interest in studies → WEAK ✗
                (unsubstantiated assumption; millions of students successfully balance
                martial arts with academics)
            Only Argument I is strong.

  Q26  C — Should new big industries be started in Delhi? (UP Constable, 27 Jan 2019, Shift-1)
            I:  No, it will add to the city's pollution → STRONG ✓
                (Delhi is already one of the world's most polluted cities; more
                industry would worsen documented air-quality crisis)
            II: Yes, it will provide employment opportunities → STRONG ✓
                (employment creation is a concrete, real economic benefit)
            Both I & II are strong — valid arguments from opposite perspectives.

  Q27  A — Should taxes be abolished in a developing country like India?
            (UP Constable, 28 Jan 2019, Shift-2)
            I:  No, taxes are a good source of income for the government to take
                steps for the development of the country → STRONG ✓
                (taxes fund essential public services, infrastructure, healthcare,
                and education — critical for a developing nation)
            II: Yes, these taxes are NOT used for the goodwill of the nation → WEAK ✗
                (misuse of tax revenue calls for better governance and accountability,
                NOT abolition of taxes; abolition would eliminate ALL government
                revenue, including for legitimate purposes)
            Only Argument I is strong.

  Q28  A — Should mid-day meals in government schools be stopped?
            (UP Constable, 28 Jan 2019, Shift-1)
            I:  No, it provides at least one meal to underprivileged children → STRONG ✓
                (concrete nutritional benefit to the most vulnerable children;
                directly addresses food security and health)
            II: Yes, it provides wrong incentives to attend school → WEAK ✗
                (getting children to school for ANY reason — including food — is the
                primary objective; once there, they receive education; the "wrong
                incentive" concern is outweighed by the attendance benefit)
            Only Argument I is strong.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Argument_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Statement Argument"

# Standard 4-option set — same for all Q23–Q28.
_A = "Only argument I is strong. / केवल तर्क I ठोस है।"
_B = "Only argument II is strong. / केवल तर्क II ठोस है।"
_C = "Both I & II are strong. / तर्क I और II दोनों ठोस हैं।"
_D = "Neither I nor II is strong. / न तो तर्क I और न ही तर्क II ठोस है।"

QUESTIONS = [
    # ── Q23 (UPSI, 20 Nov 2021, Shift-2) ─────────────────────────────────────
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should India ban Chinese products?\n\n"
            "Arguments:\n"
            "I.  No, the Chinese market will be affected compared to the Indian "
            "market.\n"
            "II. Yes, the low prices of Chinese goods attract lots of buyers which "
            "has indirectly affected the revenues of the Indian economy."
        ),
        "question_hi": (
            "कथन: क्या भारत को चीनी उत्पादों पर प्रतिबंध लगाना चाहिए?\n\n"
            "तर्क:\n"
            "I.  नहीं, भारतीय बाजार की तुलना में चीनी बाजार प्रभावित होगा।\n"
            "II. हाँ, चीनी वस्तुओं की कम कीमतें बहुत सारे खरीदारों को आकर्षित "
            "करती हैं जिसका अप्रत्यक्ष रूप से भारतीय अर्थव्यवस्था के राजस्व पर "
            "प्रभाव पड़ा है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  Arguing that China's market would be hurt MORE — India's policy
        #     decisions should focus on domestic benefit, not concern for impact
        #     on China; no reason given to refrain from the ban → WEAK ✗
        # II: Price competitiveness of Chinese imports has verifiably hurt domestic
        #     Indian producers and reduced government tax revenues — concrete
        #     economic harm with clear policy relevance → STRONG ✓
    },
    # ── Q24 (UPSI, 29 Nov 2021, Shift-2) ─────────────────────────────────────
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should the police wear body cameras?\n\n"
            "Arguments:\n"
            "I.  Yes, placing bodyworn cameras on police officers improves the "
            "civility of police-citizen encounters and enhances citizen perceptions "
            "of police transparency and legitimacy.\n"
            "II. No, it doesn't look good on their uniform."
        ),
        "question_hi": (
            "कथन: क्या पुलिस को बॉडी कैमरे पहनने चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, पुलिस अधिकारियों के शरीर पर पहनने वाले कैमरे लगाने से "
            "पुलिस-नागरिक मुठभेड़ों की सभ्यता में सुधार होता है और पुलिस की "
            "पारदर्शिता और वैधता के बारे में नागरिकों के धारणा बढ़ती है।\n"
            "II. नहीं, यह उनकी वर्दी पर अच्छा नहीं लगता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Two concrete institutional benefits — improved police-citizen civility
        #     AND enhanced public perception of transparency/legitimacy — directly
        #     relevant to police policy → STRONG ✓
        # II: Aesthetic concern about how cameras look on uniforms is entirely
        #     irrelevant to a policy decision about accountability → WEAK ✗
    },
    # ── Q25 (UPSI, 13 Nov 2021, Shift-3) ─────────────────────────────────────
    {
        "question_number": 25,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should girls learn martial arts like karate?\n\n"
            "Arguments:\n"
            "I.  Yes, it will help them to defend themselves from rogues.\n"
            "II. No, they will lose their interest in studies."
        ),
        "question_hi": (
            "कथन: क्या लड़कियों को कराटे जैसी मार्शल आर्ट सीखनी चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, इससे उन्हें बदमाशों से अपना बचाव करने में मदद मिलेगी।\n"
            "II. नहीं, पढ़ाई में उनकी रुचि खत्म हो जाएगी।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Self-defence against real threats (rogues) is a direct, practical,
        #     and safety-enhancing benefit for girls → STRONG ✓
        # II: Loss of interest in studies is an unsubstantiated assumption;
        #     countless students successfully balance sports/martial arts with
        #     academics → WEAK ✗
    },
    # ── Q26 (UP Constable, 27 Jan 2019, Shift-1) ──────────────────────────────
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should new big industries be started in Delhi?\n\n"
            "Arguments:\n"
            "I.  No, it will add to the city's pollution.\n"
            "II. Yes, it will provide employment opportunities."
        ),
        "question_hi": (
            "कथन: क्या दिल्ली में नये बड़े उद्योग शुरू किये जाने चाहिए?\n\n"
            "तर्क:\n"
            "I.  नहीं, इससे शहर का प्रदूषण बढ़ेगा।\n"
            "II. हाँ, यह रोजगार के अवसर प्रदान करेगा।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
        # I:  Delhi is already among the world's most polluted cities; adding
        #     large industries would worsen the documented air-quality crisis
        #     → STRONG ✓
        # II: Industrial development generates employment — a concrete, vital
        #     economic benefit → STRONG ✓
        # Both present valid, real, and directly relevant consequences of the policy.
    },
    # ── Q27 (UP Constable, 28 Jan 2019, Shift-2) ──────────────────────────────
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should taxes be abolished in a developing country "
            "like India?\n\n"
            "Arguments:\n"
            "I.  No, taxes are a good source of Income for the government to take "
            "steps for the development of the country.\n"
            "II. Yes, these taxes are NOT used for the goodwill of the nation."
        ),
        "question_hi": (
            "कथन: क्या भारत जैसे विकासशील देश में करों को समाप्त कर दिया जाना "
            "चाहिए?\n\n"
            "तर्क:\n"
            "I.  नहीं, कर सरकार के लिए देश के विकास के लिए कदम उठाने के लिए "
            "आय का एक अच्छा स्रोत है।\n"
            "II. हाँ, इन करों का उपयोग राष्ट्र की सद्भावना के लिए नहीं किया "
            "जाता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Tax revenue funds public services, infrastructure, healthcare,
        #     and education — indispensable for a developing nation → STRONG ✓
        # II: Alleging taxes are misused calls for better governance and
        #     accountability, NOT abolition; abolishing taxes would eliminate ALL
        #     government revenue, crippling even legitimate development spending
        #     → WEAK ✗
    },
    # ── Q28 (UP Constable, 28 Jan 2019, Shift-1) ──────────────────────────────
    {
        "question_number": 28,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should mid-day meals in government schools be stopped?\n\n"
            "Arguments:\n"
            "I.  No, it provides at least one meal to underprivileged children.\n"
            "II. Yes, it provides a wrong incentives to attend school."
        ),
        "question_hi": (
            "कथन: क्या सरकारी स्कूलों में मध्याह्न भोजन बंद कर देना चाहिए?\n\n"
            "तर्क:\n"
            "I.  नहीं, यह वंचित बच्चों को कम से कम एक समय का भोजन प्रदान करता "
            "है।\n"
            "II. हाँ, यह स्कूल जाने के लिए गलत प्रोत्साहन प्रदान करता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Providing at least one nutritious meal to underprivileged children
        #     addresses food security and health; a concrete, vital social benefit
        #     → STRONG ✓
        # II: Getting children to school for any reason — including food — achieves
        #     the primary attendance objective; once present, they receive education;
        #     the "wrong incentive" concern is minor relative to the nutrition and
        #     attendance benefits → WEAK ✗
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
