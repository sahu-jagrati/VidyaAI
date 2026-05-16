from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AttemptSubmit(BaseModel):
    question_id:     int
    selected_answer: Optional[str] = None   # None means timed out
    time_taken:      int                    # seconds taken


class AttemptResult(BaseModel):
    question_id:     int
    is_correct:      bool
    correct_answer:  str
    explanation:     str
    xp_earned:       int
    user_total_xp:   int
    current_streak:  int
