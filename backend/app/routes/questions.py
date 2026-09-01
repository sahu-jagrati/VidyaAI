from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from app.database.connection      import get_db
from app.models.user_model        import User
from app.models.question_model    import Question
from app.models.attempt_model     import Attempt
from app.schemas.question_schema  import QuestionResponse
from app.schemas.attempt_schema   import AttemptSubmit, AttemptResult
from app.services.xp_service      import calculate_xp
from app.services.streak_service  import update_streak
from app.services.question_service import get_daily_questions
from app.utils.helpers            import get_current_user

router = APIRouter(prefix="/questions", tags=["Questions"])


def _to_dict(q: Question, lang: str) -> dict:
    hi = lang == "hi"
    display_text = (q.question_hi or q.question_en) if hi else q.question_en
    return {
        "id":              q.id,
        "exam":            q.exam,
        "subject":         q.subject,
        "topic":           q.topic,
        "difficulty":      q.difficulty,
        "question_number": q.question_number,
        "question_en":     q.question_en,
        "question_hi":     q.question_hi,
        "question_text":   display_text,   # alias for frontend compat
        "option_a":        q.option_a,
        "option_b":        q.option_b,
        "option_c":        q.option_c,
        "option_d":        q.option_d,
        "source_pdf":      q.source_pdf,
        "image_url":        q.image_url,
        "answer_image_url": q.answer_image_url,
    }


@router.get("/topic", response_model=List[QuestionResponse])
def topic_questions(
    subject: str     = Query(...),
    topic:   str     = Query(...),
    lang:    str     = Query("en"),
    limit:   int     = Query(200, le=500),
    db:      Session = Depends(get_db),
):
    questions = (
        db.query(Question)
        .filter(
            func.lower(Question.subject) == subject.lower(),
            func.lower(Question.topic)   == topic.lower(),
        )
        .order_by(Question.question_number, Question.id)
        .limit(limit)
        .all()
    )
    if not questions:
        raise HTTPException(
            status_code=404,
            detail=f"No questions found for subject='{subject}' topic='{topic}'.",
        )
    return [_to_dict(q, lang) for q in questions]


@router.get("/daily", response_model=List[QuestionResponse])
def daily_questions(
    lang:         str     = Query("en"),
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    questions = get_daily_questions(current_user.id, db)
    if not questions:
        raise HTTPException(
            status_code=404,
            detail="No questions available. Please add questions to the database.",
        )
    return [_to_dict(q, lang) for q in questions]


@router.post("/submit", response_model=AttemptResult)
def submit_answer(
    payload:      AttemptSubmit,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    question = db.query(Question).filter(Question.id == payload.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    # If answer key not yet available, record attempt but award no XP
    if not question.correct_answer:
        attempt = Attempt(
            user_id         = current_user.id,
            question_id     = question.id,
            selected_answer = payload.selected_answer,
            is_correct      = False,
            xp_earned       = 0,
            time_taken      = payload.time_taken,
        )
        db.add(attempt)
        current_user.total_questions += 1
        db.commit()
        db.refresh(current_user)
        return AttemptResult(
            question_id    = question.id,
            is_correct     = False,
            correct_answer = None,
            explanation    = "Answer key for this question is coming soon.",
            xp_earned      = 0,
            user_total_xp  = current_user.xp,
            current_streak = current_user.current_streak,
        )

    is_correct = (
        payload.selected_answer is not None
        and payload.selected_answer.upper() == question.correct_answer.upper()
    )
    xp_earned = calculate_xp(question.difficulty, is_correct, payload.time_taken)

    attempt = Attempt(
        user_id         = current_user.id,
        question_id     = question.id,
        selected_answer = payload.selected_answer,
        is_correct      = is_correct,
        xp_earned       = xp_earned,
        time_taken      = payload.time_taken,
    )
    db.add(attempt)

    current_user.xp              += xp_earned
    current_user.total_questions += 1
    if is_correct:
        current_user.correct_answers += 1
        update_streak(current_user)

    db.commit()
    db.refresh(current_user)

    return AttemptResult(
        question_id    = question.id,
        is_correct     = is_correct,
        correct_answer = question.correct_answer,
        explanation    = None,
        xp_earned      = xp_earned,
        user_total_xp  = current_user.xp,
        current_streak = current_user.current_streak,
    )
