from fastapi import HTTPException, status


class MaximumUploadSizeExceedError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum file upload size exceeded.",
        )
    
class InvalidFileExtensionError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file extension.",
        )