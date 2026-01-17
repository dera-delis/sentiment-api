from __future__ import annotations

from pydantic import BaseModel, Field, field_validator


class AnalyzeRequest(BaseModel):
    text: str = Field(..., description="Input text to analyze")

    @field_validator("text")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        cleaned = " ".join(value.split())
        if not cleaned:
            raise ValueError("Text must not be empty")
        return cleaned


class AnalyzeResponse(BaseModel):
    label: str = Field(..., description="positive, negative, or neutral")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")


class HealthResponse(BaseModel):
    status: str = Field(..., description="Service status")

