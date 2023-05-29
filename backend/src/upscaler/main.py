from typing import Dict
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from upscaler.ai.model import load_model
from upscaler.api.router import router_v1
from upscaler.core.config import settings
from upscaler.middlewares.upload_middleware import LimitUploadSizeMiddleware
from upscaler.middlewares.response_time_middleware import ResponseTimeMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        load_model()
        yield
    finally:
        # clean up if needed
        pass


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    redoc_url="",  # disable redoc
    lifespan=lifespan,
)

# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_methods=settings.CORS_ALLOWED_METHODS,
    allow_headers=settings.CORS_ALLOWED_HEADERS,
)
app.add_middleware(ResponseTimeMiddleware)
app.add_middleware(LimitUploadSizeMiddleware)



@app.get("/", tags=["home"])
async def home() -> Dict[str, str]:
    return {
        "message": "Welcome to the Upscaler API",
    }


# Our routers
app.include_router(router_v1)
