from __future__ import annotations

from fastapi import APIRouter, Request

from app.schemas import AnalyzeRequest, AnalyzeResponse, HealthResponse
from app.services.sentiment import SentimentService

router = APIRouter()


def _get_service(request: Request) -> SentimentService:
    return request.app.state.sentiment_service


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_sentiment(payload: AnalyzeRequest, request: Request) -> AnalyzeResponse:
    service = _get_service(request)
    result = service.analyze(payload.text)
    return AnalyzeResponse(label=result.label, confidence=result.confidence)


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok")

