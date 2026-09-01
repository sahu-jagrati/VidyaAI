"""
seed_reasoning_dice_sheet2.py
==============================
Seeds Reasoning → Dice  Q5–Q10.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q5  C  (3)
     Minimum colours to paint all faces of a cube so no two adjacent
     faces share the same colour = chromatic number of the face-adjacency
     graph (octahedral graph K_{2,2,2}) = 3.
     Assign: {Top, Bottom}=Colour-1, {Front, Back}=Colour-2,
     {Left, Right}=Colour-3. Two colours fail because e.g. Left and Top
     are adjacent but both would need Colour-1.
     [UPPSC Prelims CSAT 2021]

Q6  C  (B — Blue)
     Net layout (row, col):
       (1,1)=R  (1,2)=B
       (2,1)=G  (2,2)=Y  (2,3)=O
                          (3,3)=W
     Fold with Y as front face:
       G (left of Y)  → left face
       O (right of Y) → right face
       B (above Y)    → top face
       W (below O)    → bottom face (wraps around O's base)
       R (above G)    → back face
     Opposite pairs: {Y,R}, {G,O}, {B,W}
     opp(White/W) = Blue/B.
     [GPSC BDO Pre Screening 04-12-2021]

Q7  A  (Violet / बैंगनी)
     6 colours: Violet, Orange, Blue, Yellow, Red, Rose.
     From four dice positions:
       Yellow adj Blue, Orange, Red  →  opp(Yellow) ≠ Blue, Orange, Red
       Violet adj Orange, Red, Rose  (from other positions)
       Pos showing Violet adj Orange, Blue; and Rose adj Red, Violet
       Only Yellow and Violet never appear on adjacent faces with each other.
     → opp(Yellow) = Violet.
     [GPSC BDO Repeat Pre Screening 18-12-2021 Set 1]

Q8  B  (P)
     6 letters: K, M, B, N, H, P on dice faces.
     Three positions adjacency:
       Pos 1: K adj M, K adj B,  M adj B
       Pos 2: N adj M, N adj P,  M adj P
       Pos 3: B adj H, B adj P,  H adj P
     Derive adjacency set for each:
       K adj {M,B};  M adj {K,B,N,P};  B adj {K,M,H,P}
       N adj {M,P};  H adj {B,P};       P adj {N,M,B,H}
     opp(M): M adj K,B,N,P → opp(M)=H (only remaining)
     opp(B): B adj K,M,H,P → opp(B)=N
     opp(K): K adj M,B → opp(K)=P (only remaining after {M,H} and {B,N} pairs)
     [GPSC BDO Repeat Pre Screening 18-12-2021 Set 1]

Q9  B  (5)
     Four dot-dice positions. Adjacency analysis:
       2 adj 1, 3, 4, 6  (seen across four positions)
     Only face NOT adjacent to 2 is 5 → opp(2) = 5.
     [GPSC BDO Repeat Pre Screening 18-12-2021 Set 1]

Q10 D  (M)
     6 letters: A, B, H, K, M, P on dice faces.
     Three positions adjacency:
       Pos 1: K adj A, K adj B,  A adj B
       Pos 2: H adj K, H adj M,  K adj M
       Pos 3: B adj H, B adj P,  H adj P
     Adjacency sets:
       K adj {A,B,H,M};  → opp(K)=P
       H adj {K,M,B,P};  → opp(H)=A  (only A not in H's adj set after removing P→K)
       opp(A)=H  ∴  opp(B)=M
     opp(B) = M.
     [GPSC BDO Pre Screening 04-12-2021]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

QUESTIONS = [

    # ── Q5 [UPPSC Prelims CSAT 2021] ─────────────────────────────────────────
    # Min colours to paint cube so no two adjacent faces share a colour.
    # Chromatic number of octahedral face-adjacency graph = 3.
    {
        "question_number": 5,
        "difficulty": "medium",
        "source_pdf": "UPPSC_CSAT_2021",
        "question_en": (
            "The minimum number of colours required to paint all faces of a cube, "
            "such that no two adjacent faces may have the same colour, is:"
        ),
        "question_hi": (
            "एक घन के सभी सतहों को रंगने के लिए आवश्यक रंगों की न्यूनतम संख्या है, "
            "ताकि किसी भी दो आसन्न सतहों का रंग एक जैसा न हो:"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "6",
        "correct_answer": "C",   # chromatic number = 3
    },

    # ── Q6 [GPSC BDO Pre Screening 04-12-2021] ───────────────────────────────
    # Net: (1,1)=R (1,2)=B / (2,1)=G (2,2)=Y (2,3)=O / (3,3)=W
    # Fold: Y=front, G=left, O=right, B=top, W=bottom, R=back
    # opp(White) = Blue
    {
        "question_number": 6,
        "difficulty": "medium",
        "source_pdf": "GPSC_BDO_Pre_Screening_04_12_2021",
        "question_en": (
            "Six squares are coloured — front and back: red (R), blue (B), yellow (Y), "
            "green (G), white (W) and orange (O) — as shown in the figure below. "
            "If they are folded to form a cube, what would be the face opposite to white colour?\n"
            "[Net layout: Row-1: R B | Row-2: G Y O | Row-3 (col-3): W]"
        ),
        "question_hi": (
            "छह वर्ग रंगीन हैं — आगे और पीछे: लाल (R), नीला (B), पीला (Y), हरा (G), "
            "सफेद (W) और नारंगी (O) — जैसा कि नीचे दिए गए चित्र में दिखाया गया है। "
            "यदि इन्हें मोड़कर एक घन बनाया जाए तो सफेद रंग के विपरीत फलक क्या होगा?\n"
            "[जाल: पंक्ति-1: R B | पंक्ति-2: G Y O | पंक्ति-3 (कॉल-3): W]"
        ),
        "image_url": None,
        "option_a": "R",
        "option_b": "G",
        "option_c": "B",
        "option_d": "O",
        "correct_answer": "C",   # opp(W) = B (Blue)
    },

    # ── Q7 [GPSC BDO Repeat Pre Screening 18-12-2021 Set 1] ─────────────────
    # 4 colour-dice positions; which colour is opposite to yellow?
    # Yellow adj Blue, Orange, Red → opp(Yellow) = Violet
    {
        "question_number": 7,
        "difficulty": "medium",
        "source_pdf": "GPSC_BDO_Repeat_Pre_Screening_18_12_2021_Set1",
        "question_en": (
            "From the four positions of a dice given below, find the colour which "
            "is opposite to yellow?"
        ),
        "question_hi": (
            "नीचे दिए गए पासे की चार स्थितियों में से वह रंग ज्ञात कीजिए जो "
            "पीले रंग के विपरीत है?"
        ),
        "image_url": None,
        "option_a": "Violet / बैंगनी",
        "option_b": "Red / लाल",
        "option_c": "Blue / नीला",
        "option_d": "None of these / इनमें से कोई नहीं",
        "correct_answer": "A",   # opp(Yellow) = Violet
    },

    # ── Q8 [GPSC BDO Repeat Pre Screening 18-12-2021 Set 1] ─────────────────
    # 3 letter-dice positions (K,M,B,N,H,P); which letter is opposite to K?
    # Full adjacency: opp(M)=H, opp(B)=N, opp(K)=P
    {
        "question_number": 8,
        "difficulty": "hard",
        "source_pdf": "GPSC_BDO_Repeat_Pre_Screening_18_12_2021_Set1",
        "question_en": (
            "From the three positions of a dice given below, which letter is opposite to K?\n"
            "[Dice faces carry letters: K, M, B, N, H, P]"
        ),
        "question_hi": (
            "नीचे दिए गए पासे की तीन स्थितियों में से कौन सा अक्षर K के विपरीत है?\n"
            "[पासे के फलकों पर अक्षर हैं: K, M, B, N, H, P]"
        ),
        "image_url": None,
        "option_a": "H",
        "option_b": "P",
        "option_c": "B",
        "option_d": "M",
        "correct_answer": "B",   # opp(K) = P
    },

    # ── Q9 [GPSC BDO Repeat Pre Screening 18-12-2021 Set 1] ─────────────────
    # 4 dot-dice positions; which dot face is opposite to dot 2?
    # 2 adj 1,3,4,6 across four positions → opp(2) = 5
    {
        "question_number": 9,
        "difficulty": "medium",
        "source_pdf": "GPSC_BDO_Repeat_Pre_Screening_18_12_2021_Set1",
        "question_en": (
            "From the four positions of a dice given below, which dot face is "
            "opposite to dot 2?"
        ),
        "question_hi": (
            "नीचे दिए गए पासे की चार स्थितियों में से, कौन सा बिंदु वाला फलक "
            "बिंदु 2 के विपरीत है?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "5",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "B",   # opp(2) = 5
    },

    # ── Q10 [GPSC BDO Pre Screening 04-12-2021] ──────────────────────────────
    # 3 letter-dice positions (A,B,H,K,M,P); which letter is opposite to B?
    # Adjacency: K adj {A,B,H,M}→opp(K)=P; H adj {K,M,B,P}→opp(H)=A; opp(B)=M
    {
        "question_number": 10,
        "difficulty": "hard",
        "source_pdf": "GPSC_BDO_Pre_Screening_04_12_2021",
        "question_en": (
            "From the three positions of a dice given below, which letter is opposite to B?\n"
            "[Dice faces carry letters: A, B, H, K, M, P]"
        ),
        "question_hi": (
            "नीचे दिए गए पासे की तीन स्थितियों में से कौन सा अक्षर B के विपरीत है?\n"
            "[पासे के फलकों पर अक्षर हैं: A, B, H, K, M, P]"
        ),
        "image_url": None,
        "option_a": "H",
        "option_b": "P",
        "option_c": "B",
        "option_d": "M",
        "correct_answer": "D",   # opp(B) = M
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
