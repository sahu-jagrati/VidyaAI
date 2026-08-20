"""
seed_reasoning_syllogism_sheet2.py
====================================
Seeds Reasoning → Syllogism  Q4–Q8 (Sheet 2).
Subject : Reasoning
Topic   : Syllogism

Option formats used
───────────────────
Q4, Q5 — standard 4-opt (2 conclusions):
  A = Only conclusion I follows.
  B = Only conclusion II follows.
  C = Both conclusions I and II follow.
  D = Neither conclusion I nor II follows.

Q6 — 3-conclusion 4-opt (custom):
  A = Only conclusion 1 follows.
  B = Only conclusion 2 follows.
  C = Only conclusion 3 follows.
  D = Both conclusions 1 and 3 follow.

Q7 — 3-conclusion 4-opt (custom):
  A = Both conclusions 1 and 3 follow.
  B = Both conclusions 2 and 3 follow.
  C = All conclusions 1, 2 and 3 follow.
  D = Both conclusions 1 and 2 follow.

Q8 — 3-conclusion 4-opt (custom, same structure as Q7):
  A = Both conclusions 1 and 3 follow.
  B = Both conclusions 2 and 3 follow.
  C = All conclusions 1, 2 and 3 follow.
  D = Both conclusions 1 and 2 follow.

Answer key:
  Q4  C  (GD Constable, 20 Feb 2024 Shift-1)
  Q5  D  (CGL, 24 Sep 2024 Shift-3)
  Q6  D  (CHSL Tier-II, 10 Jan 2024 Shift-1)
  Q7  C  (CHSL Tier-II, 10 Jan 2024 Shift-1)
  Q8  B  (CHSL Tier-II, 10 Jan 2024 Shift-1)

Reasoning notes
───────────────
Q4  All bats→balls; All balls→badminton; All badminton→wickets.
    I:  All bats are wickets → full chain (A+A+A) ✓
    II: Some badmintons are bats → All bats→badminton by chain;
        I-conversion gives Some badminton are bats ✓

Q5  All grains→cereals; Some cereals are fruits; No fruit is vegetable.
    I:  All cereals CAN BE vegetables — impossible: those cereals that
        are fruits CANNOT be vegetables (No F is V), so "all" cannot hold ✗
    II: All grains are fruits — All G→C + Some C are F does not force
        all grains to be in the fruit subset ✗

Q6  All apples→plums; Some plums are berries; Some berries are coconuts.
    1:  Some berries are plums → I-conversion of Stmt 2 ✓
    2:  All plums are apples → invalid A-conversion of Stmt 1 ✗
    3:  Some coconuts are berries → I-conversion of Stmt 3 ✓
    → Both 1 and 3 follow (option D).

Q7  Some kites are bells; All bells are pumps; All pumps are skates.
    1:  Some kites are skates → Some K→Be→P→S ✓
    2:  Some skates are bells → All Be→P→S, so All Be⊆S;
        I-conversion: Some S are Be ✓
    3:  Some skates are pumps → All P→S; I-conversion: Some S are P ✓
    → All 1, 2, 3 follow (option C).

Q8  Some kites are bells; Some tables are skates; All clocks are skates.
    1:  Some clocks are tables → no valid path between clocks and tables ✗
    2:  Some skates are tables → I-conversion of Stmt 2 ✓
    3:  Some skates are clocks → All clocks→skates; I-conversion ✓
    → Both 2 and 3 follow (option B).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Syllogism"

# Standard 2-conclusion options
_A2 = "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।"
_B2 = "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।"
_C2 = "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।"
_D2 = "Neither conclusion I nor II follows. / न तो निष्कर्ष I और न ही II अनुसरण करता है।"

QUESTIONS = [

    # ── Q4 (GD Constable, 20 Feb 2024 Shift-1) ──────────────────────────────
    # All bats→balls→badminton→wickets.
    # I:  All bats are wickets (full A-chain) ✓
    # II: Some badmintons are bats (All bats→badminton by chain; I-conversion) ✓
    {
        "question_number": 4,
        "difficulty": "easy",
        "source_pdf": "GD_Constable_20Feb2024_Shift1",
        "question_en": (
            "Three statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, decide which of the conclusions "
            "logically follow(s).\n\n"
            "Statement I:   All bats are balls.\n"
            "Statement II:  All balls are badminton.\n"
            "Statement III: All badminton is wickets.\n\n"
            "Conclusion I:  All bats are wickets.\n"
            "Conclusion II: Some badmintons are bats."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   सभी बल्ले, गेंद हैं।\n"
            "कथन II:  सभी गेंद, बैडमिंटन हैं।\n"
            "कथन III: सभी बैडमिंटन, विकेट हैं।\n\n"
            "निष्कर्ष I:  सभी बल्ले, विकेट हैं।\n"
            "निष्कर्ष II: कुछ बैडमिंटन, बल्ले हैं।"
        ),
        "option_a": _A2,
        "option_b": _B2,
        "option_c": _C2,
        "option_d": _D2,
        "correct_answer": "C",
    },

    # ── Q5 (CGL, 24 Sep 2024 Shift-3) ───────────────────────────────────────
    # All grains→cereals; Some cereals are fruits; No fruit is vegetable.
    # I:  All cereals CAN BE vegetables — impossible (fruit-cereals ≠ vegetables) ✗
    # II: All grains are fruits — All G→C + Some C are F doesn't force G⊆F ✗
    {
        "question_number": 5,
        "difficulty": "medium",
        "source_pdf": "CGL_24Sep2024_Shift3",
        "question_en": (
            "In this question, three statements are given, followed by two conclusions "
            "numbered I and II. Assuming the statements to be true, even if they seem "
            "to be at variance with commonly known facts, decide which of the "
            "conclusion(s) logically follows/follow from the statements.\n\n"
            "Statements:\n"
            "All grains are cereals.\n"
            "Some cereals are fruits.\n"
            "No fruit is a vegetable.\n\n"
            "Conclusions:\n"
            "I.  All cereals can be vegetables.\n"
            "II. All grains are fruits."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष "
            "दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों "
            "से भिन्न प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी अनाज, धान्य हैं।\n"
            "कुछ धान्य, फल हैं।\n"
            "कोई भी फल, सब्जी नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी धान्य, सब्जी हो सकते हैं।\n"
            "II. सभी अनाज, फल हैं।"
        ),
        "option_a": _A2,
        "option_b": _B2,
        "option_c": _C2,
        "option_d": _D2,
        "correct_answer": "D",
    },

    # ── Q6 (CHSL Tier-II, 10 Jan 2024 Shift-1) ──────────────────────────────
    # 3-conclusion question — custom option set.
    # All apples→plums; Some plums are berries; Some berries are coconuts.
    # 1: Some berries are plums   → I-conv of Stmt 2 ✓
    # 2: All plums are apples     → invalid conversion of Stmt 1 ✗
    # 3: Some coconuts are berries → I-conv of Stmt 3 ✓
    # Both 1 and 3 follow → option D.
    {
        "question_number": 6,
        "difficulty": "medium",
        "source_pdf": "CHSL_TierII_10Jan2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. You have to take the "
            "given statements to be true even if they seem to be at variance with "
            "commonly known facts. You have to decide which conclusion/s logically "
            "follow/s from the given statements.\n\n"
            "Statements:\n"
            "All apples are plums.\n"
            "Some plums are berries.\n"
            "Some berries are coconuts.\n\n"
            "Conclusions:\n"
            "1. Some berries are plums.\n"
            "2. All plums are apples.\n"
            "3. Some coconuts are berries."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। आपको दिए गए "
            "कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत होते हों। आपको यह तय करना है कि दिए गए कथनों में "
            "से कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी सेब, आलूबुखारे हैं।\n"
            "कुछ आलूबुखारे, जामुन हैं।\n"
            "कुछ जामुन, नारियल हैं।\n\n"
            "निष्कर्ष:\n"
            "1. कुछ जामुन, आलूबुखारे हैं।\n"
            "2. सभी आलूबुखारे, सेब हैं।\n"
            "3. कुछ नारियल, जामुन हैं।"
        ),
        "option_a": "Only conclusion 1 follows. / केवल निष्कर्ष 1 अनुसरण करता है।",
        "option_b": "Only conclusion 2 follows. / केवल निष्कर्ष 2 अनुसरण करता है।",
        "option_c": "Only conclusion 3 follows. / केवल निष्कर्ष 3 अनुसरण करता है।",
        "option_d": "Both conclusions 1 and 3 follow. / निष्कर्ष 1 और 3 दोनों अनुसरण करते हैं।",
        "correct_answer": "D",
    },

    # ── Q7 (CHSL Tier-II, 10 Jan 2024 Shift-1) ──────────────────────────────
    # 3-conclusion question — custom option set.
    # Some kites are bells; All bells are pumps; All pumps are skates.
    # 1: Some kites are skates   → Some K→Be→P→S ✓
    # 2: Some skates are bells   → All Be→P→S; All Be⊆S; I-conv: Some S are Be ✓
    # 3: Some skates are pumps   → All P→S; I-conv: Some S are P ✓
    # All 1, 2, 3 follow → option C.
    {
        "question_number": 7,
        "difficulty": "medium",
        "source_pdf": "CHSL_TierII_10Jan2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. You have to take the "
            "given statements to be true even if they seem to be at variance with "
            "commonly known facts. You have to decide which conclusion/s logically "
            "follow/s from the given statements.\n\n"
            "Statements:\n"
            "Some kites are bells.\n"
            "All bells are pumps.\n"
            "All pumps are skates.\n\n"
            "Conclusions:\n"
            "1. Some kites are skates.\n"
            "2. Some skates are bells.\n"
            "3. Some skates are pumps."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। आपको दिए गए "
            "कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत होते हों। आपको यह तय करना है कि दिए गए कथनों में "
            "से कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ पतंगें घंटियाँ हैं।\n"
            "सभी घंटियाँ पम्प हैं।\n"
            "सभी पम्प स्केट्स हैं।\n\n"
            "निष्कर्ष:\n"
            "1. कुछ पतंगें स्केट्स हैं।\n"
            "2. कुछ स्केट्स घंटियाँ हैं।\n"
            "3. कुछ स्केट्स पम्प हैं।"
        ),
        "option_a": "Both conclusions 1 and 3 follow. / निष्कर्ष 1 और 3 दोनों अनुसरण करते हैं।",
        "option_b": "Both conclusions 2 and 3 follow. / निष्कर्ष 2 और 3 दोनों अनुसरण करते हैं।",
        "option_c": "All conclusions 1, 2 and 3 follow. / सभी निष्कर्ष 1, 2 और 3 अनुसरण करते हैं।",
        "option_d": "Both conclusions 1 and 2 follow. / निष्कर्ष 1 और 2 दोनों अनुसरण करते हैं।",
        "correct_answer": "C",
    },

    # ── Q8 (CHSL Tier-II, 10 Jan 2024 Shift-1) ──────────────────────────────
    # 3-conclusion question — custom option set.
    # Some kites are bells; Some tables are skates; All clocks are skates.
    # 1: Some clocks are tables  → no valid inferential path ✗
    # 2: Some skates are tables  → I-conv of Stmt 2 ✓
    # 3: Some skates are clocks  → All clocks→skates; I-conv ✓
    # Both 2 and 3 follow → option B.
    {
        "question_number": 8,
        "difficulty": "medium",
        "source_pdf": "CHSL_TierII_10Jan2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. You have to take the "
            "given statements to be true even if they seem to be at variance with "
            "commonly known facts. You have to decide which conclusion/s logically "
            "follow/s from the given statements.\n\n"
            "Statements:\n"
            "Some kites are bells.\n"
            "Some tables are skates.\n"
            "All clocks are skates.\n\n"
            "Conclusions:\n"
            "1. Some clocks are tables.\n"
            "2. Some skates are tables.\n"
            "3. Some skates are clocks."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। आपको दिए गए "
            "कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत होते हों। आपको यह तय करना है कि दिए गए कथनों में "
            "से कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ पतंगें घंटियाँ हैं।\n"
            "कुछ मेज स्केट्स हैं।\n"
            "सभी घड़ियाँ स्केट्स हैं।\n\n"
            "निष्कर्ष:\n"
            "1. कुछ घड़ियाँ मेज हैं।\n"
            "2. कुछ स्केट्स मेज हैं।\n"
            "3. कुछ स्केट्स घड़ियाँ हैं।"
        ),
        "option_a": "Both conclusions 1 and 3 follow. / निष्कर्ष 1 और 3 दोनों अनुसरण करते हैं।",
        "option_b": "Both conclusions 2 and 3 follow. / निष्कर्ष 2 और 3 दोनों अनुसरण करते हैं।",
        "option_c": "All conclusions 1, 2 and 3 follow. / सभी निष्कर्ष 1, 2 और 3 अनुसरण करते हैं।",
        "option_d": "Both conclusions 1 and 2 follow. / निष्कर्ष 1 और 2 दोनों अनुसरण करते हैं।",
        "correct_answer": "B",
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
            qn = d["question_number"]
            if qn in existing_qnums:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

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
