from typing import List

from pydantic import BaseModel, HttpUrl


class CaptionResponse(BaseModel):
    text: str


class CategoryProbabilityModel(BaseModel):
    category: str
    probability: float


class ImageProbabilityModel(BaseModel):
    image_id: int
    image_url: HttpUrl
    probability: float
    name: str
    description: str
    category: str


class ClassifyResponse(BaseModel):
    probabilities: List[CategoryProbabilityModel]


class SimilarImagesResponse(BaseModel):
    probabilities: List[ImageProbabilityModel]
