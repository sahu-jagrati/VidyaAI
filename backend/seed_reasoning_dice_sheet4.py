"""
seed_reasoning_dice_sheet4.py
==============================
Seeds Reasoning → Dice  Q16–Q19.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q16 B  (Three dots / तीन बिंदु)
     Same solid as Q14/Q15 [UPSC CSAT 2018].
     Established pairs: {· , ····}, {·· , —}
     By elimination: opp(×) = ··· (three dots).
     NOTE: The compiled PDF lists option (b) as "Two dots" — this is
     a typo; corrected here to "Three dots".
     [UPSC Prelims CSAT 2018]

Q17 A  (8)
     4×4×4 cube painted red on all outer faces; sliced into
     1×1×1 unit cubes (total = 64).
     Interior cubes (zero painted faces) = (4−2)³ = 2³ = 8.
     [UPSC Prelims CSAT 2017]

Q18 C  (G)
     Faces: V, I, B, G, Y, O.
     Clue adjacency:
       C1: Y adj O, Y adj B, O adj B
       C2: I adj G, I adj Y, G adj Y
       C3: B adj G, B adj Y, G adj Y
       C4: O adj V, O adj B, V adj B
     Y adj {O, B, I, G} = 4 → opp(Y) = V.
     Pairs {Y,V} fixed.  From remaining {I,B,G,O}:
       B adj {Y,O,G,V} (all 4) → opp(B) = I.
       G adj {Y,I,B,V} (all 4) → opp(G) = O.
     → opp(O) = G.
     [UPSC Prelims CSAT 2015]

Q19 B  (Box b)
     Net X:  F above E | A left of E | B below E | C below B | D right of C
     Fold with E=Front: F=Top, A=Left, B=Bottom, C=Back, D=Right.
     Opposite pairs: {E,C}, {F,B}, {A,D}.
     Option (a): shows F & B (opposite) → INVALID.
     Option (b): shows F, E, D — all mutually adjacent → VALID ✓.
     Option (c): shows E & C (opposite) → INVALID.
     Option (d): shows A & D (opposite) → INVALID.
     [UPPSC Prelims CSAT 2015]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

QUESTIONS = [

    # ── Q16 [UPSC Prelims CSAT 2018] ─────────────────────────────────────────
    # Third question about the same solid as Q14/Q15.
    # Pairs: {·,····}, {··,—} → opp(×) = ··· (three dots).
    # PDF typo: option (b) printed as "Two dots"; corrected to "Three dots".
    {
        "question_number": 16,
        "difficulty": "hard",
        "source_pdf": "UPSC_CSAT_2018",
        "question_en": (
            "The rotated positions of a single solid are shown below. The various faces "
            "of the solid are marked with different symbols like dots, a cross, and a line. "
            "Answer the three items that follow the given figures.\n"
            "What is the symbol on the face opposite to that containing the cross?"
        ),
        "question_hi": (
            "एकल ठोस की घुमाई गई स्थिति नीचे दिखाई गई है। ठोस के विभिन्न चेहरों को "
            "बिंदु, एक क्रॉस और एक रेखा जैसे विभिन्न प्रतीकों से चिह्नित किया जाता है। "
            "दिए गए आंकड़ों का पालन करने वाले तीन प्रश्नों के उत्तर दीजिए।\n"
            "क्रॉस वाले फलक के विपरीत फलक पर कौन सा चिह्न है?"
        ),
        "image_url": None,
        "option_a": "Single dot / एकल बिंदु",
        "option_b": "Three dots / तीन बिंदु",   # corrected from PDF's "Two dots" typo
        "option_c": "Line / रेखा",
        "option_d": "Four dots / चार बिंदु",
        "correct_answer": "B",   # opp(cross) = three dots
    },

    # ── Q17 [UPSC Prelims CSAT 2017] ─────────────────────────────────────────
    # 4×4×4 cube painted red, sliced into 1×1×1 cubes.
    # Interior (unpainted) = (4−2)³ = 8.
    {
        "question_number": 17,
        "difficulty": "medium",
        "source_pdf": "UPSC_CSAT_2017",
        "question_en": (
            "The outer surface of a 4 cm × 4 cm × 4 cm cube is painted completely in red. "
            "It is sliced parallel to the faces to yield sixty-four 1 cm × 1 cm × 1 cm "
            "small cubes. How many small cubes do not have painted faces?"
        ),
        "question_hi": (
            "4 सेमी × 4 सेमी × 4 सेमी के घन की बाहरी सतह पूरी तरह से लाल रंग से रंगी गई है। "
            "इसे फलकों के समानांतर काटा जाता है जिससे 64 छोटे 1 सेमी × 1 सेमी × 1 सेमी "
            "के घन प्राप्त होते हैं। ऐसे कितने छोटे घन हैं जिनके फलक रंगे हुए नहीं हैं?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "16",
        "option_c": "24",
        "option_d": "36",
        "correct_answer": "A",   # (4−2)³ = 2³ = 8 interior cubes
    },

    # ── Q18 [UPSC Prelims CSAT 2015] ─────────────────────────────────────────
    # 6-colour cube with adjacency clues; find colour opposite to O.
    # Derivation: opp(Y)=V, opp(B)=I, opp(G)=O  →  opp(O)=G.
    {
        "question_number": 18,
        "difficulty": "hard",
        "source_pdf": "UPSC_CSAT_2015",
        "question_en": (
            "Each of the six different faces of a cube has been coated with a different "
            "colour i.e., V, I, B, G, Y, and O. Following information is given:\n"
            "1. Colours Y, O, and B are on adjacent faces.\n"
            "2. Colours I, G, and Y are on adjacent faces.\n"
            "3. Colours B, G, and Y are on adjacent faces.\n"
            "4. Colours O, V and B are on adjacent faces.\n"
            "Which is the colour of the face opposite to the face coloured with O?"
        ),
        "question_hi": (
            "एक घन के छह अलग-अलग चेहरों में से प्रत्येक को एक अलग रंग यानी V, I, B, G, "
            "Y और O से लेपित किया गया है। निम्नलिखित जानकारी दी गई है:\n"
            "1. रंग Y, O और B आसन्न चेहरों पर हैं।\n"
            "2. रंग I, G और Y आसन्न चेहरों पर हैं।\n"
            "3. रंग B, G और Y आसन्न चेहरों पर हैं।\n"
            "4. रंग O, V और B आसन्न चेहरों पर हैं।\n"
            "O से रंगे हुए चेहरे के विपरीत चेहरे का रंग कौन सा है?"
        ),
        "image_url": None,
        "option_a": "B",
        "option_b": "V",
        "option_c": "G",
        "option_d": "I",
        "correct_answer": "C",   # opp(O) = G
    },

    # ── Q19 [UPPSC Prelims CSAT 2015] ────────────────────────────────────────
    # Net X: F(above E), A(left of E), B(below E), C(below B), D(right of C).
    # Opposite pairs: {E,C}, {F,B}, {A,D}.
    # Only box (b) — showing F, E, D (all mutually adjacent) — is valid.
    {
        "question_number": 19,
        "difficulty": "medium",
        "source_pdf": "UPPSC_CSAT_2015",
        "question_en": (
            "Which one among the following boxes will be made from the given sheet of paper (X)?\n"
            "[Net X: F above E | A left of E | B below E | C below B | D right of C]"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा डिब्बा दिए गए कागज के टुकड़े (X) से बनाया जाएगा?\n"
            "[जाल X: F, E के ऊपर | A, E के बाएं | B, E के नीचे | C, B के नीचे | D, C के दाएं]"
        ),
        "image_url": None,
        "option_a": "Box (a) / डिब्बा (a)",
        "option_b": "Box (b) / डिब्बा (b)",
        "option_c": "Box (c) / डिब्बा (c)",
        "option_d": "Box (d) / डिब्बा (d)",
        "correct_answer": "B",   # F,E,D all mutually adjacent → only valid view
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
            if row[0] is not None
        }
        print(f"Topic '{TOPIC}' — existing question_numbers: {len(existing_qnums)}")

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
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
