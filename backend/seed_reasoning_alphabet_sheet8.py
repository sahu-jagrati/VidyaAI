"""
seed_reasoning_alphabet_sheet8.py
=========================================
Seeds Alphabet Q64-Q75 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet8.py

NOTE: Q72, Q73, Q74 share identical exam content with Q53, Q54, Q55 respectively
(same questions appear in multiple sheets of the PDF). They are seeded with their
correct question numbers so the sequential numbering is preserved.

Answer key (solutions verified):
  Q64  Descend<Desire<Desolate<Desperate<Destination<Destruction → C  (5,4,2,1,6,3)
       DES-C < DES-I < DES-O < DES-P < DEST-I < DEST-R  [CPO-05 Oct 2023 Shift 1]
  Q65  Flaw<Flec<Fleet<Flight<Flint                             → C  (3,2,4,5,1)
       FLA < FLE-C < FLE-E < FLI-G < FLI-N  [CPO-05 Oct 2023 Shift 1]
  Q66  Serious<Sermonize<Serrated<Servant<Session               → D  (2,1,5,3,4)
       SER-I < SER-M < SER-R < SER-V < SES  [CPO-05 Oct 2023 Shift 2]
  Q67  Chamber<Chance<Channel<Chapel<Charcoal<Chariot           → A  (5,6,1,4,3,2)
       CHAM < CHAN-C < CHAN-N < CHAP < CHAR-C < CHAR-I  [CPO-05 Oct 2023 Shift 2]
  Q68  Stock<Stoke<Stomach<Stoop<Storage<Storey                 → D  (4,2,6,1,3,5)
       STOC < STOK < STOM < STOO < STOR-A < STOR-E  [CPO-04 Oct 2023 Shift 3]
  Q69  Woodland<Workable<Wrangle<Wrist<Wrongful                 → D  (5,3,2,1,4)
       WO-O < WO-R < WR-A < WR-I < WR-O  [CPO-04 Oct 2023 Shift 2]
  Q70  Purgatory<Purge<Purify<Puritan<Purpose                   → D  (4,3,5,1,2)
       PURG-A < PURG-E < PURI-F < PURI-T < PURP  [CPO-04 Oct 2023 Shift 3]
  Q71  Pancakes<Pancreas<Pandemic<Panicked<Panorama<Panther     → A  (1,4,2,3,5,6)
       PANC-A < PANC-R < PAND < PANI < PANO < PANT  [CGL-14 July 2023 Shift 3]
  Q72  EADL → DEAL  (same exam Q as Q53)                       → C
       [CHSL Tier II-26 Jun 2023 Shift 1]
  Q73  Taciturn<Talisman<Tangential<Tantalizing<Tantamount      → D  (5,1,3,4,2)
       TAC < TAL < TAN-G < TANT-A-L < TANT-A-M  (same exam Q as Q54)
       [CHSL Tier II-26 Jun 2023 Shift 1]
  Q74  ETNSIL → SILENT  (same exam Q as Q55)                   → A
       [CHSL Tier II-26 Jun 2023 Shift 1]
  Q75  Reach<Reactor<Readily<Realistic<Realize<Really           → B  (3,5,2,1,6,4)
       REAC-H < REAC-T < READ < REAL-I-S < REAL-I-Z < REAL-L  [CPO-04 Oct 2023 Shift 1]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet8"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q64 ── Descend<Desire<Desolate<Desperate<Destination<Destruction → 5,4,2,1,6,3 ──
    {
        "question_number": 64,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Desperate 2.Desolate 3.Destruction 4.Desire 5.Descend 6.Destination — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CPO-05 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Desperate 2.Desolate 3.Destruction 4.Desire 5.Descend 6.Destination — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों की उस क्रम में सही व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "5, 4, 2, 1, 3, 6",
        "option_b": "5, 4, 1, 6, 2, 3",
        "option_c": "5, 4, 2, 1, 6, 3",
        "option_d": "5, 4, 1, 2, 6, 3",
        "correct_answer": "C",
        # DES-C(5) < DES-I(4) < DES-O(2) < DES-P(1) < DEST-I(6) < DEST-R(3)
    },
    # ── Q65 ── Flaw<Flec<Fleet<Flight<Flint → 3,2,4,5,1 ─────────────────────
    {
        "question_number": 65,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Flint 2.Flec 3.Flaw 4.Fleet 5.Flight — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-05 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Flint 2.Flec 3.Flaw 4.Fleet 5.Flight — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 5, 4, 2, 1",
        "option_b": "2, 3, 5, 4, 1",
        "option_c": "3, 2, 4, 5, 1",
        "option_d": "3, 4, 2, 5, 1",
        "correct_answer": "C",
        # FLA(3) < FLE-C(2) < FLE-E(4) < FLI-G(5) < FLI-N(1)
    },
    # ── Q66 ── Serious<Sermonize<Serrated<Servant<Session → 2,1,5,3,4 ─────────
    {
        "question_number": 66,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Sermonize 2.Serious 3.Servant 4.Session 5.Serrated — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-05 Oct 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Sermonize 2.Serious 3.Servant 4.Session 5.Serrated — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 1, 5, 2, 4",
        "option_b": "2, 3, 5, 1, 4",
        "option_c": "3, 2, 5, 1, 4",
        "option_d": "2, 1, 5, 3, 4",
        "correct_answer": "D",
        # SER-I(2) < SER-M(1) < SER-R(5) < SER-V(3) < SES(4)
    },
    # ── Q67 ── Chamber<Chance<Channel<Chapel<Charcoal<Chariot → 5,6,1,4,3,2 ────
    {
        "question_number": 67,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Channel 2.Chariot 3.Charcoal 4.Chapel 5.Chamber 6.Chance — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CPO-05 Oct 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Channel 2.Chariot 3.Charcoal 4.Chapel 5.Chamber 6.Chance — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों की उस क्रम में सही व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "5, 6, 1, 4, 3, 2",
        "option_b": "5, 1, 6, 4, 3, 2",
        "option_c": "5, 1, 6, 4, 2, 3",
        "option_d": "6, 4, 2, 3, 1, 5",
        "correct_answer": "A",
        # CHAM(5) < CHAN-C(6) < CHAN-N(1) < CHAP(4) < CHAR-C(3) < CHAR-I(2)
    },
    # ── Q68 ── Stock<Stoke<Stomach<Stoop<Storage<Storey → 4,2,6,1,3,5 ──────────
    {
        "question_number": 68,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Stoop 2.Stoke 3.Storage 4.Stock 5.Storey 6.Stomach — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CPO-04 Oct 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Stoop 2.Stoke 3.Storage 4.Stock 5.Storey 6.Stomach — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों की उस क्रम में सही व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "2, 4, 6, 3, 1, 5",
        "option_b": "2, 4, 3, 6, 1, 5",
        "option_c": "2, 3, 6, 1, 5, 4",
        "option_d": "4, 2, 6, 1, 3, 5",
        "correct_answer": "D",
        # STOC(4) < STOK(2) < STOM(6) < STOO(1) < STOR-A(3) < STOR-E(5)
    },
    # ── Q69 ── Woodland<Workable<Wrangle<Wrist<Wrongful → 5,3,2,1,4 ────────────
    {
        "question_number": 69,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Wrist 2.Wrangle 3.Workable 4.Wrongful 5.Woodland — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-04 Oct 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Wrist 2.Wrangle 3.Workable 4.Wrongful 5.Woodland — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 5, 2, 1, 4",
        "option_b": "3, 2, 5, 1, 4",
        "option_c": "3, 2, 1, 5, 4",
        "option_d": "5, 3, 2, 1, 4",
        "correct_answer": "D",
        # WO-O(Woodland5) < WO-R(Workable3) < WR-A(Wrangle2) < WR-I(Wrist1) < WR-O(Wrongful4)
    },
    # ── Q70 ── Purgatory<Purge<Purify<Puritan<Purpose → 4,3,5,1,2 ──────────────
    {
        "question_number": 70,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Puritan 2.Purpose 3.Purge 4.Purgatory 5.Purify — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-04 Oct 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Puritan 2.Purpose 3.Purge 4.Purgatory 5.Purify — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 4, 5, 1, 2",
        "option_b": "5, 3, 4, 1, 2",
        "option_c": "4, 5, 1, 2, 3",
        "option_d": "4, 3, 5, 1, 2",
        "correct_answer": "D",
        # PURG-A(4) < PURG-E(3) < PURI-F(5) < PURI-T(1) < PURP(2)
    },
    # ── Q71 ── Pancakes<Pancreas<Pandemic<Panicked<Panorama<Panther → 1,4,2,3,5,6 ─
    {
        "question_number": 71,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Pancakes 2.Pandemic 3.Panicked 4.Pancreas 5.Panorama 6.Panther — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-14 July 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Pancakes 2.Pandemic 3.Panicked 4.Pancreas 5.Panorama 6.Panther — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "1, 4, 2, 3, 5, 6",
        "option_b": "1, 2, 3, 4, 5, 6",
        "option_c": "1, 4, 2, 3, 6, 5",
        "option_d": "2, 1, 4, 3, 6, 5",
        "correct_answer": "A",
        # PANC-A(1) < PANC-R(4) < PAND(2) < PANI(3) < PANO(5) < PANT(6)
    },
    # ── Q72 ── Jumbled word: EADL → DEAL ─────────────────────────────────────
    # (Same exam question as Q53; appears in a different PDF sheet)
    {
        "question_number": 72,
        "difficulty": "easy",
        "question_en": (
            "The sentence below has a word in which the letters are jumbled up. "
            "Rearrange the letters of that word, written in capital letters, "
            "to form the correct word. "
            "After a long negotiation, they finally reached a EADL that satisfied both parties. "
            "[CHSL Tier II-26 Jun 2023 Shift 1]"
        ),
        "question_hi": (
            "नीचे दिए गए वाक्य में एक ऐसा शब्द है जिसके अक्षर अव्यवस्थित हैं। "
            "उस शब्द के अक्षरों को पुनर्व्यवस्थित करके सही शब्द बनाएं। "
            "लंबी वार्ता के बाद, वे अंततः एक EADL पर पहुंचे जिसने दोनों पक्षों को संतुष्ट किया।"
        ),
        "option_a": "DALE",
        "option_b": "LEAD",
        "option_c": "DEAL",
        "option_d": "LADE",
        "correct_answer": "C",  # EADL → DEAL
    },
    # ── Q73 ── Taciturn<Talisman<Tangential<Tantalizing<Tantamount → 5,1,3,4,2 ─
    # (Same exam question as Q54; appears in a different PDF sheet)
    {
        "question_number": 73,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Talisman 2.Tantamount 3.Tangential 4.Tantalizing 5.Taciturn — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CHSL Tier II-26 Jun 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Talisman 2.Tantamount 3.Tangential 4.Tantalizing 5.Taciturn — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों की उस क्रम में सही व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "4, 2, 3, 5, 1",
        "option_b": "1, 4, 3, 5, 2",
        "option_c": "3, 5, 1, 4, 2",
        "option_d": "5, 1, 3, 4, 2",
        "correct_answer": "D",
        # TAC(5) < TAL(1) < TAN-G(3) < TANT-A-L(4) < TANT-A-M(2)
    },
    # ── Q74 ── Jumbled word: ETNSIL → SILENT ──────────────────────────────────
    # (Same exam question as Q55; appears in a different PDF sheet)
    {
        "question_number": 74,
        "difficulty": "easy",
        "question_en": (
            "The sentence below has a word in which the letters are jumbled up. "
            "Rearrange the letters of that word, written in capital letters, "
            "to form the correct word. "
            "The ETNSIL night was interrupted only by the gentle rustling of leaves in the breeze. "
            "[CHSL Tier II-26 Jun 2023 Shift 1]"
        ),
        "question_hi": (
            "नीचे दिए गए वाक्य में एक ऐसा शब्द है जिसके अक्षर अव्यवस्थित हैं। "
            "उस शब्द के अक्षरों को पुनर्व्यवस्थित करके सही शब्द बनाएं। "
            "ETNSIL रात केवल पत्तियों की हल्की सरसराहट से बाधित हुई।"
        ),
        "option_a": "SILENT",
        "option_b": "LISTEN",
        "option_c": "TENILS",
        "option_d": "NILETS",
        "correct_answer": "A",  # ETNSIL → SILENT (adjective for "night")
    },
    # ── Q75 ── Reach<Reactor<Readily<Realistic<Realize<Really → 3,5,2,1,6,4 ───
    {
        "question_number": 75,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Realistic 2.Readily 3.Reach 4.Really 5.Reactor 6.Realize — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-04 Oct 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Realistic 2.Readily 3.Reach 4.Really 5.Reactor 6.Realize — "
            "उस विकल्प का चयन कीजिए जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 5, 1, 2, 6, 4",
        "option_b": "3, 5, 2, 1, 6, 4",
        "option_c": "2, 6, 1, 5, 3, 4",
        "option_d": "3, 5, 6, 1, 2, 4",
        "correct_answer": "B",
        # REAC-H(3) < REAC-T(5) < READ(2) < REAL-I-S(1) < REAL-I-Z(6) < REAL-L(4)
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
