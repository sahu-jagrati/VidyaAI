"""
seed_reasoning_statement_assumption_sheet6.py
=============================================
Seeds Statement-Conclusion Q35–Q42 from Gagan Pratap Reasoning PDFs (Sheet 6).
Subject : Reasoning
Topic   : Statement Assumption and Conclusion

All questions use the CONCLUSION format (5 options).
Options A–D stored in DB; option E injected by frontend (SAC_CONCLUSION_E)
because option_a starts with "Only I follows".

  (A) Only I follows.
  (B) Only II follows.
  (C) Both I & II follow.
  (D) Neither I nor II follows.
  (E) Either I or II follows.  ← injected by frontend; never correct for Q35–Q42.

Sources:
  Q35 = Gagan Pratap Reasoning PDF
  Q36 = Gagan Pratap Reasoning PDF
  Q37 = Gagan Pratap Reasoning PDF
  Q38 = CHSL Tier-II, 26 Jun 2023, Shift-1
  Q39 = CHSL Tier-II, 26 Jun 2023, Shift-1
  Q40 = CHSL Tier-II, 06 Mar 2023, Shift-1
  Q41 = CHSL, 03 Jun 2022, Shift-3
  Q42 = UPSI, 02 Dec 2021, Shift-1

Answer key:

  Q35  A — No country is absolutely self-dependent these days.
            Conclusion I:   It is impossible to grow and produce all that a country
                            needs → FOLLOWS ✓ (if no country is self-dependent, it
                            implies full self-sufficiency is not achievable — i.e.,
                            impossible — since otherwise at least one country would
                            be self-dependent)
            Conclusion II:  Countrymen in general have become lazy → DOES NOT FOLLOW ✗
                            (laziness has no logical connection to economic
                            interdependence; countries are interdependent due to
                            specialisation, trade advantages, and resource distribution
                            — not because people are lazy)
            Only I follows.

  Q36  B — Most Indians know they have a great heritage, but few include science in this.
            Conclusion I:   Many Indians believe science has made Indian heritage great
                            → DOES NOT FOLLOW ✗ (if many believed science MADE heritage
                            great, they would INCLUDE science in their concept of
                            heritage; but the statement says FEW include science —
                            Conclusion I contradicts the statement)
            Conclusion II:  Many Indians do not know India has a great scientific
                            heritage → FOLLOWS ✓ ("few include science" in great
                            heritage directly implies that the majority are unaware
                            of India's scientific heritage component)
            Only II follows.

  Q37  C — All members of a golf club are active golfers, and they are all rich.
           Ms. L is also a member.
            Conclusion I:   She is a golfer → FOLLOWS ✓
                            (All members → active golfers; Ms. L → member;
                            ∴ Ms. L → active golfer — valid syllogism)
            Conclusion II:  She is rich → FOLLOWS ✓
                            (All members → rich; Ms. L → member;
                            ∴ Ms. L → rich — valid syllogism)
            Both I & II follow.

  Q38  B — India's largest lender bank announced it will allow customers to
           exchange Rs. 2000 notes.  [CHSL Tier-II, 26 Jun 2023, Shift-1]
            Conclusion I:   No one will be allowed to WITHDRAW more than Rs. 20,000
                            → DOES NOT FOLLOW ✗ (the statement is about NOTE EXCHANGE,
                            not withdrawal; withdrawal and exchange are distinct banking
                            operations; no information about withdrawal limits is given)
            Conclusion II:  No requisition slip is required for exchange of up to
                            Rs. 20,000 → FOLLOWS ✓ (based on the 2023 RBI Rs. 2000
                            note exchange policy: the bank's announcement covers
                            exchange specifically, and the actual policy stipulates no
                            requisition slip for exchange up to Rs. 20,000 — directly
                            related to the exchange process mentioned in the statement)
            Only II follows.

  Q39  D — New government policy aims to reduce carbon emissions by 50% within
           the next decade.  [CHSL Tier-II, 26 Jun 2023, Shift-1]
            Conclusion I:   Government will ban ALL vehicles on fossil fuel IMMEDIATELY
                            → DOES NOT FOLLOW ✗ (the policy targets 50% reduction over
                            a DECADE — gradual, not immediate; an immediate ban on ALL
                            fossil fuel vehicles is far more extreme than the stated goal)
            Conclusion II:  Government will shut down ALL coal-fired power plants
                            → DOES NOT FOLLOW ✗ (50% carbon reduction over 10 years
                            does not imply shutting down ALL coal plants; it could be
                            achieved through a mix of measures including efficiency
                            improvements, renewables, and partial coal reduction)
            Neither I nor II follows.

  Q40  A — Since past 15 years, 75% of world pottery market comes from Country K.
           However, employment in Country K's pottery industry has been declining
           5-9% annually for the past 3 years.  [CHSL Tier-II, 06 Mar 2023, Shift-1]
            Conclusion I:   Even after declining employment, Country K has enough
                            potters to continue contributing equally to the
                            international market → FOLLOWS ✓ (the 75% market share
                            has been maintained for 15 years INCLUDING the 3 years of
                            employment decline; Country K evidently continues to
                            supply 75% of world pottery despite declining employment,
                            proving sufficient capacity remains)
            Conclusion II:  Local demand of pottery in Country K has substantially
                            decreased leading to less interest among potters
                            → DOES NOT FOLLOW ✗ (this is one hypothetical reason for
                            employment decline, but the statement gives no information
                            about local demand; employment could have declined due to
                            automation, wages, or other unrelated factors)
            Only I follows.

  Q41  A — Private school teachers are hard-working.  [CHSL, 03 Jun 2022, Shift-3]
            Conclusion I:   Some hard-working workers are private school teachers
                            → FOLLOWS ✓ (valid logical conversion: "All A → B" converts
                            to "Some B → A" by limitation; i.e., "All private school
                            teachers are hardworking" → "Some hardworking workers are
                            private school teachers")
            Conclusion II:  All people are not hardworking → DOES NOT FOLLOW ✗
                            (the statement describes private school teachers only;
                            it says nothing about whether all people in general are
                            hardworking or not — this is an unrelated inference)
            Only I follows.

  Q42  D — Every Australian speaks 6 languages. Anthony speaks 6 languages.
           [UPSI, 02 Dec 2021, Shift-1]
            Conclusion I:   Anthony is an Australian → DOES NOT FOLLOW ✗
                            (classic syllogism fallacy — affirming the consequent:
                            All Australians→6 languages; Anthony→6 languages;
                            does NOT prove Anthony is Australian; people from other
                            countries may also speak 6 languages)
            Conclusion II:  People from other countries do not speak 6 languages
                            → DOES NOT FOLLOW ✗ (the statement says every Australian
                            speaks 6 languages; it says nothing about whether people
                            from other countries can or cannot speak 6 languages)
            Neither I nor II follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Assumption_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Statement Assumption and Conclusion"

# Conclusion format — 5-option (option E injected by frontend when option_a
# starts with "Only I follows").
_A = "Only I follows. / केवल I अनुसरण करता है।"
_B = "Only II follows. / केवल II अनुसरण करता है।"
_C = "Both I & II follow. / I और II दोनों अनुसरण करते हैं।"
_D = "Neither I nor II follows. / न तो I और न ही II अनुसरण करता है।"
# _E = "Either I or II follows." ← injected by frontend as SAC_CONCLUSION_E

QUESTIONS = [
    # ── Q35 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": (
            "Statement: No country is absolutely self-dependent these days.\n\n"
            "Conclusions:\n"
            "I.  It is impossible to grow and produce all that a country needs.\n"
            "II. Countrymen in general have become lazy."
        ),
        "question_hi": (
            "कथन: कोई भी देश इन दिनों बिल्कुल आत्म-निर्भर नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  किसी देश की आवश्यकताओं के लिए सब विकसित करना और उत्पादन करना "
            "असंभव है।\n"
            "II. सामान्य रूप से देशवासी आलसी हो गए हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  If no country achieves self-dependence, it implies full self-sufficiency
        #     is impossible (otherwise at least one country would achieve it) ✓
        # II: Economic interdependence arises from specialisation, comparative
        #     advantage, and resource distribution — not from laziness ✗
    },
    # ── Q36 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 36,
        "difficulty": "medium",
        "question_en": (
            "Statement: Most Indians know that they have a great heritage, but "
            "few include science in this.\n\n"
            "Conclusions:\n"
            "I.  Many Indians believe that science has made Indian heritage great.\n"
            "II. Many Indians do not know that India has a great scientific heritage."
        ),
        "question_hi": (
            "कथन: अधिकांश भारतीय जानते हैं कि उनके पास एक महान विरासत है, किंतु "
            "कुछ इसमें विज्ञान को शामिल करते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कई भारतीय मानते हैं कि विज्ञान ने भारतीय विरासत को महान बनाया है।\n"
            "II. कई भारतीय नहीं जानते कि भारत के पास एक महान वैज्ञानिक विरासत है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  If many believed science made heritage great, they WOULD include
        #     science in it — but the statement says FEW include science; I
        #     effectively contradicts the statement ✗
        # II: "Few include science in great heritage" → majority unaware of India's
        #     scientific heritage component → FOLLOWS ✓
    },
    # ── Q37 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 37,
        "difficulty": "easy",
        "question_en": (
            "Statement: All the members of a golf club are active golfers, but "
            "they are all rich. Ms. L is also a member.\n\n"
            "Conclusions:\n"
            "I.  She is a golfer.\n"
            "II. She is rich."
        ),
        "question_hi": (
            "कथन: एक गोल्फ क्लब के सभी सदस्य सक्रियतापूर्वक गोल्फ खेलते हैं, "
            "परन्तु वे सभी धनवान हैं। श्रीमती L भी सदस्य हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  वह एक गोल्फ खिलाड़ी हैं।\n"
            "II. वह धनी हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
        # I:  All members → active golfers; Ms. L → member; ∴ Ms. L → golfer ✓
        # II: All members → rich; Ms. L → member; ∴ Ms. L → rich ✓
        # Both are valid syllogistic deductions from the given premises.
    },
    # ── Q38 (CHSL Tier-II, 26 Jun 2023, Shift-1) ─────────────────────────────
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": (
            "Statement: India's largest lender bank has announced that it will be "
            "allowing customers to exchange Rs. 2000 notes.\n\n"
            "Conclusions:\n"
            "I.  No one will be allowed to withdraw an amount of more than "
            "Rs. 20,000.\n"
            "II. No requisition slip is required for exchange of up to Rs. 20,000."
        ),
        "question_hi": (
            "कथन: भारत के सबसे बड़े ऋणदाता बैंक ने घोषणा की है कि वह ग्राहकों को "
            "2000 रु. के नोट बदलने की अनुमति देगा।\n\n"
            "निष्कर्ष:\n"
            "I.  किसी को भी रु. 20,000 से अधिक की राशि निकालने की अनुमति नहीं "
            "दी जाएगी।\n"
            "II. रु. 20,000 तक के विनिमय के लिए किसी भी पर्ची की आवश्यकता नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  Statement is about NOTE EXCHANGE; conclusion I is about WITHDRAWAL —
        #     a completely different banking operation; unrelated ✗
        # II: Conclusion relates to the same exchange operation in the statement;
        #     per the 2023 RBI Rs. 2000 note exchange policy, no requisition slip
        #     was required for exchanges up to Rs. 20,000 ✓
    },
    # ── Q39 (CHSL Tier-II, 26 Jun 2023, Shift-1) ─────────────────────────────
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": (
            "Statement: The new government policy aims to reduce carbon emissions "
            "by 50% within the next decade.\n\n"
            "Conclusions:\n"
            "I.  The government will ban all vehicles that run on fossil fuel "
            "immediately.\n"
            "II. The government will shut down all the coal-fired power plants."
        ),
        "question_hi": (
            "कथन: नई सरकारी नीति का लक्ष्य अगले दशक के भीतर कार्बन उत्सर्जन को "
            "50% तक कम करना है।\n\n"
            "निष्कर्ष:\n"
            "I.  सरकार जीवाश्म ईंधन से चलने वाले सभी वाहनों पर तुरंत प्रतिबंध "
            "लगाएगी।\n"
            "II. सरकार कोयले से चलने वाली सभी विद्युत संयंत्रों को बंद कर देगी।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  Policy is gradual (50% over a DECADE); "IMMEDIATELY ban ALL vehicles"
        #     is extreme and contradicts the decade-long timeline ✗
        # II: 50% carbon reduction ≠ shutting down ALL coal plants; many partial
        #     or mixed measures could achieve the same goal ✗
    },
    # ── Q40 (CHSL Tier-II, 06 Mar 2023, Shift-1) ─────────────────────────────
    {
        "question_number": 40,
        "difficulty": "hard",
        "question_en": (
            "Statement: Since the past 15 years, 75% of the products in the "
            "world's pottery market come from Country K. However, the employment "
            "in the pottery industry of Country K has been consistently declining "
            "by 5-9% every year since the past 3 years.\n\n"
            "Conclusions:\n"
            "I.  Even after declining employment, Country K has enough potters to "
            "continue contributing equally to the international market.\n"
            "II. The local demand of pottery in Country K has substantially "
            "decreased leading to less interest among potters."
        ),
        "question_hi": (
            "कथन: पिछले 15 वर्षों से, दुनिया के मिट्टी के बर्तन बाजार में 75% "
            "उत्पाद देश K से आते हैं। हालांकि, देश K में मिट्टी के बर्तन उद्योग में "
            "रोजगार पिछले 3 वर्षों से हर साल 5-9% की दर से घट रहा है।\n\n"
            "निष्कर्ष:\n"
            "I.  रोजगार में गिरावट के बाद भी, देश K के पास अंतर्राष्ट्रीय बाजार में "
            "समान रूप से योगदान जारी रखने के लिए पर्याप्त कुम्हार हैं।\n"
            "II. देश K में मिट्टी के बर्तनों की स्थानीय मांग में काफी कमी आई है "
            "जिससे कुम्हारों के बीच कम रुचि हो गई है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  The 15-year 75% market dominance INCLUDES the 3 years of employment
        #     decline; Country K evidently maintains its market share despite the
        #     decline, proving enough potters remain to sustain output ✓
        # II: "Local demand decreased" is one hypothetical reason for declining
        #     employment; the statement provides no information about local demand;
        #     automation, wages, migration, or other factors could also explain
        #     the employment decline ✗
    },
    # ── Q41 (CHSL, 03 Jun 2022, Shift-3) ─────────────────────────────────────
    {
        "question_number": 41,
        "difficulty": "easy",
        "question_en": (
            "Statement: Private school teachers are hard-working.\n\n"
            "Conclusions:\n"
            "I.  Some hard-working workers are private school teachers.\n"
            "II. All people are not hardworking."
        ),
        "question_hi": (
            "कथन: निजी विद्यालय के शिक्षक मेहनती होते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ मेहनती शिक्षक निजी विद्यालय के शिक्षक हैं।\n"
            "II. सभी कर्मचारी मेहनती नहीं होते हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Valid A→I conversion: "All private school teachers → hardworking"
        #     converts to "Some hardworking workers → private school teachers" ✓
        # II: The statement is about private school teachers only; it provides no
        #     basis to conclude that ALL people in general are not hardworking ✗
    },
    # ── Q42 (UPSI, 02 Dec 2021, Shift-1) ─────────────────────────────────────
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": (
            "Statement: Every Australian speaks 6 languages. Anthony speaks "
            "6 languages.\n\n"
            "Conclusions:\n"
            "I.  Anthony is an Australian.\n"
            "II. People from other countries do not speak 6 languages."
        ),
        "question_hi": (
            "कथन: प्रत्येक ऑस्ट्रेलियाई 6 भाषाएँ बोलता है। एंटनी 6 भाषाएँ "
            "बोलते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  एंटनी एक ऑस्ट्रेलियाई है।\n"
            "II. दूसरे देशों के लोग 6 भाषाएँ नहीं बोलते हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  Affirming the consequent fallacy: All Australians→6 languages;
        #     Anthony→6 languages; does NOT prove Anthony is Australian;
        #     people from other countries may also speak 6 languages ✗
        # II: Statement says every Australian speaks 6 languages; it is silent
        #     on whether non-Australians can or cannot speak 6 languages ✗
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
