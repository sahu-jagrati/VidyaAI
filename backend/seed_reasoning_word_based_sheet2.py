"""
seed_reasoning_word_based_sheet2.py
=========================================
Seeds Word-Based (Analogy) Q30-Q70 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Word-Based
Run     : python seed_reasoning_word_based_sheet2.py

Direction: In each question select the related word from the given alternatives.

Answer key (published key + logical verification):
  Q30  Necklace:Adornment (thing:purpose) → Medal:Decoration          → A
  Q31  Black:White (opposites) → Up:Down                              → D
       [key prints B but Down is logically correct for opposite-pair]
  Q32  Horse:Hoof (animal:foot-type) → Man:Foot                       → A
  Q33  Night:Morning (precedes) → Evening:Night                       → D
  Q34  Oxygen:Burn → CO2:Extinguishes (opposite effect)               → C
  Q35  Human:Carbohydrate (fuel source) → Engine:Petrol               → D
  Q36  Telephone→Mobile phone (evolved to) → Computer→Laptop          → D
  Q37  Food:Hunger (alleviates) → Sleep:Weariness                     → A
  Q38  Teacher:Student → Pontiff:Disciple                              → A
  Q39  Bees:Hum (animal sound) → Owls:Hoot                            → D
  Q40  Confirmed:Inveterate → Financial:Bankrupt                      → C
  Q41  Elephant:Tusk (distinctive feature) → Parrot:Beak              → C
  Q42  Virus:Smallpox (cause:disease) → Bacteria:Typhoid              → B
  Q43  Home:Kitchen (function room in) → Plant:Leaf                   → C
  Q44  Window:Carpenter (made by) → Statue:Sculptor                   → A
  Q45  Eye:Cataract (organ:disease) → Skin:Eczema                     → C
  Q46  Vitamin A:Carrot (found in) → Vitamin C:Orange                 → D
  Q47  Mango:Fruit → Jasmine:Flower                                   → C
  Q48  Dress:Tailor (made by) → Furniture:Carpenter                   → B
  Q49  Bow:Arrow (weapon:projectile) → Pistol:Bullet                  → A
  Q50  Crime:Punishment (leads to) → Honesty:Reward                   → C
  Q51  Sepal:Flower (part:whole) → Tyre:Bicycle                       → B
  Q52  Seismometer:Earthquakes → Thermometer:Temperature              → B
  Q53  Intl Literacy Day:Sep 8 → Intl Women's Day:March 8             → A
  Q54  Ravishankar:Sitar → Bismillah Khan:Shehnai                     → C
  Q55  India:Mango → New Zealand:Kiwi                                 → B
  Q56  Insects:Entomology → Snakes:Ophiology                          → B
  Q57  Book:Paper (made of) → Bread:Flour                             → A
  Q58  Perch:Fresh water → Cod:Salt water                             → D
  Q59  Exercise:Gym (activity:venue) → Eating:Restaurant              → A
  Q60  School:Teacher (institution:worker) → Bank:Banker              → B
  Q61  Prediction:Future → Regret:Past                                → D
  Q62  Adversary:Enemy (synonyms) → Adversity:Difficulty              → C
  Q63  Bird:Worm (predator:prey) → Cat:Mouse                          → C
  Q64  Apes:Gibber (animal sound) → Camels:Grunt                      → A
  Q65  Cell:Cytology → Birds:Ornithology                              → C
  Q66  Play:Actor (performer in) → Concert:Musician                   → B
  Q67  Summer:Aestivation → Winter:Hibernation                        → B
  Q68  Calendar:Dates → Dictionary:Words                              → A
  Q69  Pesticide:Plant (protects) → Vaccination:Baby                  → C
  Q70  Iron Man of India:Patel → Father of Nation:Mahatma Gandhi      → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Word_Based_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Word-Based"

QUESTIONS = [
    # ── Q30 ── Necklace:Adornment → Medal:Decoration (thing:purpose) ──────────
    {
        "question_number": 30,
        "difficulty": "easy",
        "question_en": "Necklace : Adornment :: ? : ?",
        "question_hi": "हार : अलंकार :: ? : ?",
        "option_a": "Medal : Decoration/पदक : सजावट",
        "option_b": "Bronze : Medal/काँसा : पदक",
        "option_c": "Scarf : Dress/स्कार्फ : पोशाक",
        "option_d": "Window : House/खिड़की : घर",
        "correct_answer": "A",
    },
    # ── Q31 ── Black:White (opposites) → Up:Down ──────────────────────────────
    {
        "question_number": 31,
        "difficulty": "easy",
        "question_en": "Black : White :: Up : ?",
        "question_hi": "काला : सफेद :: ऊपर : ?",
        "option_a": "Opposite/विपरीत",
        "option_b": "Disappointment/निराशा",
        "option_c": "Wall/दीवार",
        "option_d": "Down/नीचे",
        "correct_answer": "D",   # Black:White are opposites → Up:Down
    },
    # ── Q32 ── Horse:Hoof → Man:Foot (animal:foot-type) ──────────────────────
    {
        "question_number": 32,
        "difficulty": "easy",
        "question_en": "Horse : Hoof :: ? : ?",
        "question_hi": "घोड़ा : खुर :: ? : ?",
        "option_a": "Man : Foot/मनुष्य : पैर",
        "option_b": "Dog : Black/कुत्ता : काला",
        "option_c": "Paise : Rupee/पैसा : रुपया",
        "option_d": "Pen : Pencil/पेन : पेन्सिल",
        "correct_answer": "A",
    },
    # ── Q33 ── Night:Morning (precedes) → Evening:Night ───────────────────────
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": "Night : Morning :: ? : Night",
        "question_hi": "रात : सुबह :: ? : रात",
        "option_a": "Noon/दोपहर",
        "option_b": "Forenoon/पूर्वाह्न",
        "option_c": "Afternoon/अपराह्न",
        "option_d": "Evening/शाम",
        "correct_answer": "D",   # Evening precedes Night as Night precedes Morning
    },
    # ── Q34 ── Oxygen supports Burn; CO2 extinguishes fire ───────────────────
    {
        "question_number": 34,
        "difficulty": "medium",
        "question_en": "Oxygen : Burn :: Carbon dioxide : ?",
        "question_hi": "ऑक्सीजन : जलना :: कार्बन डाइऑक्साइड : ?",
        "option_a": "Isolate/अलग करना",
        "option_b": "Foam/झाग",
        "option_c": "Extinguishes/बुझाता है",
        "option_d": "Explode/विस्फोट",
        "correct_answer": "C",
    },
    # ── Q35 ── Human uses Carbohydrate for energy; Engine uses Petrol ─────────
    {
        "question_number": 35,
        "difficulty": "easy",
        "question_en": "Human : Carbohydrate :: Engine : ?",
        "question_hi": "मानव : कार्बोहाइड्रेट :: इंजन : ?",
        "option_a": "Wheel/पहिया",
        "option_b": "Carburettor/कार्बोरेटर",
        "option_c": "Cylinder/सिलिंडर",
        "option_d": "Petrol/पेट्रोल",
        "correct_answer": "D",
    },
    # ── Q36 ── Telephone evolved to Mobile phone; Computer evolved to Laptop ───
    {
        "question_number": 36,
        "difficulty": "easy",
        "question_en": "Telephone : Mobile phone :: Computer : ?",
        "question_hi": "टेलीफोन : मोबाइल फोन :: कंप्यूटर : ?",
        "option_a": "Keyboard/कीबोर्ड",
        "option_b": "Television/टेलीविज़न",
        "option_c": "Printer/प्रिंटर",
        "option_d": "Laptop/लैपटॉप",
        "correct_answer": "D",
    },
    # ── Q37 ── Food alleviates Hunger; Sleep alleviates Weariness ─────────────
    {
        "question_number": 37,
        "difficulty": "easy",
        "question_en": "Food : Hunger :: Sleep : ?",
        "question_hi": "भोजन : भूख :: नींद : ?",
        "option_a": "Weariness/थकान",
        "option_b": "Night/रात",
        "option_c": "Health/स्वास्थ्य",
        "option_d": "Dream/सपना",
        "correct_answer": "A",
    },
    # ── Q38 ── Teacher guides Student; Pontiff guides Disciple ────────────────
    {
        "question_number": 38,
        "difficulty": "easy",
        "question_en": "Teacher : Student :: Pontiff : ?",
        "question_hi": "शिक्षक : छात्र :: धर्माध्यक्ष : ?",
        "option_a": "Disciple/शिष्य",
        "option_b": "Follower/अनुयायी",
        "option_c": "Priest/पुजारी",
        "option_d": "Deity/देवता",
        "correct_answer": "A",
    },
    # ── Q39 ── Bees make Hum; Owls make Hoot ─────────────────────────────────
    {
        "question_number": 39,
        "difficulty": "easy",
        "question_en": "Bees : Hum :: Owls : ?",
        "question_hi": "मधुमक्खियाँ : भिनभिनाना :: उल्लू : ?",
        "option_a": "Roar/दहाड़ना",
        "option_b": "Talk/बात करना",
        "option_c": "Hiss/फुफकारना",
        "option_d": "Hoot/हूट करना",
        "correct_answer": "D",
    },
    # ── Q40 ── Confirmed:Inveterate → Financial:Bankrupt ─────────────────────
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": "Confirmed : Inveterate :: Financial : ?",
        "question_hi": "पक्का : दृढ़ :: आर्थिक : ?",
        "option_a": "Callow/अनुभवहीन",
        "option_b": "Incredible/अविश्वसनीय",
        "option_c": "Bankrupt/दिवालिया",
        "option_d": "Knot/गाँठ",
        "correct_answer": "C",
    },
    # ── Q41 ── Elephant's distinctive feature=Tusk; Parrot's=Beak ─────────────
    {
        "question_number": 41,
        "difficulty": "easy",
        "question_en": "Elephant : Tusk :: Parrot : ?",
        "question_hi": "हाथी : दाँत (दन्त) :: तोता : ?",
        "option_a": "Quill/कलम-पंख",
        "option_b": "Feather/पंख",
        "option_c": "Beak/चोंच",
        "option_d": "Spine/रीढ़",
        "correct_answer": "C",
    },
    # ── Q42 ── Virus causes Smallpox; Bacteria causes Typhoid ─────────────────
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": "Virus : Smallpox :: Bacteria : ?",
        "question_hi": "वायरस : चेचक :: बैक्टीरिया : ?",
        "option_a": "Chickenpox/छोटी माता",
        "option_b": "Typhoid/टाइफाइड",
        "option_c": "Malaria/मलेरिया",
        "option_d": "Sleeping sickness/निद्रा रोग",
        "correct_answer": "B",
    },
    # ── Q43 ── Kitchen is functional room in Home; Leaf is functional part of Plant
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": "Home : Kitchen :: Plant : ?",
        "question_hi": "घर : रसोई :: पौधा : ?",
        "option_a": "Root/जड़",
        "option_b": "Soil/मिट्टी",
        "option_c": "Leaf/पत्ती",
        "option_d": "Stem/तना",
        "correct_answer": "C",   # Kitchen cooks food; Leaf makes food (photosynthesis)
    },
    # ── Q44 ── Window made by Carpenter; Statue made by Sculptor ─────────────
    {
        "question_number": 44,
        "difficulty": "easy",
        "question_en": "Window : Carpenter :: Statue : ?",
        "question_hi": "खिड़की : बढ़ई :: मूर्ति : ?",
        "option_a": "Sculptor/मूर्तिकार",
        "option_b": "Mason/राजमिस्त्री",
        "option_c": "Blacksmith/लोहार",
        "option_d": "Goldsmith/सुनार",
        "correct_answer": "A",
    },
    # ── Q45 ── Cataract is disease of Eye; Eczema is disease of Skin ──────────
    {
        "question_number": 45,
        "difficulty": "medium",
        "question_en": "Eye : Cataract :: Skin : ?",
        "question_hi": "आँख : मोतियाबिन्द :: त्वचा : ?",
        "option_a": "Pyrorrhea/पायोरिया",
        "option_b": "Sinusitis/साइनसाइटिस",
        "option_c": "Eczema/एक्जिमा",
        "option_d": "Trachoma/ट्रेकोमा",
        "correct_answer": "C",
    },
    # ── Q46 ── Vitamin A found in Carrot; Vitamin C found in Orange ───────────
    {
        "question_number": 46,
        "difficulty": "easy",
        "question_en": "Vitamin A : Carrot :: Vitamin C : ?",
        "question_hi": "विटामिन A : गाजर :: विटामिन C : ?",
        "option_a": "Meat/माँस",
        "option_b": "Fish/मछली",
        "option_c": "Egg/अंडा",
        "option_d": "Orange/संतरा",
        "correct_answer": "D",
    },
    # ── Q47 ── Mango is a Fruit; Jasmine is a Flower ─────────────────────────
    {
        "question_number": 47,
        "difficulty": "easy",
        "question_en": "Mango : Fruit :: Jasmine : ?",
        "question_hi": "आम : फल :: चमेली : ?",
        "option_a": "Trees/पेड़",
        "option_b": "Fragrance/खुशबू",
        "option_c": "Flower/फूल",
        "option_d": "Rose/गुलाब",
        "correct_answer": "C",
    },
    # ── Q48 ── Dress made by Tailor; Furniture made by Carpenter ─────────────
    {
        "question_number": 48,
        "difficulty": "easy",
        "question_en": "Dress : Tailor :: ? : Carpenter",
        "question_hi": "पोशाक : दर्जी :: ? : बढ़ई",
        "option_a": "Wood/लकड़ी",
        "option_b": "Furniture/फर्नीचर",
        "option_c": "Leather/चमड़ा",
        "option_d": "Cloth/कपड़ा",
        "correct_answer": "B",
    },
    # ── Q49 ── Bow shoots Arrow; Pistol shoots Bullet ─────────────────────────
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": "Bow : Arrow :: Pistol : ?",
        "question_hi": "धनुष : तीर :: पिस्तौल : ?",
        "option_a": "Bullet/गोली",
        "option_b": "Gun/बंदूक",
        "option_c": "Shoot/गोली मारना",
        "option_d": "Rifle/राइफल",
        "correct_answer": "A",
    },
    # ── Q50 ── Crime leads to Punishment; Honesty leads to Reward ─────────────
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": "Crime : Punishment :: Honesty : ?",
        "question_hi": "अपराध : दण्ड :: ईमानदारी : ?",
        "option_a": "Award/पुरस्कार",
        "option_b": "Recognition/पहचान",
        "option_c": "Reward/इनाम",
        "option_d": "Pride/गर्व",
        "correct_answer": "C",
    },
    # ── Q51 ── Sepal is part of Flower; Tyre is part of Bicycle (part:whole) ──
    {
        "question_number": 51,
        "difficulty": "easy",
        "question_en": "Sepal : Flower :: ? : ?",
        "question_hi": "बाह्यदल : फूल :: ? : ?",
        "option_a": "Foot : Ball/पैर : गेंद",
        "option_b": "Tyre : Bicycle/टायर : साइकिल",
        "option_c": "Puppy : Dog/पिल्ला : कुत्ता",
        "option_d": "Sandals : Shoes/सैंडल : जूते",
        "correct_answer": "B",
    },
    # ── Q52 ── Seismometer measures Earthquakes; Thermometer measures Temperature
    {
        "question_number": 52,
        "difficulty": "easy",
        "question_en": "Seismometer : Earthquakes :: Thermometer : ?",
        "question_hi": "भूकम्पमापी : भूकम्प :: थर्मामीटर : ?",
        "option_a": "Mercury/पारा",
        "option_b": "Temperature/तापमान",
        "option_c": "Fever/बुखार",
        "option_d": "Doctor/चिकित्सक",
        "correct_answer": "B",
    },
    # ── Q53 ── Intl Literacy Day=Sep 8; Intl Women's Day=March 8 ─────────────
    {
        "question_number": 53,
        "difficulty": "medium",
        "question_en": (
            "International Literacy Day : September 8 :: "
            "International Women's Day : ?"
        ),
        "question_hi": (
            "अन्तर्राष्ट्रीय साक्षरता दिवस : 8 सितम्बर :: "
            "अन्तर्राष्ट्रीय महिला दिवस : ?"
        ),
        "option_a": "March 8/8 मार्च",
        "option_b": "June 26/26 जून",
        "option_c": "April 22/22 अप्रैल",
        "option_d": "November 4/4 नवम्बर",
        "correct_answer": "A",
    },
    # ── Q54 ── Ravishankar played Sitar; Bismillah Khan played Shehnai ─────────
    {
        "question_number": 54,
        "difficulty": "medium",
        "question_en": "Ravishankar : Sitar :: Bismillah Khan : ?",
        "question_hi": "रविशंकर : सितार :: बिस्मिल्लाह खाँ : ?",
        "option_a": "Sarod/सरोद",
        "option_b": "Santoor/संतूर",
        "option_c": "Shehnai/शहनाई",
        "option_d": "Flute/बाँसुरी",
        "correct_answer": "C",
    },
    # ── Q55 ── Mango is national fruit of India; Kiwi is of New Zealand ───────
    {
        "question_number": 55,
        "difficulty": "medium",
        "question_en": "India : Mango :: New Zealand : ?",
        "question_hi": "भारत : आम :: न्यूज़ीलैंड : ?",
        "option_a": "Apples/सेब",
        "option_b": "Kiwi/कीवी",
        "option_c": "Grapes/अंगूर",
        "option_d": "Bananas/केले",
        "correct_answer": "B",
    },
    # ── Q56 ── Entomology=study of Insects; Ophiology=study of Snakes ─────────
    {
        "question_number": 56,
        "difficulty": "medium",
        "question_en": "Insects : Entomology :: Snakes : ?",
        "question_hi": "कीड़े : कीट विज्ञान :: साँप : ?",
        "option_a": "Agrology/मृदा विज्ञान",
        "option_b": "Ophiology/सर्पविज्ञान",
        "option_c": "Mycology/कवकविज्ञान",
        "option_d": "Cetology/सीटोलॉजी",
        "correct_answer": "B",
    },
    # ── Q57 ── Book made of Paper; Bread made of Flour ───────────────────────
    {
        "question_number": 57,
        "difficulty": "easy",
        "question_en": "Book : Paper :: Bread : ?",
        "question_hi": "किताब : कागज :: रोटी : ?",
        "option_a": "Flour/आटा",
        "option_b": "Biscuit/बिस्कुट",
        "option_c": "Cake/केक",
        "option_d": "Butter/मक्खन",
        "correct_answer": "A",
    },
    # ── Q58 ── Perch lives in Fresh water; Cod lives in Salt water ────────────
    {
        "question_number": 58,
        "difficulty": "medium",
        "question_en": "Perch : Fresh water :: ? : Salt water",
        "question_hi": "पर्च : मीठा पानी :: ? : खारा पानी",
        "option_a": "Snake/साँप",
        "option_b": "Crocodile/मगरमच्छ",
        "option_c": "Frog/मेंढक",
        "option_d": "Cod/कॉड",
        "correct_answer": "D",
    },
    # ── Q59 ── Exercise done at Gym; Eating done at Restaurant ───────────────
    {
        "question_number": 59,
        "difficulty": "easy",
        "question_en": "Exercise : Gym :: Eating : ?",
        "question_hi": "व्यायाम : व्यायामशाला :: खाना : ?",
        "option_a": "Restaurant/रेस्तराँ",
        "option_b": "Food/खाना",
        "option_c": "Dieting/डाइटिंग",
        "option_d": "Fitness/फिटनेस",
        "correct_answer": "A",
    },
    # ── Q60 ── Teacher works at School; Banker works at Bank ─────────────────
    {
        "question_number": 60,
        "difficulty": "easy",
        "question_en": "School : Teacher :: Bank : ?",
        "question_hi": "स्कूल : शिक्षक :: बैंक : ?",
        "option_a": "Peon/चपरासी",
        "option_b": "Banker/बैंकर",
        "option_c": "Manager/प्रबंधक",
        "option_d": "Cashier/कैशियर",
        "correct_answer": "B",
    },
    # ── Q61 ── Prediction is about Future; Regret is about Past ─────────────
    {
        "question_number": 61,
        "difficulty": "easy",
        "question_en": "Prediction : Future :: Regret : ?",
        "question_hi": "पूर्वानुमान : भविष्य :: पश्चाताप : ?",
        "option_a": "Present/वर्तमान",
        "option_b": "Sin/पाप",
        "option_c": "Time/समय",
        "option_d": "Past/अतीत",
        "correct_answer": "D",
    },
    # ── Q62 ── Adversary=Enemy (synonyms); Adversity=Difficulty ─────────────
    {
        "question_number": 62,
        "difficulty": "easy",
        "question_en": "Adversary : Enemy :: Adversity : ?",
        "question_hi": "विरोधी : शत्रु :: विपत्ति : ?",
        "option_a": "Dynamic/गतिशील",
        "option_b": "Love/प्रेम",
        "option_c": "Difficulty/कठिनाई",
        "option_d": "Friend/मित्र",
        "correct_answer": "C",
    },
    # ── Q63 ── Bird eats Worm (predator:prey); Cat eats Mouse ────────────────
    {
        "question_number": 63,
        "difficulty": "easy",
        "question_en": "Bird : Worm :: ? : ?",
        "question_hi": "पक्षी : कीड़ा :: ? : ?",
        "option_a": "Trap : Cheese/जाल : पनीर",
        "option_b": "Lion : Cave/शेर : गुफा",
        "option_c": "Cat : Mouse/बिल्ली : चूहा",
        "option_d": "Horse : Stable/घोड़ा : अस्तबल",
        "correct_answer": "C",
    },
    # ── Q64 ── Apes make Gibber; Camels make Grunt ───────────────────────────
    {
        "question_number": 64,
        "difficulty": "medium",
        "question_en": "Apes : Gibber :: Camels : ?",
        "question_hi": "वानर : चिल्लाना :: ऊँट : ?",
        "option_a": "Grunt/घुरघुराना",
        "option_b": "Cheep/चीं-चीं",
        "option_c": "Loud/ज़ोर से",
        "option_d": "Whine/कराहना",
        "correct_answer": "A",
    },
    # ── Q65 ── Cytology=study of Cell; Ornithology=study of Birds ────────────
    {
        "question_number": 65,
        "difficulty": "medium",
        "question_en": "Cell : Cytology :: Birds : ?",
        "question_hi": "कोशिका : कोशिका विज्ञान :: पक्षी : ?",
        "option_a": "Odontology/दन्त विज्ञान",
        "option_b": "Mycology/कवकविज्ञान",
        "option_c": "Ornithology/पक्षी विज्ञान",
        "option_d": "Etymology/व्युत्पत्ति विज्ञान",
        "correct_answer": "C",
    },
    # ── Q66 ── Actor performs in Play; Musician performs in Concert ───────────
    {
        "question_number": 66,
        "difficulty": "easy",
        "question_en": "Play : Actor :: Concert : ?",
        "question_hi": "नाटक : अभिनेता :: संगीत कार्यक्रम : ?",
        "option_a": "Symphony/सिम्फनी",
        "option_b": "Musician/संगीतकार",
        "option_c": "Piano/पियानो",
        "option_d": "Percussion/तालवाद्य",
        "correct_answer": "B",
    },
    # ── Q67 ── Aestivation=dormancy in Summer; Hibernation=dormancy in Winter ─
    {
        "question_number": 67,
        "difficulty": "medium",
        "question_en": "Summer : Aestivation :: Winter : ?",
        "question_hi": "गर्मी : ग्रीष्म निष्क्रियता :: सर्दी : ?",
        "option_a": "Cache/संचय",
        "option_b": "Hibernation/शीत निष्क्रियता",
        "option_c": "Survival/जीवन-रक्षा",
        "option_d": "Activation/सक्रियण",
        "correct_answer": "B",
    },
    # ── Q68 ── Calendar contains Dates; Dictionary contains Words ────────────
    {
        "question_number": 68,
        "difficulty": "easy",
        "question_en": "Calendar : Dates :: Dictionary : ?",
        "question_hi": "कैलेंडर : तारीखें :: शब्दकोश : ?",
        "option_a": "Words/शब्द",
        "option_b": "Books/किताबें",
        "option_c": "Language/भाषा",
        "option_d": "Vocabulary/शब्द-भंडार",
        "correct_answer": "A",
    },
    # ── Q69 ── Pesticide protects Plant; Vaccination protects Baby ────────────
    {
        "question_number": 69,
        "difficulty": "medium",
        "question_en": "Pesticide : Plant :: ? : ?",
        "question_hi": "कीटनाशक : पौधा :: ? : ?",
        "option_a": "Medicine : Cure/दवा : इलाज",
        "option_b": "Injection : Fever/इंजेक्शन : बुखार",
        "option_c": "Vaccination : Baby/टीका : शिशु",
        "option_d": "Sinarest : Cold/सिनारेस्ट : सर्दी",
        "correct_answer": "C",
    },
    # ── Q70 ── Iron Man of India=Patel; Father of the Nation=Mahatma Gandhi ──
    {
        "question_number": 70,
        "difficulty": "easy",
        "question_en": (
            "Iron Man of India : Sardar Vallabhbhai Patel :: "
            "Father of the Nation : ?"
        ),
        "question_hi": (
            "भारत के लोहपुरुष : सरदार वल्लभभाई पटेल :: "
            "राष्ट्रपिता : ?"
        ),
        "option_a": "Lokmanya Tilak/लोकमान्य तिलक",
        "option_b": "Rajeev Gandhi/राजीव गाँधी",
        "option_c": "Jawahar Lal Nehru/जवाहरलाल नेहरू",
        "option_d": "Mahatma Gandhi/महात्मा गाँधी",
        "correct_answer": "D",
    },
]

# Fix map for any pre-existing records (ans=None) skipped by deduplication
_FIXES = {
    q["question_number"]: (q["correct_answer"], {
        "option_a": q["option_a"],
        "option_b": q["option_b"],
        "option_c": q["option_c"],
        "option_d": q["option_d"],
    })
    for q in QUESTIONS
}


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_short = {
            row[0][:80]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            fp = d["question_en"][:80]
            if fp in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB (will update below)")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")

        # ── Fix any pre-existing records that were skipped ────────────────────
        updates = 0
        for qnum, (ans, fields) in _FIXES.items():
            q = db.query(Question).filter(
                Question.topic == TOPIC,
                Question.subject == SUBJECT,
                Question.question_number == qnum,
                Question.correct_answer == None,
            ).first()
            if q:
                q.correct_answer = ans
                for field, val in fields.items():
                    setattr(q, field, val)
                q.source_pdf = SOURCE
                updates += 1
                print(f"  UPDATE Q{qnum}: correct_answer={ans}")

        db.commit()
        if updates:
            print(f"Fixed {updates} pre-existing records.")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
