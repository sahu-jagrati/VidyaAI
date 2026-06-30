from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    name:     str
    email:    EmailStr
    password: str


class UserLogin(BaseModel):
    email:    EmailStr
    password: str


class UserResponse(BaseModel):
    id:              int
    name:            str
    email:           str
    xp:              int
    current_streak:  int
    highest_streak:  int
    total_questions: int
    accuracy:        float
    created_at:      datetime

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type:   str = "bearer"
    user:         UserResponse


class GoogleAuthRequest(BaseModel):
    token: str
