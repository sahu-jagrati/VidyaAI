"""
Mixture and Alligation questions — Gagan Pratap Maths (New Batch Q1–Q22).
Topic: "Mixture & Alligation" under Quantitative Aptitude.
Run: python seed_mixture_alligation_7.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # Q1 - Rural:Urban = 4:7, avg 65/63; overall avg
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "In a class the ratio of rural to urban students is 4:7. In an examination the average percentage marks of the rural and the urban students are respectively 65 and 63. What is the overall average percentage marks of the class (correct to two decimal places)?",
        "option_a": "65.87%",
        "option_b": "73.63%",
        "option_c": "63.73%",
        "option_d": "64.37%",
        "correct_answer": "c",
        "explanation": "Overall = (4×65 + 7×63)/(4+7) = (260+441)/11 = 701/11 = 63.73%.",
    },
    # Q2 - 42 students: 18 avg 95, 24 avg 73; overall avg (SSC MTS 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "A class of 42 students took a Physics test. 18 students had an average score of 95. The other students had an average score of 73. What is the average score (rounded off to one decimal place) of the whole class? (SSC MTS 2024)",
        "option_a": "79.6",
        "option_b": "86.1",
        "option_c": "90.7",
        "option_d": "82.4",
        "correct_answer": "d",
        "explanation": "Overall = (18×95 + 24×73)/42 = (1710+1752)/42 = 3462/42 = 82.4.",
    },
    # Q3 - 147 workers, male:female=13:8, avg weight 65; male avg 72; find female avg
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "There are 147 workers in a factory whose average weight is 65 kg. The ratio of the number of male workers and female workers in the factory is 13:8. If the average weight of male workers is 72 kg, find the average weight (x kg) of female workers.",
        "option_a": "54.125 kg",
        "option_b": "53.625 kg",
        "option_c": "58.375 kg",
        "option_d": "57.625 kg",
        "correct_answer": "b",
        "explanation": "Males=91, females=56. 91×72 + 56×x = 147×65 → 6552+56x=9555 → x=3003/56=53.625 kg.",
    },
    # Q4 - 240 students: 37.5% boys avg 67.1, girls avg 85.5; overall avg
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In a class of 240 students, 37.5% are boys and the remaining are girls. The average of the boys' marks is 67.1 and that of the girls is 85.5. What are the average marks of the whole class?",
        "option_a": "80.2",
        "option_b": "79.4",
        "option_c": "77.5",
        "option_d": "78.6",
        "correct_answer": "d",
        "explanation": "Boys=90, girls=150. Overall=(90×67.1+150×85.5)/240=(6039+12825)/240=18864/240=78.6.",
    },
    # Q5 - 42 students avg 69; boys:girls=10:11; boys 20% more avg than girls; boys avg?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The average score of 42 students in a test is 69. The ratio of the number of boys to that of girls is 10:11. The average score of the boys is 20% more than that of the girls. The average score of the boys is:",
        "option_a": "73.5",
        "option_b": "75.2",
        "option_c": "82.8",
        "option_d": "75.6",
        "correct_answer": "d",
        "explanation": "Boys=20, girls=22. Let girls avg=g, boys=1.2g. (24g+22g)/42=69 → 46g=2898 → g=63. Boys avg=1.2×63=75.6.",
    },
    # Q6 - 120 students avg 13.56 yrs; 35% girls; boys:girls avg ratio=6:5; girls avg?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The average age of 120 students in a group is 13.56 years. 35% of the number of students are girls and the rest are boys. If the ratio of the average age of boys and girls is 6:5, then what is the average age (in years) of the girls?",
        "option_a": "10",
        "option_b": "12",
        "option_c": "11.6",
        "option_d": "14.4",
        "correct_answer": "b",
        "explanation": "Girls=42, boys=78. Let girls avg=5k, boys=6k. (78×6k+42×5k)/120=13.56 → 678k=1627.2 → k=2.4. Girls avg=5×2.4=12.",
    },
    # Q7 - 80 questions; 60% correct in first 55; need 70% overall; % correct in remaining?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In a test consisting of 80 questions, Anita answered 60% of the first 55 questions correctly. What per cent of the remaining questions should she answer correctly to obtain 70% in the entire exam?",
        "option_a": "85%",
        "option_b": "92%",
        "option_c": "80%",
        "option_d": "78%",
        "correct_answer": "b",
        "explanation": "Correct in first 55 = 33. Need total = 56. Remaining 25 questions: need 23. % = 23/25×100 = 92%.",
    },
    # Q8 - City pop 18000; males +5%, females +7%; total 19200; male:female ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In a certain year, the population of a city was 18000. If in the next year, the population of males increased by 5% and that of females increased by 7%, and the total population increased to 19200, then what was the ratio of the populations of males and females in that given year?",
        "option_a": "2:5",
        "option_b": "1:5",
        "option_c": "4:3",
        "option_d": "3:5",
        "correct_answer": "b",
        "explanation": "1.05m + 1.07(18000-m) = 19200 → -0.02m = -60 → m = 3000, f = 15000. Ratio = 1:5.",
    },
    # Q9 - 600 employees; male avg 42, female avg 41; overall 41yr 9mo; females?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In a company with 600 employees, the average age of the male employees is 42 years and that of the female employees is 41 years. If the average age of all the employees in the company is 41 years 9 months, then the number of female employees is:",
        "option_a": "150",
        "option_b": "250",
        "option_c": "450",
        "option_d": "350",
        "correct_answer": "a",
        "explanation": "Overall = 41.75 years. 42(600-f) + 41f = 41.75×600 → 25200-f = 25050 → f = 150.",
    },
    # Q10 - Junior Rs.325, senior Rs.400; 80 juniors; avg Rs.352; seniors? (SSC CGL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "During a school excursion each student of junior school was charged Rs.325 and each student of senior school was charged Rs.400. If there were 80 students from junior school and the combined average amount charged per student was Rs.352, then how many students from senior school went for the excursion? (SSC CGL 2023 PRE)",
        "option_a": "55",
        "option_b": "45",
        "option_c": "50",
        "option_d": "40",
        "correct_answer": "b",
        "explanation": "(80×325 + s×400)/(80+s) = 352 → 26000+400s = 28160+352s → 48s = 2160 → s = 45.",
    },
    # Q11 - Army 12000: Europeans 70 in, Indians 69 in, overall 69.25 in; Indians?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "An army of 12,000 consists of Europeans and Indians. The average height of Europeans is 70 inches and that of an Indian is 69 inches. The average height of the whole army is 69¼ inches. Find the number of Indians in the army.",
        "option_a": "9000",
        "option_b": "3000",
        "option_c": "6000",
        "option_d": "8000",
        "correct_answer": "a",
        "explanation": "(12000-i)×70 + i×69 = 12000×69.25 → 840000-i = 831000 → i = 9000.",
    },
    # Q12 - 12 employees avg Rs.3950; another group avg Rs.1850; overall Rs.2150; total? (SSC CHSL PRE 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The average salary of a group of 12 employees in an institution is ₹3,950 per month and that of another group of employees is ₹1,850. If the average salary of all employees is ₹2,150, then the total number of employees is: (SSC CHSL PRE 2024)",
        "option_a": "100",
        "option_b": "88",
        "option_c": "84",
        "option_d": "72",
        "correct_answer": "c",
        "explanation": "(12×3950 + n×1850)/(12+n) = 2150 → 21600 = 300n → n = 72. Total = 84.",
    },
    # Q13 - A+B income Rs.42000; A +8%, B +3%; total up Rs.2800; B's income? (DSSSB HEAD CLERK 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The total income of two persons A and B is Rs.42,000. If the income of A and B is increased by 8% and 3% respectively, then the total income of both of them is increased by Rs.2800. What is the income (in Rs) of B? (DSSSB HEAD CLERK 2022)",
        "option_a": "Rs.29,900",
        "option_b": "Rs.11,200",
        "option_c": "Rs.30,800",
        "option_d": "Rs.12,100",
        "correct_answer": "b",
        "explanation": "0.08a + 0.03(42000-a) = 2800 → 0.05a = 1540 → a = 30800. B = 42000-30800 = Rs.11,200.",
    },
    # Q14 - 952 tickets: parents Rs.7.50, children Rs.3; total Rs.5925; children tickets? (RRB GROUP D 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Tickets for one show cost Rs.7.50 for parents and Rs.3 for children. If an amount of Rs.5925 was collected from the sale of 952 tickets, then find the number of children tickets sold. (RRB GROUP D 2022)",
        "option_a": "270",
        "option_b": "300",
        "option_c": "500",
        "option_d": "682",
        "correct_answer": "a",
        "explanation": "Let c = children tickets. 7.5(952-c)+3c=5925 → 7140-4.5c=5925 → c=270.",
    },
    # Q15 - Rice 720kg@Rs.325 + 675kg@Rs.195; 22% profit on 1st, 40% overall; SP of 2nd?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A person buys two types of rice costing Rs.325/kg and Rs.195/kg respectively. The quantities bought are 720 kg and 675 kg. He wants to earn 22% profit on the 1st kind of rice but wants to gain 40% overall profit. At what price should he sell the second kind of rice (Rs/kg)?",
        "option_a": "331.5 Rs/kg",
        "option_b": "341.25 Rs/kg",
        "option_c": "315.9 Rs/kg",
        "option_d": "335.4 Rs/kg",
        "correct_answer": "d",
        "explanation": "Total CP=365625; Total SP=511875. SP of 1st=720×325×1.22=285480. SP of 2nd=226395. Rate=226395/675=335.4 Rs/kg.",
    },
    # Q16 - Saves x%; income +26%, expenditure +20%, savings +50%; x?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Rishu saves x% of her income. If her income increases by 26% and the expenditure increases by 20%, then her savings increase by 50%. What is the value of x?",
        "option_a": "30",
        "option_b": "20",
        "option_c": "10",
        "option_d": "25",
        "correct_answer": "b",
        "explanation": "Income=100, savings=x, expenditure=100-x. New savings=126-1.2(100-x)=6+1.2x. (6+1.2x)/x=1.5 → x=20.",
    },
    # Q17 - Saves 35%; income +20.1%, expenditure +25%; savings change?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A saves 35% of his income. His income is increased by 20.1% and expenditure is increased by 25%. By what percentage does his saving increase or decrease?",
        "option_a": "11% increase",
        "option_b": "9% decrease",
        "option_c": "13% increase",
        "option_d": "14% decrease",
        "correct_answer": "a",
        "explanation": "Income=100, savings=35, expenditure=65. New savings=120.1-65×1.25=120.1-81.25=38.85. Change=(3.85/35)×100=11% increase.",
    },
    # Q18 - Expenditure 50% more than savings; income +15%, expenditure +21%, savings +Rs.240; initial income?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Expenditure of a person is 50% more than his savings. If the income increases by 15% and his expenditure also increases by 21%, if his savings increases by Rs.240, find his initial income.",
        "option_a": "Rs.5,000",
        "option_b": "Rs.4,000",
        "option_c": "Rs.8,000",
        "option_d": "Rs.10,000",
        "correct_answer": "d",
        "explanation": "E=1.5S, I=2.5S. New savings=(2.875S-1.815S)=1.06S. 0.06S=240 → S=4000. Income=2.5×4000=Rs.10,000.",
    },
    # Q19 - Milk Rs.70/L + Rs.50/L → Rs.55/L; ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "There are two types of milk. The price of one type of milk is ₹70/litre and the price of other type is ₹50/litre. If the two types of milk are mixed, the price of new mixture will be ₹55/litre. Find the ratio of the two types of milk in this new mixture.",
        "option_a": "1:1",
        "option_b": "1:2",
        "option_c": "1:4",
        "option_d": "1:3",
        "correct_answer": "d",
        "explanation": "Alligation: (55-50):(70-55) = 5:15 = 1:3. So Rs.70 type:Rs.50 type = 1:3.",
    },
    # Q20 - 60L milk at 1½ L/Re; add water to make mixture at 2 L/Re (SSC CHSL PRE 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "How much water should be added to 60 liters of milk at 1½ liters a rupee so as to have a mixture worth 1⅓ liters a rupee? (SSC CHSL PRE 2024)",
        "option_a": "15 L",
        "option_b": "12 L",
        "option_c": "27 L",
        "option_d": "20 L",
        "correct_answer": "d",
        "explanation": "Milk at 1½ L/Re = cost 2/3 Rs/L. Water = free (0). By alligation for target mixture rate: milk:water = 3:1. For 60L milk, water = 60/3 = 20 L.",
    },
    # Q21 - 48L mixture; sell at Rs.45/L no profit no loss; pure milk Rs.54/L; water in mixture?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A milkman sells the milk by adding water in it at Rs.45/litre with no profit no loss. If he had 48 litre of mixture of milk and water with him and the pure milk costs Rs.54/litre, what is the quantity of water in the mixture?",
        "option_a": "6 L",
        "option_b": "12 L",
        "option_c": "8 L",
        "option_d": "9 L",
        "correct_answer": "c",
        "explanation": "Alligation: milk(54) + water(0), mean=45. Milk:Water=(45-0):(54-45)=45:9=5:1. In 48L: water=48/6=8 L.",
    },
    # Q22 - Rs.41 among 50 students; boys 90p, girls 65p; boys count?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A sum of Rs.41 was divided among 50 students. If each boy got 90 paise and each girl got 65 paise, find the number of boys.",
        "option_a": "43",
        "option_b": "33",
        "option_c": "34",
        "option_d": "32",
        "correct_answer": "c",
        "explanation": "90b + 65(50-b) = 4100 → 25b = 850 → b = 34.",
    },
]


def seed():
    db = SessionLocal()
    try:
        added = 0
        for q in QUESTIONS:
            exists = db.query(Question).filter(
                Question.question_text == q["question_text"]
            ).first()
            if not exists:
                db.add(Question(**q))
                added += 1
        db.commit()
        print(f"Seeded {added} new Mixture & Alligation questions (new batch Q1-Q22) (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
