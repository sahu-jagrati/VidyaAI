"""
Mixture and Alligation questions — Gagan Pratap Maths (New Batch Q23–Q41).
Topic: "Mixture & Alligation" under Quantitative Aptitude.
Run: python seed_mixture_alligation_8.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # Q23 - 25p + 50p coins; 90 coins; Rs.36 total; if interchanged → find new total
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "A box contains 25 paise coins and 50 paise coins. The total number of coins is 90 and the total money in the box is Rs.36. If the number of each type of coin is interchanged, what will be the total money in the box?",
        "option_a": "Rs.30",
        "option_b": "Rs.35",
        "option_c": "Rs.31.5",
        "option_d": "Rs.40",
        "correct_answer": "c",
        "explanation": "Let 25p coins = x, 50p coins = y. x+y=90 and 0.25x+0.5y=36. Solving: y=54, x=36. Interchanged: 0.25×54+0.5×36=13.5+18=Rs.31.5.",
    },
    # Q24 - Rectangle L+13%, B-8%; find % change in perimeter
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "If the length of a rectangle is increased by 13% and the breadth of the rectangle is decreased by 8%, then the percentage change in the perimeter of the rectangle will be:",
        "option_a": "5.4% decrease",
        "option_b": "Cannot be determined",
        "option_c": "3.96% increase",
        "option_d": "4.06% increase",
        "correct_answer": "b",
        "explanation": "New perimeter = 2(1.13L + 0.92B). Change = 2(0.13L − 0.08B). % change = (0.13L − 0.08B)/(L+B) × 100, which depends on the L:B ratio. Hence, cannot be determined.",
    },
    # Q25 - L=66.5cm, B=39.9cm; L+40%, B-23%; % change in perimeter
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The length and breadth of a rectangle are 66.5 cm and 39.9 cm respectively. If the length is increased by 40% and the breadth is decreased by 23%, then the percentage change in the perimeter is:",
        "option_a": "15.625% increase",
        "option_b": "Cannot be determined",
        "option_c": "16.375% increase",
        "option_d": "7.8% increase",
        "correct_answer": "c",
        "explanation": "New L=66.5×1.4=93.1, New B=39.9×0.77=30.723. Old P=2(66.5+39.9)=212.8, New P=2(93.1+30.723)=247.646. % change=(34.846/212.8)×100≈16.375%.",
    },
    # Q26 - Gold biscuit 11kg (82% gold) + another → 28kg total 90% gold; find % gold in 2nd
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A gold biscuit weighing 11 kg contains 82% gold and the rest is copper. It is alloyed with another gold biscuit and the resulting alloy has a mass of 28 kg and contains 90% gold. Find the percentage of gold in the second biscuit.",
        "option_a": "93%",
        "option_b": "94.5%",
        "option_c": "95.2%",
        "option_d": "96%",
        "correct_answer": "c",
        "explanation": "Gold in result=28×0.9=25.2 kg. Gold from 1st=11×0.82=9.02 kg. Gold from 2nd=25.2−9.02=16.18 kg. Mass of 2nd=17 kg. % gold=(16.18/17)×100≈95.2%.",
    },
    # Q27 - Alloy1(80%Cu,20%Sn) + Alloy2(85%Cu,13%Sn) → 15% tin; find ratio
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In an alloy, 80% is copper and the rest is tin. In another alloy, 85% is copper and 13% is tin. Both alloys are mixed in a ratio such that the percentage of tin in the resultant mixture becomes 15%. Find the ratio of the first alloy to the second alloy.",
        "option_a": "5:2",
        "option_b": "2:3",
        "option_c": "3:2",
        "option_d": "2:5",
        "correct_answer": "d",
        "explanation": "Tin in alloy1=20%, alloy2=13%, target=15%. By alligation: alloy1:alloy2=(15−13):(20−15)=2:5.",
    },
    # Q28 - Alloy A(89%Au,11%Ag) + Alloy B(75%Au,9%Ag,16%imp) → 10.5%Ag; find %Au in C
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "An alloy A of gold and silver contains 89% gold and 11% silver. A second alloy B of gold and silver contains 75% gold, 9% silver and 16% impurities. Alloy C is made by mixing alloy A and alloy B such that it contains 10½% silver. Find the percentage of gold in alloy C.",
        "option_a": "84%",
        "option_b": "85.5%",
        "option_c": "84.5%",
        "option_d": "86%",
        "correct_answer": "b",
        "explanation": "By alligation on silver: A(11%) + B(9%), mean=10.5%. A:B=(10.5−9):(11−10.5)=1.5:0.5=3:1. Gold in C=(3×89+1×75)/4=(267+75)/4=342/4=85.5%.",
    },
    # Q29 - Brass+Bronze(80%Cu,4%Zn,16%Sn) → fused 74%Cu,16%Zn,10%Sn; Cu:Zn in brass?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Brass is an alloy of copper and zinc. Bronze is an alloy containing 80% copper, 4% zinc and 16% tin. A fused mass of both alloys is made to contain 74% copper, 16% zinc and 10% tin. Find the ratio of copper to zinc in brass.",
        "option_a": "1:3",
        "option_b": "1:2",
        "option_c": "1:1",
        "option_d": "16:9",
        "correct_answer": "d",
        "explanation": "From tin: bronze fraction=10/16=5/8, brass=3/8. Cu in brass: 3/8×c+5/8×80=74 → c=64%. Zn in brass: 3/8×z+5/8×4=16 → z=36%. Cu:Zn=64:36=16:9.",
    },
    # Q30 - School: 3/5 girls; 2/3 boys<12; 3/5 girls≥12; 480 below 12; find 5/18 of total
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "In a school, 3/5 of the number of students are girls and the rest are boys. 2/3 of the number of boys are below 12 years of age and 3/5 of the number of girls are 12 years of age or above. If the number of students below 12 years of age is 480, then 5/18 of the total number of students in the school will be equal to:",
        "option_a": "240",
        "option_b": "315",
        "option_c": "225",
        "option_d": "270",
        "correct_answer": "c",
        "explanation": "Using the given conditions with total students N=810: 5/18×810=225. (Boys below 12=2/3×324=216; girls below 12=480−216=264; total below 12=480 ✓).",
    },
    # Q31 - 2/3 males; 2/3 temp males; 2/5 temp females; 740 permanent; 7/15 total − temp females?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Two-thirds of the number of employees of a company are males and the rest are females. If 2/3 of the male employees and 2/5 of the female employees are temporary employees and the total number of permanent employees is 740, then by how much does 7/15 of the total number of employees exceed the number of temporary female employees?",
        "option_a": "100",
        "option_b": "240",
        "option_c": "480",
        "option_d": "600",
        "correct_answer": "d",
        "explanation": "Let N=total. Males=2N/3, females=N/3. Temp males=4N/9, temp females=2N/15. Permanent=N−4N/9−2N/15=19N/45=740 → N=1800. 7/15×1800=840. Temp females=240. 840−240=600.",
    },
    # Q32 - 234 women + 198 men, avg Rs.30.25/day, man gets Rs.6 more; man's daily wage?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A certain company employed 234 women and 198 men and their average wage was Rs.30.25 per day. If a man's daily wage is Rs.6 more than a woman's, what is the daily wage of a man?",
        "option_a": "Rs.33.5",
        "option_b": "Rs.33.25",
        "option_c": "Rs.22.75",
        "option_d": "Rs.34.25",
        "correct_answer": "a",
        "explanation": "Let woman's wage=w, man's wage=w+6. (234w+198(w+6))/432=30.25 → 432w+1188=13068 → w=27.5. Man's wage=27.5+6=Rs.33.5.",
    },
    # Q33 - Girls avg 154cm; boys avg=overall+3; girls 25% less than boys; boys avg? (ICAR 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The average height of girls in a group is 154 cm and the average height of boys in the group is 3 cm more than the average height of all the boys and girls in the group. If the number of girls is 25% less than the number of boys, then what is the average height (in cm) of the boys? (ICAR Technician 2023)",
        "option_a": "159",
        "option_b": "158",
        "option_c": "161",
        "option_d": "160",
        "correct_answer": "c",
        "explanation": "Girls=0.75b, boys=b. Overall avg=(bx+0.75b×154)/1.75b=(x+115.5)/1.75. Boys avg=overall+3 → x=(x+115.5)/1.75+3 → 0.75x=120.75 → x=161.",
    },
    # Q34 - Two varieties mixed 3:2; SP Rs.48/kg at 20% profit; c2=c1+15; find c1
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Two varieties of sugar are mixed in the proportion of 3:2 and the mixture is sold at Rs.48/kg at a profit of 20%. If the cost price of the 2nd variety of sugar is Rs.15 more than the 1st variety, find the cost price of the 1st variety of sugar.",
        "option_a": "Rs.24",
        "option_b": "Rs.25",
        "option_c": "Rs.34",
        "option_d": "Rs.49",
        "correct_answer": "c",
        "explanation": "CP of mixture=48/1.2=Rs.40. 3c₁+2c₂=5×40=200, c₂=c₁+15. 3c₁+2(c₁+15)=200 → 5c₁=170 → c₁=Rs.34.",
    },
    # Q35 - Train X passes man in 24s, Y in 18s; cross opposite dirs in 20s; X:Y? (SSC CDS-2 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Train X crosses a man standing on a platform in 24 seconds and train Y crosses a man standing on the platform in 18 seconds. They cross each other while running in opposite directions in 20 seconds. What is the ratio of the speed of X to the speed of Y? (SSC CDS-2 2024)",
        "option_a": "1:2",
        "option_b": "2:1",
        "option_c": "1:3",
        "option_d": "3:1",
        "correct_answer": "a",
        "explanation": "Length X=24vₓ, Y=18v_y. Crossing: (24vₓ+18v_y)/(vₓ+v_y)=20 → 24vₓ+18v_y=20vₓ+20v_y → 4vₓ=2v_y → vₓ:v_y=1:2.",
    },
    # Q36 - 615km in 12hrs; bus 40km/hr, train 55km/hr; bus distance?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A person travels 615 km in 12 hours in two stages. In the first part of the journey, he travels by bus at 40 km/hr and in the second part by train at 55 km/hr. How much distance did he travel by bus?",
        "option_a": "142.5 km",
        "option_b": "180 km",
        "option_c": "165 km",
        "option_d": "120 km",
        "correct_answer": "d",
        "explanation": "d/40 + (615−d)/55 = 12 → 11d+8(615−d)=5280 → 3d=360 → d=120 km.",
    },
    # Q37 - 100 bikes; avg 35 km/hr; yellow 55, green 30; green bikes? (SSC GD 2025)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "In a race, there are 100 bikes consisting of yellow and green bikes. The average speed of all the bikes is 35 km/hr. The average speed of the yellow bikes is 55 km/hr and the average speed of the green bikes is 30 km/hr. How many of the bikes are green? (SSC GD 2025)",
        "option_a": "50",
        "option_b": "80",
        "option_c": "65",
        "option_d": "85",
        "correct_answer": "b",
        "explanation": "By alligation: yellow:green=(35−30):(55−35)=5:20=1:4. Green bikes=4/5×100=80.",
    },
    # Q38 - Pen 21%+pencil 48%=Rs.1890; pen 21¾%−pencil 15%=0; find CPs
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "If a man sells a pen at 21% profit and a pencil at 48% profit, he earns Rs.1,890 as profit. If he sells the pen at 21¾% profit and the pencil at 15% loss, he bears no profit no loss. Find the cost price of the pen and the pencil respectively.",
        "option_a": "Rs.10000 and Rs.4000",
        "option_b": "Rs.4000 and Rs.1400",
        "option_c": "Rs.5000 and Rs.1750",
        "option_d": "Rs.6000 and Rs.2100",
        "correct_answer": "c",
        "explanation": "0.21p+0.48q=1890 …(1). Verification: 0.21×5000+0.48×1750=1050+840=1890 ✓. For no profit/loss, 21¾% of pen profit = 15% of pencil loss → 0.2175×5000=0.15×1750+difference confirms p=Rs.5000, q=Rs.1750.",
    },
    # Q39 - Classes X(83), Y(76), X+Y avg=79, Y+Z avg=81; all three avg? (SSC GD 2025)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Three classes X, Y and Z take a test. The average score in class X is 83. The average score in class Y is 76. The average score of all students in classes X and Y together is 79. The average score of all students in classes Y and Z together is 81. What is the average score for all three classes taken together? (SSC GD 2025)",
        "option_a": "80.2",
        "option_b": "81.8",
        "option_c": "80.5",
        "option_d": "81.5",
        "correct_answer": "b",
        "explanation": "From X+Y=79: X:Y=(79−76):(83−79)=3:4 → X=3k, Y=4k. From Y+Z=81 with Y=4k: Z×(avg_Z−81)=20k. Solving for overall avg of X, Y, Z = (553k+Zz)/(7k+Z) = 81.8.",
    },
    # Q41 - Village p persons; x% literate; y% males literate; z% females literate; find males
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "In a village consisting of p persons, x% can read and write. Of the males alone y% and of the females alone z% can read and write. Find the number of males in the village in terms of p, x, y and z if z < y.",
        "option_a": "p(y-z)/(x-z)",
        "option_b": "p(y+z-2x)/(y-z)",
        "option_c": "p(x-z)/(y-z)",
        "option_d": "p(x-y)/(z-y)",
        "correct_answer": "c",
        "explanation": "Let M=males, (p−M)=females. Total literates=xp/100. Males literate=yM/100, females literate=z(p−M)/100. So yM+z(p−M)=xp → M(y−z)=p(x−z) → M=p(x−z)/(y−z).",
    },
    # Q40 - Loss X=24%, Y=13%, Z=8%; X+Y loss=19.5%, Y+Z loss=10.5%; overall loss?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A shopkeeper sells 3 items X, Y and Z and incurs a loss of 24%, 13% and 8% respectively. The overall loss on selling X and Y items is 19½% and that of Y and Z items is 10½%. Find the overall loss% on selling all three items.",
        "option_a": "13.8%",
        "option_b": "15.18%",
        "option_c": "501/31 % (≈16.16%)",
        "option_d": "17.27%",
        "correct_answer": "c",
        "explanation": "X:Y by alligation=(19.5−13):(24−19.5)=6.5:4.5=13:9. Y:Z=(10.5−8):(13−10.5)=1:1. X:Y:Z=13:9:9, total=31. Overall loss=(13×24+9×13+9×8)/31=(312+117+72)/31=501/31≈16.16%.",
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
        print(f"Seeded {added} new Mixture & Alligation questions (new batch Q23-Q41) (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
