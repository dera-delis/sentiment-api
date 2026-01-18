FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/app/.cache/huggingface

COPY requirements.docker.txt .
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.docker.txt

RUN python -c "from pathlib import Path; from optimum.onnxruntime import ORTModelForSequenceClassification; from transformers import AutoTokenizer; model_name='distilbert-base-uncased-finetuned-sst-2-english'; model_path=Path('/app/model'); model_path.mkdir(parents=True, exist_ok=True); tokenizer=AutoTokenizer.from_pretrained(model_name); tokenizer.save_pretrained(model_path); ORTModelForSequenceClassification.from_pretrained(model_name, export=True, provider='CPUExecutionProvider').save_pretrained(model_path)"

COPY app ./app

ENV PORT=8000

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]

