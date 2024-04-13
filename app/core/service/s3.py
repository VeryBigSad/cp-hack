import logging
from io import BytesIO

import aioboto3
from botocore.exceptions import BotoCoreError
from core.models.models import UploadedImage
from fastapi import UploadFile
from settings import config_parameters

logger = logging.getLogger(__name__)


async def upload_image_to_s3(image: BytesIO, object_name: str) -> str | None:
    session = aioboto3.Session(
        config_parameters.S3_ACCESS_KEY, config_parameters.S3_SECRET_KEY
    )
    async with session.client("s3", endpoint_url=config_parameters.S3_ENDPOINT) as s3:
        try:
            # make file public
            await s3.upload_fileobj(
                image,
                config_parameters.S3_BUCKET_NAME,
                object_name,
                ExtraArgs={"ACL": "public-read"},
            )
        except BotoCoreError as e:
            logger.error(f"Botocore error when uploading: {e}")
            return
        return f"{config_parameters.S3_ENDPOINT}/{config_parameters.S3_BUCKET_NAME}/{object_name}"


async def save_image(image: UploadFile, image_id: int) -> str:
    """Compresses image to webp, saves it to s3, creates image object with said uuid"""
    try:
        image_extension = image.filename.split(".")[-1]
        image_url = await upload_image_to_s3(
            image.file, f"{image_id}.{image_extension}"
        )
    except Exception as e:
        logger.error(f"Error uploading image to S3: {e}")
        return
    if image_url is None:
        logger.error("Image not uploaded to s3")
        return
    try:
        await UploadedImage.create(id=image_id, url=image_url)
    except Exception as e:
        logger.error(f"Error creating UploadedImage object: {e}")
        return None
    return image_url
