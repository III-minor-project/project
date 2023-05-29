from fastapi import APIRouter

from upscaler.api.handlers.upload_handler import upload_router

router_v1 = APIRouter(prefix="/api/v1")

router_v1.include_router(upload_router)


