from fastapi import APIRouter
from fastapi import UploadFile, File

from upscaler.core.config import settings
from upscaler.api.handlers.exceptions import InvalidFileExtensionError


upload_router = APIRouter(tags=["uploads"])


@upload_router.post("/upload")
async def upload(file: UploadFile = File(...)):
    """
    Upload a file to the server for processing with ai.
    """
    
    if file.content_type not in settings.ALLOWED_EXTENSIONS:
        raise InvalidFileExtensionError()
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File uploaded successfully"
    }
    