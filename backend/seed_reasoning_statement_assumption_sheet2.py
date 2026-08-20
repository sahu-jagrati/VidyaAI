"""
seed_reasoning_statement_assumption_sheet2.py
=============================================
Seeds Statement-Assumption Q6–Q11 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Statement Assumption and Conclusion

Fixed 4-option format — same options for every question:
  (A) Only Assumption I is implicit.
  (B) Only Assumption II is implicit.
  (C) Both I & II are implicit.
  (D) Neither I nor II is implicit.

No 5th option injection needed.

Sources: Gagan Pratap Reasoning PDF; Q10 = CGL Tier-II 06 Mar 2023 Shift-1;
         Q11 = CGL Tier-II 03 Mar 2023 Shift-1.

Answer key:
  Q6   A — Govt appoints Joint Parliamentary Committee to investigate market crash.
            Assumption I:   Members may possess requisite expertise to carry out
                            investigation → IMPLICIT ✓ (forming an investigative
                            committee ASSUMES the members are competent to do the
                            job; otherwise the appointment would be pointless)
            Assumption II:  Responsible people may destroy documents before
                            committee reaches them → NOT implicit ✗ (possible
                            risk/fear, but NOT taken for granted in making the
                            appointment; the committee acts assuming it CAN
                            access evidence, not that it will be destroyed)
            Only Assumption I is implicit.

  Q7   C — Why don't you go to court if employer doesn't pay Provident Fund?
            Assumption I:   Courts can intervene in employer-employee disputes
                            → IMPLICIT ✓ (advising someone to go to court assumes
                            courts HAVE jurisdiction over such disputes; otherwise
                            the advice would be meaningless)
            Assumption II:  It is obligatory for employer to pay PF contribution
                            → IMPLICIT ✓ (advising court action for non-payment
                            assumes the employer is LEGALLY BOUND to pay; without
                            this obligation there would be no legal recourse)
            Both I & II are implicit.

  Q8   A — Weapon inspectors of country X could not detect chemical weapons
           in the custody of country Y.
            Assumption I:   Country X allowed its weapon inspectors to inspect
                            weapons → IMPLICIT ✓ (the fact that X's inspectors
                            conducted the inspection presupposes X deployed/allowed
                            them to do so)
            Assumption II:  Presence of chemical weapons cannot be detected
                            → NOT implicit ✗ (this broad claim directly contradicts
                            the POINT of sending inspectors; the action assumes
                            detection IS possible — otherwise no inspection would
                            be ordered)
            Only Assumption I is implicit.

  Q9   A — It is desirable for a child to enter school at the age of 5.
            Assumption I:   At that age child reaches appropriate level of
                            development and is ready to learn → IMPLICIT ✓
                            (calling age-5 entry "desirable" presupposes children
                            are developmentally ready and able to benefit at 5)
            Assumption II:  Schools do not admit children after age of 6 years
                            → NOT implicit ✗ (too extreme; the statement calls age
                            5 "desirable" but never implies admission becomes
                            impossible after 6; schools admit at various ages)
            Only Assumption I is implicit.

  Q10  A — Many students play mobile games habitually and that is why they
           perform poorly.   [CGL Tier-II, 06 Mar 2023, Shift-1]
            Assumption I:   Many students not paying attention to studies because
                            of mobile games → IMPLICIT ✓ (the causal link "games
                            → poor performance" directly assumes students are
                            neglecting studies in favour of gaming)
            Assumption II:  Mobile games cause students to FAIL in examinations
                            → NOT implicit ✗ ("perform poorly" ≠ "fail"; the
                            statement uses a milder term; assuming outright failure
                            goes beyond what is stated)
            Only Assumption I is implicit.

  Q11  C — Excessive pesticide use contaminates soil and water, leaves residues
           in crops, enters the food chain, and creates a threat to humans.
           [CGL Tier-II, 03 Mar 2023, Shift-1]
            Assumption I:   Excessive pesticide use is not good for people
                            → IMPLICIT ✓ (the entire statement, culminating in
                            "creating a threat to humans", takes for granted that
                            this chain of contamination is harmful to people)
            Assumption II:  Excessive pesticide use can have a bad effect on water
                            → IMPLICIT ✓ (the statement explicitly states
                            "contaminates soil and water"; the author assumes and
                            takes it as a given fact that water is adversely
                            affected — this is the premise of the statement)
            Both I & II are implicit.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Assumption_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Statement Assumption and Conclusion"

# Standard fixed options — same for every question.
_A = "Only Assumption I is implicit. / केवल पूर्वानुमान I अंतर्निहित है।"
_B = "Only Assumption II is implicit. / केवल पूर्वानुमान II अंतर्निहित है।"
_C = "Both I & II are implicit. / I और II दोनों अंतर्निहित हैं।"
_D = "Neither I nor II is implicit. / न तो I और न ही II अंतर्निहित है।"

QUESTIONS = [
    # ── Q6 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            "Statement: The Government of India has appointed a Joint Parliamentary "
            "Committee to investigate the recent market crash.\n\n"
            "Assumptions:\n"
            "I.  The members of the committee may possess requisite expertise to "
            "carry out the investigation.\n"
            "II. The people responsible for the crash may destroy all their "
            "documents before the committee lay their hands on them."
        ),
        "question_hi": (
            "कथन: हाल ही में स्टॉक एक्सचेंज मार्केट में आई जबरदस्त गिरावट की "
            "जांच के लिए भारत सरकार ने एक संयुक्त संसदीय समिति का गठन किया है।\n\n"
            "पूर्वानुमान:\n"
            "I.  समिति के सदस्यों में जांच करने की अपेक्षित विशेषज्ञता हो सकती है।\n"
            "II. इससे पूर्व कि समिति उन दस्तावेजों पर कब्जा करे, हो सकता है उस "
            "गिरावट के लिए जिम्मेदार लोग अपने सभी दस्तावेज नष्ट कर सकते हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  An investigative committee is appointed assuming its members have
        #     the expertise to investigate; competence is the prerequisite for
        #     forming the committee → IMPLICIT ✓
        # II: Document destruction is a possible future risk, NOT a premise
        #     embedded in the act of forming the committee; the committee acts
        #     assuming it CAN access evidence → NOT implicit ✗
    },
    # ── Q7 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": (
            "Statement: Why don't you go to the court if the employer does not "
            "pay you the Provident Fund contribution?\n\n"
            "Assumptions:\n"
            "I.  Courts can intervene in matters of dispute between employer and "
            "employees.\n"
            "II. It is obligatory for the employer to pay the Provident Fund "
            "contribution to the employees."
        ),
        "question_hi": (
            "कथन: यदि आपका नियोक्ता आपको भविष्य निधि का अंशदान नहीं देता है "
            "तो आप अदालत में क्यों नहीं जाते?\n\n"
            "पूर्वानुमान:\n"
            "I.  नियोक्ता और कर्मचारियों में यदि विवाद हो, तब न्यायालय हस्तक्षेप "
            "करते हैं।\n"
            "II. नियोक्ता के लिए कर्मचारियों की भविष्य निधि के अंशदान का भुगतान "
            "करना अनिवार्य है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
        # I:  Advising "go to court" assumes courts HAVE jurisdiction and CAN
        #     intervene in employer-employee PF disputes; without this, the
        #     advice would serve no purpose → IMPLICIT ✓
        # II: Advising court action for non-payment of PF assumes the employer
        #     is LEGALLY OBLIGATED to pay; without this obligation, there is no
        #     legal right to enforce → IMPLICIT ✓
    },
    # ── Q8 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "Statement: Weapon inspectors of country 'X' could not detect the "
            "presence of chemical weapons in the custody of country 'Y'.\n\n"
            "Assumptions:\n"
            "I.  Country 'X' allowed the weapon inspectors to inspect weapons.\n"
            "II. Presence of chemical weapons cannot be detected."
        ),
        "question_hi": (
            "कथन: X देश के हथियार निरीक्षक Y देश के कब्जे में रासायनिक हथियारों "
            "की उपस्थिति का पता नहीं लगा पाये।\n\n"
            "पूर्वानुमान:\n"
            "I.  X देश ने हथियार निरीक्षकों को हथियारों के निरीक्षण की अनुमति दी।\n"
            "II. सामान्यतः हथियारों की उपस्थिति का पता नहीं लगाया जा सकता।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  The inspection by X's inspectors presupposes that country X
        #     authorised/deployed them to carry out the inspection → IMPLICIT ✓
        # II: Claiming chemical weapons "cannot be detected" at all directly
        #     contradicts the purpose of sending inspectors; the action assumes
        #     detection IS achievable — this is not an implicit premise ✗
    },
    # ── Q9 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": (
            "Statement: It is desirable for the child to enter the school at "
            "the age of 5.\n\n"
            "Assumptions:\n"
            "I.  At that age the child reaches the appropriate level of "
            "development and is ready to learn.\n"
            "II. Schools do not admit children after the age of 6 years."
        ),
        "question_hi": (
            "कथन: बालक को 5 वर्ष की आयु में स्कूल में प्रवेश करना उचित है।\n\n"
            "पूर्वानुमान:\n"
            "I.  उस आयु अवस्था पर बालक विकास के उचित स्तर पर पहुँच जाता है और "
            "सीखने के लिए तैयार होता है।\n"
            "II. 6 वर्ष की आयु के पश्चात् बच्चों को विद्यालय में दाखिला नहीं "
            "मिलता।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Calling age-5 school entry "desirable" presupposes the child is
        #     developmentally ready to benefit from schooling at that age;
        #     without this assumption the recommendation has no basis → IMPLICIT ✓
        # II: The statement recommends age 5 as desirable but nowhere implies
        #     admission becomes impossible after 6; schools enrol at various
        #     ages → NOT implicit ✗
    },
    # ── Q10 (CGL Tier-II, 06 Mar 2023, Shift-1) ──────────────────────────────
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": (
            "Statement: Many students have got into the habit of playing mobile "
            "games and that is why they perform poorly.\n\n"
            "Assumptions:\n"
            "I.  Many students are not paying attention to studies because of "
            "mobile games.\n"
            "II. It is because of mobile games that students fail in the "
            "examination."
        ),
        "question_hi": (
            "कथन: कई विद्यार्थियों को मोबाइल गेम खेलने की आदत पड़ गई है और "
            "इसी कारण वे खराब प्रदर्शन करते हैं।\n\n"
            "पूर्वानुमान:\n"
            "I.  कई विद्यार्थी मोबाइल गेम के कारण पढ़ाई पर ध्यान नहीं दे रहे "
            "हैं।\n"
            "II. मोबाइल गेम के कारण ही विद्यार्थी परीक्षा में अनुत्तीर्ण होते "
            "हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  "Games → poor performance" directly assumes students are neglecting
        #     their studies in favour of gaming; this is embedded in the causal
        #     claim → IMPLICIT ✓
        # II: The statement says students "perform poorly" — NOT that they "fail".
        #     Failure is a stronger claim that goes beyond the stated consequence;
        #     poor performance ≠ examination failure → NOT implicit ✗
    },
    # ── Q11 (CGL Tier-II, 03 Mar 2023, Shift-1) ──────────────────────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": (
            "Statement: Excessive use of pesticides in agricultural production "
            "contaminates soil and water, residues in crops and eventually enter "
            "the food chain, creating a threat to humans.\n\n"
            "Assumptions:\n"
            "I.  Excessive use of pesticides in agricultural production is not "
            "good for the people.\n"
            "II. Excessive use of pesticides in agricultural production can have "
            "a bad effect on water."
        ),
        "question_hi": (
            "कथन: कृषि उत्पादन में कीटनाशकों का अत्यधिक उपयोग करने से मिट्टी "
            "और जल दूषित होते हैं, फसलों में इसका अवशेष रह जाता है जो अंततः "
            "खाद्य श्रृंखला में प्रवेश करता है, जिससे मानवों के लिए खतरा पैदा "
            "हो जाता है।\n\n"
            "पूर्वानुमान:\n"
            "I.  कृषि उत्पादन में कीटनाशकों का अत्यधिक उपयोग किया जाना लोगों "
            "के लिए अच्छा नहीं है।\n"
            "II. कृषि उत्पादन में कीटनाशकों का अत्यधिक उपयोग पानी पर बुरा प्रभाव "
            "डाल सकता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
        # I:  The entire chain — soil contamination → water contamination →
        #     food-chain residues → threat to humans — presupposes the process
        #     is harmful to people; the author takes this as given → IMPLICIT ✓
        # II: The statement explicitly states pesticides "contaminate soil and
        #     water"; the author takes it as a given premise that water is
        #     adversely affected — this assumed fact supports the conclusion
        #     → IMPLICIT ✓
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
