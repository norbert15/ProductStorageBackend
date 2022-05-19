from datetime import date, datetime
from typing import Any, Optional
from pydantic import BaseModel

from models.schemas.base import BaseSchema


class LoggingBase(BaseModel):
    description: str
    period: datetime


class LoggingCreate(LoggingBase):
    pass


class LoggingResponse(BaseSchema, LoggingBase):
    pass