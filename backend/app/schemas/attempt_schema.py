from pydantic import BaseModel
from typing import Optional


class AttemptSubmit(BaseModel):
    question_id:     int
    selected_answer: Optional[str] = None
    time_taken:      int
    lang:            str = "en"


class AttemptResult(BaseModel):
    question_id:     int
    is_correct:      bool
    correct_answer:  Optional[str]   # null when answer not yet available
    explanation:     Optional[str]   # null when answer not yet available
    xp_earned:       int
    user_total_xp:   int
    current_streak:  int
