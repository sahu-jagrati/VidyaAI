"""
seed_reasoning_assumptions_sheet7.py
=========================================
Seeds Assumptions Q31-Q40 from Gagan Pratap Reasoning PDFs (Sheet 7).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet7.py

NOTE: All Q31-Q40 are CONCLUSIONS type questions ("follows / does not follow").
      Q31-Q39 have 5 options in original PDF; option_e ("Either I or II follows")
      is omitted in DB since the model stores only option_a through option_d and
      none of the correct answers for this batch is option_e.
      Q40 has 4 options only (no option_e in original PDF).

Answer key (solutions verified from image tick/cross markings):
  Q31  Statement: The PM emphatically stated that his government will make every
       possible effort for the upliftment of poor farmers & farmhands.
       I)  Except poor farmers, all others have got the benefits of development → ✗
           (PM's forward-looking pledge says nothing about what others have received)
       II) No serious efforts have been made in the past for any section → ✗
           ("will make effort" is future-oriented; does not condemn past efforts)
       Answer: D  (Neither I nor II follows)

  Q32  Statement: The Cabinet of State X took steps to tackle the milk glut as
       cooperatives & government dairies failed to use the available milk.
       I)  The milk production of state X is more than its need → ✓
           ("glut" directly means overproduction relative to consumption)
       II) The Government & co-operative dairies are not equipped in terms of
           resources & technology to handle such excess milk → ✓
           ("failed to use the available milk" implies inability → resource/tech gap)
       Answer: C  (Both I & II follow)

  Q33  Statement: The manager humiliated Sachin in the presence of his colleagues.
       I)  The manager didn't like Sachin → ✗
           (humiliation could stem from performance issues, discipline, etc., not
            necessarily personal dislike)
       II) Sachin was not popular among his colleagues → ✗
           (being humiliated in front of colleagues says nothing about Sachin's
            popularity with those colleagues)
       Answer: D  (Neither I nor II follows)

  Q34  Statement: The Government of country X has recently announced several
       concessions & offered attractive package tours for foreign visitors.
       I)  Now, more number of foreign visitors will visit the country → ✓
           (concessions + package tours are designed to attract visitors → more will come)
       II) The Government of country X seems to be serious in attracting tourists → ✓
           (announcing concessions and packages is clear evidence of seriousness)
       Answer: C  (Both I & II follow)

  Q35  Statement: Only good singers are invited in the conference. No one without
       a sweet voice is a good singer.
       I)  All invited singers in the conference have sweet voice → ✓
           (Only good singers invited + good singer ≡ sweet voice → all invited have
            sweet voice; valid syllogism)
       II) Those singers who do not have sweet voice are not invited → ✓
           (contrapositive of statement 2: no sweet voice → not good singer;
            + only good singers invited → not invited; valid chain)
       Answer: C  (Both I & II follow)

  Q36  Statement: In a recent survey report, those who undertake physical exercise for
       at least half an hour a day are less prone to have any heart ailments.
       I)  Moderate level of physical exercise is necessary for leading a healthy life → ✓
           (less prone to heart ailments through exercise implies exercise is necessary
            for health; "moderate" aligns with "half an hour a day")
       II) All people who do desk-bound jobs definitely suffer from heart ailments → ✗
           ("definitely suffer" is circled as too extreme; the statement says "less prone"
            for those who exercise, not that all sedentary workers definitely suffer)
       Answer: A  (Only I follows)

  Q37  Statement: This world is neither good nor evil; each man manufactures a world
       for himself.
       I)  Some people find this world quite good → ✓
           (since each person creates their own world, some will create a good one)
       II) Some people find this world quite bad → ✓
           (similarly, some will create a bad one; both can simultaneously be true)
       Answer: C  (Both I & II follow)

  Q38  Statement: Double your money in five months - An advertisement.
       I)  The assurance is not genuine → ✗
           (we cannot conclude the ad is false purely from reading the ad; this is a
            judgement about credibility, not a logical conclusion from the content)
       II) People want their money to grow → ✓
           (an advertisement promising to double money is effective only if people
            desire financial growth; this is the implicit audience assumption of the ad)
       Answer: B  (Only II follows)

  Q39  Statement: No country is absolutely self-dependent these days.
       I)  It is impossible to grow and produce all that a country needs → ✓
           (if no country is self-dependent, it follows that countries cannot produce
            everything they need entirely on their own)
       II) Countrymen in general have become lazy → ✗
           (lack of self-dependence is about economic interdependence, not laziness;
            there is no logical link between the two)
       Answer: A  (Only I follows)

  Q40  Statement: Most Indians know that they have a great heritage, but few include
       science in this.
       [4-option format — no option_e in original PDF]
       I)  Many Indians believe that science has made Indian heritage great → ✗
           ("few include science" directly contradicts "many believe science made
            heritage great"; cannot follow from the statement)
       II) Many Indians do not know that India has a great scientific heritage → ✓
           ("few include science in their heritage" → most don't recognise India's
            scientific heritage → many don't know about it)
       Answer: B  (Only II follows)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q31 ── [CONCLUSIONS] Neither follows (PM upliftment of poor farmers) ────
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: The Prime Minister emphatically stated that his government will "
            "make every possible effort for the upliftment of poor farmers & farmhands.\n\n"
            "Conclusions:\n"
            "I.  Except poor farmers & farmhands, all others have got the benefits of "
            "fruits of development.\n"
            "II. No serious efforts have been made in the past for the upliftment of "
            "any section of the society."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: प्रधानमंत्री ने जोर देकर कहा कि उनकी सरकार गरीब किसानों और कृषि "
            "श्रमिकों के उत्थान के लिए हर संभव प्रयास करेगी।\n\n"
            "निष्कर्ष:\n"
            "I.  गरीब किसानों और कृषि श्रमिकों को छोड़कर अन्य सभी को विकास के फलों "
            "का लाभ मिला है।\n"
            "II. समाज के किसी भी वर्ग के उत्थान के लिए अतीत में कोई गंभीर प्रयास "
            "नहीं किए गए हैं।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I: the PM's pledge about farmers says nothing about what others received → ✗
        # II: "will make effort" is future-oriented; does not imply no past efforts → ✗
    },
    # ── Q32 ── [CONCLUSIONS] Both follow (milk glut in state X) ─────────────────
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: The Cabinet of State X took certain steps to tackle the milk "
            "glut in the state as the cooperatives & government dairies failed to use "
            "the available milk - A news report.\n\n"
            "Conclusions:\n"
            "I.  The milk production of state X is more than its need.\n"
            "II. The Government & co-operative dairies in state X are not equipped in "
            "terms of resources & technology to handle such excess milk."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: राज्य 'X' के कैबिनेट ने राज्य में मिल्क ग्लट से निपटने के लिए "
            "कुछ कदम उठाए क्योंकि सहकारी समितियां और सरकारी डेयरियां उपलब्ध दूध का "
            "उपयोग करने में विफल रहीं - एक समाचार विवरण।\n\n"
            "निष्कर्ष:\n"
            "I.  राज्य 'X' का दूध उत्पादन उसकी आवश्यकता से अधिक है।\n"
            "II. राज्य में सरकारी और सहकारी डेयरियां इस तरह के अतिरिक्त दूध को "
            "संभालने के लिए संसाधनों और प्रौद्योगिकी के मामले में सुसज्जित नहीं हैं।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # I: "glut" = surplus production > consumption → directly follows ✓
        # II: dairies "failed to use" the milk → implies inability due to resource/tech
        #    constraints → follows ✓
    },
    # ── Q33 ── [CONCLUSIONS] Neither follows (manager humiliated Sachin) ────────
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: The manager humiliated Sachin in the presence of his colleagues.\n\n"
            "Conclusions:\n"
            "I.  The manager didn't like Sachin.\n"
            "II. Sachin was not popular among his colleagues."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: प्रबंधक ने अपने सहयोगियों की उपस्थिति में सचिन को अपमानित किया।\n\n"
            "निष्कर्ष:\n"
            "I.  प्रबंधक को सचिन पसंद नहीं था।\n"
            "II. सचिन अपने सहयोगियों के साथ लोकप्रिय नहीं थे।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I: humiliation could be due to performance/discipline reasons, not dislike → ✗
        # II: being humiliated IN FRONT of colleagues ≠ being unpopular WITH colleagues → ✗
    },
    # ── Q34 ── [CONCLUSIONS] Both follow (country X concessions + package tours) ─
    {
        "question_number": 34,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: The Government of country X has recently announced several "
            "concessions & offered attractive package tours for foreign visitors.\n\n"
            "Conclusions:\n"
            "I.  Now, more number of foreign visitors will visit the country.\n"
            "II. The Government of country X seems to be serious in attracting tourists."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: देश X की सरकार ने हाल ही में कई रियायतों की घोषणा की है और विदेशी "
            "आगंतुकों के लिए आकर्षक पैकेज टूर की पेशकश की है।\n\n"
            "निष्कर्ष:\n"
            "I.  अब, अधिक संख्या में विदेशी पर्यटक देश का दौरा करेंगे।\n"
            "II. X देश की सरकार पर्यटकों को आकर्षित करने में गंभीर प्रतीत होती है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # I: concessions + attractive packages → designed to draw visitors → more will come ✓
        # II: announcing concrete incentives = clear evidence of government seriousness ✓
    },
    # ── Q35 ── [CONCLUSIONS] Both follow (good singers / sweet voice / conference) ─
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": (
            "In the question below are given two statements followed by two conclusions "
            "numbered I and II. You have to take the given statements to be true even "
            "if they seem to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "1. Only good singers are invited in the conference.\n"
            "2. No one without a sweet voice is a good singer.\n\n"
            "Conclusions:\n"
            "I.  All invited singers in the conference have sweet voice.\n"
            "II. Those singers who do not have sweet voice are not invited in the "
            "conference."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से निष्कर्ष कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "1. सम्मेलन में केवल अच्छे गायक ही आमंत्रित हैं।\n"
            "2. मीठी आवाज के बिना कोई भी अच्छा गायक नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  सम्मेलन में आमंत्रित सभी गायकों की मधुर आवाज है।\n"
            "II. जिन गायकों की मधुर आवाज नहीं होती है उन्हें सम्मेलन में आमंत्रित "
            "नहीं किया जाता है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # I: Only good singers invited + good singer ≡ sweet voice → all invited have sweet
        #    voice; valid syllogism → ✓
        # II: contrapositive chain: no sweet voice → not good singer + not good → not invited
        #    → valid → ✓
    },
    # ── Q36 ── [CONCLUSIONS] Only I follows (physical exercise & heart ailments) ─
    {
        "question_number": 36,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: In a recent survey report, it has been stated that those who "
            "undertake physical exercise for at least half an hour a day are less prone "
            "to have any heart ailments.\n\n"
            "Conclusions:\n"
            "I.  Moderate level of physical exercise is necessary for leading a healthy "
            "life.\n"
            "II. All people who do desk-bound jobs definitely suffer from heart ailments."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: एक हालिया सर्वेक्षण रिपोर्ट में, यह कहा गया है कि जो लोग दिन में "
            "आधे घंटे शारीरिक व्यायाम करते हैं, उन्हें दिल की बीमारियां होने का खतरा "
            "कम होता है।\n\n"
            "निष्कर्ष:\n"
            "I.  स्वस्थ जीवन जीने के लिए शारीरिक व्यायाम का मध्यम स्तर आवश्यक है।\n"
            "II. डेस्क-बाउंड जॉब करने वाले सभी लोग निश्चित रूप से दिल की बीमारियों "
            "से पीड़ित हैं।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "A",
        # I: exercise → less prone to heart ailments → exercise necessary for healthy life ✓
        # II: "definitely suffer" is too extreme; statement says "less prone" for those who
        #    exercise, not that all sedentary workers definitely get heart disease → ✗
    },
    # ── Q37 ── [CONCLUSIONS] Both follow (world neither good nor evil) ───────────
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: This world is neither good nor evil; each man manufactures a "
            "world for himself.\n\n"
            "Conclusions:\n"
            "I.  Some people find this world quite good.\n"
            "II. Some people find this world quite bad."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: यह दुनिया न अच्छी है और न ही बुरी, प्रत्येक आदमी अपने लिए एक दुनिया "
            "बनाता है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ लोगों को ये दुनिया काफी अच्छी लगती है।\n"
            "II. कुछ लोगों को ये दुनिया काफी बुरी लगती है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # "each man manufactures a world for himself" → different people create different
        # worlds → some make good ones (I ✓) and some make bad ones (II ✓); both can be
        # simultaneously true → Both follow
    },
    # ── Q38 ── [CONCLUSIONS] Only II follows (Double money ad) ──────────────────
    {
        "question_number": 38,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Double your money in five months - An advertisement.\n\n"
            "Conclusions:\n"
            "I.  The assurance is not genuine.\n"
            "II. People want their money to grow."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: पांच महीने में अपना पैसा दोगुना करें - एक विज्ञापन।\n\n"
            "निष्कर्ष:\n"
            "I.  आश्वासन वास्तविक नहीं है।\n"
            "II. लोग चाहते हैं कि उनका पैसा बढ़े।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I: we cannot conclude an advertisement is false just by reading it; that is a
        #    credibility judgement, not a logical conclusion from the content → ✗
        # II: an ad promising to double money is effective only if people desire growth;
        #    the ad's very existence implies this audience motivation → ✓
    },
    # ── Q39 ── [CONCLUSIONS] Only I follows (no country absolutely self-dependent) ─
    {
        "question_number": 39,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: No country is absolutely self-dependent these days.\n\n"
            "Conclusions:\n"
            "I.  It is impossible to grow and produce all that a country needs.\n"
            "II. Countrymen in general have become lazy."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: कोई भी देश इन दिनों बिल्कुल आत्म-निर्भर नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  किसी देश की आवश्यकता के लिए सब विकसित करना और उत्पादन करना असंभव है।\n"
            "II. सामान्य तौर पर देशवासी आलसी हो गए हैं।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "A",
        # I: no self-dependent country → countries can't produce everything they need ✓
        # II: economic interdependence has no connection to laziness; an external economic
        #    reality ≠ a character trait of citizens → ✗
    },
    # ── Q40 ── [CONCLUSIONS] Only II follows (Indians & scientific heritage) ─────
    # 4-option format only (no option_e in original PDF)
    {
        "question_number": 40,
        "difficulty": "hard",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Most Indians know that they have a great heritage, but few "
            "include science in this.\n\n"
            "Conclusions:\n"
            "I.  Many Indians believe that science has made Indian heritage great.\n"
            "II. Many Indians do not know that India has a great scientific heritage."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: अधिकांश भारतीय जानते हैं कि उनके पास एक महान विरासत है, किंतु कुछ "
            "इसमें विज्ञान का शामिल हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कई भारतीय मानते हैं कि विज्ञान ने भारतीय विरासत को महान बनाया है।\n"
            "II. कई भारतीय नहीं जानते कि भारत के पास महान वैज्ञानिक विरासत है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I: statement says "few include science in heritage" → contradicts "many believe
        #    science made heritage great"; directly opposite → ✗
        # II: "few include science in heritage" → most don't recognise India's scientific
        #    heritage → many don't know about it → ✓
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_number"] in existing_qnums:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}")

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
