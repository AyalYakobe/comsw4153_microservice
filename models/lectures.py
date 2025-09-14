from __future__ import annotations

from typing import Optional, List, Annotated
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr, StringConstraints

from .address import AddressBase

# Columbia UNI: 2–3 lowercase letters + 1–4 digits (e.g., abc1234)
UNIType = Annotated[str, StringConstraints(pattern=r"^[a-z]{2,3}\d{1,4}$")]


class LectureBase(BaseModel):
    code: UNIType = Field(
        ...,
        description="Code of the lecture.",
        json_schema_extra={"example": "abc1234"},
    )
    professor: str = Field(
        ...,
        description="Given name.",
        json_schema_extra={"example": "Ada"},
    )
    start_date: Optional[date] = Field(
        None,
        description="start date (YYYY-MM-DD).",
        json_schema_extra={"example": "1815-12-10"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "abc1234",
                    "professor": "Ada",
                    "start_date": "Lovelace"
                }
            ]
        }
    }


class LectureCreate(LectureBase):
    """Creation payload for a Person."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "abc1234",
                    "professor": "Ada",
                    "start_date": "Lovelace"
                }
            ]
        }
    }


class LectureUpdate(BaseModel):
    """Partial update for a Person; supply only fields to change."""
    code: Optional[UNIType] = Field(
        None, description="Columbia UNI.", json_schema_extra={"example": "ab1234"}
    )
    professor: Optional[str] = Field(None, json_schema_extra={"example": "Augusta"})
    start_date: Optional[date] = Field(None, json_schema_extra={"example": "1815-12-10"})


class LectureRead(LectureBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Lecture ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "99999999-9999-4999-8999-999999999999",
                    "code": "abc1234",
                    "professor": "Ada",
                    "start_date": "1815-12-10",
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }
