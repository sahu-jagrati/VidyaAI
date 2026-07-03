"""
seed_reasoning_series_sheet1.py
=================================
Seeds questions 1–11 (Series) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Series
Run     : python seed_reasoning_series_sheet1.py

Answer key verification:
  Q1:  jklmno repeating; blanks k,l,n,o → klno                                 → D
  Q2:  ×2+2 each step: 158×2+2=318                                              → D
  Q3:  1st+6: F,L,R,X,D; 2nd+7: N,U,B,I,P; 3rd-17: V,E,N,W,F → RBN           → D
  Q4:  CJS→DKT→ELU each letter +1 → FMV                                         → D
  Q5:  diff=+2³,-3³,+4³,-5³,+6³ → 62+216=278                                   → C
  Q6:  each letter -1: NRT→MQS→LPR→KOQ→JNP                                     → C
  Q7:  blanks fill repeating "mnpqrrqpnm" pattern → mqqnnrpmqp                  → A
  Q8:  groups _NE_ with 1st+last +5 each; blanks N,K,M,E,Z → NKMEZ             → C
  Q9:  GA_B... 1st+6, 2nd=A, 3rd+6, 4th=B; blanks J,A,V,B,E → JAVBE           → B
  Q10: All 4 columns each -7 mod 26; blanks Z,U,O,E,Z → ZUOEZ                  → D
  Q11: Groups step -7,-5,-3,-1,+1; MJG fits 3rd group (step -3, start M=13)    → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Reasoning_Series_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Series"

QUESTIONS = [
    # Q1
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "Which of the following groups of letters when sequentially placed from left to right will complete the given series? jklmnojklmnoj_lmnojk_m_ojklmn_",
        "question_hi": "निम्नलिखित में से अक्षरों का कौन सा समूह बाएं से दाएं क्रमवार रखने पर दी गई श्रृंखला को पूरा करेगा? jklmnojklmnoj_lmnojk_m_ojklmn_",
        "option_a": "jklm",
        "option_b": "mnol",
        "option_c": "knlo",
        "option_d": "klno",
        "correct_answer": "D",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q2
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 8, 18, 38, 78, 158, ? [GD Con - 20 Feb 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 8, 18, 38, 78, 158, ?",
        "option_a": "290",
        "option_b": "340",
        "option_c": "278",
        "option_d": "318",
        "correct_answer": "D",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q3
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": "What should come in place of '?' in the given series based on the English alphabetical order? FNV, LUE, ?, XIW, DPF [CHSL - 1 July 2024 - Shift 1]",
        "question_hi": "अंग्रेजी वर्णमाला क्रम के आधार पर दी गई श्रृंखला में '?' के स्थान पर क्या आना चाहिए? FNV, LUE, ?, XIW, DPF",
        "option_a": "GOZ",
        "option_b": "UWZ",
        "option_c": "HRY",
        "option_d": "RBN",
        "correct_answer": "D",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q4
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "Which of the following terms will replace the question mark (?) in the given series? CJS, DKT, ELU, ? [CPO - 27 Jun 2024 - Shift 3]",
        "question_hi": "निम्नलिखित में से कौन-सा पद दी गई श्रृंखला में प्रश्नवाचक चिह्न (?) को प्रतिस्थापित करेगा? CJS, DKT, ELU, ?",
        "option_a": "DLO",
        "option_b": "DHB",
        "option_c": "DRT",
        "option_d": "FMV",
        "correct_answer": "D",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "Select the missing number from the given series. 142, 150, 123, 187, 62, ? [GD Con - 20 Feb 2024 - Shift 1]",
        "question_hi": "दी गई श्रृंखला में से लुप्त संख्या का चयन कीजिए। 142, 150, 123, 187, 62, ?",
        "option_a": "281",
        "option_b": "285",
        "option_c": "278",
        "option_d": "300",
        "correct_answer": "C",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": "A series is given with one term missing. Select the correct alternative. NRT, MQS, LPR, KOQ, ? [GD Con - 20 Feb 2024 - Shift 2]",
        "question_hi": "एक श्रृंखला दी गई है, जिसमें एक पद लुप्त है। दिए गए विकल्पों में से वह सही विकल्प चुनिए जो श्रृंखला को पूरा करेगा। NRT, MQS, LPR, KOQ, ?",
        "option_a": "KLR",
        "option_b": "MNP",
        "option_c": "JNP",
        "option_d": "JKL",
        "correct_answer": "C",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q7
    {
        "question_number": 7,
        "difficulty": "hard",
        "question_en": "Select the combination of letters that when sequentially placed in the blanks will complete the series. _np_rr_p_mm_pq_rq_nm_np_rq_nm [CHSL - 1 July 2024 - Shift 4]",
        "question_hi": "अक्षरों के उस संयोजन का चयन कीजिए जो दी गई श्रृंखला की रिक्त स्थानों में क्रमिक रूप से रखे जाने पर श्रृंखला को पूरा करेगा। _np_rr_p_mm_pq_rq_nm_np_rq_nm",
        "option_a": "mqqnnrpmqp",
        "option_b": "mrqnnrpmqp",
        "option_c": "mqqrnrpmqp",
        "option_d": "mqqnnrpnqp",
        "correct_answer": "A",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q8
    {
        "question_number": 8,
        "difficulty": "hard",
        "question_en": "Select the combination of letters that when sequentially placed in the blanks will complete the series. C_EF HNE_ _NEP RN_U WNE_ [CHSL Tier II - 10 Jan 2024 - Shift 1]",
        "question_hi": "अक्षरों के उस संयोजन का चयन कीजिए जो दी गई श्रृंखला की रिक्त स्थानों में क्रमिक रूप से रखे जाने पर श्रृंखला को पूरा करेगा। C_EF HNE_ _NEP RN_U WNE_",
        "option_a": "PAWER",
        "option_b": "FHOSM",
        "option_c": "NKMEZ",
        "option_d": "CAHKL",
        "correct_answer": "C",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q9
    {
        "question_number": 9,
        "difficulty": "hard",
        "question_en": "Select the combination of letters that when sequentially placed in the blanks will complete the series. GA_B M_PB SA_B YAB_ _AHB [CHSL Tier II - 10 Jan 2024 - Shift 1]",
        "question_hi": "अक्षरों के उस संयोजन का चयन कीजिए जो दी गई श्रृंखला की रिक्त स्थानों में क्रमिक रूप से रखे जाने पर श्रृंखला को पूरा करेगा। GA_B M_PB SA_B YAB_ _AHB",
        "option_a": "AWBUY",
        "option_b": "JAVBE",
        "option_c": "CHFJK",
        "option_d": "MXOVZ",
        "correct_answer": "B",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q10
    {
        "question_number": 10,
        "difficulty": "hard",
        "question_en": "Select the combination of letters that when sequentially placed in the blanks will complete the series. CB_W V_SP _NLI HG_B A_XU [CHSL Tier II - 10 Jan 2024 - Shift 1]",
        "question_hi": "अक्षरों के उस संयोजन का चयन कीजिए जो दी गई श्रृंखला की रिक्त स्थानों में क्रमिक रूप से रखे जाने पर श्रृंखला को पूरा करेगा। CB_W V_SP _NLI HG_B A_XU",
        "option_a": "XUOFY",
        "option_b": "XUOEZ",
        "option_c": "XUOEY",
        "option_d": "ZUOEZ",
        "correct_answer": "D",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
    },
    # Q11
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": "What should come in place of (?) in the given series based on the English alphabetical order? SLE, CXS, ?, WVU, GHI [CHSL - 2 July 2024 - Shift 4]",
        "question_hi": "अंग्रेजी वर्णमाला क्रम के आधार पर दी गई श्रृंखला में (?) के स्थान पर क्या आना चाहिए? SLE, CXS, ?, WVU, GHI",
        "option_a": "MJG",
        "option_b": "OWG",
        "option_c": "COR",
        "option_d": "HAP",
        "correct_answer": "A",
        "source_pdf": "Gagan_Pratap_Reasoning_Series_Sheet1",
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
            fp = d.pop("source_pdf")
            if d["question_en"][:80] in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                d["source_pdf"] = fp
                continue

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = fp,
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
