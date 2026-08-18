"""
seed_reasoning_alphabet_sheet1.py
=========================================
Seeds Alphabet / Dictionary-Order Q1-Q13 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet1.py

Types of questions:
  - Alphabetical / Dictionary ordering of words  (Q1,Q2,Q5,Q7,Q8,Q9,Q12,Q13)
  - Word formation from given letters of a word  (Q3,Q4)
  - Alphabet letter-series distance               (Q6)
  - Which word comes at Nth position              (Q10,Q11)

Answer key:
  Q1  → (a) 4, 3, 1, 2, 5    [CPO-27 Jun 2024 Shift 1]
  Q2  → (d) 2, 3, 1, 4, 5    [GD Con-29 Feb 2024 Shift 4]
  Q3  → (a) None              [CHSL Tier II-10 Jan 2024 Shift 1]
  Q4  → (c) Two               [CHSL Tier II-10 Jan 2024 Shift 1]
  Q5  → (d) 4, 1, 3, 2, 5    [CPO-27 Jun 2024 Shift 2]
  Q6  → (d) 8                 [CHSL-2 July 2024 Shift 4]
  Q7  → (a) 4, 1, 2, 5, 3    [GD Con-29 Feb 2024 Shift 1]
  Q8  → (b) 2, 1, 4, 3, 5    [GD Con-29 Feb 2024 Shift 2]
  Q9  → (b) 5, 4, 1, 2, 3    [GD Con-29 Feb 2024 Shift 3]
  Q10 → (d) Smart             [GD Con-20 Feb 2024 Shift 4]
  Q11 → (b) Privilege         [GD Con-21 Feb 2024 Shift 1]
  Q12 → (b) 51423             [GD Con-20 Feb 2024 Shift 2]
  Q13 → (a) 4, 3, 2, 1, 5    [GD Con — exact letter inferred from solution]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q1 ── Dictionary order: Literacy, Literature, Litany, Listen, Lithograph ─
    # Listen < Litany < Literacy < Literature < Lithograph → 4,3,1,2,5
    {
        "question_number": 1,
        "difficulty": "medium",
        "question_en": (
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "1. Literacy  2. Literature  3. Litany  4. Listen  5. Lithograph"
        ),
        "question_hi": (
            "उस विकल्प का चयन करें जो दिए गए शब्दों की अंग्रेजी शब्दकोश में उनके क्रम में "
            "सही व्यवस्था को इंगित करता है। "
            "1. Literacy  2. Literature  3. Litany  4. Listen  5. Lithograph"
        ),
        "option_a": "4, 3, 1, 2, 5",
        "option_b": "3, 4, 1, 2, 5",
        "option_c": "4, 3, 2, 1, 5",
        "option_d": "3, 4, 2, 1, 5",
        "correct_answer": "A",
        # Listen(Lis) < Litany(Lita) < Literacy(Litere) < Literature(Literat) < Lithograph(Lith) → 4,3,1,2,5
    },
    # ── Q2 ── Alphabetical order: PARALLEL, PARADISE, PARAGRAPH, PARALLELISM, PARASITE ─
    # PARADISE < PARAGRAPH < PARALLEL < PARALLELISM < PARASITE → 2,3,1,4,5
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "Arrange the given words in alphabetical order. "
            "1. PARALLEL  2. PARADISE  3. PARAGRAPH  4. PARALLELISM  5. PARASITE"
        ),
        "question_hi": (
            "दिए गए शब्दों को वर्णमाला क्रम में व्यवस्थित करें। "
            "1. PARALLEL  2. PARADISE  3. PARAGRAPH  4. PARALLELISM  5. PARASITE"
        ),
        "option_a": "3, 1, 4, 2, 5",
        "option_b": "2, 1, 4, 3, 5",
        "option_c": "2, 3, 4, 5, 1",
        "option_d": "2, 3, 1, 4, 5",
        "correct_answer": "D",
        # 5th letter: PARADISE(D) < PARAGRAPH(G) < PARALLEL(L)< PARALLELISM(L+more) < PARASITE(S)
    },
    # ── Q3 ── Word formation from TOURIST (2nd,3rd,5th,7th) = O,U,I,T ─────────
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": (
            "How many meaningful four-letter English words can be formed using the second, "
            "third, fifth and seventh letters of the word TOURIST (counted from left to right) "
            "using each letter only once in each word?"
        ),
        "question_hi": (
            "शब्द TOURIST के दूसरे, तीसरे, पाँचवें और सातवें अक्षरों का उपयोग करके (बाएं से दाएं गिनने पर) "
            "प्रत्येक शब्द में प्रत्येक अक्षर का केवल एक बार उपयोग करते हुए कितने सार्थक "
            "चार-अक्षरी अंग्रेजी शब्द बनाए जा सकते हैं?"
        ),
        "option_a": "None/कोई नहीं",
        "option_b": "Two/दो",
        "option_c": "One/एक",
        "option_d": "More than two/दो से अधिक",
        "correct_answer": "A",
        # T-O-U-R-I-S-T: 2nd=O,3rd=U,5th=I,7th=T → OUIT,OITU,OUIT... no meaningful word
    },
    # ── Q4 ── Word formation from SAVOUR (1st,4th,5th,6th) = S,O,U,R ──────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "How many meaningful four-letter English words can be formed using the first, "
            "fourth, fifth and sixth letters of the word SAVOUR (counted from left to right) "
            "using each letter only once in each word?"
        ),
        "question_hi": (
            "शब्द SAVOUR के पहले, चौथे, पाँचवें और छठे अक्षरों का उपयोग करके (बाएं से दाएं गिनने पर) "
            "प्रत्येक शब्द में प्रत्येक अक्षर का केवल एक बार उपयोग करते हुए कितने सार्थक "
            "चार-अक्षरी अंग्रेजी शब्द बनाए जा सकते हैं?"
        ),
        "option_a": "One/एक",
        "option_b": "More than two/दो से अधिक",
        "option_c": "Two/दो",
        "option_d": "None/कोई नहीं",
        "correct_answer": "C",
        # S-A-V-O-U-R: 1st=S,4th=O,5th=U,6th=R → SOUR ✓, OURS ✓ → Two words
    },
    # ── Q5 ── Dictionary order: Elate, Election, Elbow, Elastic, Electoral ──────
    # Elastic < Elate < Elbow < Election < Electoral → 4,1,3,2,5
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "1. Elate  2. Election  3. Elbow  4. Elastic  5. Electoral"
        ),
        "question_hi": (
            "उस विकल्प का चयन करें जो दिए गए शब्दों की उस क्रम में सही व्यवस्था दर्शाता है "
            "जिस क्रम में वे अंग्रेजी शब्दकोश में दिखाई देते हैं। "
            "1. Elate  2. Election  3. Elbow  4. Elastic  5. Electoral"
        ),
        "option_a": "1, 3, 4, 2, 5",
        "option_b": "4, 3, 2, 1, 5",
        "option_c": "1, 4, 5, 2, 3",
        "option_d": "4, 1, 3, 2, 5",
        "correct_answer": "D",
        # Ela-s(Elastic) < Ela-t(Elate) < Elb(Elbow) < Ele-c-t-i(Election) < Ele-c-t-o(Electoral)
    },
    # ── Q6 ── FRAMED alphabetically: A,D,E,F,M,R — 2nd from left=D, 2nd from right=M ─
    # Letters between D(4th) and M(13th) in alphabet: E,F,G,H,I,J,K,L = 8
    {
        "question_number": 6,
        "difficulty": "hard",
        "question_en": (
            "Each of the letters in the word FRAMED is arranged in alphabetical order. "
            "How many letters are there in the English alphabetical series between the letter "
            "which is second from the left and the one which is second from the right "
            "in the new letter cluster thus formed?"
        ),
        "question_hi": (
            "शब्द FRAMED में प्रत्येक अक्षर को वर्णमाला क्रम में व्यवस्थित किया गया है। "
            "इस प्रकार बने नए अक्षर समूह में बाएं से दूसरे अक्षर और दाएं से दूसरे अक्षर के बीच "
            "अंग्रेजी वर्णमाला श्रृंखला में कितने अक्षर हैं?"
        ),
        "option_a": "7",
        "option_b": "6",
        "option_c": "9",
        "option_d": "8",
        "correct_answer": "D",
        # FRAMED → A,D,E,F,M,R; 2nd from left=D(4th), 2nd from right=M(13th); between: 13-4-1=8
    },
    # ── Q7 ── Alphabetical order: MYSTERY,MYSTICAL,MYTHOLOGY,MYSTERIOUS,MYTHICAL ─
    # MYSTERIOUS < MYSTERY < MYSTICAL < MYTHICAL < MYTHOLOGY → 4,1,2,5,3
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": (
            "Arrange the given words in alphabetical order. "
            "1. MYSTERY  2. MYSTICAL  3. MYTHOLOGY  4. MYSTERIOUS  5. MYTHICAL"
        ),
        "question_hi": (
            "दिए गए शब्दों को वर्णमाला क्रम में व्यवस्थित कीजिए। "
            "1. MYSTERY  2. MYSTICAL  3. MYTHOLOGY  4. MYSTERIOUS  5. MYTHICAL"
        ),
        "option_a": "4, 1, 2, 5, 3",
        "option_b": "4, 2, 5, 3, 1",
        "option_c": "4, 1, 5, 3, 2",
        "option_d": "4, 1, 2, 3, 5",
        "correct_answer": "A",
        # MYS-T-E-R-I(MYSTERIOUS) < MYS-T-E-R-Y(MYSTERY) < MYS-T-I(MYSTICAL) < MYT-H-I(MYTHICAL) < MYT-H-O(MYTHOLOGY)
    },
    # ── Q8 ── Dictionary order: Lid, Lick, Lien, Lie, Lieu ──────────────────────
    # Lick < Lid < Lie < Lien < Lieu → 2,1,4,3,5
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "Arrange the given words in the sequence in which they occur in the dictionary. "
            "1. Lid  2. Lick  3. Lien  4. Lie  5. Lieu"
        ),
        "question_hi": (
            "दिए गए शब्दों को उस क्रम में व्यवस्थित कीजिए जिसमें वे शब्दकोश में आते हैं। "
            "1. Lid  2. Lick  3. Lien  4. Lie  5. Lieu"
        ),
        "option_a": "2, 4, 1, 3, 5",
        "option_b": "2, 1, 4, 3, 5",
        "option_c": "1, 2, 3, 4, 5",
        "option_d": "1, 2, 4, 3, 5",
        "correct_answer": "B",
        # Lic(Lick) < Lid < Lie < Lie-n(Lien) < Lie-u(Lieu) → 2,1,4,3,5
    },
    # ── Q9 ── Dictionary order: Liberal, Libra, Library, Libel, Liability ────────
    # Liability < Libel < Liberal < Libra < Library → 5,4,1,2,3
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": (
            "Arrange the given words in the sequence in which they occur in the dictionary. "
            "1. Liberal  2. Libra  3. Library  4. Libel  5. Liability"
        ),
        "question_hi": (
            "विषाप शब्दों को उस क्रम में व्यवस्थित कीजिए जिसमें वे शब्दकोश में आते हैं। "
            "1. Liberal  2. Libra  3. Library  4. Libel  5. Liability"
        ),
        "option_a": "4, 5, 2, 1, 3",
        "option_b": "5, 4, 1, 2, 3",
        "option_c": "4, 5, 1, 2, 3",
        "option_d": "5, 4, 1, 3, 2",
        "correct_answer": "B",
        # Lia(Liability) < Lib-e-l(Libel) < Lib-e-r(Liberal) < Lib-r-a(Libra) < Lib-r-a-r(Library)
    },
    # ── Q10 ── 3rd word in dictionary order: Small,Smart,Smack,Smash,Smatter ────
    # Smack < Small < Smart < Smash < Smatter → 3rd = Smart
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": (
            "After arranging the given words according to dictionary order, "
            "which word will come at the third position? "
            "1. Small  2. Smart  3. Smack  4. Smash  5. Smatter"
        ),
        "question_hi": (
            "दिए गए शब्दों को शब्दकोश क्रम के अनुसार व्यवस्थित करने के बाद कौन सा शब्द "
            "तीसरे स्थान पर आएगा? "
            "1. Small  2. Smart  3. Smack  4. Smash  5. Smatter"
        ),
        "option_a": "Small",
        "option_b": "Smack",
        "option_c": "Smash",
        "option_d": "Smart",
        "correct_answer": "D",
        # Smack(Sma-c) < Small(Sma-l) < Smart(Sma-r) ← 3rd < Smash(Sma-s) < Smatter(Sma-t)
    },
    # ── Q11 ── 4th word in dictionary order: Private,Prison,Privacy,Privy,Privilege ─
    # Prison < Privacy < Private < Privilege < Privy → 4th = Privilege
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": (
            "After arranging the given words according to dictionary order, "
            "which word will come at the fourth position? "
            "1. Private  2. Prison  3. Privacy  4. Privy  5. Privilege"
        ),
        "question_hi": (
            "दिए गए शब्दों को शब्दकोश क्रम के अनुसार व्यवस्थित करने पर कौन सा शब्द चौथे स्थान पर आएगा? "
            "1. Private  2. Prison  3. Privacy  4. Privy  5. Privilege"
        ),
        "option_a": "Prison",
        "option_b": "Privilege",
        "option_c": "Privacy",
        "option_d": "Privy",
        "correct_answer": "B",
        # Pris-o(Prison) < Priv-a-c(Privacy) < Priv-a-t(Private) < Priv-i-l(Privilege) < Priv-y(Privy)
    },
    # ── Q12 ── Dictionary order: Let, Lethargy, Letter, Lethal, Lest ────────────
    # Lest < Let < Lethal < Lethargy < Letter → 5,1,4,2,3
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": (
            "Arrange the given words in the sequence in which they occur in the dictionary. "
            "1. Let  2. Lethargy  3. Letter  4. Lethal  5. Lest"
        ),
        "question_hi": (
            "दिए गए शब्दों को उस क्रम में व्यवस्थित कीजिए जिसमें वे शब्दकोश में आते हैं। "
            "1. Let  2. Lethargy  3. Letter  4. Lethal  5. Lest"
        ),
        "option_a": "15324",
        "option_b": "51423",
        "option_c": "15234",
        "option_d": "51243",
        "correct_answer": "B",
        # Les(Lest) < Let < Let-h-a-l(Lethal) < Let-h-a-r(Lethargy) < Let-t(Letter) → 5,1,4,2,3
    },
    # ── Q13 ── Dictionary order: Dear, Dean, Deal, Dead, Death ──────────────────
    # Dead < Deal < Dean < Dear < Death → 4,3,2,1,5
    {
        "question_number": 13,
        "difficulty": "easy",
        "question_en": (
            "Arrange the given words in the sequence in which they occur in the dictionary. "
            "1. Dear  2. Dean  3. Deal  4. Dead  5. Death"
        ),
        "question_hi": (
            "दिए गए शब्दों को उस क्रम में व्यवस्थित कीजिए जिसमें वे शब्दकोश में आते हैं। "
            "1. Dear  2. Dean  3. Deal  4. Dead  5. Death"
        ),
        "option_a": "4, 3, 2, 1, 5",
        "option_b": "4, 3, 1, 2, 5",
        "option_c": "3, 4, 2, 1, 5",
        "option_d": "4, 2, 3, 1, 5",
        "correct_answer": "A",
        # Dea-d(Dead) < Dea-l(Deal) < Dea-n(Dean) < Dea-r(Dear) < Dea-t(Death) → 4,3,2,1,5
    },
]

# Fix map for pre-existing records (ans=None)
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
