"""
seed_reasoning_venn_diagram_sheet8.py
=======================================
Seeds Reasoning → Venn Diagram  Q56–Q64.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch8.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q56 B  (Indian/Leader/Singer diagram — Indian AND Leader AND Singer)
     Region map: a=Indian only, b=Indian∩Leader, c=all three,
       d=Indian∩Singer, e=Leader∩Singer, f=Leader only, g=Singer only.
     "Indian AND Leader AND Singer" = region c (triple intersection). → B.

Q57 A  (Same diagram — Indian AND Leader but NOT Singer)
     "Indian AND Leader, NOT Singer" = region b (Indian∩Leader overlap,
     outside Singer circle). → A.

Q58 C  (Garden: Square=Jackfruit trees, Circle=Mango trees, △=Coconut trees)
     "Common area where all types of trees are grown" = region where
     circle, square, and triangle all overlap. From the numbered figure
     = region 7. → C.

Q59 C  (TV Survey: ○=Asia net, □=ZTV, △=Sun TV)
     "Number indicating people who watch all three TV channels" =
     intersection of circle, square, and triangle = region 6. → C.

Q60 C  (Numbers present in ONLY ONE of the geometric figures)
     From the Venn diagram of overlapping geometric shapes:
     Numbers in only one shape (non-overlapping regions) = 3, 7, 9. → C.

Q61 B  (Figure: Women, Employed, Doctors — Women Doctors NOT Employed)
     "Women Doctors who are not Employed" = Women ∩ Doctors region,
     outside the Employed shape. From the diagram = region 3. → B.

Q62 A  (3 unions Venn diagram — members of ALL THREE unions)
     "Persons who are members of all three unions" = triple intersection
     of three overlapping circles = region 2. → A.

Q63 B  (○=wise men, □=experienced men, △=teachers —
        teachers who are wise AND experienced)
     "Teachers who are wise as well as experienced" = triple intersection
     of circle, square, and triangle = region 3. → B.

Q64 B  (○=villagers, △=educated, □=employed —
        "Some educated villagers are employed")
     The region where villagers (circle), educated (triangle), and
     employed (rectangle) all overlap = region 4. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q56 ──────────────────────────────────────────────────────────────────
    # Same Indian/Leader/Singer Venn diagram (regions a–g).
    # "Indian AND Leader AND Singer" = region c (triple intersection).
    {
        "question_number": 56,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the figure carefully and answer the questions. "
            "Which symbol indicates an Indian, a leader as well as a singer?"
        ),
        "question_hi": (
            "चित्र का ध्यानपूर्वक अध्ययन करें और प्रश्नों के उत्तर दें। "
            "कौन सा प्रतीक एक भारतीय, एक नेता और एक गायक को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "b",
        "option_b": "c",
        "option_c": "d",
        "option_d": "e",
        "correct_answer": "B",
        # Region c = Indian ∩ Leader ∩ Singer (all three circles).
    },

    # ── Q57 ──────────────────────────────────────────────────────────────────
    # Same Indian/Leader/Singer Venn diagram (regions a–g).
    # "Indian AND Leader, NOT Singer" = region b.
    {
        "question_number": 57,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the figure carefully and answer the questions. "
            "Which symbol indicates Indian and a leader but not a singer?"
        ),
        "question_hi": (
            "चित्र का ध्यानपूर्वक अध्ययन करें और प्रश्नों के उत्तर दें। "
            "कौन सा प्रतीक भारतीय और एक नेता को दर्शाता है "
            "लेकिन एक गायक को नहीं?"
        ),
        "image_url": None,
        "option_a": "b",
        "option_b": "c",
        "option_c": "d",
        "option_d": "e",
        "correct_answer": "A",
        # Region b = Indian ∩ Leader, outside Singer circle.
    },

    # ── Q58 ──────────────────────────────────────────────────────────────────
    # Garden figure: Square=Jackfruit, Circle=Mango, Triangle=Coconut.
    # "Common area where all types of trees are grown" = triple intersection = 7.
    {
        "question_number": 58,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following figure in a garden, square represents the area "
            "where Jackfruit trees are grown; circle represents Mango trees and "
            "triangle represents Coconut trees. Which number represents the "
            "common area in which all types of trees are grown?"
        ),
        "question_hi": (
            "नीचे दिए गए आकृति में, वर्ग उस क्षेत्र को दर्शाता है "
            "जहाँ कटहल के पेड़ उगाए जाते हैं; वृत्त आम के पेड़ों को "
            "दर्शाता है और त्रिकोण नारियल के पेड़ों को दर्शाता है। "
            "कौन सी संख्या उस सामान्य क्षेत्र को दर्शाती है "
            "जिसमें सभी प्रकार के पेड़ उगाए जाते हैं?"
        ),
        "image_url": None,
        "option_a": "4",
        "option_b": "3",
        "option_c": "7",
        "option_d": "8",
        "correct_answer": "C",
        # Region 7 = intersection of circle (Mango), square (Jackfruit),
        # and triangle (Coconut) — common to all three.
    },

    # ── Q59 ──────────────────────────────────────────────────────────────────
    # TV survey: Circle=Asia net, Square=ZTV, Triangle=Sun TV.
    # "People who watch all three channels" = triple intersection = 6.
    {
        "question_number": 59,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "When a survey was made regarding the preferences in the watching "
            "of TV channel, a few said that they watch only ZTV channel, the "
            "others liked only Sun TV channel, while others Asianet TV Channel. "
            "A small percentage said that they watch all the three TV channels. "
            "In the figure given below the circle indicates the Asia net TV "
            "channel, the square ZTV and the triangle the Sun TV channel. "
            "Which number in the figure indicates the fact that some people "
            "watch all the three TV channels?"
        ),
        "question_hi": (
            "जब टीवी चैनल देखने की प्राथमिकताओं के संबंध में एक सर्वेक्षण "
            "किया गया, तो कुछ ने कहा कि वे केवल ZTV चैनल देखते हैं, "
            "अन्य ने केवल सन टीवी चैनल पसंद किया, जबकि अन्य ने "
            "एशियानेट टीवी चैनल पसंद किया। एक छोटे प्रतिशत ने कहा "
            "कि वे तीनों टीवी चैनल देखते हैं। नीचे दिए गए चित्र में "
            "वृत्त एशिया नेट टीवी चैनल, वर्ग ZTV और त्रिभुज सन टीवी "
            "चैनल को दर्शाता है। चित्र में कौन सी संख्या इस तथ्य को "
            "दर्शाती है कि कुछ लोग तीनों टीवी चैनल देखते हैं?"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "5",
        "option_c": "6",
        "option_d": "3",
        "correct_answer": "C",
        # Region 6 = intersection of circle (Asia net), square (ZTV),
        # and triangle (Sun TV) — people watching all three.
    },

    # ── Q60 ──────────────────────────────────────────────────────────────────
    # Numbers present in ONLY ONE of the geometric figures (not in any overlap).
    # From the Venn diagram: numbers in non-overlapping regions = 3, 7, 9.
    {
        "question_number": 60,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which are the numbers that make their presence felt in "
            "only one of the geometric figures?"
        ),
        "question_hi": (
            "वे कौन सी संख्याएँ हैं जो ज्यामितीय आकृतियों में से "
            "केवल एक में अपनी उपस्थिति दर्ज कराती हैं?"
        ),
        "image_url": None,
        "option_a": "4, 6, 7",
        "option_b": "1, 2, 9",
        "option_c": "3, 7, 9",
        "option_d": "2, 3, 8",
        "correct_answer": "C",
        # Numbers 3, 7, 9 lie in non-overlapping (exclusive) regions.
    },

    # ── Q61 ──────────────────────────────────────────────────────────────────
    # Figure: Women (circle/top), Employed (circle/right), Doctors (triangle/bottom).
    # "Women Doctors who are NOT Employed" = Women ∩ Doctors, outside Employed = 3.
    {
        "question_number": 61,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following figure, which number represent the "
            "Women Doctors who are not Employed?"
        ),
        "question_hi": (
            "निम्नलिखित आंकड़े में, कौन सी संख्या उन महिला "
            "डॉक्टरों का प्रतिनिधित्व करती है जो कार्यरत नहीं हैं?"
        ),
        "image_url": None,
        "option_a": "7",
        "option_b": "3",
        "option_c": "1",
        "option_d": "8",
        "correct_answer": "B",
        # Region 3 = Women ∩ Doctors, excluding Employed.
    },

    # ── Q62 ──────────────────────────────────────────────────────────────────
    # Three-circle Venn diagram for 3 unions.
    # "Members of all three unions" = triple intersection = region 2.
    {
        "question_number": 62,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Membership in 3 unions are represented by the following diagram. "
            "Which region represents the persons who are members of all the "
            "three unions?"
        ),
        "question_hi": (
            "3 यूनियनों में सदस्यता को निम्नलिखित चित्र द्वारा दर्शाया "
            "गया है। कौन सा क्षेत्र उन व्यक्तियों का प्रतिनिधित्व करता "
            "है जो तीनों यूनियनों के सदस्य हैं?"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "5",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "A",
        # Region 2 = triple intersection of all three union circles.
    },

    # ── Q63 ──────────────────────────────────────────────────────────────────
    # ○=wise men, □=experienced men, △=teachers.
    # "Teachers who are wise as well as experienced" = triple intersection = 3.
    {
        "question_number": 63,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given diagram, circle represents wise men, square "
            "represents experienced men, triangle represents teachers. "
            "Which region represents teachers who are wise as well as experienced?"
        ),
        "question_hi": (
            "दिए गए आरेख में, वृत्त बुद्धिमान पुरुषों को दर्शाता है, "
            "वर्ग अनुभवी पुरुषों को दर्शाता है, त्रिकोण शिक्षकों को "
            "दर्शाता है। कौन सा क्षेत्र बुद्धिमान और अनुभवी "
            "शिक्षकों का प्रतिनिधित्व करता है?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "3",
        "option_c": "4",
        "option_d": "2",
        "correct_answer": "B",
        # Region 3 = intersection of circle (wise), square (experienced),
        # and triangle (teachers) — all three overlap.
    },

    # ── Q64 ──────────────────────────────────────────────────────────────────
    # ○=villagers, △=educated, □=employed.
    # Statement: "Some educated villagers are employed" = triple intersection = 4.
    {
        "question_number": 64,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the figure given below circle represents 'villagers', the "
            "triangle stands for the 'educated' and the rectangle for the "
            "'employed'. Which numbered space represents the statement — "
            "Some educated villagers are employed."
        ),
        "question_hi": (
            "नीचे दिए गए चित्र में वृत्त 'ग्रामीणों' को दर्शाता है, "
            "त्रिभुज 'शिक्षित' को दर्शाता है और आयत 'रोजगार' को "
            "दर्शाता है। कौन सा क्रमांकित स्थान कथन को दर्शाता है — "
            "कुछ शिक्षित ग्रामीण कार्यरत हैं।"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "4",
        "option_c": "6",
        "option_d": "8",
        "correct_answer": "B",
        # Region 4 = villagers (circle) ∩ educated (triangle) ∩ employed (rectangle).
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q56–Q64 into '{TOPIC}' / '{SUBJECT}'")

        for d in QUESTIONS:
            qn = d["question_number"]
            exists = (
                db.query(Question)
                .filter(
                    Question.subject == SUBJECT,
                    Question.topic == TOPIC,
                    Question.question_number == qn,
                )
                .first()
            )
            if exists:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
        if inserted:
            print(
                "\n  Upload venn_56.png … venn_64.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch8.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
