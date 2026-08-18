"""
seed_reasoning_alphabet_sheet9.py
=========================================
Seeds Alphabet Q76-Q88 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet9.py

Mixed question types:
  - Letter distance after alphabetical sort (Q76)
  - Dictionary ordering (Q77-82, Q86)
  - Word formation / meaningful words (Q83-85)
  - Logical meaningful order (Q87-88)

Answer key (solutions verified):
  Q76  JOURNAL sorted→A,J,L,N,O,R,U; 4th=N(14), 2nd-right=R(18) → B  (Three)
       Between N and R: O,P,Q = 3 letters  [CHSL-2 Aug 2023 Shift 2]
  Q77  Aureole<Auspicious<Authentic<Authority<Automate           → C  (5,4,3,1,2)
       AUR < AUS < AUTH-E < AUTH-O < AUTO  [CPO-03 Oct 2023 Shift 2]
  Q78  Foreign<Forest<Forge<Forgotten<Forlorn<Formal             → A  (2,3,5,4,6,1)
       FORE-I < FORE-S < FORG-E < FORG-O < FORL < FORM  [CPO-03 Oct 2023 Shift 2]
  Q79  Descend<Desire<Desolate<Desperate<Destination<Destructive → C  (3,1,5,6,2,4)
       DES-C < DES-I < DES-O < DES-P < DEST-I < DEST-R  [CPO-03 Oct 2023 Shift 1]
  Q80  Logician<Loincloth<Lollipop<Lonely<Longways               → C  (4,2,1,5,3)
       LOG < LOI < LOL < LON-E < LON-G  [CPO-03 Oct 2023 Shift 1]
  Q81  Docile<Dock<Doctor<Doctorate<Doctrine<Documentary          → C  (3,5,1,2,6,4)
       DOCI < DOCK < DOCTO-R < DOCTO-R-A < DOCTR < DOCU  [CPO-04 Oct 2023 Shift 2]
  Q82  Vivisection<Vocalist<Vogue<Voice<Void                      → A  (3,2,5,1,4)
       VI < VOC < VOG < VOI-C < VOI-D  [CPO-04 Oct 2023 Shift 1]
  Q83  B,E,O,R → BORE + ROBE = 2 words                           → B  (Two/दो)
       [CHSL Tier II-2 Nov 2023 Shift 1]
  Q84  CRACKER positions 2,3,6,7 = R,A,E,R → REAR + RARE = 2    → A  (Two/दो)
       [CHSL Tier II-2 Nov 2023 Shift 1]
  Q85  T,U,K,S four-letter words → TUSK only = 1                 → B  (One/एक)
       [CHSL Tier II-2 Nov 2023 Shift 1]
  Q86  Mecamylamine<Mechanical<Meclizine<Meconium<Medication<Mediocrity → A (6,4,5,1,2,3)
       MEC-A < MEC-H < MEC-L < MEC-O < MEDI-C < MEDI-O  [Stenographer-13 Oct 2023 Shift 3]
  Q87  Logical: Letter<Word<Sentence<Paragraph                    → C  (4,1,3,2)
       Smallest to largest writing unit  [Stenographer-13 Oct 2023 Shift 3]
  Q88  Logical: Cotton→Thread→Fabric→Shirt piece→Shirt           → A  (5,2,3,1,4)
       Production sequence  [CGL Tier II-26 Oct 2023 Shift 1]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet9"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q76 ── JOURNAL sorted; 4th from left ↔ 2nd from right distance ────────
    # JOURNAL → sorted A,J,L,N,O,R,U; 4th=N(14), 2nd-right=R(18); O,P,Q = 3 between
    {
        "question_number": 76,
        "difficulty": "medium",
        "question_en": (
            "Each of the letters in the word JOURNAL are arranged in alphabetical order. "
            "How many letters are there in the English alphabetical series between the letter "
            "which is fourth from the left and the letter which is second from the right "
            "in the new letter cluster thus formed? "
            "[CHSL-2 Aug 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द JOURNAL के प्रत्येक अक्षर को वर्णमाला क्रम में व्यवस्थित किया गया है। "
            "इस प्रकार बने नए अक्षर-समूह में बाएं से चौथे अक्षर और दाएं से दूसरे अक्षर के बीच "
            "अंग्रेजी वर्णमाला श्रृंखला में कितने अक्षर हैं?"
        ),
        "option_a": "Six/छह",
        "option_b": "Three/तीन",
        "option_c": "Five/पाँच",
        "option_d": "Four/चार",
        "correct_answer": "B",
        # A,J,L,N,O,R,U; 4th=N(14), 2nd-right=R(18); between N and R: O,P,Q = 3
    },
    # ── Q77 ── Aureole<Auspicious<Authentic<Authority<Automate → 5,4,3,1,2 ──────
    {
        "question_number": 77,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Authority 2.Automate 3.Authentic 4.Auspicious 5.Aureole — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-03 Oct 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Authority 2.Automate 3.Authentic 4.Auspicious 5.Aureole — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "4, 5, 3, 1, 2",
        "option_b": "5, 3, 4, 1, 2",
        "option_c": "5, 4, 3, 1, 2",
        "option_d": "5, 4, 1, 3, 2",
        "correct_answer": "C",
        # AUR(5) < AUS(4) < AUTH-E(3) < AUTH-O(1) < AUTO(2)
    },
    # ── Q78 ── Foreign<Forest<Forge<Forgotten<Forlorn<Formal → 2,3,5,4,6,1 ──────
    {
        "question_number": 78,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Formal 2.Foreign 3.Forest 4.Forgotten 5.Forge 6.Forlorn — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CPO-03 Oct 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Formal 2.Foreign 3.Forest 4.Forgotten 5.Forge 6.Forlorn — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों की उस क्रम में सही व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "2, 3, 5, 4, 6, 1",
        "option_b": "3, 5, 1, 6, 2, 4",
        "option_c": "3, 2, 5, 4, 1, 6",
        "option_d": "3, 5, 6, 1, 2, 4",
        "correct_answer": "A",
        # FORE-I(2) < FORE-S(3) < FORG-E(5) < FORG-O(4) < FORL(6) < FORM(1)
    },
    # ── Q79 ── Descend<Desire<Desolate<Desperate<Destination<Destructive → 3,1,5,6,2,4 ─
    {
        "question_number": 79,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Desire 2.Destination 3.Descend 4.Destructive 5.Desolate 6.Desperate — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CPO-03 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Desire 2.Destination 3.Descend 4.Destructive 5.Desolate 6.Desperate — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों की उस क्रम में सही व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 1, 2, 6, 5, 4",
        "option_b": "3, 1, 6, 5, 2, 4",
        "option_c": "3, 1, 5, 6, 2, 4",
        "option_d": "3, 1, 5, 6, 4, 2",
        "correct_answer": "C",
        # DES-C(3) < DES-I(1) < DES-O(5) < DES-P(6) < DEST-I(2) < DEST-R(4)
    },
    # ── Q80 ── Logician<Loincloth<Lollipop<Lonely<Longways → 4,2,1,5,3 ──────────
    {
        "question_number": 80,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Lollipop 2.Loincloth 3.Longways 4.Logician 5.Lonely — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-03 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Lollipop 2.Loincloth 3.Longways 4.Logician 5.Lonely — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 2, 1, 5, 4",
        "option_b": "4, 3, 1, 5, 2",
        "option_c": "4, 2, 1, 5, 3",
        "option_d": "1, 4, 5, 3, 2",
        "correct_answer": "C",
        # LOG(4) < LOI(2) < LOL(1) < LON-E(5) < LON-G(3)
    },
    # ── Q81 ── Docile<Dock<Doctor<Doctorate<Doctrine<Documentary → 3,5,1,2,6,4 ──
    {
        "question_number": 81,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Doctor 2.Doctorate 3.Docile 4.Documentary 5.Dock 6.Doctrine — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CPO-04 Oct 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Doctor 2.Doctorate 3.Docile 4.Documentary 5.Dock 6.Doctrine — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों की उस क्रम में सही व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 5, 2, 1, 6, 4",
        "option_b": "3, 5, 1, 2, 4, 6",
        "option_c": "3, 5, 1, 2, 6, 4",
        "option_d": "2, 3, 5, 1, 6, 4",
        "correct_answer": "C",
        # DOCI(3) < DOCK(5) < DOCTO-R(1) < DOCTO-R-A(2) < DOCTR(6) < DOCU(4)
    },
    # ── Q82 ── Vivisection<Vocalist<Vogue<Voice<Void → 3,2,5,1,4 ──────────────
    {
        "question_number": 82,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Voice 2.Vocalist 3.Vivisection 4.Void 5.Vogue — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-04 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Voice 2.Vocalist 3.Vivisection 4.Void 5.Vogue — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 2, 5, 1, 4",
        "option_b": "5, 2, 3, 1, 4",
        "option_c": "2, 3, 5, 1, 4",
        "option_d": "4, 2, 3, 1, 5",
        "correct_answer": "A",
        # VI(3) < VOC(2) < VOG(5) < VOI-C(1) < VOI-D(4)
    },
    # ── Q83 ── Meaningful words from B, E, O, R ────────────────────────────────
    # BORE and ROBE → 2 words
    {
        "question_number": 83,
        "difficulty": "easy",
        "question_en": (
            "How many meaningful English words can be formed with the letters B, E, O and R, "
            "using each letter only once in each word? "
            "[CHSL Tier II-2 Nov 2023 Shift 1]"
        ),
        "question_hi": (
            "B, E, O और R अक्षरों से प्रत्येक अक्षर का प्रयोग प्रत्येक शब्द में केवल एक बार करते हुए "
            "कितने सार्थक अंग्रेजी शब्द बनाए जा सकते हैं?"
        ),
        "option_a": "One/एक",
        "option_b": "Two/दो",
        "option_c": "None/कोई नहीं",
        "option_d": "Three/तीन",
        "correct_answer": "B",  # BORE + ROBE = 2 words
    },
    # ── Q84 ── CRACKER letters at positions 2,3,6,7 → R,A,E,R → REAR/RARE ──────
    {
        "question_number": 84,
        "difficulty": "medium",
        "question_en": (
            "How many meaningful English words can be formed using the second, third, "
            "sixth and seventh letters of the word CRACKER "
            "(when counted from left to right), using each letter only once in each word? "
            "[CHSL Tier II-2 Nov 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द CRACKER के दूसरे, तीसरे, छठे और सातवें अक्षरों (बाएं से दाएं गिनने पर) का "
            "प्रयोग करते हुए, प्रत्येक अक्षर का प्रत्येक शब्द में केवल एक बार उपयोग करके "
            "कितने सार्थक अंग्रेजी शब्द बनाए जा सकते हैं?"
        ),
        "option_a": "Two/दो",
        "option_b": "One/एक",
        "option_c": "Three/तीन",
        "option_d": "Zero/शून्य",
        "correct_answer": "A",
        # CRACKER: C(1)R(2)A(3)C(4)K(5)E(6)R(7); 2nd=R, 3rd=A, 6th=E, 7th=R
        # R,A,E,R → REAR + RARE = 2 words
    },
    # ── Q85 ── Four-letter words from T, U, K, S → TUSK only ─────────────────
    {
        "question_number": 85,
        "difficulty": "easy",
        "question_en": (
            "How many meaningful four-letter English words can be formed using "
            "T, U, K and S, using each letter only once in each word? "
            "[CHSL Tier II-2 Nov 2023 Shift 1]"
        ),
        "question_hi": (
            "T, U, K और S का प्रयोग करते हुए, प्रत्येक अक्षर का प्रत्येक शब्द में केवल एक बार "
            "उपयोग करके कितने सार्थक चार-अक्षरीय अंग्रेजी शब्द बनाए जा सकते हैं?"
        ),
        "option_a": "More than two/दो से अधिक",
        "option_b": "One/एक",
        "option_c": "None/कोई नहीं",
        "option_d": "Two/दो",
        "correct_answer": "B",  # TUSK is the only 4-letter word using T,U,K,S each once
    },
    # ── Q86 ── Mecamylamine<Mechanical<Meclizine<Meconium<Medication<Mediocrity → 6,4,5,1,2,3 ─
    {
        "question_number": 86,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Meconium 2.Medication 3.Mediocrity 4.Mechanical 5.Meclizine 6.Mecamylamine — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[Stenographer-13 Oct 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Meconium 2.Medication 3.Mediocrity 4.Mechanical 5.Meclizine 6.Mecamylamine — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "6, 4, 5, 1, 2, 3",
        "option_b": "4, 5, 1, 2, 3, 6",
        "option_c": "6, 5, 1, 4, 2, 3",
        "option_d": "6, 4, 2, 3, 5, 1",
        "correct_answer": "A",
        # MEC-A(6) < MEC-H(4) < MEC-L(5) < MEC-O(1) < MEDI-C(2) < MEDI-O(3)
    },
    # ── Q87 ── Logical order: Letter < Word < Sentence < Paragraph → 4,1,3,2 ──
    {
        "question_number": 87,
        "difficulty": "easy",
        "question_en": (
            "Select the correct option that represents the arrangement of the following words "
            "in a logical and meaningful order. "
            "1. Word  2. Paragraph  3. Sentence  4. Letter "
            "[Stenographer-13 Oct 2023 Shift 3]"
        ),
        "question_hi": (
            "उस सही विकल्प का चयन कीजिए जो निम्नलिखित शब्दों की तार्किक और सार्थक क्रम में "
            "व्यवस्था को दर्शाता है। "
            "1. Word/शब्द  2. Paragraph/पैराग्राफ  3. Sentence/वाक्य  4. Letter/अक्षर"
        ),
        "option_a": "4, 3, 1, 2",
        "option_b": "1, 3, 4, 2",
        "option_c": "4, 1, 3, 2",
        "option_d": "1, 4, 3, 2",
        "correct_answer": "C",
        # Smallest to largest: Letter(4) → Word(1) → Sentence(3) → Paragraph(2)
    },
    # ── Q88 ── Logical order: Cotton→Thread→Fabric→Shirt piece→Shirt → 5,2,3,1,4 ─
    {
        "question_number": 88,
        "difficulty": "easy",
        "question_en": (
            "Select the correct option that indicates the arrangement of the given words "
            "in a logical and meaningful order. "
            "1. Shirt piece  2. Thread  3. Fabric  4. Shirt  5. Cotton "
            "[CGL Tier II-26 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "उस सही विकल्प का चयन कीजिए जो दिए गए शब्दों को तार्किक और सार्थक क्रम में "
            "व्यवस्थित करने वाला सही विकल्प हो। "
            "1. Shirt piece/कपड़े का टुकड़ा  2. Thread/धागा  3. Fabric/कपड़ा  "
            "4. Shirt/शर्ट  5. Cotton/कपास"
        ),
        "option_a": "5, 2, 3, 1, 4",
        "option_b": "5, 2, 3, 4, 1",
        "option_c": "5, 3, 1, 2, 4",
        "option_d": "3, 1, 2, 4, 5",
        "correct_answer": "A",
        # Production: Cotton(5) → Thread(2) → Fabric(3) → Shirt piece(1) → Shirt(4)
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
