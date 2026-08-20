"""
seed_reasoning_assumptions_sheet4.py
=========================================
Seeds Assumptions Q11-Q15 from Gagan Pratap Reasoning PDFs (Sheet 4).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet4.py

Answer key (solutions verified):
  Q11  Statement: Many students have got into the habit of playing mobile games and
       that is why they perform poorly.
       I)  Many students are not paying attention to studies because of mobile games
           → IMPLICIT (mobile games causing poor performance implies distraction from
           study is the mechanism)
       II) It is because of mobile games that students fail in the examination
           → NOT IMPLICIT ("perform poorly" ≠ "fail"; and "ही" (only) in Hindi
           makes it too extreme — the statement does not go so far as to say failure)
       Answer: A  (Only I is implicit)

  Q12  Statement: Excessive use of pesticides in agricultural production contaminates
       soil and water, residues in crops and eventually enter the food chain, creating
       a threat to humans.
       I)  Excessive use of pesticides in agricultural production is not good for the
           people → IMPLICIT (the entire causal chain in the statement leads to
           a threat to humans → harmful to people is directly implied)
       II) Excessive use of pesticides in agricultural production can have a bad
           effect on water → IMPLICIT (the statement explicitly mentions contamination
           of water as one of the consequences)
       Answer: C  (Both I & II are implicit)

  Q13  Statement: National Expressway-A is the widest expressway and is used by few
       people. When people see a wide road, they drive at high speed, which leads to
       accidents.
       I)  All accidents are caused by excessive speed → NOT IMPLICIT
           (the statement says high speed on wide roads leads to accidents, not that
            ALL accidents everywhere are from speed — overgeneralisation)
       II) High speed increases the risk of accident → IMPLICIT
           (the statement explicitly states that high speed "leads to accidents",
            directly implying higher risk)
       Answer: B  (Only II is implicit)

  Q14  Statement: In a football match between Team-X and Team-Y, the total number of
       goals scored by Team-Y was 5, out of which 3 goals were scored by the
       left-footed player.
       I)  The left-footed player was expert in scoring goals → IMPLICIT
           (scoring 3 out of 5 team goals implies the player was skilled/expert at
            scoring; the statement rests on this assumption)
       II) 60% of Team-Y players are left footed → NOT IMPLICIT
           (goals scored ≠ proportion of left-footed players in the team;
            this cannot be inferred from the percentage of goals alone)
       Answer: A  (Only I is implicit)

  Q15  Statement: Computer education should start at schools itself.
       I)  Computer education fetches job easily → NOT IMPLICIT
           (job outcomes are not the stated reason for starting computer education
            at school; this is an indirect/speculative benefit)
       II) Learning computer is easy → NOT IMPLICIT
           (schools teaching computers doesn't imply computers are easy to learn;
            the statement says nothing about the difficulty of the subject)
       Answer: D  (Neither I nor II is implicit)
       Source: NTPC CBT-2, 2021
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q11 ── Only Assumption I implicit (mobile games and poor performance) ──
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Many students have got into the habit of playing mobile games "
            "and that is why they perform poorly.\n\n"
            "Assumptions:\n"
            "I.  Many students are not paying attention to studies because of mobile "
            "games.\n"
            "II. It is because of mobile games that students fail in the examination."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: कई विद्यार्थियों को मोबाइल गेम्स खेलने की आदत पड़ गई है और इसी "
            "कारण वे खराब शैक्षिक प्रदर्शन करते हैं।\n\n"
            "पूर्वानुमान:\n"
            "I.  कई विद्यार्थी मोबाइल गेम्स के कारण पढ़ाई पर ध्यान नहीं दे रहे हैं।\n"
            "II. मोबाइल गेम्स के कारण ही विद्यार्थी परीक्षा में अनुत्तीर्ण होते हैं।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: mobile games → poor performance implies distraction from studies → IMPLICIT ✓
        # II: "perform poorly" ≠ "fail in examination"; too extreme and specific → NOT IMPLICIT ✗
    },
    # ── Q12 ── Both assumptions implicit (pesticides, food chain, humans) ──────
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Excessive use of pesticides in agricultural production "
            "contaminates soil and water, residues in crops and eventually enter the "
            "food chain, creating a threat to humans.\n\n"
            "Assumptions:\n"
            "I.  Excessive use of pesticides in agricultural production is not good "
            "for the people.\n"
            "II. Excessive use of pesticides in agricultural production can have a bad "
            "effect on water."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: कृषि उत्पादन में कीटनाशकों का अत्यधिक उपयोग करने से वे मिट्टी और "
            "जल को दूषित करते हैं, फसलों में उनका अंश रह जाता है और आखिरकार वे खाद्य "
            "शृंखला में प्रवेश करते हैं, जिससे मानवों के लिए खतरा पैदा हो जाता है।\n\n"
            "पूर्वानुमान:\n"
            "I.  कृषि उत्पादन में कीटनाशकों का अत्यधिक उपयोग किया जाना, लोगों के "
            "लिए अच्छा नहीं है।\n"
            "II. कृषि उत्पादन में कीटनाशकों का अत्यधिक उपयोग करने से जल पर बुरा "
            "प्रभाव पड़ सकता है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "C",
        # I: the causal chain ends in "threat to humans" → harmful to people → IMPLICIT ✓
        # II: statement explicitly says "contaminates soil and water" → IMPLICIT ✓
    },
    # ── Q13 ── Only Assumption II implicit (expressway speed and accidents) ────
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: National Expressway-A is the widest expressway and is used by "
            "few people. When people see a wide road, they drive at high speed, which "
            "leads to accidents.\n\n"
            "Assumptions:\n"
            "I.  All accidents are caused by excessive speed.\n"
            "II. High speed increases the risk of accident."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: राष्ट्रीय दुतगामी मार्ग-A, सबसे चौड़ा दुतगामी मार्ग है और कुछ लोग "
            "इसका इस्तेमाल करते हैं। जब लोग कोई खाली और चौड़ी सड़क देखते हैं, तब वे "
            "तेज गति से वाहन चलाते हैं, जिससे दुर्घटनाएँ होती हैं।\n\n"
            "पूर्वानुमान:\n"
            "I.  सभी दुर्घटनाएँ अत्यधिक गति के कारण होती हैं।\n"
            "II. तेज गति से दुर्घटना का खतरा बढ़ जाता है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "B",
        # I: "ALL accidents are from speed" — extreme overgeneralisation beyond the statement → NOT IMPLICIT ✗
        # II: statement says high speed "leads to accidents" → directly implies increased risk → IMPLICIT ✓
    },
    # ── Q14 ── Only Assumption I implicit (football match left-footed goals) ───
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: In a football match between Team-X and Team-Y, the total "
            "number of goals scored by Team-Y was 5, out of which 3 goals were scored "
            "by the left-footed player.\n\n"
            "Assumptions:\n"
            "I.  The left-footed player was expert in scoring goals.\n"
            "II. 60% of Team-Y players are left footed."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: टीम-X और टीम-Y के बीच एक फुटबॉल मैच में, टीम-Y द्वारा किए गए गोलों "
            "की कुल संख्या 5 थी, जिनमें से 3 गोल बाएँ पैर वाले खिलाड़ी द्वारा किए "
            "गए थे।\n\n"
            "पूर्वानुमान:\n"
            "I.  बाएँ पैर वाला खिलाड़ी गोल करने में माहिर था।\n"
            "II. टीम-Y के 60% खिलाड़ी बाएँ पैर वाले हैं।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: scoring 3/5 of the team's goals implies the player was skilled/expert at
        #    goal-scoring → IMPLICIT ✓
        # II: 3/5 goals (60%) scored by left-footed player ≠ 60% of players are
        #    left-footed; goals% ≠ player composition% → NOT IMPLICIT ✗
    },
    # ── Q15 ── Neither assumption implicit (computer education at school) ──────
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Computer education should start at schools itself.\n\n"
            "Assumptions:\n"
            "I.  Computer education fetches job easily.\n"
            "II. Learning computer is easy."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: कंप्यूटर शिक्षा स्कूलों में ही शुरू होनी चाहिए।\n\n"
            "पूर्वानुमान:\n"
            "I.  कंप्यूटर शिक्षा से आसानी से नौकरी मिल जाती है।\n"
            "II. कंप्यूटर सीखना आसान है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Either I or II is implicit / I या II अंतर्निहित है",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "D",
        # I: job outcomes are indirect/speculative; not stated as reason for school
        #    computer education → NOT IMPLICIT ✗ (NTPC CBT-2, 2021)
        # II: the statement doesn't say computers are easy to learn; teaching a subject
        #    at school doesn't depend on its ease → NOT IMPLICIT ✗
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
