"""
seed_reasoning_cube_and_dice_sheet5.py
=======================================
Seeds Reasoning → Cube and Dice  Q26–Q35 (DSSSB / KVS exam papers source).

question_numbers 26–35.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q26 D  (II, III and IV)
     — Net with symbols @,$,#,&,©,%; spine (col 2) = @–#–©–%;
       branches: $ off #, & off ©.  Pairs: {@,©},{#,%},{$,&}.
       Cubes II, III, IV are consistent; cube I shows a contradictory pair.
       [DSSSB TGT English (Female) - 14 Sep 2021 - Shift 3]

Q27 A  (8)
     — 4×4×4 cube (64 small). Each of the 3 pairs of opposite faces is painted
       one distinct colour (Red / Yellow / Brown). At every corner of the big
       cube, all 3 differently-coloured faces meet → all 8 corner small cubes
       have 3 faces painted with 3 different colours. Answer = 8.
       [DSSSB TGT CS - 07 Aug 2021 - Shift 1]

Q28 C  (64)
     — 3 equal cuts per axis → 4 sections per axis → 4×4×4 = 64 small cubes.
       [DSSSB TGT English (Female) - 14 Sep 2021 - Shift 3]

Q29 A  (Both I and III)
     — Net with symbols M,K,T,9,7,L; from net layout:
       pairs {M,T},{K,9},{7,L}. Cubes I and III satisfy all constraints;
       cube II shows an impossible adjacent-opposite pair.
       [DSSSB PRT - 14 Nov 2019 - Shift 1]

Q30 C  (I & III Both)
     — Net (cross shape): horizontal spine A–9–8–7; vertical branches 3 (above 8)
       and C (below 8). Pairs: {A,8},{9,7},{3,C}.
       Cubes I and III are consistent with net; cube II is not.
       [DSSSB PRT - 15 Nov 2019 - Shift 1]

Q31 C  (Only II)
     — Net: spine D–7–3–4 (col 2); branch A off D; branch B off 4.
       Pairs: {D,3},{7,4},{A,B}.
       Only cube II shows an impossible pair as adjacent faces → only II CANNOT be made.
       [DSSSB PRT - 13 Nov 2019 - Shift 1]

Q32 C  (14)
     — 4×4×4 cube (3 cuts/axis). Red=Top+Bottom (opp), Yellow=Front+Right (adj),
       Green=Back+Left.
       Cubes with ≥1 Red face AND ≥1 Yellow face:
         z=1∩{y=1}: 4; z=1∩{x=4}: 4; corner(z=1,y=1,x=4): −1 → 7 for layer z=1
         z=4∩{y=1}: 4; z=4∩{x=4}: 4; corner(z=4,y=1,x=4): −1 → 7 for layer z=4
         Total = 7+7 = 14.
       [DSSSB PRT - 13 Nov 2019 - Shift 1]

Q33 C  (56)
     — 8 cm cube, 2 cm cuts → 4/edge → 4³=64 total small cubes.
       Interior (no painted face) = (4−2)³ = 8.
       Painted (≥1 face) = 64−8 = 56.
       [KVS PRT - 2018]

Q34 A  (24 cm)
     — Volume of brick = 18×48×16 = 13,824 cm³.
       Edge of cube a: a³=13,824 → a=24 (since 24³=13,824). ✓
       [KVS PRT - 2018]

Q35 C  (Three / 3)
     — Minimum colours for a cube so no two adjacent faces share a colour.
       The face-adjacency graph is the octahedral graph (chromatic number = 3).
       Colour each pair of opposite faces one colour → 3 colours suffice.
       [KVS PRT - 2015]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube and Dice"
SOURCE  = "DSSSB_KVS_Cube_and_Dice"

QUESTIONS = [

    # ── Q26 [DSSSB TGT English (Female) - 14 Sep 2021 - Shift 3] ─────────────
    # Net with symbols @,$,#,&,©,%; spine=@–#–©–%; branches: $ off #, & off ©.
    # Pairs: {@,©},{#,%},{$,&}. Cubes II, III, IV can be formed; cube I cannot.
    {
        "question_number": 26,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "By folding the given paper, which of the following cube can be made?\n"
            "[Net shows six symbols: @, $, #, &, ©, % in a connected layout]"
        ),
        "question_hi": (
            "दिए गए कागज को मोड़कर निम्नलिखित में से कौन सा घन बनाया जा सकता है?\n"
            "[दिए गए जाल में @, $, #, &, ©, % छह प्रतीक हैं]"
        ),
        "image_url": None,
        "option_a": "I, II, III and IV / I, II, III और IV",
        "option_b": "I and II / I और II",
        "option_c": "III and IV / III और IV",
        "option_d": "II, III and IV / II, III और IV",
        "correct_answer": "D",   # Cubes II, III, IV can be formed; I cannot
    },

    # ── Q27 [DSSSB TGT CS - 07 Aug 2021 - Shift 1] ──────────────────────────
    # 4×4×4 = 64 cubes. Each pair of opposite faces: Red / Yellow / Brown.
    # All 8 corner cubes have 3 faces of 3 different colours.
    {
        "question_number": 27,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Pairs of adjacent sides of a big cube are coloured with red, yellow "
            "and brown colour. Now this big cube is divided into 64 small equal "
            "cubes. How many small cubes will have 3 faces painted with different colours?"
        ),
        "question_hi": (
            "एक बड़े घन की दो आसन्न भुजाओं के युग्म लाल, पीले और भूरे रंग से "
            "रंगे गए हैं। अब यह बड़ा घन, 64 छोटे बराबर घनों में विभाजित हो "
            "गया है। कितने छोटे घनों के 3 फलक अलग-अलग रंगों से रंगे होंगे?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "0",
        "option_c": "2",
        "option_d": "6",
        "correct_answer": "A",   # All 8 corner cubes have 3 differently-coloured faces
    },

    # ── Q28 [DSSSB TGT English (Female) - 14 Sep 2021 - Shift 3] ─────────────
    # 3 equal cuts on each axis → 4 sections per axis → 4×4×4 = 64 small cubes.
    {
        "question_number": 28,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            "A cube is taken and 3 equal cuts are made on each of the axis. "
            "How many small cubes will be obtained?"
        ),
        "question_hi": (
            "एक घन लिया जाता है और प्रत्येक अक्ष पर 3 बराबर कट लगाए जाते हैं। "
            "कितने छोटे घन प्राप्त होंगे?"
        ),
        "image_url": None,
        "option_a": "9",
        "option_b": "16",
        "option_c": "64",
        "option_d": "125",
        "correct_answer": "C",   # 3 cuts/axis → 4 sections/axis → 4³ = 64
    },

    # ── Q29 [DSSSB PRT - 14 Nov 2019 - Shift 1] ──────────────────────────────
    # Net with M, K, T, 9, 7, L; pairs: {M,T},{K,9},{7,L}.
    # Cubes I and III satisfy all constraints.
    {
        "question_number": 29,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "By folding the given paper, which of the following cube can be made?\n"
            "[Net shows symbols/numbers: M, K, T, 9, 7, L in a connected layout]"
        ),
        "question_hi": (
            "दिए गए कागज को मोड़कर निम्नलिखित में से कौन सा घन बनाया जा सकता है?\n"
            "[जाल में M, K, T, 9, 7, L प्रतीक/संख्याएँ हैं]"
        ),
        "image_url": None,
        "option_a": "Both I and III / I और III दोनों",
        "option_b": "Only I / केवल I",
        "option_c": "Both II and III / II और III दोनों",
        "option_d": "Only III / केवल III",
        "correct_answer": "A",   # Cubes I and III can be formed
    },

    # ── Q30 [DSSSB PRT - 15 Nov 2019 - Shift 1] ──────────────────────────────
    # Cross net: horizontal spine A–9–8–7; vertical branches 3 (above 8) & C (below 8).
    # Pairs: {A,8},{9,7},{3,C}. Cubes I and III are consistent.
    {
        "question_number": 30,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "When the given paper is folded, which of the following cubes can be formed?\n"
            "[Net: cross shape with numbers A,9,8,7 horizontal and 3,C vertical through 8]"
        ),
        "question_hi": (
            "दिए गए कागज को मोड़ने पर, निम्नलिखित में से कौन सा घन बनाया जा "
            "सकता है?\n[जाल: क्रॉस आकार जिसमें A,9,8,7 क्षैतिज और 3,C ऊर्ध्वाधर हैं]"
        ),
        "image_url": None,
        "option_a": "Only I / केवल I",
        "option_b": "II & III Both / II तथा III दोनों",
        "option_c": "I & III Both / I तथा III दोनों",
        "option_d": "Only IV / केवल IV",
        "correct_answer": "C",   # Cubes I and III can be formed
    },

    # ── Q31 [DSSSB PRT - 13 Nov 2019 - Shift 1] ──────────────────────────────
    # Net: spine D–7–3–4 (col 2); A branches left off D; B branches left off 4.
    # Pairs: {D,3},{7,4},{A,B}. Only cube II shows an impossible adjacent-opposite pair.
    {
        "question_number": 31,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "By folding the given paper, which of the following cubes cannot be made?\n"
            "[Net: A,D top row; 7,3 middle; B,4 bottom row — spine D–7–3–4 with "
            "branches A and B; pairs: {D,3},{7,4},{A,B}]"
        ),
        "question_hi": (
            "दिए गए कागज को मोड़कर निम्नलिखित में से कौन सा घन नहीं बनाया जा सकता है?\n"
            "[जाल: A,D ऊपर; 7,3 बीच में; B,4 नीचे — विपरीत युग्म: {D,3},{7,4},{A,B}]"
        ),
        "image_url": None,
        "option_a": "Both I and II / I और II दोनों",
        "option_b": "Both II and III / II और III दोनों",
        "option_c": "Only II / केवल II",
        "option_d": "Only III / केवल III",
        "correct_answer": "C",   # Only cube II cannot be made
    },

    # ── Q32 [DSSSB PRT - 13 Nov 2019 - Shift 1] ──────────────────────────────
    # Red=Top+Bottom (opp), Yellow=Front+Right (adj), Green=Back+Left.
    # 3 cuts/axis → 4×4×4 = 64 small cubes.
    # Cubes with ≥1 Red AND ≥1 Yellow face:
    #   z=1∩{y=1 or x=4}: 7; z=4∩{y=1 or x=4}: 7. Total = 14.
    {
        "question_number": 32,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "A big solid cube is painted with red colour on two opposite faces, "
            "yellow colour on two adjacent faces and green colour on the remaining "
            "two faces. Now 3 cuts are made on each axis of this cube and then some "
            "small cubes are obtained. How many small cubes will have one face painted "
            "with red colour and one face painted with yellow colour?"
        ),
        "question_hi": (
            "एक बड़े ठोस घन के दो विपरीत फलकों पर लाल रंग, दो आसन्न फलकों पर "
            "पीला रंग तथा शेष दो फलकों पर हरा रंग लगाया गया है। अब इस घन के "
            "प्रत्येक अक्ष पर 3 बराबर कट लगाए जाते हैं तथा कुछ छोटे घन प्राप्त "
            "होते हैं। कितने छोटे घनों के एक फलक पर लाल रंग तथा एक फलक पर "
            "पीला रंग लगा होगा?"
        ),
        "image_url": None,
        "option_a": "20",
        "option_b": "16",
        "option_c": "14",
        "option_d": "12",
        "correct_answer": "C",   # 14 cubes have ≥1 red face AND ≥1 yellow face
    },

    # ── Q33 [KVS PRT - 2018] ─────────────────────────────────────────────────
    # 8 cm cube cut into 2 cm cubes → 4/edge → 64 total.
    # Interior cubes = (4−2)³ = 8. Painted = 64−8 = 56.
    {
        "question_number": 33,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "A cube of side 8 cm is painted red on all the sides. It is then cut "
            "into smaller cubes, each of side 2 cm. How many of these smaller cubes "
            "have one or more sides painted red?"
        ),
        "question_hi": (
            "8 सेमी भुजा वाले एक घन की सभी भुजाओं पर लाल रंग से रंगा गया है। "
            "फिर इसे 2 सेमी भुजा वाले छोटे घनों में काटा गया है। इन छोटे "
            "घनों में से कितनी की एक या अधिक भुजाओं पर लाल रंग से रंगा गया है?"
        ),
        "image_url": None,
        "option_a": "32",
        "option_b": "48",
        "option_c": "56",
        "option_d": "24",
        "correct_answer": "C",   # 64 − 8 (interior) = 56 painted cubes
    },

    # ── Q34 [KVS PRT - 2018] ─────────────────────────────────────────────────
    # Volume = 18×48×16 = 13,824 cm³. Cube edge a: a³ = 13,824 → a = 24 cm.
    {
        "question_number": 34,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "A solid brick of Gold measuring 18 cm × 48 cm × 16 cm is melted and "
            "converted into a cubical shape. An edge of this new shape is equal to:"
        ),
        "question_hi": (
            "18 सेमी × 48 सेमी × 16 सेमी माप वाली सोने की एक ठोस ईंट को "
            "पिघलाकर एक घनाकार आकार में परिवर्तित किया जाता है। इस नए "
            "आकार का एक किनारा बराबर है:"
        ),
        "image_url": None,
        "option_a": "24 cm / 24 सेमी",
        "option_b": "12 cm / 12 सेमी",
        "option_c": "18 cm / 18 सेमी",
        "option_d": "48 cm / 48 सेमी",
        "correct_answer": "A",   # 18×48×16 = 13,824 = 24³ → edge = 24 cm
    },

    # ── Q35 [KVS PRT - 2015] ─────────────────────────────────────────────────
    # Minimum colours for a cube so no adjacent faces share a colour.
    # Chromatic number of face-adjacency (octahedral) graph = 3.
    # Colour each pair of opposite faces one colour → 3 colours suffice.
    {
        "question_number": 35,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            "A cube is to be coloured in such a way as to avoid the same colour on "
            "adjacent surfaces. What is the minimum number of colours you will require?"
        ),
        "question_hi": (
            "एक घन को इस तरह से रंगा जाना चाहिए कि आसन्न सतहों पर एक "
            "ही रंग न हो। आपको न्यूनतम कितने रंगों की आवश्यकता होगी?"
        ),
        "image_url": None,
        "option_a": "Six / छह",
        "option_b": "Four / चार",
        "option_c": "Three / तीन",
        "option_d": "Nine / नौ",
        "correct_answer": "C",   # Minimum 3 colours (one per pair of opposite faces)
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
            if row[0] is not None
        }
        print(f"Topic '{TOPIC}' — existing question_numbers: {len(existing_qnums)}")

        for d in QUESTIONS:
            qn = d["question_number"]
            if qn in existing_qnums:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
