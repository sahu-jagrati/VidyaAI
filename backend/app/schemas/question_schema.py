from pydantic import BaseModel
from typing import Optional


class QuestionResponse(BaseModel):
    id:            int
    subject:       str
    subject_code:  str
    topic:         Optional[str]
    difficulty:    str
    phase:         str
    question_text: str
    option_a:      str
    option_b:      str
    option_c:      str
    option_d:      str
    # correct_answer is NOT included here — sent only after submission

    model_config = {"from_attributes": True}


class QuestionCreate(BaseModel):
    subject:        str
    subject_code:   str
    topic:          Optional[str] = None
    difficulty:     str
    phase:          str = "main"
    question_text:  str
    option_a:       str
    option_b:       str
    option_c:       str
    option_d:       str
    correct_answer: str
    explanation:    str
