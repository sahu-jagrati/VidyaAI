from sqlalchemy.orm import Session
from app.models.question_model import Question
from app.services.translation_service import translate_hi


def translate_missing_questions(db: Session) -> int:
    questions = db.query(Question).filter(Question.question_text_hi.is_(None)).all()
    updated = 0
    for q in questions:
        q.question_text_hi = translate_hi(q.question_text)
        q.option_a_hi      = translate_hi(q.option_a)
        q.option_b_hi      = translate_hi(q.option_b)
        q.option_c_hi      = translate_hi(q.option_c)
        q.option_d_hi      = translate_hi(q.option_d)
        q.explanation_hi   = translate_hi(q.explanation)
        updated += 1
    if updated:
        db.commit()
        print(f"[questions] Translated {updated} questions to Hindi")
    return updated
