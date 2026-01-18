from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
        protected_namespaces=(),
    )

    model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"
    model_path: str = "/app/model"
    neutral_margin: float = 0.1
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()

