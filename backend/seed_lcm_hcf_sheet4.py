"""
seed_lcm_hcf_sheet4.py
======================
Seeds questions 50–63 (LCM & HCF) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : LCM & HCF
Run     : python seed_lcm_hcf_sheet4.py

Answer key verification:
  Q50: LCM(16,20,35,42)=1680; x=1680×2-6=3354 (div 13✓); 3350<3354<3360            → A
  Q51: LCM(32,41,48)=3936; N=3936×2-28=7844 (div 53✓); 7834<7844<7854              → D
  Q52: LCM(3,5,8,9,10)=360s=6 min                                                   → A
  Q53: LCM(1/4,1/10,1/8)=LCM(1,1,1)/HCF(4,10,8)=1/2=0.5s                         → A
  Q54: LCM(72,108,48)=432s=7m12s; 9:30+7:12=9:37:12                                → B
  Q55: LCM(8,10,12)=120s=2min; in 30min: 30/2+1=16 times                           → C
  Q56: LCM(15,20,25,30)=300s=5min; 5:30–8:15=165min; 165/5+1=34                    → B
  Q57: Red=30s, Green=50s; LCM=150s; 3600/150=24 times/hour                        → D
  Q58: LCM(63,70,77)=6930 cm                                                        → C
  Q59: LCM(5,24,9)=360 days; 360=51×7+3; Sunday+3=Wednesday                        → B
  Q60: 111..115: only 113 is new prime >110; LCM(1..115)=113N                       → B
  Q61: 21-27 new factors: 23, 5(via 25), 3(via 27); K=23×5×3=345                   → B
  Q62: 4752=2⁴×3³×11; x=216=2³×3³ gives LCM=2⁴×3³×11=4752 ✓                      → C
  Q63: x=2^a×3³×5^b; a∈{0..4}(5), b∈{0..2}(3); total=15                           → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_LCM_HCF_Sheet4"
SUBJECT = "Quant"
TOPIC   = "LCM & HCF"

QUESTIONS = [
    # Q50 — ICAR Technician 2023
    {
        "question_number": 50,
        "difficulty": "hard",
        "question_en": "Let x be the least number which when divided by 16, 20, 35 and 42, the remainders are 10, 14, 29 and 36, respectively and x is divisible by 13. The value of x lies between: (ICAR Technician 2023)",
        "question_hi": "माना कि x वह सबसे छोटी संख्या है जिसे 16, 20, 35 और 42 से भाग देने पर क्रमशः 10, 14, 29 और 36 शेषफल बचता है, और x, 13 से विभाज्य है। x का मान निम्नलिखित में से किनके बीच स्थित होगा? (ICAR Technician 2023)",
        "option_a": "3350 and 3360",
        "option_b": "3370 and 3380",
        "option_c": "3380 and 3390",
        "option_d": "3360 and 3370",
        "correct_answer": "A",
    },
    # Q51 — RRB NTPC GRADUATE LEVEL 2025 CBT-1
    {
        "question_number": 51,
        "difficulty": "hard",
        "question_en": "Nandan had some marbles. When he distributed the marbles equally among 32 children, 4 marbles were left. Equally among 41 children, 13 marbles were left, and among 48 children, 20 marbles were left. When distributed equally among 53 children, no marble was left. The number of marbles Nandan initially had may lie between: (RRB NTPC GRADUATE LEVEL 2025 CBT-1)",
        "question_hi": "नंदन के पास कुछ कंचे थे। जब उसने कंचों को 32 बच्चों में बराबर-बराबर बाँट दिए, तो उसने पाया कि 4 कंचे शेष रह गए। यदि उसने कंचों को 41 और 48 बच्चों में बराबर-बराबर बाँटा, तो भी उसके पास क्रमशः 13 और 20 कंचे शेष बचते। लेकिन जब उसने उन्हें 53 बच्चों में बराबर-बराबर बाँटा, तो एक भी कंचा शेष नहीं बचा। नंदन के पास आरंभ में जितने कंचे थे, उनकी संख्या _____ के बीच हो सकती है। (RRB NTPC GRADUATE LEVEL 2025 CBT-1)",
        "option_a": "7814 and 7824",
        "option_b": "7794 and 7804",
        "option_c": "7864 and 7874",
        "option_d": "7834 and 7854",
        "correct_answer": "D",
    },
    # Q52
    {
        "question_number": 52,
        "difficulty": "easy",
        "question_en": "Five bells ring together at the same time at intervals of 3, 5, 8, 9 and 10 seconds. They will again ring simultaneously after:",
        "question_hi": "पाँच घंटियाँ 3, 5, 8, 9 और 10 सेकंड के अंतराल पर एक साथ बजती हैं, सभी घंटियाँ एक समय पर एक साथ बजती हैं। वे कितने समय के बाद पुनः एक साथ बजेंगी?",
        "option_a": "6 min.",
        "option_b": "8 min.",
        "option_c": "9 min.",
        "option_d": "4 min.",
        "correct_answer": "A",
    },
    # Q53 — RRB NTPC 2021
    {
        "question_number": 53,
        "difficulty": "medium",
        "question_en": "Three bells start ringing simultaneously. Each of them rings after 0.25 seconds, 0.1 seconds and 0.125 seconds. After how many seconds will they ring together again? (RRB NTPC 2021)",
        "question_hi": "तीन घंटियाँ एक साथ बजना आरंभ करती हैं। उनमें से प्रत्येक 0.25 सेकंड, 0.1 सेकंड और 0.125 सेकंड के बाद बजती हैं। कितने सेकंड बाद वे पुनः एक साथ बजेंगी? (RRB NTPC 2021)",
        "option_a": "0.5",
        "option_b": "0.1",
        "option_c": "0.2",
        "option_d": "0.6",
        "correct_answer": "A",
    },
    # Q54 — RRB NTPC 2021
    {
        "question_number": 54,
        "difficulty": "medium",
        "question_en": "The lights of three different traffic signals change every 72, 108 and 48 seconds respectively. If the lights change together at 9:30:00 am, at what time will they change together again? (RRB NTPC 2021)",
        "question_hi": "तीन अलग-अलग ट्रैफिक सिग्नलों की लाइटें क्रमशः प्रत्येक 72, 108 और 48 सेकंड के बाद बदलती हैं। यदि लाइटें सुबह 9:30 बजे एक साथ बदलती हैं, तो वे किस समय पुनः एक साथ बदलेंगी? (RRB NTPC 2021)",
        "option_a": "9:44:24 am",
        "option_b": "9:37:12 am",
        "option_c": "9:37:20 am",
        "option_d": "9:36:12 am",
        "correct_answer": "B",
    },
    # Q55
    {
        "question_number": 55,
        "difficulty": "easy",
        "question_en": "Three bells commence tolling together and toll at intervals of 8 sec, 10 sec and 12 sec respectively. In 30 min, how many times do they toll together?",
        "question_hi": "तीन घंटियाँ एक साथ बजना शुरू होती हैं और क्रमशः 8 sec, 10 sec और 12 sec के अंतराल पर बजती हैं। 30 मिन में वे कितनी बार एक साथ बजती हैं?",
        "option_a": "14",
        "option_b": "17",
        "option_c": "16",
        "option_d": "18",
        "correct_answer": "C",
    },
    # Q56 — RRB JE 2024
    {
        "question_number": 56,
        "difficulty": "medium",
        "question_en": "Four chimes ring simultaneously at 5:30 a.m. After that, they ring at the intervals of 15 seconds, 20 seconds, 25 seconds and 30 seconds, respectively. How many times do they ring together till 8:15 a.m., including at 5:30 a.m.? (RRB JE 2024)",
        "question_hi": "चार घंटियाँ 5:30 a.m. पर एक साथ बजती हैं। इसके बाद, वे क्रमशः 15 सेकंड, 20 सेकंड, 25 सेकंड और 30 सेकंड के अंतराल पर बजती हैं। 5:30 a.m. सहित 8:15 a.m. तक ये घंटियाँ कितनी बार एक साथ बजेंगी? (RRB JE 2024)",
        "option_a": "32",
        "option_b": "34",
        "option_c": "31",
        "option_d": "33",
        "correct_answer": "B",
    },
    # Q57 — RRB JE 2024
    {
        "question_number": 57,
        "difficulty": "medium",
        "question_en": "At a traffic signal, a red light flashes two times per minute and a green light flashes six times in five minutes at regular intervals. If both the lights start flashing at the same time, how many times do they flash together in each hour? (RRB JE 2024)",
        "question_hi": "एक ट्रैफिक सिग्नल पर, एक लाल बत्ती नियमित अंतराल पर प्रति मिनट दो बार चमकती है और एक हरी बत्ती पाँच मिनट में छह बार चमकती है। यदि दोनों बत्तियाँ एक ही समय पर चमकना शुरू करती हैं, तो वे प्रत्येक घंटे में एक साथ कितनी बार चमकती हैं? (RRB JE 2024)",
        "option_a": "25",
        "option_b": "28",
        "option_c": "20",
        "option_d": "24",
        "correct_answer": "D",
    },
    # Q58
    {
        "question_number": 58,
        "difficulty": "easy",
        "question_en": "Three men move from one place to another. Their steps are of length 63 cm, 70 cm and 77 cm, respectively. What is the minimum distance that all three persons can cover in a whole number of steps?",
        "question_hi": "तीन आदमी एक स्थान से दूसरे स्थान की ओर एक साथ चलते हैं। उनके कदम क्रमशः 63 सेमी, 70 सेमी और 77 सेमी के हैं। न्यूनतम कितनी दूरी तय की जानी चाहिए कि सभी उस दूरी को पूरे कदमों में तय कर सकें?",
        "option_a": "9630 cm",
        "option_b": "9360 cm",
        "option_c": "6930 cm",
        "option_d": "6950 cm",
        "correct_answer": "C",
    },
    # Q59
    {
        "question_number": 59,
        "difficulty": "easy",
        "question_en": "Joseph visits the club on every 5th day, Harsh visits on every 24th day, while Sumit visits on every 9th day. If all three of them met at the club on Sunday, then on which day will all three of them meet again?",
        "question_hi": "जोसेफ प्रत्येक 5वें दिन क्लब का दौरा करता है, हर्ष प्रत्येक 24वें दिन क्लब का दौरा करता है, जबकि सुमित प्रत्येक 9वें दिन क्लब का दौरा करता है। यदि वे तीनों रविवार को क्लब में मिले, तो वे तीनों किस दिन फिर मिलेंगे?",
        "option_a": "Monday",
        "option_b": "Wednesday",
        "option_c": "Thursday",
        "option_d": "Sunday",
        "correct_answer": "B",
    },
    # Q60
    {
        "question_number": 60,
        "difficulty": "hard",
        "question_en": "If the LCM of the first 110 natural numbers is N, then find the LCM of the first 115 natural numbers.",
        "question_hi": "यदि प्रथम 110 प्राकृत संख्याओं का लघुत्तम समापवर्त्य N है, तो प्रथम 115 प्राकृत संख्याओं का लघुत्तम समापवर्त्य ज्ञात कीजिए।",
        "option_a": "111 × 112 × 113 × 114 × 115 N",
        "option_b": "113 N",
        "option_c": "115 N",
        "option_d": "111 × 113 N",
        "correct_answer": "B",
    },
    # Q61
    {
        "question_number": 61,
        "difficulty": "hard",
        "question_en": "If LCM(1, 2, 3, 4, …, 20) = x and LCM(1, 2, 3, 4, …, 27) = K × x, then find the value of K.",
        "question_hi": "यदि LCM (1, 2, 3, 4 ... 20) = x और LCM (1, 2, 3, 4 ... 27) = K×x, तो K का मान ज्ञात कीजिए।",
        "option_a": "3289",
        "option_b": "345",
        "option_c": "429",
        "option_d": "115",
        "correct_answer": "B",
    },
    # Q62
    {
        "question_number": 62,
        "difficulty": "hard",
        "question_en": "The LCM of 48, 88 and another number x is 4752. Which of the following can be the value of x?",
        "question_hi": "48, 88 और एक अन्य संख्या x का लघुत्तम समापवर्त्य (LCM) 4752 है। x का मान ज्ञात कीजिए।",
        "option_a": "202",
        "option_b": "307",
        "option_c": "216",
        "option_d": "123",
        "correct_answer": "C",
    },
    # Q63
    {
        "question_number": 63,
        "difficulty": "hard",
        "question_en": "LCM of three natural numbers 150, 144 and x is 10800. How many values of x are possible?",
        "question_hi": "तीन प्राकृतिक संख्याओं 150, 144 और x का LCM 10800 है। x के कितने मान संभव हैं?",
        "option_a": "10",
        "option_b": "16",
        "option_c": "12",
        "option_d": "15",
        "correct_answer": "D",
    },
]


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
            if d["question_en"][:80] in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = SOURCE,
                **d,
            ))
            inserted += 1

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
