"""
seed_reasoning_word_based_sheet1.py
=========================================
Seeds Word-Based (Analogy) Q1-Q29 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Word-Based
Run     : python seed_reasoning_word_based_sheet1.py

Direction: In each question select the related word from the given alternatives.

Answer key (verified against published key + logic):
  Q1   Genuine:Authentic (synonyms) → Mirage:Illusion               → A
  Q2   Thunder:Rain (precedes) → ?:Night → Dusk precedes Night       → B
  Q3   Botany:Plants (study of) → Entomology:Insects                 → C
  Q4   Parliament:Great Britain → Congress:USA                       → C
  Q5   Architect:Building (creates) → Sculptor:Statue                → D
  Q6   Ice:Coldness (property of) → Earth:Gravitation                → B
  Q7   Anaemia:Blood (disorder of) → Anarchy:Government              → C
  Q8   Paddy:Field (produced in) → Steel:Factory                     → B
  Q9   Laugh:Joke (caused by) → Explode:Cracker                      → D
  Q10  President:India → King:England                                 → A
  Q11  Ecstasy:Gloom (antonyms) → Humiliation:Exaltation             → D
  Q12  Country:President → State:Governor (India)                     → D
  Q13  Mirage:Desert (optical illusion in) → Rainbow:Sky             → B
  Q14  Lock:Key (opened by) → Crime:Investigation                    → A
  Q15  Radio:Listener → Film:Audience                                → D
  Q16  Book:Library → Animal:Zoo                                      → D
  Q17  Elbow:Wrist (arm joints) → Knee:Ankle (leg joints)            → C
  Q18  Scribble:Write (imperfect form) → Stammer:Speak               → C
  Q19  MINE:I (possessive:nominative) → HIS:HE                       → C
  Q20  Immigration:Arrival → Emigration:Leaving                      → A
  Q21  Blind:Visual (lacks) → Deaf:Auditory                          → C
  Q22  Monotony:Variety (opposites) → Crudeness:Refinement           → D
  Q23  Rat:Cat (prey:predator) → Worm:Bird                           → B
  Q24  Goldsmith:Gold (works with) → Carpenter:Wood                  → A
  Q25  Druggist:Pharmacy (professional:reference) →                    → B
       Librarian:Catalogue
  Q26  Poet:Poem (creates) → Dramatist:Play                          → C
  Q27  Handsome:Beautiful::Man:Woman (gender pair)                    → C
  Q28  Mechanic:Spanner (uses tool) → Carpenter:Saw                  → D
  Q29  Volcano:Lava (produces/emits) → Fire:Ashes                    → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Word_Based_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Word-Based"

QUESTIONS = [
    # ── Q1 ── Genuine:Authentic (synonyms) → Mirage:Illusion ─────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "Genuine : Authentic :: Mirage : ?",
        "question_hi": "वास्तविक : प्रामाणिक :: मृगतृष्णा : ?",
        "option_a": "Illusion/भ्रम",
        "option_b": "Image/छवि",
        "option_c": "Hideout/छुपने की जगह",
        "option_d": "Reflection/प्रतिबिम्ब",
        "correct_answer": "A",
    },
    # ── Q2 ── Thunder precedes Rain; Dusk precedes Night ─────────────────────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "Thunder : Rain :: ? : Night",
        "question_hi": "गड़गड़ाहट : बारिश :: ? : रात",
        "option_a": "Day/दिन",
        "option_b": "Dusk/सन्ध्या",
        "option_c": "Dark/अँधेरा",
        "option_d": "Evening/शाम",
        "correct_answer": "B",
    },
    # ── Q3 ── Botany=study of Plants; Entomology=study of Insects ─────────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "Botany : Plants :: Entomology : ?",
        "question_hi": "वनस्पति विज्ञान : पौधे :: कीट विज्ञान : ?",
        "option_a": "Birds/पक्षी",
        "option_b": "Plants/पौधे",
        "option_c": "Insects/कीड़े",
        "option_d": "Snakes/साँप",
        "correct_answer": "C",
    },
    # ── Q4 ── Parliament=legislature of Great Britain; Congress=of USA ─────────
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "Parliament : Great Britain :: Congress : ?",
        "question_hi": "संसद : ग्रेट ब्रिटेन :: कांग्रेस : ?",
        "option_a": "Japan/जापान",
        "option_b": "India/भारत",
        "option_c": "USA/अमेरिका",
        "option_d": "Netherlands/नीदरलैंड",
        "correct_answer": "C",
    },
    # ── Q5 ── Architect creates Building; Sculptor creates Statue ─────────────
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": "Architect : Building :: Sculptor : ?",
        "question_hi": "वास्तुकार : इमारत :: मूर्तिकार : ?",
        "option_a": "Museum/संग्रहालय",
        "option_b": "Stone/पत्थर",
        "option_c": "Chisel/छेनी",
        "option_d": "Statue/मूर्ति",
        "correct_answer": "D",
    },
    # ── Q6 ── Ice→Coldness (property); Earth→Gravitation ─────────────────────
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": "Ice : Coldness :: Earth : ?",
        "question_hi": "बर्फ : ठण्डक :: पृथ्वी : ?",
        "option_a": "Weight/भार",
        "option_b": "Gravitation/गुरुत्वाकर्षण",
        "option_c": "Jungle/जंगल",
        "option_d": "Sea/समुद्र",
        "correct_answer": "B",
    },
    # ── Q7 ── Anaemia=disorder of Blood; Anarchy=disorder of Government ───────
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": "Anaemia : Blood :: Anarchy : ?",
        "question_hi": "रक्तहीनता : रक्त :: अराजकता : ?",
        "option_a": "Disorder/अव्यवस्था",
        "option_b": "Monarchy/राजतंत्र",
        "option_c": "Government/सरकार",
        "option_d": "Lawlessness/अराजकता",
        "correct_answer": "C",
    },
    # ── Q8 ── Paddy grown in Field; Steel produced in Factory ─────────────────
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": "Paddy : Field :: Steel : ?",
        "question_hi": "धान : खेत :: इस्पात : ?",
        "option_a": "Iron/लोहा",
        "option_b": "Factory/कारखाना",
        "option_c": "Ore/अयस्क",
        "option_d": "Mine/खान",
        "correct_answer": "B",
    },
    # ── Q9 ── Laugh caused by Joke; Explode caused by Cracker ─────────────────
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": "Laugh : Joke :: ? : Cracker",
        "question_hi": "हँसना : मजाक :: ? : पटाखा",
        "option_a": "Fear/डर",
        "option_b": "Anger/क्रोध",
        "option_c": "Fireball/आग का गोला",
        "option_d": "Explode/फटना",
        "correct_answer": "D",
    },
    # ── Q10 ── President heads India; King heads England ──────────────────────
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": "President : India :: King : ?",
        "question_hi": "राष्ट्रपति : भारत :: राजा : ?",
        "option_a": "England/इंग्लैंड",
        "option_b": "China/चीन",
        "option_c": "Jordan/जॉर्डन",
        "option_d": "France/फ्रांस",
        "correct_answer": "A",
    },
    # ── Q11 ── Ecstasy:Gloom (antonyms) → Humiliation:Exaltation ─────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": "Ecstasy : Gloom :: ? : ?",
        "question_hi": "परमानन्द : उदासी :: ? : ?",
        "option_a": "Congratulations : Occasion/बधाई : अवसर",
        "option_b": "Diligent : Successful/परिश्रमी : सफल",
        "option_c": "Measure : Scale/माप : पैमाना",
        "option_d": "Humiliation : Exaltation/अपमान : उत्थान",
        "correct_answer": "D",   # antonym pair: Ecstasy↔Gloom = Humiliation↔Exaltation
    },
    # ── Q12 ── Country head=President; State head=Governor (India) ───────────
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": "Country : President :: State : ?",
        "question_hi": "देश : राष्ट्रपति :: राज्य : ?",
        "option_a": "Chief Minister/मुख्यमंत्री",
        "option_b": "Prime Minister/प्रधानमंत्री",
        "option_c": "Speaker/अध्यक्ष",
        "option_d": "Governor/राज्यपाल",
        "correct_answer": "D",
    },
    # ── Q13 ── Mirage=optical illusion in Desert; Rainbow=optical illusion in Sky
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": "Mirage : Desert :: ? : ?",
        "question_hi": "मृगतृष्णा : रेगिस्तान :: ? : ?",
        "option_a": "Sky : Illusion/आकाश : भ्रम",
        "option_b": "Rainbow : Sky/इन्द्रधनुष : आकाश",
        "option_c": "Rain : Rainbow/बारिश : इन्द्रधनुष",
        "option_d": "Image : Mirror/छवि : दर्पण",
        "correct_answer": "B",
    },
    # ── Q14 ── Lock opened by Key; Crime solved by Investigation ─────────────
    {
        "question_number": 14,
        "difficulty": "easy",
        "question_en": "Lock : Key :: Crime : ?",
        "question_hi": "ताला : चाबी :: अपराध : ?",
        "option_a": "Investigation/जाँच",
        "option_b": "Mystery/रहस्य",
        "option_c": "Criminal/अपराधी",
        "option_d": "Conviction/दोषसिद्धि",
        "correct_answer": "A",
    },
    # ── Q15 ── Radio's audience=Listener; Film's audience=Audience ───────────
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": "Radio : Listener :: Film : ?",
        "question_hi": "रेडियो : श्रोता :: फिल्म : ?",
        "option_a": "Transmission/प्रसारण",
        "option_b": "Criticism/आलोचना",
        "option_c": "Hero/नायक",
        "option_d": "Audience/दर्शक",
        "correct_answer": "D",
    },
    # ── Q16 ── Book kept in Library; Animal kept in Zoo ───────────────────────
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": "Book : Library :: Animal : ?",
        "question_hi": "पुस्तक : पुस्तकालय :: जानवर : ?",
        "option_a": "Domestic/घरेलू",
        "option_b": "Hunter/शिकारी",
        "option_c": "Wild/जंगली",
        "option_d": "Zoo/चिड़ियाघर",
        "correct_answer": "D",
    },
    # ── Q17 ── Elbow & Wrist are arm joints; Knee & Ankle are leg joints ──────
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": "Elbow : Wrist :: Knee : ?",
        "question_hi": "कोहनी : कलाई :: घुटना : ?",
        "option_a": "Fingers/उँगलियाँ",
        "option_b": "Feet/पैर",
        "option_c": "Ankle/टखना",
        "option_d": "Thigh/जाँघ",
        "correct_answer": "C",
    },
    # ── Q18 ── Scribble=imperfect writing; Stammer=imperfect speaking ─────────
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": "Scribble : Write :: Stammer : ?",
        "question_hi": "घसीटना : लिखना :: हकलाना : ?",
        "option_a": "Walk/चलना",
        "option_b": "Play/खेलना",
        "option_c": "Speak/बोलना",
        "option_d": "Dance/नाचना",
        "correct_answer": "C",   # Stammer is imperfect form of Speaking
    },
    # ── Q19 ── MINE=possessive of I; HIS=possessive of HE ────────────────────
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": "MINE : I :: ? : ?",
        "question_hi": "MINE : I :: ? : ?",
        "option_a": "OURS and US",
        "option_b": "SHE and HERS",
        "option_c": "HIS and HE",
        "option_d": "THEIRS and THEM",
        "correct_answer": "C",   # MINE:I (possessive:nominative) = HIS:HE
    },
    # ── Q20 ── Immigration=Arrival; Emigration=Leaving ───────────────────────
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": "Immigration : Arrival :: Emigration : ?",
        "question_hi": "आव्रजन : आगमन :: उत्प्रवास : ?",
        "option_a": "Leaving/प्रस्थान",
        "option_b": "Alien/विदेशी",
        "option_c": "Native/स्थानीय",
        "option_d": "Emigrant/प्रवासी",
        "correct_answer": "A",
    },
    # ── Q21 ── Blind lacks Visual; Deaf lacks Auditory ───────────────────────
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": "Blind : Visual :: Deaf : ?",
        "question_hi": "अंधा : दृश्य :: बहरा : ?",
        "option_a": "Hearing/सुनना",
        "option_b": "Listening/सुनाई देना",
        "option_c": "Auditory/श्रवण",
        "option_d": "Sound/ध्वनि",
        "correct_answer": "C",
    },
    # ── Q22 ── Monotony↔Variety (opposites); Crudeness↔Refinement ───────────
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": "Monotony : Variety :: Crudeness : ?",
        "question_hi": "एकरसता : विविधता :: असभ्यता : ?",
        "option_a": "Sobriety/संयम",
        "option_b": "Simplicity/सरलता",
        "option_c": "Raw/कच्चा",
        "option_d": "Refinement/परिष्कार",
        "correct_answer": "D",
    },
    # ── Q23 ── Rat=prey of Cat; Worm=prey of Bird ────────────────────────────
    {
        "question_number": 23,
        "difficulty": "easy",
        "question_en": "Rat : Cat :: Worm : ?",
        "question_hi": "चूहा : बिल्ली :: कीड़ा : ?",
        "option_a": "Silk/रेशम",
        "option_b": "Bird/पक्षी",
        "option_c": "Earth/पृथ्वी",
        "option_d": "Fishing/मछली पकड़ना",
        "correct_answer": "B",
    },
    # ── Q24 ── Goldsmith works with Gold; Carpenter works with Wood ───────────
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": "Goldsmith : Gold :: ? : ?",
        "question_hi": "सुनार : सोना :: ? : ?",
        "option_a": "Carpenter : Wood/बढ़ई : लकड़ी",
        "option_b": "Cobbler : Shoes/मोची : जूते",
        "option_c": "Jeweller : Jewellery/जौहरी : जेवर",
        "option_d": "Barber : Shave/नाई : हजामत",
        "correct_answer": "A",
    },
    # ── Q25 ── Druggist uses Pharmacy (professional:reference); Librarian:Catalogue
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": "Druggist : Pharmacy :: ? : ?",
        "question_hi": "दवाविक्रेता : औषधालय :: ? : ?",
        "option_a": "Chef : Restaurant/रसोइया : रेस्तराँ",
        "option_b": "Librarian : Catalogue/पुस्तकालयाध्यक्ष : सूची",
        "option_c": "Carpenter : Wood/बढ़ई : लकड़ी",
        "option_d": "Physician : Patient/चिकित्सक : रोगी",
        "correct_answer": "B",
    },
    # ── Q26 ── Poet creates Poem; Dramatist creates Play ─────────────────────
    {
        "question_number": 26,
        "difficulty": "easy",
        "question_en": "Poet : Poem :: Dramatist : ?",
        "question_hi": "कवि : कविता :: नाटककार : ?",
        "option_a": "Dialogue/संवाद",
        "option_b": "Stage/मंच",
        "option_c": "Play/नाटक",
        "option_d": "Direction/निर्देशन",
        "correct_answer": "C",
    },
    # ── Q27 ── Handsome:Beautiful (gender pair); Man:Woman ───────────────────
    {
        "question_number": 27,
        "difficulty": "easy",
        "question_en": "Handsome : Beautiful :: Man : ?",
        "question_hi": "सुन्दर (पु.) : सुन्दर (स्त्री.) :: पुरुष : ?",
        "option_a": "Charming/आकर्षक",
        "option_b": "Man/पुरुष",
        "option_c": "Woman/महिला",
        "option_d": "She/वह (स्त्री.)",
        "correct_answer": "C",
    },
    # ── Q28 ── Mechanic uses Spanner; Carpenter uses Saw ─────────────────────
    {
        "question_number": 28,
        "difficulty": "easy",
        "question_en": "Mechanic : Spanner :: Carpenter : ?",
        "question_hi": "मिस्त्री : पाना :: बढ़ई : ?",
        "option_a": "Tree/पेड़",
        "option_b": "Wood/लकड़ी",
        "option_c": "Furniture/फर्नीचर",
        "option_d": "Saw/आरी",
        "correct_answer": "D",
    },
    # ── Q29 ── Volcano produces Lava; Fire produces Ashes ────────────────────
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": "Volcano : Lava :: Fire : ?",
        "question_hi": "ज्वालामुखी : लावा :: आग : ?",
        "option_a": "Heat/गर्मी",
        "option_b": "Light/रोशनी",
        "option_c": "Smoke/धुआँ",
        "option_d": "Ashes/राख",
        "correct_answer": "D",
    },
]

# Fix map for any pre-existing records (ans=None) skipped by deduplication
_FIXES = {
    q["question_number"]: (q["correct_answer"], {
        "option_a": q["option_a"],
        "option_b": q["option_b"],
        "option_c": q["option_c"],
        "option_d": q["option_d"],
    })
    for q in QUESTIONS
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
                print(f"  UPDATE Q{qnum}: correct_answer={ans}")

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
