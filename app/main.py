from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings
from app.routers.analyze import router as analyze_router
from app.services.sentiment import SentimentService


def create_app() -> FastAPI:
    settings = get_settings()
    logging.basicConfig(level=settings.log_level)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.sentiment_service = SentimentService(settings)
        logging.getLogger(__name__).info("Sentiment model loaded")
        yield

    app = FastAPI(title="Sentiment Analysis API", lifespan=lifespan)
    app.include_router(analyze_router)
    return app


app = create_app()

