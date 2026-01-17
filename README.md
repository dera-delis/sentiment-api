# Sentiment Analysis API

Production-grade FastAPI microservice that runs transformer-based sentiment analysis using
`distilbert-base-uncased-finetuned-sst-2-english`.

## Tech Stack
- FastAPI (Python 3.11)
- Hugging Face Transformers
- Pydantic
- Uvicorn
- Docker + docker-compose
- pytest

## API

`POST /analyze`

Request:
```json
{
  "text": "I love this product"
}
```

Response:
```json
{
  "label": "positive",
  "confidence": 0.9821
}
```

Rules:
- `label`: `positive`, `negative`, or `neutral`
- `confidence`: float between 0 and 1
- Empty or whitespace-only text returns 422

`GET /health` → `{ "status": "ok" }`

## Local Run
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker
```bash
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```

Using docker-compose:
```bash
docker-compose up --build
```

## Testing
```bash
pytest
```

## Why This Matters
This project demonstrates real model integration, clean API design, deterministic
inference, and production-ready packaging—exactly the skill set expected from an
AI-capable backend engineer.

