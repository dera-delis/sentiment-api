from __future__ import annotations

from dataclasses import dataclass

from transformers import pipeline

from app.config import Settings


@dataclass(frozen=True)
class SentimentResult:
    label: str
    confidence: float


class SentimentService:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._pipeline = pipeline(
            "sentiment-analysis",
            model=settings.model_name,
            truncation=True,
            top_k=None,
        )

    def analyze(self, text: str) -> SentimentResult:
        scores = self._pipeline(text)[0]
        score_map = {item["label"].upper(): float(item["score"]) for item in scores}
        positive = score_map.get("POSITIVE", 0.0)
        negative = score_map.get("NEGATIVE", 0.0)

        diff = abs(positive - negative)
        if diff <= self._settings.neutral_margin:
            return SentimentResult(label="neutral", confidence=max(0.0, 1.0 - diff))

        if positive >= negative:
            return SentimentResult(label="positive", confidence=positive)

        return SentimentResult(label="negative", confidence=negative)

