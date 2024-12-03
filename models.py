from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    gender: str
    birth_date: datetime
    country: str
    address: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    gender: Optional[str] = None
    birth_date: Optional[datetime] = None
    country: Optional[str] = None
    address: Optional[str] = None

class Student(StudentBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True