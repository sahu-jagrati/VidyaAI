from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
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


@router.get("/daily", response_model=List[QuestionResponse])
def daily_questions(
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    """Return 5 mixed-difficulty questions for today's challenge."""
    questions = get_daily_questions(current_user.id, db)
    if not questions:
        raise HTTPException(status_code=404, detail="No questions available. Please add questions to the database.")
    return questions


@router.post("/submit", response_model=AttemptResult)
def submit_answer(
    payload:      AttemptSubmit,
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    """Submit an answer, record the attempt, update XP and streak."""
    question = db.query(Question).filter(Question.id == payload.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    is_correct = (
        payload.selected_answer is not None
        and payload.selected_answer.upper() == question.correct_answer.upper()
    )
    xp_earned = calculate_xp(question.difficulty, is_correct, payload.time_taken)

    # Record attempt
    attempt = Attempt(
        user_id         = current_user.id,
        question_id     = question.id,
        selected_answer = payload.selected_answer,
        is_correct      = is_correct,
        xp_earned       = xp_earned,
        time_taken      = payload.time_taken,
    )
    db.add(attempt)

    # Update user stats
    current_user.xp              += xp_earned
    current_user.total_questions += 1
    if is_correct:
        current_user.correct_answers += 1
        update_streak(current_user)    # streak only advances on correct answers

    db.commit()
    db.refresh(current_user)

    return AttemptResult(
        question_id    = question.id,
        is_correct     = is_correct,
        correct_answer = question.correct_answer,
        explanation    = question.explanation,
        xp_earned      = xp_earned,
        user_total_xp  = current_user.xp,
        current_streak = current_user.current_streak,
    )
