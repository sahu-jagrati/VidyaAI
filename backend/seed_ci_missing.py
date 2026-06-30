"""
Missing Compound Interest questions not covered in other CI seed files.
Run: python seed_ci_missing.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [

{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"If a certain sum of money of Rs.345600 amounts to Rs.439400 in 3 years. Find the rate of compound interest.",
  "question_text_hi":"345600 रू का धन 3 वर्ष में 439400 रू हो जाता है। चक्रवृद्धि ब्याज की दर ज्ञात करें?",
  "option_a":"6 2/3%","option_a_hi":"6 2/3%",
  "option_b":"8 1/3%","option_b_hi":"8 1/3%",
  "option_c":"12 1/2%","option_c_hi":"12 1/2%",
  "option_d":"7 9/13%","option_d_hi":"7 9/13%",
  "correct_answer":"b",
  "explanation":"439400/345600=(1+r)^3. ∛(1.2714)≈1.0833. r=8.33%=8⅓%",
  "explanation_hi":"r≈8⅓%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"If the amount received at the end of 2nd and 3rd year at compound interest on a certain Principal is Rs.9,600 and Rs.10,272 respectively, what is the rate of interest (in %)?",
  "question_text_hi":"यदि किसी मूलधन पर दूसरे और तीसरे वर्ष में मिलने वाले मिश्रधन, चक्रवृद्धि ब्याज की दर से क्रमशः 9,600 रूपये और 10,272 रूपये है तो ब्याज की दर (% में) क्या होगी?",
  "option_a":"7","option_a_hi":"7",
  "option_b":"8","option_b_hi":"8",
  "option_c":"6","option_c_hi":"6",
  "option_d":"5","option_d_hi":"5",
  "correct_answer":"a",
  "explanation":"Rate = (10272 − 9600)/9600 × 100 = 7%",
  "explanation_hi":"(10272−9600)/9600 × 100 = 7%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"Rahul earns an interest of Rs 2996 for the third year and Rs 1400 for the second year on the same sum. Find the rate of interest per annum if it is lent at compound interest (compounding annually).",
  "question_text_hi":"राहुल को उसी राशि पर तीसरे वर्ष में 2996 रुपये और दूसरे वर्ष में 1400 रुपये का ब्याज मिलता है। यदि चक्रवृद्धि ब्याज (वार्षिक चक्रवृद्धि) पर उधार दिया गया है तो ब्याज की वार्षिक दर ज्ञात करें?",
  "option_a":"114%","option_a_hi":"114%",
  "option_b":"112%","option_b_hi":"112%",
  "option_c":"110%","option_c_hi":"110%",
  "option_d":"113%","option_d_hi":"113%",
  "correct_answer":"a",
  "explanation":"CI(3rd year)/CI(2nd year) = 1+r. 2996/1400 = 2.14 → r = 114%",
  "explanation_hi":"2996/1400 = 2.14 → r=114%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"At what rate% per annum will Rs.4704 amount to Rs.5766 in two years compounded annually?",
  "question_text_hi":"4704 रू का धन 2 वर्ष में 5766 हो जाता है। चक्रवृद्धि ब्याज की दर ज्ञात करें?",
  "option_a":"8 4/7%","option_a_hi":"8 4/7%",
  "option_b":"11 3/7%","option_b_hi":"11 3/7%",
  "option_c":"12 1/7%","option_c_hi":"12 1/7%",
  "option_d":"10 5/7%","option_d_hi":"10 5/7%",
  "correct_answer":"d",
  "explanation":"5766/4704=(1+r)^2=1.225625. 1+r=31/28. r=3/28=10 5/7%",
  "explanation_hi":"r=3/28=10 5/7%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"At what rate of interest per annum compounded annually, will an amount of ₹8,000 yield a compound interest of ₹904.2 in 2 years?",
  "question_text_hi":"वार्षिक रूप से संयोजित किस वार्षिक ब्याज दर पर, रुपये 8,000 की धनराशि पर 2 वर्षों में रुपये 904.2 का चक्रवृद्धि ब्याज प्राप्त होगा?",
  "option_a":"6%","option_a_hi":"6%",
  "option_b":"8%","option_b_hi":"8%",
  "option_c":"10%","option_c_hi":"10%",
  "option_d":"5.5%","option_d_hi":"5.5%",
  "correct_answer":"d",
  "explanation":"8000×((1+r)^2−1)=904.2 → (1+r)^2=1.113025 → r=5.5%",
  "explanation_hi":"r=5.5%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"A sum of money lent on interest compounded semi-annually amounts to ₹54,000 in one year and ₹65,340 in two years. What is the rate of interest per annum?",
  "question_text_hi":"ब्याज पर उधार दी गई एक धनराशि, ब्याज अर्ध-वार्षिक रूप से संयोजित होता है, एक वर्ष में ₹54,000 और दो वर्षों में ₹65,340 हो जाती है। वार्षिक ब्याज दर ज्ञात करें।",
  "option_a":"20%","option_a_hi":"20%",
  "option_b":"10%","option_b_hi":"10%",
  "option_c":"16%","option_c_hi":"16%",
  "option_d":"12%","option_d_hi":"12%",
  "correct_answer":"a",
  "explanation":"(1+r/2)^2 = 65340/54000 = 1.21 → 1+r/2=1.1 → r=20%",
  "explanation_hi":"r=20%",
},

]


def seed():
    db = SessionLocal()
    try:
        existing = {
            r[0]
            for r in db.query(Question.question_text)
                         .filter(Question.subject_code == "quant",
                                 Question.topic == "Compound Interest")
                         .all()
        }
        new_qs = [q for q in QUESTIONS if q["question_text"] not in existing]
        for qdata in new_qs:
            db.add(Question(**qdata))
        db.commit()
        print(f"✓ Inserted {len(new_qs)} new CI questions. "
              f"({len(QUESTIONS)-len(new_qs)} already existed)")
    except Exception as e:
        db.rollback()
        print(f"✗ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
