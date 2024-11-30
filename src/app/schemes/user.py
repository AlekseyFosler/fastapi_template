from datetime import datetime

from pydantic import UUID4, BaseModel, Field


class RequestUser(BaseModel):
    full_name: str = Field(
        examples=['Fosler Alexey Anatolevich'],
    )
    mobile_phone: str = Field(
        examples=['9026777080'],
        max_length=10,
        min_length=10,
    )


class ResponseBriefUser(BaseModel):
    user_id: UUID4
    full_name: str


class ResponseUser(ResponseBriefUser):
    mobile_phone: str
    created_at: datetime
    updated_at: datetime
