"""
seed_reasoning_statement_assumption_sheet3.py
=============================================
Seeds Statement-Assumption Q12–Q19 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Statement Assumption and Conclusion

Fixed 4-option format — same options for every question:
  (A) Only Assumption I is implicit.
  (B) Only Assumption II is implicit.
  (C) Both I & II are implicit.
  (D) Neither I nor II is implicit.

No 5th option injection needed.

Sources:
  Q12 = CGL Tier-II, 02 Mar 2023, Shift-1
  Q13 = Gagan Pratap Reasoning PDF
  Q14 = NTPC CBT-2, 2021
  Q15 = ALP, 14 Aug 2018, Shift-2
  Q16 = ALP, 13 Aug 2018, Shift-3
  Q17 = ALP, 13 Aug 2018, Shift-3
  Q18 = ALP, 13 Aug 2018, Shift-3
  Q19 = ALP, 10 Aug 2018, Shift-2

Answer key:
  Q12  B — National Expressway-A is widest, used by few; wide road → high speed → accidents.
            Assumption I:   All accidents are caused by excessive speed → NOT implicit ✗
                            (the statement says high speed on a wide road leads to
                            accidents in this context; "ALL accidents everywhere" is an
                            absolute overgeneralisation not embedded in the statement)
            Assumption II:  High speed increases the risk of accident → IMPLICIT ✓
                            (the entire causal chain "wide road → high speed → accidents"
                            directly assumes that higher speed raises accident risk)
            Only Assumption II is implicit.

  Q13  D — Football match: total 5 goals; 3 scored by the left-footed player.
            Assumption I:   Left-footed player was expert in scoring goals → NOT implicit ✗
                            (3 goals in one match is a stated fact; "expert" is a general
                            characterisation that goes beyond a single match performance)
            Assumption II:  60% of Team-Y players are left footed → NOT implicit ✗
                            (completely external statistical information with no connection
                            to the statement about match goals)
            Neither I nor II is implicit.

  Q14  B — Computer education should start at schools itself.
            Assumption I:   Computer education fetches job easily → NOT implicit ✗
                            (employability is one possible reason but not the only or
                            primary assumption behind introducing computers at school;
                            digital literacy, cognitive skill, and future readiness are
                            equally valid reasons not dependent on this assumption)
            Assumption II:  Learning computer is easy → IMPLICIT ✓
                            (recommending that computer education START at school level
                            assumes it is learnable/accessible for school-age children;
                            if it were impossibly difficult at that age, starting at
                            schools would not be recommended)
            Only Assumption II is implicit.

  Q15  D — Akbar said to his queen, 'Birbal is the wisest man in my kingdom.'
            Assumption I:   Akbar is not as wise as Birbal → NOT implicit ✗
                            (kings often speak of their advisors/subjects in superlatives
                            without implying personal inferiority; praising Birbal's wisdom
                            is a compliment, not a self-deprecating comparison)
            Assumption II:  Akbar wants Birbal to become the next king → NOT implicit ✗
                            (acknowledging someone's wisdom is wholly unrelated to any
                            desire for succession; this goes far beyond what the statement
                            implies)
            Neither I nor II is implicit.

  Q16  C — If you're a classical dancer we have an exciting job for you.
            Assumption I:   We need a classical dancer → IMPLICIT ✓
                            (offering a job to classical dancers presupposes the speaker
                            has a requirement/vacancy for one; you cannot offer a job you
                            do not have or need)
            Assumption II:  You are a classical dancer → NOT implicit ✗
                            (the "If you're a classical dancer" clause is a condition
                            addressed to the reader; the statement does NOT assume the
                            reader IS a dancer — it is conditional, not assumed)
            Only Assumption I is implicit.

  Q17  A — This year in the budget section, there was no fund allotment for travel insurance.
            Assumption I:   Travel insurance requires funds → IMPLICIT ✓
                            (the fact that a "fund allotment" for travel insurance is even
                            discussed presupposes that providing/maintaining travel insurance
                            requires financial resources; otherwise no allotment would be
                            relevant)
            Assumption II:  There are many other areas that need more financial attention
                            → NOT implicit ✗
                            (this is one possible REASON for not allotting funds, but it is
                            not embedded in the statement; the non-allotment could be due to
                            budget cuts, low priority, or any other reason)
            Only Assumption I is implicit.

  Q18  B — A flyover has been constructed at 200 crores cost, yet people are not utilising it much.
            Assumption I:   Construction of the flyover is useless → NOT implicit ✗
                            (too absolute; low current utilisation does not mean the flyover
                            is permanently useless; infrastructure often takes time to be
                            adopted; "useless" goes beyond what the statement implies)
            Assumption II:  The time, money and energy spent on the construction of the
                            flyover was wasted → IMPLICIT ✓
                            (the contrast "200 crore cost YET people not utilising it"
                            directly implies the speaker assumes the high investment was
                            not justified by the low utilisation — i.e., it was wasted)
            Only Assumption II is implicit.

  Q19  A — Today is Sunday.
            Assumption I:   Tomorrow is Monday → IMPLICIT ✓
                            (stating "Today is Sunday" presupposes the standard calendar
                            week order; Monday follows Sunday by definition, so this is an
                            embedded factual assumption)
            Assumption II:  Today is a holiday → NOT implicit ✗
                            (Sunday is a holiday in many contexts but not universally;
                            many people work on Sundays; the statement only specifies the
                            day of the week, not its holiday status)
            Only Assumption I is implicit.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Assumption_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Statement Assumption and Conclusion"

# Standard fixed options — same for every question.
_A = "Only Assumption I is implicit. / केवल पूर्वानुमान I अंतर्निहित है।"
_B = "Only Assumption II is implicit. / केवल पूर्वानुमान II अंतर्निहित है।"
_C = "Both I & II are implicit. / I और II दोनों अंतर्निहित हैं।"
_D = "Neither I nor II is implicit. / न तो I और न ही II अंतर्निहित है।"

QUESTIONS = [
    # ── Q12 (CGL Tier-II, 02 Mar 2023, Shift-1) ──────────────────────────────
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": (
            "Statement: National Expressway-A is the widest expressway and is "
            "used by few people. When people get a wide road, then they drive at "
            "high speed, which leads to accidents.\n\n"
            "Assumptions:\n"
            "I.  All accidents are caused by excessive speed.\n"
            "II. High speed increases the risk of accident."
        ),
        "question_hi": (
            "कथन: राष्ट्रीय दुतगामी मार्ग-A सबसे चौड़ी दुतगामी मार्ग है, तथा "
            "कम लोगों द्वारा इसका इस्तेमाल किया जाता है। जब लोगों को चौड़ी और "
            "मोटी सड़क देखने हैं, तब वे तेज गति से वाहन चलाना चाहते हैं, "
            "जिससे दुर्घटनाएं होती हैं।\n\n"
            "पूर्वानुमान:\n"
            "I.  सभी दुर्घटनाएं अत्यधिक गति से वाहन चलाने के कारण होती हैं।\n"
            "II. तेज गति से दुर्घटना का खतरा बढ़ जाता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  "ALL accidents caused by speed" is an absolute claim far beyond the
        #     statement's scope; the statement addresses THIS expressway context
        #     only, not all accidents everywhere → NOT implicit ✗
        # II: The causal chain "wide road → high speed → accidents" directly
        #     assumes that higher speed raises the risk of accidents → IMPLICIT ✓
    },
    # ── Q13 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 13,
        "difficulty": "easy",
        "question_en": (
            "Statement: In a football match between Team-X and Team-Y, the total "
            "number of goals scored was 5, out of which 3 goals were scored by "
            "the left-footed player.\n\n"
            "Assumptions:\n"
            "I.  The left footed player was expert in scoring goals.\n"
            "II. 60% of Team-Y players are left footed."
        ),
        "question_hi": (
            "कथन: टीम-X और टीम-Y के बीच एक फुटबॉल मैच में कुल पाँच (5) गोल किए "
            "गए जिनमें से 3 गोल बाएँ पैर वाले खिलाड़ी द्वारा किए गए थे।\n\n"
            "पूर्वानुमान:\n"
            "I.  बाएँ पैर वाला खिलाड़ी गोल में माहिर था।\n"
            "II. टीम-Y के 60% खिलाड़ी बाएँ पैर वाले हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  Scoring 3/5 goals in one match is a stated fact; "expert in scoring"
        #     is a broad general characterisation requiring consistent performance
        #     — a single match cannot establish expertise → NOT implicit ✗
        # II: The percentage of left-footed players in Team-Y is entirely external
        #     information unconnected to the match goal tally → NOT implicit ✗
    },
    # ── Q14 (NTPC CBT-2, 2021) ────────────────────────────────────────────────
    {
        "question_number": 14,
        "difficulty": "easy",
        "question_en": (
            "Statement: Computer education should start at schools itself.\n\n"
            "Assumptions:\n"
            "I.  Computer education fetches job easily.\n"
            "II. Learning computer is easy."
        ),
        "question_hi": (
            "कथन: कंप्यूटर शिक्षा स्कूलों में ही शुरू होनी चाहिए।\n\n"
            "पूर्वानुमान:\n"
            "I.  कंप्यूटर शिक्षा से आसानी से नौकरी मिल जाती है।\n"
            "II. कंप्यूटर सीखना आसान है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  Job-fetching is one possible benefit but the statement does not
        #     rest on this assumption; digital literacy, cognitive development,
        #     and future readiness justify school computer education independently
        #     → NOT implicit ✗
        # II: Recommending that computers be taught starting at school assumes
        #     school-age children CAN learn it (it is accessible/manageable for
        #     them); if it were impossibly difficult, schools would not be the
        #     starting point → IMPLICIT ✓
    },
    # ── Q15 (ALP, 14 Aug 2018, Shift-2) ──────────────────────────────────────
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": (
            "Statement: Akbar said to his queen, 'Birbal is the wisest man in "
            "my kingdom.'\n\n"
            "Assumptions:\n"
            "I.  Akbar is not as wise as Birbal.\n"
            "II. Akbar wants Birbal to become the next king."
        ),
        "question_hi": (
            "कथन: अकबर ने अपनी रानी से कहा, 'बीरबल मेरे राज्य का सबसे बुद्धिमान "
            "व्यक्ति है।'\n\n"
            "पूर्वानुमान:\n"
            "I.  अकबर बीरबल जितना बुद्धिमान नहीं है।\n"
            "II. अकबर चाहता है कि बीरबल अगला राजा बने।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  A king complimenting a subject's wisdom does not imply the king
        #     is personally less wise; rulers routinely praise advisors in
        #     superlatives without self-comparison → NOT implicit ✗
        # II: Acknowledging someone as the wisest man in the kingdom has no
        #     connection to wanting them to become the next king — an entirely
        #     different political act → NOT implicit ✗
    },
    # ── Q16 (ALP, 13 Aug 2018, Shift-3) ──────────────────────────────────────
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": (
            "Statement: If you're a classical dancer we have an exciting job "
            "for you.\n\n"
            "Assumptions:\n"
            "I.  We need a classical dancer.\n"
            "II. You are a classical dancer."
        ),
        "question_hi": (
            "कथन: यदि आप एक शास्त्रीय नृत्यांगना हैं तो हमारे पास आपके लिए एक "
            "रोमांचक काम है।\n\n"
            "पूर्वानुमान:\n"
            "I.  हमें एक शास्त्रीय नृत्यांगना की आवश्यकता है।\n"
            "II. आप एक शास्त्रीय नृत्यांगना हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Offering "an exciting job for a classical dancer" presupposes there
        #     is a genuine vacancy/need for one; you cannot offer a job that does
        #     not exist → IMPLICIT ✓
        # II: "If you're a classical dancer" is a conditional clause addressed to
        #     the reader; the speaker does NOT assume the reader IS a dancer —
        #     the whole statement is conditional on this being true → NOT implicit ✗
    },
    # ── Q17 (ALP, 13 Aug 2018, Shift-3) ──────────────────────────────────────
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": (
            "Statement: This year in the budget section, there was no fund "
            "allotment for travel insurance.\n\n"
            "Assumptions:\n"
            "I.  Travel insurance requires funds.\n"
            "II. There are many other areas that need more financial attention."
        ),
        "question_hi": (
            "कथन: इस वर्ष बजट अनुभाग में यात्रा बीमा के लिए कोई निधि आवंटन "
            "नहीं किया गया।\n\n"
            "पूर्वानुमान:\n"
            "I.  यात्रा बीमा के लिए धन की आवश्यकता होती है।\n"
            "II. ऐसे कई अन्य क्षेत्र हैं जिन पर अधिक वित्तीय ध्यान देने की "
            "आवश्यकता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Discussing whether funds are allotted for travel insurance assumes
        #     travel insurance requires financial resources; without this, the
        #     mention of fund allotment would be irrelevant → IMPLICIT ✓
        # II: "Other areas need more attention" is one possible reason for not
        #     allotting funds but is not embedded in the statement; the omission
        #     could be due to budget cuts, policy change, or other reasons
        #     → NOT implicit ✗
    },
    # ── Q18 (ALP, 13 Aug 2018, Shift-3) ──────────────────────────────────────
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "Statement: A flyover has been constructed with a whopping cost of "
            "200 crores, yet people are not utilising the flyover much.\n\n"
            "Assumptions:\n"
            "I.  Construction of the flyover is useless.\n"
            "II. The time, money and energy spent on the construction of the "
            "flyover was wasted."
        ),
        "question_hi": (
            "कथन: 200 करोड़ की भारी लागत से फ्लाईओवर का निर्माण किया गया है, "
            "फिर भी लोग फ्लाईओवर का अधिक उपयोग नहीं कर रहे हैं।\n\n"
            "पूर्वानुमान:\n"
            "I.  फ्लाईओवर का निर्माण व्यर्थ है।\n"
            "II. फ्लाईओवर के निर्माण में खर्च किया गया समय, पैसा और ऊर्जा "
            "बर्बाद हो गई।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  "Useless" is too absolute; low utilisation now does not mean the
        #     flyover is permanently useless — people may start using it more over
        #     time → NOT implicit ✗
        # II: The contrast "200 crore cost YET not utilised much" directly implies
        #     the speaker is assuming the massive investment has not yielded
        #     corresponding benefit — i.e., it was wasted → IMPLICIT ✓
    },
    # ── Q19 (ALP, 10 Aug 2018, Shift-2) ──────────────────────────────────────
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": (
            "Statement: Today is Sunday.\n\n"
            "Assumptions:\n"
            "I.  Tomorrow is Monday.\n"
            "II. Today is a holiday."
        ),
        "question_hi": (
            "कथन: आज रविवार है।\n\n"
            "पूर्वानुमान:\n"
            "I.  कल सोमवार है।\n"
            "II. आज छुट्टी है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Stating "today is Sunday" presupposes the standard calendar week
        #     order; Monday always follows Sunday — this is a directly embedded
        #     assumption of the weekly calendar sequence → IMPLICIT ✓
        # II: Sundays are not universally holidays; many people work on Sundays
        #     (healthcare, hospitality, retail, etc.); the statement only specifies
        #     the day of the week, not its holiday status → NOT implicit ✗
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
