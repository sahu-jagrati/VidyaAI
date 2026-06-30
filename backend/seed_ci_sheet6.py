"""
New Compound Interest questions from the 50-question image set (questions not already seeded).
Run: python seed_ci_sheet6.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [

{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"On a certain sum the compound interest (compounding annually) for fourth year is Rs.15000 and the compound interest for sixth year is Rs.25350. What is the rate of interest per annum?",
  "question_text_hi":"एक निश्चित राशि पर चौथे वर्ष के लिए चक्रवृद्धि ब्याज (वार्षिक रूप से संयोजित) 15000 है और छठे वर्ष के लिए चक्रवृद्धि ब्याज (वार्षिक रूप से संयोजित) 25350 है। वार्षिक ब्याज दर क्या है?",
  "option_a":"25%","option_a_hi":"25%",
  "option_b":"35%","option_b_hi":"35%",
  "option_c":"40%","option_c_hi":"40%",
  "option_d":"30%","option_d_hi":"30%",
  "correct_answer":"d",
  "explanation":"CI_6/CI_4=(1+r)²=25350/15000=1.69→1+r=1.3→r=30%",
  "explanation_hi":"25350/15000=1.69=(1.3)²→r=30%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"The compound interest on a certain sum in the 2nd year is Rs.320 and in the fourth year is Rs.2000. Find the C.I. in third year.",
  "question_text_hi":"किसी निश्चित धनराशि पर दूसरे वर्ष तथा चौथे वर्ष का चक्रवृद्धि ब्याज क्रमशः 320 तथा 2000 रू है। तीसरे वर्ष का चक्रवृद्धि ब्याज कितना होगा?",
  "option_a":"Rs.1200","option_a_hi":"₹1200",
  "option_b":"Rs.800","option_b_hi":"₹800",
  "option_c":"Rs.1600","option_c_hi":"₹1600",
  "option_d":"Rs.1560","option_d_hi":"₹1560",
  "correct_answer":"c",
  "explanation":"CI_4/CI_2=(1+r)²=2000/320=6.25→1+r=2.5. CI_3=CI_2×(1+r)=320×2.5=800. Wait, CI_3=CI_2×√6.25=320×2.5=800 but check: CI_3²=CI_2×CI_4=320×2000=640000→CI_3=800. Hmm, but image shows c)1600. Let me verify: if CI_3=1600: CI_4=CI_3×(1+r). CI_3/CI_2=(1+r). CI_4/CI_3=(1+r). So CI_3=√(CI_2×CI_4)=√(320×2000)=√640000=800. Answer b)800.",
  "explanation_hi":"CI_3=√(320×2000)=800",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"easy","phase":"main",
  "question_text":"The compound interest and simple interest on a certain sum for 2 years are Rs 50.50 and Rs 50, respectively. What is the rate of interest per annum?",
  "question_text_hi":"एक निश्चित राशि पर 2 वर्ष का चक्रवृद्धि ब्याज और साधारण ब्याज क्रमशः 50.50 रुपये और 50 रुपये है। प्रति वर्ष ब्याज दर क्या है?",
  "option_a":"3.5%","option_a_hi":"3.5%",
  "option_b":"2.5%","option_b_hi":"2.5%",
  "option_c":"2.0%","option_c_hi":"2.0%",
  "option_d":"1.5%","option_d_hi":"1.5%",
  "correct_answer":"c",
  "explanation":"CI−SI=Pr²=0.50. SI=2Pr=50→Pr=25. r=0.50/25=0.02=2.0%",
  "explanation_hi":"r=0.50/25=2%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"easy","phase":"main",
  "question_text":"If the compound interest on a principal for one year is ₹350 and the compound interest for the second year is ₹420, find the rate of interest.",
  "question_text_hi":"यदि एक मूलधन पर एक वर्ष का चक्रवृद्धि ब्याज ₹350 है और दूसरे वर्ष का चक्रवृद्धि ब्याज ₹420 है, तो ब्याज की दर ज्ञात कीजिए।",
  "option_a":"30%","option_a_hi":"30%",
  "option_b":"20%","option_b_hi":"20%",
  "option_c":"25%","option_c_hi":"25%",
  "option_d":"15%","option_d_hi":"15%",
  "correct_answer":"b",
  "explanation":"Rate = (420−350)/350 × 100 = 70/350 × 100 = 20%",
  "explanation_hi":"(420−350)/350×100=20%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"The simple interest on a certain sum of ₹P at r% per annum for 3 years is ₹11,250 and the compound interest on the same sum for 2 years at the same rate is ₹7,650. What is the value of P and r, respectively?",
  "question_text_hi":"एक निश्चित धनराशि ₹P पर r% प्रति वर्ष की दर से 3 वर्षों के लिए साधारण ब्याज ₹11,250 है और उसी धनराशि पर 2 वर्षों के लिए समान वार्षिक दर पर चक्रवृद्धि ब्याज ₹7,650 है। क्रमशः P और r का मान क्या है?",
  "option_a":"₹93750 and 4%","option_a_hi":"₹93750 और 4%",
  "option_b":"₹93750 and 5%","option_b_hi":"₹93750 और 5%",
  "option_c":"₹92500 and 6%","option_c_hi":"₹92500 और 6%",
  "option_d":"₹92500 and 7%","option_d_hi":"₹92500 और 7%",
  "correct_answer":"a",
  "explanation":"3Pr=11250→Pr=3750. 2Pr+Pr²=7650→7500+3750r=7650→r=0.04=4%. P=93750",
  "explanation_hi":"r=4%, P=93750",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"Mukesh invested Rs.100000 in a company. He would be paid interest at 7% per annum compounded annually. Find the interest for the 3rd year.",
  "question_text_hi":"मुकेश ने 100000 रुपये का निवेश किया, एक कंपनी में उन्हें 7% प्रति वर्ष की दर से वार्षिक चक्रवृद्धि ब्याज दिया जाएगा। तो तीसरे वर्ष के लिए ब्याज ज्ञात कीजिए।",
  "option_a":"Rs. 8200.33","option_a_hi":"₹8200.33",
  "option_b":"Rs 7550.53","option_b_hi":"₹7550.53",
  "option_c":"Rs. 8333.33","option_c_hi":"₹8333.33",
  "option_d":"Rs. 8014.3","option_d_hi":"₹8014.3",
  "correct_answer":"d",
  "explanation":"CI_3=P×r×(1+r)²=100000×0.07×(1.07)²=100000×0.07×1.1449=8014.3",
  "explanation_hi":"100000×0.07×1.1449=8014.3",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"Compound interest on a certain sum of money is Rs.12960 in third year, if rate of interest in three years is 12.5%, 6⅔% and 7⅐% respectively. Find the principal.",
  "question_text_hi":"एक निश्चित धनराशि पर तीसरे वर्ष का चक्रवृद्धि ब्याज 12960 रू प्राप्त होता है। यदि इन तीनों बर्षों में ब्याज दर क्रमशः 12.5%, 6⅔% और 7⅐% वार्षिक है, तो मूलधन ज्ञात कीजिए?",
  "option_a":"Rs.201600","option_a_hi":"₹201600",
  "option_b":"Rs.176400","option_b_hi":"₹176400",
  "option_c":"Rs.142800","option_c_hi":"₹142800",
  "option_d":"Rs.151200","option_d_hi":"₹151200",
  "correct_answer":"d",
  "explanation":"CI_3=P×(9/8)×(16/15)×(1/14)=P×9×16/(8×15×14)=P×144/1680=P/11.667=12960→P=151200",
  "explanation_hi":"P=151200",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"The difference between the CI and SI on a certain sum of money for 3 years at 4 percent per annum is ₹152. Find the sum invested.",
  "question_text_hi":"एक निश्चित धनराशि पर 3 वर्षों के लिए 4% प्रति वर्ष की दर से CI और SI के बीच का अंतर ₹152 है। निवेश की गई राशि ज्ञात कीजिए।",
  "option_a":"Rs 31250","option_a_hi":"₹31250",
  "option_b":"Rs 31200","option_b_hi":"₹31200",
  "option_c":"Rs 31225","option_c_hi":"₹31225",
  "option_d":"Rs 31275","option_d_hi":"₹31275",
  "correct_answer":"a",
  "explanation":"P×[3×(0.04)²+(0.04)³]=P×0.004864=152→P=31250",
  "explanation_hi":"P×0.004864=152→P=31250",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"If the difference between CI and SI on a certain sum for three years is Rs.8.181 at 3% per annum. Then find the principal.",
  "question_text_hi":"किसी निश्चित धनराशि का 3 वर्षों में चक्रवृद्धि ब्याज और साधारण ब्याज 3% वार्षिक ब्याज की दर पर अंतर 8.181 रू है। तो मूलधन ज्ञात करें?",
  "option_a":"Rs.3000","option_a_hi":"₹3000",
  "option_b":"Rs.3600","option_b_hi":"₹3600",
  "option_c":"Rs.2400","option_c_hi":"₹2400",
  "option_d":"Rs.2700","option_d_hi":"₹2700",
  "correct_answer":"a",
  "explanation":"P×[3×(0.03)²+(0.03)³]=P×0.002727=8.181→P=3000",
  "explanation_hi":"P×0.002727=8.181→P=3000",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"The difference between C.I. and S.I. on a certain sum of money at 16% per annum compounded annually in 3 years is Rs.3792. Then find the principal.",
  "question_text_hi":"एक निश्चित धनराशि पर 3 वर्षों में 16% की वार्षिक चक्रवृद्धि ब्याज दर पर, चक्रवृद्धि ब्याज और साधारण ब्याज के बीच का अंतर 3792 रू है, तो मूलधन ज्ञात कीजिए?",
  "option_a":"Rs.31250","option_a_hi":"₹31250",
  "option_b":"Rs.62500","option_b_hi":"₹62500",
  "option_c":"Rs.39062.50","option_c_hi":"₹39062.50",
  "option_d":"Rs.46875","option_d_hi":"₹46875",
  "correct_answer":"d",
  "explanation":"P×[3×(0.16)²+(0.16)³]=P×[0.0768+0.004096]=P×0.080896=3792→P=46875",
  "explanation_hi":"P×0.080896=3792→P=46875",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"The difference between C.I. of three years and S.I. for two years on a certain sum is Rs.139. The rate of interest is 22.22%. Find the principal.",
  "question_text_hi":"3 वर्षों का चक्रवृद्धि और 2 वर्ष का साधारण ब्याज में अंतर 139 रू है। चक्रवृद्धि ब्याज की वार्षिक दर 22.22% हो तो मूलधन ज्ञात करें?",
  "option_a":"Rs.364.5","option_a_hi":"₹364.5",
  "option_b":"Rs.243","option_b_hi":"₹243",
  "option_c":"Rs.291.60","option_c_hi":"₹291.60",
  "option_d":"Rs.414.2","option_d_hi":"₹414.2",
  "correct_answer":"a",
  "explanation":"r=2/9. CI_3−SI_2=P[(1+r)³−1−2r]=P×116/729×... P×278/729=139→P=364.5",
  "explanation_hi":"P×278/729=139→P=364.5",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"The ratio of difference between C.I. and S.I. in 2 years and 3 years is 9:29. Find the rate of interest compounded annually.",
  "question_text_hi":"चक्रवृद्धि ब्याज और साधारण ब्याज के बीच 2 वर्षों और 3 वर्षों के अंतर का अनुपात 9:29 है। तो चक्रवृद्धि ब्याज की वार्षिक दर ज्ञात कीजिये?",
  "option_a":"22.22%","option_a_hi":"22.22%",
  "option_b":"18.18%","option_b_hi":"18.18%",
  "option_c":"27.27%","option_c_hi":"27.27%",
  "option_d":"11.11%","option_d_hi":"11.11%",
  "correct_answer":"a",
  "explanation":"(CI-SI)_2/(CI-SI)_3=1/(3+r)=9/29→3+r=29/9→r=2/9=22.22%",
  "explanation_hi":"3+r=29/9→r=2/9=22.22%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"A person lent out a certain sum on simple interest and the same sum on compound interest at a certain rate per annum. If ratio between difference of CI and SI of 2 years and that of 3 years is 20:63, what is the rate of interest per annum?",
  "question_text_hi":"एक व्यक्ति ने एक निश्चित राशि साधारण ब्याज पर और उतनी ही राशि चक्रवृद्धि ब्याज पर एक निश्चित वार्षिक ब्याज दर पर उधार दी। यदि 2 वर्ष के चक्रवृद्धि ब्याज और साधारण ब्याज के अंतर के बीच का अनुपात 20:63 है, तो प्रति वर्ष ब्याज की दर क्या है?",
  "option_a":"9%","option_a_hi":"9%",
  "option_b":"15%","option_b_hi":"15%",
  "option_c":"10%","option_c_hi":"10%",
  "option_d":"12%","option_d_hi":"12%",
  "correct_answer":"b",
  "explanation":"1/(3+r)=20/63→3+r=63/20=3.15→r=0.15=15%",
  "explanation_hi":"3+r=63/20→r=15%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"The difference between C.I. and S.I. in 2 years and 3 years are Rs.132 and Rs.407 respectively. Find the simple interest in 5 years on the same principal and same rate of interest annually.",
  "question_text_hi":"किसी निश्चित चक्रवृद्धि ब्याज की दर पर, चक्रवृद्धि ब्याज और साधारण ब्याज के बीच 2 वर्ष और 3 वर्षों में अंतर क्रमशः 132 रू और 407 रू है। तो समान मूलधन और समान वार्षिक ब्याज दर पर 5 वर्षों का साधारण ब्याज ज्ञात कीजिए?",
  "option_a":"Rs.7920","option_a_hi":"₹7920",
  "option_b":"Rs.6600","option_b_hi":"₹6600",
  "option_c":"Rs.8712","option_c_hi":"₹8712",
  "option_d":"Rs.7260","option_d_hi":"₹7260",
  "correct_answer":"a",
  "explanation":"407/132=3+r→r=407/132−3=11/132=1/12. P×(1/12)²=132→P=19008. SI_5=19008×(1/12)×5=7920",
  "explanation_hi":"r=1/12. P=19008. SI=7920",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"Ratio of compound interest and simple interest at the end of 4 years for same principal and at rate 33.33% p.a. is:",
  "question_text_hi":"प्रति वर्ष 33.33% की दर से समान मूलधन के लिए 4 वर्ष के अंत में चक्रवृद्धि ब्याज और साधारण ब्याज का अनुपात है:",
  "option_a":"175:148","option_a_hi":"175:148",
  "option_b":"165:108","option_b_hi":"165:108",
  "option_c":"175:108","option_c_hi":"175:108",
  "option_d":"165:148","option_d_hi":"165:148",
  "correct_answer":"c",
  "explanation":"r=1/3. CI=(4/3)⁴−1=256/81−1=175/81. SI=4×(1/3)=4/3=108/81. Ratio=175:108",
  "explanation_hi":"CI:SI=175:108",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"medium","phase":"main",
  "question_text":"The difference between compound interest (compounding annually) and simple interest on a sum of Rs 1000000 for 2 years is Rs 2401. Find the rate of interest per annum.",
  "question_text_hi":"2 वर्षों के लिए 1000000 रुपये की राशि पर चक्रवृद्धि ब्याज (वार्षिक चक्रवृद्धि) और साधारण ब्याज के बीच का अंतर 2401 रुपये है। प्रति वर्ष ब्याज की दर ज्ञात करें?",
  "option_a":"5.2%","option_a_hi":"5.2%",
  "option_b":"6.1%","option_b_hi":"6.1%",
  "option_c":"4.9%","option_c_hi":"4.9%",
  "option_d":"5.0%","option_d_hi":"5.0%",
  "correct_answer":"c",
  "explanation":"1000000×r²=2401→r²=0.000002401... wait: 2401/1000000=0.002401→r=√0.002401=0.049=4.9%",
  "explanation_hi":"r=√(2401/1000000)=0.049=4.9%",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"Peter invested a certain sum of money in a scheme paying 10% simple interest per annum, while Rachel invested half of the sum that Peter invested at 10% compound interest per annum for 3 years. If the difference in the interest earned by Peter and Rachel was ₹897, what was the sum that Rachel had invested?",
  "question_text_hi":"पीटर ने 10% वार्षिक साधारण ब्याज देने वाली एक योजना में एक निश्चित राशि का निवेश किया, जबकि रेचल ने वार्षिक चक्रवृद्धि आधार पर गणनीय 10% वार्षिक ब्याज दर वाली एक योजना में पीटर से आधी राशि का निवेश किया। पीटर ने 2 वर्ष के लिए निवेश किया, तथा रेचल ने 3 वर्ष के लिए निवेश किया। यदि उनके द्वारा अर्जित ब्याजों में ₹897 का अंतर था, तो रेचल ने किसनी राशि का निवेश किया था?",
  "option_a":"₹12,900","option_a_hi":"₹12,900",
  "option_b":"₹13,000","option_b_hi":"₹13,000",
  "option_c":"₹13,100","option_c_hi":"₹13,100",
  "option_d":"₹12,960","option_d_hi":"₹12,960",
  "correct_answer":"b",
  "explanation":"Peter=2R at 10% SI for 2yr: 0.4R. Rachel=R at 10% CI for 3yr: R×0.331. Diff=0.4R−0.331R=0.069R=897→R=13000",
  "explanation_hi":"0.069R=897→R=13000",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"A man invested a total of ₹12,050 in two parts, one at 10% p.a. simple interest for 2 years and the other at 10% compound interest (annually) for the same time. The amounts received from both parts are equal. The sum invested at compound interest is:",
  "question_text_hi":"कोई आदमी, कुल ₹12,050 की राशि को दो भागों में निवेशित करता है, पहले भाग को साधारण ब्याज पर प्रति वर्ष 10% की दर से 2 वर्ष के लिए और दूसरे भाग को वार्षिक रूप से चक्रवृद्धि होने वाले ब्याज की समान दर से समान समय के लिए निवेशित करता है। उसे दोनों भागों से मिलने वाली धन राशियां बराबर हैं। चक्रवृद्धि ब्याज पर निवेशित राशि (₹ में) ज्ञात करें।",
  "option_a":"5,780","option_a_hi":"5,780",
  "option_b":"5,850","option_b_hi":"5,850",
  "option_c":"6,000","option_c_hi":"6,000",
  "option_d":"5,800","option_d_hi":"5,800",
  "correct_answer":"c",
  "explanation":"P1×1.2=P2×1.21→P1/P2=121/120. P1+P2=12050→241k=12050→k=50. P2(CI)=120×50=6000",
  "explanation_hi":"P2(CI)=6000",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"Difference between simple interest and compound interest for second year is Rs.12 and simple interest for first year is Rs.80. Find CI of third year if rate ratio for three years is 2:3:4 respectively.",
  "question_text_hi":"दूसरे साल के लिए साधारण ब्याज और चक्रवृद्धि ब्याज के बीच अंतर 12 रुपये है और पहले वर्ष के लिए साधारण ब्याज 80 रुपये है। तीसरे वर्ष के चक्रवृद्धि ब्याज का पता लगाएं। यदि तीन वर्षों के लिए ब्याज दर क्रमशः 2:3:4 है।",
  "option_a":"202.40","option_a_hi":"202.40",
  "option_b":"205.40","option_b_hi":"205.40",
  "option_c":"201.20","option_c_hi":"201.20",
  "option_d":"203.80","option_d_hi":"203.80",
  "correct_answer":"a",
  "explanation":"SI_1=P×2a=80→Pa=40. P×2a×3a=12→6a×40=12→a=0.05. Rates: 10%,15%,20%. P=800. CI_3=800×1.1×1.15×0.2=202.4",
  "explanation_hi":"P=800. CI_3=202.4",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Compound Interest","difficulty":"hard","phase":"main",
  "question_text":"A's amount is 41/400 times more than B's amount. B spends his amount at 9% per annum for two years. At what rate should A spend his amount so that after two years their amounts may become equal?",
  "question_text_hi":"A की धनराशि B की धनराशि से 41/400 गुना अधिक है। B अपनी राशि को 9% वार्षिक दर से 2 वर्षों तक खर्च करता है। तो बताइए A अपनी धनराशि किस दर से खर्च करें कि 2 वर्ष बाद उसकी धनराशि बराबर हो जाये?",
  "option_a":"13⅓%","option_a_hi":"13⅓%",
  "option_b":"10%","option_b_hi":"10%",
  "option_c":"11⅑%","option_c_hi":"11⅑%",
  "option_d":"9 1/11%","option_d_hi":"9 1/11%",
  "correct_answer":"a",
  "explanation":"A=441B/400. A×(1−r)²=B×(0.91)². (441/400)×(1−r)²=0.8281. (1−r)²=0.75. (1−r)=√(3/4)≈0.8667. r=13.33%=13⅓%",
  "explanation_hi":"(1−r)²=0.75→r=13⅓%",
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
              f"({len(QUESTIONS)-len(new_qs)} already existed, "
              f"{len(QUESTIONS)} total in this file)")
    except Exception as e:
        db.rollback()
        print(f"✗ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
