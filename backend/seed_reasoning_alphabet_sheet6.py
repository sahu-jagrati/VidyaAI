"""
seed_reasoning_alphabet_sheet6.py
=========================================
Seeds Alphabet Q41-Q50 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet6.py

NOTE: All are dictionary-ordering questions. "Words: [list] — ..." prefix keeps
first-80-char fingerprints unique across all ordering questions in this topic.

Answer key (solutions verified):
  Q41  Universe/Unicorn/Understood/Unhappy/Uniform  → A  (3,4,2,5,1)
       Understood<Unhappy<Unicorn<Uniform<Universe   [GD Con-1 Feb 2023 Shift 2]
  Q42  FAWN/FAVOUR/FATHER/FATIGUE/FAT/FATE          → C  (5,6,3,4,2,1)
       FAT<FATE<FATHER<FATIGUE<FAVOUR<FAWN           [GD Con-23 Jan 2023 Shift 1]
  Q43  Elegant/Emerald/Elaborate/Elasticity/Elephant → B  (3,4,1,5,2)
       Elaborate<Elasticity<Elegant<Elephant<Emerald  [GD Con-24 Jan 2023 Shift 1]
  Q44  Book/Bowl/Board/Boundary/Botanical            → B  (3,1,5,4,2)
       Board<Book<Botanical<Boundary<Bowl            [GD Con-23 Jan 2023 Shift 4]
  Q45  Vehicle/Verify/Vegan/Venom/Vein              → B  (3,1,5,4,2)
       Vegan<Vehicle<Vein<Venom<Verify              [GD Con-23 Jan 2023 Shift 3]
  Q46  Pillow/Pile/Pint/Picked/Pickle               → B  (4,5,2,1,3)
       Picked<Pickle<Pile<Pillow<Pint              [GD Con-12 Jan 2023 Shift 4]
  Q47  Dream/Drown/Drone/Dropped/Drama              → C  (5,1,3,4,2)
       Drama<Dream<Drone<Dropped<Drown
  Q48  Track/Trace/Trade/Treasure/Triangle          → B  (2,1,3,4,5)
       Trace<Track<Trade<Treasure<Triangle         [GD Con-17 Jan 2023 Shift 1]
  Q49  Jumping/Juice/Jumble/Jupiter/Junior          → B  (2,3,1,5,4)
       Juice<Jumble<Jumping<Junior<Jupiter         [GD Con-16 Jan 2023 Shift 3]
  Q50  Tasty/Tackle/Tamarind/Tadpole/Tagline       → C  (2,4,5,3,1)
       Tackle<Tadpole<Tagline<Tamarind<Tasty       [GD Con-13 Jan 2023 Shift 1]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q41 ── Understood<Unhappy<Unicorn<Uniform<Universe → 3,4,2,5,1 ────────
    # Und(3) < Unh(4) < Uni-c(2) < Uni-f(5) < Uni-v(1)
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Universe 2.Unicorn 3.Understood 4.Unhappy 5.Uniform — "
            "Which option represents the correct order of the given words "
            "as they would appear in the English dictionary? "
            "[GD Con-1 Feb 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Universe 2.Unicorn 3.Understood 4.Unhappy 5.Uniform — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "3, 4, 2, 5, 1",
        "option_b": "3, 4, 5, 1, 2",
        "option_c": "3, 2, 1, 5, 4",
        "option_d": "3, 2, 1, 4, 5",
        "correct_answer": "A",
        # Und(Understood3) < Unh(Unhappy4) < Uni-c(Unicorn2) < Uni-f(Uniform5) < Uni-v(Universe1)
    },
    # ── Q42 ── FAT<FATE<FATHER<FATIGUE<FAVOUR<FAWN → 5,6,3,4,2,1 ─────────────
    # Fat(5) < Fat-e(6) < Fat-h(3) < Fat-i(4) < Fav(2) < Faw(1)
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.FAWN 2.FAVOUR 3.FATHER 4.FATIGUE 5.FAT 6.FATE — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[GD Con-23 Jan 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.FAWN 2.FAVOUR 3.FATHER 4.FATIGUE 5.FAT 6.FATE — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "5, 3, 6, 4, 1, 2",
        "option_b": "2, 6, 3, 4, 5, 1",
        "option_c": "5, 6, 3, 4, 2, 1",
        "option_d": "6, 5, 3, 4, 2, 1",
        "correct_answer": "C",
        # FAT(5) < FATE(6) < FATHER(3) < FATIGUE(4) < FAVOUR(2) < FAWN(1)
    },
    # ── Q43 ── Elaborate<Elasticity<Elegant<Elephant<Emerald → 3,4,1,5,2 ──────
    # Ela-b(3) < Ela-s(4) < Ele-g(1) < Ele-p(5) < Eme(2)
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Elegant 2.Emerald 3.Elaborate 4.Elasticity 5.Elephant — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[GD Con-24 Jan 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Elegant 2.Emerald 3.Elaborate 4.Elasticity 5.Elephant — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 4, 5, 1, 2",
        "option_b": "3, 4, 1, 5, 2",
        "option_c": "4, 3, 2, 5, 1",
        "option_d": "4, 3, 1, 5, 2",
        "correct_answer": "B",
        # Ela-b(Elaborate3) < Ela-s(Elasticity4) < Ele-g(Elegant1) < Ele-p(Elephant5) < Eme(Emerald2)
    },
    # ── Q44 ── Board<Book<Botanical<Boundary<Bowl → 3,1,5,4,2 ─────────────────
    # Bo-a(3) < Bo-o(1) < Bo-t(5) < Bo-u-n(4) < Bo-w(2)
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Book 2.Bowl 3.Board 4.Boundary 5.Botanical — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-23 Jan 2023 Shift 4]"
        ),
        "question_hi": (
            "शब्द: 1.Book 2.Bowl 3.Board 4.Boundary 5.Botanical — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "3, 1, 4, 2, 5",
        "option_b": "3, 1, 5, 4, 2",
        "option_c": "3, 5, 1, 4, 2",
        "option_d": "3, 4, 1, 2, 5",
        "correct_answer": "B",
        # Board(Bo-a-r) < Book(Bo-o) < Botanical(Bo-t) < Boundary(Bo-u-n) < Bowl(Bo-w)
    },
    # ── Q45 ── Vegan<Vehicle<Vein<Venom<Verify → 3,1,5,4,2 ───────────────────
    # Ve-g(3) < Ve-h(1) < Ve-i(5) < Ve-n(4) < Ve-r(2)
    {
        "question_number": 45,
        "difficulty": "easy",
        "question_en": (
            "Words: 1.Vehicle 2.Verify 3.Vegan 4.Venom 5.Vein — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-23 Jan 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Vehicle 2.Verify 3.Vegan 4.Venom 5.Vein — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "3, 4, 2, 1, 5",
        "option_b": "3, 1, 5, 4, 2",
        "option_c": "4, 2, 1, 3, 5",
        "option_d": "4, 1, 2, 3, 5",
        "correct_answer": "B",
        # Vegan(Ve-g) < Vehicle(Ve-h) < Vein(Ve-i) < Venom(Ve-n) < Verify(Ve-r)
    },
    # ── Q46 ── Picked<Pickle<Pile<Pillow<Pint → 4,5,2,1,3 ────────────────────
    # Pic-k-e(4) < Pic-k-l(5) < Pil-e(2) < Pil-l(1) < Pin(3)
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Pillow 2.Pile 3.Pint 4.Picked 5.Pickle — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-12 Jan 2023 Shift 4]"
        ),
        "question_hi": (
            "शब्द: 1.Pillow 2.Pile 3.Pint 4.Picked 5.Pickle — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "5, 2, 4, 1, 3",
        "option_b": "4, 5, 2, 1, 3",
        "option_c": "2, 3, 4, 1, 5",
        "option_d": "3, 1, 4, 5, 2",
        "correct_answer": "B",
        # Pic-k-e(Picked4) < Pic-k-l(Pickle5) < Pil-e(Pile2) < Pil-l(Pillow1) < Pin(Pint3)
    },
    # ── Q47 ── Drama<Dream<Drone<Dropped<Drown → 5,1,3,4,2 ───────────────────
    # Dra-m(5) < Dre(1) < Dro-n(3) < Dro-p(4) < Dro-w(2)
    # NOTE: word 2 = Drown (not Drawn); user noted PDF option (c) may show "5,3,1,4,2"
    # but corrected to 5,1,3,4,2 since Dream(Dre) < Drone(Dro), so option C is 5,1,3,4,2.
    {
        "question_number": 47,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Dream 2.Drown 3.Drone 4.Dropped 5.Drama — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary?"
        ),
        "question_hi": (
            "शब्द: 1.Dream 2.Drown 3.Drone 4.Dropped 5.Drama — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "3, 4, 2, 5, 1",
        "option_b": "3, 4, 1, 5, 2",
        "option_c": "5, 1, 3, 4, 2",
        "option_d": "4, 1, 3, 5, 2",
        "correct_answer": "C",
        # Dra-m(Drama5) < Dre(Dream1) < Dro-n(Drone3) < Dro-p(Dropped4) < Dro-w(Drown2)
    },
    # ── Q48 ── Trace<Track<Trade<Treasure<Triangle → 2,1,3,4,5 ───────────────
    # Trac-e(2) < Trac-k(1) < Tra-d(3) < Tre(4) < Tri(5)
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Track 2.Trace 3.Trade 4.Treasure 5.Triangle — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-17 Jan 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Track 2.Trace 3.Trade 4.Treasure 5.Triangle — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "1, 2, 3, 4, 5",
        "option_b": "2, 1, 3, 4, 5",
        "option_c": "2, 3, 1, 5, 4",
        "option_d": "3, 1, 4, 2, 5",
        "correct_answer": "B",
        # Trac-e(Trace2) < Trac-k(Track1) < Tra-d(Trade3) < Tre(Treasure4) < Tri(Triangle5)
    },
    # ── Q49 ── Juice<Jumble<Jumping<Junior<Jupiter → 2,3,1,5,4 ─────────────────
    # Jui(2) < Jum-b(3) < Jum-p(1) < Jun(5) < Jup(4)
    {
        "question_number": 49,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Jumping 2.Juice 3.Jumble 4.Jupiter 5.Junior — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-16 Jan 2023 Shift 3]"
        ),
        "question_hi": (
            "शब्द: 1.Jumping 2.Juice 3.Jumble 4.Jupiter 5.Junior — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "2, 3, 4, 1, 5",
        "option_b": "2, 3, 1, 5, 4",
        "option_c": "3, 4, 2, 1, 5",
        "option_d": "3, 2, 1, 5, 4",
        "correct_answer": "B",
        # Jui(Juice2) < Jum-b(Jumble3) < Jum-p(Jumping1) < Jun(Junior5) < Jup(Jupiter4)
    },
    # ── Q50 ── Tackle<Tadpole<Tagline<Tamarind<Tasty → 2,4,5,3,1 ────────────
    # Tac(2) < Tad(4) < Tag(5) < Tam(3) < Tas(1)
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": (
            "Words: 1.Tasty 2.Tackle 3.Tamarind 4.Tadpole 5.Tagline — "
            "Which option represents the correct order of the given words "
            "as they would appear in an English dictionary? "
            "[GD Con-13 Jan 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Tasty 2.Tackle 3.Tamarind 4.Tadpole 5.Tagline — "
            "कौन सा विकल्प दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे?"
        ),
        "option_a": "4, 3, 2, 5, 1",
        "option_b": "4, 2, 1, 5, 3",
        "option_c": "2, 4, 5, 3, 1",
        "option_d": "2, 4, 3, 5, 1",
        "correct_answer": "C",
        # Tac(Tackle2) < Tad(Tadpole4) < Tag(Tagline5) < Tam(Tamarind3) < Tas(Tasty1)
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        # Use question_number-based dedup to avoid fingerprint collision issues
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
