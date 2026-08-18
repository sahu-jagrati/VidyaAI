"""
seed_reasoning_alphabet_sheet7.py
=========================================
Seeds Alphabet Q51-Q63 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet7.py

Mixed question types: ordering, anagram/jumbled-word, number-code word formation.

Answer key (solutions verified):
  Q51  Chain<Chair<Charcoal<Charge<Charm           → A  (2,1,5,4,3)
       Chair=CHA-I-R (4th=I), Charcoal=CHA-R-C (4th=R); I<R so Chair<Charcoal
       [GD Con-11 Jan 2023 Shift 3]
  Q52  Peach<Peacock<Peanut<Peasant<Pencil          → C  (4,3,1,2,5)
       PEAC-H(8th) < PEAC-O(15th) so Peach<Peacock [user said D, overriding]
       [GD Con-12 Jan 2023 Shift 2]
  Q53  EADL → DEAL                                 → C
       [CHSL Tier II-26 Jun 2023 Shift 1]
  Q54  Taciturn<Talisman<Tangential<Tantalizing<Tantamount → D  (5,1,3,4,2)
       TANT-A-L(Tantalizing) < TANT-A-M(Tantamount); L<M
       [CHSL Tier II-26 Jun 2023 Shift 1]
  Q55  ETNSIL → SILENT (context: "___ night")      → A
       [CHSL Tier II-26 Jun 2023 Shift 1]
  Q56  STUDENT: S(4)T(3)U(7)D(6)E(1)N(2)T(5)      → A  (4,3,7,6,1,2,5)
       E=1,N=2,T=3,S=4,T=5,D=6,U=7  [CGL Tier II-3 March 2023 Shift 1]
  Q57  Kind<Kindle<King<Kite<Knit                  → A  (1,5,4,2,3)
       KIND is prefix of KINDLE → Kind first; then King(KIN-G) < Kite(KIT) < Knit(KNI)
       [GD Con-11 Jan 2023 Shift 1]
  Q58  Individual<Inertia<Inside<Insight<Instruction → B  (5,2,1,4,3)
       IN-D < IN-E < INS-I-D < INS-I-G < INS-T
       [GD Con-10 Jan 2023 Shift 4]
  Q59  Magic<Manage<Manner<Masculine<Matter         → C  (4,2,1,3,5)
       MA-G < MA-N-A < MA-N-N < MA-S < MA-T
       [GD Con-10 Jan 2023 Shift 1]
  Q60  Locker<Lonely<Longitude<Lounge<Lovely        → C  (5,1,2,4,3)
       LO-C < LO-N-E < LO-N-G < LO-U < LO-V
       [GD Con-10 Jan 2023 Shift 2]
  Q61  PUZZLE: P(4)U(5)Z(6)Z(2)L(3)E(1)            → D  (4,5,6,2,3,1)
       E=1,Z=2,L=3,P=4,U=5,Z=6  [CGL Tier II-2 March 2023 Shift 1]
  Q62  Brief<Bright<Brine<Brocade<Brochure          → C  (4,3,2,5,1)
       BRI-E < BRI-G < BRI-N < BRO-C-A < BRO-C-H
       [CPO-05 Oct 2023 Shift 3]
  Q63  Warden<Wardrobe<Warehouse<Warfare<Warrant<Warship → B  (2,4,1,6,5,3)
       WAR-D-E < WAR-D-R < WAR-E < WAR-F < WAR-R-A < WAR-S
       [CPO-05 Oct 2023 Shift 3]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q51 ── Chain<Chair<Charcoal<Charge<Charm → 2,1,5,4,3 ─────────────────
    # Words: 1.Chair 2.Chain 3.Charm 4.Charge 5.Charcoal
    # CHA-I: Chain(5th=N) < Chair(5th=R); CHA-R: Charcoal(C)<Charge(G)<Charm(M)
    {
        "question_number": 51,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Chair 2.Chain 3.Charm 4.Charge 5.Charcoal — "
            "Which option represents the correct order of the given words "
            "as they would appear in the English dictionary? "
            "[GD Con-11 Jan 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Chair 2.Chain 3.Charm 4.Charge 5.Charcoal — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "2, 1, 5, 4, 3",
        "option_b": "1, 2, 3, 4, 5",
        "option_c": "3, 5, 1, 4, 2",
        "option_d": "2, 3, 1, 4, 5",
        "correct_answer": "A",
        # CHAIN(CHA-I-N) < CHAIR(CHA-I-R) < CHARCOAL(CHA-R-C) < CHARGE(CHA-R-G) < CHARM(CHA-R-M)
    },
    # ── Q52 ── Peach<Peacock<Peanut<Peasant<Pencil → 4,3,1,2,5 ──────────────
    # Words: 1.Peanut 2.Peasant 3.Peacock 4.Peach 5.Pencil
    # PEAC-H(8th letter) < PEAC-O(15th letter) → Peach before Peacock
    {
        "question_number": 52,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Peanut 2.Peasant 3.Peacock 4.Peach 5.Pencil — "
            "Which option represents the correct order of the given words "
            "as they would appear in the English dictionary? "
            "[GD Con-12 Jan 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Peanut 2.Peasant 3.Peacock 4.Peach 5.Pencil — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "4, 3, 5, 1, 2",
        "option_b": "3, 4, 5, 1, 2",
        "option_c": "4, 3, 1, 2, 5",
        "option_d": "3, 4, 1, 2, 5",
        "correct_answer": "C",
        # Peach(PEAC-H) < Peacock(PEAC-O) < Peanut(PEA-N) < Peasant(PEA-S) < Pencil(PEN)
    },
    # ── Q53 ── Jumbled word: EADL → DEAL ─────────────────────────────────────
    {
        "question_number": 53,
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
        "correct_answer": "C",  # EADL rearranged → DEAL
    },
    # ── Q54 ── Taciturn<Talisman<Tangential<Tantalizing<Tantamount → 5,1,3,4,2 ─
    # Words: 1.Talisman 2.Tantamount 3.Tangential 4.Tantalizing 5.Taciturn
    {
        "question_number": 54,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Talisman 2.Tantamount 3.Tangential 4.Tantalizing 5.Taciturn — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[CHSL Tier II-26 Jun 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Talisman 2.Tantamount 3.Tangential 4.Tantalizing 5.Taciturn — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "4, 2, 3, 5, 1",
        "option_b": "1, 4, 3, 5, 2",
        "option_c": "3, 5, 1, 4, 2",
        "option_d": "5, 1, 3, 4, 2",
        "correct_answer": "D",
        # TAC(5) < TAL(1) < TAN-G(3) < TANT-A-L(4) < TANT-A-M(2)
    },
    # ── Q55 ── Jumbled word: ETNSIL → SILENT ─────────────────────────────────
    {
        "question_number": 55,
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
        "correct_answer": "A",  # ETNSIL → SILENT (context: adjective for "night")
    },
    # ── Q56 ── Number codes: STUDENT = S(4)T(3)U(7)D(6)E(1)N(2)T(5) → 4,3,7,6,1,2,5 ──
    # E=1, N=2, T=3, S=4, T=5, D=6, U=7
    {
        "question_number": 56,
        "difficulty": "medium",
        "question_en": (
            "A number has been denoted to each of the given letters. "
            "Select the option from the following four possible arrangements "
            "of these numbers that form a meaningful word. "
            "E=1, N=2, T=3, S=4, T=5, D=6, U=7 "
            "[CGL Tier II-3 March 2023 Shift 1]"
        ),
        "question_hi": (
            "दिए गए प्रत्येक अक्षर को एक संख्या दी गई है। "
            "नीचे दिए गए चार संभावित व्यवस्थाओं में से उस विकल्प का चयन कीजिए "
            "जो एक सार्थक शब्द बनाती है। "
            "E=1, N=2, T=3, S=4, T=5, D=6, U=7"
        ),
        "option_a": "4, 3, 7, 6, 1, 2, 5",
        "option_b": "4, 7, 3, 6, 2, 1, 5",
        "option_c": "1, 4, 7, 6, 2, 3, 5",
        "option_d": "7, 3, 4, 6, 2, 1, 5",
        "correct_answer": "A",
        # 4,3,7,6,1,2,5 = S,T,U,D,E,N,T = STUDENT ✓
    },
    # ── Q57 ── Kind<Kindle<King<Kite<Knit → 1,5,4,2,3 ────────────────────────
    # Words: 1.Kind 2.Kite 3.Knit 4.King 5.Kindle
    # KIND is a prefix of KINDLE → Kind(1) before Kindle(5); King(KIN-G) < Kite(KIT) < Knit(KNI)
    {
        "question_number": 57,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Kind 2.Kite 3.Knit 4.King 5.Kindle — "
            "Which option represents the correct order of the given words "
            "as they would appear in the English dictionary? "
            "[GD Con-11 Jan 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Kind 2.Kite 3.Knit 4.King 5.Kindle — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "1, 5, 4, 2, 3",
        "option_b": "1, 4, 2, 5, 3",
        "option_c": "1, 5, 2, 4, 3",
        "option_d": "2, 3, 1, 4, 5",
        "correct_answer": "A",
        # Kind(KIN-D) < Kindle(KIN-D-L) < King(KIN-G) < Kite(KIT) < Knit(KNI) → 1,5,4,2,3
    },
    # ── Q58 ── Individual<Inertia<Inside<Insight<Instruction → 5,2,1,4,3 ──────
    # Words: 1.Inside 2.Inertia 3.Instruction 4.Insight 5.Individual
    {
        "question_number": 58,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Inside 2.Inertia 3.Instruction 4.Insight 5.Individual — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-10 Jan 2023 Shift 4]"
        ),
        "question_hi": (
            "शब्द: 1.Inside 2.Inertia 3.Instruction 4.Insight 5.Individual — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "5, 3, 1, 2, 4",
        "option_b": "5, 2, 1, 4, 3",
        "option_c": "5, 1, 2, 3, 4",
        "option_d": "5, 2, 3, 4, 1",
        "correct_answer": "B",
        # IN-D(Individual5) < IN-E(Inertia2) < INS-I-D(Inside1) < INS-I-G(Insight4) < INS-T(Instruction3)
    },
    # ── Q59 ── Magic<Manage<Manner<Masculine<Matter → 4,2,1,3,5 ─────────────
    # Words: 1.Manner 2.Manage 3.Masculine 4.Magic 5.Matter
    {
        "question_number": 59,
        "difficulty": "easy",
        "question_en": (
            "Words: 1.Manner 2.Manage 3.Masculine 4.Magic 5.Matter — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-10 Jan 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Manner 2.Manage 3.Masculine 4.Magic 5.Matter — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "1, 2, 4, 3, 5",
        "option_b": "4, 2, 3, 1, 5",
        "option_c": "4, 2, 1, 3, 5",
        "option_d": "4, 1, 2, 3, 5",
        "correct_answer": "C",
        # MA-G(Magic4) < MA-N-A(Manage2) < MA-N-N(Manner1) < MA-S(Masculine3) < MA-T(Matter5)
    },
    # ── Q60 ── Locker<Lonely<Longitude<Lounge<Lovely → 5,1,2,4,3 ─────────────
    # Words: 1.Lonely 2.Longitude 3.Lovely 4.Lounge 5.Locker
    {
        "question_number": 60,
        "difficulty": "easy",
        "question_en": (
            "Words: 1.Lonely 2.Longitude 3.Lovely 4.Lounge 5.Locker — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-10 Jan 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Lonely 2.Longitude 3.Lovely 4.Lounge 5.Locker — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "5, 1, 2, 3, 4",
        "option_b": "5, 2, 1, 3, 4",
        "option_c": "5, 1, 2, 4, 3",
        "option_d": "4, 5, 3, 1, 2",
        "correct_answer": "C",
        # LO-C(Locker5) < LO-N-E(Lonely1) < LO-N-G(Longitude2) < LO-U(Lounge4) < LO-V(Lovely3)
    },
    # ── Q61 ── Number codes: PUZZLE = P(4)U(5)Z(6)Z(2)L(3)E(1) → 4,5,6,2,3,1 ──
    # E=1, Z=2, L=3, P=4, U=5, Z=6
    {
        "question_number": 61,
        "difficulty": "medium",
        "question_en": (
            "A number has been denoted to each of the given letters. "
            "Select the option from the following four possible arrangements "
            "of these numbers that form a meaningful word. "
            "E=1, Z=2, L=3, P=4, U=5, Z=6 "
            "[CGL Tier II-2 March 2023 Shift 1]"
        ),
        "question_hi": (
            "दिए गए प्रत्येक अक्षर को एक संख्या दी गई है। "
            "नीचे दिए गए चार संभावित व्यवस्थाओं में से उस विकल्प का चयन कीजिए "
            "जो एक सार्थक शब्द बनाती है। "
            "E=1, Z=2, L=3, P=4, U=5, Z=6"
        ),
        "option_a": "4, 5, 3, 2, 1, 6",
        "option_b": "1, 5, 3, 4, 2, 6",
        "option_c": "1, 5, 4, 6, 3, 2",
        "option_d": "4, 5, 6, 2, 3, 1",
        "correct_answer": "D",
        # 4,5,6,2,3,1 = P,U,Z,Z,L,E = PUZZLE ✓
    },
    # ── Q62 ── Brief<Bright<Brine<Brocade<Brochure → 4,3,2,5,1 ──────────────
    # Words: 1.Brochure 2.Brine 3.Bright 4.Brief 5.Brocade
    {
        "question_number": 62,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Brochure 2.Brine 3.Bright 4.Brief 5.Brocade — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-05 Oct 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Brochure 2.Brine 3.Bright 4.Brief 5.Brocade — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "1, 2, 3, 4, 5",
        "option_b": "1, 2, 3, 5, 4",
        "option_c": "4, 3, 2, 5, 1",
        "option_d": "3, 2, 5, 4, 1",
        "correct_answer": "C",
        # BRI-E(Brief4) < BRI-G(Bright3) < BRI-N(Brine2) < BRO-C-A(Brocade5) < BRO-C-H(Brochure1)
    },
    # ── Q63 ── Warden<Wardrobe<Warehouse<Warfare<Warrant<Warship → 2,4,1,6,5,3 ──
    # Words: 1.Warehouse 2.Warden 3.Warship 4.Wardrobe 5.Warrant 6.Warfare
    {
        "question_number": 63,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Warehouse 2.Warden 3.Warship 4.Wardrobe 5.Warrant 6.Warfare — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-05 Oct 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Warehouse 2.Warden 3.Warship 4.Wardrobe 5.Warrant 6.Warfare — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "4, 2, 1, 6, 5, 3",
        "option_b": "2, 4, 1, 6, 5, 3",
        "option_c": "2, 4, 6, 1, 5, 3",
        "option_d": "2, 4, 1, 5, 6, 3",
        "correct_answer": "B",
        # WAR-D-E(Warden2) < WAR-D-R(Wardrobe4) < WAR-E(Warehouse1) < WAR-F(Warfare6) < WAR-R-A(Warrant5) < WAR-S(Warship3)
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
