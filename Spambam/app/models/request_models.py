from pydantic import BaseModel, EmailStr, Field


class EmailRequest(BaseModel):
    sender_email: EmailStr = Field(..., description="Sender email address")
    subject: str = Field(default="", description="Email subject line")
    body: str = Field(default="", description="Email body text")