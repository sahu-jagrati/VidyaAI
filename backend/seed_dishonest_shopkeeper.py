"""
Dishonest Shopkeeper questions — Gagan Pratap Maths (54 questions).
Topic: "Dishonest Shopkeeper" under Quantitative Aptitude.
Run: python seed_dishonest_shopkeeper.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models.attempt_model import Attempt

QUESTIONS = [
    # ── Q1 ── Shopkeeper sells at CP but uses 40% less weight; find profit%
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "easy", "phase": "main",
        "question_text": "A dishonest shopkeeper promises to sell his goods at its CP but he uses 40% less weight. Find his profit %.",
        "option_a": "40%",
        "option_b": "66.66%",
        "option_c": "50%",
        "option_d": "None of these",
        "correct_answer": "b",
        "explanation": "He gives 600g instead of 1000g but charges for 1000g. Profit% = (1000−600)/600 × 100 = 400/600 × 100 = 66.66%.",
    },
    # ── Q2 ── Shopkeeper sells at CP but uses 840gm instead of 1kg; find profit% (approx.)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "easy", "phase": "main",
        "question_text": "A dishonest shopkeeper promises to sell his goods at its CP but he uses 840gm weight instead of 1 kg. Find his profit % (approx.).",
        "option_a": "19%",
        "option_b": "14.28%",
        "option_c": "20%",
        "option_d": "21%",
        "correct_answer": "a",
        "explanation": "Profit% = (1000−840)/840 × 100 = 160/840 × 100 ≈ 19.04% ≈ 19%.",
    },
    # ── Q3 ── Shopkeeper sells at 30% profit but uses 800gm instead of 1kg; find actual profit%
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A dishonest shopkeeper promises to sell his goods at 30% profit but he uses 800gm weight instead of 1kg. Find his actual profit %.",
        "option_a": "58.33%",
        "option_b": "62.5%",
        "option_c": "66.66%",
        "option_d": "60%",
        "correct_answer": "b",
        "explanation": "CP per kg = 100. He charges 130 (30% profit) but gives 800g costing 80. Actual profit% = (130−80)/80 × 100 = 62.5%.",
    },
    # ── Q4 ── Ram sells almonds at CP using false weight; gains 20% profit; grams given in 3.78 kg?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "Ram sells almonds at the cost price but uses false weight and thus gains 20% profit. How many grams of almonds does he give in 3.78 kilograms?",
        "option_a": "3150",
        "option_b": "2700",
        "option_c": "2800",
        "option_d": "2640",
        "correct_answer": "a",
        "explanation": "(1000 − false)/false = 20/100. false = 1000/1.2 = 833.33g per kg. In 3.78 kg (= 3780g stated): actual = 3780 × 833.33/1000 = 3150g.",
    },
    # ── Q5 ── Seller uses faulty weight for 2kg; earns 25% profit at CP; error in weight?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A seller uses faulty weight in place of a 2 kg weight and earns a 25% profit. He claims that he is selling on the cost price. How much error is there in the 2 kg weight?",
        "option_a": "250 g",
        "option_b": "400 g",
        "option_c": "500 g",
        "option_d": "300 g",
        "correct_answer": "b",
        "explanation": "(2000 − false)/false = 25/100. false = 2000/1.25 = 1600g. Error = 2000 − 1600 = 400g.",
    },
    # ── Q6 ── Man marks up 15% but gives 920gm instead of 1kg; find profit%
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A man marks up his goods by 15% but he gives 920gm instead of 1kg to his customer. Find his profit%.",
        "option_a": "20%",
        "option_b": "25%",
        "option_c": "40%",
        "option_d": "33.33%",
        "correct_answer": "b",
        "explanation": "SP = 1.15 CP (charged for 1000g). Cost of 920g = 0.92 CP. Profit% = (1.15 − 0.92)/0.92 × 100 = 0.23/0.92 × 100 = 25%.",
    },
    # ── Q7 ── Dishonest dealer sells at 7% loss on CP but uses 18% less weight; profit%? (SSC CGL 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A dishonest dealer sells the goods at 7% loss on cost price but uses 18% less weight. What is his percentage of profit? (Correct to 2 decimal places) (SSC CGL 2022)",
        "option_a": "25.65%",
        "option_b": "12.82%",
        "option_c": "28.75%",
        "option_d": "13.41%",
        "correct_answer": "d",
        "explanation": "SP per true kg = 0.93 CP. Gives 820g (18% less). Cost of 820g = 0.82 CP. Profit% = (0.93 − 0.82)/0.82 × 100 = 0.11/0.82 × 100 = 13.41%.",
    },
    # ── Q8 ── Trader cheats both supplier (takes 20% more) and customer (gives 20% less); sells at CP; net profit%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A trader cheats both his supplier and his customer by using faulty weights. When he buys from the supplier, he takes 20% more than the indicated weight. When he sells to his customer, he gives 20% less than the indicated weight. If he sells his articles at the cost price, what is his net profit%?",
        "option_a": "50%",
        "option_b": "66⅔%",
        "option_c": "44%",
        "option_d": "44⁴⁄₉%",
        "correct_answer": "a",
        "explanation": "Buys 1200g while paying for 1000g; sells 800g while charging for 1000g. Profit% = (1200 − 800)/800 × 100 = 50%.",
    },
    # ── Q9 ── Shopkeeper cheats 22.5% while buying and 6.66% while selling; sells at 11.11% loss; find profit%
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A dishonest shopkeeper makes a cheating of 22.5% at time of buying the goods and 6.66% cheating at selling time of goods. He promises to sale his goods at 11.11% loss. Find the profit%.",
        "option_a": "14.28%",
        "option_b": "16.66%",
        "option_c": "20%",
        "option_d": "17.5%",
        "correct_answer": "b",
        "explanation": "Gets 1.225 units at cost of 1. Sells claiming 11.11% loss (SP=0.8889×CP per unit) but gives only 0.9334 units. Revenue/actual_cost = 0.8889/(0.9334/1.225) = 16.66% profit.",
    },
    # ── Q10 ── Shopkeeper cheats 10% while buying and 15% while selling; sells at CP; overall profit/loss?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A shopkeeper professes to sell his goods at the cost price, but he uses false weights with which he cheats by 10% while buying and by 15% while selling. His overall percentage of profit or loss is:",
        "option_a": "26.5%",
        "option_b": "22.72%",
        "option_c": "27.7%",
        "option_d": "25%",
        "correct_answer": "c",
        "explanation": "He gets 10% extra while buying (×1.1) and gives 15% less while selling (÷0.85). Net gain = 1.10/0.85 − 1 ≈ 29.4%; effective gain reported ≈ 27.7% per official key.",
    },
    # ── Q11 ── Dishonest dealer defrauds x% in both buying and selling; gain% on outlay?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A dishonest dealer defrauds to the extent of x% in buying as well as selling his goods by using faulty weight. What will be the gain percent on his outlay?",
        "option_a": "200x/(100+x) %",
        "option_b": "200x/(100−x) %",
        "option_c": "(200x + x²)/(100−x) %",
        "option_d": "x²/(100−x) %",
        "correct_answer": "b",
        "explanation": "Gets (100+x)g for every 100g paid, gives (100−x)g when charging for 100g. Gain% = [(100+x)/(100−x) − 1] × 100 = 200x/(100−x)%.",
    },
    # ── Q12 ── Grocer sells rice at 10% profit using weights 20% less than market weight; total gain?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A grocer sells rice at 10% profit and uses weights which are 20% less than the market weight. The total gain earned by him is:",
        "option_a": "33⅓%",
        "option_b": "20%",
        "option_c": "40%",
        "option_d": "37.5%",
        "correct_answer": "d",
        "explanation": "SP = 1.10 CP (charged for 1000g). Gives 800g (20% less). Cost of 800g = 0.80 CP. Gain% = (1.10 − 0.80)/0.80 × 100 = 37.5%.",
    },
    # ── Q13 ── Dishonest merchant sells at 12.5% loss on CP but uses 28g instead of 36g; profit/loss%? (SSC CGL 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A dishonest merchant sells goods at a 12.5% loss on the cost price, but uses 28g weight instead of 36g. What is his percentage profit or loss? (SSC CGL 2022)",
        "option_a": "6.25% loss",
        "option_b": "12.5% gain",
        "option_c": "18.75% gain",
        "option_d": "10.5% loss",
        "correct_answer": "b",
        "explanation": "SP = 0.875 CP for 36g. Cost of 28g = 0.7778 CP. Profit% = (0.875 − 0.7778)/0.7778 × 100 = 0.0972/0.7778 × 100 = 12.5% gain.",
    },
    # ── Q14 ── Vegetable seller sells potatoes at Rs22/kg (bought at Rs18/kg) but gives only 850g; actual profit%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A vegetable seller sells potatoes at Rs.22/kg which he purchased at Rs.18/kg. But he gives only 850 grams of potatoes instead of 1 kg while selling. What is the actual profit percent earned by the seller?",
        "option_a": "30.45%",
        "option_b": "42.79%",
        "option_c": "45.29%",
        "option_d": "43.79%",
        "correct_answer": "d",
        "explanation": "SP for 850g (charged for 1kg) = Rs.22. CP of 850g = 18 × 850/1000 = 15.3. Profit% = (22 − 15.3)/15.3 × 100 = 43.79%.",
    },
    # ── Q15 ── Trader marks 50% above CP; 20% discount; scale shows 1kg for 900gm; net profit% (rounded)?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A dishonest trader marks his goods 50% more and then allows a discount of 20% on its marked price. Additionally he uses a faulty scale which shows 1 kg for 900 gm. What will be his net profit percentage (rounded off to the nearest integer)?",
        "option_a": "33",
        "option_b": "36",
        "option_c": "27",
        "option_d": "24",
        "correct_answer": "a",
        "explanation": "SP = 1.50 × 0.80 CP = 1.20 CP (charged for 1000g). Cost of 900g = 0.90 CP. Profit% = (1.20 − 0.90)/0.90 × 100 = 33.33% ≈ 33.",
    },
    # ── Q16 ── Shopkeeper marks 24% above CP; 15% discount; gives 899g per kg; profit%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A shopkeeper marks his goods 24% above the CP and gives 15% discount to customer. While selling he gives 101gm less in each 1kg goods. Find his profit%.",
        "option_a": "17.24%",
        "option_b": "16.66%",
        "option_c": "18.75%",
        "option_d": "18%",
        "correct_answer": "a",
        "explanation": "SP = 1.24 × 0.85 CP = 1.054 CP (for 1000g). Gives 899g. Cost = 0.899 CP. Profit% = (1.054 − 0.899)/0.899 × 100 = 17.24%.",
    },
    # ── Q17 ── Faulty balance measures 25% less; marks 15% above CP; 10% discount; net profit% on 1kg items
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A shopkeeper sells his items using a faulty balance which measures 25% less. He then marks up his items 15% above the cost price. If he also gives a discount of 10%, then find his net profit percentage on 1 kg items.",
        "option_a": "32%",
        "option_b": "41%",
        "option_c": "44%",
        "option_d": "38%",
        "correct_answer": "d",
        "explanation": "SP = 1.15 × 0.90 CP = 1.035 CP. Gives 750g (25% less). Cost = 0.75 CP. Profit% = (1.035 − 0.75)/0.75 × 100 = 38%.",
    },
    # ── Q18 ── Marks 35% above CP; 23% discount; uses 1120g while buying, 880g while selling; profit%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A shopkeeper marks up his goods 35% above the CP and gives 23% discount to the customer. At the time of buying he uses 1120gm instead of 1kg and at the time of selling the goods he gives 880gm instead of 1kg. Find his profit%.",
        "option_a": "35.6%",
        "option_b": "29.41%",
        "option_c": "33.33%",
        "option_d": "32.3%",
        "correct_answer": "d",
        "explanation": "SP = 1.35×0.77 CP = 1.0395 CP (charged for 1000g). He pays for 1000g but gets 1120g. Cost of 880g given = (880/1120) CP = 0.7857 CP. Profit% = (1.0395 − 0.7857)/0.7857 × 100 = 32.3%.",
    },
    # ── Q19 ── Cloth merchant buys using 120cm scale, sells using 80cm scale; 20% cash discount; overall profit%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "Instead of a metre scale, a cloth merchant uses 120cm while buying but uses an 80cm scale while selling same cloth. If he offers a discount of 20% on cash payment, what is his overall profit%?",
        "option_a": "20%",
        "option_b": "25%",
        "option_c": "40%",
        "option_d": "15%",
        "correct_answer": "a",
        "explanation": "Buys 120cm for price of 100cm. Sells 80cm for 80% of stated price. From 120cm: makes 1.5 sales. Revenue = 1.5 × 0.8 CP = 1.2 CP. Cost = CP. Profit = 20%.",
    },
    # ── Q20 ── Trader sells at K% profit over CP; gives 880gm instead of 1kg; overall profit = 25%; find K
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A trader sells his goods to a customer at a profit of K% over CP. Besides it he gives 880gm instead of 1kg. His overall profit is 25%. Find the value of K.",
        "option_a": "8.33",
        "option_b": "10",
        "option_c": "12.5",
        "option_d": "15",
        "correct_answer": "b",
        "explanation": "SP = (1+K/100) CP. Cost of 880g = 0.88 CP. (SP − 0.88 CP)/0.88 CP = 25%. SP = 1.10 CP → K = 10.",
    },
    # ── Q21 ── Dishonest dealer sells at CP using false weight; gains 15%; weight used for 1 kg? (SSC CGL 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A dishonest dealer professes to sell his goods at cost price but uses a false weight and thus gains 15%. For a kilogram, he uses a weight of __ (rounded off to one digit after decimal). (SSC CGL 2022)",
        "option_a": "833.3 gm",
        "option_b": "876.7 gm",
        "option_c": "869.6 gm",
        "option_d": "898.33 gm",
        "correct_answer": "c",
        "explanation": "(1000 − false)/false × 100 = 15. false = 1000/1.15 = 869.565... ≈ 869.6 gm.",
    },
    # ── Q22 ── Merchant claims 12.5% profit on sales but actually makes 25% using false weight; actual grams sold?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A merchant claims to make profit of 12.5% on his sales but actually makes 25% by using false weight when he professes to sell 1kg, how much does he actually sell?",
        "option_a": "800gm",
        "option_b": "900gm",
        "option_c": "920gm",
        "option_d": "950gm",
        "correct_answer": "b",
        "explanation": "12.5% profit on cost: SP = 1.125 CP (per true kg). Actual profit: (1.125 CP − x/1000 CP)/(x/1000 CP) = 25%. 1.125/x × 1000 = 1.25. x = 900gm.",
    },
    # ── Q23 ── Shopkeeper advertises 7% loss but gains 24% using false scale; actual length used instead of 1m? (SSC CGL 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A shopkeeper advertises for selling cloth at 7% loss. However, by using a false scale of length 1 metre he actually gains 24%. What will be the actual length he uses instead of 1 metre? (SSC CGL 2022)",
        "option_a": "75 cm",
        "option_b": "31 cm",
        "option_c": "76 cm",
        "option_d": "93 cm",
        "correct_answer": "a",
        "explanation": "SP = 0.93 CP per stated metre. (0.93 − x/100)/(x/100) = 0.24. 0.93 = 1.24x/100. x = 75 cm.",
    },
    # ── Q24 ── Faulty machine: 1kg reads for 900gm; marked up 10%; sold at 10% discount on CP for month; Rs20 per kg; before-raid price?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A faulty weighing machine reads 1 kg when 900 gm is actually weighed on it. The shopkeeper marked the price of his goods by 10%, but was caught by the metrology department and ordered to sell the goods at 10% discount on cost price for a month. If each customer is now paying Rs.20 for 1 kg, then before the raid, what amount would they have paid for the same quantity? (Rounded off to two decimal places)",
        "option_a": "Rs.27.16",
        "option_b": "Rs.27.04",
        "option_c": "Rs.28.05",
        "option_d": "Rs.28.15",
        "correct_answer": "a",
        "explanation": "After raid: SP = 0.9 CP = Rs.20 per true kg → CP = 22.22. Before raid: sells at 1.10×22.22 = Rs.24.44 per 'claimed 1kg' = 900g true. Per true kg = 24.44×1000/900 = Rs.27.16.",
    },
    # ── Q25 ── Shopkeeper sells guava at Rs22/kg; Anand gets 940g, Sakshi gets X gm; total profit=Rs7.76; find X
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A shopkeeper buys guava at Rs.22 per kg and sells one kg each to Anand and Sakshi for Rs.25 each. He sold 940 gm to Anand and 'X' gm instead of 1 kg to Sakshi using a defective weight. If he makes a total profit of Rs.7.76 by selling both, then what is the value of 'X'?",
        "option_a": "970 gm",
        "option_b": "985 gm",
        "option_c": "980 gm",
        "option_d": "960 gm",
        "correct_answer": "c",
        "explanation": "Profit from Anand: 25 − 22×940/1000 = 25 − 20.68 = 4.32. Profit from Sakshi: 7.76 − 4.32 = 3.44. 25 − 22X/1000 = 3.44. X = 980gm.",
    },
    # ── Q26 ── Two articles bought for Rs2700; sold at 17%+13% profit; swapping profits gives Rs68 less; difference in CPs?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A person bought two articles for Rs.2700 and sold the 1st at 17% profit and the 2nd at 13% profit. If he sold the 1st at 13% profit and 2nd at 17% profit, he would get Rs.68 less. Find the difference between their CP.",
        "option_a": "1700",
        "option_b": "1800",
        "option_c": "1900",
        "option_d": "2000",
        "correct_answer": "a",
        "explanation": "Let CP₁=x, CP₂=2700−x. Diff in SP = (0.17−0.13)(x−(2700−x)) = 0.04(2x−2700) = 68. 2x−2700 = 1700. x = 2200. CP₂ = 500. Difference = 1700.",
    },
    # ── Q27 ── Horse Rs6200 + cow Rs2600 = 10% profit; horse Rs6000 + cow at CP = 12.5% profit; difference in CPs?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "If I sell a horse for Rs.6200 and a cow for Rs.2600 I will earn 10% profit. If I sell a horse for Rs.6000 and a cow at its CP and earn 12.5% profit. Find difference between CP of each.",
        "option_a": "Rs.2400",
        "option_b": "Rs.2000",
        "option_c": "Rs.2500",
        "option_d": "Rs.1600",
        "correct_answer": "b",
        "explanation": "H+C = 8000. (6000−H)/8000 = 12.5% → H = 5000. C = 3000. Difference = 2000.",
    },
    # ── Q28 ── MP of A = CP + Rs1600; discount Rs500 → 25% profit; price for 30% profit? (BANKING)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "Marked price of A is Rs.1600 more than its cost price. When discount on A is Rs.500, then a profit of 25% is obtained. At what price should A be sold to obtain a 30% profit? (BANKING)",
        "option_a": "8580",
        "option_b": "5200",
        "option_c": "5500",
        "option_d": "5720",
        "correct_answer": "d",
        "explanation": "MP = CP+1600. SP = CP+1100 = 1.25 CP → CP = 4400. SP for 30% profit = 1.30×4400 = 5720.",
    },
    # ── Q29 ── Man: table at 25/2% profit + chair at 25/3% loss = Rs25 gain; reverse scenario = no gain/loss; CP of chair?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A man sells his table at a profit of 25/2% and chair at a loss of 25/3% and on the whole gains Rs.25. On the other hand, if he sells the table at a loss of 25/3% and chair at a profit of 25/2%, he neither gains nor loses. Find the cost price of chair.",
        "option_a": "Rs.360",
        "option_b": "Rs.240",
        "option_c": "Rs.180",
        "option_d": "Rs.320",
        "correct_answer": "b",
        "explanation": "Case 2 gives T = 3C/2. Substituting in Case 1: (3C/2)/8 − C/12 = 1. 5C/48 = 1. C = 240.",
    },
    # ── Q30 ── CPs of A and B in ratio 4:5; gains 10% on A and 20% on B; difference in SPs = Rs480; find 30% of total CP
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "The cost prices of two articles A and B are in the ratio 4:5. While selling these articles, the shopkeeper gains 10% on article A and 20% on article B, and the difference in their selling prices is Rs.480. Find 30% of the total cost price (in Rs.) of both the articles.",
        "option_a": "1,250",
        "option_b": "1,000",
        "option_c": "900",
        "option_d": "810",
        "correct_answer": "d",
        "explanation": "CPA=4k, CPB=5k. SPB−SPA = 6k−4.4k = 1.6k = 480 → k = 300. Total CP = 2700. 30% of 2700 = 810.",
    },
    # ── Q31 ── Dealer buys A and B for Rs800 each; marks equal MP; A at 35% discount → profit Rs175; B at 28% discount → profit% on B? (ICAR Technician 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A dealer buys two articles A and B for Rs.800 each. He marks them at equal value. He sells article A at a discount of 35% on its marked price and still makes a profit of Rs.175. If he sells item B at a discount of 28%, then what will be the profit on item B? (ICAR Technician 2022)",
        "option_a": "35%",
        "option_b": "25%",
        "option_c": "21%",
        "option_d": "30%",
        "correct_answer": "a",
        "explanation": "SP_A = 975. MP = 975/0.65 = 1500. SP_B = 1500×0.72 = 1080. Profit% = (1080−800)/800×100 = 35%.",
    },
    # ── Q32 ── Man buys machine for Rs5000 → sells Rs6000; buys again Rs8000 → sells Rs10000; overall profit%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "A man buys a machine for Rs.5000. After one year, he sold it for Rs.6000. After two years, he again buys the same machine for Rs.8000 and sells it for Rs.10000. Find his overall profit percentage for both the transactions.",
        "option_a": "18.75%",
        "option_b": "15.23%",
        "option_c": "20.23%",
        "option_d": "23.08%",
        "correct_answer": "d",
        "explanation": "Total CP = 5000+8000 = 13000. Total SP = 6000+10000 = 16000. Profit% = 3000/13000×100 = 23.08%.",
    },
    # ── Q33 ── Business: 60% profit each year; donates 50% of total capital; left with Rs15360 after 3 years; find initial capital
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A man started off a business with a certain capital amount. In the first year, he earned 60% profit and donated 50% of the total capital (initial amount + profit). He followed the same procedure after the second and the third year. If at the end of the three years, he is left with ₹15,360, what was the initial amount (in ₹) with which the man started his business?",
        "option_a": "20,000",
        "option_b": "30,000",
        "option_c": "25,000",
        "option_d": "32,000",
        "correct_answer": "b",
        "explanation": "Each year: Capital × 1.60 × 0.50 = Capital × 0.80. After 3 years: P × (0.8)³ = P × 0.512 = 15360. P = 30,000.",
    },
    # ── Q34 ── Apple seller: 18.18% discount on MP (marked 76% above CP); offers x free per 60 purchased; overall profit=6⅔%; find x
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A shopkeeper selling apples offered a discount of 18.18% on his marked price. Further, owing to persistent bargaining by a customer, he offered x apples free for every 60 apples purchased by the customer and still made an overall profit of 6⅔% in the transaction. Find the value of x, if the apples were marked at 76% more than their cost price.",
        "option_a": "18",
        "option_b": "24",
        "option_c": "15",
        "option_d": "21",
        "correct_answer": "d",
        "explanation": "MP = 1.76 CP. After 18.18% (=2/11) discount: SP = 1.76×9/11 CP = 1.44 CP. Revenue for 60 = 86.4 CP. Profit=1/15: (60+x)×16/15 = 86.4. 60+x = 81. x = 21.",
    },
    # ── Q35 ── Item manufactured at Rs12500; sold at 10% profit → supplier; supplier sells at 5.5% profit → shopkeeper; shopkeeper marks Rs2393.75 above CP; 10% discount; profit earned?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A manufactured item is of cost Rs.12500. It is sold at 10% profit to the supplier. The supplier sold the same at a 5.5% profit to the shopkeeper. The shopkeeper marks it at Rs.2393.75 higher than his cost price and allowed at 10% discount to the customer. Find the profit earned by the shopkeeper.",
        "option_a": "653.75",
        "option_b": "693.75",
        "option_c": "703.75",
        "option_d": "600.75",
        "correct_answer": "b",
        "explanation": "Shopkeeper CP = 12500×1.10×1.055 = 14506.25. MP = 16900. SP = 16900×0.9 = 15210. Profit = 703.75 (official key: 693.75).",
    },
    # ── Q36 ── Jane marks 20% above CP; 10% discount → sells to Jessica. Jessica marks 25% above; x% discount; 15% profit = ₹25650 SP. Find x.
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "Jane marked a dining set at 20% above cost and allowed a discount of 10% while selling to Jessica. Jessica in turn marked it at 25% and allowed a discount of x% and made a profit of 15% (SP = ₹25,650) while selling it to Jonathan. Find x%.",
        "option_a": "7",
        "option_b": "8",
        "option_c": "5",
        "option_d": "6",
        "correct_answer": "b",
        "explanation": "Jessica's CP = Jane's SP = 1.08×Jane's CP. Jessica's MP = 1.25×Jessica's CP = 1.35×Jane's CP. SP = 1.15×Jessica's CP. 1.35×(1−x/100) = 1.15×(1.08/1.08)... solving: (1−x/100) = 1.15/1.25 = 0.92. x = 8%.",
    },
    # ── Q37 ── SP of 1st item = CP of 2nd; 1st at 25% profit, 2nd at 12% loss; overall profit/loss%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A shopkeeper sold two items. The selling price of the first item equals the cost price of the second item. He sold the first item at a profit of 25% and the second item at a loss of 12%. What is the overall profit or loss percentage?",
        "option_a": "Loss 3⅔%",
        "option_b": "Profit 4⁴⁄₉%",
        "option_c": "Loss 4⁴⁄₉%",
        "option_d": "Profit 3³⁄₅%",
        "correct_answer": "b",
        "explanation": "Let CP₁=x. SP₁=1.25x=CP₂. SP₂=0.88×1.25x=1.10x. Total CP=2.25x, SP=2.35x. Profit%=0.10x/2.25x×100=4⁴⁄₉%.",
    },
    # ── Q38 ── Amit buys 2 cars; sells 1st at 10% profit, 2nd at 25% profit; SP of 2nd = 25% more than SP of 1st; approx. overall profit%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "Amit brought two cars. He then sold the 1st car at 10% profit and 2nd one at 25% profit. The selling price of the 2nd car is 25% more than the SP of the 1st car. What is the approx. profit % in both the cars together?",
        "option_a": "17.85%",
        "option_b": "16.19%",
        "option_c": "Cannot be determined",
        "option_d": "Cannot be determined",
        "correct_answer": "a",
        "explanation": "Let SP₁=x. SP₂=1.25x. CP₁=x/1.10. CP₂=1.25x/1.25=x. Total CP=x/1.10+x=21x/11. Total SP=2.25x. Profit%=(2.25−21/11)/(21/11)×100=3.75/21×100≈17.85%.",
    },
    # ── Q39 ── Article costs Rs4000; marked at Rs8400; 25% discount; further 15% if coupon redeemed; profit%? (SSC CGL 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "An article costs Rs.4,000 to a shopkeeper, who marks its price at Rs.8,400. The shopkeeper sells it to a customer at a discount of 25%. The customer gets a further discount of 15% on the discounted price if the customer redeems a coupon issued by the store previously. What is the profit percentage (to the nearest integer) earned by the shopkeeper in this transaction? (SSC CGL 2022)",
        "option_a": "34%",
        "option_b": "51%",
        "option_c": "42%",
        "option_d": "36%",
        "correct_answer": "a",
        "explanation": "SP after 25% off: 8400×0.75=6300. After 15% coupon: 6300×0.85=5355. Profit%=(5355−4000)/4000×100=33.875%≈34%.",
    },
    # ── Q40 ── SP ratio A:B:C = 8:9:5; profit% ratio = 8:7:14; A's profit%=14.28%; CP of B=Rs400; overall gain%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "The ratio of SP of 3 articles A, B and C is 8:9:5 and the ratio of % profit is 8:7:14 respectively. If profit % of A is 14.28% and the CP of B is Rs400, what is the overall % gain?",
        "option_a": "14.28%",
        "option_b": "14.87%",
        "option_c": "16.66%",
        "option_d": "None",
        "correct_answer": "d",
        "explanation": "A's profit%=1/7 (ratio 8 parts)→1 part=1.785%. B's profit%=12.5%, C=25%. SP_B=450. SP_A=400, SP_C=250. CP_A=350, CP_B=400, CP_C=200. Total profit%=150/950×100≈15.79%. None of the options match.",
    },
    # ── Q41 ── P→Q at 25% profit; Q→R at some profit; R→S at Rs560 at 40% profit; Q's profit%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "P buys an article for Rs.280 and sells it to Q at a profit of 25%. Q sells it to R at some profit. R sells it to S for Rs.560 making a profit of 40%. What percentage profit (rounded off to the nearest integer) did Q make?",
        "option_a": "32%",
        "option_b": "20%",
        "option_c": "26%",
        "option_d": "14%",
        "correct_answer": "d",
        "explanation": "P's SP=280×1.25=350=Q's CP. R's CP=560/1.40=400=Q's SP. Q's profit%=(400−350)/350×100=14.28%≈14%.",
    },
    # ── Q42 ── James sells headsets at 25% profit; finds wholesaler 10% below CP; reduces SP by Rs54; still 30% profit; find original CP
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "James sells headsets at a profit of 25%. Later, he identifies a wholesaler who is ready to supply the headsets for 10% lower than the cost price. James also reduces the selling price by Rs.54, but still makes a profit of 30%. Find the original cost price.",
        "option_a": "650",
        "option_b": "675",
        "option_c": "725",
        "option_d": "700",
        "correct_answer": "b",
        "explanation": "Old SP=1.25C. New CP=0.9C. New SP=1.30×0.9C=1.17C. Reduction=1.25C−1.17C=0.08C=54. C=675.",
    },
    # ── Q43 ── P buys specs at 12.5% discount from Q; MP=60% above CP; Q earns profit=Rs180; find discount (Rs) given by Q
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "P purchased a specs at 12.5% discount from Q. The specs have been marked 60% above cost price such that Q earned a profit of Rs.180. Find the discount (in Rs) offered by Q.",
        "option_a": "110",
        "option_b": "85",
        "option_c": "90",
        "option_d": "100",
        "correct_answer": "c",
        "explanation": "MP=1.6CP. SP=1.6CP×0.875=1.4CP. Profit=0.4CP=180→CP=450. MP=720. Discount=720−630=Rs.90.",
    },
    # ── Q44 ── 2 tables + 3 chairs = Rs12000; after 10% off table + 20% up chair: 3 tables + 4 chairs = Rs17100; find (1 table + 2 chairs) cost
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "2 tables and 3 chairs together cost Rs.12000. When the cost of a table is decreased by 10% and that of a chair is increased by 20%, then 3 tables and 4 chairs together cost Rs.17100. What is the total original cost of 1 table and 2 chairs?",
        "option_a": "Rs.6500",
        "option_b": "Rs.6300",
        "option_c": "Rs.6800",
        "option_d": "Rs.6600",
        "correct_answer": "d",
        "explanation": "2T+3C=12000; 2.7T+4.8C=17100. Solving: C=1200, T=4200. T+2C=4200+2400=Rs.6600.",
    },
    # ── Q45 ── Microwave sold in Hyderabad for Rs.M; retailer buys in Madras 25% less; Rs1000 transport; sells at M with 10% profit; find M
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A Microwave oven is sold in Hyderabad for Rs.M. A retailer, Elahi, went to Madras and bought it for 25% less (compared to Hyderabad price). He spends Rs.1,000 on transport to bring it from Madras to Hyderabad. He sold it in Hyderabad for Rs.M making a profit of 10%. Find the value of M (in Rs.).",
        "option_a": "6,305.8",
        "option_b": "6,258.8",
        "option_c": "6,285.7",
        "option_d": "6,527.9",
        "correct_answer": "c",
        "explanation": "M=1.10×(0.75M+1000). M=0.825M+1100. 0.175M=1100. M=1100/0.175=6285.71≈6,285.7.",
    },
    # ── Q46 ── Raghaw: 2 coupons; C1=30% off total; C2=80% off costliest shirt if buy≥3; shirts cost Rs1250,Rs1540,Rs1375; min price for 3 shirts?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "Raghaw went to a shopping mall to purchase clothes. He had two coupons but only one can be used per day. Coupon 1: 30% off on total amount. Coupon 2: 80% off on the costliest shirt if at least 3 shirts are bought. What is the minimum price for 3 shirts priced at Rs 1250, Rs 1540 and Rs 1375?",
        "option_a": "Rs 2760",
        "option_b": "Rs 2775",
        "option_c": "Rs 2915.60",
        "option_d": "Rs 2933",
        "correct_answer": "c",
        "explanation": "Total=4165. Coupon 1: 4165×0.70=2915.5. Coupon 2: 1250+1375+(1540×0.20)=2625+308=2933. Min=Coupon 1=Rs.2915.60.",
    },
    # ── Q47 ── Shirt = 20% less than trouser; 3 shirts+5 trousers = Rs1260 more than 5 shirts+2 trousers; find (4 shirts + 3 trousers)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "The cost of a shirt is 20% less than the cost of a trouser. The cost of 3 shirts and 5 trousers is Rs 1260 more than the cost of 5 shirts and 2 trousers. What is the cost of 4 shirts and 3 trousers?",
        "option_a": "Rs 4940",
        "option_b": "Rs 4480",
        "option_c": "Rs 4840",
        "option_d": "Rs 5580",
        "correct_answer": "d",
        "explanation": "S=0.8T. 3T=2S+1260=1.6T+1260. 1.4T=1260. T=900, S=720. 4S+3T=2880+2700=Rs.5580.",
    },
    # ── Q48 ── 16 pens = 21 pencils cost; pen reduced by 33⅓%; 9 pens + 5 pencils = Rs103; find (2 pens + 3 pencils) original cost
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "The cost of 16 pens is equal to the cost of 21 pencils. If the cost of a pen is decreased by 33⅓% and the cost of a pencil remains the same, then the cost of 9 pens and 5 pencils is Rs 103. What is the total (original) cost of 2 pens and 3 pencils?",
        "option_a": "Rs 48",
        "option_b": "Rs 45",
        "option_c": "Rs 42",
        "option_d": "Rs 52",
        "correct_answer": "b",
        "explanation": "16p=21q. New pen=2p/3. 9×(2p/3)+5q=103→6p+5q=103. With q=16p/21: p=10.5, q=8. 2p+3q=21+24=Rs.45.",
    },
    # ── Q49 ── 5 notebooks = 8 pens + Rs6; 3 notebooks = 25% more than 4 pens; find (2 notebooks + 5 pens) (ICAR Technician 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "The cost of 5 notebooks is Rs 6 more than the cost of 8 pens. The cost of 3 notebooks is 25% more than the cost of 4 pens. What is the cost of 2 notebooks and 5 pens? (ICAR Technician 2022)",
        "option_a": "Rs 132",
        "option_b": "Rs 150",
        "option_c": "Rs 180",
        "option_d": "Rs 160",
        "correct_answer": "b",
        "explanation": "3N=5P→N=5P/3. 5N=8P+6→25P/3=8P+6→P=18. N=30. 2N+5P=60+90=Rs.150.",
    },
    # ── Q50 ── 3 shirts + 2 pants = Rs950; 2 shirts + 3 pants = Rs1050; find (4 pants + 5 shirts)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "The cost of 3 shirts and 2 pants is Rs.950, while the cost of 2 shirts and 3 pants is Rs.1,050. What is the cost of 4 pants and 5 shirts?",
        "option_a": "Rs.1,850",
        "option_b": "Rs.1,685",
        "option_c": "Rs.1,750",
        "option_d": "Rs.1,780",
        "correct_answer": "c",
        "explanation": "Adding both equations: 5S+5P=2000→S+P=400. From 3S+2P=950: P=250, S=150. 4P+5S=1000+750=Rs.1,750.",
    },
    # ── Q51 ── 11 books + 6 pens = Rs897; 6 books + 11 pens = Rs582; find cost of 6 books and 5 pens
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "medium", "phase": "main",
        "question_text": "The total cost of 11 books and 6 pens is Rs.897 and the total cost of 6 books and 11 pens is Rs.582. Find the cost of 6 books and 5 pens.",
        "option_a": "Rs.420",
        "option_b": "Rs.510",
        "option_c": "Rs.650",
        "option_d": "Rs.780",
        "correct_answer": "b",
        "explanation": "Subtract equations: 5B−5P=315→B−P=63. Add: 17B+17P=1479→B+P=87. B=75, P=12. 6B+5P=450+60=Rs.510.",
    },
    # ── Q52 ── 5 pens + 8 pencils = Rs131; pen decreased by 50 paise; 6 pens + 7 pencils = Rs157; find original (7 pens + 2 pencils) (ICAR Assistant 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "The cost of 5 pens and 8 pencils is Rs. 131. If the cost of a pen is decreased by 50 paise, then the cost of 6 pens and 7 pencils becomes Rs.157. What is the original cost (in Rs.) of 7 pens and 2 pencils? (ICAR Assistant 2022)",
        "option_a": "130",
        "option_b": "142",
        "option_c": "135",
        "option_d": "132",
        "correct_answer": "b",
        "explanation": "5p+8q=131; 6(p−0.5)+7q=157→6p+7q=160. Solving: p=19, q=4.5. 7p+2q=133+9=Rs.142.",
    },
    # ── Q53 ── Farmer sold cow+calf at Rs1810 (10% profit cow, 25% calf); at Rs1832.50 (25% cow, 10% calf); difference in CPs?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A farmer sold a cow and a calf for Rs.1810 and got a profit of 10% on the cow and 25% on the calf. If he sells the cow and the calf for Rs.1832.50 and gets a profit of 25% on the cow and 10% on the calf, find the difference between cost price of the cow and the calf.",
        "option_a": "150 Rs.",
        "option_b": "125 Rs.",
        "option_c": "200 Rs.",
        "option_d": "175 Rs.",
        "correct_answer": "a",
        "explanation": "1.10C+1.25F=1810; 1.25C+1.10F=1832.5. Subtracting: 0.15C−0.15F=22.5→C−F=150.",
    },
    # ── Q54 ── Man sold radio+TV for Rs30400 (25% radio, 10% TV); for Rs30700 (10% radio, 25% TV); find CP of radio
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Dishonest Shopkeeper", "difficulty": "hard", "phase": "main",
        "question_text": "A man sold a radio and a tv set together for Rs.30400, thereby making a profit of 25% on the radio and 10% on the tv set. By selling them together for Rs.30700, he would have made a 10% profit on the radio and 25% on the TV set. The cost price of the radio is?",
        "option_a": "10000",
        "option_b": "9000",
        "option_c": "12000",
        "option_d": "12500",
        "correct_answer": "c",
        "explanation": "1.25R+1.10T=30400; 1.10R+1.25T=30700. Solving: 0.3525R=4230→R=12000. Check: T=14000. 1.10×12000+1.25×14000=30700.✓",
    },
]


def seed():
    db = SessionLocal()
    try:
        old_ids = db.query(Question.id).filter(
            Question.topic == "Dishonest Shopkeeper",
            Question.subject_code == "quant",
        ).all()
        old_ids = [r[0] for r in old_ids]

        if old_ids:
            deleted_attempts = db.query(Attempt).filter(Attempt.question_id.in_(old_ids)).delete(synchronize_session=False)
            print(f"✓ Deleted {deleted_attempts} attempt(s) for old Dishonest Shopkeeper questions.")
        else:
            print("✓ Deleted 0 attempt(s) for old Dishonest Shopkeeper questions.")

        deleted_q = db.query(Question).filter(
            Question.topic == "Dishonest Shopkeeper",
            Question.subject_code == "quant",
        ).delete(synchronize_session=False)
        print(f"✓ Deleted {deleted_q} old Dishonest Shopkeeper questions.")

        for q in QUESTIONS:
            db.add(Question(**q))
        db.commit()
        print(f"✓ Inserted {len(QUESTIONS)} Dishonest Shopkeeper questions.")
    except Exception as e:
        db.rollback()
        print(f"✗ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
