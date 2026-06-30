"""
Additional Coordinate Geometry questions (Q41 + Q53-Q68) not previously seeded.
Run: python seed_coordinate_extra.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [

# ── Q41: graph-based (line through (0,4) and (6,0)) ──────────
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"easy","phase":"main",
  "question_text":"In the following graph, line AB satisfy which of the following equations?",
  "question_text_hi":"निम्नलिखित ग्राफ में, रेखा AB निम्नलिखित में से किस समीकरण को संतुष्ट करती है?",
  "option_a":"x+4y=2","option_a_hi":"x+4y=2",
  "option_b":"3x-2y=6","option_b_hi":"3x-2y=6",
  "option_c":"2x+3y=12","option_c_hi":"2x+3y=12",
  "option_d":"4y-x=8","option_d_hi":"4y-x=8",
  "correct_answer":"c",
  "explanation":"Line AB passes through (6,0) and (0,4). Equation: x/6+y/4=1 → 2x+3y=12",
  "explanation_hi":"x-अंतःखंड=6, y-अंतःखंड=4. x/6+y/4=1 → 2x+3y=12",
},

# ── Q53-Q68: Systems of Linear Equations ─────────────────────
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"hard","phase":"main",
  "question_text":"For which of the following values of m will the system of equations 17x+my+102=0 & 23x+299y+138=0 have infinite number of solutions?",
  "question_text_hi":"निम्नलिखित में से m के किस मान से समीकरण निकाय 17x+my+102=0 & 23x+299y+138=0 के असंख्य हल प्राप्त होंगे?",
  "option_a":"220","option_a_hi":"220",
  "option_b":"219","option_b_hi":"219",
  "option_c":"221","option_c_hi":"221",
  "option_d":"223","option_d_hi":"223",
  "correct_answer":"c",
  "explanation":"For infinite solutions: 17/23=m/299=102/138. 17/23: m=17×299/23=17×13=221",
  "explanation_hi":"m=17×13=221",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"For what value of k, the system of equations 4x+12y+36=0 and 5x+ky+45=0 has an infinite number of solutions?",
  "question_text_hi":"k के किस मान के लिए, समीकरण निकाय 4x+12y+36=0 और 5x+ky+45=0 में अनंत संख्या में हल हैं?",
  "option_a":"20","option_a_hi":"20",
  "option_b":"25","option_b_hi":"25",
  "option_c":"22","option_c_hi":"22",
  "option_d":"15","option_d_hi":"15",
  "correct_answer":"d",
  "explanation":"4/5=12/k=36/45. 12/k=4/5→k=15",
  "explanation_hi":"12/k=4/5→k=15",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"The relation between K₁ and K₂ for which the system of linear equations K₁x+3y=8 and 4x+K₂y=16 represents coincident lines is:",
  "question_text_hi":"K₁ और K₂ के बीच संबंध जिसके लिए रैखिक समीकरणों K₁x+3y=8 और 4x+K₂y=16 का निकाय संपाती रेखाओं को दर्शाता है, क्या है?",
  "option_a":"K₂=3K₁","option_a_hi":"K₂=3K₁",
  "option_b":"K₂+3K₁=0","option_b_hi":"K₂+3K₁=0",
  "option_c":"K₂=K₁","option_c_hi":"K₂=K₁",
  "option_d":"K₁+K₂=0","option_d_hi":"K₁+K₂=0",
  "correct_answer":"a",
  "explanation":"K₁/4=3/K₂=8/16=1/2 → K₁=2, K₂=6. K₂=3K₁=6 ✓",
  "explanation_hi":"K₁=2, K₂=6. K₂=3K₁ ✓",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"Which of the following is the sum of the values of a and b if the equations 2x+y=a, 8x+by=12 have infinite solutions?",
  "question_text_hi":"यदि समीकरणों 2x+y=a, 8x+by=12 के अनंत हल है, तो a और b के मान का योग निम्नलिखित में से कौन-सा है?",
  "option_a":"16","option_a_hi":"16",
  "option_b":"9","option_b_hi":"9",
  "option_c":"7","option_c_hi":"7",
  "option_d":"18","option_d_hi":"18",
  "correct_answer":"c",
  "explanation":"2/8=1/b=a/12. b=4, a=3. Sum=7",
  "explanation_hi":"b=4, a=3. योग=7",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"hard","phase":"main",
  "question_text":"For what positive values of k do the following pair of linear equations have infinitely many solutions? kx+3y-(k-3)=0 and 12x+ky-k=0",
  "question_text_hi":"k के किन धनात्मक मानों के लिए निम्नलिखित रैखिक समीकरण युग्म के अपरिमित रूप से अनेक हल हैं? kx+3y-(k-3)=0 और 12x+ky-k=0",
  "option_a":"6","option_a_hi":"6",
  "option_b":"2","option_b_hi":"2",
  "option_c":"12","option_c_hi":"12",
  "option_d":"4","option_d_hi":"4",
  "correct_answer":"a",
  "explanation":"k/12=3/k → k²=36 → k=6 (positive). Verify: 3/6=0.5 and (k-3)/k=3/6=0.5 ✓",
  "explanation_hi":"k²=36→k=6",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"hard","phase":"main",
  "question_text":"Find the values of 'a' and 'b' for which the system of equations 3x+y=3 and (a-b)x+(a+b)y=3a+b-3 has infinite solutions.",
  "question_text_hi":"'a' और 'b' के मान ज्ञात कीजिए जिनके लिए समीकरणों के निकाय 3x+y=3 तथा (a-b)x+(a+b)y=3a+b-3 के अनंत हल हैं।",
  "option_a":"a=3, b=-2/3","option_a_hi":"a=3, b=-2/3",
  "option_b":"a=-3/2, b=2","option_b_hi":"a=-3/2, b=2",
  "option_c":"a=3, b=-3/2","option_c_hi":"a=3, b=-3/2",
  "option_d":"a=2, b=-3/2","option_d_hi":"a=2, b=-3/2",
  "correct_answer":"c",
  "explanation":"3/(a-b)=1/(a+b). 3(a+b)=a-b→a=-2b. a+b=3/2. -b=3/2→b=-3/2, a=3",
  "explanation_hi":"a=3, b=-3/2",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"hard","phase":"main",
  "question_text":"The system of equations 2x+3y=7 and (a-b)x+(a+b)y=3a+b-2 have infinitely many solutions, if:",
  "question_text_hi":"समीकरणों के निकायः 2x+3y=7 and (a-b)x+(a+b)y=3a+b-2 के अपरिमित रूप से अनेक हल होते हैं, यदि:",
  "option_a":"a=5, b=3","option_a_hi":"a=5, b=3",
  "option_b":"a=2, b=3","option_b_hi":"a=2, b=3",
  "option_c":"a=2, b=1","option_c_hi":"a=2, b=1",
  "option_d":"a=5, b=1","option_d_hi":"a=5, b=1",
  "correct_answer":"d",
  "explanation":"2/(a-b)=3/(a+b)→2a+2b=3a-3b→a=5b. From constant ratio: (3a+b-2)/(a-b)=7/2. With a=5b: b=1, a=5",
  "explanation_hi":"a=5, b=1",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"For what value of p does the system of equations 18x+36y+45=0 and px-54y+67=0 have no solution?",
  "question_text_hi":"p के किस मान के लिए समीकरण 18x+36y+45=0 और px-54y+67=0 का कोई हल नहीं होगा?",
  "option_a":"54","option_a_hi":"54",
  "option_b":"-27","option_b_hi":"-27",
  "option_c":"-36","option_c_hi":"-36",
  "option_d":"27","option_d_hi":"27",
  "correct_answer":"b",
  "explanation":"No solution: 18/p=36/(-54)=-2/3. 18/p=-2/3→p=-27",
  "explanation_hi":"18/p=-2/3→p=-27",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"For which of the following values of m will the system of equations 18x-72y+13=0 and 7x-my-17=0 have no solution?",
  "question_text_hi":"निम्नलिखित में से m के किस मान के समीकरण निकाय 18x-72y+13=0 और 7x-my-17=0 का कोई हल नहीं होगा?",
  "option_a":"9","option_a_hi":"9",
  "option_b":"12","option_b_hi":"12",
  "option_c":"24","option_c_hi":"24",
  "option_d":"28","option_d_hi":"28",
  "correct_answer":"d",
  "explanation":"No solution: 18/7=(-72)/(-m). 18m=72×7=504. m=28",
  "explanation_hi":"18/7=72/m→m=28",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"If 0.4x+0.16y=1.7 and 0.3x+0.12y=3.4, then which of the following is correct?",
  "question_text_hi":"यदि 0.4x+0.16y=1.7 और 0.3x+0.12y=3.4 है, तो निम्नलिखित में से कौन सा कथन सही है?",
  "option_a":"The system has finitely many solutions but not unique","option_a_hi":"निकाय में परिमित रूप से अनेक हल हैं लेकिन अद्वितीय नहीं हैं",
  "option_b":"The system has infinitely many solutions","option_b_hi":"निकाय के अपरिमित रूप से अनेक हल हैं",
  "option_c":"The system has no solution","option_c_hi":"निकाय का कोई हल नहीं है",
  "option_d":"The system has unique solution","option_d_hi":"निकाय का अद्वितीय हल है",
  "correct_answer":"c",
  "explanation":"0.4/0.3=4/3 and 0.16/0.12=4/3 but 1.7/3.4=0.5≠4/3. Ratios a/d=b/e≠c/f → no solution",
  "explanation_hi":"a/d=b/e≠c/f → कोई हल नहीं",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"Given 5x+7y-8=0, which of the following linear equations, along with the given equation, forms a system having no solution?",
  "question_text_hi":"दो चरों में एक रैखिक समीकरण दिया गया है: 5x+7y-8=0, निम्नलिखित में से कौन सा रैखिक समीकरण, दिए गए समीकरण के साथ, रैखिक समीकरणों का एक निकाय बनाता है जिसका कोई हल नहीं है?",
  "option_a":"5x+7y-16=0","option_a_hi":"5x+7y-16=0",
  "option_b":"7x+5y-8=0","option_b_hi":"7x+5y-8=0",
  "option_c":"5x-7y-8=0","option_c_hi":"5x-7y-8=0",
  "option_d":"10x+14y-16=0","option_d_hi":"10x+14y-16=0",
  "correct_answer":"a",
  "explanation":"For no solution: same coefficient ratio but different constant. 5/5=7/7≠-8/16. So 5x+7y-16=0 works. (d gives coincident lines since 10/5=14/7=16/8=2)",
  "explanation_hi":"5x+7y-16=0 समानांतर रेखा है",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"hard","phase":"main",
  "question_text":"For which of the following values of a and b do the given equations have NO solution? x-ay=2-a and (1-a)x+6y=a+b",
  "question_text_hi":"निम्नलिखित में से a और b के किन मानों के लिए दिए गए समीकरणों का कोई हल नहीं है? x-ay=2-a और (1-a)x+6y=a+b",
  "option_a":"a=-3, b≠1","option_a_hi":"a=-3, b≠1",
  "option_b":"a=3, b≠-1","option_b_hi":"a=3, b≠-1",
  "option_c":"a=-3, b≠-1","option_c_hi":"a=-3, b≠-1",
  "option_d":"a=3, b≠1","option_d_hi":"a=3, b≠1",
  "correct_answer":"b",
  "explanation":"1/(1-a)=(-a)/6 → a²-a-6=0 → a=3 or a=-2. For a=3: check ≠constant ratio: b≠-1",
  "explanation_hi":"a=3, b≠-1",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"Find the value of 'k' for which the system of equations 4x+6y=7 and 6x+(k+4)y-21=0 has a unique solution.",
  "question_text_hi":"'k' का वह मान ज्ञात कीजिए जिसके लिए समीकरणों के निकाय 4x+6y=7 तथा 6x+(k+4)y-21=0 का एक अद्वितीय हल है।",
  "option_a":"k=5","option_a_hi":"k=5",
  "option_b":"k≠5","option_b_hi":"k≠5",
  "option_c":"k=7","option_c_hi":"k=7",
  "option_d":"k≠7","option_d_hi":"k≠7",
  "correct_answer":"b",
  "explanation":"For unique solution: 4/6≠6/(k+4) → 2/3≠6/(k+4) → k+4≠9 → k≠5",
  "explanation_hi":"k≠5",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"medium","phase":"main",
  "question_text":"Let k be a constant. The equations kx+y=3 and 4x+ky=4 have a unique solution if and only if:",
  "question_text_hi":"मान लीजिए k एक नियतांक है। समीकरण kx+y=3 और 4x+ky=4 का एक अनूठा हल है यदि और केवल यदि:",
  "option_a":"k≠2","option_a_hi":"k≠2",
  "option_b":"|k|=2","option_b_hi":"|k|=2",
  "option_c":"|k|≠2","option_c_hi":"|k|≠2",
  "option_d":"k=2","option_d_hi":"k=2",
  "correct_answer":"c",
  "explanation":"Unique solution: k/4≠1/k → k²≠4 → k≠±2 → |k|≠2",
  "explanation_hi":"k²≠4 → |k|≠2",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"easy","phase":"main",
  "question_text":"What conclusion can be drawn about the solution of the following system of linear equations in two variables: 3x+2y=7 and 2x+3y=7?",
  "question_text_hi":"दो चरों में रैखिक समीकरणों के निम्नलिखित निकाय के हल के बारे में क्या निष्कर्ष निकाला जा सकता है? 3x+2y=7 और 2x+3y=7",
  "option_a":"No solution","option_a_hi":"कोई हल नहीं",
  "option_b":"Unique solution","option_b_hi":"अद्वितीय हल",
  "option_c":"Infinite solutions","option_c_hi":"अनंत हल",
  "option_d":"More than two solutions","option_d_hi":"दो से अधिक हल",
  "correct_answer":"b",
  "explanation":"3/2≠2/3 (coefficient ratios unequal) → unique solution",
  "explanation_hi":"3/2≠2/3 → अद्वितीय हल",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"hard","phase":"main",
  "question_text":"Select the option that is true regarding the following: Assertion (A): The system 9x+6y=11 and 7x+ky=9 has no solution, if k=14/3. Reason (R): System Ax+by=c & dx+ey=f has no solution, if a/d=b/e≠c/f",
  "question_text_hi":"उस विकल्प का चयन करें जो निम्नलिखित लेबल वाले दावे (A) और कारण (R) के संबंध में सत्य है। दावा (A): समीकरण निकाय 9x+6y=11 और 7x+ky=9 का कोई हल नहीं है, यदि k=14/3. कारण (R): समीकरण निकाय Ax+by=c और dx+ey=f का कोई हल नहीं है, यदि a/d=b/e≠c/f",
  "option_a":"A is true and R is false","option_a_hi":"A सत्य है और R असत्य है",
  "option_b":"A is false and R is true","option_b_hi":"A असत्य है और R सत्य है",
  "option_c":"Both A and R are true but R is not correct explanation of A","option_c_hi":"A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
  "option_d":"Both A and R are true and R is a correct explanation of A","option_d_hi":"A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
  "correct_answer":"d",
  "explanation":"9/7=6/k → k=42/9=14/3. And 11/9≠9/7 (99≠81). So no solution. R is the correct reason. Answer D",
  "explanation_hi":"k=14/3 ✓ और 11/9≠9/7 ✓. R सही व्याख्या है",
},

# ── Additional questions from Q50-Q52 that add variety ───────
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"hard","phase":"main",
  "question_text":"If the equations 4x+(k-2)y+3=0 and (k-2)x+9y-5=0 (k>0) are parallel, then find the value of k²+6.",
  "question_text_hi":"यदि समीकरण 4x+(k-2)y+3=0 और (k-2)x+9y-5=0 (k>0) समांतर हैं, तो k²+6 का मान ज्ञात कीजिए।",
  "option_a":"68","option_a_hi":"68",
  "option_b":"70","option_b_hi":"70",
  "option_c":"72","option_c_hi":"72",
  "option_d":"64","option_d_hi":"64",
  "correct_answer":"b",
  "explanation":"For parallel: 4/(k-2)=(k-2)/9 → (k-2)²=36 → k-2=6 (k>0) → k=8. k²+6=64+6=70",
  "explanation_hi":"k=8. k²+6=70",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"easy","phase":"main",
  "question_text":"If two straight lines are coinciding with each other, then the number of points of intersection is/are:",
  "question_text_hi":"यदि दो सीधी रेखाएँ संपाती हैं, तो प्रतिच्छेदन बिंदुओं की संख्या ________ होगी।",
  "option_a":"Infinitely many points of intersection","option_a_hi":"अपरिमित रूप से अनेक प्रतिच्छेदन बिंदु",
  "option_b":"Finite number of points of intersection","option_b_hi":"प्रतिच्छेदन बिंदु की परिमित संख्या",
  "option_c":"No points of intersection","option_c_hi":"कोई प्रतिच्छेदन बिंदु नहीं",
  "option_d":"Unique point of intersection","option_d_hi":"अद्वितीय प्रतिच्छेदन बिंदु",
  "correct_answer":"a",
  "explanation":"Coincident lines overlap completely, so every point is a point of intersection → infinitely many",
  "explanation_hi":"संपाती रेखाओं पर अनंत प्रतिच्छेदन बिंदु होते हैं",
},
{
  "subject":"Quantitative Aptitude","subject_code":"quant","topic":"Coordinate","difficulty":"easy","phase":"main",
  "question_text":"The graphs of two linear equations, x+2y=15 and 4x+8y=13 will be?",
  "question_text_hi":"दो रैखिक समीकरण x+2y=15 और 4x+8y=13 के ग्राफ क्या होंगे?",
  "option_a":"Parallel","option_a_hi":"समांतर",
  "option_b":"Coincident","option_b_hi":"संपाती",
  "option_c":"Intersecting at one point","option_c_hi":"एक बिंदु पर प्रतिच्छेदित",
  "option_d":"Intersecting at two points","option_d_hi":"दो बिंदुओं पर प्रतिच्छेदित",
  "correct_answer":"a",
  "explanation":"1/4=2/8=0.5 but 15/13≠0.5. So a/d=b/e≠c/f → parallel lines",
  "explanation_hi":"1/4=2/8≠15/13 → समांतर रेखाएं",
},

]


def seed():
    db = SessionLocal()
    try:
        existing = {
            r[0]
            for r in db.query(Question.question_text)
                         .filter(Question.subject_code == "quant",
                                 Question.topic == "Coordinate")
                         .all()
        }
        new_qs = [q for q in QUESTIONS if q["question_text"] not in existing]
        for qdata in new_qs:
            db.add(Question(**qdata))
        db.commit()
        print(f"✓ Inserted {len(new_qs)} new Coordinate questions. "
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
