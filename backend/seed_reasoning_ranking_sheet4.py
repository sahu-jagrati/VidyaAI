"""
seed_reasoning_ranking_sheet4.py
=========================================
Seeds Ranking Q22-Q28 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Ranking
Run     : python seed_reasoning_ranking_sheet4.py

Answer key (all verified via Python):
  Q22  16 girls between Priya (32nd left) & Natasha; Priya nearer right;
       Natasha_left = 32-(16+1) = 15                                      → C  15th
       NOTE: exists in DB with ans=None; handled via update below
  Q23  Shikhar=9th back, Arun=8th front, Nikhil between; min boys?
       min = (8+9)-1-2 = 14                                               → D  14
  Q24  Monika shifted 4 right → 12th from left; earlier pos from right?
       earlier_left=8; earlier_right=21-8+1=14
       NOTE: exists in DB with garbled opts; fixed via update below       → D  14th
  Q25  Pallavi=21st right; Reena=31st right; Malini=27th right=17th left;
       total=17+27-1=43                                                    → B  43
  Q26  Peter=12th right shifts 3 left → new_right=15, new_left=10;
       total=10+15-1=24                                                    → D  24
  Q27  A=10th left, B=9th right; interchange → A=15th left (B's pos=9th right);
       total=15+9-1=23                                                     → A  23
  Q28  Ashish=15th left, Sachin=7th right; interchange → Sachin=15th left, 15th right;
       total=15+15-1=29                                                    → C  29
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Ranking_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Ranking"

QUESTIONS = [
    # ── Q22 ── Natasha_left = 32 - (16+1) = 15 ───────────────────────────────
    # NOTE: already in DB with ans=None; will be SKIPPED → updated separately
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "In a row of girls, there are 16 girls between Priya and Natasha. "
            "Priya is thirty-second from the left end of the row. If Priya is "
            "nearer than Natasha to the right end of the row, then how far away "
            "is Natasha from the left end of the row?"
        ),
        "question_hi": (
            "लड़कियों की एक पंक्ति में प्रिया और नताशा के बीच में 16 लड़कियाँ "
            "हैं। प्रिया पंक्ति में बाएँ छोर से 32वें स्थान पर है। यदि प्रिया "
            "नताशा की तुलना में पंक्ति के दाएँ छोर से पास है तो बाएँ छोर से "
            "नताशा कितने स्थान दूर है?"
        ),
        "option_a": "Data inadequate",
        "option_b": "14th",
        "option_c": "15th",
        "option_d": "16th",
        "correct_answer": "C",   # 32-(16+1)=15
    },
    # ── Q23 ── min total = (8+9)-1-2 = 14 ────────────────────────────────────
    {
        "question_number": 23,
        "difficulty": "hard",
        "question_en": (
            "In a queue, Shikhar is ninth from the back. Arun's place is eighth "
            "from the front. Nikhil is standing between the two. What could be "
            "the minimum number of boys standing in the queue?"
        ),
        "question_hi": (
            "एक पंक्ति में शिखर पीछे से 9वाँ है। अरुण का स्थान सामने से आठवाँ "
            "है। निखिल दोनों के बीच में है, तो पंक्ति में कम से कम कितने लड़के "
            "हो सकते हैं?"
        ),
        "option_a": "8",
        "option_b": "10",
        "option_c": "12",
        "option_d": "14",
        "correct_answer": "D",   # min=(8+9)-1-2=14 (overlapping case)
    },
    # ── Q24 ── earlier_right = 21-8+1 = 14 ───────────────────────────────────
    # NOTE: already in DB with ans=None and garbled opts; updated separately
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": (
            "In a row of 21 girls, when Monika was shifted by four places towards "
            "the right, she became 12th from the left end. What was her earlier "
            "position from the right end of the row?"
        ),
        "question_hi": (
            "21 लड़कियों की एक पंक्ति में मोनिका का स्थान दाएँ से खिसककर 12वें "
            "स्थान पर आ जाती है तो दाएँ छोर से 12वें स्थान पर हो जाती है तो "
            "पंक्ति में उसकी पूर्व स्थिति क्या थी?"
        ),
        "option_a": "9th",
        "option_b": "10th",
        "option_c": "11th",
        "option_d": "14th",
        "correct_answer": "D",   # earlier_left=8; earlier_right=21-8+1=14
    },
    # ── Q25 ── Reena_right=31; Malini_right=27; total=17+27-1=43 ────────────
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": (
            "In a row of girls facing North, Reena is 10th to the left of Pallavi, "
            "who is 21st from the right end. If Malini, who is 17th from the left "
            "end, is fourth to the right of Reena, how many girls are there in the row?"
        ),
        "question_hi": (
            "उत्तर की ओर मुख करके खड़ी लड़कियों की एक पंक्ति में रीना, पल्लवी "
            "के बाएँ से 10वाँ स्थान पर है जो दाएँ छोर से 21वाँ है। यदि मालिनी "
            "जो बाएँ छोर से 17वीं है, रीना की दाएँ से चौथी है तो पंक्ति में "
            "कितनी लड़कियाँ हैं?"
        ),
        "option_a": "37",
        "option_b": "43",
        "option_c": "44",
        "option_d": "Data inadequate",
        "correct_answer": "B",   # Malini_right=27; total=17+27-1=43
    },
    # ── Q26 ── Peter new_right=15; total=10+15-1=24 ──────────────────────────
    {
        "question_number": 26,
        "difficulty": "hard",
        "question_en": (
            "George is fifth from the left and Peter is twelfth from the right end "
            "in a row of children. If Peter shifts by three places towards George, "
            "he becomes tenth from the left end. How many children are there in the row?"
        ),
        "question_hi": (
            "बच्चों की एक पंक्ति में जॉर्ज बाएँ से पाँचवाँ है और पीटर दाएँ छोर "
            "से 12वाँ है। यदि पीटर जॉर्ज की तरफ तीन स्थान खिसकता है तो वह बाएँ "
            "छोर से 10वें स्थान पर आ जाता है, तो पंक्ति में कितने बच्चे हैं?"
        ),
        "option_a": "21",
        "option_b": "22",
        "option_c": "23",
        "option_d": "24",
        "correct_answer": "D",   # Peter_new_right=15; total=10+15-1=24
    },
    # ── Q27 ── After interchange A=15th left, 9th right; total=15+9-1=23 ─────
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "In a row of boys, if A who is tenth from the left and B who is ninth "
            "from the right interchange their positions, A becomes fifteenth from "
            "the left. How many boys are there in the row?"
        ),
        "question_hi": (
            "लड़कों की एक पंक्ति में यदि A जो बाएँ से 10वें स्थान पर है और B "
            "जो दाएँ से नौवें है आपस में एक दूसरे से अपने स्थान बदलते हैं तो "
            "A बाएँ से 15वाँ बन जाता है, तो पंक्ति में कितने लड़के हैं?"
        ),
        "option_a": "23",
        "option_b": "27",
        "option_c": "28",
        "option_d": "31",
        "correct_answer": "A",   # A takes B's pos (9th right); total=15+9-1=23
    },
    # ── Q28 ── After interchange Sachin=15th left, 15th right; total=29 ──────
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            "Students line up in a queue in which Ashish stands fifteenth from the "
            "left and Sachin is seventh from the right. If they interchange their "
            "places, Sachin would be fifteenth from the right. How many students "
            "are there in the queue?"
        ),
        "question_hi": (
            "विद्यार्थियों की एक पंक्ति में आशीष बाएँ से 15वाँ है और सचिन दाएँ "
            "से 7वाँ है। यदि वे आपस में अपने स्थान बदलते हैं तो सचिन दाएँ से "
            "15वाँ होगा, तो पंक्ति में कितने विद्यार्थी हैं?"
        ),
        "option_a": "21",
        "option_b": "22",
        "option_c": "29",
        "option_d": "None of these",
        "correct_answer": "C",   # Sachin_new_left=15, new_right=15; total=15+15-1=29
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_short = {
            row[0][:80]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            fp = d["question_en"][:80]
            if fp in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB (will update separately)")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")

        # ── Fix Q22 and Q24 that were skipped ────────────────────────────────
        updates = 0
        for qnum, ans, opt_d, q_hi in [
            (22, "C", "16th",
             "लड़कियों की एक पंक्ति में प्रिया और नताशा के बीच में 16 लड़कियाँ हैं। प्रिया पंक्ति में बाएँ छोर से 32वें स्थान पर है। यदि प्रिया नताशा की तुलना में पंक्ति के दाएँ छोर से पास है तो बाएँ छोर से नताशा कितने स्थान दूर है?"),
            (24, "D", "14th",
             "21 लड़कियों की एक पंक्ति में मोनिका का स्थान दाएँ से खिसककर 12वें स्थान पर आ जाती है, तो पंक्ति में उसकी पूर्व स्थिति दाएँ छोर से क्या थी?"),
        ]:
            q = db.query(Question).filter(
                Question.topic == TOPIC,
                Question.subject == SUBJECT,
                Question.question_number == qnum,
                Question.correct_answer == None,
            ).first()
            if q:
                q.correct_answer = ans
                q.option_d = opt_d          # fix garbled option_d
                q.question_hi = q_hi        # clean Hindi text
                q.source_pdf = SOURCE
                updates += 1
                print(f"  UPDATE Q{qnum}: set correct_answer={ans}, fixed option_d={opt_d!r}")

        db.commit()
        if updates:
            print(f"Fixed {updates} pre-existing records.")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
