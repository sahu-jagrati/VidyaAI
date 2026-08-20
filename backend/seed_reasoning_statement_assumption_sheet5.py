"""
seed_reasoning_statement_assumption_sheet5.py
=============================================
Seeds Statement-Conclusion Q28–Q34 from Gagan Pratap Reasoning PDFs (Sheet 5).
Subject : Reasoning
Topic   : Statement Assumption and Conclusion

All questions use the CONCLUSION format (5 options).
Options A–D stored in DB; option E injected by frontend (SAC_CONCLUSION_E)
because option_a starts with "Only I follows".

  (A) Only I follows.
  (B) Only II follows.
  (C) Both I & II follow.
  (D) Neither I nor II follows.
  (E) Either I or II follows.  ← injected by frontend; never correct here.

Answer key:

  Q28  A — Cabinet of State X tackles milk glut (cooperatives & dairies failed
           to use available milk).
            Conclusion I:   Milk production of State X is more than its need
                            → FOLLOWS ✓ (a "glut" is by definition excess supply
                            over demand; the cabinet tackling a milk glut directly
                            implies production exceeds requirement)
            Conclusion II:  Govt & co-operative dairies not equipped in resources
                            & technology to handle excess milk → DOES NOT FOLLOW ✗
                            (the statement says they "failed to use" the available
                            milk, but the reason could be demand shortage, pricing,
                            storage, distribution, etc.; "not equipped in resources
                            & technology" is one specific reason, not established
                            by the statement)
            Only I follows.

  Q29  D — The manager humiliated Sachin in the presence of his colleagues.
            Conclusion I:   The manager did not like Sachin → DOES NOT FOLLOW ✗
                            (a manager can humiliate an employee as a disciplinary
                            measure, for performance reasons, or under peer pressure
                            — not necessarily due to personal dislike)
            Conclusion II:  Sachin was not popular with his colleagues → DOES NOT FOLLOW ✗
                            (the statement says nothing about Sachin's relationship
                            with his colleagues; their presence during the humiliation
                            reveals nothing about his popularity among them)
            Neither I nor II follows.

  Q30  C — The Government of country X has recently announced several concessions
           & offered attractive package tours for foreign visitors.
            Conclusion I:   More foreign visitors will now visit the country
                            → FOLLOWS ✓ (the government's actions — concessions and
                            attractive packages — are specifically designed to increase
                            foreign tourist arrivals; it is a logical consequence that
                            such measures will draw more visitors)
            Conclusion II:  The Government of country X seems serious in attracting
                            tourists → FOLLOWS ✓ (announcing concessions AND creating
                            attractive package tours are active, purposeful steps;
                            these actions directly demonstrate the government's
                            seriousness in promoting tourism)
            Both I & II follow.

  Q31  C — Only good singers are invited in the conference. No one without a
           sweet voice is a good singer.
            [Deductive chain: invited → good singer → has sweet voice]
            Conclusion I:   All invited singers in the conference have sweet voice
                            → FOLLOWS ✓ (invited → good singer [P1]; good singer →
                            sweet voice [P2]; ∴ invited → sweet voice — valid syllogism)
            Conclusion II:  Singers without sweet voice are not invited → FOLLOWS ✓
                            (contrapositive chain: no sweet voice → not good singer
                            [P2-contra] → not invited [P1-contra]; logically valid)
            Both I & II follow.

  Q32  D — Those who undertake physical exercise ≥30 min/day are less prone to
           heart ailments (recent survey report).
            Conclusion I:   Moderate physical exercise is necessary for leading a
                            healthy life → DOES NOT FOLLOW ✗ (the statement says
                            exercise reduces heart ailment risk; "necessary for a
                            healthy life" is broader than this single finding;
                            "necessary" is too absolute — other factors also
                            contribute to health)
            Conclusion II:  All people with desk-bound jobs definitely suffer from
                            heart ailments → DOES NOT FOLLOW ✗ (far too absolute;
                            the statement says exercisers are LESS PRONE — it does
                            not say non-exercisers DEFINITELY suffer; many desk-bound
                            workers remain heart-ailment-free)
            Neither I nor II follows.

  Q33  C — This world is neither good nor evil; each man manufactures a world
           for himself.
            Conclusion I:   Some people find this world quite good → FOLLOWS ✓
                            ("each man manufactures a world for himself" implies
                            different people build different worlds; some will
                            naturally create a positive/good world for themselves)
            Conclusion II:  Some people find this world quite bad → FOLLOWS ✓
                            (equally, some will create a negative/bad world for
                            themselves; both outcomes are implied by the statement
                            that each person's world is self-constructed)
            Both I & II follow.

  Q34  B — Double your money in five months — An advertisement.
            Conclusion I:   The assurance is not genuine → DOES NOT FOLLOW ✗
                            (the statement does not provide evidence that the claim
                            is fraudulent; concluding it is "not genuine" requires
                            an external judgment about what returns are realistic,
                            which goes beyond the information given)
            Conclusion II:  People want their money to grow → FOLLOWS ✓
                            (the advertisement targets people interested in growing
                            their money; such an ad is placed because people desire
                            financial growth — this is the premise behind its existence)
            Only II follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Assumption_Sheet5"
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
    # ── Q28 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            "Statement: The Cabinet of State X took certain steps to tackle the "
            "milk glut in the state as the cooperatives & government dairies "
            "failed to use the available milk - A news report.\n\n"
            "Conclusions:\n"
            "I.  The milk production of state X is more than its need.\n"
            "II. The Government & co-operative dairies in state X are not equipped "
            "in terms of resources & technology to handle such excess milk."
        ),
        "question_hi": (
            "कथन: राज्य में दूध की अधिकता से निपटने के लिए राज्य X के कैबिनेट ने "
            "कुछ कदम उठाए क्योंकि सहकारी समितियाँ और सरकारी डेयरियाँ उपलब्ध दूध "
            "का उपयोग करने में विफल रही थीं — एक समाचार विवरण।\n\n"
            "निष्कर्ष:\n"
            "I.  राज्य X का दूध उत्पादन उसकी आवश्यकता से अधिक है।\n"
            "II. राज्य X की सरकारी और सहकारी डेयरियाँ इस तरह के अतिरिक्त दूध को "
            "संभालने के लिए संसाधनों और प्रौद्योगिकी के मामले में सुसज्जित नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  "Glut" = excess supply; taking steps to tackle a milk glut directly
        #     proves production > requirement → FOLLOWS ✓
        # II: Dairies "failed to use" milk — possible reasons are many (demand,
        #     pricing, storage, distribution); "not equipped in resources & technology"
        #     is one specific unverified reason → DOES NOT FOLLOW ✗
    },
    # ── Q29 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": (
            "Statement: The manager humiliated Sachin in the presence of his "
            "colleagues.\n\n"
            "Conclusions:\n"
            "I.  The manager did not like Sachin.\n"
            "II. Sachin was not popular among his colleagues."
        ),
        "question_hi": (
            "कथन: प्रबंधक ने अपने सहकर्मियों की उपस्थिति में सचिन को अपमानित किया।\n\n"
            "निष्कर्ष:\n"
            "I.  प्रबंधक सचिन को पसंद नहीं था।\n"
            "II. सचिन अपने सहकर्मियों के साथ लोकप्रिय नहीं था।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  Humiliation may be disciplinary or performance-related, not
        #     necessarily rooted in personal dislike → DOES NOT FOLLOW ✗
        # II: Statement says nothing about Sachin's relationship with or
        #     popularity among his colleagues → DOES NOT FOLLOW ✗
    },
    # ── Q30 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "Statement: The Government of country X has recently announced several "
            "concessions & offered attractive package tours for foreign visitors.\n\n"
            "Conclusions:\n"
            "I.  Now, more number of foreign visitors will visit the country.\n"
            "II. The Government of country X seems to be serious in attracting "
            "tourists."
        ),
        "question_hi": (
            "कथन: देश X की सरकार ने हाल ही में कई रियायतों की घोषणा की है और "
            "विदेशी पर्यटकों के लिए आकर्षक पैकेज टूर की पेशकश की है।\n\n"
            "निष्कर्ष:\n"
            "I.  अब, अधिक संख्या में विदेशी पर्यटक देश का दौरा करेंगे।\n"
            "II. X देश की सरकार पर्यटकों को आकर्षित करने में गंभीर प्रतीत होती है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
        # I:  Concessions + attractive packages are specifically designed to
        #     increase tourist arrivals; logical consequence is more visitors ✓
        # II: Announcing concessions AND offering packages are active, purposeful
        #     measures that directly demonstrate seriousness in tourism promotion ✓
    },
    # ── Q31 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            "Statement: Only good singers are invited in the conference. No one "
            "without a sweet voice is a good singer.\n\n"
            "Conclusions:\n"
            "I.  All invited singers in the conference have sweet voice.\n"
            "II. Those singers who do not have sweet voice are not invited in "
            "the conference."
        ),
        "question_hi": (
            "कथन: सम्मेलन में केवल अच्छे गायक ही आमंत्रित हैं। मीठी आवाज के बिना "
            "कोई भी अच्छा गायक नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  सम्मेलन में आमंत्रित सभी गायकों की मधुर आवाज है।\n"
            "II. जिन गायकों की मधुर आवाज नहीं होती है उन्हें सम्मेलन में आमंत्रित "
            "नहीं किया जाता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
        # Deductive chain: Premise 1 → invited ∴ good singer
        #                  Premise 2 → good singer ∴ sweet voice
        #                  Combined  → invited ∴ sweet voice
        # I:  All invited singers have sweet voice — valid syllogism ✓
        # II: No sweet voice → not good singer → not invited (contrapositive chain) ✓
    },
    # ── Q32 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": (
            "Statement: In a recent survey report, it has been stated that those "
            "who undertake physical exercise for at least half an hour a day are "
            "less prone to have any heart ailments.\n\n"
            "Conclusions:\n"
            "I.  Moderate level of physical exercise is necessary for leading a "
            "healthy life.\n"
            "II. All people who do desk-bound jobs definitely suffer from heart "
            "ailments."
        ),
        "question_hi": (
            "कथन: एक हालिया सर्वेक्षण रिपोर्ट में, यह कहा गया है कि जो लोग "
            "प्रतिदिन कम से कम आधे घंटे शारीरिक व्यायाम करते हैं, उन्हें दिल की "
            "बीमारियाँ होने का खतरा कम होता है।\n\n"
            "निष्कर्ष:\n"
            "I.  स्वस्थ जीवन जीने के लिए शारीरिक व्यायाम का मध्यम स्तर आवश्यक है।\n"
            "II. डेस्क-बाउंड जॉब करने वाले सभी लोग निश्चित रूप से दिल की "
            "बीमारियों से पीड़ित हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  Exercise reduces heart risk but "necessary for healthy life" is too
        #     broad — health depends on many factors; "necessary" is too absolute ✗
        # II: Statement says exercisers are LESS PRONE, not that non-exercisers
        #     DEFINITELY suffer; "definitely suffer" is far too absolute ✗
    },
    # ── Q33 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": (
            "Statement: This world is neither good nor evil; each man manufactures "
            "a world for himself.\n\n"
            "Conclusions:\n"
            "I.  Some people find this world quite good.\n"
            "II. Some people find this world quite bad."
        ),
        "question_hi": (
            "कथन: यह दुनिया न अच्छी है और न ही बुरी है; प्रत्येक व्यक्ति अपने लिए "
            "एक दुनिया बनाता है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ लोगों को यह दुनिया काफी अच्छी लगती है।\n"
            "II. कुछ लोगों को यह दुनिया काफी बुरी लगती है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
        # "Each man manufactures his own world" implies different people create
        # different worlds for themselves.
        # I:  Some will create/perceive a good world for themselves → FOLLOWS ✓
        # II: Some will create/perceive a bad world for themselves → FOLLOWS ✓
    },
    # ── Q34 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 34,
        "difficulty": "medium",
        "question_en": (
            "Statement: Double your money in five months - An advertisement.\n\n"
            "Conclusions:\n"
            "I.  The assurance is not genuine.\n"
            "II. People want their money to grow."
        ),
        "question_hi": (
            "कथन: पाँच महीनों में अपना पैसा दोगुना करें - एक विज्ञापन।\n\n"
            "निष्कर्ष:\n"
            "I.  आश्वासन वास्तविक नहीं है।\n"
            "II. लोग चाहते हैं कि उनका पैसा बढ़े।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  Concluding the assurance is "not genuine" requires judging the claim's
        #     validity from outside the statement; no evidence of fraud is given
        #     → DOES NOT FOLLOW ✗
        # II: The advertisement exists because people desire financial growth;
        #     such an ad would not be placed if people did not want money to grow
        #     → FOLLOWS ✓
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
