import logging

from core.schemas.v1 import CaptionResponse, ClassifyResponse, SimilarImagesResponse
from fastapi import APIRouter, status

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Image endpoints"])


@router.post(
    "/similar-images",
    response_model=SimilarImagesResponse,
    status_code=status.HTTP_200_OK,
)
async def similar_images(
    image_id: int,
):
    """Get a list of all similar images and their probability/id/url"""
    # TODO: unmock
    return {
        "probabilities": [
            {
                "image_id": 6885589,
                "image_url": "https://goskatalog.ru/muzfo-imaginator/rest/images/original/6885589",
                "probability": 0.69,
                "name": "Картина 1",
                "category": "Категория 1",
                "description": "Егор лох",
            },
            {
                "image_id": 23423445,
                "image_url": "https://goskatalog.ru/muzfo-imaginator/rest/images/original/23423445",
                "probability": 0.43,
                "name": "Картина 2",
                "category": "Категория 2",
                "description": "Егор лох 2",
            },
            {
                "image_id": 34343433,
                "image_url": "https://goskatalog.ru/muzfo-imaginator/rest/images/original/34343433",
                "probability": 0.21,
                "name": "Картина 3",
                "category": "Категория 3",
                "description": "Егор лох 3",
            },
        ]
    }


@router.post(
    "/classify-image",
    response_model=ClassifyResponse,
    status_code=status.HTTP_200_OK,
)
async def classify_images(
    image_id: int,
):
    """Classify images, get list of category/category change"""
    return {
        "probabilities": [
            {"category": "Оружие", "probability": 0.43},
            {"category": "Картины", "probability": 0.56},
        ]
    }


@router.post(
    "/generate-image-caption",
    response_model=CaptionResponse,
    status_code=status.HTTP_200_OK,
)
async def generate_image_caption(
    image_id: int,
):
    """Generate image caption. Returns caption text"""
    return {"text": "lolkys"}
