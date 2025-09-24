from datetime import datetime

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str = Field(..., max_length=20)
    content: str = Field(max_length=300)
    is_public: bool = True
    is_completed: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

class NoteUpdate(BaseModel):
    title: str = Field(max_length=20)
    content: str = Field(max_length=300)
    is_public: bool = True
    is_completed: bool = True
    updated_at: datetime = Field(default_factory=datetime.now)

class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    is_public: bool
    is_completed: bool
    created_at: datetime
    updated_at: datetime