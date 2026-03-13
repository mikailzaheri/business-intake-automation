from pydantic import BaseModel, EmailStr
from typing import Optional

class IntakeRequest(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    business_type: str
    message: str

class IntakeResponse(BaseModel):
    status: str
    category: str
    urgency: str
    summary: str
