from typing import Coroutine, Any

from starlette import status
from starlette.types import ASGIApp
from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from upscaler.core.config import settings

class LimitUploadSizeMiddleware(BaseHTTPMiddleware):
    """
    This middleware is still susceptible to attacks that spoof content-length.
    i.e provide a fake content-length header.
    """
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.max_upload_size = settings.FILE_UPLOAD_MAX_SIZE

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.method == 'POST':
            if 'content-length' not in request.headers:
                return Response(status_code=status.HTTP_411_LENGTH_REQUIRED)
            
            content_length = int(request.headers['content-length'])

            if content_length > self.max_upload_size:
                return Response(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
            
        return await call_next(request)
