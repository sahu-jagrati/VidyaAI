"""
seed_reasoning_assertion_reason_sheet4.py
==========================================
Seeds Assertion and Reason Q17-Q26 from Gagan Pratap Reasoning PDFs (Sheet 4).
Subject : Reasoning
Topic   : Assertion and Reason

NOTE on Q24, Q25, Q26 (exam-sourced questions):
  These come from UPSI / NTPC CBT-2 exam papers which use only 4 options (no
  option e) with a non-standard ordering. The options are stored exactly as they
  appear in the original PDF. The frontend will still show the injected option E
  ("Both A & R are false") for the topic, but the correct answer is within A-D
  so this causes no marking error.

Answer key:
  Q17  C — A is true but R is false.
       A: The boiling point of water is 100°C. → TRUE ✓ (at standard 1 atm pressure)
       R: The boiling point of water increases at higher altitudes. → FALSE ✗
          At higher altitudes atmospheric pressure decreases, so water boils at a
          LOWER temperature (<100 °C). The boiling point DECREASES with altitude
          (same error as Q15 R). → C

  Q18  B — Both A & R are true but R is not the correct explanation of A.
       A: The conversion of a solid directly into a gas is known as sublimation. → TRUE ✓
          Correct scientific definition: solid → gas without passing through liquid.
       R: Naphthalene does not leave residue when kept open for some time. → TRUE ✓
          Naphthalene sublimes at room temperature, which is why it disappears without
          leaving a liquid or solid residue — an example of sublimation.
       Does R explain A? NO — R provides an EXAMPLE/ILLUSTRATION of sublimation but
       does not explain the definition itself. The definition in A (solid → gas
       directly) does not need naphthalene as its explanation; R merely corroborates A
       without explaining why it is called sublimation. → B

  Q19  A — Both A & R are true & R is the correct explanation of A.
       A: Steam is better than boiling water for heating purposes. → TRUE ✓
          Steam at 100 °C causes more severe burns than water at 100 °C.
       R: Steam contains more heat in the form of latent heat than boiling water. → TRUE ✓
          Steam at 100 °C carries the same sensible heat as boiling water PLUS the
          latent heat of vaporisation (~2260 J/g). On condensing, steam releases all
          this latent heat in addition to cooling, transferring far more heat energy
          per gram than boiling water cooling from 100 °C.
       Does R explain A? YES — the extra latent heat in steam is precisely why it is
       more effective for heating purposes. → A

  Q20  C — A is true but R is false.
       A: Sugar and salt both are easily dissolved in water. → TRUE ✓
          Both NaCl and sucrose are highly water-soluble.
       R: Sugar and salt are solid hence it is easily dissolved in water. → FALSE ✗
          Being solid is NOT the reason for easy dissolution. Many solids (sand,
          marble, glass) are insoluble or sparingly soluble in water. Solubility
          depends on the nature of the solute-solvent interaction:
          NaCl: ionic compound — water (polar) dissolves ionic solutes ("like
          dissolves like"); Sucrose: has multiple –OH groups that form hydrogen bonds
          with water molecules. The physical state (solid) has no bearing on
          water-solubility. → C

  Q21  A — Both A & R are true & R is the correct explanation of A.
       A: Ice floats on water. → TRUE ✓ (observable fact; icebergs, ice cubes etc.)
       R: Density of ice is lesser than water. → TRUE ✓
          Water has an anomalous property: on freezing, hydrogen bonds lock molecules
          into an open hexagonal lattice (V↑, d↓). Ice density ≈ 0.917 g/cm³ vs
          liquid water density ≈ 1.000 g/cm³ at 4 °C.
       Does R explain A? YES — Archimedes' principle: an object floats when its
       density < the fluid density. Ice density < water density → ice floats. → A

  Q22  A — Both A & R are true & R is the correct explanation of A.
       A: The matter around us exists in three different states: solid, liquid, gas. → TRUE ✓
          Basic fact; plasma is a 4th but not covered at this level.
       R: These states arise due to the variation in characteristics of the particle
          of matter. → TRUE ✓
          The three states differ in: (i) arrangement of particles, (ii) inter-particle
          forces/distances, (iii) kinetic energy of particles. These varying particle
          characteristics produce the three distinct macroscopic states.
       Does R explain A? YES — it is precisely the variation in particle
       characteristics (arrangement, energy, forces) that gives rise to the three
       states of matter. → A

  Q23  A — Both A & R are true & R is the correct explanation of A.
       A: Solid carbon dioxide is known as dry ice. → TRUE ✓
          CO₂ in solid form (−78.5 °C at 1 atm) is commercially called dry ice.
       R: Solid carbon dioxide gets converted directly to gaseous state on decrease
          of pressure to 1 atmosphere without coming into liquid state. → TRUE ✓
          CO₂ has its triple point at 5.1 atm; at normal atmospheric pressure (1 atm)
          solid CO₂ sublimes directly to gas without any liquid phase.
       Does R explain A? YES — CO₂ is called "DRY" ice because it sublimes directly
       without ever becoming a liquid, so it leaves no wet residue. R describes
       exactly this sublimation property that gives dry ice its name. → A

  Q24  D — Both A & R are true & R is the correct explanation of A.  [UPSI 20-Nov-2021 Shift-2]
       Non-standard 4-option ordering: (a)=both true R NOT explains, (b)=A true R false,
       (c)=A false R true, (d)=both true R explains ← CORRECT
       A: Urban India is sicker than rural India in spite of better healthcare
          facilities. → TRUE ✓ (public health paradox observed in India)
       R: Urban life is facing the problem of increasing pollution levels, unhygienic
          garbage dumping, and a fast-food culture. → TRUE ✓
          Well-documented urban challenges that negatively impact health.
       Does R explain A? YES — pollution → respiratory & cardiovascular disease;
       unhygienic garbage → infectious disease; fast-food → obesity, diabetes, etc.
       These urban-specific health hazards outweigh the benefit of better healthcare
       access, explaining why urban Indians are sicker. → D

  Q25  A — Both A & R are true & R is the correct explanation of A.  [UPSI 20-Nov-2021 Shift-2]
       Non-standard 4-option ordering: (a)=both true R explains ← CORRECT, (b)=A true
       R false, (c)=A false R true, (d)=both true R NOT explains
       A: The sale of mobile phones has increased manifold in recent times. → TRUE ✓
          Global smartphone shipments have grown enormously over the past decade.
       R: The craze for e-commerce drives mobile sales. → TRUE ✓
          E-commerce platforms are primarily accessed via smartphones; growth of
          e-commerce directly creates demand for mobile phones.
       Does R explain A? YES — the e-commerce boom (online shopping, digital payments,
       app-based services) has been a major driver of smartphone adoption; R is a
       valid and direct explanation for the surge in mobile phone sales. → A

  Q26  C — A is true but R is false.  [NTPC CBT-2, 2021]
       Non-standard 4-option ordering: (a)=both true R NOT explains, (b)=A false R true,
       (c)=A true R false ← CORRECT, (d)=both true R explains
       A: Nowadays, more people opt for fast food. → TRUE ✓
          Fast food consumption has risen sharply globally and in urban India.
       R: Fast food is always inexpensive. → FALSE ✗
          The word "always" makes this too absolute. Fast food ranges from very cheap
          street food to expensive premium fast-food chains. Price/convenience/taste
          are all factors, but fast food is NOT always inexpensive. R is factually
          incorrect. → C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assertion_Reason_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Assertion and Reason"

_OPT_A = "Both A & R are true & R is the correct explanation of A. / A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"
_OPT_B = "Both A & R are true but R is not the correct explanation of A. / A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।"
_OPT_C = "A is true but R is false. / A सत्य है लेकिन R असत्य है।"
_OPT_D = "A is false but R is true. / A असत्य है लेकिन R सत्य है।"
_OPT_E_LINE = "(e) Both A & R are false. / A और R दोनों असत्य हैं।"

QUESTIONS = [
    # ── Q17 ── A true (B.P. 100°C at std pressure), R false (B.P. DECREASES at altitude)
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): The boiling point of water is 100°C.\n"
            "Reason (R): The boiling point of water increases at higher altitudes.\n\n"
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
            "अभिकथन (A): पानी का क्वथनांक 100°C है।\n"
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
        # A: TRUE — Water boils at 100 °C at standard atmospheric pressure (1 atm /
        # sea level). This is the definition of the Celsius scale's upper fixed point.
        # R: FALSE — At higher altitudes, atmospheric pressure is LOWER, so water
        # boils at temperatures BELOW 100 °C. Boiling point DECREASES with altitude;
        # R states the opposite. → C
    },
    # ── Q18 ── Both true; R doesn't explain A (naphthalene = example, not definition)
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): The conversion of a solid directly into a gas is known as "
            "sublimation.\n"
            "Reason (R): Naphthalene does not leave residue when kept open for "
            "sometime.\n\n"
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
            "अभिकथन (A): किसी ठोस का सीधे गैस में परिवर्तन उर्ध्वपातन कहलाता है।\n"
            "कारण (R): कुछ देर तक खुला रखने पर नेफ्थलीन अवशेष नहीं छोड़ता।\n\n"
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
        # A: TRUE — Sublimation is correctly defined as solid → gas directly without
        # passing through the liquid phase.
        # R: TRUE — Naphthalene (moth-ball material) sublimes at room temperature;
        # it disappears without leaving any liquid or solid residue because it goes
        # directly from solid to vapour.
        # Does R explain A? NO — R provides an EXAMPLE of sublimation (naphthalene
        # subliming), not an explanation of the definition. A defines what sublimation
        # IS; R merely illustrates that naphthalene undergoes it. An example does not
        # constitute an explanation of the phenomenon. → B
    },
    # ── Q19 ── Both true; R explains A (steam / latent heat) ────────────────────────
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Steam is better than boiling water for heating purposes.\n"
            "Reason (R): Steam contains more heat in the form of latent heat than "
            "boiling water.\n\n"
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
            "अभिकथन (A): गर्म करने के लिए उबलते पानी में भाप बेहतर है।\n"
            "कारण (R): उबलते पानी की तुलना में भाप में गुप्त ऊष्मा के रूप में अधिक "
            "ऊष्मा होती है।\n\n"
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
        # A: TRUE — Steam burns are more severe than boiling water burns at the same
        # temperature (100 °C), making steam more effective for heating.
        # R: TRUE — Steam at 100 °C carries the same sensible heat as boiling water
        # PLUS ~2260 J/g of latent heat of vaporisation. When steam condenses on a
        # surface it releases this large amount of latent heat in addition to cooling,
        # delivering far more heat energy per gram than liquid water alone.
        # Does R explain A? YES — the extra latent heat stored in steam is exactly
        # why it is superior to boiling water for heating (and why steam burns more
        # severely). → A
    },
    # ── Q20 ── A true (dissolve easily), R false (being solid ≠ soluble) ─────────────
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Sugar and Salt both are easily dissolved in water.\n"
            "Reason (R): Sugar and Salt are solid hence it is easily dissolved in "
            "water.\n\n"
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
            "अभिकथन (A): चीनी और नमक दोनों पानी में आसानी से घुल जाते हैं।\n"
            "कारण (R): चीनी और नमक ठोस होते हैं इसलिए यह पानी में आसानी से घुल जाते हैं।\n\n"
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
        # A: TRUE — Both NaCl (table salt) and sucrose (sugar) are highly soluble in
        # water, which is a well-known practical fact.
        # R: FALSE — Being SOLID is not the reason for easy dissolution. Many solids
        # (sand, marble, glass, chalk) are insoluble or barely soluble in water.
        # Solubility depends on the nature of solute-solvent interactions:
        # NaCl (ionic) → water (polar) breaks ionic bonds: "like dissolves like";
        # Sucrose → –OH groups form H-bonds with water → solvation. Physical state
        # (solid/liquid/gas) does not determine water-solubility. → C
    },
    # ── Q21 ── Both true; R explains A (ice floats / density of ice < water) ─────────
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Ice floats on water.\n"
            "Reason (R): Density of ice is lesser than water.\n\n"
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
            "अभिकथन (A): बर्फ पानी पर तैरती है।\n"
            "कारण (R): बर्फ का घनत्व पानी से कम होता है।\n\n"
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
        # A: TRUE — Ice cubes and icebergs float on liquid water; a universal
        # observation.
        # R: TRUE — Water expands when it freezes (anomalous expansion): H-bonds
        # form an open hexagonal lattice → V↑, so d↓. Ice density ≈ 0.917 g/cm³;
        # liquid water density ≈ 1.00 g/cm³ at 4 °C.
        # Does R explain A? YES — Archimedes/Buoyancy principle: an object floats when
        # its density is less than the fluid. Ice density < water density → ice floats.
        # R is the precise physical reason for A. → A
    },
    # ── Q22 ── Both true; R explains A (3 states of matter / particle characteristics)
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): The matter around us exists in three different states: "
            "solid, liquid, gas.\n"
            "Reason (R): These states arise due to the variation in characteristics "
            "of the particle of matter.\n\n"
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
            "अभिकथन (A): हमारे आस-पास का पदार्थ तीन अलग-अलग अवस्थाओं ठोस, तरल, गैस "
            "में मौजूद है।\n"
            "कारण (R): ये अवस्थाएँ पदार्थ के कण की विशेषताओं में भिन्नता के कारण "
            "उत्पन्न होती हैं।\n\n"
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
        # A: TRUE — Matter commonly exists in three physical states: solid (fixed shape
        # and volume), liquid (fixed volume, no fixed shape), and gas (neither fixed).
        # R: TRUE — The three states differ in: (i) particle arrangement (ordered ↔
        # disordered), (ii) inter-particle forces (strong ↔ weak), (iii) kinetic
        # energy (low ↔ high). These varying particle characteristics produce the
        # distinct macroscopic properties of each state.
        # Does R explain A? YES — it is precisely the variation in particle
        # characteristics (arrangement, energy, inter-molecular forces) that gives
        # rise to the three different states of matter. → A
    },
    # ── Q23 ── Both true; R explains A (dry ice = CO₂ sublimation — no liquid) ───────
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Solid carbon dioxide is known as dry ice.\n"
            "Reason (R): Solid carbon dioxide gets converted directly to gaseous "
            "state on decrease of pressure to 1 atmosphere without coming into liquid "
            "state.\n\n"
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
            "अभिकथन (A): ठोस कार्बन डाइऑक्साइड को सूखी बर्फ के रूप में जाना जाता है।\n"
            "कारण (R): दबाव कम होने पर ठोस कार्बन डाइऑक्साइड तरल अवस्था में आए बिना "
            "वायुमंडल से सीधे गैस अवस्था में परिवर्तित हो जाती है।\n\n"
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
        # A: TRUE — Solid CO₂ is universally called "dry ice" in industrial/commercial
        # usage.
        # R: TRUE — CO₂'s triple point is at 5.18 atm (−56.6 °C). At normal
        # atmospheric pressure (~1 atm), which is below the triple point pressure, solid
        # CO₂ sublimes directly to gas (at −78.5 °C) without ever becoming liquid.
        # Does R explain A? YES — CO₂ is called "DRY" ice because it sublimes (no
        # liquid phase), so it never becomes wet/damp. R describes exactly this
        # sublimation behaviour that justifies the name "dry" ice. → A
    },
    # ── Q24 ── [UPSI 20-Nov-2021 Shift-2] Both true; R explains A (urban health)
    # Non-standard 4-option ordering: (a)=Both true R NOT explains, (b)=A true R false,
    # (c)=A false R true, (d)=Both true R IS the explanation ← CORRECT ANSWER
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Urban India is sicker than rural India in spite of better "
            "healthcare facilities.\n"
            "Reason (R): Urban life is facing the problem of increasing pollution "
            "levels, unhygienic garbage dumping, and a fast-food culture.\n\n"
            "(Source: UPSI, 20 Nov 2021, Shift-2)\n\n"
            "Options:\n"
            "(a) Both A & R are true but R is not the correct explanation of A.\n"
            "(b) A is true but R is false.\n"
            "(c) A is false but R is true.\n"
            "(d) Both A & R are true & R is the correct explanation of A."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): बेहतर स्वास्थ्य सुविधाओं के बावजूद शहरी भारत ग्रामीण भारत की "
            "तुलना में बीमार है।\n"
            "कारण (R): शहरी जीवन बढ़ते प्रदूषण स्तर, अस्वच्छ कचरा डंपिंग और फास्ट-फूड "
            "संस्कृति की समस्याओं का सामना कर रहा है।\n\n"
            "(स्रोत: UPSI, 20 नवम्बर 2021, Shift-2)\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(b) A सत्य है लेकिन R असत्य है।\n"
            "(c) A असत्य है लेकिन R सत्य है।\n"
            "(d) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"
        ),
        "option_a": "Both A & R are true but R is not the correct explanation of A. / A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।",
        "option_b": "A is true but R is false. / A सत्य है लेकिन R असत्य है।",
        "option_c": "A is false but R is true. / A असत्य है लेकिन R सत्य है।",
        "option_d": "Both A & R are true & R is the correct explanation of A. / A और R दोनों सत्य हैं और R, A की सही व्याख्या है।",
        "correct_answer": "D",
        # A: TRUE — Urban India does exhibit higher prevalence of lifestyle diseases
        # (diabetes, hypertension, respiratory disease) compared to rural India,
        # despite urban areas having better hospitals and healthcare access.
        # R: TRUE — Rapid urbanisation in India has brought increased air/water/noise
        # pollution, poor solid-waste management (garbage dumping), and widespread
        # fast-food consumption contributing to obesity and metabolic disorders.
        # Does R explain A? YES — These three urban health hazards (pollution →
        # respiratory/cardiovascular disease; unhygienic waste → infectious disease;
        # fast-food → obesity/diabetes) create new disease burdens that outweigh the
        # benefit of better healthcare access in cities. → D
    },
    # ── Q25 ── [UPSI 20-Nov-2021 Shift-2] Both true; R explains A (mobile/e-commerce)
    # Non-standard 4-option ordering: (a)=Both true R IS explanation ← CORRECT,
    # (b)=A true R false, (c)=A false R true, (d)=Both true R NOT explains
    {
        "question_number": 25,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): The sale of mobile phones has increased manifold in recent "
            "times.\n"
            "Reason (R): The craze for e-commerce drives mobile sales.\n\n"
            "(Source: UPSI, 20 Nov 2021, Shift-2)\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) A is true but R is false.\n"
            "(c) A is false but R is true.\n"
            "(d) Both A & R are true but R is not the correct explanation of A."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): हाल के दिनों में मोबाइल फोन की बिक्री कई गुना बढ़ गई है।\n"
            "कारण (R): ई-कॉमर्स के प्रति दीवानगी मोबाइल बिक्री को बढ़ावा देती है।\n\n"
            "(स्रोत: UPSI, 20 नवम्बर 2021, Shift-2)\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A सत्य है लेकिन R असत्य है।\n"
            "(c) A असत्य है लेकिन R सत्य है।\n"
            "(d) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।"
        ),
        "option_a": "Both A & R are true & R is the correct explanation of A. / A और R दोनों सत्य हैं और R, A की सही व्याख्या है।",
        "option_b": "A is true but R is false. / A सत्य है लेकिन R असत्य है।",
        "option_c": "A is false but R is true. / A असत्य है लेकिन R सत्य है।",
        "option_d": "Both A & R are true but R is not the correct explanation of A. / A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।",
        "correct_answer": "A",
        # A: TRUE — Global (and especially Indian) smartphone shipments have grown
        # enormously in the past decade; manifold increase is well-documented.
        # R: TRUE — E-commerce platforms (Amazon, Flipkart, etc.) are primarily
        # accessed via smartphones; the boom in online shopping creates sustained
        # demand for mobile phones.
        # Does R explain A? YES — The rapid growth of e-commerce has been one of the
        # most direct drivers of smartphone adoption. Consumers buy phones to shop
        # online, pay digitally, and access app-based marketplaces; R is a valid
        # causal explanation for the manifold increase in mobile phone sales. → A
    },
    # ── Q26 ── [NTPC CBT-2, 2021] A true, R false (fast food NOT "always" cheap)
    # Non-standard 4-option ordering: (a)=Both true R NOT explains, (b)=A false R true,
    # (c)=A true R false ← CORRECT, (d)=Both true R IS explanation
    {
        "question_number": 26,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Nowadays, more people opt for fast food.\n"
            "Reason (R): Fast food is always inexpensive.\n\n"
            "(Source: NTPC CBT-2, 2021)\n\n"
            "Options:\n"
            "(a) Both A & R are true but R is not the correct explanation of A.\n"
            "(b) A is false but R is true.\n"
            "(c) A is true but R is false.\n"
            "(d) Both A & R are true & R is the correct explanation of A."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): आजकल, अधिक लोग फास्ट फूड का विकल्प चुनते हैं।\n"
            "कारण (R): फास्ट फूड हमेशा सस्ता होता है।\n\n"
            "(स्रोत: NTPC CBT-2, 2021)\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(b) A असत्य है लेकिन R सत्य है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"
        ),
        "option_a": "Both A & R are true but R is not the correct explanation of A. / A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।",
        "option_b": "A is false but R is true. / A असत्य है लेकिन R सत्य है।",
        "option_c": "A is true but R is false. / A सत्य है लेकिन R असत्य है।",
        "option_d": "Both A & R are true & R is the correct explanation of A. / A और R दोनों सत्य हैं और R, A की सही व्याख्या है।",
        "correct_answer": "C",
        # A: TRUE — Fast food consumption has risen substantially in urban India and
        # globally; an easily observable trend.
        # R: FALSE — "Fast food is ALWAYS inexpensive" is factually incorrect. Fast
        # food spans a wide price range: from cheap roadside vada pav (₹10) to
        # expensive fast-food chains (₹400+ meals at Burger King/McDonald's premium
        # items). The word "always" makes the claim too absolute and wrong. People opt
        # for fast food due to convenience, taste, and busy lifestyles — not solely
        # because of price. → C
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
