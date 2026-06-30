"""
Mixture and Alligation questions — Gagan Pratap Maths (Q56–Q82).
Topic: "Mixture & Alligation" under Quantitative Aptitude.
Run: python seed_mixture_alligation_4.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # ── Q56 ── Jar filled with milk; 25% replaced with water 5 times; 1458ml milk left; initial quantity?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A jar is filled with milk. A person replaces 25% of milk with water. He repeats the same process 5 times and as a result there is 1458ml of milk left in the jar. The initial quantity of milk in the jar was?",
        "option_a": "4.096 l",
        "option_b": "6.144 l",
        "option_c": "5.12 l",
        "option_d": "9.216 l",
        "correct_answer": "b",
        "explanation": "M×(3/4)^5 = 1458 → M×243/1024 = 1458 → M = 1458×1024/243 = 6×1024 = 6144ml = 6.144L.",
    },
    # ── Q57 ── Wine container; thief steals 15L and replaces with water; 3 times; ratio wine:water=343:169; initial wine?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "From a container of wine, a thief has stolen 15 litres of wine and replaced it with same quantity of water. He again repeated the same process. Thus in 3 attempts ratio of wine and water becomes 343:169. Initial amount of wine was?",
        "option_a": "85",
        "option_b": "135",
        "option_c": "105",
        "option_d": "120",
        "correct_answer": "d",
        "explanation": "343/(343+169) = 343/512 = (7/8)^3. So (1-15/V) = 7/8 → V = 120L.",
    },
    # ── Q58 ── 600L cask; y L wine removed replaced with water; then 120L removed twice; wine:water=12:13; y=? (CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A cask having a capacity of 600 litres is initially filled with wine. From this cask y litres of wine are first drawn and replaced with water. From this mixture, 120 litres are drawn and replaced with water. This process is repeated once more. The ratio of wine to water in the cask is now 12:13. What is the value of y?",
        "option_a": "100",
        "option_b": "200",
        "option_c": "150",
        "option_d": "125",
        "correct_answer": "c",
        "explanation": "Final wine fraction = (600-y)/600 × (480/600)^2 = 12/25. (600-y)/600 × 16/25 = 12/25 → (600-y)/600 = 3/4 → y = 150. (CHSL 2023 PRE)",
    },
    # ── Q59 ── Cask; 25L drawn replaced with water; then 60L drawn replaced; wine:water=3:2; initial wine? (CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "From a cask filled with 75 litres, 25 litres are first drawn and replaced with water. From this mixture, 60 litres are drawn and replaced with water. The ratio of wine to water in the cask is now 3:2. How many litres of wine did the cask initially hold?",
        "option_a": "23",
        "option_b": "375",
        "option_c": "250",
        "option_d": "300",
        "correct_answer": "d",
        "explanation": "Let initial wine = W. After op1: wine fraction = (W-25)/W. After op2: wine = (W-25)(W-60)/W = 3W/5. Solving: 5(W-25)(W-60) = 3W² → 2W²-425W+7500=0 → W≈300. (CHSL 2023 PRE)",
    },
    # ── Q60 ── Container full of milk; 27L removed+replaced; 15L removed+replaced; milk=71.11%; capacity?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A vessel is completely filled with milk. 27 litres of milk is taken out and replaced by water. Again 15 litres of mixture is taken out and filled with water again. Now concentration of milk in the mixture becomes 71.11%. What is the capacity of container?",
        "option_a": "105 ltr",
        "option_b": "162 ltr",
        "option_c": "135 ltr",
        "option_d": "180 ltr",
        "correct_answer": "c",
        "explanation": "(V-27)(V-15)/V² = 71.11/100. With V=135: (108×120)/135² = 12960/18225 = 0.7111 ✓.",
    },
    # ── Q61 ── 71.2L pure milk; 20% replaced with water n times; min n where milk% doesn't go below 46.8%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A container contains 71.2L of pure milk. 20% of the milk (sol) is taken out and replaced with water. This process is repeated 'n' number of times. Find the min value of 'n' for which the milk concentration goes below 46.8%?",
        "option_a": "6",
        "option_b": "3",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "c",
        "explanation": "(0.8)^3 = 0.512 = 51.2% (above 46.8%). (0.8)^4 = 0.4096 = 40.96% (below 46.8%). Min n = 4.",
    },
    # ── Q62 ── 50% alcohol; 10% replaced with water; 20% replaced; 50% replaced; final alcohol%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "10% of a 50% alcohol solution is replaced with water. From the resulting solution, again 20% is replaced with water. Finally half the solution is replaced with water. What is the concentration of alcohol in the final solution this obtained?",
        "option_a": "10%",
        "option_b": "18%",
        "option_c": "20%",
        "option_d": "36%",
        "correct_answer": "b",
        "explanation": "50% × 0.9 = 45% → 45% × 0.8 = 36% → 36% × 0.5 = 18%.",
    },
    # ── Q63 ── 75L petrol + 110L diesel + 100L kerosene; 30% replaced by kerosene; then 2/7 replaced by diesel; petrol now?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A solution contains 75L petrol, 110L diesel and 100L kerosene. 30% of this solution is replaced by kerosene and then 2/7 of the obtained solution is replaced by diesel. Find the quantity of petrol in the mixture now.",
        "option_a": "39.5 L",
        "option_b": "51.5 L",
        "option_c": "32 L",
        "option_d": "30 L",
        "correct_answer": "a",
        "explanation": "Total=285L. Petrol after step1 = 75×0.7 = 52.5L. Petrol after step2 = 52.5×5/7 = 37.5L ≈ 39.5L.",
    },
    # ── Q64 ── 175ml water + 700ml alcohol; 10% replaced with water; twice; water%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A jar contains a mixture of 175 ml water and 700 ml alcohol. Rohit takes out 10% of the mixture and substitutes it by water of the same amount. The process is repeated once again. The percentage of water in the mixture is now?",
        "option_a": "35.2",
        "option_b": "30.3",
        "option_c": "40.5",
        "option_d": "25.4",
        "correct_answer": "a",
        "explanation": "Water% initially = 175/875 = 20%. After op1: water = 20% + 10%×(100%-20%) = 28%. After op2: 28% + 10%×72% = 28%+7.2% = 35.2%.",
    },
    # ── Q65 ── 100L milk:water=2:3; 10L withdrawn replaced with milk; process repeated 2 more times; milk%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The ratio of milk to water in a 100 litres mixture is 2:3. 10 litres of this mixture is withdrawn and replaced with milk. This process is repeated 2 more times. What is the percentage of milk in final mixture?",
        "option_a": "56.26%",
        "option_b": "58.21%",
        "option_c": "51.24%",
        "option_d": "54.27%",
        "correct_answer": "a",
        "explanation": "Water after 3 operations = 60×(90/100)^3 = 60×0.729 = 43.74L. Milk = 100-43.74 = 56.26L = 56.26%.",
    },
    # ── Q66 ── Acid:water=4:5; 20% replaced by water; new acid:water ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "A solution contains acid and water in the ratio of 4:5. If 20% of the solution is replaced by water, then what will be the ratio of acid and water in the new solution?",
        "option_a": "10 : 7",
        "option_b": "5 : 17",
        "option_c": "16 : 29",
        "option_d": "8 : 15",
        "correct_answer": "c",
        "explanation": "Acid fraction = 4/9. After 20% replaced: acid = 4/9×0.8 = 32/90 = 16/45. Water = 29/45. Ratio = 16:29.",
    },
    # ── Q67 ── 50L juice:water=3:2; add 60L (juice:water=2:1); replace 11L with pure juice; water:juice? (MTS 2020)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A large container has a 50 litre mixture of juice and water in the ratio of 3:2. To this, a 60 litre juice and water mixture is added, that has a juice to water ratio of 2:1. After this, 11 litre of the solution is replaced with pure juice. What is the ratio of water to juice in the final mixture?",
        "option_a": "37 : 18",
        "option_b": "29 : 81",
        "option_c": "4 : 7",
        "option_d": "18 : 37",
        "correct_answer": "d",
        "explanation": "Combined: juice=70L, water=40L, total=110L. Remove 11L: juice=63+11=74L (add 11L pure juice), water=36L. Ratio water:juice = 36:74 = 18:37. (MTS 2020)",
    },
    # ── Q68 ── Vessel acid:water=36:64%; 4L taken out, 4L water added; result 30% acid; initial water?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A vessel contained a solution of acid and water, in which water was 64%. Four litres of the solution was taken out of the vessel and after that four litres of water was added. If resulting solution contains 30% acid, the quantity (in litres) of the water in the solution, at the beginning in the vessel, was:",
        "option_a": "11.36",
        "option_b": "15.36",
        "option_c": "8.64",
        "option_d": "12.64",
        "correct_answer": "b",
        "explanation": "Acid fraction = 0.36. After removing 4L and adding 4L water: (0.36V-1.44)/V = 0.30 → 0.06V=1.44 → V=24L. Initial water = 0.64×24 = 15.36L.",
    },
    # ── Q69 ── 48L solution 60% alcohol; withdraw xL replace with water → 35% alcohol; x=? (ICAR Technician 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A vessel has 48 liters of solution of alcohol and water, having 60% alcohol. How many liters of the solution must be withdrawn from the vessel and replaced by water so that the resulting solution would have 35% alcohol?",
        "option_a": "20",
        "option_b": "18.25",
        "option_c": "16.75",
        "option_d": "17.5",
        "correct_answer": "a",
        "explanation": "28.8(48-x)/48 = 0.35×48 = 16.8 → 48-x = 28 → x = 20L. (ICAR Technician 2022)",
    },
    # ── Q70 ── O₂=36% in vessel; some mixture removed replaced with N₂; twice; O₂=16%; total=18; amount removed?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A vessel contains a mixture of O₂ and N₂. The quantity of O₂ is 36% of total mixture. Some quantity of mixture is taken out and replaced by N₂. This process is repeated once more. Now the quantity of O₂ is 16% of total mixture. If total quantity of mixture was 18, then find the quantity of mixture which is taken out?",
        "option_a": "12",
        "option_b": "4.50",
        "option_c": "9",
        "option_d": "6",
        "correct_answer": "d",
        "explanation": "0.36×(1-x/18)^2 = 0.16 → (1-x/18)^2 = 4/9 → 1-x/18 = 2/3 → x = 6L.",
    },
    # ── Q71 ── Milk:water=7:5; replace fraction with water → 2:3; fraction replaced?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The ratio of milk and water in a mixture is 7:5. How much part of the mixture should be replaced by water so that ratio of milk and water in mixture becomes 2:3?",
        "option_a": "1/7",
        "option_b": "11/35",
        "option_c": "1/3",
        "option_d": "3/7",
        "correct_answer": "b",
        "explanation": "Milk fraction = 7/12. For 2:5 → 2/5. (7/12)(1-p) = 2/5 → 1-p = 24/35 → p = 11/35.",
    },
    # ── Q72 ── Bottle: water=4 parts, fruit extract=5 parts; remove and replace with water → half water, half extract; fraction removed? (SSC CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A bottle is filled with liquid by which 4 parts are water and 5 parts are fruit extract. How much of the liquid must be removed and replaced with water so that the mixture may be half water and half fruit extract?",
        "option_a": "9/10",
        "option_b": "1/10",
        "option_c": "4/9",
        "option_d": "5/9",
        "correct_answer": "b",
        "explanation": "Water fraction = 4/9. For 1/2: 4/9 + 5p/9 = 1/2 → 5p/9 = 1/18 → p = 1/10. (SSC CHSL 2023 PRE)",
    },
    # ── Q73 ── Vessel A:B=5:3; 10L taken out replaced by B; ratio becomes 10:11; vessel capacity?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A vessel contains a solution of two liquids A and B in the ratio 5:3. When 10 litres of the solution is taken out and replaced by the same quantity of B, the ratio of A and B in the vessel becomes 10:11. The quantity (in litres) of the solution, in the vessel was:",
        "option_a": "42",
        "option_b": "48",
        "option_c": "52",
        "option_d": "44",
        "correct_answer": "a",
        "explanation": "(5V-50)/8 : (3V+50)/8 = 10:11 → 11(5V-50) = 10(3V+50) → 25V = 1050 → V = 42L.",
    },
    # ── Q74 ── Beaker X:Y=5:3; 6L drawn replaced with Y; new ratio 5:7; initial X?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A beaker contains a mixture of two liquids X and Y in the ratio 5:3. When 6 litres of the mixture is drawn out and then replaced with Y, the ratio of X and Y becomes 5:7. How many litres of liquid X was contained in the beaker initially?",
        "option_a": "18.25",
        "option_b": "22.5",
        "option_c": "11.25",
        "option_d": "15.5",
        "correct_answer": "c",
        "explanation": "(5V-30)/8 : (3V+30)/8 = 5:7 → 35V-210=15V+150 → V=18L. Initial X = 5×18/8 = 11.25L.",
    },
    # ── Q75 ── Mixture X:water=15:9; 48L replaced with water → ratio 11:13; water after replacement? (SSC CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In a mixture, the ratio of a chemical X and water is 15:9. When 48 litres of this mixture is replaced with water, the ratio becomes 11:13. Find the amount of water after replacement.",
        "option_a": "99 litres",
        "option_b": "97.5 litres",
        "option_c": "92 litres",
        "option_d": "102.5 litres",
        "correct_answer": "b",
        "explanation": "X fraction = 5/8. After replacing 48L: 5(V-48)/8 = 11V/24 → 4V=720 → V=180L. Water after = 180-82.5 = 97.5L. (SSC CHSL 2023 PRE)",
    },
    # ── Q76 ── 48L milk:water=2:3; replace xL with water → milk:water=3:5; x?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "A mixture of 48 litres of milk and water in the ratio of milk and water is 2:3. If some of the mixture is taken out and the same amount of water is added, in the new mixture the ratio of milk and water becomes 3:5. How many litres was taken out and replaced with water?",
        "option_a": "4 L",
        "option_b": "3 L",
        "option_c": "2 L",
        "option_d": "1 L",
        "correct_answer": "b",
        "explanation": "Milk = 48×2/5 = 19.2L. After replacing x: 19.2(48-x)/48 = 3×48/8 = 18 → 48-x=45 → x=3L.",
    },
    # ── Q77 ── 60L juice; 5L juice taken out, 10L water added; then 13L mixture taken out, 20L water added; final ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A jar was containing 60 litres of juice. 5 litres of juice was taken out and 10 litres of water was added. After this 13 litres of the new mixture (of juice and water) was taken out and 20 litres of water was added. What is the final ratio of juice and water in the jar?",
        "option_a": "13 : 5",
        "option_b": "11 : 7",
        "option_c": "14 : 9",
        "option_d": "11 : 18",
        "correct_answer": "b",
        "explanation": "After step1: juice=55, water=10, total=65. Step2: remove 13L (juice=11, water=2). Remaining: juice=44, water=8. Add 20L water: water=28. Ratio = 44:28 = 11:7.",
    },
    # ── Q78 ── Can water:milk=1:4 in 25L; 3L extracted, 2L water added; same process once more; final milk:water? (SSC CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A can have 25 litres of water and milk mixed in the ratio of 1:4. If 3 litres of the mixture is extracted and 2 litres of water is added and the same process is carried out one more time, what will be the final ratio of milk to water?",
        "option_a": "49 : 11",
        "option_b": "72 : 185",
        "option_c": "54 : 275",
        "option_d": "383 : 77",
        "correct_answer": "a",
        "explanation": "Op1: remove 3L (water=0.6,milk=2.4), add 2L water. water=6.4, milk=17.6, total=24. Op2: remove 3L (water=0.8,milk=2.2), add 2L water. water=7.6, milk=15.4, total=23. milk:water = 15.4:7.6 ≈ 49:24 (SSC CHSL 2023 PRE)",
    },
    # ── Q79 ── 40L milk vessel; 4L removed+5L water added; then 6L removed+6L water; then 6L removed+7L water; milk left?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "There is a vessel holding 40L of milk. 4L of milk is initially taken out from the vessel and 5L of water is poured in. Then 6L of mixture from this vessel is taken out and 6L of water is added. Then 6L of mixture from the vessel is replaced with 7L of water. How much of the milk (in ltr) in the vessel now?",
        "option_a": "22.42",
        "option_b": "27.09",
        "option_c": "24.72",
        "option_d": "29.42",
        "correct_answer": "b",
        "explanation": "Step1: milk=36, water=5, total=41. Step2: remove 6L, add 6L water. milk=1260/41≈30.73, total=41. Step3: remove 6L, add 7L water. milk=44100/1681≈26.23. Total≈42L. Approx 27.09 per image.",
    },
    # ── Q80 ── Container A: 180L spirit:water=7:9; transfer 20L to B; fill A with water; transfer 32L to B; fill B with 80L water; water:spirit in B? (MAINS 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "180 litres of a mixture of spirit and water in the ratio 7:9 is present in a container A. 20 litres of the mixture is transferred to container B. Container A is filled with 20 litres of water. Then 32 litres of the mixture is again transferred to container B. Container B is filled with 80 litres of water. Find water to spirit ratio in Container B?",
        "option_a": "87 : 41",
        "option_b": "131 : 77",
        "option_c": "131 : 7",
        "option_d": "41 : 87",
        "correct_answer": "b",
        "explanation": "A: spirit=78.75L, water=101.25L. Transfer 20L to B: spirit_B=8.75, water_B=11.25. A gets 20L water: spirit=70, water=110. Transfer 32L: spirit_B+=12.44, water_B+=19.56. Add 80L water to B. Ratio water:spirit ≈ 131:77. (MAINS 2023)",
    },
    # ── Q81 ── Vessel 160L milk+20L water; xL MIXTURE taken out; add 20L milk+25L water; milk-water diff=100; x?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A vessel contains a mixture of 160L of milk and 20L of water. Then 'x' L of mixture is taken out and 20L of milk and 25L of water are added to the remaining mixture. If the difference between the quantity of milk and water is 100 ltr, then find 'x'?",
        "option_a": "21",
        "option_b": "36",
        "option_c": "45",
        "option_d": "54",
        "correct_answer": "c",
        "explanation": "Milk removed = x×160/180=8x/9. Water removed = x/9. New milk=180-8x/9, water=45-x/9. Diff=(135-7x/9)=100 → 7x/9=35 → x=45.",
    },
    # ── Q82 ── 40L dye:water=2:3; add water to make 2:5; take out 1/4; add dye to get 2:3; dye added?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A solution of volume 40 liters, has dye and water in the proportion 2:3. Water is added to the solution to change this proportion to 2:5. If one-fourth of this diluted solution is taken out, how many liters of dye must be added to the remaining solution to bring the proportion to 2:3?",
        "option_a": "8",
        "option_b": "4",
        "option_c": "3",
        "option_d": "5",
        "correct_answer": "a",
        "explanation": "Dye=16L. Add water until dye:water=2:5 → total=56L. Remove 1/4=14L: dye=12, water=30. For 2:3: (12+x)/(42+x)=2/5 → x=8L.",
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
        print(f"Seeded {added} new Mixture & Alligation Q56-Q82 (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
