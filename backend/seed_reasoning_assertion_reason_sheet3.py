"""
seed_reasoning_assertion_reason_sheet3.py
==========================================
Seeds Assertion and Reason Q9-Q16 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Assertion and Reason

Answer key:
  Q9   D — A is false but R is true.
       A: Safety fuses are made of elements with HIGH melting points. → FALSE ✗
          Image annotation confirms "low M.P." Fuses must have a LOW melting point
          (e.g., tin–lead alloy, Al–Zn alloy) so they melt and break the circuit
          when excessive current heats them up. HIGH melting point would prevent them
          from doing their job.
       R: Safety fuse protects against damage caused by excessive electric current. → TRUE ✓
          That is exactly the purpose of a fuse: to act as a sacrificial element that
          melts and opens the circuit before excessive current can damage appliances.
       → A false, R true → (d)

  Q10  A — Both true; R explains A.
       A: Water of an open pond remains cool even on a hot summer day. → TRUE ✓
          Open ponds are noticeably cooler than the surroundings in summer.
       R: When heated, water vaporizes and the heat energy is converted into latent
          heat. → TRUE ✓
          Evaporation from the pond surface absorbs latent heat of vaporization from
          the remaining water, cooling it.
       Does R explain A? YES — the continuous evaporation from the pond surface takes
       latent heat from the water body, keeping it cool even on a hot day. → (a)

  Q11  B — Both true; R does NOT explain A.
       A: Carbon can form more compounds than other elements. → TRUE ✓
          Carbon has unparalleled compound diversity due to tetravalency, catenation
          (self-linking), and ability to form C–, C=, C≡ (single/double/triple bonds).
       R: Carbon can exist in different forms. → TRUE ✓
          Carbon has allotropes: diamond, graphite, fullerene (C₆₀), graphene, etc.
          (Hindi: "अपरूप" = allotropic forms)
       Does R explain A? NO — carbon's ability to form more compounds is due to its
       TETRAVALENCY (4 valence electrons), CATENATION ability, and capacity for
       single/double/triple bonds. Allotropy (existing in different physical forms) is
       a separate property that does not explain why carbon forms more compounds.
       R is true but not the correct explanation of A. → (b)

  Q12  A — Both true; R explains A.
       A: In 1928, a protest against the Simon Commission was organised in Lahore
          under the leadership of Lala Lajpat Rai. → TRUE ✓
          Historical fact: Simon Commission arrived in India in 1928; Lala Lajpat Rai
          led the Lahore march against it and was fatally lathi-charged.
       R: Not a single Indian member was included in the Simon Commission. → TRUE ✓
          The Simon Commission (1927) comprised 7 British MPs with zero Indian
          representation — the primary grievance that sparked nationwide protests.
       Does R explain A? YES — Indians protested precisely because no Indian voice was
       included in a commission deciding India's constitutional future. R gives the
       direct reason for the protest described in A. → (a)

  Q13  A — Both true; R explains A.
       A: Humus is found in abundance in the soils of the Himalayas. → TRUE ✓
          Himalayan soils are rich in humus due to dense vegetation and high organic
          matter decomposition.
       R: Most of the area in the Himalayas is forested. → TRUE ✓
          Himalayan slopes support extensive forests (Terai, temperate, alpine zones).
       Does R explain A? YES — forests produce fallen leaves, dead wood, and other
       organic material which decompose to form humus. Dense forests → more organic
       input → higher humus content. R is the direct cause of A. → (a)

  Q14  A — Both true; R explains A.
       A: A gas can easily be compressed by applying pressure. → TRUE ✓
          Gases are highly compressible; liquids and solids are nearly incompressible.
       R: Since the inter-particle spaces between gas molecules are very large, they
          can decrease by applying pressure. → TRUE ✓
          Kinetic Molecular Theory: gas particles are far apart with negligible
          inter-particle forces; applying pressure reduces these large empty spaces.
       Does R explain A? YES — it is precisely because gas particles have very large
       inter-particle distances that there is room to compress them; R is the correct
       molecular-level explanation of A. → (a)

  Q15  C — A is true but R is false.
       A: It is easier to cook food at sea level as compared to higher altitudes. → TRUE ✓
          At sea level: atmospheric pressure is ~1 atm → water boils at 100 °C.
          At high altitudes: lower pressure → water boils at <100 °C → food takes
          longer to cook (less thermal energy per unit time).
       R: The boiling point of water INCREASES at high altitudes. → FALSE ✗
          Image annotation "h↑ Atm↓ B.P.↓" confirms: as altitude (h) increases,
          atmospheric pressure (Atm) decreases, and boiling point (B.P.) DECREASES.
          Water boils at ~70 °C at the top of Everest. R states the opposite of the
          correct science.
       → A true, R false → (c)

  Q16  A — Both true; R explains A.
       A: When a solid melts, its temperature remains the same. → TRUE ✓
          During melting (solid → liquid), temperature stays at the melting point
          until the entire solid has converted to liquid (plateau on a heating curve).
       R: The heat gets used up in changing the state by overcoming the forces of
          attraction between the particles. → TRUE ✓
          The supplied heat (latent heat of fusion) is used to break inter-particle
          bonds, not to raise kinetic energy, so temperature does not increase.
       Does R explain A? YES — because the heat energy goes into overcoming
       inter-particle attractions rather than raising temperature, the temperature
       remains constant during melting. R is the exact physical explanation of A. → (a)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assertion_Reason_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Assertion and Reason"

_OPT_A = "Both A & R are true & R is the correct explanation of A. / A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"
_OPT_B = "Both A & R are true but R is not the correct explanation of A. / A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।"
_OPT_C = "A is true but R is false. / A सत्य है लेकिन R असत्य है।"
_OPT_D = "A is false but R is true. / A असत्य है लेकिन R सत्य है।"
_OPT_E_LINE = "(e) Both A & R are false. / A और R दोनों असत्य हैं।"

QUESTIONS = [
    # ── Q9 ── A false (fuses = LOW MP), R true (protects from excess current) ──────
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Safety fuses are made of elements with high melting points.\n"
            "Reason (R): Safety fuse protects against damage caused by excessive "
            "electric current.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): सेफ्टी फ्यूज उच्च गलनांक वाले तत्व का बना होता है।\n"
            "कारण (R): सेफ्टी अधिक विद्युतीय प्रवाह से होने वाले नुकसान से बचाता है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # A: FALSE — Safety fuses are made of materials with LOW melting points
        # (e.g., tin–lead alloy ~183 °C, or aluminium–zinc alloy). A LOW melting
        # point is essential: when excessive current flows, the fuse wire heats up
        # and MELTS, breaking the circuit and protecting appliances. A HIGH melting
        # point wire would not melt and would provide no protection. → ✗
        # R: TRUE — A safety fuse's purpose is exactly to protect circuits and
        # electrical appliances from damage due to excessive (fault) current. → ✓
        # → D
    },
    # ── Q10 ── Both true; R explains A (pond cool due to evaporation/latent heat) ──
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): The water of the open pond remains cool even on a hot "
            "summer day.\n"
            "Reason (R): When heated, water vaporizes and the heat energy is converted "
            "into latent heat.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): एक गर्म उष्ण दिवस में भी खुले तालाब का पानी ठंडा रहता है।\n"
            "कारण (R): गर्म होने पर पानी वाष्पीकृत होता है तथा ताप ऊर्जा, गुप्त ऊष्मा "
            "में बदल जाती है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # A: TRUE — Open ponds remain noticeably cooler than the surrounding air on
        # hot summer days, a well-known observation.
        # R: TRUE — When surface water is heated by the sun it vaporises; the energy
        # for vaporisation (latent heat of vaporisation, ~2260 J/g) is drawn from the
        # remaining water, cooling it.
        # Does R explain A? YES — continuous evaporation from the pond surface absorbs
        # latent heat from the water body, maintaining a lower temperature. → A
    },
    # ── Q11 ── Both true; R does NOT explain A (allotropy ≠ more compounds) ─────────
    {
        "question_number": 11,
        "difficulty": "hard",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Carbon can form more compounds than other elements.\n"
            "Reason (R): Carbon can exist in different forms.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): कार्बन अन्य तत्वों की अपेक्षा अधिक यौगिक बना सकता है।\n"
            "कारण (R): कार्बन विभिन्न अपरूपों में विद्यमान रह सकता है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # A: TRUE — Carbon forms millions of organic compounds, far more than any
        # other element, due to its tetravalency, catenation, and ability to form
        # single (C–C), double (C=C), and triple (C≡C) bonds.
        # R: TRUE — Carbon has allotropes (diamond, graphite, fullerene C₆₀, graphene
        # etc.). Hindi "अपरूप" specifically means allotropic forms.
        # Does R explain A? NO — Carbon's ability to form more compounds is due to
        # TETRAVALENCY (4 valence electrons), CATENATION (self-bonding chains/rings),
        # and multiple bond types (C–, C=, C≡). Allotropy (different physical forms
        # of the same element) is a separate phenomenon and is NOT the reason carbon
        # forms more compounds. → B
    },
    # ── Q12 ── Both true; R explains A (Simon Commission — no Indian → protest) ─────
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): In the year 1928, a protest against the Simon Commission "
            "was organized in Lahore under the leadership of Lala Lajpat Rai.\n"
            "Reason (R): Not a single Indian member was included in the Simon "
            "Commission.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): वर्ष 1928 में लाहौर में लाला लाजपत राय के नेतृत्व में साइमन "
            "कमीशन का विरोध आयोजित किया गया था।\n"
            "कारण (R): साइमन कमीशन में एक भी भारतीय सदस्य सम्मिलित नहीं था।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # A: TRUE — Historically confirmed. Simon Commission reached India in Feb 1928.
        # Lala Lajpat Rai led the anti-Simon protest in Lahore; he was brutally
        # lathi-charged and later died from injuries sustained in that charge.
        # R: TRUE — The Simon Commission (constituted 1927) consisted of 7 British
        # Members of Parliament with no Indian member, which Indians found insulting
        # as it denied them any voice in deciding their own constitutional future.
        # Does R explain A? YES — the absence of any Indian representative in a
        # commission deciding India's constitutional reforms was the principal reason
        # Indians across the country protested under the banner "Simon Go Back." → A
    },
    # ── Q13 ── Both true; R explains A (forests → humus in Himalayas) ───────────────
    {
        "question_number": 13,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Humus is found in abundance in the soils of the "
            "Himalayas.\n"
            "Reason (R): Most of the area in the Himalayas is forested.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): हिमालय की मिट्टियों में 'ह्यूमस' प्रचुर मात्रा में पाई जाती है।\n"
            "कारण (R): हिमालय में सर्वाधिक क्षेत्र वनाच्छादित है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # A: TRUE — Himalayan soils are rich in humus due to dense vegetation and
        # the cool, moist conditions that promote decomposition of organic matter.
        # R: TRUE — The Himalayas support extensive forest cover across the Shivalik,
        # temperate, and sub-alpine zones (e.g., Terai, Sal, Oak, Rhododendron forests).
        # Does R explain A? YES — forests continuously shed leaves, bark, and organic
        # matter; microbes decompose this material into humus. Dense forests = more
        # organic input = higher humus content. R is the direct cause of A. → A
    },
    # ── Q14 ── Both true; R explains A (gas compressed / large inter-particle spaces)
    {
        "question_number": 14,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): A gas can easily be compressed by applying pressure.\n"
            "Reason (R): Since the inter-particle spaces between gases are very large, "
            "they can decrease by applying pressure.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): किसी गैस को दबाव डालकर आसानी से संपीड़ित किया जा सकता है।\n"
            "कारण (R): चूंकि गैसों के बीच अंतर-कण स्थान बहुत बड़े होते हैं, दबाव डालने "
            "से वे कम हो सकते हैं।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # A: TRUE — Gases are far more compressible than liquids or solids. LPG
        # cylinders and CNG tanks are everyday examples of compressed gases.
        # R: TRUE — Kinetic Molecular Theory: gas particles are widely separated with
        # very large inter-particle spaces and negligible inter-molecular forces. These
        # large spaces can be reduced by applying external pressure.
        # Does R explain A? YES — the existence of very large inter-particle spaces
        # is the molecular-level reason why gases can be compressed; applying pressure
        # decreases those spaces, reducing the overall volume. → A
    },
    # ── Q15 ── A true (sea level easier to cook), R false (B.P. DECREASES at altitude)
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): It is easier to cook food at sea level as compared to "
            "higher altitudes.\n"
            "Reason (R): The boiling point of water increases at high altitudes.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): अधिक ऊंचाई की तुलना में समुद्र तल पर भोजन पकाना आसान है।\n"
            "कारण (R): अधिक ऊंचाई पर पानी का क्वथनांक बढ़ जाता है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # A: TRUE — At sea level, atmospheric pressure ≈ 1 atm → water boils at 100 °C.
        # At high altitude, lower pressure → water boils at <100 °C → less thermal
        # energy → food takes much longer to cook. Cooking at sea level is indeed
        # easier/faster.
        # R: FALSE — Image annotation "h↑ Atm↓ B.P.↓" confirms: as altitude increases
        # (h↑), atmospheric pressure decreases (Atm↓), and the boiling point DECREASES
        # (B.P.↓). Water boils at ~70 °C at the top of Mt. Everest. R claims boiling
        # point INCREASES at high altitude — the exact opposite of the correct science.
        # → C
    },
    # ── Q16 ── Both true; R explains A (solid melts at const temp / latent heat) ────
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): When a solid melts, its temperature remains the same.\n"
            "Reason (R): The heat gets used up in changing the state by overcoming "
            "the forces of attraction between the particles.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_LINE}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): जब कोई ठोस पिघलता है, तो उसका तापमान समान रहता है।\n"
            "कारण (R): ऊष्मा का उपयोग कणों के बीच आकर्षण बल पर काबू पाकर अवस्था बदलने "
            "में हो जाता है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # A: TRUE — On a heating curve for a solid, temperature remains constant at
        # the melting point while the phase transition (solid → liquid) occurs; this
        # plateau is a well-established experimental observation.
        # R: TRUE — The supplied heat (latent heat of fusion) goes into breaking the
        # inter-particle bonds (overcoming inter-molecular/inter-atomic attractive
        # forces) to change state, rather than increasing kinetic energy (temperature).
        # Does R explain A? YES — because all the supplied heat is consumed in
        # overcoming inter-particle attraction during melting, none is left to raise
        # the kinetic energy of particles, so temperature stays constant until the
        # phase change is complete. R is the precise physical reason for A. → A
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
