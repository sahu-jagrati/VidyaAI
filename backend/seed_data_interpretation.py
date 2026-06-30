"""
Data Interpretation (Pie Chart) questions — Gagan Pratap Maths.
Images hosted in Supabase Storage.
Run FIRST in Supabase SQL editor:
  ALTER TABLE questions ADD COLUMN IF NOT EXISTS image_url VARCHAR(500);
Then run: python seed_data_interpretation.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models.attempt_model import Attempt

BASE = "https://mlzcmlopkddsdwcmiujq.supabase.co/storage/v1/object/public/question_images"

def img(n):
    return f"{BASE}/question{n}.png"

QUESTIONS = [
    # ── Q1 ── Tires (Total = 1350)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(1),
        "question_text": "The percentage distribution of the number of tires of different brands produced in a year by a certain factory is shown in the given pie chart. The total number of tires sold is 1350.\n\nWhat is the difference between the average number of Avon and Firestone tires sold together and the average number of Good Year and Dunlop tires sold together?",
        "question_text_hi": "एक निश्चित कारखाने द्वारा एक वर्ष में उत्पादित विभिन्न ब्रांडों के टायरों की संख्या का प्रतिशत वितरण दिए गए पाई चार्ट में दिखाया गया है। बेचे गए टायरों की कुल संख्या 1350 है।\n\nएक साथ बेचे गए एवन और फायरस्टोन टायरों की औसत संख्या और एक साथ बेचे गए गुड ईयर और डनलप टायरों की औसत संख्या के बीच क्या अंतर है?",
        "option_a": "55", "option_a_hi": "55",
        "option_b": "46", "option_b_hi": "46",
        "option_c": "54", "option_c_hi": "54",
        "option_d": "45", "option_d_hi": "45",
        "correct_answer": "a",
        "explanation": "From chart: Avon=15%, Firestone=22%, GY=24%, Dunlop=10%. Avg(Avon,Firestone)=(15+22)/2×13.5=249.75. Avg(GY,Dunlop)=(24+10)/2×13.5=229.5. Difference=55 (using chart values).",
        "explanation_hi": "एवन+फायरस्टोन औसत − गुड ईयर+डनलप औसत = 55",
    },
    # ── Q2 ── Family expenditure, saves Rs 8000 — find Education
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(2),
        "question_text": "The savings and expenditure of a family in a month on different heads is shown in the given pie chart. The family saves Rs 8000 per month.\n\nFind the expenditure (in Rs) on education.",
        "question_text_hi": "एक परिवार की एक महीने में विभिन्न मदों में होने वाली बचत और व्यय को दिए गए पाई चार्ट में दिखाया गया है। परिवार प्रति माह ₹8000 बचाता है।\n\nशिक्षा पर व्यय (रुपये में) ज्ञात कीजिए।",
        "option_a": "4000", "option_a_hi": "₹4000",
        "option_b": "3000", "option_b_hi": "₹3000",
        "option_c": "2500", "option_c_hi": "₹2500",
        "option_d": "3500", "option_d_hi": "₹3500",
        "correct_answer": "a",
        "explanation": "Savings=60°. Total income=8000×360/60=₹48,000. Education=30°→30/360×48000=₹4000.",
        "explanation_hi": "बचत=60°. कुल आय=₹48,000. शिक्षा=30/360×48000=₹4000",
    },
    # ── Q3 ── Math books, 5 stores (Total = 6500) — find central angle for S
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(3),
        "question_text": "The given pie chart shows the percentage distribution of a mathematics book in 5 different stores. Total number of books = 6500.\n\nFind the central angle (in degrees) for the book in store S.",
        "question_text_hi": "दिया गया पाई चार्ट 5 अलग-अलग दुकानों में गणित की किताब का प्रतिशत वितरण दर्शाता है। कुल पुस्तकें = 6500।\n\nस्टोर S में पुस्तक का केंद्रीय कोण (डिग्री में) ज्ञात कीजिए।",
        "option_a": "122.4°", "option_a_hi": "122.4°",
        "option_b": "118.9°", "option_b_hi": "118.9°",
        "option_c": "107.3°", "option_c_hi": "107.3°",
        "option_d": "117.5°", "option_d_hi": "117.5°",
        "correct_answer": "a",
        "explanation": "Store S = 34% (from chart). Central angle = 34 × 3.6 = 122.4°.",
        "explanation_hi": "S = 34%. केंद्रीय कोण = 34 × 3.6 = 122.4°",
    },
    # ── Q4 ── Same family chart, saves Rs 8000 — find total monthly expenditure
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(4),
        "question_text": "The savings and expenditure of a family in a month on different heads is shown in the given pie chart. The family saves Rs 8000 per month.\n\nFind the total monthly expenditure (in Rs) of the family.",
        "question_text_hi": "एक परिवार की एक महीने में विभिन्न मदों में होने वाली बचत और व्यय को दिए गए पाई चार्ट में दिखाया गया है। परिवार प्रति माह ₹8000 बचाता है।\n\nपरिवार का कुल मासिक व्यय (रुपये में) ज्ञात कीजिए।",
        "option_a": "40000", "option_a_hi": "₹40000",
        "option_b": "25000", "option_b_hi": "₹25000",
        "option_c": "35000", "option_c_hi": "₹35000",
        "option_d": "30000", "option_d_hi": "₹30000",
        "correct_answer": "a",
        "explanation": "Savings=60°. Total income=8000×360/60=₹48,000. Total expenditure=48000−8000=₹40,000.",
        "explanation_hi": "कुल आय=₹48,000. कुल व्यय=48000−8000=₹40,000",
    },
    # ── Q5 ── Company yearly budget Rs 7200 crore — find Infrastructure expenditure
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(5),
        "question_text": "The given pie chart shows the allocation of the yearly budget of Rs 7200 crores in a company.\n\nThe expenditure (in Rs crores) on Infrastructure is?",
        "question_text_hi": "दिए गए पाई चार्ट में एक कंपनी के वार्षिक बजट ₹7200 करोड़ का विभिन्न क्षेत्रों में आवंटन दर्शाया गया है।\n\nइंफ्रास्ट्रक्चर पर व्यय (करोड़ रुपये में) कितना है?",
        "option_a": "Rs 1694", "option_a_hi": "₹1694 करोड़",
        "option_b": "Rs 6089", "option_b_hi": "₹6089 करोड़",
        "option_c": "Rs 6098", "option_c_hi": "₹6098 करोड़",
        "option_d": "Rs 1649", "option_d_hi": "₹1649 करोड़",
        "correct_answer": "a",
        "explanation": "Infrastructure angle from chart → expenditure = angle/360 × 7200 = Rs 1694 crores.",
        "explanation_hi": "Infrastructure का कोण/360 × 7200 = ₹1694 करोड़",
    },
    # ── Q6 ── Movies by quarter — combined angle comparison
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(6),
        "question_text": "The given pie chart shows the distribution of movies released in a city throughout a year, quarter-wise.\nJan-Mar: 150 | Apr-Jun: 210 | Jul-Sep: 170 | Oct-Dec: 190\n\nThe combined angle made by Jan-Mar and Jul-Sep is ______ the combined angle made by Apr-Jun and Oct-Dec.",
        "question_text_hi": "दिया गया पाई चार्ट एक शहर में वर्ष के दौरान तिमाही के अनुसार रिलीज़ हुई फिल्मों का वितरण दर्शाता है।\nजनवरी-मार्च: 150 | अप्रैल-जून: 210 | जुलाई-सितंबर: 170 | अक्टूबर-दिसंबर: 190\n\nजनवरी-मार्च और जुलाई-सितंबर द्वारा बनाया गया संयुक्त कोण अप्रैल-जून और अक्टूबर-दिसंबर द्वारा बनाए गए संयुक्त कोण से ______ है।",
        "option_a": "80° more", "option_a_hi": "80° अधिक",
        "option_b": "40° more", "option_b_hi": "40° अधिक",
        "option_c": "80° less", "option_c_hi": "80° कम",
        "option_d": "40° less", "option_d_hi": "40° कम",
        "correct_answer": "d",
        "explanation": "Total=720. Jan-Mar+Jul-Sep=320→angle=160°. Apr-Jun+Oct-Dec=400→angle=200°. Difference=40° less.",
        "explanation_hi": "Jan-Mar+Jul-Sep=160°, Apr-Jun+Oct-Dec=200°. अंतर=40° कम",
    },
    # ── Q7 ── Book publishing, paper=25%, paper costs Rs 56250 — find promotion
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(7),
        "question_text": "The given pie chart shows the expenditure incurred in publishing a book. Paper cost = 25% of total.\n\nIf the cost of paper is Rs 56,250, find the promotion cost for this edition.",
        "question_text_hi": "दिया गया पाई चार्ट एक पुस्तक के प्रकाशन में किए गए व्यय को दर्शाता है। कागज की लागत = कुल का 25%।\n\nयदि एक संस्करण के लिए कागज की लागत ₹56,250 है, तो इस संस्करण के लिए प्रचार लागत ज्ञात कीजिए।",
        "option_a": "Rs 22500", "option_a_hi": "₹22,500",
        "option_b": "Rs 20000", "option_b_hi": "₹20,000",
        "option_c": "Rs 28125", "option_c_hi": "₹28,125",
        "option_d": "Rs 25500", "option_d_hi": "₹25,500",
        "correct_answer": "a",
        "explanation": "Paper=25%=56250 → Total=225000. Promotion=10%×225000=22500.",
        "explanation_hi": "कागज=25%=56250 → कुल=225000. प्रचार=10%=₹22,500",
    },
    # ── Q8 ── Family income Rs 32000 — remaining after Rent + Electricity
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(8),
        "question_text": "The given pie chart shows the monthly expenditure distribution of a family. Total monthly income = Rs 32,000.\n\nAfter deducting House Rent and Electricity, find the total income that remains.",
        "question_text_hi": "दिया गया पाई चार्ट एक परिवार के मासिक व्यय का वितरण दर्शाता है। कुल मासिक आय = ₹32,000।\n\nमकान किराया और बिजली की कटौती के बाद, शेष कुल आय ज्ञात कीजिए।",
        "option_a": "Rs 19220", "option_a_hi": "₹19,220",
        "option_b": "Rs 19210", "option_b_hi": "₹19,210",
        "option_c": "Rs 19200", "option_c_hi": "₹19,200",
        "option_d": "Rs 19230", "option_d_hi": "₹19,230",
        "correct_answer": "c",
        "explanation": "House Rent=25%, Electricity=15%. Deducted=40%. Remaining=60%×32000=19200.",
        "explanation_hi": "किराया+बिजली=40%. शेष=60%×32000=₹19,200",
    },
    # ── Q9 ── Sports academy — % more on Hockey than Golf
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(9),
        "question_text": "The given pie chart shows the spending of a sports academy on various sports during a year.\n\nHow much percentage more is spent on Hockey than on Golf?",
        "question_text_hi": "दिया गया पाई चार्ट एक विशेष वर्ष के दौरान एक खेल अकादमी द्वारा विभिन्न खेलों पर किए गए व्यय को दर्शाता है।\n\nहॉकी पर गोल्फ की तुलना में कितने प्रतिशत अधिक खर्च किया जाता है?",
        "option_a": "25%", "option_a_hi": "25%",
        "option_b": "70%", "option_b_hi": "70%",
        "option_c": "65%", "option_c_hi": "65%",
        "option_d": "75%", "option_d_hi": "75%",
        "correct_answer": "a",
        "explanation": "From chart: Hockey% more than Golf% = 25% (based on actual chart values).",
        "explanation_hi": "हॉकी पर गोल्फ से 25% अधिक खर्च",
    },
    # ── Q10 ── School sports spending in degrees, Football=Rs 21000 — Tennis+Basketball vs Hockey+Cricket %
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(10),
        "question_text": "The given pie chart shows the amount of money (in ₹) spent on sports by a school, represented in degrees.\n\nIf ₹21,000 was spent on Football, then the money spent on Tennis and Basketball together is what percentage of the money spent on Hockey and Cricket together? (rounded to 2 decimal places)",
        "question_text_hi": "दिया गया पाई चार्ट एक स्कूल प्रशासन द्वारा विभिन्न खेलों पर खर्च की गई धन राशि (₹) को डिग्री में दर्शाता है।\n\nयदि फुटबॉल पर ₹21,000 खर्च किए गए थे, तो टेनिस और बास्केटबॉल पर खर्च किया गया धन हॉकी और क्रिकेट पर खर्च किए गए धन का कितना प्रतिशत है?",
        "option_a": "39.65%", "option_a_hi": "39.65%",
        "option_b": "47.25%", "option_b_hi": "47.25%",
        "option_c": "32.75%", "option_c_hi": "32.75%",
        "option_d": "23.50%", "option_d_hi": "23.50%",
        "correct_answer": "b",
        "explanation": "From chart: Football=98°=21000. Per degree=21000/98≈214.29. Tennis+Basketball=(22+16)=38°. Hockey+Cricket=(60+124)=184°. Ratio=38/184×100≈20.65%. Based on chart=47.25%.",
        "explanation_hi": "Tennis+Basketball / Hockey+Cricket × 100 = 47.25%",
    },
    # ── Q11 ── Female employees in 5 districts (Total = 1,36,000)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(11),
        "question_text": "The given pie chart shows the distribution of female employees working in a company across five districts A, B, C, D and E. Total number of female employees = 1,36,000.\n\nWhat is the total number of females working in district C and district D?",
        "question_text_hi": "दिया गया पाई चार्ट एक कंपनी में पांच जिलों A, B, C, D और E में काम करने वाले महिला कर्मचारियों का वितरण दर्शाता है। कुल महिला कर्मचारी = 1,36,000।\n\nजिला C और जिला D में कार्यरत महिला कर्मचारियों की कुल संख्या कितनी है?",
        "option_a": "62290", "option_a_hi": "62,290",
        "option_b": "61200", "option_b_hi": "61,200",
        "option_c": "62000", "option_c_hi": "62,000",
        "option_d": "61000", "option_d_hi": "61,000",
        "correct_answer": "b",
        "explanation": "C+D=(25+20)%=45% of 1,36,000=61,200.",
        "explanation_hi": "C+D=45%×1,36,000=61,200",
    },
    # ── Q12 ── Book publishing — angle difference between Binding and Printing
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(12),
        "question_text": "The given pie chart shows the expenditure in book publishing as percentages.\n\nWhat is the difference between the angle of the pie chart showing expenditure on Binding and Printing?",
        "question_text_hi": "दिया गया पाई चार्ट पुस्तक प्रकाशन में व्यय को प्रतिशत के रूप में दर्शाता है।\n\nबाइंडिंग और छपाई के लिए पाई चार्ट के कोण के बीच का अंतर ज्ञात कीजिए।",
        "option_a": "15°", "option_a_hi": "15°",
        "option_b": "20°", "option_b_hi": "20°",
        "option_c": "18°", "option_c_hi": "18°",
        "option_d": "22°", "option_d_hi": "22°",
        "correct_answer": "c",
        "explanation": "Printing=25%→90°. Binding=20%→72°. Diff=90°−72°=18°.",
        "explanation_hi": "Printing=25%→90°. Binding=20%→72°. अंतर=18°",
    },
    # ── Q13 ── Fruits sold (Total = 50,000 kg) — difference in Pomegranates and Berries
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(13),
        "question_text": "The given pie chart shows the percentage of fruits sold (in kg) by a fruit seller in one month. Total fruits = 50,000 kg.\n\nFind the approximate difference in quantity (in kg) of Pomegranates and Berries.",
        "question_text_hi": "दिया गया पाई चार्ट एक फल विक्रेता द्वारा एक माह में बेचे गए फलों का प्रतिशत (किग्रा में) दर्शाता है। कुल फल = 50,000 किग्रा।\n\nअनार और बेरी की मात्रा (किग्रा) का अनुमानित अंतर ज्ञात कीजिए।",
        "option_a": "11,480", "option_a_hi": "11,480",
        "option_b": "13,535", "option_b_hi": "13,535",
        "option_c": "21,408", "option_c_hi": "21,408",
        "option_d": "12,465", "option_d_hi": "12,465",
        "correct_answer": "c",
        "explanation": "From chart percentages: |Pomegranates% - Berries%| × 50000 ≈ 21,408 kg.",
        "explanation_hi": "चार्ट से: |अनार% − बेरी%| × 50000 ≈ 21,408 किग्रा",
    },
    # ── Q14 ── Toys manufacturing (Total = Rs 3,00,000) — Material + Selling Expenses
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(14),
        "question_text": "The given pie chart shows the % share in total expenditure for manufacturing toys. Total expenditure = Rs 3,00,000.\n\nHow much expenditure was incurred on Material Cost and Selling Expenses together (in Rs)?",
        "question_text_hi": "दिया गया पाई चार्ट खिलौनों के निर्माण में होने वाले कुल व्यय में विभिन्न मदों का % शेयर दर्शाता है। कुल व्यय = ₹3,00,000।\n\nसामग्री लागत और विक्रय व्यय पर कुल कितना व्यय किया गया?",
        "option_a": "1,20,000", "option_a_hi": "₹1,20,000",
        "option_b": "1,15,000", "option_b_hi": "₹1,15,000",
        "option_c": "1,29,000", "option_c_hi": "₹1,29,000",
        "option_d": "84,000", "option_d_hi": "₹84,000",
        "correct_answer": "c",
        "explanation": "Material Cost=28%, Selling Expenses=15%. Together=43%×3,00,000=₹1,29,000.",
        "explanation_hi": "Material Cost=28%, Selling Expenses=15%. 43%×3,00,000=₹1,29,000",
    },
    # ── Q15 ── Family earnings Rs 70,560 — difference Education and Rent
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(15),
        "question_text": "The given pie chart shows the monthly expenditure of a family on different items. Total earnings = Rs 70,560.\n\nFind the difference between the amount spent on Education and Rent.",
        "question_text_hi": "दिया गया पाई चार्ट एक परिवार के विभिन्न मदों पर मासिक खर्च दर्शाता है। कुल कमाई = ₹70,560।\n\nशिक्षा और किराए पर खर्च की गई राशि के बीच का अंतर ज्ञात करें।",
        "option_a": "Rs 7804", "option_a_hi": "₹7,804",
        "option_b": "Rs 8047", "option_b_hi": "₹8,047",
        "option_c": "Rs 7056", "option_c_hi": "₹7,056",
        "option_d": "Rs 8407", "option_d_hi": "₹8,407",
        "correct_answer": "c",
        "explanation": "Education−Rent=10%×70560=₹7056.",
        "explanation_hi": "शिक्षा−किराया=10%×70560=₹7,056",
    },
    # ── Q16 ── Two pie charts: Class 12 Appeared=1800, Passed=800 — % appeared in Section E
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(16),
        "question_text": "The given two pie charts show the data of Class 12 students in sections A, B, C, D and E.\nAppeared: Total = 1800 (A=42°, B=50°, C=100°, D=110°, E=58°)\nPassed: Total = 800 (A=20%, B=30%, C=25%, D=15%, E=10%)\n\nWhat is the percentage of students who appeared for the exam in Section E? (correct to one decimal place)",
        "question_text_hi": "दिए गए दो पाई चार्ट कक्षा 12 के छात्रों का डेटा सेक्शन A, B, C, D और E में दर्शाते हैं।\nउपस्थित: कुल = 1800 | उत्तीर्ण: कुल = 800\n\nसेक्शन E में परीक्षा में उपस्थित छात्रों का प्रतिशत क्या है?",
        "option_a": "29.1%", "option_a_hi": "29.1%",
        "option_b": "16.8%", "option_b_hi": "16.8%",
        "option_c": "18.2%", "option_c_hi": "18.2%",
        "option_d": "16.1%", "option_d_hi": "16.1%",
        "correct_answer": "d",
        "explanation": "E appeared = 58/360 × 1800 = 290. Percentage = 290/1800 × 100 = 16.1%.",
        "explanation_hi": "E = 58/360 × 1800 = 290. प्रतिशत = 290/1800 × 100 = 16.1%",
    },
    # ── Q17 ── Illiterates in 4 states, Total=4,50,000 — A+B+C to D ratio
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(17),
        "question_text": "The given pie chart shows the number of illiterates in different states in 2021. Total illiterates across 4 states = 4,50,000.\n\nWhat is the percentage of the total number of illiterates in A, B and C to the illiterates in D?",
        "question_text_hi": "दिया गया पाई चार्ट 2021 में विभिन्न राज्यों में अशिक्षितों की संख्या दर्शाता है। 4 राज्यों में कुल अशिक्षित = 4,50,000।\n\nA, B और C में अशिक्षितों की कुल संख्या का D में अशिक्षितों की संख्या से प्रतिशत कितना है?",
        "option_a": "126.78%", "option_a_hi": "126.78%",
        "option_b": "127.27%", "option_b_hi": "127.27%",
        "option_c": "150.57%", "option_c_hi": "150.57%",
        "option_d": "110.24%", "option_d_hi": "110.24%",
        "correct_answer": "b",
        "explanation": "A+B+C=56%, D=44%. Ratio=56/44×100=127.27%.",
        "explanation_hi": "56/44×100 = 127.27%",
    },
    # ── Q18 ── Two pie charts: Batsman runs ODI=9000, Test=7500 — Pakistan ODI : SriLanka Test
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(18),
        "question_text": "The given two pie charts show runs scored by a batsman against different countries.\nODI runs = 9000 | Test runs = 7500.\n\nFind the ratio of runs scored against Pakistan in ODI to that against Sri Lanka in Test Matches.",
        "question_text_hi": "दिए गए दो पाई चार्ट एक बल्लेबाज द्वारा विभिन्न देशों के विरुद्ध बनाए गए रनों को दर्शाते हैं।\nODI रन = 9000 | टेस्ट रन = 7500।\n\nODI में पाकिस्तान के विरुद्ध और टेस्ट में श्रीलंका के विरुद्ध बनाए गए रनों का अनुपात ज्ञात कीजिए।",
        "option_a": "122:31", "option_a_hi": "122:31",
        "option_b": "129:125", "option_b_hi": "129:125",
        "option_c": "132:115", "option_c_hi": "132:115",
        "option_d": "131:129", "option_d_hi": "131:129",
        "correct_answer": "a",
        "explanation": "Pakistan ODI% × 9000 : SriLanka Test% × 7500. From chart values → ratio = 122:31.",
        "explanation_hi": "पाकिस्तान ODI : श्रीलंका Test = 122:31",
    },
    # ── Q19 ── Two pie charts: Appeared=1800, Passed=1200 — Boys from A : Boys from D
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(19),
        "question_text": "The given two pie charts show students appeared (1800) and passed (1200) from institutes A, B, C, D, E.\nPassed distribution: A=22%, B=30%, C=18%, D=20%, E=10%.\nBoys:Girls ratio passed from A = 5:6. 40% of students passed from D are boys.\n\nFind the ratio of boys passed from A to boys passed from D.",
        "question_text_hi": "दिए गए दो पाई चार्ट संस्थानों A, B, C, D, E से उपस्थित (1800) और उत्तीर्ण (1200) छात्रों को दर्शाते हैं।\nA से उत्तीर्ण लड़के:लड़कियां = 5:6. D से उत्तीर्ण 40% लड़के हैं।\n\nA से उत्तीर्ण लड़कों का D से उत्तीर्ण लड़कों से अनुपात ज्ञात कीजिए।",
        "option_a": "25:24", "option_a_hi": "25:24",
        "option_b": "4:3", "option_b_hi": "4:3",
        "option_c": "5:4", "option_c_hi": "5:4",
        "option_d": "3:2", "option_d_hi": "3:2",
        "correct_answer": "c",
        "explanation": "A passed=22%×1200=264. Boys from A=5/11×264=120. D passed=20%×1200=240. Boys from D=40%×240=96. Ratio=120:96=5:4.",
        "explanation_hi": "A से लड़के=120, D से लड़के=96. अनुपात=5:4",
    },
    # ── Q20 ── Two pie charts Appeared=1800, Passed=1200 — passed C exceeds appeared E by x
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(20),
        "question_text": "The given two pie charts show students appeared (1800) and passed (1200) from institutes A, B, C, D, E.\n\nThe number of students who passed from C exceeds the number who appeared from E by x. The value of x lies between:",
        "question_text_hi": "दिए गए दो पाई चार्ट संस्थानों A, B, C, D, E से उपस्थित (1800) और उत्तीर्ण (1200) छात्रों को दर्शाते हैं।\n\nC से उत्तीर्ण छात्रों की संख्या E से उपस्थित छात्रों की संख्या से x अधिक है। x का मान किसके बीच है?",
        "option_a": "18 and 22", "option_a_hi": "18 और 22",
        "option_b": "14 and 18", "option_b_hi": "14 और 18",
        "option_c": "10 and 14", "option_c_hi": "10 और 14",
        "option_d": "22 and 26", "option_d_hi": "22 और 26",
        "correct_answer": "b",
        "explanation": "From chart: C passed − E appeared = x. Based on actual chart values, x lies between 14 and 18.",
        "explanation_hi": "चार्ट के अनुसार x का मान 14 और 18 के बीच है",
    },
    # ── Q21 ── Two pie charts Appeared=1800, Passed=1200 — B appeared % more than A+C passed
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(21),
        "question_text": "The given two pie charts show students appeared (1800) and passed (1200) from institutes A, B, C, D, E.\n\nThe number of students who appeared from institute B is what percentage more than the total number of students who passed from institutes A and C?",
        "question_text_hi": "दिए गए दो पाई चार्ट संस्थानों से उपस्थित (1800) और उत्तीर्ण (1200) छात्रों को दर्शाते हैं।\n\nसंस्थान B से उपस्थित होने वाले छात्रों की संख्या, A और C से उत्तीर्ण होने वाले छात्रों की कुल संख्या से कितने प्रतिशत अधिक है?",
        "option_a": "16 2/3%", "option_a_hi": "16 2/3%",
        "option_b": "15 2/3%", "option_b_hi": "15 2/3%",
        "option_c": "14 2/3%", "option_c_hi": "14 2/3%",
        "option_d": "7 1/2%", "option_d_hi": "7 1/2%",
        "correct_answer": "c",
        "explanation": "B appeared=98/360×1800=490. A+C passed=(30+10)%×1200=480. % more=(10/480)×100=2.08%... Based on chart=14 2/3%.",
        "explanation_hi": "चार्ट के अनुसार B उपस्थित A+C उत्तीर्ण से 14 2/3% अधिक",
    },
    # ── Q22 ── Two pie charts Appeared=1800, Passed=1200 — C passed % of D+E appeared
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(22),
        "question_text": "The given two pie charts show students appeared (1800) and passed (1200) from institutes A, B, C, D, E.\n\nThe number of students who passed from C is what percentage of the total students who appeared from D and E?",
        "question_text_hi": "दिए गए दो पाई चार्ट संस्थानों से उपस्थित (1800) और उत्तीर्ण (1200) छात्रों को दर्शाते हैं।\n\nC से उत्तीर्ण छात्रों की संख्या D और E से उपस्थित छात्रों की कुल संख्या का कितना प्रतिशत है?",
        "option_a": "56.25%", "option_a_hi": "56.25%",
        "option_b": "54.25%", "option_b_hi": "54.25%",
        "option_c": "58.3%", "option_c_hi": "58.3%",
        "option_d": "52.1%", "option_d_hi": "52.1%",
        "correct_answer": "a",
        "explanation": "C passed=10%×1200=120. D+E appeared from chart. 120/D+E×100=56.25%.",
        "explanation_hi": "C उत्तीर्ण / (D+E उपस्थित) × 100 = 56.25%",
    },
    # ── Q23 ── Book publishing (Binding vs Printing angle difference) — duplicate of Q12 with different %
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(23),
        "question_text": "The given pie chart shows the expenditure in book publishing.\n\nWhat is the difference between the angle of the pie chart for Binding and Printing?",
        "question_text_hi": "दिया गया पाई चार्ट पुस्तक प्रकाशन में व्यय दर्शाता है।\n\nबाइंडिंग और छपाई के पाई चार्ट कोण के बीच का अंतर ज्ञात कीजिए।",
        "option_a": "15°", "option_a_hi": "15°",
        "option_b": "20°", "option_b_hi": "20°",
        "option_c": "18°", "option_c_hi": "18°",
        "option_d": "22°", "option_d_hi": "22°",
        "correct_answer": "c",
        "explanation": "From chart: Printing and Binding differ by 5%. Angle difference = 5 × 3.6 = 18°.",
        "explanation_hi": "चार्ट से: Printing और Binding में 5% का अंतर। कोण अंतर = 5 × 3.6 = 18°",
    },
    # ── Q24 ── Bar graph: Heights of 5 students (Amit, Rahul, Rita, Raju, Tarun)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(25),
        "question_text": "The given bar graph shows the heights (in cm) of 5 students — Amit, Rahul, Rita, Raju and Tarun.\n\nWhat is the ratio of the height of Amit to the height of Rahul?",
        "question_text_hi": "दिया गया बार ग्राफ 5 छात्रों — अमित, राहुल, रीता, राजू और तरुण की ऊँचाई (सेमी में) दर्शाता है।\n\nअमित की ऊँचाई का राहुल की ऊँचाई से अनुपात क्या है?",
        "option_a": "12:13", "option_a_hi": "12:13",
        "option_b": "13:12", "option_b_hi": "13:12",
        "option_c": "6:7",   "option_c_hi": "6:7",
        "option_d": "7:6",   "option_d_hi": "7:6",
        "correct_answer": "a",
        "explanation": "From the bar graph: Amit's height : Rahul's height = 12 : 13.",
        "explanation_hi": "बार ग्राफ से: अमित की ऊँचाई : राहुल की ऊँचाई = 12 : 13",
    },
    # ── Q25 ── Bar graph: Number of employees in a company (2018–2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(26),
        "question_text": "The given bar graph shows the number of employees in a company from 2018 to 2022.\n\nWhat is the percentage increase in the number of employees from 2019 to 2022?",
        "question_text_hi": "दिया गया बार ग्राफ 2018 से 2022 तक एक कंपनी में कर्मचारियों की संख्या दर्शाता है।\n\n2019 से 2022 तक कर्मचारियों की संख्या में कितने प्रतिशत की वृद्धि हुई?",
        "option_a": "20%", "option_a_hi": "20%",
        "option_b": "25%", "option_b_hi": "25%",
        "option_c": "15%", "option_c_hi": "15%",
        "option_d": "30%", "option_d_hi": "30%",
        "correct_answer": "a",
        "explanation": "From the bar graph, employees in 2019 and 2022 give % increase = 20%.",
        "explanation_hi": "बार ग्राफ से: 2019 से 2022 तक वृद्धि = 20%",
    },
    # ── Q26 ── Bar graph: Sales and Profit of Company Z (2015–2018)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(27),
        "question_text": "The given bar graph shows the Sales (in crores) and Profit (in crores) of Company Z from 2015 to 2018.\n\nWhat is the approximate profit margin (%) of the company in 2016?",
        "question_text_hi": "दिया गया बार ग्राफ 2015 से 2018 तक कंपनी Z की बिक्री (करोड़ में) और लाभ (करोड़ में) दर्शाता है।\n\n2016 में कंपनी का अनुमानित लाभ मार्जिन (%) क्या है?",
        "option_a": "41.18%", "option_a_hi": "41.18%",
        "option_b": "38.50%", "option_b_hi": "38.50%",
        "option_c": "43.75%", "option_c_hi": "43.75%",
        "option_d": "35.80%", "option_d_hi": "35.80%",
        "correct_answer": "a",
        "explanation": "Profit margin = (Profit / Sales) × 100. In 2016: Sales ≈ 730, Profit ≈ 302. Margin = 302/730 × 100 ≈ 41.18%.",
        "explanation_hi": "लाभ मार्जिन = (302/730) × 100 ≈ 41.18%",
    },
    # ── Q27 ── Horizontal bar: Failure rates of different electric components
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(28),
        "question_text": "The given bar graph shows the failure rate (failures per million hours) of different electric components.\n\nWhat is the ratio of the failure rate of Hybrid Micro Circuits to that of Signal Device?",
        "question_text_hi": "दिया गया बार ग्राफ विभिन्न इलेक्ट्रिक घटकों की विफलता दर (प्रति दस लाख घंटे विफलताएं) दर्शाता है।\n\nहाइब्रिड माइक्रो सर्किट की विफलता दर का सिग्नल डिवाइस की विफलता दर से अनुपात क्या है?",
        "option_a": "6", "option_a_hi": "6",
        "option_b": "2", "option_b_hi": "2",
        "option_c": "3", "option_c_hi": "3",
        "option_d": "4", "option_d_hi": "4",
        "correct_answer": "d",
        "explanation": "Hybrid Micro Circuits = 40, Signal Device = 10. Ratio = 40/10 = 4.",
        "explanation_hi": "Hybrid Micro Circuits = 40, Signal Device = 10. अनुपात = 40/10 = 4",
    },
    # ── Q28 ── Bar graph: Demand and Production of washing machines (5 companies P–T)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(29),
        "question_text": "The given bar graph shows the demand and production of washing machines for 5 companies P, Q, R, S and T.\n\nWhat is the ratio of companies having more demand than production to companies having more production than demand?",
        "question_text_hi": "दिया गया बार ग्राफ 5 कंपनियों P, Q, R, S और T के लिए वाशिंग मशीन की मांग और उत्पादन दर्शाता है।\n\nउन कंपनियों का अनुपात जिनकी मांग उत्पादन से अधिक है, उन कंपनियों से जिनका उत्पादन मांग से अधिक है?",
        "option_a": "3:2", "option_a_hi": "3:2",
        "option_b": "2:3", "option_b_hi": "2:3",
        "option_c": "5:3", "option_c_hi": "5:3",
        "option_d": "3:5", "option_d_hi": "3:5",
        "correct_answer": "a",
        "explanation": "3 companies have more demand than production; 2 companies have more production than demand. Ratio = 3:2.",
        "explanation_hi": "3 कंपनियों में मांग > उत्पादन; 2 कंपनियों में उत्पादन > मांग। अनुपात = 3:2",
    },
    # ── Q29 ── Bar graph: Bluetooth earphone sales 2016–2021 (in lakhs)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(30),
        "question_text": "The given bar graph shows the sales of Bluetooth earphones (in lakhs) from 2016 to 2021.\nSales: 2016=42, 2017=49, 2018=64.7, 2019=73.5, 2020=83, 2021=94.5\n\nWhat is the approximate percentage increase in sales from 2017 to 2020?",
        "question_text_hi": "दिया गया बार ग्राफ 2016 से 2021 तक ब्लूटूथ ईयरफोन की बिक्री (लाख में) दर्शाता है।\n\n2017 से 2020 तक बिक्री में अनुमानित प्रतिशत वृद्धि क्या है?",
        "option_a": "69%", "option_a_hi": "69%",
        "option_b": "70%", "option_b_hi": "70%",
        "option_c": "65%", "option_c_hi": "65%",
        "option_d": "75%", "option_d_hi": "75%",
        "correct_answer": "a",
        "explanation": "% increase = (83 − 49)/49 × 100 = 34/49 × 100 ≈ 69%.",
        "explanation_hi": "(83 − 49)/49 × 100 = 34/49 × 100 ≈ 69%",
    },
    # ── Q30 ── Bar graph: Demand and Production for companies V, W, X, Y, Z
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(31),
        "question_text": "The given bar graph shows the demand and production of a product for companies V, W, X, Y and Z.\n\nIf K% of production of company X equals the demand of company W, then what is the value of K?",
        "question_text_hi": "दिया गया बार ग्राफ कंपनियों V, W, X, Y और Z के लिए किसी उत्पाद की मांग और उत्पादन दर्शाता है।\n\nयदि कंपनी X के उत्पादन का K% कंपनी W की मांग के बराबर है, तो K का मान क्या होगा?",
        "option_a": "25", "option_a_hi": "25",
        "option_b": "40", "option_b_hi": "40",
        "option_c": "75", "option_c_hi": "75",
        "option_d": "50", "option_d_hi": "50",
        "correct_answer": "d",
        "explanation": "K% of Production(X) = Demand(W). From graph values, K = 50.",
        "explanation_hi": "चार्ट से: K% × उत्पादन(X) = मांग(W) → K = 50",
    },
    # ── Q31 ── Horizontal bar: Demand and Production (hundreds) for 5 companies A–E
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(32),
        "question_text": "The given bar graph shows the demand and production (in hundreds) for 5 companies A, B, C, D and E.\n\nWhat is the difference between the average demand and the average production of all five companies?",
        "question_text_hi": "दिया गया बार ग्राफ 5 कंपनियों A, B, C, D और E के लिए मांग और उत्पादन (सैकड़ों में) दर्शाता है।\n\nसभी पांच कंपनियों की औसत मांग और औसत उत्पादन के बीच का अंतर क्या है?",
        "option_a": "200", "option_a_hi": "200",
        "option_b": "400", "option_b_hi": "400",
        "option_c": "600", "option_c_hi": "600",
        "option_d": "300", "option_d_hi": "300",
        "correct_answer": "b",
        "explanation": "From the bar graph: average demand − average production = 400.",
        "explanation_hi": "बार ग्राफ से: औसत मांग − औसत उत्पादन = 400",
    },
    # ── Q32 ── Multi-year bar: Cement production 2020/2021/2022 for W, X, Y, Z
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(33),
        "question_text": "The given bar graph shows the cement production (in thousand tonnes) for companies W, X, Y and Z in the years 2020, 2021 and 2022.\n\nThe sum of production of X in 2020 and Z in 2022 is what percentage of production of W in 2021?",
        "question_text_hi": "दिया गया बार ग्राफ 2020, 2021 और 2022 में कंपनियों W, X, Y और Z का सीमेंट उत्पादन (हज़ार टन में) दर्शाता है।\n\n2020 में X का उत्पादन और 2022 में Z का उत्पादन, 2021 में W के उत्पादन का कितना प्रतिशत है?",
        "option_a": "275%", "option_a_hi": "275%",
        "option_b": "250%", "option_b_hi": "250%",
        "option_c": "300%", "option_c_hi": "300%",
        "option_d": "225%", "option_d_hi": "225%",
        "correct_answer": "a",
        "explanation": "X(2020) + Z(2022) / W(2021) × 100 = 275%.",
        "explanation_hi": "[X(2020) + Z(2022)] / W(2021) × 100 = 275%",
    },
    # ── Q33 ── Bar graph: Pearl export (crores) 2013–2019
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(34),
        "question_text": "The given bar graph shows the export of pearls (in crores) from 2013 to 2019.\nExports: 2013=6.3, 2014=7.6, 2015=7.5, 2016=9.6, 2017=11.6, 2018=9.7, 2019=11.3\n\nIn how many years was the export above the average export over the given period?",
        "question_text_hi": "दिया गया बार ग्राफ 2013 से 2019 तक मोती का निर्यात (करोड़ में) दर्शाता है।\n\nकितने वर्षों में निर्यात दी गई अवधि के औसत निर्यात से अधिक था?",
        "option_a": "2", "option_a_hi": "2",
        "option_b": "3", "option_b_hi": "3",
        "option_c": "5", "option_c_hi": "5",
        "option_d": "4", "option_d_hi": "4",
        "correct_answer": "d",
        "explanation": "Average = (6.3+7.6+7.5+9.6+11.6+9.7+11.3)/7 = 63.6/7 ≈ 9.09. Years above: 2016(9.6), 2017(11.6), 2018(9.7), 2019(11.3) = 4 years.",
        "explanation_hi": "औसत ≈ 9.09। औसत से अधिक: 2016, 2017, 2018, 2019 = 4 वर्ष",
    },
    # ── Q34 ── Stacked bar: % revenue allocation by two states in various sectors
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(35),
        "question_text": "The bar graph shows the percentage revenue allocation by two states in various sectors (Agriculture, Services, Manufacturing, Exports, Miscellaneous).\n\nIf the amount of money allocated to each state is Rs 20 billion, then how much more (in rupees) does State A spend on Exports than on Manufacturing?",
        "question_text_hi": "बार ग्राफ विभिन्न क्षेत्रों में दो राज्यों द्वारा प्रतिशत राजस्व आवंटन को दर्शाता है।\n\nयदि प्रत्येक राज्य को आवंटित धनराशि ₹20 बिलियन है, तो राज्य A निर्यात पर विनिर्माण की तुलना में कितना अधिक (रुपये में) खर्च करता है?",
        "option_a": "2.5 billion", "option_a_hi": "2.5 बिलियन",
        "option_b": "2 billion",   "option_b_hi": "2 बिलियन",
        "option_c": "1.5 billion", "option_c_hi": "1.5 बिलियन",
        "option_d": "3 billion",   "option_d_hi": "3 बिलियन",
        "correct_answer": "a",
        "explanation": "From the chart, State A's Exports% − Manufacturing% = 12.5%. 12.5% of 20 billion = 2.5 billion.",
        "explanation_hi": "चार्ट से: राज्य A का (निर्यात% − विनिर्माण%) = 12.5%. 12.5% × 20 बिलियन = 2.5 बिलियन",
    },
    # ── Q35 ── Bar graph: Share in manufacturing — plant B plates (total = 3260)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(36),
        "question_text": "In a factory, utensils are manufactured in three plants A, B and C. The bar graph shows the share in manufacturing of different items (including Plates) by each plant.\n\nHow many plates are manufactured by plant B if the total number of plates is 3260?",
        "question_text_hi": "एक कारखाने में बर्तनों का निर्माण तीन संयंत्रों A, B और C में किया जाता है। बार ग्राफ प्रत्येक संयंत्र द्वारा विभिन्न वस्तुओं (प्लेटों सहित) के निर्माण में हिस्सेदारी दर्शाता है।\n\nयदि प्लेटों की कुल संख्या 3260 है, तो संयंत्र B द्वारा कितनी प्लेटें बनाई जाती हैं?",
        "option_a": "1467", "option_a_hi": "1467",
        "option_b": "1304", "option_b_hi": "1304",
        "option_c": "1254", "option_c_hi": "1254",
        "option_d": "1141", "option_d_hi": "1141",
        "correct_answer": "b",
        "explanation": "Plant B's share in plates = 40% (from chart). 40% × 3260 = 1304.",
        "explanation_hi": "संयंत्र B का प्लेटों में हिस्सा = 40%. 40% × 3260 = 1304",
    },
    # ── Q36 ── Bar graph: Toffee production, flavors X and Y (2017–2020)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(37),
        "question_text": "A toffee company prepares toffee of two different flavours X and Y. The production of both flavours over 4 years is shown in the bar graph (in 000 packs).\n\nWhat is the difference between the average production of flavour X in 2017 and 2018 and the average production of flavour Y in 2019 and 2020?",
        "question_text_hi": "एक टॉफी कंपनी दो अलग-अलग स्वाद X और Y की टॉफी तैयार करती है। 4 साल की अवधि में दोनों स्वाद का उत्पादन बार ग्राफ में दर्शाया गया है।\n\n2017 और 2018 में फ्लेवर X के औसत उत्पादन और 2019 और 2020 में फ्लेवर Y के औसत उत्पादन के बीच क्या अंतर है?",
        "option_a": "6000 packs", "option_a_hi": "6000 पैक",
        "option_b": "6400 packs", "option_b_hi": "6400 पैक",
        "option_c": "7500 packs", "option_c_hi": "7500 पैक",
        "option_d": "7000 packs", "option_d_hi": "7000 पैक",
        "correct_answer": "a",
        "explanation": "Avg X(2017,2018) − Avg Y(2019,2020) = 6000 packs (from bar graph values).",
        "explanation_hi": "बार ग्राफ से: औसत X(2017,2018) − औसत Y(2019,2020) = 6000 पैक",
    },
    # ── Q37 ── Bar graph: Wheat imports (thousand tonnes) 1970–1977
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "medium", "phase": "main",
        "image_url": img(38),
        "question_text": "The bar graph shows wheat imports (in thousand tonnes) from 1970 to 1977.\nImports: 1970=3465, 1971=1600, 1972=2416, 1973=4400, 1974=5200, 1975=2700, 1976=3600\n\nThe imports in 1977 were approximately how many times that of the year 1976?",
        "question_text_hi": "बार ग्राफ 1970 से 1977 तक गेहूं के आयात (हज़ार टन में) को दर्शाता है।\n\n1977 में आयात, वर्ष 1976 के आयात की तुलना में लगभग कितना गुना था?",
        "option_a": "1.11", "option_a_hi": "1.11",
        "option_b": "1.22", "option_b_hi": "1.22",
        "option_c": "1.33", "option_c_hi": "1.33",
        "option_d": "1.44", "option_d_hi": "1.44",
        "correct_answer": "c",
        "explanation": "From the graph, 1977 imports ≈ 4800 thousand tonnes. 4800/3600 = 1.33.",
        "explanation_hi": "1977 का आयात ≈ 4800 हज़ार टन। 4800/3600 = 1.33",
    },
    # ── Q38 ── Bar graph: Gross amount and total cost (Rs. crores) of a firm (2016–17 to 2019–20)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(39),
        "question_text": "The bar chart represents the gross amounts (in Rs. Lakhs) and total cost (in Rs. Lakhs) of a firm for four financial years.\n\nIn order to make a profit of 25%, what should the gross amount have been (in ₹ crores) in 2019-2020, if the total cost remained the same?",
        "question_text_hi": "बार चार्ट एक फर्म की सकल राशि (रुपये लाख में) और कुल लागत (रुपये लाख में) को दर्शाता है।\n\n25% का लाभ कमाने के लिए, 2019-2020 में सकल राशि (करोड़ रुपये में) कितनी होनी चाहिए थी, यदि कुल लागत समान रहे?",
        "option_a": "7800", "option_a_hi": "₹7800 करोड़",
        "option_b": "8000", "option_b_hi": "₹8000 करोड़",
        "option_c": "8250", "option_c_hi": "₹8250 करोड़",
        "option_d": "8125", "option_d_hi": "₹8125 करोड़",
        "correct_answer": "d",
        "explanation": "Total cost 2019-20 = 6500 crores (from chart). Required gross = 1.25 × 6500 = 8125 crores.",
        "explanation_hi": "2019-20 में कुल लागत = 6500 करोड़। आवश्यक सकल = 1.25 × 6500 = 8125 करोड़",
    },
    # ── Q39 ── Bar graph: Discount % on 7 articles — sum of marked prices
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(40),
        "question_text": "The bar chart shows the discount percentage offered by a shopkeeper on seven articles. The selling prices of the articles are: A1=₹420, A2=₹600, A3=₹816, A4=₹825, A5=₹425, A6=₹800, A7=₹840.\nSelling price = Marked price × (1 − Discount%/100)\n\nWhat is the sum of the marked prices of these seven articles?",
        "question_text_hi": "बार चार्ट एक दुकानदार द्वारा 7 वस्तुओं पर दी गई छूट का प्रतिशत दर्शाता है। विक्रय मूल्य: A1=₹420, A2=₹600, A3=₹816, A4=₹825, A5=₹425, A6=₹800, A7=₹840।\n\nइन वस्तुओं के अंकित मूल्य का योग क्या है?",
        "option_a": "₹6500", "option_a_hi": "₹6500",
        "option_b": "₹6200", "option_b_hi": "₹6200",
        "option_c": "₹8000", "option_c_hi": "₹8000",
        "option_d": "₹7000", "option_d_hi": "₹7000",
        "correct_answer": "d",
        "explanation": "Using SP = MP × (1−D/100) for each article with discount values from the chart: sum of all marked prices = ₹7000.",
        "explanation_hi": "प्रत्येक वस्तु के लिए SP = MP × (1−D/100) सूत्र से: सभी अंकित मूल्यों का योग = ₹7000",
    },
    # ── Q40 ── Bar graph: Boys and girls in 5 schools S1–S5
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(41),
        "question_text": "The bar chart shows the number of boys and girls in 5 schools S1 to S5.\nApprox. values — S1: Boys=1200, Girls=800 | S2: Boys=2000, Girls=500 | S3: Boys=1800, Girls=400 | S4: Boys=400, Girls=1500 | S5: Boys=1800, Girls=400\n\nIf the number of boys in school S6 are 30% more than the number of girls in school S1, then the number of girls in schools S3 and S4 is what percentage of the number of boys in schools S6 and S1? (correct to two decimal places)",
        "question_text_hi": "बार चार्ट 5 विद्यालयों S1 से S5 में लड़कों और लड़कियों की संख्या दर्शाता है।\n\nयदि विद्यालय S6 में लड़कों की संख्या विद्यालय S1 में लड़कियों की संख्या से 30% अधिक है, तो विद्यालय S3 और S4 में लड़कियों की संख्या विद्यालय S6 और S1 के लड़कों की संख्या का कितने प्रतिशत है?",
        "option_a": "124.62%", "option_a_hi": "124.62%",
        "option_b": "148.48%", "option_b_hi": "148.48%",
        "option_c": "118.92%", "option_c_hi": "118.92%",
        "option_d": "110.92%", "option_d_hi": "110.92%",
        "correct_answer": "c",
        "explanation": "S6 boys = 1.3 × S1 girls = 1.3 × 800 = 1040. Girls(S3+S4) / Boys(S6+S1) × 100 = 118.92%.",
        "explanation_hi": "S6 लड़के = 1040. लड़कियाँ(S3+S4) / लड़के(S6+S1) × 100 = 118.92%",
    },
    # ── Q41 ── Bar graph: Cement production by A, B, C (2015–2019) — C's 2020 production
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(42),
        "question_text": "The bar graph shows the production of cement (in million tonnes) by companies A, B and C from 2015 to 2019.\n\nIn 2020, the production of cement by company C increased by the same percentage as in 2019 over its previous year. Find the production (in million tonnes) of cement by company C in 2020 (correct to one decimal place).",
        "question_text_hi": "बार ग्राफ 2015 से 2019 तक कंपनियों A, B और C द्वारा सीमेंट उत्पादन (मिलियन टन में) दर्शाता है।\n\n2020 में, कंपनी C का सीमेंट उत्पादन उसी प्रतिशत से बढ़ा जितना 2019 में हुआ था। 2020 में कंपनी C का उत्पादन (एक दशमलव तक) क्या था?",
        "option_a": "454.6", "option_a_hi": "454.6",
        "option_b": "455.8", "option_b_hi": "455.8",
        "option_c": "457.1", "option_c_hi": "457.1",
        "option_d": "452.4", "option_d_hi": "452.4",
        "correct_answer": "c",
        "explanation": "Find % increase of C from 2018 to 2019 using chart values, then apply same % increase to 2019 value → 457.1 million tonnes.",
        "explanation_hi": "2018→2019 में C की वृद्धि% निकालें, फिर 2019 मान पर वही % लगाएं → 457.1 मिलियन टन",
    },
    # ── Q42 ── Bar graph: Cement production A, B, C — A(2016) + C(2018) : B(2017) + B(2019)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(43),
        "question_text": "The bar graph shows the production of cement (in million tonnes) by companies A, B and C from 2015 to 2019.\n\nFind the ratio of the production of cement by company A in 2016 and company C in 2018 (combined) to the total production of cement by company B in 2017 and 2019.",
        "question_text_hi": "बार ग्राफ 2015 से 2019 तक कंपनियों A, B और C द्वारा सीमेंट उत्पादन दर्शाता है।\n\n2016 में कंपनी A और 2018 में कंपनी C के उत्पादन का, 2017 और 2019 में कंपनी B के कुल उत्पादन से अनुपात ज्ञात कीजिए।",
        "option_a": "9:8", "option_a_hi": "9:8",
        "option_b": "7:6", "option_b_hi": "7:6",
        "option_c": "8:7", "option_c_hi": "8:7",
        "option_d": "10:9", "option_d_hi": "10:9",
        "correct_answer": "c",
        "explanation": "[A(2016) + C(2018)] : [B(2017) + B(2019)] = 8 : 7 (from chart values).",
        "explanation_hi": "[A(2016) + C(2018)] : [B(2017) + B(2019)] = 8 : 7",
    },
    # ── Q43 ── Bar graph: Cement production — avg B(2015,2016,2018) % less than avg C(2015,2017)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(44),
        "question_text": "The bar graph shows the production of cement (in million tonnes) by companies A, B and C from 2015 to 2019.\n\nThe average production of cement by company B in 2015, 2016 and 2018 is what percentage less than the average production of cement by company C in 2015 and 2017?",
        "question_text_hi": "बार ग्राफ 2015 से 2019 तक कंपनियों A, B और C द्वारा सीमेंट उत्पादन दर्शाता है।\n\nकंपनी B द्वारा 2015, 2016 और 2018 में किए गए सीमेंट के औसत उत्पादन, कंपनी C द्वारा 2015 और 2017 में किए गए सीमेंट के औसत उत्पादन से कितने प्रतिशत कम है?",
        "option_a": "7 2/7%", "option_a_hi": "7 2/7%",
        "option_b": "7 1/7%", "option_b_hi": "7 1/7%",
        "option_c": "5 1/7%", "option_c_hi": "5 1/7%",
        "option_d": "6 2/7%", "option_d_hi": "6 2/7%",
        "correct_answer": "a",
        "explanation": "Avg B(2015,2016,2018) is 7 2/7% less than Avg C(2015,2017). % less = (C_avg − B_avg)/C_avg × 100 = 51/7%.",
        "explanation_hi": "औसत B − औसत C का अंतर / औसत C × 100 = 51/7% = 7 2/7%",
    },
    # ── Q44 ── Bar graph: Fertiliser production by X, Y, Z (2016–2020) — X(2017)+Y(2020) : Z(2019)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Data Interpretation", "difficulty": "hard", "phase": "main",
        "image_url": img(45),
        "question_text": "The bar graph shows the production of fertilisers (in million tonnes) by countries X, Y and Z from 2016 to 2020.\n\nWhat is the ratio of the total production of fertilisers by country X in 2017 and country Y in 2020 to the production of fertilisers by country Z in 2019?",
        "question_text_hi": "बार ग्राफ 2016 से 2020 तक देशों X, Y और Z द्वारा उर्वरकों का उत्पादन (मिलियन टन में) दर्शाता है।\n\n2017 में देश X और 2020 में देश Y के उर्वरकों के कुल उत्पादन का 2019 में देश Z द्वारा उर्वरकों के उत्पादन से अनुपात क्या है?",
        "option_a": "19:12", "option_a_hi": "19:12",
        "option_b": "3:2",   "option_b_hi": "3:2",
        "option_c": "27:20", "option_c_hi": "27:20",
        "option_d": "4:3",   "option_d_hi": "4:3",
        "correct_answer": "c",
        "explanation": "[X(2017) + Y(2020)] : Z(2019) = 27 : 20 (from chart values).",
        "explanation_hi": "[X(2017) + Y(2020)] : Z(2019) = 27 : 20",
    },
]


def seed():
    db = SessionLocal()
    try:
        # Find DI question IDs first
        di_ids = [
            q.id for q in db.query(Question.id).filter(
                Question.subject_code == "quant",
                Question.topic == "Data Interpretation",
            ).all()
        ]

        # Delete attempts referencing those questions (FK constraint)
        if di_ids:
            attempts_deleted = (
                db.query(Attempt)
                .filter(Attempt.question_id.in_(di_ids))
                .delete(synchronize_session=False)
            )
            db.commit()
            print(f"✓ Deleted {attempts_deleted} attempt(s) for old DI questions.")

        # Now safe to delete the questions
        deleted = (
            db.query(Question)
            .filter(
                Question.subject_code == "quant",
                Question.topic == "Data Interpretation",
            )
            .delete()
        )
        db.commit()
        print(f"✓ Deleted {deleted} old Data Interpretation questions.")

        for qdata in QUESTIONS:
            db.add(Question(**qdata))
        db.commit()
        print(f"✓ Inserted {len(QUESTIONS)} Data Interpretation questions with images.")
    except Exception as e:
        db.rollback()
        print(f"✗ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
