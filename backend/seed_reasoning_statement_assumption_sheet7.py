"""
seed_reasoning_statement_assumption_sheet7.py
=============================================
Seeds Statement-Conclusion Q43–Q51 from Gagan Pratap Reasoning PDFs (Sheet 7).
Subject : Reasoning
Topic   : Statement Assumption and Conclusion

All questions use the CONCLUSION format (5 options).
Options A–D stored in DB; option E injected by frontend (SAC_CONCLUSION_E)
because option_a starts with "Only I follows".

  (A) Only I follows.
  (B) Only II follows.
  (C) Both I & II follow.
  (D) Neither I nor II follows.
  (E) Either I or II follows.  ← injected by frontend; CORRECT for Q44, Q46, Q48.

Sources:
  Q43 = UPSI, 27 Nov 2021, Shift-3
  Q44 = UPSI, 01 Dec 2021, Shift-2
  Q45 = UPSI, 13 Nov 2021, Shift-2
  Q46 = UPSI, 25 Nov 2021, Shift-3
  Q47 = UPSI, 27 Nov 2021, Shift-2
  Q48 = UPSI, 20 Nov 2021, Shift-2
  Q49 = NTPC CBT-2, 2021
  Q50 = NTPC CBT-2, 2021
  Q51 = NTPC CBT-2, 2021

Answer key:

  Q43  A — School allows kids to drink only hot water during Winter.
            Conclusion I:   Drinking hot water is good for kids during Winter
                            → FOLLOWS ✓ (restricting kids to ONLY hot water during
                            Winter is a deliberate policy decision that implies hot
                            water is considered beneficial/healthy for them in cold
                            weather; the restriction would serve no purpose otherwise)
            Conclusion II:  The school doesn't have the facility to provide cold water
                            → DOES NOT FOLLOW ✗ (the caretaker says kids are
                            "allowed to drink only hot water" — this is a policy
                            choice for health reasons, not a statement about lacking
                            cold water infrastructure)
            Only I follows.

  Q44  E — Vinod is a good cricketer.
            Conclusion I:   Vinod bats well → DOES NOT FOLLOW ALONE ✗
                            (a good cricketer can excel through batting, bowling, or
                            fielding; the statement doesn't specify which skill makes
                            Vinod good)
            Conclusion II:  Vinod bowls well → DOES NOT FOLLOW ALONE ✗
                            (same reason — the statement does not specify the skill
                            that makes Vinod a good cricketer)
            → A good cricketer must excel in at least one of batting or bowling
              (the primary skills), but we cannot determine which one specifically.
            Either I or II follows.

  Q45  D — Rahul reads 20 pages a day.
            Conclusion I:   Rahul is poor in reading → DOES NOT FOLLOW ✗
                            (20 pages per day could represent a lot or a little;
                            the statement makes no judgment about reading ability
                            or speed — it is a neutral quantity statement)
            Conclusion II:  Rahul must be having exams → DOES NOT FOLLOW ✗
                            (reading 20 pages is a general habit; there is no
                            indication of examination pressure; people read for
                            pleasure, knowledge, or study without exams)
            Neither I nor II follows.

  Q46  E — It rains every Monday. It rains today.
            Conclusion I:   It must be a rainy season → POSSIBLE if today is not
                            Monday and it is raining for a seasonal reason
            Conclusion II:  Today is Monday → POSSIBLE if today is Monday, which
                            explains why it is raining
            → The rain today is explained by EITHER (i) today being Monday (II)
              OR (ii) it being rainy season and raining for an independent reason (I).
              Both are plausible explanations; we cannot determine which is true.
            Either I or II follows.

  Q47  D — Girls native to Seoul will definitely get married at age 23.
           Beni is a 24 year old girl.
            Conclusion I:   Girls in other cities (except Seoul) marry BEFORE 23
                            → DOES NOT FOLLOW ✗ (statement says nothing about
                            other cities' marriage ages; Beni's age alone gives
                            no information about non-Seoul cities' customs)
            Conclusion II:  Girls in other cities (except Seoul) marry AFTER 23
                            → DOES NOT FOLLOW ✗ (same reason — other cities are
                            not mentioned anywhere in the statement)
            Neither I nor II follows.

  Q48  E — Shyam is one of the students who are EXPECTED to get placed in ABC
           India Pvt. Ltd.
            Conclusion I:   Shyam will get placed in ABC India Pvt. Ltd.
                            → DOES NOT FOLLOW ALONE ✗ ("expected" ≠ certain;
                            expectation does not guarantee the outcome)
            Conclusion II:  Shyam will NOT get placed in ABC India Pvt. Ltd.
                            → DOES NOT FOLLOW ALONE ✗ (being expected to get placed
                            does not prove he won't; the outcome is still uncertain)
            → I and II are mutually exclusive and exhaustive (he either gets placed
              or he does not); exactly one will be true, but the given information
              does not allow us to determine which.
            Either I or II follows.

  Q49  A — In modern days, a man influences his destiny by the choices he makes
           unlike in the past days.
            Conclusion I:   Earlier there were less options available to choose from
                            → FOLLOWS ✓ ("unlike in the past" implies the past was
                            different from modern times with respect to choice-making
                            and its effect on destiny; the most direct inference is
                            that fewer options existed in the past — if past had the
                            same options, it would not be "unlike" modern days)
            Conclusion II:  There is no need to influence the destiny → DOES NOT
                            FOLLOW ✗ (the statement says people CAN and DO influence
                            destiny through choices; it says nothing about whether
                            this is needed or not — Conclusion II contradicts the
                            spirit of the statement)
            Only I follows.

  Q50  A — (A) People who exercise regularly are health conscious.
           (B) Meena, in spite of her busy schedule, exercises every day.
            Conclusion I:   Meena is health-conscious → FOLLOWS ✓
                            (valid syllogism: All regular exercisers → health conscious;
                            Meena exercises every day → Meena is a regular exerciser;
                            ∴ Meena is health conscious)
            Conclusion II:  Meena has inculcated the importance of exercise right
                            from her childhood → DOES NOT FOLLOW ✗ (no information
                            about when or why Meena started exercising is given;
                            childhood inculcation is not mentioned or implied)
            Only I follows.

  Q51  B — (I)  Use of electronic book reading has increased considerably during
                recent times.
           (II) Printed books are costly.
            Conclusion I:   Nobody reads books nowadays → DOES NOT FOLLOW ✗
                            (the first statement explicitly says electronic book
                            reading has INCREASED — meaning people ARE reading,
                            just in electronic form; "nobody reads" directly
                            contradicts the given information)
            Conclusion II:  Electronic book reading is gaining popularity
                            → FOLLOWS ✓ ("increased considerably during recent
                            times" is precisely what gaining popularity means;
                            the conclusion directly restates the first statement
                            in other words)
            Only II follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Assumption_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Statement Assumption and Conclusion"

# Conclusion format — 5-option (option E injected by frontend when option_a
# starts with "Only I follows").
_A = "Only I follows. / केवल I अनुसरण करता है।"
_B = "Only II follows. / केवल II अनुसरण करता है।"
_C = "Both I & II follow. / I और II दोनों अनुसरण करते हैं।"
_D = "Neither I nor II follows. / न तो I और न ही II अनुसरण करता है।"
# _E = "Either I or II follows." ← injected by frontend as SAC_CONCLUSION_E;
#                                   CORRECT for Q44, Q46, Q48 → correct_answer = "E"

QUESTIONS = [
    # ── Q43 (UPSI, 27 Nov 2021, Shift-3) ─────────────────────────────────────
    {
        "question_number": 43,
        "difficulty": "easy",
        "question_en": (
            "Statement: 'In our school, kids are allowed to drink only hot water "
            "during Winter', said a caretaker of a school.\n\n"
            "Conclusions:\n"
            "I.  Drinking hot water is good for the kids during Winter.\n"
            "II. The school doesn't have the facility to provide cold water."
        ),
        "question_hi": (
            "कथन: एक स्कूल के केयरटेकर ने कहा, 'हमारे स्कूल में, बच्चों को "
            "सर्दियों के दौरान केवल गर्म पानी पीने की अनुमति है।'\n\n"
            "निष्कर्ष:\n"
            "I.  सर्दियों के दौरान बच्चों के लिए गर्म पानी पीना अच्छा है।\n"
            "II. स्कूल में ठंडा पानी उपलब्ध कराने की सुविधा नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Restricting kids to ONLY hot water in winter is a deliberate health
        #     policy → implies hot water is beneficial during cold weather ✓
        # II: "Allowed to drink only hot water" = a policy rule, not a statement
        #     about lack of cold water infrastructure ✗
    },
    # ── Q44 (UPSI, 01 Dec 2021, Shift-2) ─────────────────────────────────────
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": (
            "Statement: Vinod is a good cricketer.\n\n"
            "Conclusions:\n"
            "I.  Vinod bats well.\n"
            "II. Vinod bowls well."
        ),
        "question_hi": (
            "कथन: विनोद एक अच्छा क्रिकेटर है।\n\n"
            "निष्कर्ष:\n"
            "I.  विनोद अच्छी बल्लेबाजी करता है।\n"
            "II. विनोद अच्छी गेंदबाजी करता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "E",
        # A good cricketer must excel in at least one primary skill — batting (I)
        # or bowling (II) — but the statement does not specify which; at least one
        # of the two conclusions must apply, but we cannot determine which.
        # → Either I or II follows (injected by frontend as SAC_CONCLUSION_E).
    },
    # ── Q45 (UPSI, 13 Nov 2021, Shift-2) ─────────────────────────────────────
    {
        "question_number": 45,
        "difficulty": "easy",
        "question_en": (
            "Statement: Rahul reads 20 pages a day.\n\n"
            "Conclusions:\n"
            "I.  Rahul is poor in reading.\n"
            "II. Rahul must be having exams."
        ),
        "question_hi": (
            "कथन: राहुल एक दिन में 20 पेज पढ़ते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  राहुल पढ़ने में कमजोर है।\n"
            "II. राहुल की परीक्षा हो रही होगी।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  20 pages/day is a neutral fact; no basis to judge reading ability ✗
        # II: Reading could be for pleasure or general study; no indication of exams ✗
    },
    # ── Q46 (UPSI, 25 Nov 2021, Shift-3) ─────────────────────────────────────
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": (
            "Statement: It rains every Monday. It rains today.\n\n"
            "Conclusions:\n"
            "I.  It must be a rainy season.\n"
            "II. Today is Monday."
        ),
        "question_hi": (
            "कथन: हर सोमवार को वर्षा होती है। आज वर्षा हो रही है।\n\n"
            "निष्कर्ष:\n"
            "I.  यह वर्षा का मौसम होना चाहिए।\n"
            "II. आज सोमवार है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "E",
        # Rain today can be explained by EITHER (i) today is Monday (routine Monday
        # rain, Conclusion II) OR (ii) it is rainy season so it rains for independent
        # reasons (Conclusion I). Both are plausible; neither is definitively certain.
        # → Either I or II follows (injected by frontend as SAC_CONCLUSION_E).
    },
    # ── Q47 (UPSI, 27 Nov 2021, Shift-2) ─────────────────────────────────────
    {
        "question_number": 47,
        "difficulty": "medium",
        "question_en": (
            "Statement: Girls native to Seoul will definitely get married at the "
            "age of 23. Beni is a 24 year old girl.\n\n"
            "Conclusions:\n"
            "I.  Except for Seoul girls, girls in other cities marry before 23.\n"
            "II. Except for Seoul girls, girls in other cities marry after 23."
        ),
        "question_hi": (
            "कथन: सियोल की मूल निवासी लड़कियों की शादी निश्चित रूप से 23 वर्ष "
            "की आयु में हो जाएगी। बेनी 24 वर्ष की लड़की है।\n\n"
            "निष्कर्ष:\n"
            "I.  सियोल की लड़कियों को छोड़कर, अन्य शहरों में लड़कियों की शादी "
            "23 वर्ष से पहले हो जाती है।\n"
            "II. सियोल की लड़कियों को छोड़कर अन्य शहरों में लड़कियों की शादी "
            "23 वर्ष के बाद होती है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # Statement only establishes Seoul girls' marriage age (23).
        # No information about girls in other cities is provided.
        # I & II both make claims about "other cities" → NEITHER follows ✗✗
    },
    # ── Q48 (UPSI, 20 Nov 2021, Shift-2) ─────────────────────────────────────
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": (
            "Statement: Shyam is one of the students who are expected to get "
            "placed in ABC India Pvt. Ltd.\n\n"
            "Conclusions:\n"
            "I.  Shyam will get placed in ABC India Pvt. Ltd.\n"
            "II. Shyam will not get placed in ABC India Pvt. Ltd."
        ),
        "question_hi": (
            "कथन: श्याम उन छात्रों में से एक है जिन्हें एबीसी इंडिया प्राइवेट "
            "लिमिटेड में नौकरी मिलने की उम्मीद है।\n\n"
            "निष्कर्ष:\n"
            "I.  श्याम को एबीसी इंडिया प्राइवेट लिमिटेड में नौकरी मिल जाएगी।\n"
            "II. श्याम को एबीसी इंडिया प्राइवेट लिमिटेड में नौकरी नहीं मिलेगी।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "E",
        # I and II are mutually exclusive and exhaustive — Shyam either gets placed
        # or does not. "Expected" ≠ certain, so we cannot determine which is true.
        # But exactly one MUST ultimately be true.
        # → Either I or II follows (injected by frontend as SAC_CONCLUSION_E).
    },
    # ── Q49 (NTPC CBT-2, 2021) ────────────────────────────────────────────────
    {
        "question_number": 49,
        "difficulty": "medium",
        "question_en": (
            "Statement: In modern days, a man influences his destiny by the choices "
            "he makes unlike in the past days.\n\n"
            "Conclusions:\n"
            "I.  Earlier there were less options available to choose from.\n"
            "II. There is no need to influence the destiny."
        ),
        "question_hi": (
            "कथन: आधुनिक दिनों में, एक व्यक्ति उन विकल्पों के माध्यम से अपनी "
            "नियति को प्रभावित करता है जो वो अतीत के दिनों की तुलना में चुनता है।\n\n"
            "निष्कर्ष:\n"
            "I.  पहले चुनने के लिए कम विकल्प उपलब्ध थे।\n"
            "II. अतीत में, भाग्य को प्रभावित करने की कोई इच्छा नहीं थी।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  "Unlike in the past" implies fewer choices in past days, which explains
        #     why destiny wasn't influenced by choices back then → FOLLOWS ✓
        # II: The statement says people CAN influence destiny through choices;
        #     "no need to influence destiny" contradicts this premise → DOES NOT FOLLOW ✗
    },
    # ── Q50 (NTPC CBT-2, 2021) ────────────────────────────────────────────────
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": (
            "Statement:\n"
            "A. People who exercise regularly are health conscious.\n"
            "B. Meena in spite of her busy schedule, exercises every day.\n\n"
            "Conclusions:\n"
            "I.  Meena is health-conscious.\n"
            "II. Meena has inculcated the importance of exercise right from her "
            "childhood."
        ),
        "question_hi": (
            "कथन:\n"
            "A. जो लोग नियमित रूप से व्यायाम करते हैं वे स्वास्थ्य के प्रति "
            "जागरूक होते हैं।\n"
            "B. मीना अपने व्यस्त कार्यक्रम के बावजूद हर दिन व्यायाम करती है।\n\n"
            "निष्कर्ष:\n"
            "I.  मीना स्वास्थ्य के प्रति जागरूक है।\n"
            "II. मीना ने बचपन से ही व्यायाम के महत्व को आत्मसात किया है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Valid syllogism: All regular exercisers → health conscious [A];
        #     Meena exercises daily → Meena is a regular exerciser [B];
        #     ∴ Meena is health conscious ✓
        # II: No information about when or why Meena began exercising;
        #     childhood inculcation is not mentioned or implied ✗
    },
    # ── Q51 (NTPC CBT-2, 2021) ────────────────────────────────────────────────
    {
        "question_number": 51,
        "difficulty": "easy",
        "question_en": (
            "Statement:\n"
            "I.  Use of electronic book reading has increased considerably during "
            "recent times.\n"
            "II. Printed books are costly.\n\n"
            "Conclusions:\n"
            "I.  Nobody reads books nowadays.\n"
            "II. Electronic book reading is gaining popularity."
        ),
        "question_hi": (
            "कथन:\n"
            "I.  हाल ही में इलेक्ट्रॉनिक रूप से पुस्तक पढ़ने का उपयोग काफी "
            "बढ़ गया है।\n"
            "II. छपी हुई पुस्तकें महंगी होती हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  आजकल कोई भी पुस्तक नहीं पढ़ता।\n"
            "II. इलेक्ट्रॉनिक रूप से पुस्तक पढ़ना लोकप्रिय हो रहा है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  "Nobody reads books nowadays" CONTRADICTS Statement I (e-book reading
        #     has INCREASED = people ARE reading, just electronically) ✗
        # II: "Increased considerably during recent times" = gaining popularity;
        #     Conclusion II directly rephrases Statement I ✓
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
