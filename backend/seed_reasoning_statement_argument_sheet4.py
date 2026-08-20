"""
seed_reasoning_statement_argument_sheet4.py
============================================
Seeds Statement-Argument Q16–Q22 from Gagan Pratap Reasoning PDFs (Sheet 4).
Subject : Reasoning
Topic   : Statement Argument

All questions use the EXTENDED 5-option format where option (C) = "Either I or II
is strong." The 5th option "Both I and II are strong." is NOT stored in DB and is
injected by the frontend (SA_5OPT_E) when option_c starts with "Either I or II".
None of Q16–Q22's correct answers is (E) — the injected option is never correct
for these questions, but its presence keeps the display consistent with Q14–Q15.

Standard extended option order (A–D stored in DB):
  (A) Only argument I is strong.
  (B) Only argument II is strong.
  (C) Either I or II is strong.     ← triggers frontend SA_5OPT_E injection
  (D) Neither I nor II is strong.
  (E) Both I and II are strong.     ← injected by frontend, never correct here

Original exam sources: UPSI & NTPC CBT-2, 2021.

Answer key:
  Q16  A — Smoking ban in public places? (UPSI 02 Dec 2021, Shift-1)
            I:  Decreases possibility of fire disasters → STRONG ✓
                (concrete environmental-safety consequence directly linked to smoking)
            II: Not effective → WEAK ✗ (vague claim with no supporting reasoning)
            Only Argument I is strong.

  Q17  B — Government should control all news in a democracy? (UPSI 21 Nov 2021, Shift-3)
            I:  Unverified news might confuse people → WEAK ✗
                (supports targeted fact-checking, not blanket government control of
                ALL news; extreme measure for a limited concern)
            II: Controlled news loses credibility → STRONG ✓
                (fundamental principle: government-controlled news is perceived as
                propaganda, directly damaging public trust)
            Only Argument II is strong.

  Q18  A — Joint families better than nuclear families? (NTPC CBT-2, 2021)
            I:  Joint families ensure security and reduce burden of work → STRONG ✓
                (two concrete, well-documented benefits: shared security + division
                of labour)
            II: Nuclear families require more money to run → WEAK ✗
                (contradictory: if nuclear families cost more, that SUPPORTS joint
                families being better — the "No" position is self-undermining)
            Only Argument I is strong.

  Q19  A — Ban on advertising junk food? (UPSI 17 Nov 2021, Shift-1)
            I:  Will reduce overconsumption of junk food → STRONG ✓
                (advertising is a proven driver of consumption; restricting it
                directly reduces demand)
            II: It is very tasty → WEAK ✗
                (taste is a personal preference and an entirely irrelevant basis
                for a public-health policy decision)
            Only Argument I is strong.

  Q20  A — Ban on smoking in public places? (UPSI 13 Nov 2021, Shift-2)
            I:  Lessens possibility of second-hand smoke inhaled by non-smokers
                → STRONG ✓ (core public-health justification; protecting non-smokers
                from involuntary exposure to carcinogens)
            II: Can affect businesses → WEAK ✗
                (commercial impact does not outweigh public-health benefits;
                businesses can adapt)
            Only Argument I is strong.

  Q21  D — Ban on hunting of wild animals? (UPSI 25 Nov 2021, Shift-3)
            I:  Carelessness during hunting is dangerous to team members, passers-by,
                and the hunter himself → WEAK ✗
                (addresses HOW hunting is conducted, not WHETHER to ban it;
                better safety regulations — not a complete ban — would address
                this concern)
            II: Hunting serves as a form of exercise → WEAK ✗
                (countless safer forms of exercise exist; this trivial benefit
                cannot justify allowing wild animal hunting)
            Neither I nor II is strong.

  Q22  A — Restrict cell phone use in public places? (UPSI 27 Nov 2021, Shift-2)
            I:  Phones in libraries, music halls, and galleries can annoy others
                and ruin their experience → STRONG ✓
                (concrete, specific harm to other people's enjoyment of public
                spaces; directly supports the restriction)
            II: Life is impossible without cell phones → WEAK ✗
                (exaggerated; restricting phones in certain venues ≠ banning them
                entirely; people function fine with phones off for short periods)
            Only Argument I is strong.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Argument_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Statement Argument"

# Extended 5-option set (option E injected by frontend as SA_5OPT_E because
# option_c starts with "Either I or II").
_A = "Only argument I is strong. / केवल तर्क I मजबूत है।"
_B = "Only argument II is strong. / केवल तर्क II मजबूत है।"
_C = "Either I or II is strong. / या तो I या II मजबूत है।"   # triggers injection
_D = "Neither I nor II is strong. / न तो I और न ही II मजबूत है।"
# (E) "Both I and II are strong." injected by frontend; never correct for Q16–Q22.

QUESTIONS = [
    # ── Q16 (UPSI, 02 Dec 2021, Shift-1) ─────────────────────────────────────
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should there be a ban on smoking in public places?\n\n"
            "Arguments:\n"
            "I.  Yes, this will decrease the possibility of fire disasters.\n"
            "II. No, they are not effective."
        ),
        "question_hi": (
            "कथन: क्या सार्वजनिक स्थानों पर धूम्रपान पर प्रतिबंध होना चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, इससे अग्नि आपदाओं की संभावना कम हो जाएगी।\n"
            "II. नहीं, वे प्रभावी नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Fire disasters are a concrete, real risk from public smoking;
        #     banning directly reduces this risk → STRONG ✓
        # II: "Not effective" — vague assertion without any explanation;
        #     cannot be considered a strong argument → WEAK ✗
    },
    # ── Q17 (UPSI, 21 Nov 2021, Shift-3) ─────────────────────────────────────
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should all news be controlled by the Government in "
            "a democracy?\n\n"
            "Arguments:\n"
            "I.  Yes, Unverified news might confuse people.\n"
            "II. No, Controlled news loses credibility."
        ),
        "question_hi": (
            "कथन: क्या लोकतंत्र में सभी समाचारों पर सरकार का नियंत्रण होना "
            "चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, असत्यापित समाचार लोगों को भ्रमित कर सकते हैं।\n"
            "II. नहीं, नियंत्रित समाचार विश्वसनीयता खो देते हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  Misinformation is a real concern, but blanket government control of
        #     ALL news is an extreme overreach; independent fact-checking or press
        #     accountability are better solutions → WEAK ✗
        # II: Government-controlled news is inherently perceived as propaganda;
        #     loss of credibility directly undermines news' purpose → STRONG ✓
    },
    # ── Q18 (NTPC CBT-2, 2021) ────────────────────────────────────────────────
    {
        "question_number": 18,
        "difficulty": "easy",
        "question_en": (
            "Statement: Are joint families better than nuclear families?\n\n"
            "Arguments:\n"
            "I.  Yes, joint families ensure security and also reduce the burden "
            "of work.\n"
            "II. No, it requires more money to run the nuclear family."
        ),
        "question_hi": (
            "कथन: क्या संयुक्त परिवार एकल परिवारों से बेहतर हैं?\n\n"
            "तर्क:\n"
            "I.  हाँ, संयुक्त परिवार सुरक्षा सुनिश्चित करते हैं और कार्य का "
            "बोझ भी कम करते हैं।\n"
            "II. नहीं, एकल परिवार चलाने के लिए अधिक धन की आवश्यकता होती है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Two concrete benefits — shared security and division of domestic
        #     work — are well-documented advantages of joint families → STRONG ✓
        # II: "Nuclear families require more money" actually SUPPORTS joint
        #     families being better (contradicts the "No" position); the argument
        #     is logically self-undermining → WEAK ✗
    },
    # ── Q19 (UPSI, 17 Nov 2021, Shift-1) ─────────────────────────────────────
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should there be a ban on advertising junk food?\n\n"
            "Arguments:\n"
            "I.  Yes, this will reduce the overconsumption of junk food.\n"
            "II. No, it is very tasty."
        ),
        "question_hi": (
            "कथन: क्या जंक फूड के विज्ञापन पर रोक लगनी चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, इससे जंक फूड का अधिक सेवन कम हो जाएगा।\n"
            "II. नहीं, यह बहुत स्वादिष्ट होता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Advertising is a proven driver of consumption; restricting ads
        #     directly reduces demand and overconsumption → STRONG ✓
        # II: "It is very tasty" is a personal preference with zero relevance
        #     to a public-health policy decision → WEAK ✗
    },
    # ── Q20 (UPSI, 13 Nov 2021, Shift-2) ─────────────────────────────────────
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should there be a ban on smoking in public places?\n\n"
            "Arguments:\n"
            "I.  Yes, it can lessen the possibility of second-hand smoke being "
            "inhaled by nonsmokers.\n"
            "II. No, they can affect businesses."
        ),
        "question_hi": (
            "कथन: क्या सार्वजनिक स्थानों पर धूम्रपान पर प्रतिबंध लगाया जाना "
            "चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, यह धूम्रपान न करने वालों द्वारा सेकंड हैंड धूम्रपान "
            "करने की संभावना को कम कर सकता है।\n"
            "II. नहीं, वे व्यवसायों को प्रभावित कर सकते हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Protecting non-smokers from involuntary exposure to carcinogens
        #     (second-hand smoke) is the primary public-health justification for
        #     a public smoking ban → STRONG ✓
        # II: Business impact is a minor economic concern that does not outweigh
        #     documented public-health benefits; businesses adapt to regulations
        #     → WEAK ✗
    },
    # ── Q21 (UPSI, 25 Nov 2021, Shift-3) ─────────────────────────────────────
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should there be a ban on the hunting of wild animals?\n\n"
            "Arguments:\n"
            "I.  Yes, carelessness during hunting can be dangerous to other "
            "members of a hunting team, passers-by, and even the hunter himself.\n"
            "II. No, it serves as a form of exercise."
        ),
        "question_hi": (
            "कथन: क्या जंगली जानवरों के शिकार पर रोक लगनी चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, शिकार के दौरान लापरवाही शिकार दल के अन्य सदस्यों, "
            "राहगीर और यहाँ तक कि खुद शिकारी के लिए भी खतरनाक हो सकती है।\n"
            "II. नहीं, यह अभ्यास के रूप में कार्य करता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  "Carelessness during hunting" is about HOW hunting is conducted, not
        #     whether to ban it; improved safety training and regulations — not a
        #     complete ban — would address this concern → WEAK ✗
        # II: Countless safer forms of exercise exist; this trivial benefit cannot
        #     justify allowing wild animal hunting → WEAK ✗
    },
    # ── Q22 (UPSI, 27 Nov 2021, Shift-2) ─────────────────────────────────────
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should usage of cell phones be restricted in public places?\n\n"
            "Arguments:\n"
            "I.  Yes, in public places like libraries, music halls, and galleries, "
            "phones can annoy and ruin the experience of others.\n"
            "II. No, life is impossible without cell phones."
        ),
        "question_hi": (
            "कथन: क्या सार्वजनिक स्थानों पर सेल फोन का उपयोग प्रतिबंधित होना "
            "चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, सार्वजनिक स्थानों जैसे पुस्तकालयों, संगीत हॉलों और दीर्घाओं "
            "में, फोन दूसरों को परेशान कर सकते हैं और उनके अनुभव को बर्बाद कर "
            "सकते हैं।\n"
            "II. नहीं, सेलफोन के बिना जीवन असंभव है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Specific, concrete harm to other people's experience in named public
        #     spaces (libraries, music halls, galleries); directly and proportionately
        #     justifies the restriction → STRONG ✓
        # II: "Life is impossible without cell phones" is a gross exaggeration;
        #     restricting phones in certain public venues ≠ banning them entirely
        #     → WEAK ✗
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
