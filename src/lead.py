
from pydantic import BaseModel, Field, EmailStr


class Lead(BaseModel):
    name: str = Field(min_length=2)
    email: EmailStr
    business_name: str = Field(min_length=2)
    service_needed: str = Field(min_length=3)
    budget: str = Field(min_length=1)
    message: str = Field(min_length=10)
