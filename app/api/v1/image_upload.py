import logging
import random

from fastapi import APIRouter, UploadFile, status

from core.schemas.image_upload import UploadedImageResponse

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Image upload"])


@router.post(
    "/upload-image",
    response_model=UploadedImageResponse,
    status_code=status.HTTP_200_OK,
)
async def upload_image(image: UploadFile):
    """Uploads a file and returns a file id"""
    return {"image_id": random.randint(50_000_000, 100_000_000), "image_url": "https://goskatalog.ru/muzfo-imaginator/rest/images/original/23423445"}

