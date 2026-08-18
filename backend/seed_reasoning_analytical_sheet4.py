"""
seed_reasoning_analytical_sheet4.py
=========================================
Seeds Analytical Reasoning Q10-Q14 from Gagan Pratap Reasoning PDFs (Sheet 4).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet4.py

NOTE:
  Q11 old content ("two statements I and II have been given...") was deleted.
  Q13 already in DB with correct content — correct_answer patched separately.
  Q10, Q11 (new), Q12, Q14 are fresh inserts.

Answer key (solutions verified):
  Q10  Statement: Parents prepared to pay any fee for elite institute for perfect
       development of children.
       I)  Parents have obsessive passion for perfect development via good institutes.
           → Directly restates/paraphrases the statement → TRUE
       II) These days all parents are very well off.
           → Willingness to pay ≠ wealth; "all" is too sweeping → FALSE
       Answer: A  (Only Conclusion I follows)

  Q11  Statements: All numbers divisible by 2. All numbers divisible by 3.
       I)  All numbers are divisible by 6.
           → LCM(2, 3) = 6; divisible by both 2 and 3 → divisible by 6 → TRUE
       II) All numbers are divisible by 4.
           → e.g. 6 is divisible by 2 and 3 but NOT by 4 → FALSE
       Answer: A  (Only Conclusion I follows)

  Q12  Premises: No hero is coward. Some soldiers are cowards.
       Deduction: Some soldiers (those who are cowards) cannot be heroes.
       → Some soldiers are not heroes.
       Answer: C

  Q13  Passage: Pharmaceutical patent monopoly → high prices → could be unaffordable;
       but drives R&D → long-term public benefit. Governments must balance rights.
       Assumptions:
         I)   Patent protection burdens public purchasing power → VALID (passage states
              medicines "could be unaffordable to the public")
         II)  Dependence on other countries is a burden → NOT in passage → INVALID
         III) Affordable medicines is key public health policy goal → VALID (implied
              by the conflict the passage describes)
         IV)  Govts must balance patentee rights vs patient needs → VALID (central
              trade-off of the passage)
       Answer: C  (III and IV)  [I is also valid but the best option is III & IV]

  Q14  Statement: Letter to candidates: "You have to bear your expenses on travel etc."
       Assumption I:  Without clarification candidates might claim reimbursement → IMPLICIT
       Assumption II: Many organisations do reimburse travel for written exams →  IMPLICIT
                     (explains why the clarification is needed in the first place)
       Answer: D  (Both I and II are implicit)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q10 ── Only Conclusion I follows ──────────────────────────────────────
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": (
            "A statement is given followed by two Conclusions numbered I and II. "
            "You have to assume everything in the statement to be true, then consider "
            "the two conclusions together and decide which of them logically follows.\n\n"
            "Statement: Nowadays parents are prepared to pay any fee for an elite "
            "education institute for the perfect development of their children.\n\n"
            "Conclusion I: Parents have an obsessive passion for a perfect development "
            "of their children through good education institute.\n"
            "Conclusion II: These days all parents are very well off."
        ),
        "question_hi": (
            "एक कथन के बाद दो निष्कर्ष I और II दिए गए हैं। आपको कथन में दी गई सभी "
            "बातों को सच मानना है, फिर दोनों निष्कर्षों पर विचार करके तय करें कि "
            "इनमें से कौन सा तार्किक रूप से अनुसरण करता है।\n\n"
            "कथन: आजकल माता-पिता अपने बच्चों के संपूर्ण विकास के लिए किसी भी अभिजात "
            "शिक्षा संस्थान को कोई भी शुल्क देने के लिए तैयार हैं।\n\n"
            "निष्कर्ष I: माता-पिता को अच्छे शिक्षा संस्थान के माध्यम से अपने बच्चों "
            "के पूर्ण विकास की जुनूनी चाह है।\n"
            "निष्कर्ष II: आजकल सभी माता-पिता बहुत संपन्न हैं।"
        ),
        "option_a": "Only Conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Only Conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Neither conclusion I nor II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "option_d": "Both Conclusion I and Conclusion II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "correct_answer": "A",
        # I: directly paraphrases the premise (any fee → passionate about development) → TRUE
        # II: willingness to pay ≠ actually wealthy; "all" is too sweeping → FALSE
    },
    # ── Q11 ── Only Conclusion I (div by 6) follows ───────────────────────────
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": (
            "Two Statements are given followed by two Conclusions. "
            "You have to take the given Statements to be true even if they seem to be "
            "at variance from commonly known facts. Read all the Conclusions and then "
            "decide which of the given Conclusions logically follow(s) from the given Statements.\n\n"
            "Statements:\n"
            "All numbers are divisible by 2.\n"
            "All numbers are divisible by 3.\n\n"
            "Conclusions:\n"
            "I.  All numbers are divisible by 6.\n"
            "II. All numbers are divisible by 4."
        ),
        "question_hi": (
            "दो कथनों के बाद दो निष्कर्ष दिए गए हैं। आपको दिए गए कथनों को सत्य मानना है। "
            "सभी निष्कर्ष पढ़िए और फिर तय कीजिए कि दिए गए कथनों से तार्किक रूप से "
            "कौन सा निष्कर्ष अनुसरण करता है।\n\n"
            "कथन:\n"
            "सभी संख्याएँ 2 से विभाज्य हैं।\n"
            "सभी संख्याएँ 3 से विभाज्य हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी संख्याएँ 6 से विभाज्य हैं।\n"
            "II. सभी संख्याएँ 4 से विभाज्य हैं।"
        ),
        "option_a": "Only Conclusion I / केवल निष्कर्ष I",
        "option_b": "Only Conclusion II / केवल निष्कर्ष II",
        "option_c": "Neither I nor II / न तो I और न ही II",
        "option_d": "Both Conclusion I and Conclusion II / निष्कर्ष I और II दोनों",
        "correct_answer": "A",
        # I: LCM(2,3)=6; divisible by 2 AND 3 → divisible by 6 ✓ TRUE
        # II: e.g. 6 is div by 2 and 3 but NOT by 4 → FALSE
    },
    # ── Q12 ── Some soldiers are not heroes ───────────────────────────────────
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": (
            "Which of the following conclusions can be validly drawn from the given "
            "set of premises?\n\n"
            "I.  No hero is coward.\n"
            "II. Some soldiers are cowards."
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा निष्कर्ष दिए गए आधारों से वैध रूप से निकाला "
            "जा सकता है?\n\n"
            "I.  कोई भी वीर (नायक) कायर नहीं है।\n"
            "II. कुछ सैनिक कायर हैं।"
        ),
        "option_a": "No soldier is coward / कोई भी सैनिक कायर नहीं है",
        "option_b": "No hero is coward / कोई भी नायक कायर नहीं है",
        "option_c": "Some soldiers are not heroes / कुछ सैनिक नायक नहीं हैं",
        "option_d": "Some soldiers are heroes / कुछ सैनिक नायक हैं",
        "correct_answer": "C",
        # Hero ∩ Coward = ∅ (premise I); some Soldiers ∈ Coward (premise II)
        # → those soldiers ∉ Hero → Some soldiers are not heroes ✓
        # (a) false — premise II says some ARE cowards
        # (b) just restates premise I, not a new deduction
        # (d) cannot be derived
    },
    # ── Q13 ── Pharmaceutical patent passage: assumptions III and IV valid ─────
    # (Q13 already in DB; this entry is included here so the script stays
    #  complete and self-documented. It will be skipped by the dedup check.)
    {
        "question_number": 13,
        "difficulty": "hard",
        "question_en": (
            "Pharmaceutical patents grant protection to the patentee for the duration "
            "of the patent term. The patentees enjoy the liberty to determine the prices "
            "of medicines, which is time-limited to the period of monopoly, but could be "
            "unaffordable to the public. Such patent protection offered to the patentees "
            "is believed to benefit the public over the longer term through innovations "
            "and research and development (R&D), although it comes at a cost, in the "
            "nature of higher prices for the patented medicine. The patent regime and "
            "price protection through a legally validated high price for the medicine "
            "during the currency of the patent provide the patentee with a legitimate "
            "mechanism to get returns on the costs incurred in innovation and research.\n\n"
            "Based on the above passage, the following assumptions have been made:\n"
            "I.   Patent protection given to patentees puts a huge burden on public's "
            "purchasing power in accessing patented medicines.\n"
            "II.  Dependence on other countries for pharmaceutical products is a huge "
            "burden for developing and poor countries.\n"
            "III. Providing medicines to the public at affordable prices is a key goal "
            "during public health policy design in many countries.\n"
            "IV.  Governments need to find an appropriate balance between the rights of "
            "patentees and the requirements of the patients.\n\n"
            "Which of the above assumptions are valid?"
        ),
        "question_hi": (
            "फार्मास्यूटिकल पेटेंट पेटेंट अवधि के लिए पेटेंटधारक को सुरक्षा प्रदान "
            "करते हैं। पेटेंटधारक को दवाओं की कीमतें निर्धारित करने की स्वतंत्रता "
            "होती है, जो एकाधिकार की अवधि तक सीमित है, लेकिन जनता के लिए वहनीय नहीं "
            "हो सकती। माना जाता है कि पेटेंटधारकों को दी जाने वाली ऐसी पेटेंट सुरक्षा "
            "नवाचारों और R&D के माध्यम से लंबे समय में जनता को लाभ पहुँचाती है, हालांकि "
            "इसके कारण पेटेंट दवा की कीमत अधिक होती है।\n\n"
            "उपरोक्त गद्यांश के आधार पर निम्नलिखित धारणाएँ बनाई गई हैं:\n"
            "I.   पेटेंटधारकों को दी गई पेटेंट सुरक्षा पेटेंट दवाओं तक पहुँचने में "
            "जनता की क्रय शक्ति पर भारी बोझ डालती है।\n"
            "II.  फार्मास्यूटिकल उत्पादों के लिए अन्य देशों पर निर्भरता विकासशील और "
            "गरीब देशों के लिए एक बड़ा बोझ है।\n"
            "III. कई देशों में सार्वजनिक स्वास्थ्य नीति डिजाइन के दौरान सस्ती कीमतों "
            "पर दवाएँ उपलब्ध कराना एक प्रमुख लक्ष्य है।\n"
            "IV.  सरकारों को पेटेंटधारकों के अधिकारों और रोगियों की आवश्यकताओं के बीच "
            "उचित संतुलन खोजने की आवश्यकता है।\n\n"
            "उपर्युक्त में से कौन सी धारणाएँ मान्य हैं?"
        ),
        "option_a": "I and II / I और II",
        "option_b": "I and IV / I और IV",
        "option_c": "III and IV / III और IV",
        "option_d": "II and III / II और III",
        "correct_answer": "C",
        # I:  valid — passage says medicines "could be unaffordable to the public"
        # II: INVALID — passage says nothing about foreign dependence
        # III: valid — the conflict over pricing assumes affordable access is a policy goal
        # IV: valid — the core trade-off of the passage (R&D returns vs patient affordability)
        # Best matching option: C (III and IV)
    },
    # ── Q14 ── Both assumptions implicit ──────────────────────────────────────
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: A sentence in the letter to the candidates called for written "
            "examinations — 'You have to bear your expenses on travel etc.'\n\n"
            "Assumptions:\n"
            "I.  If not clarified, all the candidates can claim reimbursement of "
            "expenses.\n"
            "II. Many organisations reimburse expenses on travel to candidates called "
            "for written examinations."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: लिखित परीक्षाओं के लिए बुलाए गए अभ्यर्थियों को पत्र में एक वाक्य "
            "— 'आपको यात्रा आदि पर होने वाले खर्च स्वयं वहन करने होंगे।'\n\n"
            "अनुमान:\n"
            "I.  यदि स्पष्ट नहीं किया गया, तो सभी अभ्यर्थी खर्च की प्रतिपूर्ति का "
            "दावा कर सकते हैं।\n"
            "II. कई संगठन लिखित परीक्षाओं के लिए बुलाए गए अभ्यर्थियों की यात्रा पर "
            "खर्च की प्रतिपूर्ति करते हैं।"
        ),
        "option_a": "If only assumption I is implicit / यदि केवल अनुमान I अंतर्निहित है",
        "option_b": "If only assumption II is implicit / यदि केवल अनुमान II अंतर्निहित है",
        "option_c": "If either I or II is implicit / यदि I या II अंतर्निहित है",
        "option_d": "If both I and II are implicit / यदि I और II दोनों अंतर्निहित हैं",
        "correct_answer": "D",
        # I: IMPLICIT — if no clarification were needed, the sentence would be unnecessary;
        #    its inclusion assumes candidates might otherwise expect reimbursement
        # II: IMPLICIT — explains WHY the clarification is necessary; many orgs do reimburse,
        #     so candidates could reasonably assume it is standard practice
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
