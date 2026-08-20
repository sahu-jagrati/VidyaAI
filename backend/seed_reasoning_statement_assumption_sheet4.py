"""
seed_reasoning_statement_assumption_sheet4.py
=============================================
Seeds Statement-Assumption-Conclusion Q20–Q27 from Gagan Pratap Reasoning
PDFs (Sheet 4).
Subject : Reasoning
Topic   : Statement Assumption and Conclusion

TWO option formats used in this batch:

  Q20–Q23  →  ASSUMPTION format (4 options, no frontend injection)
    (A) Only Assumption I is implicit.
    (B) Only Assumption II is implicit.
    (C) Both I & II are implicit.
    (D) Neither I nor II is implicit.

  Q24–Q27  →  CONCLUSION format (5 options; 5th injected by frontend)
    (A) Only I follows.
    (B) Only II follows.
    (C) Both I & II follow.
    (D) Neither I nor II follows.
    (E) Either I or II follows.   ← NOT stored; injected by frontend as
                                    SAC_CONCLUSION_E when option_a starts
                                    "Only I follows".

Sources:
  Q20 = ALP, 09 Aug 2018, Shift-3
  Q21 = ALP, 09 Aug 2018, Shift-3
  Q22 = ALP, 09 Aug 2018, Shift-3
  Q23 = ALP, 17 Aug 2018, Shift-3
  Q24 = Gagan Pratap Reasoning PDF (Statement-Conclusion)
  Q25 = Gagan Pratap Reasoning PDF (Statement-Conclusion)
  Q26 = Gagan Pratap Reasoning PDF (Statement-Conclusion)
  Q27 = Gagan Pratap Reasoning PDF (Statement-Conclusion)

Answer key:

  ── ASSUMPTION questions ──────────────────────────────────────────────────────

  Q20  A — Due to water crisis, authority asked citizens to reduce water
           consumption by 25%.
            Assumption I:   Many citizens may reduce their water consumption
                            → IMPLICIT ✓ (the whole purpose of issuing the
                            advisory is deterrence/compliance; asking assumes
                            that at least many citizens will follow the request)
            Assumption II:  Many citizens may protest to this advisory
                            → NOT implicit ✗ (protest is a possible reaction,
                            not an assumption embedded in issuing the advisory;
                            authorities act hoping for compliance, not protest)
            Only Assumption I is implicit.

  Q21  A — Shyam tells Gita, 'The way to reach Sri Lanka is through air and water'.
            Assumption I:   Gita likes to travel to Sri Lanka → IMPLICIT ✓
                            (Shyam gives Gita the route to Sri Lanka, which
                            assumes Gita has interest in or plans to travel
                            there; otherwise the route information is irrelevant)
            Assumption II:  Shyam is fond of advising people → NOT implicit ✗
                            (a single instance of sharing route information does
                            not establish a general fondness for advising; this is
                            an external character trait not embedded in the act)
            Only Assumption I is implicit.

  Q22  D — All girls love reading novels.
            Assumption I:   Novels are the only reading materials → NOT implicit ✗
                            (the statement says all girls love novels; it does NOT
                            imply novels are the only reading materials in existence)
            Assumption II:  No other girl loves to read other materials → NOT implicit ✗
                            (loving novels does not mean girls cannot love other
                            reading materials too; the statement doesn't exclude
                            other reading preferences)
            Neither I nor II is implicit.

  Q23  B — The Supreme Court has decided that all rapists will be hanged till death.
            Assumption I:   Women will get protection → NOT implicit ✗
                            (this is a hoped-for OUTCOME of the policy, not an
                            assumption embedded in the court's decision; the court
                            makes the decision assuming punishment deters crime, not
                            directly assuming "women will be protected")
            Assumption II:  The number of rape cases can be reduced → IMPLICIT ✓
                            (imposing capital punishment as a deterrent presupposes
                            that the severity of punishment will reduce future crimes,
                            i.e., that the number of rape cases CAN be brought down)
            Only Assumption II is implicit.

  ── CONCLUSION questions (5-opt; E injected by frontend as SAC_CONCLUSION_E) ─

  Q24  D — All organised persons find time for rest. Sunita, in spite of her
           very busy schedule, finds time for rest.
            Conclusion I:   Sunita is an organised person → DOES NOT FOLLOW ✗
                            (syllogism fallacy — affirming the consequent; "All A→B,
                            Sunita→B, ∴ Sunita→A" is invalid; not only organised
                            people find time for rest)
            Conclusion II:  Sunita is an industrious person → DOES NOT FOLLOW ✗
                            (the statement concerns being "organised" and finding
                            rest; "industrious" is an unrelated trait not derivable
                            from the given premises)
            Neither I nor II follows.

  Q25  B — This book 'z' is the ONLY book which focuses its attention to the
           problem of poverty in India between 1950 & 1980.
            Conclusion I:   There was no question of poverty before 1950
                            → DOES NOT FOLLOW ✗ (the book's scope covers 1950–1980;
                            this says nothing about whether poverty existed before
                            1950 — the book simply does not cover that period)
            Conclusion II:  No other book deals with poverty in India from 1950 to
                            1980 → FOLLOWS ✓ (the statement explicitly calls book 'z'
                            the "ONLY" book on this subject in this period, which
                            directly implies no other book covers the same topic)
            Only II follows.

  Q26  B — The percentage of the national income shared by the top 10% of
           households in India is 35.
            Conclusion I:   When an economy grows fast, concentration of wealth in
                            certain pockets takes place → DOES NOT FOLLOW ✗
                            (the statement gives a specific income-share statistic;
                            it says nothing about economic growth rates; introducing
                            "fast economic growth" goes far beyond the data given)
            Conclusion II:  The national income is unevenly distributed in India
                            → FOLLOWS ✓ (35% of national income going to just 10%
                            of households while the remaining 90% share 65% directly
                            demonstrates uneven/disproportionate distribution)
            Only II follows.

  Q27  D — The Prime Minister emphatically stated that his government will make
           every possible effort for the upliftment of poor farmers & farmhands.
            Conclusion I:   Except poor farmers & farmhands, all others have got
                            the benefits of fruits of development → DOES NOT FOLLOW ✗
                            (focusing on one deprived group does not imply ALL other
                            sections are already well-off; the claim is too absolute)
            Conclusion II:  No serious efforts have been made in the past for the
                            upliftment of any section of society → DOES NOT FOLLOW ✗
                            (too extreme; promising future efforts for farmers does
                            not imply NO efforts were EVER made for ANY section;
                            past government schemes could have targeted other groups)
            Neither I nor II follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Assumption_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Statement Assumption and Conclusion"

# ── Assumption format options (Q20–Q23) ──────────────────────────────────────
_AA = "Only Assumption I is implicit. / केवल पूर्वानुमान I अंतर्निहित है।"
_AB = "Only Assumption II is implicit. / केवल पूर्वानुमान II अंतर्निहित है।"
_AC = "Both I & II are implicit. / I और II दोनों अंतर्निहित हैं।"
_AD = "Neither I nor II is implicit. / न तो I और न ही II अंतर्निहित है।"

# ── Conclusion format options (Q24–Q27) ──────────────────────────────────────
# Option_a starts with "Only I follows" → triggers isSACConclusion5Opt in frontend
# which injects SAC_CONCLUSION_E = "Either I or II follows." as option E.
_CA = "Only I follows. / केवल I अनुसरण करता है।"
_CB = "Only II follows. / केवल II अनुसरण करता है।"
_CC = "Both I & II follow. / I और II दोनों अनुसरण करते हैं।"
_CD = "Neither I nor II follows. / न तो I और न ही II अनुसरण करता है।"
# _CE = "Either I or II follows." ← injected by frontend; never correct for Q24–Q27

QUESTIONS = [
    # ── Q20 (ALP, 09 Aug 2018, Shift-3) — ASSUMPTION ─────────────────────────
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": (
            "Statement: Due to the water crisis in the city, the authority had "
            "asked all the citizens to reduce their water consumption by 25%.\n\n"
            "Assumptions:\n"
            "I.  Many citizens may reduce their water consumption.\n"
            "II. Many citizens may protest to this advisory by the authority."
        ),
        "question_hi": (
            "कथन: शहर में पानी के संकट के कारण, प्राधिकरण ने सभी नागरिकों को "
            "अपनी पानी की खपत को 25% कम करने के लिए कहा था।\n\n"
            "पूर्वानुमान:\n"
            "I.  कई नागरिक अपनी पानी की खपत कम कर सकते हैं।\n"
            "II. प्राधिकरण की इस सलाह का कई नागरिक विरोध कर सकते हैं।"
        ),
        "option_a": _AA,
        "option_b": _AB,
        "option_c": _AC,
        "option_d": _AD,
        "correct_answer": "A",
        # I:  Issuing the advisory assumes citizens will comply/reduce usage;
        #     without this assumption the advisory would serve no purpose ✓
        # II: Protest is a possible future reaction, not embedded in the advisory;
        #     the authority assumes compliance, not opposition ✗
    },
    # ── Q21 (ALP, 09 Aug 2018, Shift-3) — ASSUMPTION ─────────────────────────
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": (
            "Statement: Shyam tells Gita, 'The way to reach Sri Lanka is through "
            "air and water'.\n\n"
            "Assumptions:\n"
            "I.  Gita likes to travel to Sri Lanka.\n"
            "II. Shyam is fond of advising people."
        ),
        "question_hi": (
            "कथन: श्याम, गीता को बताता है, 'श्रीलंका पहुंचने का मार्ग वायु और जल "
            "से होकर है।'\n\n"
            "पूर्वानुमान:\n"
            "I.  गीता को श्रीलंका यात्रा करना पसंद है।\n"
            "II. श्याम को लोगों को सलाह देने का शौक है।"
        ),
        "option_a": _AA,
        "option_b": _AB,
        "option_c": _AC,
        "option_d": _AD,
        "correct_answer": "A",
        # I:  Shyam giving Gita the route to Sri Lanka assumes she has interest in
        #     or is planning to travel there; otherwise the information is irrelevant ✓
        # II: One instance of sharing route information does not establish a general
        #     fondness for advising — external character trait not embedded here ✗
    },
    # ── Q22 (ALP, 09 Aug 2018, Shift-3) — ASSUMPTION ─────────────────────────
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": (
            "Statement: All girls love reading novels.\n\n"
            "Assumptions:\n"
            "I.  Novels are the only reading materials.\n"
            "II. No other girl loves to read other materials."
        ),
        "question_hi": (
            "कथन: सभी लड़कियों को उपन्यास पढ़ना बहुत पसंद होता है।\n\n"
            "पूर्वानुमान:\n"
            "I.  उपन्यास ही एकमात्र पठन सामग्री हैं।\n"
            "II. कोई भी लड़की दूसरी सामग्री पढ़ना पसंद नहीं करती है।"
        ),
        "option_a": _AA,
        "option_b": _AB,
        "option_c": _AC,
        "option_d": _AD,
        "correct_answer": "D",
        # I:  Novels being the ONLY reading materials is an extreme claim not
        #     implied by girls loving novels; other materials exist too ✗
        # II: Girls can love novels AND also love other reading materials;
        #     the statement does not exclude other reading preferences ✗
    },
    # ── Q23 (ALP, 17 Aug 2018, Shift-3) — ASSUMPTION ─────────────────────────
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "Statement: The Supreme Court has decided that all rapists will be "
            "hanged till death.\n\n"
            "Assumptions:\n"
            "I.  Women will get protection.\n"
            "II. The number of rape cases can be reduced."
        ),
        "question_hi": (
            "कथन: सर्वोच्च न्यायालय ने निर्णय लिया है कि सभी बलात्कारियों को "
            "मृत्यु तक फांसी दी जाएगी।\n\n"
            "पूर्वानुमान:\n"
            "I.  महिलाओं को सुरक्षा मिलेगी।\n"
            "II. बलात्कार के मामलों को कम किया जा सकता है।"
        ),
        "option_a": _AA,
        "option_b": _AB,
        "option_c": _AC,
        "option_d": _AD,
        "correct_answer": "B",
        # I:  "Women will get protection" is a desired outcome/conclusion of the
        #     policy, not an assumption directly embedded in the court's decision ✗
        # II: Capital punishment as deterrence presupposes the severity of punishment
        #     will reduce future crimes, i.e., rape cases CAN be brought down ✓
    },

    # ── Q24 (Statement-Conclusion, 5-opt) ─────────────────────────────────────
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": (
            "Statement: All the organised persons find time for rest. Sunita, in "
            "spite of her very busy schedule finds time for rest.\n\n"
            "Conclusions:\n"
            "I.  Sunita is an organised person.\n"
            "II. Sunita is an industrious person."
        ),
        "question_hi": (
            "कथन: सभी संगठित व्यक्ति विश्राम के लिए समय पाते हैं। सुनीता, अपने "
            "बहुत व्यस्त कार्यक्रम के बावजूद विश्राम के लिए समय निकालती है।\n\n"
            "निष्कर्ष:\n"
            "I.  सुनीता एक संगठित व्यक्ति है।\n"
            "II. सुनीता एक मेहनती इंसान है।"
        ),
        "option_a": _CA,
        "option_b": _CB,
        "option_c": _CC,
        "option_d": _CD,
        "correct_answer": "D",
        # I:  Syllogism fallacy (affirming the consequent): All A→B, Sunita→B
        #     does NOT prove Sunita→A; other non-organised people can also find
        #     rest → DOES NOT FOLLOW ✗
        # II: "Industrious" is not mentioned in the statement; a busy schedule ≠
        #     industrious; this trait is not derivable from the given premises
        #     → DOES NOT FOLLOW ✗
        # Option E ("Either I or II follows") injected by frontend; never correct here.
    },
    # ── Q25 (Statement-Conclusion, 5-opt) ─────────────────────────────────────
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": (
            "Statement: This book 'z' is the only book which focuses its attention "
            "to the problem of poverty in India between 1950 & 1980.\n\n"
            "Conclusions:\n"
            "I.  There was no question of poverty before 1950.\n"
            "II. No other book deals with poverty in India from 1950 to 1980."
        ),
        "question_hi": (
            "कथन: यह पुस्तक 'z' एकमात्र पुस्तक है जो 1950 और 1980 के बीच भारत "
            "में गरीबी की समस्या पर ध्यान केंद्रित करती है।\n\n"
            "निष्कर्ष:\n"
            "I.  1950 से पहले गरीबी का कोई सवाल नहीं था।\n"
            "II. 1950 से 1980 के दौरान भारत में गरीबी से संबंधित कोई अन्य पुस्तक "
            "नहीं है।"
        ),
        "option_a": _CA,
        "option_b": _CB,
        "option_c": _CC,
        "option_d": _CD,
        "correct_answer": "B",
        # I:  The book covers 1950–1980; this says nothing about poverty before
        #     1950 — poverty certainly existed before then; the book just doesn't
        #     address that period → DOES NOT FOLLOW ✗
        # II: The statement says book 'z' is the "ONLY" book on poverty in India
        #     from 1950–1980; this directly implies no other book covers the same
        #     topic and time period → FOLLOWS ✓
        # Option E injected by frontend; never correct here.
    },
    # ── Q26 (Statement-Conclusion, 5-opt) ─────────────────────────────────────
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "Statement: The percentage of the national income shared by the top "
            "10% of households in India is 35.\n\n"
            "Conclusions:\n"
            "I.  When an economy grows fast, concentration of wealth in certain "
            "pockets of population takes place.\n"
            "II. The national income is unevenly distributed in India."
        ),
        "question_hi": (
            "कथन: भारत में शीर्ष 10 प्रतिशत परिवारों द्वारा साझा राष्ट्रीय आय का "
            "प्रतिशत 35 है।\n\n"
            "निष्कर्ष:\n"
            "I.  जब कोई अर्थव्यवस्था तेजी से बढ़ती है, तो आबादी के कुछ हिस्सों "
            "में धन का एकाग्रता होती है।\n"
            "II. भारत में राष्ट्रीय आय असमान रूप से वितरित की जाती है।"
        ),
        "option_a": _CA,
        "option_b": _CB,
        "option_c": _CC,
        "option_d": _CD,
        "correct_answer": "B",
        # I:  The statement provides a static income-share statistic; it does NOT
        #     mention economic growth rates; introducing "fast economic growth" as
        #     a cause goes beyond the data given → DOES NOT FOLLOW ✗
        # II: 35% of national income to just 10% of households while 90% of
        #     households share the remaining 65% is direct evidence of uneven/
        #     disproportionate distribution → FOLLOWS ✓
        # Option E injected by frontend; never correct here.
    },
    # ── Q27 (Statement-Conclusion, 5-opt) ─────────────────────────────────────
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "Statement: The Prime Minister emphatically stated that his government "
            "will make every possible effort for the upliftment of poor farmers "
            "& farmhands.\n\n"
            "Conclusions:\n"
            "I.  Except poor farmers & farmhands, all others have got the benefits "
            "of fruits of development.\n"
            "II. No serious efforts have been made in the past for the upliftment "
            "of any section of the society."
        ),
        "question_hi": (
            "कथन: प्रधानमंत्री ने जोर देकर कहा कि उनकी सरकार गरीब किसानों और "
            "कृषि श्रमिकों के उत्थान के लिए हर संभव प्रयास करेगी।\n\n"
            "निष्कर्ष:\n"
            "I.  गरीब किसानों और कृषि श्रमिकों को छोड़कर अन्य सभी को विकास के "
            "फलों का लाभ मिल चुका है।\n"
            "II. समाज के किसी भी वर्ग के उत्थान के लिए अतीत में कोई गंभीर प्रयास "
            "नहीं किए गए हैं।"
        ),
        "option_a": _CA,
        "option_b": _CB,
        "option_c": _CC,
        "option_d": _CD,
        "correct_answer": "D",
        # I:  Focusing on poor farmers does not imply ALL other sections are fully
        #     developed; multiple groups can be simultaneously deprived; the
        #     absolute claim "all others have got benefits" is unwarranted ✗
        # II: Past efforts being made for OTHER sections of society is not ruled
        #     out by this statement; promising future efforts for farmers does not
        #     imply NO efforts were EVER made for ANY section → DOES NOT FOLLOW ✗
        # Option E injected by frontend; never correct here.
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
