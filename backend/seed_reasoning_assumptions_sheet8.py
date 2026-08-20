"""
seed_reasoning_assumptions_sheet8.py
=========================================
Seeds Assumptions Q41-Q50 from Gagan Pratap Reasoning PDFs (Sheet 8).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet8.py

NOTE: All Q41-Q50 are CONCLUSIONS type questions ("follows / does not follow").
      All have 4 options stored (original PDF option order preserved so that
      correct_answer letter matches the PDF).

      Q42 and Q45 contain the SAME statement and conclusions (both from CHSL
      Tier-II, 26 June 2023, Shift-1 — Gagan Pratap included it twice in the
      practice PDF for reinforcement).

      Q43 and Q46 similarly share the SAME statement and conclusions (same exam
      source, included twice).

Answer key (solutions verified from image tick/cross markings):
  Q41  All members of a golf club are active golfers, but all rich. Ms. L is a member.
       I)  She is a golfer → ✓ (all members = golfers + Ms. L is member → she's a golfer)
       II) She is rich → ✓ (all members = rich + Ms. L is member → she's rich)
       Answer: C  (Both I & II follow)  [4-option standard order]

  Q42  India's largest lender bank: exchange Rs.2000 notes without requisition slip
       for amounts up to Rs.20,000.
       I)  No one allowed to withdraw more than Rs.20,000 → ✗
           (statement is about EXCHANGE, not WITHDRAWAL; this conclusion is irrelevant)
       II) No requisition slip required for exchange up to Rs.20,000 → ✓
           (directly and explicitly stated in the statement)
       Answer: A  (Only II follows)  [non-std: (a)=OnlyII (b)=Both (c)=Neither (d)=OnlyI]
       Source: CHSL Tier-II, 26 June 2023 (Shift-1)

  Q43  New government policy: reduce carbon emissions by 50% within the next decade.
       I)  Government will ban ALL vehicles on fossil fuel IMMEDIATELY → ✗
           ("ban immediately" is extreme and contradicts "within the next decade";
            also, banning all fossil vehicles is just one of many possible measures)
       II) Government will shut down ALL coal-fired power plants → ✗
           (shutting all coal plants is too extreme an inference from a 50% reduction
            target; there are many other ways to reduce emissions)
       Answer: D  (Neither I nor II follows)  [4-option standard order]
       Source: CHSL Tier-II, 26 June 2023 (Shift-1)

  Q44  Past 15 years: 75% of world pottery from Country K. Employment in pottery
       declining 5–9% every year for past 3 years.
       I)  Even after declining employment, Country K has enough potters to continue
           contributing equally to the international market → ✓
           (Country K still supplies 75% of the market despite declining employment,
            which directly implies they have sufficient potters to maintain that level)
       II) Local demand of pottery in Country K has substantially decreased leading to
           less interest among potters → ✗
           (statement gives no information about local demand; the employment decline
            could be due to automation, migration, or other reasons — too speculative)
       Answer: C  (Only I follows)  [non-std: (a)=Neither (b)=OnlyII (c)=OnlyI (d)=Both]
       Source: CHSL Tier-II, 6 March 2023 (Shift-1)

  Q45  [Duplicate of Q42 — same statement & conclusions from the same exam source]
       I)  No one allowed to withdraw more than Rs.20,000 → ✗
       II) No requisition slip required for exchange up to Rs.20,000 → ✓
       Answer: A  (Only II follows)  [non-std: (a)=OnlyII (b)=Both (c)=Neither (d)=OnlyI]
       Source: CHSL Tier-II, 26 June 2023 (Shift-1)

  Q46  [Duplicate of Q43 — same statement & conclusions from the same exam source]
       I)  Government will ban ALL vehicles on fossil fuel IMMEDIATELY → ✗
       II) Government will shut down ALL coal-fired power plants → ✗
       Answer: D  (Neither I nor II follows)  [4-option standard order]
       Source: CHSL Tier-II, 26 June 2023 (Shift-1)

  Q47  Private school teachers are hard-working.
       (Note: treated as "Some private school teachers are hard-working")
       I)  Some hard-working teachers are private school teachers → ✓
           (simple conversion: if some A are B, then some B are A — valid syllogism)
       II) Government employees are NOT hardworking → ✗
           ("not" is circled; the statement is ONLY about private school teachers;
            nothing about government employees can be concluded)
       Answer: C  (Only I follows)  [non-std: (a)=OnlyII (b)=Neither (c)=OnlyI (d)=Both]
       Source: CHSL, 03 June 2022 (Shift-3)

  Q48  Every Australian speaks 6 languages. Anthony speaks 6 languages.
       I)  Anthony is an Australian → ✗
           (affirming the consequent fallacy: All A→6lang, Anthony→6lang does NOT
            mean Anthony→A; other nationalities may also speak 6 languages)
       II) People from other countries do not speak 6 languages → ✗
           (the statement says every Australian speaks 6 languages but says nothing
            about other nationalities being unable to speak 6 languages)
       Answer: B  (Neither I nor II follows)  [non-std: (a)=Both (b)=Neither (c)=OnlyI (d)=OnlyII]
       Source: UPSI, 02 Dec 2021 (Shift-1)

  Q49  'In our school, kids are allowed to drink ONLY hot water during Winter',
       said a caretaker of a school.
       I)  Drinking hot water is good for the kids during Winter → ✓
           (the school policy of allowing ONLY hot water implies the school believes
            hot water is beneficial for kids in winter — this is the implicit rationale)
       II) The school doesn't have the facility to provide cold water → ✗
           (the statement is a deliberate POLICY decision, not a statement about
            infrastructure; the school may have cold water but chose to restrict it)
       Answer: B  (Only I follows)  [non-std: (a)=Neither (b)=OnlyI (c)=Both (d)=OnlyII]
       Source: UPSI, 27 Nov 2021 (Shift-3)

  Q50  Vinod is a good cricketer.
       I)  Vinod bats well → ✗
           (a "good cricketer" may excel in fielding, captaincy, or strategy; we cannot
            specifically conclude that Vinod bats well from the general label)
       II) Vinod bowls well → ✗
           (same reasoning — "good cricketer" is not specific enough to conclude he
            bowls well; the label may reflect a different skill set)
       Answer: A  (Neither I nor II follows)
       [non-std: (a)=Neither (b)=EitherIorII (c)=OnlyI (d)=OnlyII]
       Note: (b) "Either I or II follows" has a cross through it in the PDF.
       Source: UPSI, 01 Dec 2021 (Shift-1)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet8"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q41 ── [CONCLUSIONS] Both follow (golf club — Ms. L) ────────────────────
    # 4-option standard order; correct_answer maps directly to letter.
    {
        "question_number": 41,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: All the members of a golf club are active golfers, but they "
            "are all rich. Ms. L is also a member.\n\n"
            "Conclusions:\n"
            "I.  She is a golfer.\n"
            "II. She is rich."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: एक गोल्फ क्लब के सभी सदस्य क्रियाशील गोल्फ खिलाड़ी हैं, परन्तु वे "
            "सभी धनवान हैं। सुश्री Y भी सदस्य हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  वह गोल्फ खिलाड़ी है।\n"
            "II. वह धनी है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # All members = active golfers + Ms. L is member → She is a golfer → I ✓
        # All members = rich + Ms. L is member → She is rich → II ✓
    },
    # ── Q42 ── [CONCLUSIONS] Only II follows (bank — Rs.2000 exchange) ──────────
    # Non-standard option order from PDF: (a)=OnlyII (b)=Both (c)=Neither (d)=OnlyI
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: India's largest lender bank has announced that it will be "
            "allowing customers to exchange Rs. 2000 notes without a requisition slip "
            "for amounts up to Rs. 20,000.\n\n"
            "Conclusions:\n"
            "I.  No one will be allowed to withdraw an amount of more than Rs. 20,000.\n"
            "II. No requisition slip is required for exchange of up to Rs. 20,000."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: भारत के सबसे बड़े ऋणदाता बैंक ने घोषणा की है कि वह ग्राहकों को "
            "रु. 20,000 तक की राशि के लिए बिना किसी मांग पर्ची के रु. 2,000 के नोट "
            "बदलने की अनुमति देगा।\n\n"
            "निष्कर्ष:\n"
            "I.  किसी को भी रु. 20,000 से अधिक की राशि निकालने की अनुमति नहीं दी "
            "जाएगी।\n"
            "II. रु. 20,000 तक के विनिमय के लिए किसी मांग पर्ची की आवश्यकता नहीं है।"
        ),
        "option_a": "Only II follows / केवल II अनुसरण करता है",
        "option_b": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_c": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_d": "Only I follows / केवल I अनुसरण करता है",
        "correct_answer": "A",
        # I: statement is about EXCHANGE of notes, not WITHDRAWAL limits — irrelevant → ✗
        # II: directly and explicitly stated in the announcement → ✓
    },
    # ── Q43 ── [CONCLUSIONS] Neither follows (carbon emissions 50% next decade) ──
    # 4-option standard order.
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: The new government policy aims to reduce carbon emissions by "
            "50% within the next decade.\n\n"
            "Conclusions:\n"
            "I.  The government will ban all vehicles that run on fossil fuel "
            "immediately.\n"
            "II. The government will shut down all the coal-fired power plants."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: नई सरकारी नीति का लक्ष्य अगले दशक के भीतर कार्बन उत्सर्जन को "
            "50% तक कम करना है।\n\n"
            "निष्कर्ष:\n"
            "I.  सरकार जीवाश्म ईंधन से चलने वाले सभी वाहनों पर तुरंत प्रतिबंध "
            "लगाएगी।\n"
            "II. सरकार कोयले से चलने वाले सभी विद्युत संयंत्रों को बंद कर देगी।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_c": "Only II follows / केवल II अनुसरण करता है",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I: "ban immediately" contradicts "within next decade"; also banning ALL fossil
        #    vehicles is just one possible measure — far too extreme → ✗
        # II: shutting ALL coal plants is too extreme an inference from a 50% target;
        #    multiple strategies could be used → ✗
    },
    # ── Q44 ── [CONCLUSIONS] Only I follows (Country K pottery market) ──────────
    # Non-standard option order: (a)=Neither (b)=OnlyII (c)=OnlyI (d)=Both
    {
        "question_number": 44,
        "difficulty": "hard",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Since the past 15 years, 75% of the products in the world's "
            "pottery market come from Country K. However, the employment in the pottery "
            "industry of Country K has been consistently declining by 5-9% every year "
            "since the past 3 years.\n\n"
            "Conclusions:\n"
            "I.  Even after declining employment, Country K has enough potters to "
            "continue contributing equally to the international market.\n"
            "II. The local demand of pottery in Country K has substantially decreased "
            "leading to less interest among potters."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: पिछले 15 वर्षों से, दुनिया के मिट्टी के बर्तन बाजार में 75% उत्पाद "
            "देश K से आते हैं। हालाँकि, देश K के मिट्टी के बर्तन उद्योग में रोजगार में "
            "पिछले 3 वर्षों से हर साल 5-9% की लगातार गिरावट आ रही है।\n\n"
            "निष्कर्ष:\n"
            "I.  रोजगार में गिरावट के बाद भी, देश K के पास अंतर्राष्ट्रीय बाजार में "
            "समान रूप से योगदान जारी रखने के लिए पर्याप्त कुम्हार हैं।\n"
            "II. देश K में मिट्टी के बर्तनों की स्थानीय मांग में काफी कमी आई है, "
            "जिससे कुम्हारों के बीच रुचि कम हो गई है।"
        ),
        "option_a": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "C",
        # I: Country K still supplies 75% despite declining employment → implies sufficient
        #    potters remain to maintain that contribution → ✓
        # II: statement gives no data on local demand; employment decline could be due to
        #    automation, migration, or globalisation — too speculative → ✗
    },
    # ── Q45 ── [CONCLUSIONS] Only II follows (bank — Rs.2000 exchange — duplicate) ─
    # Identical content to Q42 (same question from same exam, included twice in PDF).
    # Non-standard option order: (a)=OnlyII (b)=Both (c)=Neither (d)=OnlyI
    {
        "question_number": 45,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: India's largest lender bank has announced that it will be "
            "allowing customers to exchange Rs. 2000 notes without a requisition slip "
            "for amounts up to Rs. 20,000.\n\n"
            "Conclusions:\n"
            "I.  No one will be allowed to withdraw an amount of more than Rs. 20,000.\n"
            "II. No requisition slip is required for exchange of up to Rs. 20,000."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: भारत के सबसे बड़े ऋणदाता बैंक ने घोषणा की है कि वह ग्राहकों को "
            "रु. 20,000 तक की राशि के लिए बिना किसी मांग पर्ची के रु. 2,000 के नोट "
            "बदलने की अनुमति देगा।\n\n"
            "निष्कर्ष:\n"
            "I.  किसी को भी रु. 20,000 से अधिक की राशि निकालने की अनुमति नहीं दी "
            "जाएगी।\n"
            "II. रु. 20,000 तक के विनिमय के लिए किसी मांग पर्ची की आवश्यकता नहीं है।"
        ),
        "option_a": "Only II follows / केवल II अनुसरण करता है",
        "option_b": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_c": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_d": "Only I follows / केवल I अनुसरण करता है",
        "correct_answer": "A",
        # Same as Q42: I is about withdrawal not exchange → ✗; II directly stated → ✓
    },
    # ── Q46 ── [CONCLUSIONS] Neither follows (carbon emissions — duplicate of Q43) ─
    # Identical content to Q43 (same question from same exam, included twice in PDF).
    # 4-option standard order.
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: The new government policy aims to reduce carbon emissions by "
            "50% within the next decade.\n\n"
            "Conclusions:\n"
            "I.  The government will ban all vehicles that run on fossil fuel "
            "immediately.\n"
            "II. The government will shut down all the coal-fired power plants."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: नई सरकारी नीति का लक्ष्य अगले दशक के भीतर कार्बन उत्सर्जन को "
            "50% तक कम करना है।\n\n"
            "निष्कर्ष:\n"
            "I.  सरकार जीवाश्म ईंधन से चलने वाले सभी वाहनों पर तुरंत प्रतिबंध "
            "लगाएगी।\n"
            "II. सरकार कोयले से चलने वाले सभी विद्युत संयंत्रों को बंद कर देगी।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_c": "Only II follows / केवल II अनुसरण करता है",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # Same as Q43: both conclusions are too extreme for a 50% reduction target → ✗ ✗
    },
    # ── Q47 ── [CONCLUSIONS] Only I follows (private school teachers hardworking) ─
    # Non-standard option order: (a)=OnlyII (b)=Neither (c)=OnlyI (d)=Both
    # Note: "some" written above the statement — treated as "Some private school
    # teachers are hard-working."
    {
        "question_number": 47,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Private school teachers are hard-working.\n\n"
            "Conclusions:\n"
            "I.  Some hard-working teachers are private school teachers.\n"
            "II. Government employees are not hardworking."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: निजी विद्यालय के शिक्षक मेहनती होते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ मेहनती शिक्षक निजी विद्यालय के शिक्षक हैं।\n"
            "II. सरकारी कर्मचारी मेहनती नहीं होते हैं।"
        ),
        "option_a": "Only II follows / केवल II अनुसरण करता है",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "C",
        # I: simple conversion — if "some private school teachers are hardworking" then
        #    "some hardworking [people who are] teachers are private school teachers" ✓
        # II: statement only covers private teachers; no information about govt employees;
        #    "not" is circled in PDF as an extreme unwarranted inference → ✗
    },
    # ── Q48 ── [CONCLUSIONS] Neither follows (Australians speak 6 languages) ─────
    # Non-standard option order: (a)=Both (b)=Neither (c)=OnlyI (d)=OnlyII
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": (
            "In the question below are given two statements followed by two conclusions "
            "numbered I and II. You have to take the given statements to be true even "
            "if they seem to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "1. Every Australian speaks 6 languages.\n"
            "2. Anthony speaks 6 languages.\n\n"
            "Conclusions:\n"
            "I.  Anthony is an Australian.\n"
            "II. People from other countries do not speak 6 languages."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से निष्कर्ष कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "1. प्रत्येक ऑस्ट्रेलियाई 6 भाषाएँ बोलता है।\n"
            "2. एंटनी 6 भाषाएँ बोलते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  एंटनी एक ऑस्ट्रेलियाई हैं।\n"
            "II. दूसरे देशों के लोग 6 भाषाएँ नहीं बोलते हैं।"
        ),
        "option_a": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Only II follows / केवल II अनुसरण करता है",
        "correct_answer": "B",
        # I: affirming the consequent fallacy: All-Australian→6lang, Anthony→6lang
        #    does NOT mean Anthony is Australian → ✗
        # II: statement only says every Australian speaks 6 languages; it says nothing
        #    about other nationalities being unable to → ✗
    },
    # ── Q49 ── [CONCLUSIONS] Only I follows (school hot water policy) ────────────
    # Non-standard option order: (a)=Neither (b)=OnlyI (c)=Both (d)=OnlyII
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: 'In our school, kids are allowed to drink only hot water during "
            "Winter', said a caretaker of a school.\n\n"
            "Conclusions:\n"
            "I.  Drinking hot water is good for the kids during Winter.\n"
            "II. The school doesn't have the facility to provide cold water."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: एक स्कूल के केयरटेकर ने कहा, 'हमारे स्कूल में, बच्चों को सर्दियों के "
            "दौरान केवल गर्म पानी पीने की अनुमति है।'\n\n"
            "निष्कर्ष:\n"
            "I.  सर्दियों के दौरान गर्म पानी पीना बच्चों के लिए अच्छा होता है।\n"
            "II. स्कूल में ठंडा पानी उपलब्ध कराने की सुविधा नहीं है।"
        ),
        "option_a": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_b": "Only I follows / केवल I अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Only II follows / केवल II अनुसरण करता है",
        "correct_answer": "B",
        # I: allowing ONLY hot water is a deliberate health policy → implies school believes
        #    hot water is beneficial for kids in winter → ✓
        # II: the restriction is a policy decision, not a statement about infrastructure;
        #    the school may have cold water facilities but chose to restrict access → ✗
    },
    # ── Q50 ── [CONCLUSIONS] Neither follows (Vinod is a good cricketer) ─────────
    # Non-standard option order: (a)=Neither (b)=EitherIorII (c)=OnlyI (d)=OnlyII
    # Special option: (b) "Either I or II follows" — stored in option_b.
    {
        "question_number": 50,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Vinod is a good cricketer.\n\n"
            "Conclusions:\n"
            "I.  Vinod bats well.\n"
            "II. Vinod bowls well."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: विनोद एक अच्छा क्रिकेटर है।\n\n"
            "निष्कर्ष:\n"
            "I.  विनोद अच्छी बल्लेबाजी करता है।\n"
            "II. विनोद अच्छी गेंदबाजी करता है।"
        ),
        "option_a": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_b": "Either I or II follows / या तो I या II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Only II follows / केवल II अनुसरण करता है",
        "correct_answer": "A",
        # "Good cricketer" is a general label — could reflect excellence in fielding,
        # captaincy, or strategy; does NOT specifically imply good batting OR bowling.
        # I: cannot specifically conclude batting skill from "good cricketer" → ✗
        # II: cannot specifically conclude bowling skill from "good cricketer" → ✗
        # (b) "Either I or II" is crossed in PDF — both are rejected
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
