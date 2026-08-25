from pydantic import BaseModel
from typing import Optional


class QuestionResponse(BaseModel):
    id:              int
    exam:            Optional[str]
    subject:         str
    topic:           Optional[str]
    difficulty:      Optional[str]
    question_number: Optional[int]
    question_en:     str
    question_hi:     Optional[str]
    # question_text alias for frontend compatibility
    question_text:   Optional[str] = None
    option_a:        str
    option_b:        str
    option_c:        str
    option_d:        str
    source_pdf:      Optional[str]
    image_url:       Optional[str] = None
    # correct_answer is NOT returned here — only after submission

    model_config = {"from_attributes": True}


class QuestionCreate(BaseModel):
    exam:           Optional[str] = None
    subject:        str
    topic:          Optional[str] = None
    question_number: Optional[int] = None
    question_en:    str
    question_hi:    Optional[str] = None
    option_a:       str
    option_b:       str
    option_c:       str
    option_d:       str
    correct_answer: Optional[str] = None
    difficulty:     Optional[str] = None
    source_pdf:     Optional[str] = None
