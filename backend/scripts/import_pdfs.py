import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import fitz  # PyMuPDF  # noqa: E402

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "questions")
EXTRACTED_DIR = os.path.join(BASE_DIR, "extracted_text")

SUBJECT_MAP = {
    "quant": "Quantitative Aptitude",
    "reasoning": "Reasoning",
    "english": "English",
    "general_awareness": "General Awareness",
}

TOPIC_MAP = {
    "profit_loss": "Profit & Loss",
    "percentage": "Percentage",
    "ratio": "Ratio",
    "ratio_and_proportion": "Ratio & Proportion",
    "average": "Average",
    "time_and_work": "Time & Work",
    "pipe_cistern": "Pipe & Cistern",
    "train_sheet": "Train Sheet",
    "simple_interest": "Simple Interest",
    "compound_interest": "Compound Interest",
    "mixture_alligation": "Mixture & Alligation",
    "partnership": "Partnership",
    "discount": "Discount",
    "data_interpretation": "Data Interpretation",
    "probability": "Probability",
    "permutation_combination": "Permutation & Combination",
    "boat_stream": "Boat & Stream",
    "coordinate_geometry": "Coordinate Geometry",
    "number_system": "Number System",
    "speed_time_distance": "Speed, Time & Distance",
    "geometry": "Geometry",
    "mensuration_2d": "Mensuration 2D",
    "mensuration_3d": "Mensuration 3D",
    "algebra": "Algebra",
    "trigonometry": "Trigonometry",
    "lcm_hcf": "LCM & HCF",
    "simplification": "Simplification",
    "statistics": "Statistics",
    "quadratic_equations": "Quadratic Equations",
    "surds_indices": "Surds & Indices",
    "ap_gp_hp": "AP, GP & HP",
    "height_distance": "Height & Distance",
    "maxima_minima": "Maxima & Minima",
    "race_sheet": "Race",
    "problem_on_ages": "Problem on Ages",
    "dishonest_shopkeeper": "Dishonest Shopkeeper",
    "analogy": "Analogy",
    "classification": "Classification",
    "series": "Series",
    "blood_relation": "Blood Relation",
    "direction_distance": "Direction & Distance",
    "coding_decoding": "Coding-Decoding",
    "alphabet": "Alphabet",
    "syllogism": "Syllogism",
    "inequality": "Inequality",
    "ranking": "Ranking",
    "seating_arrangement": "Seating Arrangement",
    "puzzle": "Puzzle",
    "calendar": "Calendar",
    "clock": "Clock",
    "dice": "Dice",
    "cube_cuboid": "Cube & Cuboid",
    "venn_diagram": "Venn Diagram",
    "non_verbal": "Non-Verbal Reasoning",
    "counting_figures": "Counting Figures",
    "number_series": "Number Series",
    "letter_series": "Letter Series",
    "missing_number": "Missing Number",
    "pair_formation": "Pair Formation",
    "analytical_reasoning": "Analytical Reasoning",
    "assertion_reason": "Assertion & Reason",
    "statement_argument": "Statement & Argument",
    "assumptions": "Assumptions",
    "cause_effect": "Cause & Effect",
    "course_of_action": "Course of Action",
    "decision_making": "Decision Making",
    "data_sufficiency": "Data Sufficiency",
    "coded_equation": "Coded Equation",
    "word_based": "Word-Based Problems",
    "synonym": "Synonym",
    "antonym": "Antonym",
    "idioms": "Idioms & Phrases",
    "error_detection": "Error Detection",
    "fill_blanks": "Fill in the Blanks",
    "reading_comprehension": "Reading Comprehension",
    "sentence_improvement": "Sentence Improvement",
    "one_word_substitution": "One Word Substitution",
    "spelling": "Spelling",
    "cloze_test": "Cloze Test",
    "history": "History",
    "polity": "Polity",
    "geography": "Geography",
    "science": "Science",
    "current_affairs": "Current Affairs",
    "economy": "Economy",
    "static_gk": "Static GK",
    "sports": "Sports",
    "art_culture": "Art & Culture",
}


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


def save_extracted_text(filename, subject_folder, topic_folder, text):
    out_dir = os.path.join(EXTRACTED_DIR, subject_folder, topic_folder)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename + ".txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    return out_path


def process_all_pdfs():
    found = 0

    for subject_folder in os.listdir(DATA_DIR):
        subject_path = os.path.join(DATA_DIR, subject_folder)
        if not os.path.isdir(subject_path):
            continue

        subject_name = SUBJECT_MAP.get(subject_folder, subject_folder.replace("_", " ").title())

        for topic_folder in os.listdir(subject_path):
            topic_path = os.path.join(subject_path, topic_folder)
            if not os.path.isdir(topic_path):
                continue

            topic_name = TOPIC_MAP.get(topic_folder, topic_folder.replace("_", " ").title())

            for file in os.listdir(topic_path):
                if not file.endswith(".pdf"):
                    continue

                pdf_path = os.path.join(topic_path, file)
                print(f"\n[{subject_name} → {topic_name}] {file}")

                try:
                    text = extract_text_from_pdf(pdf_path)
                    out_path = save_extracted_text(file, subject_folder, topic_folder, text)
                    rel_path = os.path.relpath(out_path, BASE_DIR)
                    preview = text[:300].replace("\n", " ")
                    print(f"  {len(text)} chars → {rel_path}")
                    print(f"  Preview: {preview}")
                    found += 1
                except Exception as e:
                    print(f"  ERROR: {e}")

    if found == 0:
        print(
            "\nNo PDFs found.\n"
            "Place PDFs inside:  backend/data/questions/<subject>/<topic>/\n"
            "Example:            backend/data/questions/quant/profit_loss/Sheet-1.pdf"
        )
    else:
        print(f"\nDone. Processed {found} PDF(s). Check extracted_text/ for output.")


if __name__ == "__main__":
    process_all_pdfs()
