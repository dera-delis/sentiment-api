from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app


def test_analyze_positive() -> None:
    with TestClient(app) as client:
        response = client.post("/analyze", json={"text": "I love this product"})
        assert response.status_code == 200
        payload = response.json()
        assert payload["label"] in {"positive", "negative", "neutral"}
        assert 0.0 <= payload["confidence"] <= 1.0
        assert payload["label"] == "positive"


def test_analyze_negative() -> None:
    with TestClient(app) as client:
        response = client.post("/analyze", json={"text": "This is terrible and disappointing"})
        assert response.status_code == 200
        payload = response.json()
        assert payload["label"] in {"positive", "negative", "neutral"}
        assert 0.0 <= payload["confidence"] <= 1.0
        assert payload["label"] == "negative"


def test_analyze_empty_rejected() -> None:
    with TestClient(app) as client:
        response = client.post("/analyze", json={"text": "   "})
        assert response.status_code == 422

