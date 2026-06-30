"""
Partnership questions — Gagan Pratap Maths (Partnership Sheet Q1–Q26).
Topic: "Partnership" under Quantitative Aptitude.
Run: python seed_partnership_sheet.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # Q1 - Lady invests Rs.27600 in 3:4:5 shares; dividends 20%/15%/5%; total dividend? (MTS 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "easy", "phase": "main",
        "question_text": "A lady invests Rs.27600 in three shares in the ratio 3:4:5 which pay dividends of 20%, 15% and 5% on her investment for that year respectively. What is the total dividend? (SSC MTS 2023)",
        "option_a": "Rs.3852",
        "option_b": "Rs.3335",
        "option_c": "Rs.3125",
        "option_d": "Rs.2535",
        "correct_answer": "b",
        "explanation": "Each part=27600/12=2300. Shares: 6900, 9200, 11500. Dividends: 6900×20%=1380, 9200×15%=1380, 11500×5%=575. Total=1380+1380+575=Rs.3335.",
    },
    # Q2 - Profit 8:7:5; invested for 7, 8, 14 months; ratio of capitals?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "Three partners shared the profit in a business in the ratio 8:7:5. They invested their capitals for 7 months, 8 months and 14 months respectively. What was the ratio of their capitals?",
        "option_a": "49:64:20",
        "option_b": "20:49:64",
        "option_c": "20:64:49",
        "option_d": "64:49:20",
        "correct_answer": "d",
        "explanation": "Capital = Profit / Time. C₁:C₂:C₃ = 8/7 : 7/8 : 5/14. LCM(7,8,14)=56. Multiply: 64:49:20.",
    },
    # Q3 - Capital ratio 3:4:8; profit ratio 2:3:5; time ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "A, B and C invested capitals in the ratio 3:4:8. At the end of the business period, they got profits in the ratio 2:3:5. What is the ratio of their time invested?",
        "option_a": "16:18:15",
        "option_b": "13:18:15",
        "option_c": "16:21:18",
        "option_d": "15:16:13",
        "correct_answer": "a",
        "explanation": "Time = Profit/Capital. T_A:T_B:T_C = (2/3):(3/4):(5/8). LCM(3,4,8)=24. Multiply: 16:18:15.",
    },
    # Q4 - Sathi:Rathin = 6:5; Sathi withdrew; year-end profit 7:10; Rathin alone months? (UP Constable 2018)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "Sathi and Rathin invested some money in a business in the ratio 6:5, but Sathi withdrew her money after a few months. If the end-of-twelve-months' profit was shared between Sathi and Rathin in the ratio 7:10, for how many months did Rathin alone invest? (UP Constable 19/06/2018 1st Shift)",
        "option_a": "4",
        "option_b": "5",
        "option_c": "6",
        "option_d": "7",
        "correct_answer": "b",
        "explanation": "6t : 5×12 = 7:10 → 6t=42 → t=7 months (Sathi). Rathin alone = 12−7 = 5 months.",
    },
    # Q5 - Mitali Rs.336, Jhulan Rs.231; Mitali withdrew; profit 2:3; Mitali's months? (UP Police 2018)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "Mitali and Jhulan invested Rs.336 and Rs.231 respectively in a business but Mitali withdrew her money after a few months. If the end of twelve months profit was shared between Mitali and Jhulan in the ratio 2:3, after how many months did Mitali take out her money? (UP Police Constable 2018)",
        "option_a": "4.5",
        "option_b": "5.5",
        "option_c": "6.5",
        "option_d": "7.5",
        "correct_answer": "b",
        "explanation": "336t : 231×12 = 2:3 → 336t = 1848 → t = 5.5 months. Verify: 1848:2772 = 2:3 ✓.",
    },
    # Q6 - P's investment = 3/4 of Q's; Q gained Rs.1200 on Rs.40000; P's profit:investment? (UP Police Head Operator 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "P's investment in a business is 3/4 of Q's investment. Q gained a profit of Rs.1200 by investing Rs.40000 in the business. What will be the ratio of P's profit to his investment in the business? (UP Police Head Operator 2024)",
        "option_a": "10:3",
        "option_b": "100:3",
        "option_c": "3:10",
        "option_d": "3:100",
        "correct_answer": "d",
        "explanation": "P's investment=3/4×40000=Rs.30000. P's profit=3/4×1200=Rs.900. Ratio=900:30000=3:100.",
    },
    # Q7 - A=13750, B=16250, C=18750; B's profit share=5200; total profit?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "easy", "phase": "main",
        "question_text": "A, B and C start a business by investing Rs.13,750, Rs.16,250 and Rs.18,750 respectively. If B's share in the profit received by them is Rs.5,200, find the total profit (in Rs) of the three together.",
        "option_a": "15,600",
        "option_b": "18,200",
        "option_c": "16,600",
        "option_d": "17,500",
        "correct_answer": "a",
        "explanation": "Ratio=13750:16250:18750=11:13:15. Total parts=39. B's share=13/39×T=5200 → T=5200×3=Rs.15,600.",
    },
    # Q8 - P=1430, Q=1870, R=2420 profit; total invested=41600; Q's investment?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "Three partners P, Q and R invested a total of Rs.41600 in a business. At the end of the year, P got Rs.1430, Q got Rs.1870 and R got Rs.2420. How much amount did Q invest in the business?",
        "option_a": "Rs.15300",
        "option_b": "Rs.18700",
        "option_c": "Rs.13600",
        "option_d": "Rs.11900",
        "correct_answer": "c",
        "explanation": "Profit ratio=1430:1870:2420=13:17:22 (divide by 110). Q's investment=17/52×41600=17×800=Rs.13600.",
    },
    # Q9 - Priya+Ayushi Rs.45600; Priya's share=1800; total profit=7500; Ayushi's investment? (RRB RPF SI 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "Priya and Ayushi together invested Rs.45600 in a business. At the end of the year, out of a total profit of Rs.7500, Priya's share was Rs.1800. What was the investment of Ayushi? (RRB RPF SI 2024)",
        "option_a": "Rs.34656",
        "option_b": "Rs.35535",
        "option_c": "Rs.32910",
        "option_d": "Rs.34445",
        "correct_answer": "a",
        "explanation": "Priya's investment=1800/7500×45600=6/25×45600=Rs.10944. Ayushi=45600−10944=Rs.34656.",
    },
    # Q10 - A=1/3 total, B=1/3 remaining, C=rest; profit=4050; C−B? (UP Constable Re-Exam 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "A, B and C started a business. A invested 33⅓% of the total capital, B invested 33⅓% of the remaining capital and C, the remaining. If the total profit at the end of the year was Rs.4050, then find the amount by which the profit of C exceeds the profit of B. (UP Constable Re-Exam 2024)",
        "option_a": "Rs.675",
        "option_b": "Rs.700",
        "option_c": "Rs.520",
        "option_d": "Rs.900",
        "correct_answer": "d",
        "explanation": "A=1/3, B=1/3×2/3=2/9, C=1−1/3−2/9=4/9 of total. Profit ratio A:B:C=3:2:4. C−B=(4−2)/9×4050=2/9×4050=Rs.900.",
    },
    # Q11 - Capital 2:3:5, months 4:2:3; A−B diff=Rs.1,86,000; C's share?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "A, B and C invested their capitals in the ratio 2:3:5. The ratio of months for which they invested is 4:2:3. If the difference between the profit shares of A and B is Rs.1,86,000, then C's share of profit (in Rs) is:",
        "option_a": "15,39,000",
        "option_b": "19,35,000",
        "option_c": "13,95,000",
        "option_d": "10,29,500",
        "correct_answer": "c",
        "explanation": "Effective capital A:B:C=2×4:3×2:5×3=8:6:15. A−B=2 parts=1,86,000 → 1 part=93,000. C=15×93,000=Rs.13,95,000.",
    },
    # Q12 - 2A=3B=5C; total profit=Rs.15.5 lakhs; B's share?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "A, B and C started a business. Twice the investment of A is equal to thrice the investment of B and also five times the investment of C. If the total profit after a year is Rs.15.5 lakhs, then the share of B in the profit is (in Rs lakhs):",
        "option_a": "7.5",
        "option_b": "3",
        "option_c": "5",
        "option_d": "4.5",
        "correct_answer": "c",
        "explanation": "2A=3B=5C=k → A=k/2, B=k/3, C=k/5. Ratio A:B:C=15:10:6. B's share=10/31×15.5=155/31=5 lakhs.",
    },
    # Q13 - A=B+6L, B invests 7.5mo, A invests 10mo; profit=12.4L, A−B=2.48L; B's capital?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "A invests Rs.6,00,000 more than B in a business. B invests his capital for 7½ months, while A invests his capital for 2½ months more than B. Out of the total profit of Rs.12,40,000, if the share of B is Rs.2,48,000 less than the share of A, then the capital of B is:",
        "option_a": "Rs.40,00,000",
        "option_b": "Rs.42,00,000",
        "option_c": "Rs.48,00,000",
        "option_d": "Rs.45,00,000",
        "correct_answer": "c",
        "explanation": "Let B=x, A=x+600000. A's time=10mo, B's=7.5mo. (A−B)/(A+B)=248000/1240000=1/5. [2.5x+6000000]/[17.5x+6000000]=1/5 → x=4800000=Rs.48,00,000.",
    },
    # Q14 - A+B+C=75500; A=B+3500, B=C+4500; profit=45300; A's share?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "A, B, C subscribe a sum of Rs.75,500 for a business. A subscribes Rs.3500 more than B and B subscribes Rs.4500 more than C. Out of a total profit of Rs.45,300, how much does A receive?",
        "option_a": "Rs.17,400",
        "option_b": "Rs.14,700",
        "option_c": "Rs.12,600",
        "option_d": "Rs.15,000",
        "correct_answer": "a",
        "explanation": "C=21000, B=25500, A=29000, total=75500. A:B:C=29000:25500:21000=58:51:42. A's share=58/151×45300=Rs.17,400.",
    },
    # Q15 - Arvind+Bilal+Carmen=49000; Arvind=Bilal+5000, Bilal=Carmen+4000; profit=98000; Bilal? (SSC MTS 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "medium", "phase": "main",
        "question_text": "Arvind, Bilal, Carmen invest Rs.49000 towards a business. Arvind invests Rs.5000 more than Bilal and Bilal invests Rs.4000 more than Carmen. Out of a total profit of Rs.98,000, how much does Bilal receive? (SSC MTS 2023)",
        "option_a": "Rs.34,400",
        "option_b": "Rs.33,200",
        "option_c": "Rs.30,500",
        "option_d": "Rs.32,000",
        "correct_answer": "d",
        "explanation": "Bilal=x, Arvind=x+5000, Carmen=x−4000. Sum=3x+1000=49000 → x=16000. Ratio=21000:16000:12000=21:16:12. Bilal=16/49×98000=Rs.32,000.",
    },
    # Q16 - X=1/6 cap×1/6 time, Y=1/3×1/3, Z=rest×full; profit=23000; Y's share? (UP Constable Re-Exam 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "In a partnership, X invests 1/6th of the capital for 1/6th of the time, Y invests 1/3rd of the capital for 1/3rd times and Z invests the remaining capital for the whole time. If at the end of the year the profit earned is Rs.23000, then what will be Y's share? (UP Constable Re-Exam 2024)",
        "option_a": "Rs.5000",
        "option_b": "Rs.4000",
        "option_c": "Rs.5500",
        "option_d": "Rs.6000",
        "correct_answer": "b",
        "explanation": "Effective: X=1/6×1/6=1/36, Y=1/3×1/3=1/9, Z=1/2×1=1/2. Ratio=1:4:18 (multiply by 36). Y=4/23×23000=Rs.4000.",
    },
    # Q17 - P=Q+14000; P for 8mo, Q for 10mo; P share=Q share+400, total=2000; P's capital? (UPSC CSAT 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "Two persons P and Q enter into a business. P puts Rs.14000 more than Q, but P has invested for 8 months and Q has invested for 10 months. If P's share is Rs.400 more than Q's share out of the total profit of Rs.2000, what is the capital contributed by P? (UPSC CSAT 2024)",
        "option_a": "Rs.30000",
        "option_b": "Rs.26000",
        "option_c": "Rs.24000",
        "option_d": "Rs.20000",
        "correct_answer": "a",
        "explanation": "[8(x+14000)−10x]/[8(x+14000)+10x]=400/2000=1/5. Solving: 112000−2x=18x+22400 → x=16000. P=16000+14000=Rs.30000.",
    },
    # Q18 - Mohit 5mo claims 1/16; Rohit 4mo claims 1/3; Ayush=1537 10mo; Mohit & Rohit contributions?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "Mohit, Rohit and Aayush are partners in a business. Mohit, whose money has been used for 5 months, claims 1/16 of the profit. Rohit, whose money has been used for 4 months, claims 1/3 of profit. Ayush had invested Rs.1537 for 10 months. How much money did Mohit and Rohit, respectively, contribute?",
        "option_a": "Rs.326 and Rs.2,236",
        "option_b": "Rs.318 and Rs.2,120",
        "option_c": "Rs.659 and Rs.1,896",
        "option_d": "Rs.256 and Rs.2,365",
        "correct_answer": "b",
        "explanation": "Ayush share=1−1/16−1/3=29/48. Ratios M×5:R×4:1537×10=3:16:29. k=1537×10/29=530. M=3×530/5=Rs.318, R=16×530/4=Rs.2120.",
    },
    # Q19 - A:B:C=2:3:5; 9% to charity; total=2,50,000; C's share? (SSC CGL 2024 Pre)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "easy", "phase": "main",
        "question_text": "Three people A, B and C invest in a business in the ratio 2:3:5. It was decided that 9% of the profits will go to charity. If the total profit was Rs.2,50,000, then find the share of C in the profit (in Rs). (SSC CGL 2024 Pre)",
        "option_a": "Rs.1,26,950",
        "option_b": "Rs.1,11,650",
        "option_c": "Rs.1,21,850",
        "option_d": "Rs.1,13,750",
        "correct_answer": "d",
        "explanation": "Profit after charity=91%×250000=227500. C's share=5/10×227500=Rs.1,13,750.",
    },
    # Q20 - X:Y=3:5; after 5mo X+50%, Y−60%; annual profit=6.84L; X's share?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "X and Y enter into a partnership with capital in the ratio 3:5. After 5 months X adds 50% of his capital, while Y withdraws 60% of his capital. What is the share (in Rs lakhs) of X in the annual profit of Rs.6.84 lakhs?",
        "option_a": "3.72",
        "option_b": "4.2",
        "option_c": "3.6",
        "option_d": "3.12",
        "correct_answer": "a",
        "explanation": "X: 3k×5+4.5k×7=46.5k. Y: 5k×5+2k×7=39k. Ratio=46.5:39=31:26. X's share=31/57×6.84=Rs.3.72 lakhs.",
    },
    # Q21 - Mohit:Ravi=4:5; after 4mo M+25%, R−1/5; Ravi's share=20.8L; total?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "Mohit and Ravi started a business with their capitals in the ratio 4:5. After 4 months, Mohit increased his capital by 25% and Ravi reduced his capital by one-fifth. At the end of a year, if Ravi's share in the annual profit was 20.8 lakhs, then what was the annual profit (in Rs lakhs)?",
        "option_a": "41.6",
        "option_b": "31.2",
        "option_c": "43.2",
        "option_d": "44.8",
        "correct_answer": "c",
        "explanation": "Mohit: 4k×4+5k×8=56k. Ravi: 5k×4+4k×8=52k. Ravi's share=52/108=13/27. Total=20.8×27/13=Rs.43.2 lakhs.",
    },
    # Q22 - A:B:C=2:3:5; A+50% at 4mo, B+33⅓% at 6mo, C−50% at 8mo; total=86800; A−C diff?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "A, B and C started a business with their capitals in the ratio 2:3:5. A increased his capital by 50% after 4 months, B increased his capital by 33⅓% after 6 months, from the start of the business. If C withdrew 50% of his capital after 8 months from the start of the business. If the total profit at end of a year was Rs.86,800, then the difference between the shares of A and C in the profit was:",
        "option_a": "Rs.12,600",
        "option_b": "Rs.7,000",
        "option_c": "Rs.8,400",
        "option_d": "Rs.9,800",
        "correct_answer": "a",
        "explanation": "Effective A=2k×4+3k×8=32k, B=3k×6+4k×6=42k, C=5k×8+2.5k×4=50k. Ratio=32:42:50=16:21:25. (C−A)=9/62×86800=9×1400=Rs.12,600.",
    },
    # Q23 - A=100000 12mo, B=140000 10mo, C=200000 3mo; C share=1155; A+B total profit?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "A, B and C started a business with the investment of Rs.100000, Rs.140000 and Rs.200000 respectively. After 3 months, C left the business. 7 months after C left the business, B also left the business. B and C took their investments with them. At the end of the year, C received his share of profit as Rs.1155. What is the total profits of A and B?",
        "option_a": "Rs.150",
        "option_b": "Rs.5555",
        "option_c": "Rs.5005",
        "option_d": "Rs.4995",
        "correct_answer": "c",
        "explanation": "A:B:C effective=100000×12:140000×10:200000×3=1200000:1400000:600000=6:7:3. C's share=3/16×Total=1155 → Total=6160. A+B=13/16×6160=Rs.5005.",
    },
    # Q24 - A=20000, B=25000, C=10000; A+4000 at 5mo; C+8000 at 6mo; B−8000 at 4mo; ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "A, B and C started a business with initial investments of Rs.20000, Rs.25000 and Rs.10000 respectively. After 5 months from start, A invested Rs.4000 more. After 6 months from start, C invested Rs.8000 more. After 4 months from start, B withdrew Rs.8000. At the end of the year, they will receive a profit of 'x'. In what ratio will they share the profit?",
        "option_a": "71:59:42",
        "option_b": "86:68:42",
        "option_c": "67:59:42",
        "option_d": "71:57:42",
        "correct_answer": "c",
        "explanation": "A=20000×5+24000×7=268000. B=25000×4+17000×8=236000. C=10000×6+18000×6=168000. Ratio=268:236:168=67:59:42.",
    },
    # Q25 - A=112000; B=80000 joined mo2; C=72000 joined mo4; both −8000 at mo10; B share=9800; total?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "A started a business with a capital of Rs.1,12,000. After 2 months, B joined the business with a capital of Rs.80,000, and after another 2 months, C joined the business with a capital of Rs.72,000. After 10 months from the start of the business, B withdrew Rs.8,000 and C also withdrew Rs.8,000. If B received Rs.9,800 as his share in the profit at the end of a year, then the total profit was:",
        "option_a": "Rs.32,400",
        "option_b": "Rs.35,800",
        "option_c": "Rs.30,800",
        "option_d": "Rs.33,600",
        "correct_answer": "d",
        "explanation": "A=112000×12=1344000. B=80000×8+72000×2=784000. C=72000×6+64000×2=560000. Ratio=12:7:5. B=7/24×T=9800 → T=Rs.33,600.",
    },
    # Q26 - A:B:C=4:2:9; each quarter A halves, B doubles, C unchanged; A profit=24000; total?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Partnership", "difficulty": "hard", "phase": "main",
        "question_text": "A, B and C started a business with their capitals in the ratio 4:2:9. at the end of every quarter, A halves his capital, while B doubles his capital and C leaves his capital unchanged. If A's profit was Rs.24000, then what is the total profit?",
        "option_a": "Rs.2,35,200",
        "option_b": "Rs.2,30,400",
        "option_c": "Rs.2,16,000",
        "option_d": "Rs.2,25,600",
        "correct_answer": "a",
        "explanation": "A quarters: 4,2,1,0.5 → effective=(7.5k)×3=22.5k. B quarters: 2,4,8,16 → 90k. C: 9×4=36 quarters → 108k. Ratio=22.5:90:108=5:20:24. A=5/49×T=24000 → T=Rs.2,35,200.",
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
        print(f"Seeded {added} new Partnership questions (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
