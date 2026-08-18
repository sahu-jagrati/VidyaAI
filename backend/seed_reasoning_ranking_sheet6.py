"""
seed_reasoning_ranking_sheet6.py
=========================================
Seeds Ranking Q35-Q42 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Ranking
Run     : python seed_reasoning_ranking_sheet6.py

Answer key (all verified via Python):
  Q35  Direction set (total=18); Meena→Beena's orig pos=7th left;
       Meena_new_right = 18-7+1 = 12                                   → C  12
       NOTE: may exist in DB (ans=None); updated below
  Q36  Raman=16th top, 49th bottom; total=16+49-1=64                   → A  64
  Q37  Height order: Radha>Neela>Neena>Nisha>Suja; middle(3rd)=Neena   → B  Neena
  Q38  Height order: Anil>Baby>Sunny>Bose; shortest=Bose               → D  Bose
  Q39  Height order: C>A>D>B>E; 4th=B                                  → D  B
  Q40  Ramesh=13th top; Suresh=33-5=28th top; between=28-13-1=14      → B  14
  Q41  Age order: Priya>Sati>Renu>Geeta; eldest=Priya                  → A  Priya
  Q42  Height order: Rani>Pinky≥Anita>Reema; tallest=Rani              → B  Rani
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Ranking_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Ranking"

# Q35 is the 4th question from the direction set (originally labelled Q32-34, now Q32-35)
_DIR35 = (
    "Directions (Q32-35): 4 students Reena, Beena, Meena and Neena stand in a row. "
    "Reena and Beena are 6th and 7th from the left. Meena and Neena are 4th and 5th "
    "from the right. When Beena and Meena exchange positions, Beena becomes 15th from "
    "the left (total students in row = 18). "
)

QUESTIONS = [
    # ── Q35 ── Meena takes Beena's orig pos (7th left); new_right=18-7+1=12 ──
    # NOTE: may already be in DB with ans=None; updated below if skipped
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": (
            _DIR35 +
            "After the exchange of positions between Beena and Meena, "
            "what is Meena's position from the right end of the row?"
        ),
        "question_hi": (
            "निर्देश (Q32-35): 4 छात्र रीना, बीना, मीना और नीना एक पंक्ति में "
            "खड़े हैं। रीना और बीना बाएँ से 6वें और 7वें स्थान पर हैं। मीना और "
            "नीना दाएँ से 4वें और 5वें स्थान पर हैं। जब बीना और मीना स्थान बदलते "
            "हैं, तो बीना बाएँ से 15वाँ बन जाती है (कुल=18)। "
            "बीना और मीना के स्थान बदलने के बाद मीना दाएँ छोर से कौन-से स्थान पर होगी?"
        ),
        "option_a": "5",
        "option_b": "10",
        "option_c": "12",
        "option_d": "None of these",
        "correct_answer": "C",   # Meena→7th left; 18-7+1=12
    },
    # ── Q36 ── total = 16+49-1 = 64 ───────────────────────────────────────────
    {
        "question_number": 36,
        "difficulty": "easy",
        "question_en": (
            "Raman is a student of class 10. He ranks 16th from the top and "
            "49th from the bottom in his class. What is the total number of "
            "students in the class?"
        ),
        "question_hi": (
            "रमन कक्षा 10 का विद्यार्थी है। वह अपनी कक्षा में ऊपर से 16वें और "
            "नीचे से 49वें स्थान पर है। कक्षा में कुल विद्यार्थियों की संख्या "
            "क्या है?"
        ),
        "option_a": "64",
        "option_b": "25",
        "option_c": "55",
        "option_d": "63",
        "correct_answer": "A",   # total=16+49-1=64
    },
    # ── Q37 ── Order: Radha>Neela>Neena>Nisha>Suja; middle(3rd)=Neena ─────────
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": (
            "Nisha is taller than Suja and Neena is taller than Nisha and "
            "Neela is taller than Neena. But Radha is the tallest. If they "
            "all stand in order of their height, then who will be standing "
            "in the middle?"
        ),
        "question_hi": (
            "निशा, सुजा से लम्बी है और नीना, निशा से लम्बी है तथा नीला, नीना "
            "से लम्बी है। लेकिन राधा सबसे अधिक लम्बी है। यदि वे सब लम्बाई के "
            "क्रम में खड़ी हो जाएँ, तो बीच में कौन खड़ी होगी?"
        ),
        "option_a": "Nisha/निशा",
        "option_b": "Neena/नीना",
        "option_c": "Suja/सुजा",
        "option_d": "Neela/नीला",
        "correct_answer": "B",   # Radha>Neela>Neena>Nisha>Suja; 3rd=Neena
    },
    # ── Q38 ── Order: Anil>Baby>Sunny>Bose; shortest=Bose ────────────────────
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": (
            "Anil is taller than Sunny and Sunny is shorter than Baby. "
            "Anil is taller than Bose, who is shorter than Sunny. Baby is "
            "shorter than Anil. Tell who is the shortest?"
        ),
        "question_hi": (
            "अनिल का कद सन्नी से लम्बा है और सन्नी का कद बेबी से छोटा है। "
            "अनिल का कद बोस से लम्बा है, जिसका कद सन्नी से छोटा है। बेबी "
            "अनिल के कद से छोटी है। यह बताइए कि किसका कद सबसे छोटा है?"
        ),
        "option_a": "Anil/अनिल",
        "option_b": "Baby/बेबी",
        "option_c": "Sunny/सन्नी",
        "option_d": "Bose/बोस",
        "correct_answer": "D",   # Anil>Baby>Sunny>Bose; shortest=Bose
    },
    # ── Q39 ── Height order: C>A>D>B>E; 4th=B ────────────────────────────────
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": (
            "There are five children A, B, C, D and E. Among them, B is taller "
            "than E but shorter than A. A is shorter than C but taller than D, "
            "while D is taller than B. If all the children are made to stand in "
            "a row according to their height, then who will be fourth in terms "
            "of height?"
        ),
        "question_hi": (
            "A, B, C, D और E पाँच बच्चे हैं। इनमें B, E से लम्बा है, किन्तु A से "
            "छोटा है। A, C से छोटा है, पर D से लम्बा है, जबकि D, B से लम्बा है। "
            "यदि सभी बच्चों को एक पंक्ति में लम्बाई के अनुसार खड़ा किया जाए, "
            "तो लम्बाई के अनुसार चौथे नम्बर पर कौन होगा?"
        ),
        "option_a": "A",
        "option_b": "E",
        "option_c": "D",
        "option_d": "B",
        "correct_answer": "D",   # C>A>D>B>E; 4th=B (stored as option_d)
    },
    # ── Q40 ── Suresh=28th top; between=28-13-1=14 ───────────────────────────
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": (
            "Ramesh ranks 13th in a class of 33 students. There are 5 students "
            "below Suresh in ranking. How many students are there between "
            "Ramesh and Suresh?"
        ),
        "question_hi": (
            "रमेश 33 विद्यार्थियों की एक कक्षा में 13वें स्थान पर है। श्रेणी "
            "अनुसार सुरेश के नीचे 5 विद्यार्थी हैं तो रमेश और सुरेश के बीच कितने "
            "विद्यार्थी हैं?"
        ),
        "option_a": "12",
        "option_b": "14",
        "option_c": "15",
        "option_d": "16",
        "correct_answer": "B",   # Suresh=33-5=28th; between=28-13-1=14
    },
    # ── Q41 ── Age order: Priya>Sati>Renu>Geeta; eldest=Priya ───────────────
    {
        "question_number": 41,
        "difficulty": "easy",
        "question_en": (
            "Sati is elder than Renu. Geeta is younger than Renu. Priya is "
            "elder than Sati. Tell me who is the eldest among them?"
        ),
        "question_hi": (
            "सती रेनु से बड़ी है। गीता रेनु से छोटी है। प्रिया सती से बड़ी है। "
            "यह बताएं उनमें सबसे बड़ी कौन है?"
        ),
        "option_a": "Priya/प्रिया",
        "option_b": "Sati/सती",
        "option_c": "Renu/रेनु",
        "option_d": "Geeta/गीता",
        "correct_answer": "A",   # Priya>Sati>Renu>Geeta; eldest=Priya
    },
    # ── Q42 ── Height order: Rani>Pinky≥Anita>Reema; tallest=Rani ───────────
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": (
            "Anita is taller than Reema but not taller than Pinky. Pinky is "
            "shorter than her cousin Rani but not shorter than Reema. Tell "
            "who is the tallest in the group?"
        ),
        "question_hi": (
            "अनीता रीमा से लम्बी है लेकिन पिंकी से लम्बी नहीं है। पिंकी अपनी "
            "चचेरी बहन रानी से छोटी है लेकिन रीमा से छोटी नहीं है। यह बताइए "
            "कि ग्रुप में सबसे लम्बी कौन है?"
        ),
        "option_a": "Anita/अनीता",
        "option_b": "Rani/रानी",
        "option_c": "Pinky/पिंकी",
        "option_d": "Reema/रीमा",
        "correct_answer": "B",   # Rani>Pinky≥Anita>Reema; tallest=Rani
    },
]

# Fix map for any pre-existing records (ans=None) that get skipped by deduplication
# key: question_number → (correct_answer, {field: clean_value, ...})
_FIXES = {
    35: ("C", {
        "option_a": "5",
        "option_b": "10",
        "option_c": "12",
        "option_d": "None of these",
        "question_hi": (
            "निर्देश (Q32-35): 4 छात्र रीना, बीना, मीना और नीना एक पंक्ति में "
            "खड़े हैं। रीना और बीना बाएँ से 6वें और 7वें स्थान पर हैं। मीना और "
            "नीना दाएँ से 4वें और 5वें स्थान पर हैं। जब बीना और मीना स्थान बदलते "
            "हैं, तो बीना बाएँ से 15वाँ बन जाती है (कुल=18)। "
            "बीना और मीना के स्थान बदलने के बाद मीना दाएँ छोर से कौन-से स्थान पर होगी?"
        ),
    }),
    36: ("A", {"option_a": "64", "option_b": "25", "option_c": "55", "option_d": "63"}),
    37: ("B", {
        "option_a": "Nisha/निशा",
        "option_b": "Neena/नीना",
        "option_c": "Suja/सुजा",
        "option_d": "Neela/नीला",
    }),
    38: ("D", {
        "option_a": "Anil/अनिल",
        "option_b": "Baby/बेबी",
        "option_c": "Sunny/सन्नी",
        "option_d": "Bose/बोस",
    }),
    39: ("D", {"option_a": "A", "option_b": "E", "option_c": "D", "option_d": "B"}),
    40: ("B", {"option_a": "12", "option_b": "14", "option_c": "15", "option_d": "16"}),
    41: ("A", {
        "option_a": "Priya/प्रिया",
        "option_b": "Sati/सती",
        "option_c": "Renu/रेनु",
        "option_d": "Geeta/गीता",
    }),
    42: ("B", {
        "option_a": "Anita/अनीता",
        "option_b": "Rani/रानी",
        "option_c": "Pinky/पिंकी",
        "option_d": "Reema/रीमा",
    }),
}


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

        # ── Fix any pre-existing records that were skipped ────────────────────
        updates = 0
        for qnum, (ans, fields) in _FIXES.items():
            q = db.query(Question).filter(
                Question.topic == TOPIC,
                Question.subject == SUBJECT,
                Question.question_number == qnum,
                Question.correct_answer == None,
            ).first()
            if q:
                q.correct_answer = ans
                for field, val in fields.items():
                    setattr(q, field, val)
                q.source_pdf = SOURCE
                updates += 1
                print(f"  UPDATE Q{qnum}: correct_answer={ans}, options cleaned")

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
