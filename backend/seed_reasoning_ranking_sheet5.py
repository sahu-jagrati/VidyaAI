"""
seed_reasoning_ranking_sheet5.py
=========================================
Seeds Ranking Q29-Q34 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Ranking
Run     : python seed_reasoning_ranking_sheet5.py

Answer key (all verified via Python):
  Q29  Deepti=9th left, Kashish=13th right; exchange→Deepti=17th left;
       total=17+13-1=29; Kashish_new_right=29-9+1=21               → B  21st
       NOTE: exists in DB (ans=None); updated below
  Q30  Rita=9th right, Monika=10th left; exchange→Rita=17th right;
       total=10+17-1=26                                              → B  26
  Q31  Vilas=26th left; Kewal=16th; 3 boys between Kewal&Satish →
       Satish=20 or 12; Rohan=10 or 2 (ambiguous) → Data inadequate → D  Data inadequate
       NOTE: exists in DB (garbled opts); updated below
  Q32  Direction set: Reena=6th left, Beena=7th left, Meena=4th right,
       Neena=5th right; exchange Beena↔Meena→Beena=15th left, total=18;
       Neena's actual position from left = 18-5+1 = 14              → C  14
  Q33  Same direction: Reena from right = 18-6+1 = 13               → B  13
  Q34  Same direction: After Neena↔Reena exchange, Neena takes
       Reena's position = 6th from left                             → A  6
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Ranking_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Ranking"

# Direction text shared by Q32-Q34
_DIR = (
    "Directions (Q32-34): 4 students Reena, Beena, Meena and Neena stand in a row. "
    "Reena and Beena are 6th and 7th from the left. Meena and Neena are 4th and 5th "
    "from the right. When Beena and Meena exchange positions, Beena becomes 15th from "
    "the left (total students in row = 18). "
)

QUESTIONS = [
    # ── Q29 ── total=17+13-1=29; Kashish new right=29-9+1=21 ────────────────
    # NOTE: already in DB with ans=None; cleaned & updated below
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": (
            "In a row of children, Deepti is ninth from the left and Kashish is "
            "thirteenth from the right. They exchange their positions and then "
            "Deepti becomes seventeenth from the left. Find the new position of "
            "Kashish from the right end of the row."
        ),
        "question_hi": (
            "बच्चों की एक पंक्ति में दीप्ति बाएँ से 9वीं है और काशिश दाएँ से "
            "13वीं है। वे आपस में अपना स्थान बदलते हैं और दीप्ति बाएँ से 17वीं "
            "हो जाती है, तो पंक्ति में दाएँ छोर से काशिश का नया स्थान क्या है?"
        ),
        "option_a": "20th",
        "option_b": "21st",
        "option_c": "27th",
        "option_d": "None of these",
        "correct_answer": "B",   # total=29; Kashish_new_right=29-9+1=21
    },
    # ── Q30 ── total=10+17-1=26 ──────────────────────────────────────────────
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "In a row of girls, Rita and Monika occupy the ninth place from the "
            "right and tenth place from the left end, respectively. If they "
            "interchange their places, then Rita and Monika occupy seventeenth "
            "place from the right and eighteenth place from the left respectively. "
            "How many girls are there in the row?"
        ),
        "question_hi": (
            "लड़कियों की एक पंक्ति में रीता और मोनिका क्रमानुसार दाएँ छोर से "
            "9वाँ और बाएँ छोर से 10वाँ स्थान लेती हैं। यदि वे आपस में अपना "
            "स्थान बदल लेती हैं तो रीता और मोनिका क्रमानुसार 17वाँ दाएँ और "
            "18वाँ स्थान बाएँ से लेती हैं, तो पंक्ति में कितनी लड़कियाँ हैं?"
        ),
        "option_a": "25",
        "option_b": "26",
        "option_c": "27",
        "option_d": "Data inadequate",
        "correct_answer": "B",   # Rita new_left=10, new_right=17; total=10+17-1=26
    },
    # ── Q31 ── two possible positions → Data inadequate ──────────────────────
    # NOTE: already in DB with garbled opts; cleaned & updated below
    {
        "question_number": 31,
        "difficulty": "hard",
        "question_en": (
            "In a row of 40 boys, Satish was shifted 10 places to the right of "
            "Rohan and Kewal was shifted 10 places to the left of Vilas. If Vilas "
            "was twenty-sixth from the left end and there were three boys between "
            "Kewal and Satish after shifting, what was the position of Rohan in the row?"
        ),
        "question_hi": (
            "40 लड़कों की एक पंक्ति में सतीश, रोहन के दाएँ 10 स्थान खिसकता है "
            "और केवल, विलास के बाएँ 10 स्थान खिसकता है। यदि विलास बाएँ से 26वाँ "
            "है और खिसकने के बाद केवल और सतीश के बीच तीन लड़के हैं, तो पंक्ति में "
            "रोहन का कौनसा स्थान है?"
        ),
        "option_a": "10th from right end",
        "option_b": "10th from left end",
        "option_c": "39th from right end",
        "option_d": "Data inadequate",
        "correct_answer": "D",   # Satish=20 or 12 → Rohan=10 or 2; ambiguous
    },
    # ── Q32 ── Neena_left = 18-5+1 = 14 ─────────────────────────────────────
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": _DIR + "What is Neena's actual position from the left?",
        "question_hi": (
            "निर्देश (Q32-34): 4 छात्र रीना, बीना, मीना और नीना एक पंक्ति में "
            "खड़े हैं। रीना और बीना बाएँ से 6वें और 7वें स्थान पर हैं। मीना और "
            "नीना दाएँ से 4वें और 5वें स्थान पर हैं। जब बीना और मीना स्थान बदलते "
            "हैं, तो बीना बाएँ से 15वाँ बन जाती है (कुल=18)। "
            "वास्तविक रूप से नीना का बाएँ से कौन-सा स्थान है?"
        ),
        "option_a": "5",
        "option_b": "8",
        "option_c": "14",
        "option_d": "16",
        "correct_answer": "C",   # Neena_left=18-5+1=14
    },
    # ── Q33 ── Reena_right = 18-6+1 = 13 ────────────────────────────────────
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": _DIR + "What is Reena's position from the right?",
        "question_hi": (
            "निर्देश (Q32-34) [same setup as Q32]। "
            "रीना का दाएँ से कौन-सा स्थान है?"
        ),
        "option_a": "6",
        "option_b": "13",
        "option_c": "14",
        "option_d": "18",
        "correct_answer": "B",   # Reena_right=18-6+1=13
    },
    # ── Q34 ── After Neena↔Reena exchange, Neena=6th from left ───────────────
    {
        "question_number": 34,
        "difficulty": "medium",
        "question_en": (
            _DIR +
            "Neena is 14th from left, Reena is 6th from left. "
            "If Neena and Reena also exchange their positions, "
            "what is Neena's new position from the left?"
        ),
        "question_hi": (
            "निर्देश (Q32-34) [same setup as Q32]। "
            "यदि नीना और रीना आपस में अपने स्थान बदलती हैं, "
            "तो नीना का बाएँ से कौन-सा स्थान होगा?"
        ),
        "option_a": "6",
        "option_b": "10",
        "option_c": "8",
        "option_d": "None of these",
        "correct_answer": "A",   # Neena takes Reena's spot=6th from left
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
                print(f"  SKIP  Q{d['question_number']}: already in DB (will update below)")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")

        # ── Fix Q29 and Q31 that were skipped ────────────────────────────────
        updates = 0

        # Q29: options are clean, just need answer set
        q29 = db.query(Question).filter(
            Question.topic == TOPIC, Question.subject == SUBJECT,
            Question.question_number == 29, Question.correct_answer == None,
        ).first()
        if q29:
            q29.correct_answer = "B"
            q29.option_d = "None of these"   # strip trailing "/"
            q29.source_pdf = SOURCE
            updates += 1
            print(f"  UPDATE Q29: correct_answer=B")

        # Q31: options are badly garbled — replace all option text
        q31 = db.query(Question).filter(
            Question.topic == TOPIC, Question.subject == SUBJECT,
            Question.question_number == 31, Question.correct_answer == None,
        ).first()
        if q31:
            q31.correct_answer = "D"
            q31.option_a = "10th from right end"
            q31.option_b = "10th from left end"
            q31.option_c = "39th from right end"
            q31.option_d = "Data inadequate"
            q31.question_hi = (
                "40 लड़कों की एक पंक्ति में सतीश, रोहन के दाएँ 10 स्थान खिसकता है "
                "और केवल, विलास के बाएँ 10 स्थान खिसकता है। यदि विलास बाएँ से 26वाँ "
                "है और खिसकने के बाद केवल और सतीश के बीच तीन लड़के हैं, तो पंक्ति में "
                "रोहन का कौनसा स्थान है?"
            )
            q31.source_pdf = SOURCE
            updates += 1
            print(f"  UPDATE Q31: correct_answer=D, all options cleaned")

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
