"""
seed_reasoning_analytical_sheet5.py
=========================================
Seeds Analytical Reasoning Q15-Q20 from Gagan Pratap Reasoning PDFs (Sheet 5).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet5.py

NOTE:
  Q15, Q16, Q20 share the same statement (Governing Board meeting after one year)
   — they are separate questions from different practice sets in the PDF.
  Q18 shares its statement with Q14 — again from a different practice set.
  Two wrong Q19s (different content, no answers) were deleted before this run.

Answer key (solutions verified):
  Q15  Statement: Next Governing Board meeting after one year.
       I)  Institute will remain in function after one year → IMPLICIT
           (scheduling a future meeting assumes continuity)
       II) Governing Board will be dissolved after one year → NOT IMPLICIT
           (contradicts the scheduling of a future meeting)
       Answer: A  (Only assumption I is implicit)

  Q16  (Same statement as Q15 — from a different practice set)
       Answer: A  (Only assumption I is implicit)

  Q17  Statement: Apart from entertainment value of TV, educational value cannot be ignored.
       I)  People take TV to be a means of entertainment only → IMPLICIT
           ("cannot be ignored" implies TV is generally perceived as entertainment-only)
       II) Educational value of TV is not realised properly → IMPLICIT
           ("cannot be ignored" implies it is currently underappreciated/overlooked)
       Answer: D  (Both I and II are implicit)

  Q18  Statement: "You have to bear your expenses on travel etc." (exam letter)
       I)  If not clarified, candidates may claim reimbursement → IMPLICIT
       II) Many organisations do reimburse travel for written exam candidates → IMPLICIT
       Answer: D  (Both I and II are implicit)

  Q19  Statement: If it does not rain throughout this month, most farmers will be
       in trouble this year.
       I)  Timely rain is essential for farming → IMPLICIT
           (trouble from lack of rain assumes rainfall timing is critical)
       II) Most farmers are generally dependent on rains → IMPLICIT
           (linking farmer trouble to rainfall absence directly implies dependence)
       Answer: B  (Both assumptions are implicit)

  Q20  (Same statement as Q15 — from a different practice set)
       Answer: A  (Only assumption I is implicit)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q15 ── Only Assumption I implicit (Governing Board meeting) ───────────
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: The next meeting of the Governing Board of the Institute will "
            "be held after one year.\n\n"
            "Assumptions:\n"
            "I.  The Institute will remain in function after one year.\n"
            "II. The Governing Board will be dissolved after one year."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: संस्था की शासी बोर्ड की अगली बैठक एक वर्ष बाद होगी।\n\n"
            "अनुमान:\n"
            "I.  संस्था एक वर्ष के बाद भी कार्यरत रहेगी।\n"
            "II. शासी बोर्ड एक वर्ष के बाद भंग हो जाएगा।"
        ),
        "option_a": "If only assumption I is implicit / यदि केवल अनुमान I अंतर्निहित है",
        "option_b": "If only assumption II is implicit / यदि केवल अनुमान II अंतर्निहित है",
        "option_c": "If either I or II is implicit / यदि I या II अंतर्निहित है",
        "option_d": "If neither I nor II is implicit / यदि न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: scheduling meeting after a year assumes Institute continues → IMPLICIT ✓
        # II: contradicts scheduling — why meet if board is dissolved? → NOT IMPLICIT ✗
    },
    # ── Q16 ── Only Assumption I implicit (same statement, different set) ──────
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: The next meeting of the Governing Board of the Institute will "
            "be held after one year.\n\n"
            "Assumptions:\n"
            "I.  The Institute will remain in function after one year.\n"
            "II. The Governing Board will be dissolved after one year."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: संस्था की शासी बोर्ड की अगली बैठक एक वर्ष बाद होगी।\n\n"
            "अनुमान:\n"
            "I.  संस्था एक वर्ष के बाद भी कार्यरत रहेगी।\n"
            "II. शासी बोर्ड एक वर्ष के बाद भंग हो जाएगा।"
        ),
        "option_a": "If only assumption I is implicit / यदि केवल अनुमान I अंतर्निहित है",
        "option_b": "If only assumption II is implicit / यदि केवल अनुमान II अंतर्निहित है",
        "option_c": "If either I or II is implicit / यदि I या II अंतर्निहित है",
        "option_d": "If neither I nor II is implicit / यदि न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # Same reasoning as Q15
    },
    # ── Q17 ── Both assumptions implicit (television education value) ──────────
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: Apart from the entertainment value of television, its "
            "educational value cannot be ignored.\n\n"
            "Assumptions:\n"
            "I.  People take television to be a means of entertainment only.\n"
            "II. The educational value of television is not realised properly."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: टेलीविजन के मनोरंजन मूल्य के अलावा, इसके शैक्षिक मूल्य को भी "
            "नजरअंदाज नहीं किया जाना चाहिए।\n\n"
            "अनुमान:\n"
            "I.  लोग टेलीविजन को केवल मनोरंजन का साधन मानते हैं।\n"
            "II. टेलीविजन के शैक्षिक मूल्य को ठीक से नहीं समझा जाता है।"
        ),
        "option_a": "If only assumption I is implicit / यदि केवल अनुमान I अंतर्निहित है",
        "option_b": "If only assumption II is implicit / यदि केवल अनुमान II अंतर्निहित है",
        "option_c": "If either I or II is implicit / यदि I या II अंतर्निहित है",
        "option_d": "If both I and II are implicit / यदि I और II दोनों अंतर्निहित हैं",
        "correct_answer": "D",
        # I: "cannot be ignored" implies TV currently seen as entertainment-only → IMPLICIT ✓
        # II: "cannot be ignored" implies educational value is currently underappreciated → IMPLICIT ✓
    },
    # ── Q18 ── Both assumptions implicit (travel expenses letter) ─────────────
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: A sentence in the letter to the candidates called for written "
            "examinations — 'You have to bear your expenses on travel etc.'\n\n"
            "Assumptions:\n"
            "I.  If not clarified, all the candidates may claim reimbursement of "
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
        # Same reasoning as Q14 — both assumptions underlie the clarification
    },
    # ── Q19 ── Both assumptions implicit (rain and farmers) ───────────────────
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": (
            "A statement is followed by two assumptions I and II. Consider the "
            "statement and the following assumptions and decide which of the "
            "assumption/s is/are implicit in the given statement.\n\n"
            "Statement: If it does not rain throughout this month, most of the "
            "farmers will be in trouble this year.\n\n"
            "Assumptions:\n"
            "I.  Timely rain is essential for farming.\n"
            "II. Most of the farmers are generally dependent on rains."
        ),
        "question_hi": (
            "एक कथन के बाद दो धारणाएँ I और II दी गई हैं। कथन और निम्नलिखित धारणाओं "
            "पर विचार करें और तय करें कि दिए गए कथन में कौन सी धारणा/धारणाएँ "
            "अंतर्निहित हैं।\n\n"
            "कथन: यदि इस महीने में बारिश नहीं होती है, तो इस साल अधिकांश किसान "
            "परेशानी में होंगे।\n\n"
            "धारणाएँ:\n"
            "I.  खेती के लिए समय पर बारिश होना जरूरी है।\n"
            "II. अधिकांश किसान आमतौर पर बारिश पर निर्भर होते हैं।"
        ),
        "option_a": "Neither assumption I nor assumption II is implicit / न तो धारणा I और न ही II अंतर्निहित है",
        "option_b": "Both of the assumptions are implicit / दोनों धारणाएँ अंतर्निहित हैं",
        "option_c": "If only assumption II is implicit / यदि केवल धारणा II अंतर्निहित है",
        "option_d": "If only assumption I is implicit / यदि केवल धारणा I अंतर्निहित है",
        "correct_answer": "B",
        # I: trouble from no rain assumes rain timing is critical for farming → IMPLICIT ✓
        # II: linking most-farmers' trouble to absent rain assumes they depend on rain → IMPLICIT ✓
    },
    # ── Q20 ── Only Assumption I implicit (same statement, third set) ──────────
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: The next meeting of the Governing Board of the Institute will "
            "be held after one year.\n\n"
            "Assumptions:\n"
            "I.  The Institute will remain in function after one year.\n"
            "II. The Governing Board will be dissolved after one year."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: संस्था की शासी बोर्ड की अगली बैठक एक वर्ष बाद होगी।\n\n"
            "अनुमान:\n"
            "I.  संस्था एक वर्ष के बाद भी कार्यरत रहेगी।\n"
            "II. शासी बोर्ड एक वर्ष के बाद भंग हो जाएगा।"
        ),
        "option_a": "If only assumption I is implicit / यदि केवल अनुमान I अंतर्निहित है",
        "option_b": "If only assumption II is implicit / यदि केवल अनुमान II अंतर्निहित है",
        "option_c": "If either I or II is implicit / यदि I या II अंतर्निहित है",
        "option_d": "If neither I nor II is implicit / यदि न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # Same reasoning as Q15/Q16
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
