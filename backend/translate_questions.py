"""
Run once to translate all questions to Hindi.
Usage: python translate_questions.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

try:
    from deep_translator import GoogleTranslator
    def translate(text):
        if not text: return None
        try:
            return GoogleTranslator(source='en', target='hi').translate(text)
        except Exception as e:
            print(f"  ERROR: {e}")
            return None
    print("✓ deep-translator loaded")
except ImportError:
    print("✗ deep-translator not installed. Run: pip install deep-translator")
    sys.exit(1)

db = SessionLocal()

total = db.query(Question).count()
print(f"Total questions in DB: {total}")

if total == 0:
    print("No questions in DB at all. Add questions first.")
    db.close()
    sys.exit(0)

# Show first question's current state
first = db.query(Question).first()
print(f"\nSample question:")
print(f"  EN: {first.question_text[:80]}")
print(f"  HI: {first.question_text_hi}")

# Re-translate ALL questions (overwrite whatever was there)
questions = db.query(Question).all()
print(f"\nTranslating all {len(questions)} questions...\n")

for i, q in enumerate(questions):
    print(f"[{i+1}/{len(questions)}] {q.question_text[:60]}")
    q.question_text_hi = translate(q.question_text)
    q.option_a_hi      = translate(q.option_a)
    q.option_b_hi      = translate(q.option_b)
    q.option_c_hi      = translate(q.option_c)
    q.option_d_hi      = translate(q.option_d)
    q.explanation_hi   = translate(q.explanation)
    db.commit()
    print(f"  → {q.question_text_hi}")

print(f"\nDone! All {len(questions)} questions translated.")
db.close()
