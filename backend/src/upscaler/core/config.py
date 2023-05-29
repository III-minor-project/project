from typing import List
from functools import lru_cache

from pydantic import BaseSettings

class Setting(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True

    # General
    APP_NAME: str = 'upscaler'
    APP_VERSION: str = '0.1.0'
    APP_DESCRIPTION: str = 'API for upscaling images'

    # API
    FILE_UPLOAD_MAX_SIZE: int = 50 * 1024 * 1024  # 50 MB
    ALLOWED_EXTENSIONS: List[str] = [
        'image/jpg', 'image/jpeg', 'image/png', 'application/pdf', 'text/plain'
    ]

    # CORS
    CORS_ALLOWED_ORIGINS: List[str] = ['http://localhost:5500']
    CORS_ALLOWED_HEADERS: List[str] = ['*']
    CORS_ALLOWED_METHODS: List[str] = ['*']

@lru_cache(maxsize=1)
def _setting() -> Setting:
    return Setting()


settings = _setting()