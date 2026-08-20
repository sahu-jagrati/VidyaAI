"""
seed_reasoning_assertion_reason_sheet2.py
==========================================
Seeds Assertion and Reason Q3-Q8 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Assertion and Reason

5-OPTION FORMAT (same scheme as Sheet 1):
  option_a = (a) Both A & R true, R explains A.
  option_b = (b) Both A & R true, R does NOT explain A.
  option_c = (c) A true, R false.
  option_d = (d) A false, R true.
  (e) Both A & R false — shown in question body; correct_answer stored as "E".

Answer key:
  Q3  Answer: C — A is true but R is false.
      A: Leakages in household gas cylinders can be detected. → TRUE ✓
         (we CAN detect LPG leaks by smell)
      R: LPG has a strong smell. → FALSE ✗
         LPG (propane + butane) is NATURALLY ODORLESS. The image confirms this:
         C₂H₅SH / CH₃CH₂SH (ethyl mercaptan / ethanethiol) is artificially ADDED
         to LPG as an odorant so that leaks can be detected. LPG itself has no
         smell; R is factually incorrect. → A true, R false → (c)

  Q4  Answer: A — Both A & R are true & R is the correct explanation of A.
      A: Plaster of Paris is used by doctors for setting fractured bones. → TRUE ✓
      R: When Plaster of Paris is mixed with water and applied around fractured
         limbs, it sets into a hard mass. → TRUE ✓
      Does R explain A? YES — because PoP sets into a rigid hard mass when wet,
      doctors use it as a splint/cast to immobilise fractured bones during healing.
      R provides the exact mechanism that makes A possible. → (a)

  Q5  Answer: D — A is false but R is true.
      A: We prefer to wear white clothes in winter. → FALSE ✗
         In winter we prefer DARK/BLACK clothes because dark colours ABSORB heat,
         keeping us warm. White clothes REFLECT heat, making us feel colder.
      R: White clothes are good reflectors of heat. → TRUE ✓
         White surfaces reflect visible light and solar (near-infrared) radiation;
         this is why white is preferred in SUMMER, not winter.
      → A is false, R is true → (d)

  Q6  Answer: D — A is false but R is true.
      A: Baking soda creates acidity in the stomach. → FALSE ✗
         The image notes "ENO = soda" — ENO is an antacid! Baking soda (sodium
         bicarbonate, NaHCO₃) is ALKALINE; it NEUTRALISES stomach acidity, not
         creates it. It is used as a home remedy for heartburn.
      R: Baking soda is alkaline. → TRUE ✓
         NaHCO₃ has pH > 7; it is indeed alkaline/basic.
      Does R explain A? No — A itself is false (baking soda neutralises, not
      creates acidity). R is true but it cannot be the explanation of a false
      assertion. → A false, R true → (d)

  Q7  Answer: A — Both A & R are true & R is the correct explanation of A.
      A: When common salt is kept open, it absorbs moisture from the air. → TRUE ✓
         Table salt (NaCl) is hygroscopic and clumps when exposed to humid air.
      R: Common salt contains magnesium chloride. → TRUE ✓ (as an impurity)
         The image annotation "→ Impurity" confirms: commercial NaCl contains
         MgCl₂ as an impurity. MgCl₂ is highly deliquescent (hygroscopic) and is
         the primary reason why table salt absorbs atmospheric moisture.
      Does R explain A? YES — the presence of hygroscopic MgCl₂ impurity directly
      causes NaCl to absorb moisture. → Both true, R explains A → (a)

  Q8  Answer: C — A is true but R is false.
      A: When a body is dipped in liquid fully or partially, there is a decrease
         in its weight. → TRUE ✓ (Archimedes' Principle — apparent weight loss =
         upthrust = weight of displaced liquid)
      R: The decrease in weight is due to the higher density of the displaced
         liquid. → FALSE ✗
         The correct explanation is: a submerged body experiences an UPTHRUST
         (buoyant force) equal to the WEIGHT of displaced liquid. The "decrease"
         occurs due to upthrust, not because the displaced liquid has "higher
         density". R misframes the cause — even in a low-density liquid, apparent
         weight decreases because of upthrust, not density comparison.
      → A true, R false → (c)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assertion_Reason_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Assertion and Reason"

# Standard A&R options stored in the 4 DB columns (same for every question).
# Option (e) is shown inside question_en/question_hi; answer "E" stored as String "E".
_OPT_A = "Both A & R are true & R is the correct explanation of A. / A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"
_OPT_B = "Both A & R are true but R is not the correct explanation of A. / A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।"
_OPT_C = "A is true but R is false. / A सत्य है लेकिन R असत्य है।"
_OPT_D = "A is false but R is true. / A असत्य है लेकिन R सत्य है।"
_OPT_E_LINE = "(e) Both A & R are false. / A और R दोनों असत्य हैं।"

QUESTIONS = [
    # ── Q3 ── A true (leaks detected) | R false (LPG is odorless; odorant added) ──
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Leakages in household gas cylinders can be detected.\n"
            "Reason (R): LPG has a strong smell.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): घरेलू गैस सिलेंडर में रिसाव का पता लगाया जा सकता है।\n"
            "कारण (R): एलपीजी में तेज गंध होती है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # A: TRUE — LPG leaks CAN be detected by smell.
        # R: FALSE — LPG (propane/butane mixture) is NATURALLY ODORLESS. The smell
        # that alerts us to leaks comes from ethyl mercaptan (C₂H₅SH / ethanethiol,
        # CH₃CH₂SH) which is ARTIFICIALLY ADDED to LPG as a safety odorant. LPG
        # itself has no smell; R is factually incorrect. → C
    },
    # ── Q4 ── Both true, R explains A (Plaster of Paris / fractures) ──────────────
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Plaster of Paris is used by doctors for setting "
            "fractured bones.\n"
            "Reason (R): When Plaster of Paris is mixed with water and applied "
            "around the fractured limbs, it sets into a hard mass.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): डॉक्टरों द्वारा टूटी हुई हड्डियों को सही करने के लिए प्लास्टर "
            "ऑफ पेरिस का उपयोग किया जाता है।\n"
            "कारण (R): जब प्लास्टर ऑफ पेरिस को पानी के साथ मिलाया जाता है और खंडित "
            "अंगों के चारों ओर लगाया जाता है, तो यह एक कठोर द्रव्यमान में बदल जाता है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # A: TRUE — Plaster of Paris (CaSO₄·½H₂O) is indeed used for fracture casts.
        # R: TRUE — PoP + water → CaSO₄·2H₂O (gypsum), which sets into a hard rigid
        # mass. This is the exact chemical mechanism that makes it useful for fractures.
        # R correctly and directly explains why doctors use PoP. → A
    },
    # ── Q5 ── A false (dark clothes for winter), R true (white reflects heat) ──────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): We prefer to wear white clothes in winter.\n"
            "Reason (R): White clothes are good reflectors of heat.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): हम सर्दियों में सफेद कपड़े पहनना पसंद करते हैं।\n"
            "कारण (R): सफेद कपड़े गर्मी के अच्छे परावर्तक होते हैं।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # A: FALSE — In winter we prefer DARK/BLACK clothes because dark colours
        # ABSORB heat radiation and keep us warm. White clothes REFLECT heat, making
        # us feel colder. We prefer white/light clothes in SUMMER (to reflect heat).
        # R: TRUE — White surfaces are good reflectors of both visible light and solar
        # (near-infrared) radiation. This is a scientifically accepted fact.
        # Since A is false, R (though true) cannot be the explanation of A. → D
    },
    # ── Q6 ── A false (baking soda neutralises; not creates acidity), R true ────────
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Baking soda creates acidity in the stomach.\n"
            "Reason (R): Baking soda is alkaline.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): बेकिंग सोडा पेट में एसिडिटी पैदा करता है।\n"
            "कारण (R): बेकिंग सोडा क्षारीय है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # A: FALSE — Baking soda (sodium bicarbonate, NaHCO₃) is ALKALINE. It
        # NEUTRALISES stomach acidity; it does NOT create acidity. ENO (an antacid)
        # contains NaHCO₃ and is consumed to relieve heartburn/acidity — the opposite
        # of what A claims.
        # R: TRUE — NaHCO₃ has pH > 7 and is indeed alkaline/basic.
        # A is false, so R (though true) cannot explain a false assertion. → D
    },
    # ── Q7 ── Both true, R explains A (NaCl absorbs moisture due to MgCl₂ impurity)
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): When common salt is kept open, it absorbs moisture "
            "from the air.\n"
            "Reason (R): Common salt contains magnesium chloride.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): जब आम नमक को खुला रखा जाता है, तो यह हवा से नमी को अवशोषित "
            "करता है।\n"
            "कारण (R): आम नमक में मैग्नीशियम क्लोराइड होता है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # A: TRUE — Common table salt (NaCl) clumps and absorbs moisture when left
        # open in humid conditions; this is well-known practical experience.
        # R: TRUE — Commercial NaCl contains MgCl₂ (magnesium chloride) as an
        # impurity (confirmed by the image annotation "→ Impurity"). MgCl₂ is
        # highly deliquescent (hygroscopic) and is the primary reason table salt
        # absorbs atmospheric moisture.
        # Does R explain A? YES — the MgCl₂ impurity is the direct chemical cause
        # of NaCl's hygroscopic behaviour in humid air. → A
    },
    # ── Q8 ── A true (Archimedes), R false (upthrust not 'higher density') ─────────
    {
        "question_number": 8,
        "difficulty": "hard",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): When a body is dipped in liquid fully or partially, "
            "there is a decrease in its weight.\n"
            "Reason (R): The decrease in weight is due to the higher density of "
            "the displaced liquid.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): जब कोई शरीर पूरी तरह या आंशिक रूप से तरल में डुबा होता है, "
            "तो उसके वजन में कमी होती है।\n"
            "कारण (R): वजन में कमी विस्थापित तरल के उच्च घनत्व के कारण होती है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # A: TRUE — Archimedes' Principle: any body partially or fully submerged in
        # a fluid experiences an upthrust (buoyant force) equal to the weight of
        # fluid displaced, causing an apparent decrease in the body's weight. ✓
        # R: FALSE — The reason for decreased weight is UPTHRUST (buoyant force),
        # NOT "the higher density of the displaced liquid." R misidentifies the cause.
        # Upthrust = ρ × g × V (density × gravity × volume displaced); even in a
        # low-density liquid the apparent weight decreases. The density of the liquid
        # determines the magnitude of upthrust, not the existence of weight decrease.
        # R is factually wrong as a causal explanation. → C
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
